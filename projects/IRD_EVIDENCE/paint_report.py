"""Draft a report of probable PAINT IRD errors for the PANTHER/PAINT curators.

Collects three kinds of case:

1. Family-review node assessments judging an IRD/IKR LOSS_CONTRADICTED or LOSS_TOO_BROAD
   (``interpro/panther/*/*-review.yaml``).
2. Gene-review rows whose ``propagation_review.paint_losses`` judge a loss CONTRADICTED
   or TOO_BROAD, for (node, term) pairs that no family review has assessed
   (``genes/*/*/*-ai-review.yaml``).
3. Stale overrides: IRD rows whose ancestral node no longer carries an IBD for the term
   (``ird_nodes.tsv``, from ``fetch_paint_ird.py``).
4. Fully re-annotated IRD rows, where PAINT still propagates a more specific term to every
   protein in the clade (``ird_fully_reannotated.tsv``, from ``ird_seed_check.py``).

Writes ``PAINT_REPORT.md``. It is a draft to send; nothing is posted anywhere.

Sections 2-4 read git-ignored inputs (``ird_nodes.tsv``, ``ird_clade_members.tsv.gz``,
``ird_fully_reannotated.tsv``), so the report cannot be regenerated from a clean
checkout: run ``fetch_paint_ird.py`` and ``ird_seed_check.py`` first. The script stops
rather than write a section empty.

Usage:
    uv run python projects/IRD_EVIDENCE/paint_report.py
"""

from __future__ import annotations

import csv
import gzip
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
OUT = HERE / "PAINT_REPORT.md"
SUGGEST = {
    "LOSS_CONTRADICTED": "Retract the IRD",
    "LOSS_TOO_BROAD": "Move the IRD to a lower node",
}


def first_sentences(text: str, n: int = 2) -> str:
    """The first ``n`` sentences of a reason, on one line.

    >>> first_sentences("One. Two (e.g. x). Three.", 2)
    'One. Two (e.g. x).'
    """
    flat = " ".join(text.split())
    parts = re.split(r"(?<=[.])\s+(?=[A-Z])", flat)
    return " ".join(parts[:n])


def family_cases() -> list[list[str]]:
    """Rows for node assessments that judge a PAINT loss wrong or too broad."""
    rows = []
    for path in sorted(ROOT.glob("interpro/panther/PTHR*/PTHR*-review.yaml")):
        doc = yaml.safe_load(path.read_text()) or {}
        for a in doc.get("node_assessments") or []:
            verdict = a.get("assessment", "")
            if verdict not in SUGGEST:
                continue
            term = a.get("asserted_term") or {}
            rows.append([
                path.parent.name,
                str(a.get("node_id", "")).split(":")[-1],
                f"{term.get('id')} {term.get('label', '')}",
                a.get("evidence", ""),
                verdict,
                first_sentences(a.get("assessment_reason", "")),
                SUGGEST[verdict],
                str(path.relative_to(ROOT)),
            ])
    return rows


GENE_SUGGEST = {"CONTRADICTED": "Retract the IRD", "TOO_BROAD": "Move the IRD to a lower node"}


def gene_cases(assessed: set[tuple[str, str]]) -> list[list[str]]:
    """Rows for gene-review losses judged contradicted or too broad, not already in section 1.

    The family is the one PAINT files the loss node under (``ird_nodes.tsv``); the gene's
    UniProt PANTHER cross-reference is used only when the node is not listed there, since
    the two can come from different PANTHER releases.
    """
    from ai_gene_review.validation.gene_paint_losses import panther_families

    with (HERE / "ird_nodes.tsv").open() as fh:
        node_family = {r["ird_node"]: r["family"] for r in csv.DictReader(fh, delimiter="\t")}
    members = HERE / "ird_clade_members.tsv.gz"
    if not members.exists():
        raise SystemExit(f"{members} is missing (it is git-ignored); run projects/IRD_EVIDENCE/fetch_paint_ird.py first")
    with gzip.open(members, "rt") as fh:
        clade: dict[str, set[str]] = {}
        for r in csv.DictReader(fh, delimiter="\t"):
            clade.setdefault(r["ird_node"], set()).add(r["leaf_node"])
    rows = []
    for path in sorted(ROOT.glob("genes/*/*/*-ai-review.yaml")):
        text = path.read_text()
        if "paint_losses:" not in text:
            continue
        doc = yaml.safe_load(text) or {}
        uniprot = path.with_name(path.name.replace("-ai-review.yaml", "-uniprot.txt"))
        xref_family = ", ".join(panther_families(uniprot.read_text())) if uniprot.exists() else ""
        for a in doc.get("existing_annotations") or []:
            review = a.get("review") or {}
            term = a.get("term") or {}
            for loss in (review.get("propagation_review") or {}).get("paint_losses") or []:
                agreement = loss.get("agreement", "")
                node = str(loss.get("node_id", "")).split(":")[-1]
                if agreement not in GENE_SUGGEST or (node, term.get("id")) in assessed:
                    continue
                rows.append([
                    node_family.get(node, xref_family), node, f"{term.get('id')} {term.get('label', '')}", loss.get("evidence", ""),
                    str(len(clade.get(node, ())) or "?"),
                    agreement, f"{doc.get('gene_symbol')} ({a.get('evidence_type')}:{review.get('action')})",
                    " ".join(str(loss.get("argument") or first_sentences(review.get("reason", ""), 1)).split()),
                    loss.get("suggestion") or GENE_SUGGEST[agreement],
                    str(path.relative_to(ROOT)),
                ])
    return rows


def stale_overrides() -> list[list[str]]:
    """IRD rows whose ancestral node has no IBD for the blocked term."""
    path = HERE / "ird_nodes.tsv"
    if not path.exists():
        raise SystemExit(
            f"{path} is missing (it is git-ignored); run projects/IRD_EVIDENCE/fetch_paint_ird.py "
            "first, or the stale-override section would be written empty"
        )
    with path.open() as fh:
        return [
            [r["family"], r["ird_node"], f"{r['go_id']} {r['go_label']}", r["ancestral_node"], r["date"]]
            for r in csv.DictReader(fh, delimiter="\t")
            if r["ancestral_has_ibd_for_term"] != "true"
        ]


def fully_reannotated() -> list[list[str]]:
    """IRD rows that every clade member still gets back through a more specific term."""
    path = HERE / "ird_fully_reannotated.tsv"
    if not path.exists():
        raise SystemExit(f"{path} is missing (it is git-ignored); run projects/IRD_EVIDENCE/ird_seed_check.py first")
    with path.open() as fh:
        return [
            [r["family"], r["ird_node"], f"{r['go_id']} {r['go_label']}", r["ird_date"],
             f"{r['clade_size']}/{r['clade_leaves']}", r["kind"],
             r["reannotated_by"].replace("|", "; ")]
            for r in csv.DictReader(fh, delimiter="\t")
        ]


def table(header: list[str], rows: list[list[str]]) -> list[str]:
    """A markdown table."""
    return ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)] + [
        "| " + " | ".join(str(c).replace("|", "/") for c in row) + " |" for row in rows
    ]


def main() -> int:
    """Write PAINT_REPORT.md."""
    fam = family_cases()
    stale = stale_overrides()
    genes = gene_cases({(r[1], r[2].split()[0]) for r in fam})
    full = fully_reannotated()
    md = [
        "# Probable PAINT IRD errors: draft report",
        "",
        "Draft for the PANTHER/PAINT curators, generated by `paint_report.py`. It has not been",
        "sent. Each case links the review that argues it, with verbatim quotes in that file.",
        "",
        f"## 1. Family reviews: losses judged contradicted or too broad ({len(fam)})",
        "",
        *table(["Family", "Node", "Blocked term", "Code", "Verdict", "Why (from the review)", "Suggested", "Review"], fam),
        "",
        f"## 2. Gene reviews: losses judged contradicted or too broad ({len(genes)})",
        "",
        "From `propagation_review.paint_losses` in the gene reviews, for losses no family",
        "review has assessed. The quoted evidence is in each gene review.",
        "",
        *table(["Family", "Node", "Blocked term", "Code", "Clade (leaves)", "Judged", "Gene (row)", "Why (from the review)", "Suggested", "Review"], genes),
        "",
        f"## 3. Stale overrides: the blocked IBD is gone ({len(stale)})",
        "",
        "The IRD's ancestral node no longer carries an IBD for the term, so the IRD blocks",
        "nothing and could be removed. Source: PAINT IBD.gaf via `fetch_paint_ird.py`.",
        "",
        *table(["Family", "IRD node", "Term", "Ancestral node", "IRD date"], stale),
        "",
        f"## 4. Fully re-annotated: the IRD blocks nothing ({len(full)})",
        "",
        "Every protein in the clade still gets a more specific term (is_a or part_of below the",
        "blocked one) as a positive IBA, from the IRD node itself or an ancestor. The IRD then",
        "contradicts PAINT's own propagation: it should also block that term, or be retracted.",
        "Source: `ird_seed_check.py` (see `ird_seed_check.md`).",
        "",
        *table(["Family", "IRD node", "Blocked term", "IRD date", "Clade (checked/all)", "Kind", "IBA sources (node, term, where)"], full),
        "",
    ]
    OUT.write_text("\n".join(md))
    print(f"wrote {OUT}: {len(fam)} family, {len(genes)} gene, {len(stale)} stale, {len(full)} re-annotated cases", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
