"""How much of ARFGEF1's primary literature has produced any GO annotation?

Inputs are all committed files in this gene folder -- no hardcoded PMID list:

* `ARFGEF1-deep-research-affinage.md`  -> the provider's `## Citations` block
* `ARFGEF1-uniprot.txt`                -> every `RX   PubMed=...` line
* `ARFGEF1-goa.tsv`                    -> the references GOA actually cites

For each PMID in the union of the first two, QuickGO is asked how many
annotations that reference supports anywhere in GOA, and whether any of them
land on ARFGEF1 (Q9Y6D6). A paper with zero annotations anywhere is a coverage
gap; a paper with annotations on other genes but none on ARFGEF1 is a
different, weaker signal and is counted separately.

Writes `literature_coverage.tsv`. Run from the repo root:
    uv run python genes/human/ARFGEF1/ARFGEF1-bioinformatics/literature_coverage.py
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from uniprot import quickgo_annotations  # noqa: E402

HERE = Path(__file__).parent
GENE_DIR = HERE.parent
SUBJECT = "UniProtKB:Q9Y6D6"


def affinage_citations() -> list[str]:
    text = (GENE_DIR / "ARFGEF1-deep-research-affinage.md").read_text()
    _, _, tail = text.partition("## Citations")
    if not tail:
        raise SystemExit(
            "affinage report has no '## Citations' section -- regenerate it with\n"
            "  uv run python projects/AFFINAGE_EVALUATION/affinage_deep_research.py human ARFGEF1 --write"
        )
    return re.findall(r"^-\s*PMID:(\d+)\s*$", tail, re.M)


def uniprot_pmids() -> list[str]:
    text = (GENE_DIR / "ARFGEF1-uniprot.txt").read_text()
    if "RX   PubMed=" not in text:
        raise SystemExit(
            "ARFGEF1-uniprot.txt has no RX PubMed lines -- refetch with\n"
            "  just fetch-gene human ARFGEF1"
        )
    return re.findall(r"^RX   PubMed=(\d+);", text, re.M)


def goa_references() -> set[str]:
    with (GENE_DIR / "ARFGEF1-goa.tsv").open() as fh:
        return {r["REFERENCE"] for r in csv.DictReader(fh, delimiter="\t")}


def main() -> None:
    aff = affinage_citations()
    up = uniprot_pmids()
    if not aff:
        raise SystemExit("no PMIDs parsed from the affinage citations block")
    if not up:
        raise SystemExit("no PMIDs parsed from the UniProt RX lines")
    union = sorted(set(aff) | set(up), key=int)
    in_goa = goa_references()

    rows = []
    for p in union:
        ref = f"PMID:{p}"
        d = quickgo_annotations(reference=ref, limit="200")
        results = d.get("results", [])
        n = d.get("numberOfHits", 0)
        on_subject = sum(1 for r in results if r["geneProductId"] == SUBJECT)
        rows.append({
            "pmid": ref,
            "in_affinage": str(p in set(aff)),
            "in_uniprot_rx": str(p in set(up)),
            "cited_by_ARFGEF1_goa": str(ref in in_goa),
            "annotations_anywhere": n,
            "annotations_on_ARFGEF1": "UNKNOWN (paginated)" if d["_truncated"] else str(on_subject),
        })

    with (HERE / "literature_coverage.tsv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    zero = [r["pmid"] for r in rows if r["annotations_anywhere"] == 0]
    some_not_subject = [
        r["pmid"] for r in rows
        if r["annotations_anywhere"] > 0 and r["annotations_on_ARFGEF1"] == "0"
    ]
    on_subj = [r for r in rows
               if r["annotations_on_ARFGEF1"] not in {"0", "UNKNOWN (paginated)"}]
    # Derive the totals independently and require them to partition the set,
    # so a parsing change cannot quietly shrink one bucket into another.
    unknown = [r for r in rows if r["annotations_on_ARFGEF1"] == "UNKNOWN (paginated)"]
    assert len(zero) + len(some_not_subject) + len(on_subj) + len(unknown) == len(rows), (
        "coverage buckets do not partition the reference set"
    )

    print(f"affinage citations: {len(aff)}; UniProt RX PubMed: {len(up)}; union: {len(union)}")
    print(f"references with ZERO GO annotations anywhere in GOA: {len(zero)}")
    for p in zero:
        print(f"    {p}")
    print(f"references annotating other genes but not ARFGEF1: {len(some_not_subject)} "
          f"{some_not_subject}")
    print(f"references annotating ARFGEF1: {len(on_subj)} "
          f"{[r['pmid'] for r in on_subj]}")
    print(f"references too large to attribute (paginated): {len(unknown)} "
          f"{[r['pmid'] for r in unknown]}")

    # The union above mixes functional papers with genome/proteomics surveys that
    # would never yield a GO annotation (UniProt cites them for MOD_RES and
    # VARIANT features). Restrict to the affinage set, which is functional by
    # construction, so the coverage figure is not inflated by those.
    aff_rows = [r for r in rows if r["in_affinage"] == "True"]
    a_zero = [r["pmid"] for r in aff_rows if r["annotations_anywhere"] == 0]
    a_other = [r["pmid"] for r in aff_rows
               if r["annotations_anywhere"] > 0 and r["annotations_on_ARFGEF1"] == "0"]
    a_subj = [r["pmid"] for r in aff_rows
              if r["annotations_on_ARFGEF1"] not in {"0", "UNKNOWN (paginated)"}]
    assert len(a_zero) + len(a_other) + len(a_subj) == len(aff_rows), (
        "affinage buckets do not partition"
    )
    print(f"\nAffinage-cited functional papers: {len(aff_rows)}")
    print(f"  annotating ARFGEF1:            {len(a_subj)} {a_subj}")
    print(f"  annotating only other genes:   {len(a_other)} {a_other}")
    print(f"  no GO annotation anywhere:     {len(a_zero)} {a_zero}")


if __name__ == "__main__":
    main()
