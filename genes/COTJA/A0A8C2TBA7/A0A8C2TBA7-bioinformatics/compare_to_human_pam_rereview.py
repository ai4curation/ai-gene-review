"""Align quail A0A8C2TBA7 with human PAM (P19021, canonical isoform 1).

Reports identity, coverage, and which human isoform-specific segments
(exon 16 linker 388-494; 829-914 cytosolic-region variants) are present,
plus conservation of the PHM Cu ligands and PAL Zn ligands of human PAM.
Usage: uv run --with biopython --with requests python compare_to_human_pam_rereview.py
"""
import requests
from Bio import Align
from Bio.Align import substitution_matrices


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def main() -> None:
    quail = fetch("A0A8C2TBA7")
    human = fetch("P19021")
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    aligner.mode = "global"
    aln = aligner.align(quail, human)[0]
    # map human position -> quail position
    h2q: dict[int, int] = {}
    ident = 0
    aligned = 0
    for (qs, qe), (hs, he) in zip(*aln.aligned):
        for k in range(qe - qs):
            h2q[hs + k + 1] = qs + k + 1
            aligned += 1
            if quail[qs + k] == human[hs + k]:
                ident += 1
    print(f"quail length {len(quail)}; human P19021-1 length {len(human)}")
    print(f"aligned pairs {aligned}; identity {ident/aligned:.3f} over aligned; "
          f"human coverage {aligned/len(human):.3f}")
    for name, (a, b) in {"exon16 linker (VSP_001227, 388-494)": (388, 494),
                         "region 829-914 (VSP_001228)": (829, 914)}.items():
        present = sum(1 for p in range(a, b + 1) if p in h2q)
        print(f"{name}: {present}/{b-a+1} human residues aligned in quail")
    # metal-ligand positions taken from the human UniProt record's BINDING features
    r = requests.get("https://rest.uniprot.org/uniprotkb/P19021.json", timeout=60)
    r.raise_for_status()
    for f in r.json()["features"]:
        if f["type"] != "Binding site":
            continue
        lig = f.get("ligand", {}).get("name", "")
        if not any(m in lig for m in ("Cu", "Zn", "Ca")):
            continue
        p = f["location"]["start"]["value"]
        q = h2q.get(p)
        print(f"{lig}: human {human[p-1]}{p} -> quail "
              f"{(quail[q-1] + str(q)) if q else 'gap'}")

if __name__ == "__main__":
    main()
