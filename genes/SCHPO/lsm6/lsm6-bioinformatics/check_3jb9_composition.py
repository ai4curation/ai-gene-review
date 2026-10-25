# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check whether S. pombe Lsm6 (Q9UUI1) is a modelled chain of the Yan et al. 2015
S. pombe spliceosome structure (PDB 3JB9, PMID:26292707), and which gene products carry
GO annotations citing PMID:26292707.

Queries live UniProt REST (PDB cross-references) and QuickGO. Prints results; nothing is
hardcoded except the query identifiers.
"""

import json
import urllib.request

UNIPROT = (
    "https://rest.uniprot.org/uniprotkb/search?query=xref:pdb-3JB9"
    "&fields=accession,gene_names,protein_name&format=tsv&size=200"
)
QUICKGO = (
    "https://www.ebi.ac.uk/QuickGO/services/annotation/search?"
    "geneProductId={acc}&reference=PMID:26292707&limit=100"
)
QUERY_ACCS = {
    "Q9UUI1": "lsm6",
    "O59734": "smf1 (SmF, same PANTHER family PTHR11021)",
    "Q10163": "smb1",
    "O74966": "smg1",
    "Q9USZ3": "sme1",
}


def fetch(url: str, accept: str | None = None) -> str:
    req = urllib.request.Request(url)
    if accept:
        req.add_header("Accept", accept)
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode()


def main() -> None:
    rows = fetch(UNIPROT).strip().split("\n")
    members = rows[1:]
    print(f"## UniProt entries cross-referencing PDB 3JB9: {len(members)}")
    for r in members:
        print("  " + r)
    accs = {r.split("\t")[0] for r in members}
    print(f"\nQ9UUI1 (lsm6) in 3JB9: {'Q9UUI1' in accs}")
    lsm_like = [r for r in members if "lsm" in r.lower()]
    print(f"Lsm-named entries in 3JB9: {len(lsm_like)}")
    print("\n## QuickGO annotations citing PMID:26292707")
    for acc, label in QUERY_ACCS.items():
        data = json.loads(fetch(QUICKGO.format(acc=acc), "application/json"))
        res = data["results"]
        print(f"{acc} {label}: {len(res)} annotation(s)")
        for a in res:
            print(f"    {a['qualifier']} {a['goId']} {a['goEvidence']} {a['assignedBy']}")


if __name__ == "__main__":
    main()
