"""Compare human TYW1B (Q6NUM6) with its paralog TYW1 (Q9NV66) and yeast Tyw1 (Q08960).

Reproducible: sequences for the two human proteins are parsed from the UniProt flat files
in the gene folders; yeast Tyw1 is downloaded from the UniProt REST API.
Reports pairwise identity, and the TYW1B residues aligned to TYW1 functional positions
(UniProt FT BINDING features: FMN, radical-SAM [4Fe-4S] cysteines) plus all TYW1 cysteines
that are conserved in yeast Tyw1 (candidate auxiliary-cluster ligands).

Run from repo root:  uv run python genes/human/TYW1B/TYW1B-bioinformatics/compare_paralogs.py
"""
import re
import sys
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

ROOT = Path(__file__).resolve().parents[4]


def seq_from_uniprot_txt(path: Path) -> str:
    text = path.read_text()
    m = re.search(r"^SQ .*?\n(.*?)^//", text, re.S | re.M)
    return re.sub(r"[^A-Z]", "", m.group(1))


def binding_features(path: Path):
    feats = []
    lines = path.read_text().splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"FT   BINDING\s+(\d+)(?:\.\.(\d+))?", line)
        if m:
            start = int(m.group(1)); end = int(m.group(2) or m.group(1))
            lig = ""
            for nxt in lines[i + 1:i + 4]:
                mm = re.search(r'/ligand="([^"]+)"', nxt)
                if mm:
                    lig = mm.group(1); break
            feats.append((start, end, lig))
    return feats


def fetch_fasta(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url, timeout=60) as r:
        txt = r.read().decode()
    return "".join(txt.splitlines()[1:])


def aligner():
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -10
    a.extend_gap_score = -0.5
    a.mode = "global"
    return a


def mapping(aln):
    """Map 1-based positions of seq A to seq B (None if gap)."""
    m = {}
    for (a0, a1), (b0, b1) in zip(*aln.aligned):
        for k in range(a1 - a0):
            m[a0 + k + 1] = b0 + k + 1
    return m


def identity(aln, a, b):
    mp = mapping(aln)
    same = sum(1 for i, j in mp.items() if a[i - 1] == b[j - 1])
    return same, len(mp)


def main():
    tyw1_txt = ROOT / "genes/human/TYW1/TYW1-uniprot.txt"
    tyw1b_txt = ROOT / "genes/human/TYW1B/TYW1B-uniprot.txt"
    tyw1 = seq_from_uniprot_txt(tyw1_txt)
    tyw1b = seq_from_uniprot_txt(tyw1b_txt)
    try:
        yeast = fetch_fasta("Q08960")
    except Exception as e:  # network may be unavailable
        print(f"WARNING: could not fetch yeast Tyw1: {e}", file=sys.stderr)
        yeast = None

    al = aligner()
    a_hb = al.align(tyw1, tyw1b)[0]
    s, n = identity(a_hb, tyw1, tyw1b)
    print(f"TYW1 length {len(tyw1)}; TYW1B length {len(tyw1b)}")
    print(f"TYW1 vs TYW1B: {s}/{n} aligned positions identical ({100*s/n:.1f}%)")
    m_hb = mapping(a_hb)
    unaligned = [i for i in range(1, len(tyw1) + 1) if i not in m_hb]
    if unaligned:
        # report contiguous TYW1 segments with no TYW1B counterpart
        segs, start, prev = [], unaligned[0], unaligned[0]
        for x in unaligned[1:]:
            if x != prev + 1:
                segs.append((start, prev)); start = x
            prev = x
        segs.append((start, prev))
        print("TYW1 segments without TYW1B counterpart:",
              ", ".join(f"{a}-{b}" for a, b in segs if b - a >= 4))

    print("\nTYW1 UniProt BINDING features mapped to TYW1B:")
    for st, en, lig in binding_features(tyw1_txt):
        h = tyw1[st - 1:en]
        b = "".join(tyw1b[m_hb[i] - 1] if i in m_hb else "-" for i in range(st, en + 1))
        bpos = [m_hb.get(i) for i in (st, en)]
        print(f"  TYW1 {st}-{en} ({lig}): {h}\n  TYW1B {bpos[0]}-{bpos[1]}: {b}  identical={h == b}")

    if yeast:
        a_hy = al.align(tyw1, yeast)[0]
        s, n = identity(a_hy, tyw1, yeast)
        print(f"\nTYW1 vs yeast Tyw1: {s}/{n} identical ({100*s/n:.1f}%)")
        a_by = al.align(tyw1b, yeast)[0]
        s, n = identity(a_by, tyw1b, yeast)
        print(f"TYW1B vs yeast Tyw1: {s}/{n} identical ({100*s/n:.1f}%)")
        m_hy = mapping(a_hy)
        print("\nTYW1 cysteines conserved in yeast Tyw1, and the TYW1B residue at that position:")
        lost = 0
        for i, aa in enumerate(tyw1, 1):
            if aa == "C" and i in m_hy and yeast[m_hy[i] - 1] == "C":
                bres = tyw1b[m_hb[i] - 1] if i in m_hb else "-"
                if bres != "C":
                    lost += 1
                print(f"  TYW1 C{i} / yeast C{m_hy[i]} / TYW1B {bres}{m_hb.get(i, '')}")
        print(f"Conserved cysteines not retained in TYW1B: {lost}")

    # Archaeal Taw1 from Pyrococcus abyssi (Q9V1F9): UniProt (HAMAP MF_01921) assigns
    # Cys45/Cys58/Cys71 to the auxiliary [4Fe-4S] cluster and Cys81/85/88 to the
    # radical-SAM cluster (two clusters demonstrated in PMID:23043105).
    try:
        pab = fetch_fasta("Q9V1F9")
    except Exception as e:
        print(f"WARNING: could not fetch P. abyssi Taw1: {e}", file=sys.stderr)
        pab = None
    if pab:
        a_hp = al.align(tyw1, pab)[0]
        inv = {v: k for k, v in mapping(a_hp).items()}
        print("\nP. abyssi Taw1 cluster-ligand cysteines mapped to TYW1 and TYW1B:")
        for pc, role in [(45, "auxiliary"), (58, "auxiliary"), (71, "auxiliary"),
                         (81, "radical SAM"), (85, "radical SAM"), (88, "radical SAM")]:
            hi = inv.get(pc)
            hres = f"{tyw1[hi-1]}{hi}" if hi else "-"
            bres = (f"{tyw1b[m_hb[hi]-1]}{m_hb[hi]}" if hi and hi in m_hb else "-")
            print(f"  Pab {pab[pc-1]}{pc} ({role}) -> TYW1 {hres} -> TYW1B {bres}")


if __name__ == "__main__":
    main()
