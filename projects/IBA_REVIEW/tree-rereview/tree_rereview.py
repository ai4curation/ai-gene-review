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

Usage (from the repository root):
    uv run python projects/IBA_REVIEW/tree-rereview/tree_rereview.py plan
    uv run python projects/IBA_REVIEW/tree-rereview/tree_rereview.py dossier g001 --out DIR
    uv run python projects/IBA_REVIEW/tree-rereview/tree_rereview.py inputs g001 g002 --out DIR   # dossiers + workflow args
    uv run python projects/IBA_REVIEW/tree-rereview/tree_rereview.py record g001 --analysis A.json [--verification V.json] --date YYYY-MM-DD
    uv run python projects/IBA_REVIEW/tree-rereview/tree_rereview.py apply g001
    uv run python projects/IBA_REVIEW/tree-rereview/tree_rereview.py status
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import subprocess
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable, Iterator

import yaml

from ai_gene_review.etl.gene_phylo import read_iba_rows
from ai_gene_review.tools.review_row_edit import RowEdit, RowEditError, apply_row_edits, one_paragraph
from ai_gene_review.validation.tree_evidence import OVERRULING_ACTIONS, phylo_reference_ids

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
PLAN = HERE / "plan.yaml"
RUNS = HERE / "runs"
CANDIDATES = HERE.parent / "tree-evidence-candidates.yaml"
Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

ROWS_PER_BATCH = 45
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


def plan_batch(batch: str) -> dict[str, Any]:
    """One batch of the committed plan."""
    for entry in load(PLAN)["batches"]:
        if entry["id"] == batch:
            return entry
    raise SystemExit(f"no batch {batch} in {PLAN.relative_to(ROOT)}")


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
    yield f"description: {_clip(review.get('description'), 500)}"
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
        yield f"seeds of this row ({len(row['seeds'])}; nearest first{', first 15 shown' if len(listed) > 15 else ''}):"
        for seed in listed[:15]:
            yield _seed_line(seed, names)
        yield "extract summary, by sentence (quote by number):"
        for number, sentence in enumerate(sentences(row["summary"]), 1):
            yield f"  [{number}] {sentence}"


def write_dossier(batch: str, out: Path) -> Path:
    """Write the dossier of one batch and return its path."""
    entry = plan_batch(batch)
    flags = candidate_flags()
    lines = [f"# Tree re-read dossier, batch {batch}: {len(entry['genes'])} genes", ""]
    for gene in entry["genes"]:
        lines.extend(dossier_rows(gene, flags))
        lines.append("")
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{batch}.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def workflow_inputs(batches: list[str], out: Path) -> list[dict[str, Any]]:
    """Write the dossiers of some batches and describe them for the reading workflow.

    ``flagged`` lists the rows a verifier must always check: rows on the candidate list
    and kept rows under a PAINT loss, as ``gene|term|negated``.
    """
    flags = candidate_flags()
    inputs = []
    for batch in batches:
        entry = plan_batch(batch)
        rows = [(gene, row) for gene in entry["genes"] for row in target_rows(gene, flags)]
        inputs.append({
            "id": batch,
            "dossier": str(write_dossier(batch, out)),
            "genes": len(entry["genes"]),
            "rows": len(rows),
            "flagged": [
                f"{gene}|{row['term']}|{str(row['negated']).lower()}"
                for gene, row in rows
                if row["kind"] != "overruled" or flags.get((gene, row["term"]))
            ],
        })
    return inputs


def _key(row: dict[str, Any]) -> tuple[str, str, bool]:
    return row["gene"], row["term"], bool(row.get("negated"))


def make_record(batch: str, analysis: dict[str, Any], verification: dict[str, Any] | None, date: str) -> dict[str, Any]:
    """Join the plan's rows with the analysts' readings and the verifier's checks."""
    entry = plan_batch(batch)
    flags = candidate_flags()
    read = {_key(row): row for row in analysis.get("rows") or []}
    checked = {_key(row): row for row in (verification or {}).get("rows") or []}
    rows: list[dict[str, Any]] = []
    for gene in entry["genes"]:
        for target in target_rows(gene, flags):
            key = (gene, target["term"], target["negated"])
            row: dict[str, Any] = {"gene": gene, **target}
            if flags.get((gene, target["term"])):
                row["flags"] = flags[(gene, target["term"])]
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
                    row["verifier"] = {
                        "agrees": bool(checked[key].get("agrees")),
                        **({"problem": checked[key]["problem"]} if checked[key].get("problem") else {}),
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


def row_edit(row: dict[str, Any]) -> RowEdit | str:
    """The edit a reading calls for, or the reason it is left for adjudication."""
    reading = row.get("tree_reading", "")
    verifier = row.get("verifier")
    if verifier is not None and not verifier["agrees"]:
        return "the verifier disagrees with the reading"
    if row["kind"] != "overruled":
        return "a kept row under a PAINT loss needs a decision on the loss, not a quote"
    if reading not in ADDITIVE and reading != "REASON_CONTRADICTED":
        return f"reading {reading or '(none)'} calls for a judgement the script does not apply"
    if reading == "REASON_CONTRADICTED" and verifier is None:
        return "a reason correction was not checked by the verifier"
    if row.get("proposed_action"):
        return "a change of verdict is proposed"
    sentence = one_paragraph(row.get("tree_sentence", ""))
    if len(sentence) < 40:
        return "no sentence on what the tree shows"
    _, extract_path, _ = gene_paths(row["gene"])
    extract_text = extract_path.read_text(encoding="utf-8")
    found = extract_rows(load(extract_path)).get((row["term"], row["negated"]))
    if found is None:
        return "the extract has no row for this term"
    quotes = quotes_from(found[1]["summary"], row.get("quote_sentences") or [])
    if not quotes or row["term"] not in quotes[0] or any(quote not in extract_text for quote in quotes):
        return "the quotes are not verbatim parts of the extract"
    organism, name = row["gene"].split("/")
    reference = f"file:{organism}/{name}/{name}-phylo.yaml"
    replacement = one_paragraph(row.get("reason_replacement", "")) if reading == "REASON_CONTRADICTED" else ""
    if reading == "REASON_CONTRADICTED" and len(replacement) < 80:
        return "a reason correction without a replacement reason"
    return RowEdit(
        row["term"],
        negated=row["negated"],
        add_support=tuple((reference, quote) for quote in quotes),
        append_reason="" if replacement else sentence,
        replace_reason=replacement or None,
        add_failure_modes=tuple(row.get("failure_modes_add") or []) if replacement else (),
        remove_failure_modes=tuple(row.get("failure_modes_remove") or []) if replacement else (),
    )


def validate(review_path: Path) -> tuple[bool, str]:
    """Run the gene-review validator on one file: ``(valid, first lines of its output)``."""
    result = subprocess.run(
        [sys.executable, "-m", "ai_gene_review.cli", "validate", str(review_path.relative_to(ROOT))],
        cwd=ROOT, capture_output=True, text=True, check=False,
    )
    output = result.stdout + result.stderr
    return result.returncode == 0 and "✓ Valid" in output, output


def _new_history() -> Any:
    """The history scaffolder's module (a script, so it is loaded by path)."""
    spec = importlib.util.spec_from_file_location("new_history", ROOT / "scripts" / "new_history.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def history_details(gene: str, rows: list[dict[str, Any]]) -> str:
    """What was done to one review, for its history record."""
    organism, name = gene.split("/")
    lines = [
        f"Re-read of the overruled IBA rows against the PANTHER 19.0 tree and family alignment "
        f"({name}-phylo.yaml, from `just phylo {organism} {name}`). An agent read each row's verdict "
        "and reasons next to the extract's facts for the same row; a second agent checked every "
        "correction and a sample of the rest. Verdicts are unchanged.",
        "",
    ]
    for row in rows:
        what = {
            "SUPPORTS": "the tree position agrees with the stated reason",
            "NOT_A_TREE_ARGUMENT": "the verdict rests on evidence the tree does not speak to, and the tree contradicts nothing stated",
            "PAINT_ALREADY_REMOVED": "PAINT has itself removed the term on the path to the gene",
            "REASON_CONTRADICTED": "the reason made a claim the tree contradicts; the reason was corrected",
        }[row["tree_reading"]]
        lines.append(f"- {row['term']} ({row['action']}): {what}. Added to the reason: {one_paragraph(row.get('tree_sentence', ''))}")
    lines += [
        "",
        "Each row now quotes its own extract in supported_by; the quotes were assembled from the "
        "extract's sentences by projects/IBA_REVIEW/tree-rereview/tree_rereview.py and checked "
        "verbatim. The review validates after the edit.",
    ]
    return "\n".join(lines)


def apply_batch(batch: str, jobs: int = 4) -> Counter[str]:
    """Make the edits of one batch record, validate, write history, update the record."""
    path = run_path(batch)
    record = load(path)
    by_gene: dict[str, list[dict[str, Any]]] = {}
    for row in record["rows"]:
        if row.get("outcome") == "pending":
            by_gene.setdefault(row["gene"], []).append(row)
    originals: dict[str, str] = {}
    for gene, rows in by_gene.items():
        review_path = gene_paths(gene)[0]
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
        if text != originals[gene]:
            review_path.write_text(text, encoding="utf-8")
    changed = [gene for gene, rows in by_gene.items() if any(row["outcome"] == "applied" for row in rows)]
    with ThreadPoolExecutor(max_workers=jobs) as pool:
        results = dict(zip(changed, pool.map(lambda gene: validate(gene_paths(gene)[0]), changed)))
    scaffolder = _new_history()
    for gene in changed:
        valid, output = results[gene]
        applied = [row for row in by_gene[gene] if row["outcome"] == "applied"]
        if not valid:
            gene_paths(gene)[0].write_text(originals[gene], encoding="utf-8")
            first_error = next((line.strip() for line in output.splitlines() if "ERROR" in line or "✗" in line), "no longer validates")
            for row in applied:
                row["outcome"], row["outcome_detail"] = "adjudicate", f"edit undone, the review no longer validated: {first_error[:300]}"
            continue
        organism, name = gene.split("/")
        scaffolder.main([
            "--kind", "gene", "--organism", organism, "--slug", name, "--event", "REVIEW", "--outcome", "changed",
            "--agent-tool", "claude-code", "--sections", "existing_annotations",
            "--summary", f"Re-read {len(applied)} overruled IBA row{'s' if len(applied) != 1 else ''} against the PANTHER tree; extract quoted",
            "--details", history_details(gene, applied),
        ])
    path.write_text(dump(record), encoding="utf-8")
    return Counter(row["outcome"] for row in record["rows"])


def status() -> str:
    """Progress over the committed plan and run records."""
    plan = load(PLAN)
    outcomes: Counter[str] = Counter()
    readings: Counter[str] = Counter()
    done = 0
    for entry in plan["batches"]:
        path = run_path(entry["id"])
        if not path.exists():
            continue
        done += 1
        for row in load(path)["rows"]:
            outcomes[row.get("outcome", "?")] += 1
            readings[row.get("tree_reading", "(not read)")] += 1
    lines = [
        f"plan: {plan['rows']} rows in {plan['genes']} genes, {len(plan['batches'])} batches; {done} batches recorded",
        "outcomes: " + ", ".join(f"{name} {count}" for name, count in outcomes.most_common()),
        "readings: " + ", ".join(f"{name} {count}" for name, count in readings.most_common()),
    ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").split("\n")[0])
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("plan")
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
    commands.add_parser("status")
    args = parser.parse_args(argv)

    if args.command == "plan":
        if PLAN.exists():
            raise SystemExit(f"{PLAN.relative_to(ROOT)} exists; the plan is made once and then kept")
        plan = build_plan()
        PLAN.write_text(dump(plan), encoding="utf-8")
        print(f"{plan['rows']} rows in {plan['genes']} genes, {len(plan['batches'])} batches")
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
        print(dict(apply_batch(args.batch, args.jobs)))
    else:
        print(status())
    return 0


if __name__ == "__main__":
    sys.exit(main())
