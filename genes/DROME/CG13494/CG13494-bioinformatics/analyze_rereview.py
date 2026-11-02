"""Re-review sequence analysis for Drosophila CG13494 (Q8MZA7).

Reproducible, stdlib-only (plus HMMER on PATH):
  1. composition of the segments either side of the Phobius TM helix (37-61)
  2. InterPro member-database matches for Q8MZA7 (HTTP 204 = none)
  3. hmmsearch of the Pfam CYSTM HMM (PF12734), the closest known
     TM + cysteine-rich module, against Q8MZA7
  4. OMA HOG depth and orthologs (taxonomic breadth)

Run: python3 analyze_rereview.py
"""

import gzip
import json
import subprocess
import tempfile
import urllib.request
from collections import Counter
from pathlib import Path

ACC = "Q8MZA7"
HERE = Path(__file__).parent
UNIPROT = HERE.parent / "CG13494-uniprot.txt"


def read_sequence(path: Path) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, ln in enumerate(lines) if ln.startswith("SQ "))
    seq = []
    for ln in lines[start + 1 :]:
        if ln.startswith("//"):
            break
        seq.append(ln.replace(" ", ""))
    return "".join(seq)


def composition(seg: str) -> dict:
    c = Counter(seg)
    n = len(seg)
    top = {aa: round(100 * k / n, 1) for aa, k in c.most_common(5)}
    return {"length": n, "top_residues_pct": top}


def fetch(url: str) -> tuple[int, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review/1.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.status, r.read()


def main() -> None:
    seq = read_sequence(UNIPROT)
    out: dict = {"accession": ACC, "length": len(seq)}
    out["segments"] = {
        "Nterm_1_36": composition(seq[0:36]),
        "TM_37_61": composition(seq[36:61]),
        "Cterm_62_120": composition(seq[61:]),
    }
    out["cys_count"] = seq.count("C")
    out["gly_count"] = seq.count("G")

    status, body = fetch(
        f"https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/{ACC}/"
    )
    if status == 204 or not body:
        out["interpro_matches"] = []
    else:
        out["interpro_matches"] = [
            (r["metadata"]["accession"], r["metadata"]["name"])
            for r in json.loads(body)["results"]
        ]

    _, hmm_gz = fetch(
        "https://www.ebi.ac.uk/interpro/api/entry/pfam/PF12734/?annotation=hmm"
    )
    with tempfile.TemporaryDirectory() as td:
        hmm = Path(td) / "cystm.hmm"
        hmm.write_bytes(gzip.decompress(hmm_gz))
        fa = Path(td) / "q.fa"
        fa.write_text(f">{ACC}\n{seq}\n")
        tbl = Path(td) / "tbl"
        subprocess.run(
            ["hmmsearch", "--max", "-E", "10", "--tblout", str(tbl), str(hmm), str(fa)],
            check=True,
            capture_output=True,
        )
        hits = [ln.split() for ln in tbl.read_text().splitlines() if not ln.startswith("#")]
        out["cystm_hmmsearch"] = [
            {"target": h[0], "evalue": float(h[4]), "score": float(h[5])} for h in hits
        ]

    _, prot = fetch(f"https://omabrowser.org/api/protein/{ACC}/")
    prot_j = json.loads(prot)
    out["oma_hog_id"] = prot_j.get("oma_hog_id")
    out["oma_hog_levels"] = prot_j.get("hog_levels")
    _, orth = fetch(f"https://omabrowser.org/api/protein/{ACC}/orthologs/")
    out["oma_orthologs"] = [
        (o.get("canonicalid"), o["species"]["species"], o.get("rel_type"))
        for o in json.loads(orth)
    ]
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
