# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Locate the Spo2 (C6Y4C2) sequence within Vps1302 (O42926) and list the
InterPro/Pfam/PANTHER signatures of both proteins, reporting whether any
Vps1302 signature overlaps the Spo2-identical segment.

Run: uv run --script compare_vps1302_rereview.py
"""

import json
import urllib.request

UNIPROT = "https://rest.uniprot.org/uniprotkb/{acc}.fasta"
INTERPRO = "https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/{acc}/?page_size=100"


def fasta_seq(acc: str) -> str:
    with urllib.request.urlopen(UNIPROT.format(acc=acc)) as r:
        lines = r.read().decode().splitlines()
    return "".join(lines[1:])


def signatures(acc: str) -> list[tuple[str, str, str, int, int]]:
    with urllib.request.urlopen(INTERPRO.format(acc=acc)) as r:
        body = r.read().decode()
    if not body.strip():
        return []
    out = []
    for res in json.loads(body)["results"]:
        md = res["metadata"]
        for p in res["proteins"]:
            for loc in p["entry_protein_locations"]:
                for f in loc["fragments"]:
                    out.append((md["accession"], md["source_database"], md["name"], f["start"], f["end"]))
    return out


def main() -> None:
    spo2 = fasta_seq("C6Y4C2")
    vps = fasta_seq("O42926")
    pos = vps.find(spo2)
    print(f"Spo2 length: {len(spo2)}; Vps1302 length: {len(vps)}")
    if pos < 0:
        print("Spo2 sequence is NOT an exact substring of Vps1302")
        return
    start, end = pos + 1, pos + len(spo2)
    print(f"Spo2 is identical to Vps1302 residues {start}-{end}")
    print(f"Vps1302 residue preceding the Spo2 Met: {vps[pos - 1]}{pos}")
    print("\nSpo2 (C6Y4C2) signatures:")
    sp = signatures("C6Y4C2")
    print("  none" if not sp else "\n".join(f"  {s}" for s in sp))
    print("\nVps1302 (O42926) signatures (overlap with Spo2 segment marked):")
    for acc, db, name, s, e in sorted(signatures("O42926"), key=lambda x: x[3]):
        ov = max(0, min(e, end) - max(s, start) + 1)
        print(f"  {acc}\t{db}\t{s}-{e}\toverlap_with_spo2={ov}\t{name}")


if __name__ == "__main__":
    main()
