"""Find the putative TIR-like catalytic Glu of DUF4062 in CP088958.1_900 (Q31PW6).

Osinski et al. 2026 (PMID:42146377) report a conserved Glu in DUF4062 (E97 in
K. pneumoniae Swarozyc) that is required for NAD+ hydrolysis. Without their
alignment, this script estimates per-position conservation directly: it downloads
bacterial DUF4062 (IPR025139) proteins of 200-450 aa from UniProtKB (sampled, at
most --max), aligns each globally to the query (BLOSUM62, gap -11/-1), and for every
query position in the DUF4062 region reports the fraction of homologs carrying the
same residue. Homologs below --min-id identity over the DUF4062 region are dropped.

Writes $BERIL_RUN_DIR/results.json and tables/position_conservation.tsv.
"""
import argparse
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices


def fetch_fasta(query, size):
    url = "https://rest.uniprot.org/uniprotkb/search?" + urllib.parse.urlencode(
        {"query": query, "format": "fasta", "size": size})
    with urllib.request.urlopen(url, timeout=120) as r:
        txt = r.read().decode()
    seqs, k = {}, None
    for line in txt.splitlines():
        if line.startswith(">"):
            k = line[1:].split()[0]
            seqs[k] = ""
        elif k:
            seqs[k] += line.strip()
    return seqs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fasta", type=Path, required=True)
    ap.add_argument("--region-end", type=int, default=146, help="end of DUF4062 region in query (UniProt FT 6..146)")
    ap.add_argument("--max", type=int, default=400)
    ap.add_argument("--min-id", type=float, default=0.20)
    a = ap.parse_args()
    out = Path(os.environ["BERIL_RUN_DIR"])
    (out / "tables").mkdir(parents=True, exist_ok=True)

    q = "".join(l.strip() for l in a.fasta.read_text().splitlines() if not l.startswith(">"))
    seqs = fetch_fasta("xref:interpro-IPR025139 AND taxonomy_id:2 AND length:[200 TO 450]", a.max)
    seqs.pop("tr|Q31PW6|Q31PW6_SYNE7", None)

    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score, al.mode = -11, -1, "global"

    L = a.region_end
    same = [0] * (L + 1)
    covered = [0] * (L + 1)
    used = 0
    for acc, s in seqs.items():
        aln = al.align(q, s)[0]
        cols = {}
        for (qs, qe), (ss, se) in zip(*aln.aligned):
            for i in range(qe - qs):
                cols[qs + i + 1] = s[ss + i]
        reg = [p for p in range(1, L + 1) if p in cols]
        if not reg:
            continue
        ident = sum(cols[p] == q[p - 1] for p in reg) / L
        if ident < a.min_id:
            continue
        used += 1
        for p in reg:
            covered[p] += 1
            same[p] += cols[p] == q[p - 1]

    rows = []
    for p in range(1, L + 1):
        rows.append({"pos": p, "aa": q[p - 1], "covered": covered[p],
                     "frac_identical": same[p] / used if used else 0.0})
    with open(out / "tables" / "position_conservation.tsv", "w") as f:
        f.write("pos\taa\tcovered\tfrac_identical\n")
        for r in rows:
            f.write(f"{r['pos']}\t{r['aa']}\t{r['covered']}\t{r['frac_identical']:.3f}\n")
    top = sorted(rows, key=lambda r: -r["frac_identical"])[:15]
    glu = sorted([r for r in rows if r["aa"] == "E"], key=lambda r: -r["frac_identical"])
    res = {"homologs_downloaded": len(seqs), "homologs_used": used, "min_id": a.min_id,
           "top_conserved_positions": top, "glu_positions_ranked": glu}
    (out / "results.json").write_text(json.dumps(res, indent=1))
    print(json.dumps({k: res[k] for k in ("homologs_downloaded", "homologs_used")}))
    print("top:", [(r["pos"], r["aa"], round(r["frac_identical"], 2)) for r in top])
    print("glu:", [(r["pos"], round(r["frac_identical"], 2)) for r in glu])
    print("context of top Glu:", glu[0]["pos"], q[glu[0]["pos"] - 8: glu[0]["pos"] + 7])


if __name__ == "__main__":
    main()
