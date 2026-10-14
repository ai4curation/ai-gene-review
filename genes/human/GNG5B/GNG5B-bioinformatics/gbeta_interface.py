# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython", "requests"]
# ///
"""Map Gbeta-contacting Ggamma residues from a heterotrimer structure onto GNG5/GNG5B.

Downloads a G-protein heterotrimer structure from RCSB (default 1GP2: Gi alpha1,
beta1, gamma2), finds gamma-chain residues with any heavy atom within CUTOFF A
of the beta chain, aligns the structure's gamma sequence to GNG5 (P63218) and
to GNG5B (A0A804HLA8) fetched from UniProt, and reports which interface
positions are substituted in GNG5B relative to GNG5.

Usage:
    uv run gbeta_interface.py [PDB_ID BETA_CHAIN GAMMA_CHAIN CUTOFF]
"""
import io
import sys

import requests
from Bio import Align
from Bio.Align import substitution_matrices
from Bio.PDB import MMCIFParser, NeighborSearch
from Bio.PDB.Polypeptide import three_to_index, index_to_one

pdb_id = sys.argv[1] if len(sys.argv) > 1 else "1GP2"
beta_chain = sys.argv[2] if len(sys.argv) > 2 else "B"
gamma_chain = sys.argv[3] if len(sys.argv) > 3 else "G"
cutoff = float(sys.argv[4]) if len(sys.argv) > 4 else 4.0


def seq(acc):
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def one(res):
    try:
        return index_to_one(three_to_index(res.get_resname()))
    except (KeyError, ValueError):
        return "X"


cif = requests.get(f"https://files.rcsb.org/download/{pdb_id}.cif", timeout=120).text
s = MMCIFParser(QUIET=True).get_structure(pdb_id, io.StringIO(cif))
model = next(iter(s))
beta, gamma = model[beta_chain], model[gamma_chain]
gres = [r for r in gamma if r.id[0] == " "]
gseq = "".join(one(r) for r in gres)
ns = NeighborSearch([a for a in beta.get_atoms() if a.element != "H"])
contact = set()
for i, r in enumerate(gres):
    for a in r:
        if a.element != "H" and ns.search(a.coord, cutoff):
            contact.add(i)
            break
print(f"{pdb_id}: gamma chain {gamma_chain} observed residues {len(gres)}; "
      f"residues within {cutoff} A of beta chain {beta_chain}: {len(contact)}")

aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score, aligner.extend_gap_score = -10, -0.5


def mapping(a, b):
    aln = aligner.align(a, b)[0]
    m = {}
    for (s1, e1), (s2, e2) in zip(*aln.aligned):
        for k in range(e1 - s1):
            m[s1 + k] = s2 + k
    return m


g5, g5b = seq("P63218"), seq("A0A804HLA8")
m5 = mapping(gseq, g5)
m5b = {i: j for i, j in mapping(g5, g5b).items()}
print("\nGNG5 position (gamma2 struct residue) -> GNG5B; interface positions only")
n_sub = 0
for i in sorted(contact):
    if i not in m5:
        continue
    p5 = m5[i]
    p5b = m5b.get(p5)
    r5, r5b = g5[p5], (g5b[p5b] if p5b is not None else "-")
    flag = "" if r5 == r5b else "  <-- substituted in GNG5B"
    n_sub += r5 != r5b
    print(f"  GNG5 {r5}{p5+1:<3d} (struct {gres[i].get_resname()}{gres[i].id[1]}) "
          f"GNG5B {r5b}{(p5b + 1) if p5b is not None else ''}{flag}")
print(f"\nInterface positions mapped to GNG5: {sum(1 for i in contact if i in m5)}; "
      f"substituted in GNG5B: {n_sub}")
subs = [f"{g5[i]}{i+1}{g5b[j]}" for i, j in sorted(m5b.items()) if g5[i] != g5b[j]]
print(f"All GNG5->GNG5B substitutions: {', '.join(subs)}")
