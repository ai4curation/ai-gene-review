# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Scan Q7SAD4 (from the cached UniProt flat file) for class B FMO sequence motifs
and hydrophobic segments, and compare with human FMO3 (P31513) fetched from UniProt."""
import re
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent


def seq_from_flatfile(text: str) -> str:
    s = text.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[^A-Z]", "", s)


def fetch_fasta(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    txt = urllib.request.urlopen(url).read().decode()
    return "".join(txt.splitlines()[1:])


MOTIFS = {
    "FAD dinucleotide-binding GxGxxG": r"G.G..G",
    "FMO-identifying FxGxxxHxxx[YF]": r"F.G...H...[YF]",
    "NADPH dinucleotide-binding GxGxx[GA]": r"G.G..[GA]",
    "FATGY-like motif F[AS]TG[YF]": r"[FY][AS][TS]G[YF]",
    "relaxed FMO motif FxGxxxH": r"F.G...H",
    "relaxed second dinucleotide motif [GA]x[GA]xx[GA] (residues 150-260)": r"[GA].[GA]..[GA]",
}

KD = dict(A=1.8, R=-4.5, N=-3.5, D=-3.5, C=2.5, Q=-3.5, E=-3.5, G=-0.4, H=-3.2, I=4.5,
          L=3.8, K=-3.9, M=1.9, F=2.8, P=-1.6, S=-0.8, T=-0.7, W=-0.9, Y=-1.3, V=4.2)


def hydrophobic_windows(seq: str, w: int = 19, cut: float = 1.6):
    hits = []
    for i in range(len(seq) - w + 1):
        h = sum(KD[a] for a in seq[i:i + w]) / w
        if h >= cut:
            hits.append((i + 1, round(h, 2)))
    return hits


def report(name: str, seq: str):
    print(f"## {name} (length {len(seq)})")
    for label, pat in MOTIFS.items():
        ms = [(m.start() + 1, m.group(1)) for m in re.finditer(f"(?=({pat}))", seq)]
        if "150-260" in label:
            ms = [m for m in ms if 150 <= m[0] <= 260]
        print(f"- {label}: {ms if ms else 'none'}")
    hw = hydrophobic_windows(seq)
    print(f"- Kyte-Doolittle 19-residue windows >=1.6: {len(hw)}; starts: {[h[0] for h in hw][:10]}")
    print(f"- C-terminal 40 residues: {seq[-40:]}")
    print()


if __name__ == "__main__":
    q = seq_from_flatfile((HERE.parent / "NCU06296-uniprot.txt").read_text())
    report("Q7SAD4 NCU06296", q)
    report("P31513 human FMO3", fetch_fasta("P31513"))
