#!/usr/bin/env python3
"""Join every reviewed IBA row with what the PANTHER tree and family alignment say about it.

For each IBA row of each gene review this writes one line: the review's action and
propagation taxonomy, and the tree facts that `just phylo` computes for the same row
(where the PAINT node sits, how many duplications separate it from the gene, whether the
gene lies inside the clade spanned by the seeds, how the nearest seed is related to it and
how similar the two are in the family alignment).

The facts come from the PANTHER release database (`just fetch-panther-release`), not
from the committed `GENE-phylo.yaml` files, so the table covers every gene with an IBA
row whether or not its extract has been written. Nothing about the result is
hard-coded; a row that cannot be placed is written with empty fact columns.

Usage (from the repository root):
    uv run python projects/IBA_REVIEW/tree_evidence.py                 # write tree-evidence-rows.tsv.gz
    uv run python projects/IBA_REVIEW/tree_evidence.py --summary       # print the tables in tree-evidence.md
    uv run python projects/IBA_REVIEW/tree_evidence.py --candidates    # write tree-evidence-candidates.yaml
    uv run python projects/IBA_REVIEW/tree_evidence.py --seed-lists    # GOA seed lists against the PAINT slices
"""

from __future__ import annotations

import argparse
import csv
import gzip
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

import yaml

from ai_gene_review.etl.gene_phylo import (
    build_gene_phylo,
    phylo_path,
    read_iba_rows,
    read_paint_slice,
    resolve_seed,
)
from ai_gene_review.etl.panther_release import DEFAULT_DB, FamilyTree, PantherRelease
from ai_gene_review.validation.tree_evidence import phylo_reference_ids

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
ROWS = HERE / "tree-evidence-rows.tsv.gz"
CANDIDATES = HERE / "tree-evidence-candidates.yaml"
Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

FIELDS = [
    "gene", "term", "label", "aspect", "negated", "action", "root_cause", "failure_modes",
    "family", "ibd_node", "node_event", "node_taxon", "node_is_root", "node_leaves",
    "node_species", "node_subfamilies", "placed", "steps", "duplications_on_path",
    "transfers_on_path", "path_length", "seeds", "seeds_resolved", "seeds_unresolved", "self_seed",
    "seed_branches", "node_branches", "seed_mrca_steps_below_node", "target_in_seed_clade",
    "orthologs", "one_to_one_orthologs", "paralogs", "xenologs", "nearest_seed",
    "nearest_relation", "nearest_distance", "nearest_identity", "nearest_covers_target",
    "nearest_covers_seed", "max_identity", "paint_losses_on_path", "has_extract", "cites_extract",
]
OVERRULED = {"REMOVE", "MARK_AS_OVER_ANNOTATED"}
RETAINED = {"ACCEPT", "KEEP_AS_NON_CORE"}
REFINED = {"MODIFY", "TOO_GENERAL"}


def genes_with_iba(root: Path) -> list[tuple[str, str]]:
    """Every (organism, gene) whose GOA file has an IBA row and that has a review file."""
    pairs = []
    for goa in sorted(root.glob("genes/*/*/*-goa.tsv")):
        folder = goa.parent
        if not (folder / f"{folder.name}-ai-review.yaml").exists():
            continue
        with goa.open(encoding="utf-8", errors="replace") as handle:
            if any("\tIBA\t" in line for line in handle):
                pairs.append((folder.parent.name, folder.name))
    return pairs


def _mapping(value: Any) -> dict[str, Any]:
    """``value`` when it is a mapping, otherwise an empty one."""
    return value if isinstance(value, dict) else {}


def review_rows(path: Path) -> dict[tuple[str, bool], dict[str, Any]]:
    """The review's IBA rows keyed by (term id, negated); the first row wins on a repeat."""
    data = yaml.load(path.read_text(encoding="utf-8"), Loader=Loader) or {}
    own = phylo_reference_ids(path)
    rows: dict[tuple[str, bool], dict[str, Any]] = {}
    for annotation in data.get("existing_annotations") or []:
        if not isinstance(annotation, dict) or annotation.get("evidence_type") != "IBA":
            continue
        review = _mapping(annotation.get("review"))
        propagation = _mapping(review.get("propagation_review"))
        term = _mapping(annotation.get("term")).get("id", "")
        key = (term, bool(annotation.get("negated")))
        rows.setdefault(
            key,
            {
                "action": review.get("action", ""),
                "root_cause": propagation.get("root_cause", ""),
                "failure_modes": "|".join(propagation.get("failure_modes") or []),
                "cites_extract": any(
                    isinstance(item, dict) and str(item.get("reference_id", "")) in own
                    for item in review.get("supported_by") or []
                ),
            },
        )
    return rows


def facts(root: Path, organism: str, gene: str, release: PantherRelease) -> Iterable[dict[str, Any]]:
    """One record per IBA row of one gene, review verdict joined to tree facts."""
    doc = build_gene_phylo(root, organism, gene, release)
    if doc is None:
        return
    verdicts = review_rows(root / "genes" / organism / gene / f"{gene}-ai-review.yaml")
    has_extract = phylo_path(root, organism, gene).exists()
    for tree in doc["trees"]:
        nodes = {node["node"]: node for node in tree["nodes"]}
        seeds = {seed["id"]: seed for seed in tree["seeds"]}
        for row in tree["rows"]:
            node = nodes[row["ibd_node"]]
            verdict = verdicts.get((row["term"]["id"], row["negated"]), {})
            others = [
                seeds[token]
                for token in row["seeds"]
                if token in seeds and seeds[token].get("relation") not in (None, "SELF")
            ]
            distinct = {seed["leaf"]: seed for seed in others}.values()
            nearest = seeds.get(row.get("nearest_seed") or "", {})
            identities = [seed["identity"] for seed in distinct if "identity" in seed]
            yield {
                "gene": f"{organism}/{gene}",
                "term": row["term"]["id"],
                "label": row["term"]["label"],
                "aspect": row["aspect"],
                "negated": row["negated"],
                **{key: verdict.get(key, "") for key in ("action", "root_cause", "failure_modes")},
                "family": tree["family"],
                "ibd_node": row["ibd_node"],
                "node_event": node["event"],
                "node_taxon": node.get("taxon") or node.get("after", ""),
                "node_is_root": node["is_root"],
                "node_leaves": node["leaves"],
                "node_species": node["species"],
                "node_subfamilies": node["subfamilies"],
                "placed": "steps" in row,
                **{key: row.get(key, "") for key in (
                    "steps", "duplications_on_path", "transfers_on_path", "path_length",
                )},
                "seeds": len(row["seeds"]),
                "seeds_resolved": row["seeds_resolved"],
                "seeds_unresolved": row["seeds_unresolved"],
                **{key: row.get(key, "") for key in (
                    "self_seed", "seed_branches", "node_branches", "seed_mrca_steps_below_node",
                    "target_in_seed_clade", "orthologs", "one_to_one_orthologs", "paralogs", "xenologs",
                )},
                "nearest_seed": row.get("nearest_seed") or "",
                "nearest_relation": nearest.get("relation", ""),
                "nearest_distance": nearest.get("tree_distance", ""),
                "nearest_identity": nearest.get("identity", ""),
                "nearest_covers_target": nearest.get("covers_target", ""),
                "nearest_covers_seed": nearest.get("covers_seed", ""),
                "max_identity": max(identities) if identities else "",
                "paint_losses_on_path": sum(
                    "reasserted_below" not in loss for loss in row.get("paint_losses_on_path") or []
                ),
                "has_extract": has_extract,
                "cites_extract": verdict.get("cites_extract", False),
            }
    for row in doc.get("unplaced_rows", []):
        verdict = verdicts.get((row["term"]["id"], False), {})
        yield {
            "gene": f"{organism}/{gene}", "term": row["term"]["id"], "label": row["term"]["label"],
            "negated": False, "placed": False,
            **{key: verdict.get(key, "") for key in ("action", "root_cause", "failure_modes")},
        }


def write_rows(root: Path, release: PantherRelease, out: Path) -> int:
    """Write the row table; returns the number of rows."""
    pairs = genes_with_iba(root)
    count = 0
    with gzip.open(out, "wt", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, FIELDS, delimiter="\t", restval="", lineterminator="\n")
        writer.writeheader()
        for index, (organism, gene) in enumerate(pairs, 1):
            for record in facts(root, organism, gene, release):
                writer.writerow(record)
                count += 1
            if index % 500 == 0:
                print(f"{index}/{len(pairs)} genes, {count} rows", file=sys.stderr)
    return count


def read_rows(path: Path = ROWS) -> list[dict[str, str]]:
    """The row table as dicts of strings."""
    with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def placement_class(row: dict[str, str]) -> str:
    """Where the gene stands relative to the evidence for the node, read from the tree alone."""
    if row["placed"] != "True":
        return "0 not placed"
    if int(row["paint_losses_on_path"] or 0):
        return "1 PAINT loss on the path"
    if row["self_seed"] == "True":
        return "2 gene is itself a seed"
    if not int(row["seeds_resolved"] or 0):
        return "7 no resolved seed"
    inside = row["target_in_seed_clade"] == "True"
    one_to_one = int(row["one_to_one_orthologs"] or 0) > 0
    if inside and one_to_one:
        return "3 inside the seed clade, with a one-to-one ortholog seed"
    if inside:
        return "4 inside the seed clade, no one-to-one ortholog seed"
    if one_to_one:
        return "5 outside the seed clade, with a one-to-one ortholog seed"
    return "6 outside the seed clade, no one-to-one ortholog seed"


def _bin(value: str, edges: list[float], labels: list[str]) -> str:
    if value == "":
        return "n/a"
    number = float(value)
    for edge, label in zip(edges, labels):
        if number < edge:
            return label
    return labels[-1]


def _table(title: str, groups: dict[str, list[dict[str, str]]]) -> list[str]:
    """A markdown table of verdict rates per group (rated rows only)."""
    lines = [f"### {title}", "", "| | rated | kept | refined | overruled | % overruled | % REMOVE |", "|---|---:|---:|---:|---:|---:|---:|"]
    for name in sorted(groups):
        rated = [r for r in groups[name] if r["action"] in OVERRULED | RETAINED | REFINED]
        if not rated:
            continue
        kept = sum(r["action"] in RETAINED for r in rated)
        refined = sum(r["action"] in REFINED for r in rated)
        over = sum(r["action"] in OVERRULED for r in rated)
        removed = sum(r["action"] == "REMOVE" for r in rated)
        lines.append(
            f"| {name} | {len(rated)} | {kept} | {refined} | {over} | "
            f"{100 * over / len(rated):.1f}% | {100 * removed / len(rated):.1f}% |"
        )
    return lines + [""]


def summary(rows: list[dict[str, str]]) -> str:
    """The tables quoted in tree-evidence.md."""
    positive = [r for r in rows if r["negated"] != "True"]
    placed = [r for r in positive if r["placed"] == "True"]
    out = [
        f"rows: {len(rows)} IBA rows in {len({r['gene'] for r in rows})} genes; "
        f"{len(positive)} positive; {len(placed)} placed in a PANTHER tree",
        f"seed tokens: {sum(int(r['seeds'] or 0) for r in placed)}, of which unresolved: "
        f"{sum(int(r['seeds_unresolved'] or 0) for r in placed)}; rows with every seed resolved: "
        f"{sum(int(r['seeds_unresolved'] or 0) == 0 for r in placed)}",
        f"overruled rows: {sum(r['action'] in OVERRULED for r in positive)}; with an extract file: "
        f"{sum(r['action'] in OVERRULED and r['has_extract'] == 'True' for r in positive)}; citing it: "
        f"{sum(r['action'] in OVERRULED and r['cites_extract'] == 'True' for r in positive)}",
        "",
    ]
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in positive:
        groups[placement_class(r)].append(r)
    out += _table("Verdict by where the gene stands relative to the seeds", groups)

    groups = defaultdict(list)
    for r in placed:
        if r["self_seed"] != "True":
            groups[_bin(r["duplications_on_path"], [1, 2, 3], ["0 duplications", "1 duplication", "2 duplications", "3 or more"])].append(r)
    out += _table("Verdict by duplications between the PAINT node and the gene (gene not itself a seed)", groups)

    groups = defaultdict(list)
    for r in placed:
        if r["self_seed"] != "True" and r["nearest_relation"]:
            groups[r["nearest_relation"].lower() + " (nearest seed)"].append(r)
    out += _table("Verdict by how the nearest seed is related to the gene", groups)

    groups = defaultdict(list)
    for r in placed:
        if r["self_seed"] != "True" and r["max_identity"] != "":
            groups[_bin(r["max_identity"], [0.2, 0.3, 0.4, 0.6, 0.8], ["a <20%", "b 20-30%", "c 30-40%", "d 40-60%", "e 60-80%", "f 80% or more"])].append(r)
    out += _table("Verdict by identity to the most similar seed in the family alignment", groups)

    groups = defaultdict(list)
    for r in placed:
        if r["seed_mrca_steps_below_node"] != "" and int(r["seeds_resolved"] or 0) >= 2:
            groups[_bin(r["seed_mrca_steps_below_node"], [1, 2, 4], ["0 steps: seeds bracket the node", "1 step below", "2-3 steps below", "4 or more steps below"])].append(r)
    out += _table("Verdict by how far the seeds' common ancestor is below the PAINT node (two or more seeds)", groups)

    claims = [
        r for r in positive
        if r["action"] in OVERRULED and "WRONG_ORTHOLOG_OR_PARALOG" in r["failure_modes"] and r["placed"] == "True"
    ]
    out.append(
        f"WRONG_ORTHOLOG_OR_PARALOG overrulings: {len(claims)}; with only ortholog seeds and no duplication "
        f"between the node and the gene: {sum(_only_orthologs(r) for r in claims)}; of those, with every seed "
        f"a one-to-one ortholog: {sum(_only_orthologs(r, strict=True) for r in claims)}"
    )
    out.append(
        f"overruled although the gene is itself a seed: "
        f"{sum(r['action'] in OVERRULED and r['self_seed'] == 'True' for r in positive)}; "
        f"kept or refined with an unlifted PAINT loss on the path: "
        f"{sum(r['action'] in RETAINED | REFINED and int(r['paint_losses_on_path'] or 0) > 0 for r in positive)}"
    )
    return "\n".join(out)


def _only_orthologs(row: dict[str, str], strict: bool = False) -> bool:
    """True when the tree shows no paralogy between the gene and any seed of the row.

    The seeds are all orthologs and no duplication lies between the PAINT node and the
    gene. With ``strict`` every seed must also be a one-to-one ortholog, that is, the
    seeds' own lineages have not duplicated either.
    """
    orthologs = int(row["orthologs"] or 0)
    if not orthologs or int(row["paralogs"] or 0) or int(row["xenologs"] or 0):
        return False
    if int(row["duplications_on_path"] or 0):
        return False
    return not strict or int(row["one_to_one_orthologs"] or 0) == orthologs


def candidates(rows: list[dict[str, str]]) -> dict[str, Any]:
    """Rows whose verdict and tree facts pull in different directions, for re-review."""
    def brief(r: dict[str, str]) -> dict[str, Any]:
        return {
            "gene": r["gene"], "term": r["term"], "label": r["label"], "action": r["action"],
            "ibd_node": r["ibd_node"], "placement": placement_class(r)[2:],
            "duplications_on_path": int(r["duplications_on_path"] or 0),
            "nearest_seed": r["nearest_seed"], "nearest_relation": r["nearest_relation"],
            "max_identity": float(r["max_identity"]) if r["max_identity"] else None,
        }

    positive = [r for r in rows if r["negated"] != "True" and r["placed"] == "True"]
    stale = [r for r in positive if int(r["paint_losses_on_path"] or 0)]
    paralog_claim = [
        r for r in positive
        if r["action"] in OVERRULED and "WRONG_ORTHOLOG_OR_PARALOG" in r["failure_modes"] and _only_orthologs(r)
    ]
    self_seeded = [r for r in positive if r["action"] in OVERRULED and r["self_seed"] == "True"]

    def listed(items: list[dict[str, str]]) -> list[dict[str, Any]]:
        return sorted((brief(r) for r in items), key=lambda x: (x["gene"], x["term"]))

    return {
        "generated_by": "projects/IBA_REVIEW/tree_evidence.py --candidates",
        "paint_loss_on_path": {
            "meaning": (
                "PAINT has removed the term (IRD or IKR) on the path between the node and the gene and "
                "has not asserted it again below the loss, so the cached IBA row is stale"
            ),
            "rows": listed(stale),
        },
        "paralog_claim_without_duplication": {
            "meaning": (
                "overruled as WRONG_ORTHOLOG_OR_PARALOG, but in the PANTHER tree every resolved seed is an "
                "ortholog of the gene and no duplication lies between the node and the gene; "
                "all_one_to_one marks rows whose seeds have not duplicated either"
            ),
            "rows": [
                {**item, "all_one_to_one": _only_orthologs(r, strict=True)}
                for r, item in sorted(
                    ((r, brief(r)) for r in paralog_claim), key=lambda pair: (pair[1]["gene"], pair[1]["term"])
                )
            ],
        },
        "overruled_though_gene_is_a_seed": {
            "meaning": (
                "overruled although the gene's own experimental annotation is among the node's seeds; either "
                "that annotation is disputed too (a seed-side error) or the verdict needs another look"
            ),
            "rows": listed(self_seeded),
        },
    }


def _seed_leaves(tokens: Iterable[str], tree: FamilyTree, release: PantherRelease) -> set[str]:
    """Seed tokens as tree leaves; a token that names no leaf is kept as written."""
    resolved = set()
    for token in tokens:
        leaf, _ = resolve_seed(token, tree, release)
        resolved.add(leaf if leaf is not None else f"unresolved {token}")
    return resolved


def seed_list_agreement(root: Path, release: PantherRelease) -> str:
    """Compare each cached GOA IBA row's seed list with the local PAINT slice.

    A GOA row is a snapshot of PAINT at the time the gene was fetched; the family's
    ``<PTHR>-paint.tsv`` slice is a later one. For every positive IBA row whose family has a
    slice, the slice's IBD rows for the same node and term are looked up and the two seed
    lists compared as sets of tree leaves, so a MOD id and the UniProt accession of the
    same protein count as one seed.
    """
    slices: dict[str, dict[tuple[str, str], list[str]] | None] = {}
    outcome: Counter[str] = Counter()
    differing: Counter[int] = Counter()
    for organism, gene in genes_with_iba(root):
        for row in read_iba_rows(root / "genes" / organism / gene / f"{gene}-goa.tsv"):
            if row.negated or not row.nodes:
                continue
            located = release.locate_node(row.nodes[0])
            if located is None:
                outcome["node not in a release tree"] += 1
                continue
            family = located[0]
            if family not in slices:
                records = read_paint_slice(root / "interpro" / "panther" / family / f"{family}-paint.tsv")
                index: dict[tuple[str, str], list[str]] | None = None if records is None else {}
                for rec in records or []:
                    if index is not None and rec["evidence"] == "IBD" and rec["negated"] != "true":
                        index.setdefault((rec["node"], rec["go_id"]), []).extend(
                            token for token in rec["seeds"].split("|") if token
                        )
                slices[family] = index
            paint = slices[family]
            if paint is None:
                outcome["family has no local PAINT slice"] += 1
                continue
            paint_seeds = paint.get((row.nodes[0], row.term_id))
            if not paint_seeds:
                outcome["slice has no IBD row for the node and term"] += 1
                continue
            tree = release.tree(family)
            if tree is None:
                outcome["node not in a release tree"] += 1
                continue
            outcome["compared"] += 1
            differing[len(_seed_leaves(row.seeds, tree, release) ^ _seed_leaves(paint_seeds, tree, release))] += 1
    compared = outcome["compared"]
    lines = [f"{name}: {count}" for name, count in outcome.most_common()]
    for label, count in (
        ("same seeds", differing[0]),
        ("one seed differs", differing[1]),
        ("two seeds differ", differing[2]),
        ("three or more seeds differ", sum(n for delta, n in differing.items() if delta >= 3)),
    ):
        lines.append(f"  {label}: {count} ({100 * count / compared:.1f}% of compared)" if compared else f"  {label}: {count}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").split("\n")[0])
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--candidates", action="store_true")
    parser.add_argument("--seed-lists", action="store_true")
    parser.add_argument("--rows", type=Path, default=ROWS)
    args = parser.parse_args(argv)
    if args.seed_lists:
        print(seed_list_agreement(ROOT, PantherRelease(ROOT / DEFAULT_DB)))
        return 0
    if args.summary:
        print(summary(read_rows(args.rows)))
        return 0
    if args.candidates:
        CANDIDATES.write_text(
            yaml.safe_dump(candidates(read_rows(args.rows)), sort_keys=False, width=1_000_000, allow_unicode=True),
            encoding="utf-8",
        )
        print(CANDIDATES)
        return 0
    count = write_rows(ROOT, PantherRelease(ROOT / DEFAULT_DB), args.rows)
    print(f"{count} rows written to {args.rows}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
