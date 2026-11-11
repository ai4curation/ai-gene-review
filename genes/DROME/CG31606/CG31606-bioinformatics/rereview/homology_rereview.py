"""Independent homology/phylogenetic-distribution check for CG31606 (Q8IPG8).

Fetches: OMA HOG/orthologs, InterPro match counts, and runs EBI NCBI-BLAST
blastp of the full sequence against UniProtKB reference proteomes and Swiss-Prot.
Writes raw outputs next to this script. No results are hardcoded.
Usage: uv run --with requests python homology_rereview.py
"""
import json
import time
from pathlib import Path

import requests

ACC = "Q8IPG8"
OUT = Path(__file__).parent
EBI = "https://www.ebi.ac.uk/Tools/services/rest/ncbiblast"


def get_seq() -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{ACC}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def blast(seq: str, db: str) -> list[dict]:
    data = {
        "email": "cmungall@gmail.com",
        "program": "blastp",
        "stype": "protein",
        "database": db,
        "sequence": seq,
        "exp": "1e-3",
        "alignments": "250",
        "scores": "250",
    }
    job = requests.post(f"{EBI}/run", data=data, timeout=60).text
    while requests.get(f"{EBI}/status/{job}", timeout=60).text in ("RUNNING", "QUEUED"):
        time.sleep(15)
    res = requests.get(f"{EBI}/result/{job}/json", timeout=120).json()
    hits = []
    for h in res.get("hits", []):
        hsp = h["hit_hsps"][0]
        hits.append(
            {
                "acc": h["hit_acc"],
                "desc": h["hit_desc"],
                "os": h.get("hit_os"),
                "len": h["hit_len"],
                "evalue": hsp["hsp_expect"],
                "identity": hsp["hsp_identity"],
                "q_from": hsp["hsp_query_from"],
                "q_to": hsp["hsp_query_to"],
            }
        )
    return hits


def main() -> None:
    seq = get_seq()
    report: dict = {"accession": ACC, "length": len(seq)}
    prot = requests.get(f"https://omabrowser.org/api/protein/{ACC}/", timeout=60).json()
    report["oma_hog_id"] = prot.get("oma_hog_id")
    report["oma_hog_levels"] = prot.get("hog_levels")
    orth = requests.get(f"https://omabrowser.org/api/protein/{ACC}/orthologs/", timeout=60).json()
    report["oma_orthologs"] = [
        {"omaid": o["omaid"], "id": o["canonicalid"], "rel": o["rel_type"], "len": o["sequence_length"]}
        for o in orth
    ]
    ipr = requests.get(f"https://www.ebi.ac.uk/interpro/api/protein/uniprot/{ACC}", timeout=60).json()
    report["interpro_entry_count"] = ipr["metadata"]["counters"]["entries"]
    for db in ["uniprotkb_swissprot", "uniprotkb_eukaryota"]:
        report[f"blast_{db}"] = blast(seq, db)
    (OUT / "homology_rereview.json").write_text(json.dumps(report, indent=2))
    print(json.dumps({k: (v if not isinstance(v, list) else len(v)) for k, v in report.items()}, indent=1))
    for db in ["uniprotkb_swissprot", "uniprotkb_eukaryota"]:
        print("==", db)
        for h in report[f"blast_{db}"][:40]:
            print(h["acc"], h["os"], h["len"], h["evalue"], h["identity"], h["q_from"], h["q_to"], h["desc"][:60])


if __name__ == "__main__":
    main()
