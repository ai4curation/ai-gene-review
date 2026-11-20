#!/usr/bin/env python3
"""Reproduce the two pipeline-level upstream findings from CACAO batch 3.

Both were found while reviewing CACAO annotations but neither is CACAO's:
each is a single mis-stated source annotation amplified by an automatic
pipeline across thousands of proteins.

Check 1 -- InterPro2GO and GO:0019685 "photosynthesis, dark reaction".
  The term is the carbon-fixation grouping term (its is_a children are the
  Calvin cycle, C4 and CAM photosynthesis) and its definition describes CO2
  reduction to sugar. InterPro2GO maps four *light-independent*
  (bacterio)chlorophyll biosynthesis entries to it, apparently reading the
  label "dark reaction" as "light-independent". Every GOA annotation on the
  term comes from that mapping.

Check 2 -- PANTHER/TreeGrafter and GO:0004029 aldehyde dehydrogenase (NAD+).
  One IDA on the yeast protein YLL056C (Q12177) asserts GO:0004029, but its
  cited paper (PMID:28265724) reports an NADH-dependent aldehyde *reductase*
  -- aldehyde -> alcohol, not aldehyde -> carboxylate. PAINT and TreeGrafter
  each propagate that term across PTHR48079, a family of NAD(P)-dependent
  epimerases/dehydratases.

Run:
    uv run python projects/CACAO/scripts/upstream_checks.py

Network only; writes nothing. Counts move as GOA is rebuilt, so the script
prints what it finds rather than asserting fixed numbers.
"""

from __future__ import annotations

import csv
import io
import sys
import urllib.request

QUICKGO = "https://www.ebi.ac.uk/QuickGO/services"
INTERPRO2GO = "https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/interpro2go"
UNIPROT = "https://rest.uniprot.org/uniprotkb"

DARK_REACTION = "GO:0019685"
ALDH = "GO:0004029"
SEED = "Q12177"
TREEGRAFTER_NODE = "PANTHER:PTN005180820"
PAINT_NODE = "PANTHER:PTN002449572"


def get(url: str, accept: str = "application/json") -> bytes:
    """Fetch a URL with an explicit Accept header."""
    req = urllib.request.Request(url, headers={"Accept": accept})
    with urllib.request.urlopen(req, timeout=120) as fh:
        return fh.read()


def tsv(url: str) -> list[dict[str, str]]:
    """Fetch a QuickGO download as a list of row dicts."""
    text = get(url, "text/tsv").decode("utf-8")
    return list(csv.DictReader(io.StringIO(text), delimiter="\t"))


def annotations(**params: str) -> list[dict[str, str]]:
    """Download annotation rows matching the given QuickGO parameters."""
    params.setdefault("downloadLimit", "5000")
    query = "&".join(f"{k}={v}" for k, v in params.items())
    return tsv(f"{QUICKGO}/annotation/downloadSearch?{query}")


def check_interpro2go() -> None:
    """Show which InterPro entries map to GO:0019685 and who uses the term."""
    print("=" * 72)
    print("CHECK 1: InterPro2GO -> GO:0019685 photosynthesis, dark reaction")
    print("=" * 72)

    mappings = get(INTERPRO2GO, "text/plain").decode("utf-8").splitlines()
    hits = [ln for ln in mappings if ln.endswith(DARK_REACTION)]
    print(f"\ninterpro2go lines mapping to {DARK_REACTION}: {len(hits)}")
    for line in hits:
        entry = line.split()[0].replace("InterPro:", "")
        name = line.split(" > ")[0].split(" ", 1)[1]
        print(f"  {entry}  {name}")

    print("\nEvery one is a light-independent (bacterio)chlorophyll entry.")
    print("Each already carries its correct terms, so the fix is deletion:")
    for line in mappings:
        for entry in (ln.split()[0] for ln in hits):
            if line.startswith(entry + " "):
                go_id = line.rsplit(";", 1)[-1].strip()
                mark = "  <-- REMOVE" if go_id == DARK_REACTION else ""
                label = line.split(" > GO:")[1].rsplit(" ;", 1)[0]
                print(f"  {entry.replace('InterPro:', '')}  {go_id}  {label}{mark}")

    rows = annotations(goId=DARK_REACTION, goUsage="exact")
    refs = {r["REFERENCE"] for r in rows}
    by = {r["ASSIGNED BY"] for r in rows}
    print(f"\nGOA annotations on {DARK_REACTION}: {len(rows)}")
    print(f"  distinct references : {sorted(refs)}")
    print(f"  distinct assigned-by: {sorted(by)}")
    if len(refs) == 1 and len(by) == 1:
        print("  -> the term has no use in GOA independent of this mapping.")


def protein_facts(accession: str) -> tuple[str, list[str]]:
    """Return a protein's name and its Pfam/PANTHER cross-references."""
    import json

    data = json.loads(get(f"{UNIPROT}/{accession}.json?fields=protein_name,"
                          "xref_pfam,xref_panther"))
    desc = data.get("proteinDescription", {})
    named = desc.get("recommendedName") or (desc.get("submissionNames") or [{}])[0]
    name = (named or {}).get("fullName", {}).get("value", "?")
    xrefs = [
        x["id"]
        for x in data.get("uniProtKBCrossReferences", [])
        if x["database"] in ("Pfam", "PANTHER")
    ]
    return name, xrefs


def check_panther() -> None:
    """Show the seed annotation for GO:0004029 and how far it propagates."""
    print()
    print("=" * 72)
    print("CHECK 2: PANTHER/TreeGrafter -> GO:0004029 aldehyde dehydrogenase")
    print("=" * 72)

    seed_rows = annotations(geneProductId=SEED, downloadLimit="50")
    print(f"\nSeed protein {SEED} (YLL056C), all GOA rows:")
    for r in seed_rows:
        print(f"  {r['GO TERM']}  {r['GO EVIDENCE CODE']:4s} {r['REFERENCE']:22s}"
              f" {r['ASSIGNED BY']}")
    print("\n  Its GO:0004029 IDA cites PMID:28265724, whose title is")
    print("  'YLL056C ... encodes a novel protein with aldehyde REDUCTASE")
    print("  activity' and whose abstract says the protein is 'an NADH-dependent")
    print("  aldehyde reductase, which can reduce at least seven aldehyde")
    print("  compounds'. GO:0004029 is the opposite reaction: aldehyde + H2O +")
    print("  NAD+ = carboxylate. The product is an acid, not an alcohol.")

    grafted = annotations(withFrom=TREEGRAFTER_NODE)
    by_term: dict[str, int] = {}
    for r in grafted:
        by_term[r["GO TERM"]] = by_term.get(r["GO TERM"], 0) + 1
    taxa = {r["TAXON ID"] for r in grafted}
    print(f"\nTreeGrafter node {TREEGRAFTER_NODE}:")
    for term, n in sorted(by_term.items()):
        print(f"  {term}: {n} proteins")
    print(f"  spanning {len(taxa)} taxa")

    iba = annotations(goId=ALDH, goUsage="exact", evidenceCode="ECO:0000318")
    from_node = [r for r in iba if PAINT_NODE in r["WITH/FROM"]]
    print(f"\nPAINT node {PAINT_NODE}: {len(from_node)} IBA rows")
    if from_node:
        donors = from_node[0]["WITH/FROM"]
        print(f"  WITH/FROM: {donors}")
        print("  The single donor is the seed itself. Donor count is NOT the")
        print("  argument here -- a one-donor node can be sound. The argument is")
        print("  that the donor's own term is the wrong reaction, so everything")
        print("  inheriting from the node inherits that error.")

    print("\nWhat the recipients actually are:")
    for acc in [r["GENE PRODUCT ID"] for r in from_node[:4]]:
        name, xrefs = protein_facts(acc)
        print(f"  {acc}  {name}  {xrefs}")
    print("  PF01370 is the NAD-dependent epimerase/dehydratase family, an")
    print("  extended-SDR Rossmann fold. The real ALDH superfamily is PF00171 /")
    print("  PTHR11699, which has its own well-seeded PAINT nodes.")

    total = by_term.get(ALDH, 0) + len(from_node)
    print(f"\nRows traceable to the one mis-termed IDA: {total}")


def main() -> int:
    """Run both checks."""
    check_interpro2go()
    check_panther()
    return 0


if __name__ == "__main__":
    sys.exit(main())
