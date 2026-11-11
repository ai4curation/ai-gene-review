# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython>=1.83", "requests>=2.31"]
# ///
"""Compare donkey ORC5 A0A9L0I6Y4 to human ORC5 O43913 (UniProt REST, live).

Reports global identity/coverage, PANTHER assignments from each UniProt record,
and the residues at the human Walker A (37-44) and Walker B (DKAE, 125-128) motifs and at the C-terminus.
"""

import requests
from Bio import Align
from Bio.Align import substitution_matrices

TARGET = "A0A9L0I6Y4"
HUMAN = "O43913"


def fetch(acc: str) -> dict:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=60)
    r.raise_for_status()
    return r.json()


def panther(entry: dict) -> list[str]:
    return sorted(
        x["id"] for x in entry.get("uniProtKBCrossReferences", []) if x["database"] == "PANTHER"
    )


def main() -> None:
    t, h = fetch(TARGET), fetch(HUMAN)
    tseq, hseq = t["sequence"]["value"], h["sequence"]["value"]
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aln = aligner.align(hseq, tseq)[0]
    hmap = {}
    ident = paired = 0
    for (hs, he), (ts, te) in zip(*aln.aligned):
        for i, j in zip(range(hs, he), range(ts, te)):
            hmap[i] = j
            paired += 1
            ident += hseq[i] == tseq[j]
    print(f"# ORC5 {TARGET} (donkey) vs {HUMAN} (human)\n")
    print(f"- lengths: target {len(tseq)}, human {len(hseq)}")
    print(f"- identical residues: {ident}/{paired} paired ({100*ident/paired:.2f}%); "
          f"human coverage {100*paired/len(hseq):.2f}%")
    print(f"- PANTHER target: {', '.join(panther(t))}")
    print(f"- PANTHER human: {', '.join(panther(h))}")
    wa_h = hseq[36:44]
    wa_t = "".join(tseq[hmap[i]] if i in hmap else "-" for i in range(36, 44))
    print(f"- Walker A (human 37-44): human {wa_h}, target {wa_t}")
    # Walker B: human ORC5 carries the non-canonical DKAE motif, D125 (Tocilj et al. 2017)
    wb_h = hseq[124:128]
    wb_t = "".join(tseq[hmap[i]] if i in hmap else "-" for i in range(124, 128))
    print(f"- Walker B (human 125-128, DKAE): human {wb_h}, target {wb_t}")
    # DNA-proximal beta-hairpin residue H398 (Jaremko et al. 2020)
    print(f"- beta-hairpin H398: human {hseq[397]}, target {tseq[hmap[397]] if 397 in hmap else '-'}")
    print(f"- C-terminal 15 aa: human {hseq[-15:]}, target {tseq[-15:]}")


if __name__ == "__main__":
    main()
