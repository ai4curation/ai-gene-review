"""Map the U5TVQ7 SoxB fragment onto full-length SoxB references.

Downloads sequences and the PDB-derived Mn(2+) binding-site features of
Thermus thermophilus HB27 SoxB (Q72IT0; PDB 2WDC/2WDD/2WDE/2WDF) from UniProt,
aligns U5TVQ7 (325 aa, NON_TER at both ends) to each reference with a
local (Smith-Waterman) BLOSUM62 alignment, and
reports fragment coverage, percent identity, and which Mn ligands fall inside
the fragment and whether the residue is conserved.

Usage: uv run --with biopython python map_fragment.py
"""
import json
import re
import sys
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

UNIPROT = "https://rest.uniprot.org/uniprotkb/{}.json"
FRAGMENT = "U5TVQ7"
REFERENCES = ["Q72IT0", "A0AAE6TS95"]  # T. thermophilus HB27 SoxB; P. pantotrophus SoxB
STRUCT_REF = "Q72IT0"


def fetch(acc):
    with urllib.request.urlopen(UNIPROT.format(acc)) as r:
        return json.load(r)


def mn_sites(entry):
    sites = []
    for f in entry.get("features", []):
        if f["type"] == "Binding site" and "Mn" in f.get("ligand", {}).get("name", ""):
            sites.append(f["location"]["start"]["value"])
    return sorted(set(sites))


def align(ref_seq, frag_seq):
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "local"
    return aligner.align(ref_seq, frag_seq)[0]


def main():
    frag = fetch(FRAGMENT)
    fseq = frag["sequence"]["value"]
    print(f"{FRAGMENT}: length {len(fseq)}")
    for acc in REFERENCES:
        ref = fetch(acc)
        rseq = ref["sequence"]["value"]
        org = ref["organism"]["scientificName"]
        aln = align(rseq, fseq)
        ref2frag = {}
        ident = cols = 0
        for (rs, re_), (fs, fe) in zip(*aln.aligned):
            for i, j in zip(range(rs, re_), range(fs, fe)):
                ref2frag[i + 1] = j + 1
                cols += 1
                ident += rseq[i] == fseq[j]
        rpos = sorted(ref2frag)
        print(f"\nReference {acc} ({org}), length {len(rseq)}")
        print(f"  fragment aligns to reference residues {rpos[0]}-{rpos[-1]}")
        print(f"  aligned columns {cols}; identity {ident}/{cols} = {100*ident/cols:.1f}%")
        if acc == STRUCT_REF:
            sites = mn_sites(ref)
            print(f"  PDB-derived Mn(2+) ligand positions in {acc}: {sites}")
            for p in sites:
                if p in ref2frag:
                    j = ref2frag[p]
                    print(f"    {acc} {rseq[p-1]}{p} -> {FRAGMENT} {fseq[j-1]}{j}"
                          f" {'conserved' if rseq[p-1]==fseq[j-1] else 'DIFFERENT'}")
                else:
                    print(f"    {acc} {rseq[p-1]}{p} -> outside fragment / gap")


if __name__ == "__main__":
    sys.exit(main())
