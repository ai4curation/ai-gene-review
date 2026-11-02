"""Place CG13096 among ribosomal-L1-domain proteins.

Fetches sequences from UniProt, checks H0RNN8 vs canonical Q9VLK2 identity,
aligns the panel with MAFFT, computes pairwise identity over aligned
(non-gap) columns, builds a neighbour-joining tree (Biopython), and runs
phmmer with CG13096 as query against the panel.

Run: uv run --with biopython --with requests python l1_family_placement.py
Requires mafft and phmmer on PATH.
"""

import subprocess
from pathlib import Path

import requests
from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

OUT = Path(__file__).parent / "l1_family_placement_out"
PANEL = {
    "H0RNN8": "Dmel CG13096 (benchmark TrEMBL)",
    "Q9VLK2": "Dmel CG13096 (Swiss-Prot canonical)",
    "Q54WX8": "Ddis DDB_G0279335 (PTHR48162:SF1)",
    "Q5ALY5": "Calb NRI1 (PTHR48162:SF1)",
    "O76021": "Hsap RSL1D1 (PTHR23105:SF31)",
    "Q8BVY0": "Mmus Rsl1d1 (PTHR23105:SF31)",
    "Q20720": "Cele F53F4.11",
    "P36144": "Scer UTP30 (PTHR23105:SF31)",
    "P38779": "Scer CIC1/NSA3 (PTHR23105:SF203)",
    "A0A1D8PPJ1": "Calb CIC1 (PTHR23105:SF31)",
    "P62906": "Hsap RPL10A uL1 (PTHR23105)",
    "Q9VFE0": "Dmel RpL10Aa uL1 (PTHR23105)",
    "P0CX43": "Scer RPL1A uL1 (PTHR23105)",
    "Q9BYD6": "Hsap MRPL1 uL1m (PTHR36427)",
    "Q9VHT5": "Dmel mRpL1 uL1m (PTHR36427)",
    "P09263": "VZV ORF11 (PTHR48162:SF1)",
}


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return "".join(r.text.splitlines()[1:])


def main() -> None:
    OUT.mkdir(exist_ok=True)
    seqs = {acc: fetch(acc) for acc in PANEL}
    report = []
    same = seqs["H0RNN8"] == seqs["Q9VLK2"]
    report.append(
        f"H0RNN8 length {len(seqs['H0RNN8'])}; Q9VLK2 length {len(seqs['Q9VLK2'])}; identical sequence: {same}"
    )
    fa = OUT / "panel.fasta"
    fa.write_text("".join(f">{a}\n{s}\n" for a, s in seqs.items() if a != "H0RNN8"))
    aln_path = OUT / "panel.mafft.fasta"
    with aln_path.open("w") as fh:
        subprocess.run(["mafft", "--localpair", "--maxiterate", "1000", "--quiet", str(fa)], stdout=fh, check=True)
    aln = AlignIO.read(aln_path, "fasta")
    ids = [r.id for r in aln]
    q = next(r for r in aln if r.id == "Q9VLK2")
    report.append("\nPairwise identity of CG13096 (Q9VLK2) to each panel member (aligned non-gap columns):")
    rows = []
    for r in aln:
        if r.id == "Q9VLK2":
            continue
        cols = [(a, b) for a, b in zip(str(q.seq), str(r.seq)) if a != "-" and b != "-"]
        ident = sum(a == b for a, b in cols) / len(cols) if cols else 0.0
        rows.append((ident, r.id, len(cols)))
    for ident, rid, n in sorted(rows, reverse=True):
        report.append(f"  {rid:12s} {PANEL[rid]:40s} identity={ident:.3f} over {n} cols")
    dm = DistanceCalculator("blosum62").get_distance(aln)
    tree = DistanceTreeConstructor().nj(dm)
    tree.root_with_outgroup("Q9BYD6", "Q9VHT5")
    Phylo.write(tree, OUT / "panel_nj.nwk", "newick")
    report.append("\nNJ tree (BLOSUM62 distances, rooted on mitochondrial uL1m):")
    report.append(tree.format("newick").strip())
    tbl = OUT / "phmmer.tbl"
    qfa = OUT / "query.fasta"
    qfa.write_text(f">Q9VLK2\n{seqs['Q9VLK2']}\n")
    subprocess.run(["phmmer", "--tblout", str(tbl), "-o", "/dev/null", str(qfa), str(fa)], check=True)
    report.append("\nphmmer (query CG13096 Q9VLK2) full-sequence hits:")
    for line in tbl.read_text().splitlines():
        if not line.startswith("#"):
            f = line.split()
            report.append(f"  {f[0]:12s} {PANEL.get(f[0], ''):40s} E={f[4]} score={f[5]}")
    (OUT / "report.txt").write_text("\n".join(report) + "\n")
    print("\n".join(report))
    _ = ids


if __name__ == "__main__":
    main()
