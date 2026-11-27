# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Place TRF2 (G4N2B2, MGG_04853) among PANTHER PTHR24324 relatives.

Fetches sequences and PANTHER/HOGENOM/OrthoDB/Pfam cross-references from UniProt REST,
computes global full-length and homeodomain-window identities (Biopython PairwiseAligner,
BLOSUM62, gap open -10, extend -0.5), reports the homeodomain helix-3 DNA-recognition
positions (canonical homeodomain numbering 47, 50, 51, 53 within the UniProt DNA_BIND window),
and counts PF24818 proteins in the P. oryzae 70-15 proteome.
Run: uv run --script compare_relatives.py > RESULTS.txt
"""
import re
import requests
from Bio import Align
from Bio.Align import substitution_matrices

QUERY = "G4N2B2"
OTHERS = ["Q7S7W0", "C8VLD7", "Q99160", "Q10328", "P07269", "P40923", "Q03014", "Q04116", "P34161"]


def fetch(acc: str) -> dict:
    txt = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.txt", timeout=60).text
    seq = "".join(txt.split("\nSQ ")[1].split("\n", 1)[1].split()).replace("//", "")
    gn = re.search(r"^GN   (?:Name|ORFNames)=([^;{ ]+)", txt, re.M)
    os_ = re.search(r"^OS   (.+)$", txt, re.M).group(1)
    xrefs = re.findall(r"^DR   (PANTHER|HOGENOM|OrthoDB|Pfam); ([^;]+);", txt, re.M)
    hd = re.search(r"^FT   DNA_BIND\s+(\d+)\.\.(\d+)\nFT\s+/note=\"Homeobox\"", txt, re.M)
    return {"acc": acc, "gene": gn.group(1) if gn else "", "org": os_, "seq": seq,
            "xrefs": xrefs, "hd": (int(hd.group(1)), int(hd.group(2))) if hd else None}


def align(a: str, b: str):
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    return aligner.align(a, b)[0]


def identity(a: str, b: str) -> float:
    aln = align(a, b)
    ident = sum(1 for x, y in zip(aln[0], aln[1]) if x == y and x != "-")
    return 100.0 * ident / min(len(a), len(b))


def main() -> None:
    q = fetch(QUERY)
    s, e = q["hd"]
    qhd = q["seq"][s - 1 : e]
    print(f"query {q['acc']} {q['gene']} len={len(q['seq'])} homeodomain={q['hd']}")
    print(f"query xrefs: {q['xrefs']}")
    print(f"query homeodomain window: {qhd}")
    # UniProt DNA_BIND starts at canonical homeodomain position 1 (PROSITE PS50071 profile)
    for pos in (47, 50, 51, 53):
        print(f"homeodomain position {pos}: {qhd[pos - 1]} (protein residue {s + pos - 1})")
    m = re.search(r"WF.N.R", qhd)
    print(f"WFxNxR motif in homeodomain: {m.group(0) if m else None} at protein residue {s + m.start() if m else None}")
    print("acc\tgene\tlength\tfull_id_pct_of_shorter\thd_id_pct\tshares_HOGENOM\tshares_OrthoDB\thas_PF24818\tPANTHER\torganism")
    qhog = {v for k, v in q["xrefs"] if k == "HOGENOM"}
    qodb = {v for k, v in q["xrefs"] if k == "OrthoDB"}
    for acc in OTHERS:
        o = fetch(acc)
        full = identity(q["seq"], o["seq"])
        hdid = identity(qhd, o["seq"][o["hd"][0] - 1 : o["hd"][1]]) if o["hd"] else float("nan")
        hog = bool(qhog & {v for k, v in o["xrefs"] if k == "HOGENOM"})
        odb = bool(qodb & {v for k, v in o["xrefs"] if k == "OrthoDB"})
        pf = any(k == "Pfam" and v == "PF24818" for k, v in o["xrefs"])
        pan = ";".join(v for k, v in o["xrefs"] if k == "PANTHER" and ":SF" in v)
        print(f"{acc}\t{o['gene']}\t{len(o['seq'])}\t{full:.1f}\t{hdid:.1f}\t{hog}\t{odb}\t{pf}\t{pan}\t{o['org']}")
    r = requests.get("https://rest.uniprot.org/uniprotkb/search",
                     params={"query": "xref:pfam-PF24818 AND organism_id:242507", "fields": "accession,gene_names", "format": "tsv"},
                     timeout=60)
    print("PF24818 proteins in P. oryzae 70-15 (taxon 242507):")
    print(r.text.strip())


if __name__ == "__main__":
    main()
