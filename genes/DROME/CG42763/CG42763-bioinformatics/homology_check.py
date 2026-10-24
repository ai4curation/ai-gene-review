"""Independent homology / domain / phylogenetic-distribution check for CG42763 (M9MRG9).

Fetches: UniProt sequence and other entries for the FlyBase gene, InterPro entry
matches (integrated and member-database), OMA HOG/orthologs, and runs EBI NCBI-BLAST
blastp of the full sequence against UniProtKB/Swiss-Prot and UniProtKB Eukaryota.
Writes raw outputs next to this script. No results are hardcoded.
Usage: uv run --no-project --with requests python homology_check.py
"""
import json
import time
from pathlib import Path

import requests

ACC = "M9MRG9"
FBGN = "FBgn0261831"
OUT = Path(__file__).parent
EBI = "https://www.ebi.ac.uk/Tools/services/rest/ncbiblast"


def get_seq() -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{ACC}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def gene_entries() -> list[dict]:
    r = requests.get(
        "https://rest.uniprot.org/uniprotkb/search",
        params={"query": f"xref:flybase-{FBGN}", "fields": "accession,length,protein_name,reviewed", "format": "json"},
        timeout=60,
    )
    r.raise_for_status()
    return [
        {"acc": e["primaryAccession"], "len": e["sequence"]["length"], "type": e["entryType"]}
        for e in r.json()["results"]
    ]


def interpro_entries() -> list[dict]:
    r = requests.get(f"https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/{ACC}", timeout=60)
    if r.status_code == 204:
        return []
    r.raise_for_status()
    out = []
    for e in r.json()["results"]:
        md = e["metadata"]
        locs = []
        for p in e.get("proteins", []):
            for loc in p.get("entry_protein_locations") or []:
                for f in loc["fragments"]:
                    locs.append([f["start"], f["end"]])
        out.append(
            {
                "accession": md["accession"],
                "name": md["name"],
                "source_database": md["source_database"],
                "type": md["type"],
                "integrated": md.get("integrated"),
                "locations": locs,
            }
        )
    return out


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
    report: dict = {"accession": ACC, "length": len(seq), "c_terminus": seq[-17:]}
    report["n_cys_mature"] = seq[22:].count("C")
    report["gene_uniprot_entries"] = gene_entries()
    report["interpro_entries"] = interpro_entries()
    prot = requests.get(f"https://omabrowser.org/api/protein/{ACC}/", timeout=60)
    if prot.ok:
        pj = prot.json()
        report["oma_hog_id"] = pj.get("oma_hog_id")
        report["oma_hog_levels"] = pj.get("hog_levels")
        orth = requests.get(f"https://omabrowser.org/api/protein/{ACC}/orthologs/", timeout=60)
        report["oma_orthologs"] = [
            {"omaid": o["omaid"], "id": o["canonicalid"], "rel": o["rel_type"], "len": o["sequence_length"]}
            for o in (orth.json() if orth.ok else [])
        ]
    else:
        report["oma_status"] = prot.status_code
    for db in ["uniprotkb_swissprot", "uniprotkb_eukaryota"]:
        report[f"blast_{db}"] = blast(seq, db)
    (OUT / "homology_check.json").write_text(json.dumps(report, indent=2))
    print(json.dumps({k: (v if not isinstance(v, list) else len(v)) for k, v in report.items()}, indent=1))
    print("gene entries", report["gene_uniprot_entries"])
    for e in report["interpro_entries"]:
        print("IPR", e)
    print("OMA orthologs", report.get("oma_orthologs"))
    for db in ["uniprotkb_swissprot", "uniprotkb_eukaryota"]:
        print("==", db)
        for h in report[f"blast_{db}"][:60]:
            print(h["acc"], h["os"], h["len"], h["evalue"], h["identity"], h["q_from"], h["q_to"], h["desc"][:60])


if __name__ == "__main__":
    main()
