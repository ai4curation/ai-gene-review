"""Download the panel's UniProt entries and record what UniProt itself calls them.

The identity of every accession is taken from the downloaded record, never from the
label written in panel.py -- a wrong accession with a plausible label is exactly the
failure this check exists to make visible, so `verify_panel.py` compares the two.
"""

import json
import pathlib
import time
import urllib.request

from panel import PANEL

HERE = pathlib.Path(__file__).parent
SEQ_DIR = HERE / "sequences"
META = HERE / "panel_identities.json"


def fetch(accession: str) -> dict:
    base = f"https://rest.uniprot.org/uniprotkb/{accession}"
    with urllib.request.urlopen(base + ".fasta", timeout=120) as fh:
        fasta = fh.read().decode()
    with urllib.request.urlopen(base + ".json", timeout=120) as fh:
        rec = json.load(fh)
    seq = "".join(line.strip() for line in fasta.splitlines()[1:])
    genes = [g.get("geneName", {}).get("value") for g in rec.get("genes", [])]
    dh = [
        {"start": f["location"]["start"]["value"], "end": f["location"]["end"]["value"]}
        for f in rec.get("features", [])
        if f.get("type") == "Domain" and "DH" in (f.get("description") or "")
    ]
    return {
        "accession": rec["primaryAccession"],
        "uniprot_id": rec["uniProtkbId"],
        "gene_names": [g for g in genes if g],
        "protein_name": rec.get("proteinDescription", {})
        .get("recommendedName", {})
        .get("fullName", {})
        .get("value"),
        "organism": rec.get("organism", {}).get("scientificName"),
        "length": rec["sequence"]["length"],
        "sequence_version": rec.get("entryAudit", {}).get("sequenceVersion"),
        "dh_domains": dh,
        "sequence": seq,
    }


def main() -> None:
    SEQ_DIR.mkdir(exist_ok=True)
    out = {}
    for acc in PANEL:
        rec = fetch(acc)
        (SEQ_DIR / f"{acc}.fasta").write_text(f">{acc} {rec['uniprot_id']}\n{rec['sequence']}\n")
        out[acc] = {k: v for k, v in rec.items() if k != "sequence"}
        print(
            f"{acc}  {rec['uniprot_id']:<16} {rec['organism']:<24} "
            f"len={rec['length']:<5} genes={','.join(rec['gene_names'])} DH={rec['dh_domains']}"
        )
        time.sleep(0.3)
    META.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(f"\nwrote {META}")


if __name__ == "__main__":
    main()
