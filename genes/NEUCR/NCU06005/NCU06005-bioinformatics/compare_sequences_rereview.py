# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "biopython"]
# ///
"""Re-review analysis for NCU06005 (Q7S2F2).

1. Lists every N. crassa OR74A (taxon 367110) UniProt entry in PANTHER PTHR10196
   and every entry carrying EC 2.7.1.30, to test whether NCU06005 is the sole
   glycerol kinase gene in the reference proteome.
2. Global pairwise identity of Q7S2F2 to characterized glycerol kinases
   (yeast GUT1, E. coli GlpK, Arabidopsis GLPK, human GK), with their PANTHER subfamilies.
3. Net charge of the N-terminal segment preceding the FGGY_N domain
   (a crude indicator of a presequence-type mitochondrial targeting signal).
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices

UP = "https://rest.uniprot.org/uniprotkb"


def search(q, fields):
    r = requests.get(f"{UP}/search", params={"query": q, "fields": fields, "format": "tsv"}, timeout=60)
    r.raise_for_status()
    return r.text.strip().splitlines()


def entry(acc):
    r = requests.get(f"{UP}/{acc}.json", timeout=60)
    r.raise_for_status()
    j = r.json()
    pan = [x["id"] for x in j.get("uniProtKBCrossReferences", []) if x["database"] == "PANTHER"]
    return j["sequence"]["value"], pan


print("## N. crassa (367110) PTHR10196 members")
for line in search("organism_id:367110 AND xref:panther-PTHR10196", "accession,gene_orf,protein_name,length,xref_panther"):
    print(line)
print("\n## N. crassa (367110) entries with EC 2.7.1.30")
for line in search("organism_id:367110 AND ec:2.7.1.30", "accession,gene_orf,protein_name,length"):
    print(line)

target_seq, target_pan = entry("Q7S2F2")
aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score = -10
aligner.extend_gap_score = -0.5
aligner.mode = "global"

print(f"\n## Pairwise identity of Q7S2F2 ({len(target_seq)} aa; PANTHER {target_pan})")
for acc, name in [("P32190", "S. cerevisiae GUT1"), ("Q9M8L4", "A. thaliana GLPK"),
                  ("P0A6F3", "E. coli GlpK"), ("P32189", "human GK")]:
    seq, pan = entry(acc)
    aln = aligner.align(target_seq, seq)[0]
    ident = sum(1 for a, b in zip(*aln) if a == b and a != "-")
    cols = sum(1 for a, b in zip(*aln) if a != "-" and b != "-")
    print(f"{acc}\t{name}\t{len(seq)} aa\tPANTHER {pan}\tidentity over aligned cols {ident}/{cols} = {ident/cols:.1%}")

nterm = target_seq[:63]
charge = sum(nterm.count(c) for c in "KR") - sum(nterm.count(c) for c in "DE")
print(f"\n## N-terminal 1-63 (before Pfam FGGY_N at 64): {nterm}")
print(f"K+R={sum(nterm.count(c) for c in 'KR')}, D+E={sum(nterm.count(c) for c in 'DE')}, net charge={charge}")
