# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Pairwise comparison of KAL-1 (Q7S7W0) with PANTHER PTHR24324 members.

Fetches sequences and PANTHER/HOGENOM/OrthoDB/Pfam cross-references from UniProt,
then computes global (full-length) and homeodomain-window identities with
Biopython's PairwiseAligner (BLOSUM62, gap open -10, extend -0.5).
Run: uv run --script compare_relatives_rereview.py > RESULTS-rereview.txt
"""
import re
import requests
from Bio import Align
from Bio.Align import substitution_matrices

QUERY = "Q7S7W0"
OTHERS = ["G4N2B2", "C8VLD7", "Q99160", "Q10328", "P07269", "P40923", "Q03014", "Q04116", "P34161"]


def fetch(acc: str) -> dict:
    txt = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.txt", timeout=60).text
    seq = "".join(txt.split("\nSQ ")[1].split("\n", 1)[1].split()).replace("//", "")
    gn = re.search(r"^GN   Name=([^;{ ]+)", txt, re.M)
    os_ = re.search(r"^OS   (.+)$", txt, re.M).group(1)
    xrefs = re.findall(r"^DR   (PANTHER|HOGENOM|OrthoDB|Pfam); ([^;]+);", txt, re.M)
    hd = re.search(r"^FT   DNA_BIND\s+(\d+)\.\.(\d+)\nFT\s+/note=\"Homeobox\"", txt, re.M)
    return {
        "acc": acc,
        "gene": gn.group(1) if gn else "",
        "org": os_,
        "seq": seq,
        "xrefs": xrefs,
        "hd": (int(hd.group(1)), int(hd.group(2))) if hd else None,
    }


def identity(a: str, b: str) -> tuple[float, int]:
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    aln = aligner.align(a, b)[0]
    ident = sum(1 for x, y in zip(aln[0], aln[1]) if x == y and x != "-")
    cols = sum(1 for x, y in zip(aln[0], aln[1]) if x != "-" and y != "-")
    return 100.0 * ident / min(len(a), len(b)), cols


def main() -> None:
    q = fetch(QUERY)
    print(f"query {q['acc']} {q['gene']} len={len(q['seq'])} homeodomain={q['hd']}")
    print(f"query xrefs: {q['xrefs']}")
    qhd = q["seq"][q["hd"][0] - 1 : q["hd"][1]]
    print("acc\tgene\tlength\tfull_id_pct_of_shorter\thd_id_pct\tshares_HOGENOM\tshares_OrthoDB\thas_PF24818\tPANTHER\torganism")
    qhog = {v for k, v in q["xrefs"] if k == "HOGENOM"}
    qodb = {v for k, v in q["xrefs"] if k == "OrthoDB"}
    for acc in OTHERS:
        o = fetch(acc)
        full, _ = identity(q["seq"], o["seq"])
        hd_pct = ""
        if o["hd"]:
            ohd = o["seq"][o["hd"][0] - 1 : o["hd"][1]]
            hd_pct = f"{identity(qhd, ohd)[0]:.1f}"
        hog = bool(qhog & {v for k, v in o["xrefs"] if k == "HOGENOM"})
        odb = bool(qodb & {v for k, v in o["xrefs"] if k == "OrthoDB"})
        pf = any(k == "Pfam" and v == "PF24818" for k, v in o["xrefs"])
        panther = ",".join(v for k, v in o["xrefs"] if k == "PANTHER")
        print(f"{acc}\t{o['gene']}\t{len(o['seq'])}\t{full:.1f}\t{hd_pct}\t{hog}\t{odb}\t{pf}\t{panther}\t{o['org']}")


if __name__ == "__main__":
    main()
