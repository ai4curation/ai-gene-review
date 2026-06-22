#!/usr/bin/env python3
"""Find candidate MISSING ECM GO annotations using the matrisome family -> GO mapping.

Path (2) of the matrisome work. For every reviewed gene (``genes/<species>/<gene>/<gene>-goa.tsv``):

1. Look up the gene (by UniProt accession or symbol) in the matrisome masterlist
   (``data/matrisome_*.csv``; columns gene/category/family).
2. If it is a **core matrisome** gene, apply the curated family->GO mapping
   (``matrisome2go.sssom.yaml``) to get the expected ECM cellular-component term.
3. Compare that expected term to the gene's existing GO annotations (from GOA). A proposed term that
   is neither already present nor subsumed by a more specific term the gene already has is a
   **candidate missing annotation** -- a lead for a curator, not an automatic assertion.

Only core-matrisome families are mapped (the associated families are gap rows in the SSSOM), so this
deliberately never proposes ECM localization for proteases, cross-linkers, or secreted factors.

Outputs:
- ``MISSING_ANNOTATIONS.md`` - human-readable summary.
- ``data/candidate_missing_annotations.tsv`` - one row per (gene, candidate GO term).

Usage::

    uv run python projects/MATRISOME/missing_annotation_report.py \
        --sssom projects/MATRISOME/matrisome2go.sssom.yaml \
        --matrisome-data projects/MATRISOME/data \
        --genes-dir genes \
        --out-md projects/MATRISOME/MISSING_ANNOTATIONS.md \
        --out-tsv projects/MATRISOME/data/candidate_missing_annotations.tsv
"""
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

import yaml

GO_RE = re.compile(r"GO:\d+")
CORE_CATEGORY = "Core matrisome"

# Map a genes/<species>/ directory code to the matrisome masterlist file key. The matrisome is a
# metazoan resource covering five species; genes under any other species directory (bacteria, fungi,
# plants, ...) are deliberately not matched, avoiding symbol-collision false positives.
SPECIES_MAP = {
    "human": "human",
    "mouse": "mouse",
    "zebrafish": "zebrafish",
    "danre": "zebrafish",
    "drosophila": "drosophila",
    "drome": "drosophila",
    "fly": "drosophila",
    "worm": "c_elegans",
    "caeel": "c_elegans",
}


def load_family_go_mappings(sssom_path: Path) -> dict[str, tuple[str, str]]:
    """Return ``family_label -> (go_id, go_label)`` for the GO (non-gap) mappings.

    >>> import tempfile, textwrap, pathlib
    >>> p = pathlib.Path(tempfile.mkdtemp()) / "m.yaml"
    >>> _ = p.write_text(textwrap.dedent('''
    ...   mappings:
    ...   - {subject_id: "matrisome:Proteoglycans", subject_label: "Proteoglycans",
    ...      predicate_id: "RO:0001025", object_id: "GO:0031012", object_label: "extracellular matrix",
    ...      mapping_justification: "semapv:ManualMappingCuration"}
    ...   - {subject_id: "matrisome:Secreted Factors", subject_label: "Secreted Factors",
    ...      predicate_id: "skos:relatedMatch", object_id: "sssom:NoTermFound",
    ...      mapping_justification: "semapv:ManualMappingCuration"}
    ... '''))
    >>> load_family_go_mappings(p)
    {'Proteoglycans': ('GO:0031012', 'extracellular matrix')}
    """
    doc = yaml.safe_load(sssom_path.read_text())
    out: dict[str, tuple[str, str]] = {}
    for m in doc.get("mappings", []):
        obj = str(m.get("object_id", ""))
        if obj.startswith("GO:"):
            out[m["subject_label"]] = (obj, m.get("object_label", ""))
    return out


def load_matrisome(data_dir: Path) -> dict[str, dict[str, tuple[str, str]]]:
    """Build ``{species_key: {UPPER(identifier): (category, family)}}`` per matrisome_*.csv file.

    The masterlist carries one row per identifier (symbol, alias, UniProt, RefSeq, Ensembl, GeneID),
    all sharing the same category/family, so any of a gene's identifiers resolves to its family.
    Lookups are kept per-species (rather than unioned) so that short symbols/aliases of non-metazoan
    genes cannot collide with a matrisome alias in another species. On a rare conflicting duplicate
    within a species, core-matrisome is preferred.
    """
    by_species: dict[str, dict[str, tuple[str, str]]] = {}
    for csv_path in sorted(data_dir.glob("matrisome_*.csv")):
        species_key = csv_path.stem[len("matrisome_"):]
        lookup: dict[str, tuple[str, str]] = {}
        with csv_path.open() as fh:
            for row in csv.DictReader(fh):
                gene = (row.get("gene") or "").strip()
                category = (row.get("category") or "").strip()
                family = (row.get("family") or "").strip()
                if not gene:
                    continue
                key = gene.upper()
                prev = lookup.get(key)
                if prev is None or (prev[0] != CORE_CATEGORY and category == CORE_CATEGORY):
                    lookup[key] = (category, family)
        by_species[species_key] = lookup
    return by_species


def parse_goa(goa_path: Path) -> tuple[str, str, set[str]]:
    """Return ``(uniprot_acc, symbol, {existing GO ids})`` from a QuickGO ``*-goa.tsv`` file.

    Columns are read by header name (GENE PRODUCT ID / SYMBOL / GO TERM).
    """
    acc = ""
    symbol = ""
    go_ids: set[str] = set()
    with goa_path.open() as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for row in reader:
            acc = acc or (row.get("GENE PRODUCT ID") or "").strip()
            symbol = symbol or (row.get("SYMBOL") or "").strip()
            term = (row.get("GO TERM") or "").strip()
            if GO_RE.fullmatch(term):
                go_ids.add(term)
    return acc, symbol, go_ids


def classify_candidate(
    go_id: str, existing: set[str], go_descendants: dict[str, set[str]] | None
) -> str:
    """Classify a proposed GO term against a gene's existing GO annotations.

    Returns ``"already"`` (gene has this exact term), ``"redundant"`` (gene has a more specific
    is_a descendant of the proposed term), or ``"new"`` (a genuine candidate).

    >>> desc = {"GO:0031012": {"GO:0005604"}}  # basement membrane is_a extracellular matrix
    >>> classify_candidate("GO:0031012", {"GO:0005604"}, desc)
    'redundant'
    >>> classify_candidate("GO:0031012", {"GO:0005634"}, desc)
    'new'
    >>> classify_candidate("GO:0031012", {"GO:0031012"}, desc)
    'already'
    """
    if go_id in existing:
        return "already"
    if go_descendants and (existing & go_descendants.get(go_id, set())):
        return "redundant"
    return "new"


def build_go_descendant_index(go_ids: set[str], adapter_string: str) -> dict[str, set[str]]:
    """Map each proposed GO id -> its is_a descendant GO ids (excluding self)."""
    from oaklib import get_adapter
    from oaklib.datamodels.vocabulary import IS_A

    adapter = get_adapter(adapter_string)
    index: dict[str, set[str]] = {}
    for go_id in go_ids:
        try:
            index[go_id] = set(adapter.descendants(go_id, predicates=[IS_A])) - {go_id}
        except Exception:
            index[go_id] = set()
    return index


def iter_genes(genes_dir: Path):
    """Yield ``(species, gene, goa_path)`` for every ``*-goa.tsv`` under ``genes_dir``."""
    for goa_path in sorted(genes_dir.glob("*/*/*-goa.tsv")):
        gene = goa_path.parent.name
        species = goa_path.parent.parent.name
        yield species, gene, goa_path


def compute(genes_dir, matrisome, family_go, go_descendants=None):
    """Scan genes and return (candidate_rows, stats)."""
    candidate_rows: list[dict] = []
    stats = {
        "genes_total": 0,
        "in_matrisome": 0,
        "core_matrisome": 0,
        "candidates": 0,
        "already": Counter(),
        "redundant": Counter(),
        "new_by_family": Counter(),
    }
    for species, gene, goa_path in iter_genes(genes_dir):
        stats["genes_total"] += 1
        species_key = SPECIES_MAP.get(species.lower())
        if species_key is None:
            continue  # non-metazoan / unsupported species: matrisome does not apply
        lookup = matrisome.get(species_key, {})
        acc, symbol, existing = parse_goa(goa_path)
        hit = lookup.get(acc.upper()) or lookup.get(symbol.upper()) or lookup.get(gene.upper())
        if hit is None:
            continue
        stats["in_matrisome"] += 1
        category, family = hit
        if category != CORE_CATEGORY:
            continue
        stats["core_matrisome"] += 1
        mapped = family_go.get(family)
        if mapped is None:
            continue
        go_id, go_label = mapped
        verdict = classify_candidate(go_id, existing, go_descendants)
        if verdict == "already":
            stats["already"][go_id] += 1
            continue
        if verdict == "redundant":
            stats["redundant"][go_id] += 1
            continue
        stats["candidates"] += 1
        stats["new_by_family"][family] += 1
        candidate_rows.append(
            {
                "species": species,
                "gene": gene,
                "uniprot_acc": acc,
                "symbol": symbol,
                "matrisome_category": category,
                "matrisome_family": family,
                "proposed_go_id": go_id,
                "proposed_go_label": go_label,
                "existing_go_count": len(existing),
            }
        )
    return candidate_rows, stats


def render_md(stats, candidate_rows, family_go) -> str:
    lines = [
        "# Candidate missing ECM annotations (matrisome family → GO)",
        "",
        "Genes that the matrisome masterlist classifies as **core matrisome** but whose GOA lacks the",
        "expected extracellular-matrix cellular-component term, per the curated",
        "[`matrisome2go.sssom.yaml`](matrisome2go.sssom.yaml) mapping. These are **leads for a curator,",
        "not automatic assertions**. A proposal is suppressed when the gene already has the term or a",
        "more specific (is_a descendant) term (subsumption-aware filtering).",
        "",
        "Generated by `missing_annotation_report.py` from the local `genes/**/*-goa.tsv` snapshots.",
        "",
        "## Summary",
        "",
        f"- Reviewed genes scanned: **{stats['genes_total']:,}**",
        f"- Found in matrisome masterlist: **{stats['in_matrisome']:,}**",
        f"- Core-matrisome (mappable) genes: **{stats['core_matrisome']:,}**",
        f"- Candidate missing annotations: **{stats['candidates']:,}**",
        f"- Already annotated (suppressed): **{sum(stats['already'].values()):,}**",
        f"- Redundant / has more specific term (suppressed): **{sum(stats['redundant'].values()):,}**",
        "",
        "## Candidates",
        "",
        "| species | gene | UniProt | family | proposed GO | label |",
        "|---------|------|---------|--------|-------------|-------|",
    ]
    for r in sorted(candidate_rows, key=lambda r: (r["proposed_go_id"], r["species"], r["gene"])):
        lines.append(
            f"| {r['species']} | {r['gene']} | {r['uniprot_acc']} | {r['matrisome_family']} | "
            f"{r['proposed_go_id']} | {r['proposed_go_label']} |"
        )
    if not candidate_rows:
        lines.append("| _(none)_ | | | | | |")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sssom", type=Path, default=Path("projects/MATRISOME/matrisome2go.sssom.yaml"))
    ap.add_argument("--matrisome-data", type=Path, default=Path("projects/MATRISOME/data"))
    ap.add_argument("--genes-dir", type=Path, default=Path("genes"))
    ap.add_argument("--out-md", type=Path, default=Path("projects/MATRISOME/MISSING_ANNOTATIONS.md"))
    ap.add_argument(
        "--out-tsv", type=Path, default=Path("projects/MATRISOME/data/candidate_missing_annotations.tsv")
    )
    ap.add_argument("--go-adapter", default="sqlite:obo:go")
    ap.add_argument(
        "--subsumption", dest="subsumption", default=True, action=argparse.BooleanOptionalAction,
        help="Suppress a candidate when the gene already has a more specific (is_a descendant) GO term",
    )
    args = ap.parse_args(argv)

    family_go = load_family_go_mappings(args.sssom)
    matrisome = load_matrisome(args.matrisome_data)
    go_descendants = (
        build_go_descendant_index({g for g, _ in family_go.values()}, args.go_adapter)
        if args.subsumption
        else None
    )
    candidate_rows, stats = compute(args.genes_dir, matrisome, family_go, go_descendants)

    args.out_tsv.parent.mkdir(parents=True, exist_ok=True)
    cols = [
        "species", "gene", "uniprot_acc", "symbol", "matrisome_category", "matrisome_family",
        "proposed_go_id", "proposed_go_label", "existing_go_count",
    ]
    with args.out_tsv.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t")
        w.writeheader()
        w.writerows(sorted(candidate_rows, key=lambda r: (r["proposed_go_id"], r["species"], r["gene"])))

    args.out_md.write_text(render_md(stats, candidate_rows, family_go) + "\n")
    print(
        f"# {stats['genes_total']} genes; {stats['in_matrisome']} in matrisome; "
        f"{stats['core_matrisome']} core; {stats['candidates']} candidate missing annotations."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
