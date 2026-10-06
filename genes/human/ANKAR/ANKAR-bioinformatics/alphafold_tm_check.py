"""Is ANKAR residues 309-329 a transmembrane helix or a buried helix in a soluble fold?

Uses the AlphaFold DB model of Q7Z5J8. For each residue it reads pLDDT (B-factor
column) and counts C-alpha atoms of residues more than 5 positions away in
sequence within 10 A (a burial proxy). A transmembrane helix modelled by
AlphaFold as part of a soluble protein tends to be a confident helix with few
packing contacts; a helix packed into the repeat fold has many. It also checks
helicity with the C-alpha(i)-C-alpha(i+3) distance (about 5.0-5.5 A in a helix).
Results are printed against the protein-wide distribution. Nothing is assumed.

Run: uv run python alphafold_tm_check.py
"""

import math
import statistics
import urllib.request

URL = "https://alphafold.ebi.ac.uk/files/AF-Q7Z5J8-F1-model_v6.pdb"
SEG = (309, 329)


def read_ca(url: str) -> dict[int, tuple[float, float, float, float]]:
    """Map residue number -> (x, y, z, pLDDT) for C-alpha atoms."""
    with urllib.request.urlopen(url) as handle:
        lines = handle.read().decode().splitlines()
    out = {}
    for line in lines:
        if line.startswith("ATOM") and line[12:16].strip() == "CA":
            out[int(line[22:26])] = (float(line[30:38]), float(line[38:46]), float(line[46:54]), float(line[60:66]))
    return out


def dist(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    """Euclidean distance between the first three coordinates.

    >>> dist((0, 0, 0, 90), (3, 4, 0, 90))
    5.0
    """
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(3)))


def contacts(ca: dict, res: int, cutoff: float = 10.0) -> int:
    """C-alpha atoms within cutoff of res, excluding |i-j| <= 5."""
    return sum(1 for j, c in ca.items() if abs(j - res) > 5 and dist(ca[res], c) <= cutoff)


def main() -> None:
    ca = read_ca(URL)
    allc = {r: contacts(ca, r) for r in ca}
    seg = range(SEG[0], SEG[1] + 1)
    seg_c = [allc[r] for r in seg]
    seg_p = [ca[r][3] for r in seg]
    i3 = [dist(ca[r], ca[r + 3]) for r in range(SEG[0], SEG[1] - 2)]
    confident = [r for r in ca if ca[r][3] >= 70]
    pct = sum(1 for r in confident if allc[r] <= statistics.mean(seg_c)) / len(confident)
    print(f"residues_modelled\t{len(ca)}")
    print(f"segment\t{SEG[0]}-{SEG[1]}")
    print(f"segment_mean_pLDDT\t{statistics.mean(seg_p):.1f}")
    print(f"segment_mean_CAi_CAi3\t{statistics.mean(i3):.2f}")
    print(f"segment_mean_contacts\t{statistics.mean(seg_c):.1f}")
    print(f"protein_mean_contacts_confident_residues\t{statistics.mean(allc[r] for r in confident):.1f}")
    print(f"fraction_confident_residues_with_contacts_le_segment\t{pct:.2f}")
    print(f"flank_mean_pLDDT_289-308\t{statistics.mean(ca[r][3] for r in range(289, 309)):.1f}")
    print(f"flank_mean_pLDDT_330-349\t{statistics.mean(ca[r][3] for r in range(330, 350)):.1f}")


if __name__ == "__main__":
    main()
