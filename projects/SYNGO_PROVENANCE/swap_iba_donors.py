"""Check whether the swapped GABA receptor seeds are PAINT donors for any IBA.

A PAINT IBA row lists its donor genes in WITH/FROM by model-organism database
identifier (MGI, RGD, ...), not by UniProt accession, so a WITH/FROM search for
the seed's UniProt accession finds nothing even when the gene is a donor. This
script, for each swapped seed (gene product, paper) in
``data/gaba_receptor_swaps-verdicts.yaml``:

1. looks up the gene's MGI/RGD identifier from its UniProt record;
2. lists the GO terms SynGO annotated to it from that paper;
3. for each term, counts the IBA rows on the term (any species) whose WITH/FROM
   names that identifier, and lists the donor's other experimental support for
   the same term, i.e. whether the donor would still qualify without the swap.

Being a donor does not make an IBA wrong: the PAINT node is placed from all
donors, and the term may be true of the family for other reasons. The output
says which IBAs a corrected seed would remove one donor from. Output:
``data/gaba_receptor_swaps-iba.yaml``.

    python projects/SYNGO_PROVENANCE/swap_iba_donors.py
"""
from __future__ import annotations

import datetime
import json
import urllib.request
from pathlib import Path

import yaml

from gaba_receptor_swaps import quickgo

ROOT = Path(__file__).resolve().parents[2]
VERDICTS = ROOT / "projects/SYNGO_PROVENANCE/data/gaba_receptor_swaps-verdicts.yaml"
OUT = ROOT / "projects/SYNGO_PROVENANCE/data/gaba_receptor_swaps-iba.yaml"
EXPERIMENTAL = {"EXP", "IDA", "IMP", "IGI", "IPI", "IEP", "HDA", "HMP", "HTP", "HGI", "HEP"}
IBA_ECO = "ECO:0000318"


def mod_id(accession: str) -> tuple[str, str]:
    """Return (database, identifier) for the MGI or RGD cross-reference of a UniProt entry."""
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.json?fields=xref_mgi,xref_rgd"
    with urllib.request.urlopen(url, timeout=60) as resp:
        refs = json.load(resp).get("uniProtKBCrossReferences", [])
    for ref in refs:
        if ref["database"] in ("MGI", "RGD"):
            return ref["database"], ref["id"]  # QuickGO keeps the MGI: prefix in the id
    raise ValueError(f"No MGI or RGD cross-reference on UniProtKB:{accession}")


def names_donor(row: dict, db: str, ident: str) -> bool:
    """True if an annotation's WITH/FROM names the given database identifier."""
    return any(x["db"] == db and x["id"] == ident
               for w in row.get("withFrom") or [] for x in w["connectedXrefs"])


def seeds() -> list[tuple[str, str]]:
    """(UniProt accession, PMID) for every swapped seed in the verdicts file."""
    out = []
    for paper in yaml.safe_load(VERDICTS.read_text())["papers"]:
        for acc in paper.get("seed_accessions", []):
            out.append((acc, paper["reference"]))
    return out


def main() -> None:
    """Write the IBA donor check for every swapped seed."""
    records = []
    iba_cache: dict[str, list[dict]] = {}
    for acc, ref in seeds():
        db, ident = mod_id(acc)
        seed_rows = [r for r in quickgo(geneProductId=acc, includeFields="goName")
                     if r["reference"] == ref and r["assignedBy"] == "SynGO"]
        terms = []
        for go_id in sorted({r["goId"] for r in seed_rows}):
            if go_id not in iba_cache:
                iba_cache[go_id] = quickgo(goId=go_id, goUsage="exact", evidenceCode=IBA_ECO,
                                           evidenceCodeUsage="exact")
            fed = [r for r in iba_cache[go_id] if names_donor(r, db, ident)]
            other = sorted({f"{r['goEvidence']} {r['reference']}"
                            for r in quickgo(geneProductId=acc, goId=go_id, goUsage="exact")
                            if r["goEvidence"] in EXPERIMENTAL and r["reference"] != ref})
            terms.append({
                "go_id": go_id,
                "go_name": seed_rows[[r["goId"] for r in seed_rows].index(go_id)]["goName"],
                "iba_rows_on_term": len(iba_cache[go_id]),
                "iba_rows_naming_donor": len(fed),
                "paint_nodes": sorted({x["id"] for r in fed for w in r["withFrom"]
                                       for x in w["connectedXrefs"] if x["db"] == "PANTHER"}),
                "donor_other_experimental_support": other,
            })
        donor = ident if ident.startswith(f"{db}:") else f"{db}:{ident}"
        records.append({"seed": f"UniProtKB:{acc}", "donor_id": donor, "reference": ref,
                        "terms": terms})
    OUT.write_text(yaml.safe_dump({"retrieved": datetime.date.today().isoformat(), "seeds": records},
                                  sort_keys=False, allow_unicode=True, width=100))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
