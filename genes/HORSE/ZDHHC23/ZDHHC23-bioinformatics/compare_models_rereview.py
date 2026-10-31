"""Compare the horse ZDHHC23 gene models with reviewed mammalian ZDHHC23 orthologs.

Fetches sequences live from UniProt REST (stdlib only) and reports, per protein:
length, DHHC motif position, whether the C-terminal PDZ-binding motif -EDIV
(mapped as the NOS1-interaction region in rat Q76IC6, PMID:15105416) is present,
and the C-terminal tail after the shared "LCGLIVDT" anchor that ends the last
predicted transmembrane/juxtamembrane segment.

Run: uv run --no-project python compare_models_rereview.py > results-rereview.json
"""

import json
import re
import urllib.request

ACCESSIONS = {
    # benchmark accession (Ensembl canonical transcript ENSECAT00000105517)
    "A0A9L0T4E4": "horse",
    # other horse models of the same Ensembl gene ENSECAG00000014382
    "A0A3Q2KPV4": "horse",
    "F7CNX6": "horse",
    "A0A5F5Q1C7": "horse",
    "A0A9L0RVS6": "horse",
    "A0A9L0R7E2": "horse",
    "A0A9L0SCZ1": "horse",
    # reviewed orthologs (PANTHER PTHR22883:SF475)
    "Q8IYP9": "human",
    "Q5Y5T3": "mouse",
    "Q76IC6": "rat",
}
ANCHOR = "LCGLIVDT"


def fetch(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url) as fh:
        lines = fh.read().decode().splitlines()
    return "".join(line for line in lines if not line.startswith(">"))


def summarize(acc: str, species: str) -> dict:
    seq = fetch(acc)
    dhhc = [m.start() + 1 for m in re.finditer("DHHC", seq)]
    anchor = seq.find(ANCHOR)
    tail = seq[anchor + len(ANCHOR) :] if anchor >= 0 else None
    return {
        "accession": acc,
        "species": species,
        "length": len(seq),
        "dhhc_motif_start": dhhc,
        "active_site_cys": [p + 3 for p in dhhc],
        "anchor_end": anchor + len(ANCHOR) if anchor >= 0 else None,
        "c_terminal_tail": tail,
        "ends_with_EDIV": seq.endswith("EDIV"),
        "n_terminus": seq[:12],
    }


if __name__ == "__main__":
    print(json.dumps([summarize(a, s) for a, s in ACCESSIONS.items()], indent=2))
