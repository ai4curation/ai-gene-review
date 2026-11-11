#!/usr/bin/env python3
"""Re-read overruled IBA rows against the PANTHER tree: plan, dossiers, apply.

The reading itself is done by agents, one batch each, from a dossier this script writes:
for every row, the review's verdict and reasons next to what the gene's tree extract
(`GENE-phylo.yaml`) says about the same row. An agent returns, per row, how the tree
bears on the verdict, which sentences of the extract's summary to quote, and one or two
sentences for the reason. This script then makes those edits, and only those:

- quotes are assembled here from the extract's own sentences, never typed by an agent,
  and each is checked to be a verbatim part of the extract;
- edits go through `ai_gene_review.tools.review_row_edit`, which changes the text of one
  row and refuses a result that differs from the original by anything else;
- every edited review is validated, and put back as it was if it no longer validates;
- a history record is scaffolded for every review that changed.

Rows whose reading calls for a judgement the script cannot apply mechanically (a verdict
that the tree does not support, a reading the verifier rejects) are left untouched and
listed for adjudication.

Batches named ``g...`` are gene-review rows. Batches named ``f...`` are family-review
node assessments that dispute a PAINT placement, read against the family's node listing
(`<PTHR>-tree-nodes.yaml`) in the same way.

Usage (from the repository root):
    uv run python projects/IBA_REVIEW/tree-rereview/tree_rereview.py plan [--families]
    uv run python projects/IBA_REVIEW/tree-rereview/tree_rereview.py dossier g001 --out DIR
    uv run python projects/IBA_REVIEW/tree-rereview/tree_rereview.py inputs g001 g002 --out DIR   # dossiers + workflow args
    uv run python projects/IBA_REVIEW/tree-rereview/tree_rereview.py record g001 --analysis A.json [--verification V.json] --date YYYY-MM-DD
    uv run python projects/IBA_REVIEW/tree-rereview/tree_rereview.py apply g001
    uv run python projects/IBA_REVIEW/tree-rereview/tree_rereview.py finish --journal JOURNAL --date YYYY-MM-DD   # record + apply a workflow run
    uv run python projects/IBA_REVIEW/tree-rereview/tree_rereview.py status
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import subprocess
import sys
import textwrap
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable, Iterator

import yaml

from ai_gene_review.etl.gene_phylo import read_iba_rows, read_paint_slice, resolve_seed
from ai_gene_review.etl.panther_release import DEFAULT_DB, PantherRelease
from ai_gene_review.tools.review_row_edit import RowEdit, RowEditError, apply_row_edits, one_paragraph
from ai_gene_review.validation.family_residue_validator import PLACEMENT_DISPUTES, TREE_LISTING_SUFFIXES
from ai_gene_review.validation.tree_evidence import OVERRULING_ACTIONS, phylo_reference_ids

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
PLAN = HERE / "plan.yaml"
FAMILY_PLAN = HERE / "plan-families.yaml"
RUNS = HERE / "runs"
CANDIDATES = HERE.parent / "tree-evidence-candidates.yaml"
Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

#: A batch is what one agent reads in one go: its dossier has to fit in a single file read.
ROWS_PER_BATCH = 24
DOSSIER_WIDTH = 220
SEEDS_SHOWN = 8
#: Readings whose edit is a quote plus a sentence: nothing in the review is contradicted.
ADDITIVE = {"SUPPORTS", "NOT_A_TREE_ARGUMENT", "PAINT_ALREADY_REMOVED"}
READINGS = [*sorted(ADDITIVE), "REASON_CONTRADICTED", "VERDICT_UNSUPPORTED", "LOSS_TOO_BROAD", "LOSS_APPLIES", "CANNOT_TELL"]
CANDIDATE_GROUPS = {
    "paralog_claim_without_duplication": "overruled as a paralog, but the tree shows only ortholog seeds and no duplication on the path",
    "paint_loss_on_path": "PAINT has removed this term on the path to the gene and not asserted it again below",
    "overruled_though_gene_is_a_seed": "the gene's own experimental annotation is among the seeds of this row",
}


def load(path: Path) -> Any:
    """A YAML file's content."""
    return yaml.load(path.read_text(encoding="utf-8"), Loader=Loader)


def mapping(value: Any) -> dict[str, Any]:
    """``value`` when it is a mapping, otherwise an empty one."""
    return value if isinstance(value, dict) else {}


def gene_paths(gene: str) -> tuple[Path, Path, Path]:
    """Review, extract and GOA file of ``org/GENE``."""
    organism, name = gene.split("/")
    folder = ROOT / "genes" / organism / name
    return folder / f"{name}-ai-review.yaml", folder / f"{name}-phylo.yaml", folder / f"{name}-goa.tsv"


def sentences(summary: str) -> list[str]:
    """Split an extract summary so that joining neighbours with a space gives the text back.

    >>> sentences("GO:1 (x): a node. cds1 is 4 steps below it; path length 1.512. Seeds: 2 of 2.")
    ['GO:1 (x): a node.', 'cds1 is 4 steps below it; path length 1.512.', 'Seeds: 2 of 2.']
    """
    parts = summary.strip().split(". ")
    return [part + "." for part in parts[:-1]] + [parts[-1]]


def quotes_from(summary: str, numbers: Iterable[int]) -> list[str]:
    """Verbatim quotes for the chosen sentences (1-based); neighbours are joined.

    The first sentence, which names the term and the node, is always quoted.

    >>> quotes_from("A b. C d. E f. G h.", [4, 2])
    ['A b. C d.', 'G h.']
    """
    parts = sentences(summary)
    chosen = sorted({1, *(n for n in numbers if 1 <= n <= len(parts))})
    groups: list[list[int]] = []
    for number in chosen:
        if groups and number == groups[-1][-1] + 1:
            groups[-1].append(number)
        else:
            groups.append([number])
    return [" ".join(parts[n - 1] for n in group) for group in groups]


def candidate_flags() -> dict[tuple[str, str], list[str]]:
    """``(gene, term)`` of every row on the candidate list, with the groups it is in."""
    flags: dict[tuple[str, str], list[str]] = {}
    doc = load(CANDIDATES)
    for group in CANDIDATE_GROUPS:
        for row in doc[group]["rows"]:
            flags.setdefault((row["gene"], row["term"]), []).append(group)
    return flags


def cites_extract(review: dict[str, Any], own: set[str], term: str) -> bool:
    """True when the row already quotes its own extract, with a quote that names the term."""
    for item in review.get("supported_by") or []:
        if isinstance(item, dict) and str(item.get("reference_id", "")) in own:
            if term in str(item.get("supporting_text", "")):
                return True
    return False


def extract_rows(extract: dict[str, Any]) -> dict[tuple[str, bool], tuple[dict[str, Any], dict[str, Any]]]:
    """``(term, negated)`` of every row of an extract, with its tree section and the row."""
    found: dict[tuple[str, bool], tuple[dict[str, Any], dict[str, Any]]] = {}
    for tree in extract.get("trees") or []:
        for row in tree["rows"]:
            found.setdefault((row["term"]["id"], bool(row["negated"])), (tree, row))
    return found


def target_rows(gene: str, flags: dict[tuple[str, str], list[str]]) -> list[dict[str, Any]]:
    """The rows of one gene still to be read: ``term``, ``negated``, ``kind``, ``action``.

    ``overruled`` rows are IBA rows with an overruling action that are still in the gene's
    GOA file and do not yet quote the extract. ``kept_under_loss`` rows are on the
    candidate list because PAINT has removed the term on the path while the review keeps it.
    """
    review_path, extract_path, goa_path = gene_paths(gene)
    if not (review_path.exists() and extract_path.exists() and goa_path.exists()):
        return []
    review = load(review_path) or {}
    current = {(row.term_id, row.negated) for row in read_iba_rows(goa_path)}
    in_extract = extract_rows(load(extract_path) or {})
    own = phylo_reference_ids(review_path)
    rows: list[dict[str, Any]] = []
    seen: set[tuple[str, bool]] = set()
    for annotation in review.get("existing_annotations") or []:
        if not isinstance(annotation, dict) or annotation.get("evidence_type") != "IBA":
            continue
        body = mapping(annotation.get("review"))
        term = mapping(annotation.get("term")).get("id", "")
        key = (term, bool(annotation.get("negated")))
        if key in seen or key not in current or key not in in_extract:
            continue
        action = body.get("action", "")
        loss = "paint_loss_on_path" in flags.get((gene, term), [])
        if action in OVERRULING_ACTIONS and not cites_extract(body, own, term):
            kind = "overruled"
        elif loss and action not in OVERRULING_ACTIONS and not key[1]:
            kind = "kept_under_loss"
        else:
            continue
        seen.add(key)
        rows.append({"term": term, "negated": key[1], "kind": kind, "action": action})
    return rows


def build_plan() -> dict[str, Any]:
    """Batches of genes: genes with a candidate row first, about ``ROWS_PER_BATCH`` rows each."""
    flags = candidate_flags()
    flagged = {gene for gene, _ in flags}
    genes = sorted(
        str(path.parent.relative_to(ROOT / "genes")) for path in (ROOT / "genes").glob("*/*/*-phylo.yaml")
    )
    work = [(gene, target_rows(gene, flags)) for gene in genes]
    work = [(gene, rows) for gene, rows in work if rows]
    work.sort(key=lambda item: (item[0] not in flagged, item[0]))
    batches: list[dict[str, Any]] = []
    for gene, rows in work:
        if not batches or batches[-1]["rows"] + len(rows) > ROWS_PER_BATCH:
            batches.append({"id": f"g{len(batches) + 1:03d}", "rows": 0, "genes": []})
        batches[-1]["rows"] += len(rows)
        batches[-1]["genes"].append(gene)
    return {
        "generated_by": "projects/IBA_REVIEW/tree-rereview/tree_rereview.py plan",
        "genes": len(work),
        "rows": sum(len(rows) for _, rows in work),
        "rows_overruled": sum(row["kind"] == "overruled" for _, rows in work for row in rows),
        "rows_kept_under_loss": sum(row["kind"] == "kept_under_loss" for _, rows in work for row in rows),
        "batches": batches,
    }


def is_family_batch(batch: str) -> bool:
    """True for a batch of family node assessments (``f...``)."""
    return batch.startswith("f")


def build_family_plan() -> dict[str, Any]:
    """Batches of family reviews whose node assessments dispute a placement without a tree listing."""
    families = sorted(path.parent.name for path in (ROOT / "interpro" / "panther").glob("*/*-review.yaml"))
    work = [(family, family_target_rows(family)) for family in families]
    work = [(family, rows) for family, rows in work if rows]
    batches: list[dict[str, Any]] = []
    for family, rows in work:
        if not batches or batches[-1]["rows"] + len(rows) > ROWS_PER_BATCH:
            batches.append({"id": f"f{len(batches) + 1:03d}", "rows": 0, "families": []})
        batches[-1]["rows"] += len(rows)
        batches[-1]["families"].append(family)
    return {
        "generated_by": "projects/IBA_REVIEW/tree-rereview/tree_rereview.py plan --families",
        "families": len(work),
        "rows": sum(len(rows) for _, rows in work),
        "batches": batches,
    }


def plan_batch(batch: str) -> dict[str, Any]:
    """One batch of the committed plans."""
    path = FAMILY_PLAN if is_family_batch(batch) else PLAN
    for entry in load(path)["batches"]:
        if entry["id"] == batch:
            return entry
    raise SystemExit(f"no batch {batch} in {path.relative_to(ROOT)}")


def batch_rows(batch: str) -> list[dict[str, Any]]:
    """Every row of a batch still to be read, with the gene or family it belongs to."""
    entry = plan_batch(batch)
    if is_family_batch(batch):
        return [{"family": family, **row} for family in entry["families"] for row in family_target_rows(family)]
    flags = candidate_flags()
    rows = []
    for gene in entry["genes"]:
        for row in target_rows(gene, flags):
            marked = flags.get((gene, row["term"]))
            rows.append({"gene": gene, **row, **({"flags": marked} if marked else {})})
    return rows


@lru_cache(maxsize=None)
def family_names(family: str) -> dict[str, str]:
    """Accession to ``GENE (protein name)`` from a family's member table, when there is one."""
    path = ROOT / "interpro" / "panther" / family / f"{family}-entries.csv"
    if not path.exists():
        return {}
    with path.open(encoding="utf-8", newline="") as handle:
        return {
            rec["id"]: " ".join(part for part in (rec.get("gene", ""), f"({rec['name']})" if rec.get("name") else "") if part)
            for rec in csv.DictReader(handle)
        }


def _clip(text: Any, limit: int) -> str:
    flat = one_paragraph(str(text or ""))
    return flat if len(flat) <= limit else flat[: limit - 1] + "…"


def _seed_line(seed: dict[str, Any], names: dict[str, str]) -> str:
    name = names.get(seed.get("accession", ""), "")
    parts = [seed["id"], seed.get("organism", ""), name, seed.get("subfamily", "")]
    relation = seed.get("relation", "not in this tree")
    if relation == "ORTHOLOG":
        relation = "ONE-TO-ONE ORTHOLOG" if not seed.get("duplications_between") else "ORTHOLOG across later duplications"
    parts.append(relation)
    if "mrca" in seed:
        parts.append(f"joins the gene at {seed['mrca']} ({seed.get('mrca_event', '').lower()})")
    if seed.get("duplications_between"):
        parts.append(f"{seed['duplications_between']} duplications between")
    if "identity" in seed:
        parts.append(
            f"identity {round(seed['identity'] * 100)}% over {seed.get('aligned', '?')} columns"
            f" (covers {round(seed.get('covers_target', 0) * 100)}% of the gene, {round(seed.get('covers_seed', 0) * 100)}% of the seed)"
        )
    return "  - " + "; ".join(part for part in parts if part)


def dossier_rows(gene: str, flags: dict[tuple[str, str], list[str]]) -> Iterator[str]:
    """The dossier text of one gene's rows."""
    review_path, extract_path, _ = gene_paths(gene)
    review = load(review_path) or {}
    in_extract = extract_rows(load(extract_path) or {})
    annotations = [a for a in review.get("existing_annotations") or [] if isinstance(a, dict)]
    yield f"## GENE {gene} ({review.get('id', '?')}, {review.get('gene_symbol', '?')})"
    yield f"description: {_clip(review.get('description'), 320)}"
    for target in target_rows(gene, flags):
        term, negated = target["term"], target["negated"]
        annotation = next(
            a for a in annotations
            if a.get("evidence_type") == "IBA" and (a.get("term") or {}).get("id") == term and bool(a.get("negated")) == negated
        )
        body = annotation["review"]
        tree, row = in_extract[(term, negated)]
        node = next(n for n in tree["nodes"] if n["node"] == row["ibd_node"])
        yield ""
        yield f"### ROW {gene} | {term} | {row['term']['label']} | aspect {row['aspect']} | negated: {str(negated).lower()}"
        yield f"kind: {target['kind']}    action: {target['action']}"
        for group in flags.get((gene, term), []):
            yield f"FLAG {group}: {CANDIDATE_GROUPS[group]}"
        yield f"review.summary: {_clip(body.get('summary'), 900)}"
        yield f"review.reason: {_clip(body.get('reason'), 2500) or '(none)'}"
        propagation = mapping(body.get("propagation_review"))
        if propagation:
            sources = "; ".join(
                f"{s.get('source_id')} [{s.get('source_status', '')}] {_clip(s.get('comment'), 200)}"
                for s in propagation.get("source_entities") or [] if isinstance(s, dict)
            )
            yield (
                f"propagation_review: root_cause={propagation.get('root_cause')}; "
                f"failure_modes={propagation.get('failure_modes') or []}; sources: {sources or '(none)'}"
            )
        support = "; ".join(
            f"{item.get('reference_id')} \"{_clip(item.get('supporting_text'), 220)}\""
            for item in body.get("supported_by") or [] if isinstance(item, dict)
        )
        yield f"existing supported_by: {support or '(none)'}"
        same_term = [
            f"{a.get('evidence_type')} {a.get('original_reference_id', '')} -> {(a.get('review') or {}).get('action')}"
            for a in annotations
            if a is not annotation and (a.get("term") or {}).get("id") == term and bool(a.get("negated")) == negated
        ]
        yield f"other rows of this review on the same term: {'; '.join(same_term) or '(none)'}"
        place = node.get("taxon") or " / ".join(
            part for part in (
                f"after {node['after']}" if node.get("after") else "",
                f"before {', '.join(node['before'])}" if node.get("before") else "",
            ) if part
        )
        target_leaf = tree["target"]
        facts = [
            f"family {tree['family']} ({tree.get('family_name', '')})",
            f"PAINT node {row['ibd_node']}: {node['event']} {place}; {'the family root; ' if node.get('is_root') else ''}"
            f"{node['leaves']} leaves, {node['species']} species, {node['subfamilies']} subfamilies",
            f"gene leaf {target_leaf['leaf']} in {target_leaf.get('subfamily', '?')} ({target_leaf.get('subfamily_name', '')})",
        ]
        for key in (
            "steps", "duplications_on_path", "transfers_on_path", "seeds_resolved", "seeds_unresolved",
            "seed_branches", "node_branches", "seed_mrca", "seed_mrca_steps_below_node", "target_in_seed_clade",
            "self_seed", "seeds_on_target_branch", "orthologs", "one_to_one_orthologs", "paralogs", "xenologs",
        ):
            if key in row:
                facts.append(f"{key}={row[key]}")
        losses = row.get("paint_losses_on_path") or []
        facts.append(
            "paint_losses_on_path=" + (
                "; ".join(
                    f"{loss['evidence']} at {loss['node']} ({loss['date']})"
                    + (f", re-asserted below at {loss['reasserted_below']}" if loss.get("reasserted_below") else ", NOT re-asserted below")
                    for loss in losses
                ) or "none"
            )
        )
        yield "tree facts: " + " | ".join(facts)
        names = family_names(tree["family"])
        seeds = {seed["id"]: seed for seed in tree["seeds"]}
        listed = sorted(
            (seeds[token] for token in row["seeds"] if token in seeds),
            key=lambda seed: (seed.get("relation") != "SELF", seed.get("tree_distance", 99.0)),
        )
        relations = Counter(seed.get("relation", "not in this tree") for seed in listed)
        counted = ", ".join(f"{count} {name.lower()}" for name, count in relations.most_common())
        shown = f"; the {SEEDS_SHOWN} nearest shown" if len(listed) > SEEDS_SHOWN else ""
        yield f"seeds of this row ({len(row['seeds'])}: {counted}{shown}):"
        for seed in listed[:SEEDS_SHOWN]:
            yield _seed_line(seed, names)
        yield "extract summary, by sentence (quote by number):"
        for number, sentence in enumerate(sentences(row["summary"]), 1):
            yield f"  [{number}] {sentence}"


def write_dossier(batch: str, out: Path) -> Path:
    """Write the dossier of one batch and return its path."""
    entry = plan_batch(batch)
    if is_family_batch(batch):
        lines = [f"# Tree re-read dossier, batch {batch}: {len(entry['families'])} family reviews", ""]
        for family in entry["families"]:
            lines.extend(family_dossier_rows(family))
            lines.append("")
    else:
        flags = candidate_flags()
        lines = [f"# Tree re-read dossier, batch {batch}: {len(entry['genes'])} genes", ""]
        for gene in entry["genes"]:
            lines.extend(dossier_rows(gene, flags))
            lines.append("")
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{batch}.md"
    wrapped = [
        textwrap.fill(line, width=DOSSIER_WIDTH, subsequent_indent="      ", break_long_words=False, break_on_hyphens=False)
        if len(line) > DOSSIER_WIDTH else line
        for line in lines
    ]
    path.write_text("\n".join(wrapped), encoding="utf-8")
    return path


def workflow_inputs(batches: list[str], out: Path) -> list[dict[str, Any]]:
    """Write the dossiers of some batches and describe them for the reading workflow.

    ``flagged`` lists the rows a verifier must always check: rows on the candidate list
    and kept rows under a PAINT loss, as ``gene|term|negated``.
    """
    inputs = []
    for batch in batches:
        entry = plan_batch(batch)
        rows = batch_rows(batch)
        inputs.append({
            "id": batch,
            "dossier": str(write_dossier(batch, out)),
            "units": len(entry["families" if is_family_batch(batch) else "genes"]),
            "rows": len(rows),
            "flagged": [
                "|".join(str(part).lower() if isinstance(part, bool) else str(part) for part in _key(row))
                for row in rows
                if row["kind"] != "overruled" or row.get("flags")
            ],
        })
    return inputs


def family_paths(family: str) -> tuple[Path, Path, Path]:
    """Review, node listing and PAINT slice of a family."""
    folder = ROOT / "interpro" / "panther" / family
    return folder / f"{family}-review.yaml", folder / f"{family}-tree-nodes.yaml", folder / f"{family}-paint.tsv"


def family_target_rows(family: str) -> list[dict[str, Any]]:
    """Node assessments of one family review that dispute a placement without citing a tree listing."""
    review_path, listing_path, _ = family_paths(family)
    if not (review_path.exists() and listing_path.exists()):
        return []
    rows: list[dict[str, Any]] = []
    seen: set[tuple[str, str, bool]] = set()
    for assessment in (load(review_path) or {}).get("node_assessments") or []:
        if not isinstance(assessment, dict) or assessment.get("assessment") not in PLACEMENT_DISPUTES:
            continue
        cited = any(
            isinstance(item, dict) and str(item.get("reference_id", "")).endswith(TREE_LISTING_SUFFIXES)
            for item in assessment.get("supported_by") or []
        )
        key = (
            str(assessment.get("node_id", "")),
            mapping(assessment.get("asserted_term")).get("id", ""),
            bool(assessment.get("negated")),
        )
        if cited or key in seen:
            continue
        seen.add(key)
        rows.append({"node": key[0], "term": key[1], "negated": key[2], "kind": "node", "action": assessment["assessment"]})
    return rows


def listing_assertion(listing: dict[str, Any], node: str, term: str, negated: bool) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    """The listing's node entry and its assertion for a term; either may be missing."""
    entry = next((n for n in listing.get("nodes") or [] if n["node"] == node.removeprefix("PANTHER:")), None)
    if entry is None:
        return None, None
    found = next(
        (a for a in entry.get("assertions") or [] if a["term"] == term and bool(a.get("negated")) == negated),
        None,
    )
    return entry, found


@lru_cache(maxsize=1)
def release() -> PantherRelease | None:
    """The local PANTHER release database, when it has been fetched."""
    path = ROOT / DEFAULT_DB
    return PantherRelease(path) if path.exists() else None


def tree_context(family: str, node: str, term: str, negated: bool, affected: list[str]) -> list[str]:
    """Facts read off the release tree that the listing does not carry.

    For each seed of the assertion, its organism and subfamily; for each subfamily the
    review names as affected, how many of its leaves lie below the node and how many of
    the seeds are in it.
    """
    database = release()
    tree = database.tree(family) if database else None
    an = tree.an_of.get(node.removeprefix("PANTHER:")) if tree else None
    if database is None or tree is None or an is None:
        return []
    subfamily = {row[0]: row[1] for row in database._con.execute("SELECT an, subfamily FROM node WHERE family = ?", (family,))}
    below = tree.leaves_below(an)
    slice_rows = read_paint_slice(family_paths(family)[2]) or []
    tokens = [
        token
        for rec in slice_rows
        if rec["node"] == node.removeprefix("PANTHER:") and rec["go_id"] == term and (rec["negated"] == "true") == negated
        for token in rec["seeds"].split("|")
        if token and not token.startswith("PANTHER:")
    ]
    names = family_names(family)
    lines: list[str] = []
    seed_subfamilies: Counter[str] = Counter()
    for token in tokens[:20]:
        leaf, _ = resolve_seed(token, tree, database)
        if leaf is None:
            lines.append(f"  - seed {token}: not a leaf of this tree")
            continue
        long_id = tree.nodes[leaf].long_id
        accession = long_id.rsplit("UniProtKB=", 1)[-1]
        seed_subfamilies[subfamily.get(leaf, "?")] += 1
        lines.append(
            f"  - seed {token}: {long_id.split('|')[0]} {names.get(accession, '')} in {subfamily.get(leaf, '?')}; "
            f"{tree.depth(leaf) - tree.depth(an)} steps below the node" + ("" if tree.is_ancestor(an, leaf) else " (NOT below this node)")
        )
    for name in affected:
        short = name.removeprefix("PANTHER:")
        count = sum(subfamily.get(leaf) == short for leaf in below)
        lines.append(f"  - affected subfamily {short}: {count} of the node's {len(below)} leaves; {seed_subfamilies.get(short, 0)} of its seeds")
    return lines


def family_dossier_rows(family: str) -> Iterator[str]:
    """The dossier text of one family's disputed node assessments."""
    review_path, listing_path, _ = family_paths(family)
    review = load(review_path) or {}
    listing = load(listing_path) or {}
    yield f"## FAMILY {family} ({listing.get('family_name', '')}); tree of {listing.get('tree_leaves')} leaves in {listing.get('tree_species')} species"
    yield f"family summary: {_clip(review.get('summary'), 500)}"
    assessments = [a for a in review.get("node_assessments") or [] if isinstance(a, dict)]
    for target in family_target_rows(family):
        node, term, negated = target["node"], target["term"], target["negated"]
        assessment = next(
            a for a in assessments
            if a.get("node_id") == node and mapping(a.get("asserted_term")).get("id") == term and bool(a.get("negated")) == negated
        )
        entry, found = listing_assertion(listing, node, term, negated)
        yield ""
        yield f"### ROW {family} | {node} | {term} | {mapping(assessment.get('asserted_term')).get('label', '')} | negated: {str(negated).lower()}"
        yield f"kind: node    assessment: {target['action']}    PAINT evidence: {assessment.get('evidence', '?')}"
        yield f"assessment_reason: {_clip(assessment.get('assessment_reason'), 2500) or '(none)'}"
        affected = [str(s.get("id", "")) for s in assessment.get("affected_subfamilies") or [] if isinstance(s, dict)]
        if affected:
            yield "affected_subfamilies (review): " + "; ".join(
                f"{s.get('id', '').removeprefix('PANTHER:')} ({s.get('label', '')})" for s in assessment["affected_subfamilies"] if isinstance(s, dict)
            )
        yield "seeds (review): " + ("; ".join(str(s.get("id")) for s in assessment.get("seeds") or [] if isinstance(s, dict)) or "(none)")
        support = "; ".join(
            f"{item.get('reference_id')} \"{_clip(item.get('supporting_text'), 200)}\""
            for item in assessment.get("supported_by") or [] if isinstance(item, dict)
        )
        yield f"existing supported_by: {support or '(none)'}"
        other = [
            f"{mapping(a.get('asserted_term')).get('id')}{' NOT' if a.get('negated') else ''} -> {a.get('assessment')}"
            for a in assessments if a is not assessment and a.get("node_id") == node
        ]
        yield f"other assessments of this node in the review: {'; '.join(other) or '(none)'}"
        if entry is None:
            yield "LISTING: the tree listing has no entry for this node (it is not a node of this family's PANTHER 19.0 tree, or not in the family's PAINT slice)"
            continue
        place = entry.get("taxon") or " / ".join(
            part for part in (
                f"after {entry['after']}" if entry.get("after") else "",
                f"before {', '.join(entry['before'])}" if entry.get("before") else "",
            ) if part
        )
        yield (
            f"node (listing): {entry['event']} {place}; {'the family root; ' if entry.get('is_root') else ''}depth {entry.get('depth')}; "
            f"{entry['leaves']} leaves, {entry['species']} species, {entry['subfamilies']} subfamilies; largest subfamilies: "
            + ", ".join(f"{s['id'].split(':')[-1]} {s.get('name', '')} ({s['leaves']})" for s in entry.get("top_subfamilies") or [])
        )
        yield "branches below the node (listing): " + "; ".join(
            f"{b['node']} {b.get('event', '').lower()} {b.get('taxon') or ''} ({b['leaves']} leaves, {b.get('species', '?')} species)"
            for b in entry.get("branches") or []
        )
        yield "other terms PAINT places on this node (listing): " + (
            "; ".join(
                f"{a['term']}{' NOT' if a.get('negated') else ''} {a.get('evidence')}"
                for a in entry.get("assertions") or [] if a is not found
            ) or "(none)"
        )
        context = tree_context(family, node, term, negated, affected)
        if context:
            yield "from the PANTHER 19.0 tree (not in the listing):"
            yield from context
        if found is None:
            yield "LISTING: the tree listing has no assertion of this term on this node"
            continue
        facts = [f"{key}={found[key]}" for key in (
            "seeds", "seeds_resolved", "seed_branches", "node_branches", "seed_mrca", "seed_mrca_steps_below_node", "blocks", "date",
        ) if key in found]
        yield "assertion (listing): " + " | ".join(facts)
        yield "listing summary, by sentence (quote by number):"
        for number, sentence in enumerate(sentences(found["summary"]), 1):
            yield f"  [{number}] {sentence}"


def _key(row: dict[str, Any]) -> tuple[Any, ...]:
    """What identifies a row: gene, term and negation, or family, node, term and negation."""
    if row.get("family"):
        return row["family"], row["node"], row["term"], bool(row.get("negated"))
    return row["gene"], row["term"], bool(row.get("negated"))


def make_record(batch: str, analysis: dict[str, Any], verification: dict[str, Any] | None, date: str) -> dict[str, Any]:
    """Join the plan's rows with the analysts' readings and the verifier's checks."""
    read = {_key(row): row for row in analysis.get("rows") or []}
    checked = {_key(row): row for row in (verification or {}).get("rows") or []}
    rows: list[dict[str, Any]] = []
    for row in batch_rows(batch):
        key = _key(row)
        reading = read.get(key)
        if reading is None:
            row["outcome"] = "not_read"
        else:
            for field in (
                "tree_reading", "quote_sentences", "tree_sentence", "false_claims", "reason_replacement",
                "proposed_action", "failure_modes_add", "failure_modes_remove", "note",
            ):
                if reading.get(field) not in (None, "", []):
                    row[field] = reading[field]
            if key in checked:
                fixed = mapping(checked[key].get("fixed"))
                row["verifier"] = {
                    "agrees": bool(checked[key].get("agrees")),
                    **({"problem": checked[key]["problem"]} if checked[key].get("problem") else {}),
                    **({"fixed": fixed} if one_paragraph(str(fixed.get("tree_sentence", ""))) else {}),
                }
            row["outcome"] = "pending"
        rows.append(row)
    return {"batch": batch, "read_on": date, "rows": rows}


def run_path(batch: str) -> Path:
    """Where the record of one batch lives."""
    return RUNS / f"{batch}.yaml"


def dump(data: Any) -> str:
    """YAML for a run record or the plan."""
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=110)


def quote_source(row: dict[str, Any]) -> tuple[str, str, str] | None:
    """The summary a row quotes from, the text of the file it is in, and that file's reference id."""
    if row.get("family"):
        family = row["family"]
        listing_path = family_paths(family)[1]
        found = listing_assertion(load(listing_path) or {}, row["node"], row["term"], row["negated"])[1]
        if found is None:
            return None
        return found["summary"], listing_path.read_text(encoding="utf-8"), f"file:interpro/panther/{family}/{family}-tree-nodes.yaml"
    extract_path = gene_paths(row["gene"])[1]
    in_extract = extract_rows(load(extract_path)).get((row["term"], row["negated"]))
    if in_extract is None:
        return None
    organism, name = row["gene"].split("/")
    return in_extract[1]["summary"], extract_path.read_text(encoding="utf-8"), f"file:{organism}/{name}/{name}-phylo.yaml"


def row_edit(row: dict[str, Any]) -> RowEdit | str:
    """The edit a reading calls for, or the reason it is left for adjudication.

    Where the verifier faults a reading but gives a corrected one that only quotes the row
    and adds a sentence, the corrected reading is used.
    """
    verifier = row.get("verifier")
    if verifier is not None and not verifier["agrees"]:
        fixed = mapping(verifier.get("fixed"))
        if fixed.get("tree_reading") not in ADDITIVE:
            return "the verifier disagrees with the reading"
        row = {**row, "tree_reading": fixed["tree_reading"], "tree_sentence": fixed.get("tree_sentence", ""),
               "quote_sentences": fixed.get("quote_sentences") or row.get("quote_sentences") or [],
               "proposed_action": "", "reason_replacement": ""}
    reading = row.get("tree_reading", "")
    if row["kind"] == "kept_under_loss":
        return "a kept row under a PAINT loss needs a decision on the loss, not a quote"
    if verifier is None and (row.get("flags") or row["kind"] == "node"):
        return "a row that must be verified was not checked by the verifier"
    if reading not in ADDITIVE and reading != "REASON_CONTRADICTED":
        return f"reading {reading or '(none)'} calls for a judgement the script does not apply"
    if reading == "REASON_CONTRADICTED" and verifier is None:
        return "a reason correction was not checked by the verifier"
    if row.get("proposed_action"):
        return "a change of verdict is proposed"
    sentence = one_paragraph(row.get("tree_sentence", ""))
    if len(sentence) < 40:
        return "no sentence on what the tree shows"
    source = quote_source(row)
    if source is None:
        return "the tree file has no entry for this row"
    summary, source_text, reference = source
    quotes = quotes_from(summary, row.get("quote_sentences") or [])
    if not quotes or row["term"] not in quotes[0] or any(quote not in source_text for quote in quotes):
        return "the quotes are not verbatim parts of the tree file"
    replacement = one_paragraph(row.get("reason_replacement", "")) if reading == "REASON_CONTRADICTED" else ""
    if reading == "REASON_CONTRADICTED" and len(replacement) < 80:
        return "a reason correction without a replacement reason"
    return RowEdit(
        row["term"],
        negated=row["negated"],
        node_id=row.get("node", ""),
        add_support=tuple((reference, quote) for quote in quotes),
        append_reason="" if replacement else sentence,
        replace_reason=replacement or None,
        add_failure_modes=tuple(row.get("failure_modes_add") or []) if replacement else (),
        remove_failure_modes=tuple(row.get("failure_modes_remove") or []) if replacement else (),
    )


def _run(*command: str) -> tuple[int, str]:
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
    return result.returncode, result.stdout + result.stderr


def validate(review_path: Path) -> tuple[bool, str]:
    """Validate one edited review: ``(valid, the validators' output)``.

    A gene review goes through the gene-review validator. A family review goes through
    the schema, the quote check and the residue and node checks, as `just
    validate-families` runs them.
    """
    relative = str(review_path.relative_to(ROOT))
    if relative.startswith("genes/"):
        code, output = _run(sys.executable, "-m", "ai_gene_review.cli", "validate", relative)
        return code == 0 and "✓ Valid" in output, output
    linkml = str(Path(sys.executable).with_name("linkml-validate"))
    steps = [
        (linkml, "--schema", "src/ai_gene_review/schema/family_review.yaml", "--target-class", "FamilyReview", relative),
        (sys.executable, "-m", "ai_gene_review.validation.quote_check", relative),
        (sys.executable, "-m", "ai_gene_review.validation.family_residue_validator", relative),
    ]
    outputs = []
    for step in steps:
        code, output = _run(*step)
        outputs.append(output)
        if code != 0:
            return False, "ERROR in " + " ".join(step[1:4]) + "\n" + output
    return True, "\n".join(outputs)


def unit_of(row: dict[str, Any]) -> str:
    """The gene (``org/GENE``) or family a row belongs to."""
    return row.get("family") or row["gene"]


def review_path_of(unit: str) -> Path:
    """The review file of a gene or a family."""
    return gene_paths(unit)[0] if "/" in unit else family_paths(unit)[0]


def _new_history() -> Any:
    """The history scaffolder's module (a script, so it is loaded by path)."""
    spec = importlib.util.spec_from_file_location("new_history", ROOT / "scripts" / "new_history.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def history_details(unit: str, rows: list[dict[str, Any]]) -> str:
    """What was done to one review, for its history record."""
    if "/" in unit:
        organism, name = unit.split("/")
        lines = [
            f"Re-read of the overruled IBA rows against the PANTHER 19.0 tree and family alignment "
            f"({name}-phylo.yaml, from `just phylo {organism} {name}`). An agent read each row's verdict "
            "and reasons next to the extract's facts for the same row; a second agent checked every "
            "correction and a sample of the rest. Verdicts are unchanged.",
            "",
        ]
        source = "its own extract"
    else:
        lines = [
            f"Re-read of the node assessments that dispute a PAINT placement against the PANTHER 19.0 "
            f"tree ({unit}-tree-nodes.yaml, from `just phylo-family {unit}`). An agent read each "
            "assessment next to the listing's facts for the same node and term; a second agent "
            "checked each reading. Assessments are unchanged.",
            "",
        ]
        source = "the family's node listing"
    for row in rows:
        if row.get("outcome_detail") == "applied as corrected by the verifier":
            row = {**row, **row["verifier"]["fixed"]}
        what = {
            "SUPPORTS": "the tree agrees with the stated reason",
            "NOT_A_TREE_ARGUMENT": "the verdict rests on evidence the tree does not speak to, and the tree contradicts nothing stated",
            "PAINT_ALREADY_REMOVED": "PAINT has itself removed the term on the path to the gene",
            "REASON_CONTRADICTED": "the reason made a claim the tree contradicts; the reason was corrected",
        }[row["tree_reading"]]
        where = f"{row['node']} " if row.get("node") else ""
        lines.append(f"- {where}{row['term']} ({row['action']}): {what}. Added to the reason: {one_paragraph(row.get('tree_sentence', ''))}")
    lines += [
        "",
        f"Each row now quotes {source} in supported_by; the quotes were assembled from the "
        "file's sentences by projects/IBA_REVIEW/tree-rereview/tree_rereview.py and checked "
        "verbatim. The review validates after the edit.",
    ]
    return "\n".join(lines)


def history_arguments(unit: str, applied: list[dict[str, Any]], pr: str = "") -> list[str]:
    """Arguments for the history scaffolder for one changed review."""
    count = f"{len(applied)} {'row' if len(applied) == 1 else 'rows'}"
    if "/" in unit:
        organism, name = unit.split("/")
        target = ["--kind", "gene", "--organism", organism, "--slug", name, "--sections", "existing_annotations"]
        summary = f"Re-read {count} of overruled IBA annotation against the PANTHER tree; extract quoted"
    else:
        target = [
            "--kind", "other", "--slug", unit, "--path", f"interpro/panther/{unit}/{unit}-review.yaml",
            "--sections", "node_assessments",
        ]
        summary = f"Re-read {count} of disputed node placement against the PANTHER tree; node listing quoted"
    return [
        *target, "--event", "REVIEW", "--outcome", "changed", "--agent-tool", "claude-code",
        *(["--pr", pr] if pr else []),
        "--summary", summary, "--details", history_details(unit, applied),
    ]


def apply_batch(batch: str, jobs: int = 4, pr: str = "") -> Counter[str]:
    """Make the edits of one batch record, validate, write history, update the record."""
    path = run_path(batch)
    record = load(path)
    by_gene: dict[str, list[dict[str, Any]]] = {}
    for row in record["rows"]:
        if row.get("outcome") == "pending":
            by_gene.setdefault(unit_of(row), []).append(row)
    originals: dict[str, str] = {}
    for gene, rows in by_gene.items():
        review_path = review_path_of(gene)
        text = originals[gene] = review_path.read_text(encoding="utf-8")
        for row in rows:
            edit = row_edit(row)
            if isinstance(edit, str):
                row["outcome"], row["outcome_detail"] = "adjudicate", edit
                continue
            try:
                text = apply_row_edits(text, [edit])
            except RowEditError as error:
                row["outcome"], row["outcome_detail"] = "adjudicate", f"edit refused: {error}"
                continue
            row["outcome"] = "applied"
            if row.get("verifier") and not row["verifier"]["agrees"]:
                row["outcome_detail"] = "applied as corrected by the verifier"
        if text != originals[gene]:
            review_path.write_text(text, encoding="utf-8")
    changed = [gene for gene, rows in by_gene.items() if any(row["outcome"] == "applied" for row in rows)]
    with ThreadPoolExecutor(max_workers=jobs) as pool:
        results = dict(zip(changed, pool.map(lambda gene: validate(review_path_of(gene)), changed)))
    scaffolder = _new_history()
    for gene in changed:
        valid, output = results[gene]
        applied = [row for row in by_gene[gene] if row["outcome"] == "applied"]
        if not valid:
            review_path_of(gene).write_text(originals[gene], encoding="utf-8")
            first_error = next((line.strip() for line in output.splitlines() if "ERROR" in line or "✗" in line), "no longer validates")
            for row in applied:
                row["outcome"], row["outcome_detail"] = "adjudicate", f"edit undone, the review no longer validated: {first_error[:300]}"
            continue
        scaffolder.main(history_arguments(gene, applied, pr))
    path.write_text(dump(record), encoding="utf-8")
    return Counter(row["outcome"] for row in record["rows"])


def collect(journal: Path) -> dict[str, dict[str, Any]]:
    """The results of a reading workflow, by batch: ``{"g001": {"analysis": ..., "verification": ...}}``.

    The workflow journal has a ``started`` line per agent, labelled ``read:<batch>`` or
    ``verify:<batch>``, and a ``result`` line with what the agent returned.
    """
    labels: dict[str, str] = {}
    results: dict[str, dict[str, Any]] = {}
    for line in journal.read_text(encoding="utf-8").splitlines():
        rec = json.loads(line)
        if rec.get("type") == "started":
            labels[rec["agentId"]] = rec.get("label", "")
        elif rec.get("type") == "result" and isinstance(rec.get("result"), dict):
            stage, _, batch = labels.get(rec.get("agentId"), "").partition(":")
            if stage in ("read", "verify") and batch:
                results.setdefault(batch, {})["analysis" if stage == "read" else "verification"] = rec["result"]
    return results


def finish(journal: Path, date: str, jobs: int = 4, pr: str = "") -> list[str]:
    """Record and apply every batch of a finished workflow run; returns one line per batch."""
    RUNS.mkdir(exist_ok=True)
    lines = []
    for batch, results in sorted(collect(journal).items()):
        if run_path(batch).exists():
            lines.append(f"{batch}: already recorded, left alone")
            continue
        if "analysis" not in results or "verification" not in results:
            lines.append(f"{batch}: {'no reading' if 'analysis' not in results else 'no verification'} returned; nothing recorded")
            continue
        record = make_record(batch, results["analysis"], results["verification"], date)
        run_path(batch).write_text(dump(record), encoding="utf-8")
        readings = Counter(row.get("tree_reading", "(not read)") for row in record["rows"])
        checked = [row["verifier"]["agrees"] for row in record["rows"] if "verifier" in row]
        outcomes = apply_batch(batch, jobs, pr)
        lines.append(
            f"{batch}: {len(record['rows'])} rows; readings {dict(readings)}; verifier checked {len(checked)}, "
            f"disagreed on {checked.count(False)}; outcomes {dict(outcomes)}"
        )
    return lines


def status() -> str:
    """Progress over the committed plan and run records."""
    lines = []
    for path, units in ((PLAN, "genes"), (FAMILY_PLAN, "families")):
        if not path.exists():
            continue
        plan = load(path)
        outcomes: Counter[str] = Counter()
        readings: Counter[str] = Counter()
        done = 0
        for entry in plan["batches"]:
            run = run_path(entry["id"])
            if not run.exists():
                continue
            done += 1
            for row in load(run)["rows"]:
                outcomes[row.get("outcome", "?")] += 1
                readings[row.get("tree_reading", "(not read)")] += 1
        lines += [
            f"{path.name}: {plan['rows']} rows in {plan[units]} {units}, {len(plan['batches'])} batches; {done} recorded",
            "  outcomes: " + ", ".join(f"{name} {count}" for name, count in outcomes.most_common()),
            "  readings: " + ", ".join(f"{name} {count}" for name, count in readings.most_common()),
        ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").split("\n")[0])
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("plan").add_argument("--families", action="store_true")
    dossier = commands.add_parser("dossier")
    dossier.add_argument("batch")
    dossier.add_argument("--out", type=Path, required=True)
    inputs = commands.add_parser("inputs")
    inputs.add_argument("batches", nargs="+")
    inputs.add_argument("--out", type=Path, required=True)
    record = commands.add_parser("record")
    record.add_argument("batch")
    record.add_argument("--analysis", type=Path, required=True)
    record.add_argument("--verification", type=Path)
    record.add_argument("--date", required=True)
    apply = commands.add_parser("apply")
    apply.add_argument("batch")
    apply.add_argument("--jobs", type=int, default=4)
    apply.add_argument("--pr", default="", help="pull request number or URL for the history records")
    done = commands.add_parser("finish")
    done.add_argument("--journal", type=Path, required=True)
    done.add_argument("--date", required=True)
    done.add_argument("--jobs", type=int, default=4)
    done.add_argument("--pr", default="", help="pull request number or URL for the history records")
    commands.add_parser("status")
    args = parser.parse_args(argv)

    if args.command == "plan":
        path = FAMILY_PLAN if args.families else PLAN
        if path.exists():
            raise SystemExit(f"{path.relative_to(ROOT)} exists; a plan is made once and then kept")
        plan = build_family_plan() if args.families else build_plan()
        path.write_text(dump(plan), encoding="utf-8")
        print(f"{plan['rows']} rows, {len(plan['batches'])} batches")
    elif args.command == "dossier":
        print(write_dossier(args.batch, args.out))
    elif args.command == "inputs":
        print(json.dumps(workflow_inputs(args.batches, args.out)))
    elif args.command == "record":
        RUNS.mkdir(exist_ok=True)
        verification = json.loads(args.verification.read_text(encoding="utf-8")) if args.verification else None
        made = make_record(args.batch, json.loads(args.analysis.read_text(encoding="utf-8")), verification, args.date)
        run_path(args.batch).write_text(dump(made), encoding="utf-8")
        print(Counter(row.get("tree_reading", row["outcome"]) for row in made["rows"]))
    elif args.command == "apply":
        print(dict(apply_batch(args.batch, args.jobs, args.pr)))
    elif args.command == "finish":
        print("\n".join(finish(args.journal, args.date, args.jobs, args.pr)))
    else:
        print(status())
    return 0


if __name__ == "__main__":
    sys.exit(main())
