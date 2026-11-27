"""Inventory ND (No biological Data available) annotations across gene reviews.

For every ``genes/<ORG>/<GENE>/<GENE>-ai-review.yaml`` that reviews an ND row,
join the row to the gene's GOA file and UniProt record and record:

- the ND aspect, assigning group and date (from ``<GENE>-goa.tsv``);
- what else GOA asserts *in the same aspect*, by evidence class
  (experimental, phylogenetic, sequence/orthology, electronic). A bare
  ``GO:0005515`` protein-binding IPI is counted separately, not as
  experimental: per the NO_DATA rule it identifies no function;
- the review's action and ``nd_case`` on the ND row;
- protein length and UniProt protein-existence level;
- whether the review carries ``knowledge_gaps`` (and their kinds/aspects).

From these it assigns a provisional *signal* per ND row. Signals are
triage-grade, not curated case assignments: the NO_DATA project case
taxonomy (projects/NO_DATA.md) is decided by reading, and the signal only
says where to look first.

Writes ``projects/NO_DATA/data/nd-inventory.yaml`` and
``projects/NO_DATA/data/nd-summary.md``.

Run from the repository root:
    uv run python projects/NO_DATA/scripts/nd_inventory.py
"""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "projects" / "NO_DATA" / "data"

ROOTS = {
    "GO:0003674": "MF",
    "GO:0008150": "BP",
    "GO:0005575": "CC",
}
ASPECT_NAME = {
    "molecular_function": "MF",
    "biological_process": "BP",
    "cellular_component": "CC",
}
EXPERIMENTAL = {
    "EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
    "HTP", "HDA", "HMP", "HGI", "HEP",
}
PHYLO = {"IBA", "IBD", "IKR", "IRD"}
SEQUENCE = {"ISS", "ISO", "ISA", "ISM", "IGC", "RCA"}
AUTHOR = {"TAS", "NAS", "IC"}
MICROPROTEIN_MAX_LEN = 100
SQ_RE = re.compile(r"^SQ\s+SEQUENCE\s+(\d+) AA", re.M)
PE_RE = re.compile(r"^PE\s+(\d):\s*([^;]+);", re.M)


PROTEIN_BINDING = "GO:0005515"


def evidence_class(code: str, term: str = "") -> str:
    """Bucket a GO evidence code.

    >>> evidence_class("IDA"), evidence_class("IPI", PROTEIN_BINDING)
    ('experimental', 'protein_binding')
    """
    if term == PROTEIN_BINDING:
        return "protein_binding"
    if code in EXPERIMENTAL:
        return "experimental"
    if code in PHYLO:
        return "phylogenetic"
    if code in SEQUENCE:
        return "sequence"
    if code in AUTHOR:
        return "author"
    if code == "IEA":
        return "electronic"
    if code == "ND":
        return "nd"
    return "other"


def read_goa(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def read_uniprot(path: Path) -> tuple[int | None, str | None]:
    if not path.exists():
        return None, None
    text = path.read_text(errors="replace")
    sq = SQ_RE.search(text)
    pe = PE_RE.search(text)
    return (
        int(sq.group(1)) if sq else None,
        f"{pe.group(1)}: {pe.group(2).strip()}" if pe else None,
    )


def signal(other: Counter, length: int | None) -> str:
    """Provisional triage signal for one ND row (see module docstring)."""
    if length is not None and length <= MICROPROTEIN_MAX_LEN:
        prefix = "short_orf/"
    else:
        prefix = ""
    if other["experimental"]:
        return prefix + "coexists_with_experimental"
    if other["phylogenetic"] or other["sequence"]:
        return prefix + "inferable_by_homology"
    if other["electronic"] or other["author"] or other["other"] or other["protein_binding"]:
        return prefix + "electronic_or_author_only"
    return prefix + "aspect_empty"


def main() -> None:
    rows: list[dict] = []
    for review_path in sorted(ROOT.glob("genes/*/*/*-ai-review.yaml")):
        text = review_path.read_text()
        if "evidence_type: ND" not in text:
            continue
        doc = yaml.safe_load(text) or {}
        gene_dir = review_path.parent
        org, gene = gene_dir.parent.name, gene_dir.name
        goa = read_goa(gene_dir / f"{gene}-goa.tsv")
        length, pe = read_uniprot(gene_dir / f"{gene}-uniprot.txt")

        by_aspect: dict[str, Counter] = defaultdict(Counter)
        nd_meta: dict[str, dict] = {}
        for g in goa:
            aspect = ASPECT_NAME.get(g.get("GO ASPECT", ""))
            code = g.get("GO EVIDENCE CODE", "")
            if not aspect:
                continue
            if code == "ND":
                nd_meta[aspect] = {
                    "assigned_by": g.get("ASSIGNED BY"),
                    "date": g.get("DATE"),
                }
            else:
                by_aspect[aspect][evidence_class(code, g.get("GO TERM", ""))] += 1

        gaps = doc.get("knowledge_gaps") or []
        for cf in doc.get("core_functions") or []:
            gaps = gaps + (cf.get("knowledge_gaps") or [])
        gap_kinds = sorted({k for g in gaps for k in (g.get("gap_kind") or [])})
        gap_aspects = sorted({g["dark_aspect"] for g in gaps if g.get("dark_aspect")})

        for ann in doc.get("existing_annotations") or []:
            if ann.get("evidence_type") != "ND":
                continue
            term = (ann.get("term") or {}).get("id")
            aspect = ROOTS.get(term, "non_root")
            other = by_aspect.get(aspect, Counter())
            review = ann.get("review") or {}
            rows.append({
                "organism": org,
                "gene": gene,
                "id": doc.get("id"),
                "aspect": aspect,
                "term": term,
                "action": review.get("action"),
                "nd_case": review.get("nd_case"),
                "assigned_by": nd_meta.get(aspect, {}).get("assigned_by"),
                "nd_date": nd_meta.get(aspect, {}).get("date"),
                "same_aspect_annotations": dict(sorted(other.items())),
                "length": length,
                "protein_existence": pe,
                "n_knowledge_gaps": len(gaps),
                "gap_kinds": gap_kinds,
                "gap_dark_aspects": gap_aspects,
                "signal": signal(other, length),
            })

    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "nd-inventory.yaml").open("w") as fh:
        yaml.safe_dump({"nd_rows": rows}, fh, sort_keys=False, width=100)
    write_summary(rows)


def table(counter: Counter, header: str) -> list[str]:
    lines = [f"| {header} | ND rows |", "|---|---:|"]
    lines += [f"| {k} | {v} |" for k, v in counter.most_common()]
    return lines + [""]


def crosstab(rows: list[dict], a: str, b: str) -> list[str]:
    cols = sorted({str(r[b]) for r in rows})
    counts = Counter((str(r[a]), str(r[b])) for r in rows)
    keys = sorted({str(r[a]) for r in rows})
    lines = [f"| {a} \\ {b} | " + " | ".join(cols) + " |",
             "|---|" + "---:|" * len(cols)]
    for k in keys:
        lines.append(f"| {k} | " + " | ".join(str(counts[(k, c)]) for c in cols) + " |")
    return lines + [""]


def write_summary(rows: list[dict]) -> None:
    genes = {(r["organism"], r["gene"]) for r in rows}
    with_gaps = {(r["organism"], r["gene"]) for r in rows if r["n_knowledge_gaps"]}
    biology = {(r["organism"], r["gene"]) for r in rows if "BIOLOGY" in r["gap_kinds"]}
    lines = [
        "# ND inventory summary",
        "",
        "Generated by `projects/NO_DATA/scripts/nd_inventory.py`; do not edit.",
        "Signals are provisional triage, not curated case assignments.",
        "",
        f"- ND rows reviewed: {len(rows)}",
        f"- genes with at least one ND row: {len(genes)}",
        f"- of those, genes whose review has any `knowledge_gaps`: {len(with_gaps)}",
        f"- of those, genes with a `BIOLOGY` gap: {len(biology)}",
        "",
        "## By aspect",
        "",
        *table(Counter(r["aspect"] for r in rows), "aspect"),
        "## By assigning group",
        "",
        *table(Counter(str(r["assigned_by"]) for r in rows), "assigned_by"),
        "## By review action",
        "",
        *table(Counter(str(r["action"]) for r in rows), "action"),
        "## By nd_case",
        "",
        *table(Counter(str(r["nd_case"]) for r in rows), "nd_case"),
        "## nd_case x action",
        "",
        *crosstab(rows, "nd_case", "action"),
        "## By provisional signal",
        "",
        *table(Counter(r["signal"] for r in rows), "signal"),
        "## Signal x action",
        "",
        *crosstab(rows, "signal", "action"),
        "## Signal x aspect",
        "",
        *crosstab(rows, "signal", "aspect"),
    ]
    (OUT / "nd-summary.md").write_text("\n".join(lines))


if __name__ == "__main__":
    main()
