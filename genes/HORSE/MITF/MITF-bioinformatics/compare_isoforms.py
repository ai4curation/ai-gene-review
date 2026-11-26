# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests"]
# ///
"""Compare horse MITF F6ZKQ4 with all human MITF (O75030) isoforms and the other
horse MITF TrEMBL gene models. Prints global-alignment identity and gap structure.

Run: uv run --script compare_isoforms.py
"""
import io
import requests
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices


def fetch(url: str) -> list:
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    return list(SeqIO.parse(io.StringIO(r.text), "fasta"))


horse = fetch("https://rest.uniprot.org/uniprotkb/F6ZKQ4.fasta")[0]
human = fetch(
    "https://rest.uniprot.org/uniprotkb/search?query=accession:O75030&includeIsoform=true&format=fasta"
)
horse_models = fetch(
    "https://rest.uniprot.org/uniprotkb/search?query=gene:MITF+AND+organism_id:9796&format=fasta"
)

al = PairwiseAligner()
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score = -10
al.extend_gap_score = -0.5
al.mode = "global"


def compare(a, b):
    aln = al.align(str(a.seq), str(b.seq))[0]
    s1, s2 = aln[0], aln[1]
    ident = sum(1 for x, y in zip(s1, s2) if x == y and x != "-")
    paired = sum(1 for x, y in zip(s1, s2) if x != "-" and y != "-")
    gaps_in_horse = []
    pos_b = 0
    run = ""
    for x, y in zip(s1, s2):
        if y != "-":
            pos_b += 1
        if x == "-" and y != "-":
            run += y
        elif run:
            gaps_in_horse.append((pos_b - len(run), run))
            run = ""
    if run:
        gaps_in_horse.append((pos_b - len(run) + 1, run))
    return ident, paired, gaps_in_horse


print(f"query {horse.id} length {len(horse.seq)}")
print("\n== vs human O75030 isoforms ==")
for rec in human:
    ident, paired, gaps = compare(horse, rec)
    pct = 100 * ident / paired if paired else 0
    gtxt = "; ".join(f"{p}:{g[:12]}{'...' if len(g) > 12 else ''}({len(g)})" for p, g in gaps)
    print(f"{rec.id}\tlen={len(rec.seq)}\tident={ident}/{paired} ({pct:.1f}%)\tresidues_absent_in_horse={gtxt}")

print("\n== vs other horse MITF gene models ==")
for rec in horse_models:
    ident, paired, gaps = compare(horse, rec)
    pct = 100 * ident / paired if paired else 0
    print(f"{rec.id}\tlen={len(rec.seq)}\tident={ident}/{paired} ({pct:.1f}%)\tn_segments_absent_in_horse={len(gaps)}")

# bHLH-Zip region check: human MITF-M basic region + HLH + Zip
motif = "ERRRRFNINDRIKELGTLIPKSNDPDMRWNKGTILKASVDYIRKLQREQQRAKELENRQKKLEHANRHLLLRIQELEMQARAH"
print("\nbHLH-Zip block (human MITF-M 210-293 equivalent) present verbatim in horse:",
      motif in str(horse.seq))
print("Ser73-equivalent context (ERK site, MITF-M numbering 'SPMAML'):", "SPMAML" in str(horse.seq))
print("Ser409-equivalent C-terminal context 'SSRRSSMS':", "SSRRSSMS" in str(horse.seq))
print("6-aa alt-exon (+) insert 'ACIFPT' present:", "ACIFPT" in str(horse.seq))
