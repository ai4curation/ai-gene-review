# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython>=1.83", "requests>=2.31"]
# ///
"""Compare donkey NUMB canonical (A0A9L0IHZ0) with human P49757 and mouse Q9QZS3.

Usage (from repo root):
  uv run --script genes/EQUAS/NUMB__A0A9L0IHZ0/NUMB__A0A9L0IHZ0-bioinformatics/compare_orthologs.py

Fetches human/mouse UniProt flat files (saved alongside), parses the donkey flat file,
runs global BLOSUM62 alignments, maps human Thr-102 (AAK1 site), reports DPF/NPF motif
positions and PANTHER subfamily assignments from the local PANTHER entries table.
"""
import csv
import re
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
DONKEY = HERE.parent / "NUMB__A0A9L0IHZ0-uniprot.txt"
PANTHER_CSV = ROOT / "interpro/panther/PTHR47368/PTHR47368-entries.csv"
ORTHOLOGS = {"human": "P49757", "mouse": "Q9QZS3"}


def seq_from_flat(text: str) -> str:
    seq_block = text.split("\nSQ ")[1].split("\n", 1)[1].split("//")[0]
    return re.sub(r"[^A-Z]", "", seq_block)


def first_domain(text: str):
    m = re.search(r"FT   DOMAIN\s+(\d+)\.\.(\d+)", text)
    return (int(m.group(1)), int(m.group(2))) if m else None


def motifs(seq: str, pat: str):
    return [m.start() + 1 for m in re.finditer(pat, seq)]


def main():
    dtext = DONKEY.read_text()
    dseq = seq_from_flat(dtext)
    print(f"## donkey A0A9L0IHZ0 length {len(dseq)}; PID domain {first_domain(dtext)}")
    print(f"DPF at {motifs(dseq, 'DPF')}; NPF at {motifs(dseq, 'NPF')}")
    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    for sp, acc in ORTHOLOGS.items():
        path = HERE / f"{sp}-{acc}-uniprot.txt"
        if not path.exists():
            r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.txt", timeout=60)
            r.raise_for_status()
            path.write_text(r.text)
        otext = path.read_text()
        oseq = seq_from_flat(otext)
        aln = aligner.align(dseq, oseq)[0]
        pairs = ident = 0
        o2d = {}
        for (ds, de), (os_, oe) in zip(*aln.aligned):
            for i, j in zip(range(ds, de), range(os_, oe)):
                pairs += 1
                ident += dseq[i] == oseq[j]
                o2d[j + 1] = i + 1
        print(f"\n## vs {sp} {acc} length {len(oseq)}; PID domain {first_domain(otext)}")
        print(f"aligned pairs {pairs}; identical {ident}; identity {100*ident/pairs:.2f}%")
        print(f"coverage donkey {100*pairs/len(dseq):.2f}%; coverage {sp} {100*pairs/len(oseq):.2f}%")
        print("aligned blocks (donkey : ortholog, 1-based):")
        for (ds, de), (os_, oe) in zip(*aln.aligned):
            print(f"  {ds+1}-{de} : {os_+1}-{oe}")
        if sp == "human":
            d = o2d.get(102)
            print(f"human T102 ({oseq[101]}) maps to donkey {d} ({dseq[d-1] if d else '-'})")
        print(f"{sp} DPF at {motifs(oseq, 'DPF')}; NPF at {motifs(oseq, 'NPF')}")
    print("\n## PANTHER subfamily assignments (local PTHR47368 entries table)")
    with PANTHER_CSV.open() as fh:
        for row in csv.DictReader(fh):
            if row["id"] in {"P49757", "Q9QZS3", "P16554", "O08919", "Q9Y6R0"}:
                print(f"  {row['id']} {row['source_tax_name']} {row['gene']} -> {row['subfamily']} {row['subfamily_name']}")
    dpanther = re.findall(r"DR   PANTHER; (PTHR47368[^;]*);", dtext)
    print(f"  A0A9L0IHZ0 (UniProt DR PANTHER) -> {dpanther}")


if __name__ == "__main__":
    main()
