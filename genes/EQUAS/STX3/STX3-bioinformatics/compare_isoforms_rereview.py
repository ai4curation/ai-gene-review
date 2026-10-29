# /// script
# requires-python = ">=3.10"
# dependencies = ["biopython>=1.83", "requests>=2.31"]
# ///
"""Exon-segment comparison of donkey STX3 gene models with rodent/human splice forms.

Fetches sequences from the UniProt REST API (FASTA, isoforms included), writes them to
isoforms_rereview.fasta next to this script, and reports per-segment identity of each
sequence against mouse syntaxin 3A (Q64704-1) and 3B (Q64704-2) for three segments:
  N   = residues 1..225 (shared exons 1-8 region)
  SNc = residues 226..262 of 3A (C-terminal half of the SNARE motif, alternative exon)
  TM  = residues 263..end (juxtamembrane + transmembrane anchor, alternative exon)
Segments are mapped through a global pairwise alignment to each reference.

Usage: uv run --script compare_isoforms_rereview.py
"""
from pathlib import Path
import io
import json

import requests
from Bio import Align, SeqIO

HERE = Path(__file__).resolve().parent
ACCS = [
    "A0A9L0J901",  # donkey benchmark model
    "A0A8C4LHZ8",  # donkey, UniProt gene-centric canonical
    "A0A8C4PQW9",  # donkey, other model
    "Q64704-1",  # mouse syntaxin 3A
    "Q64704-2",  # mouse syntaxin 3B
    "Q13277-1",  # human isoform A
    "Q08849",  # rat Stx3 (3A)
]


def fetch(acc: str) -> str:
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=60)
    r.raise_for_status()
    return r.text


fasta = "".join(fetch(a) for a in ACCS)
(HERE / "isoforms_rereview.fasta").write_text(fasta)
seqs = {}
for rec, acc in zip(SeqIO.parse(io.StringIO(fasta), "fasta"), ACCS):
    seqs[acc] = str(rec.seq)

aligner = Align.PairwiseAligner(
    mode="global", match_score=2, mismatch_score=-1, open_gap_score=-10, extend_gap_score=-0.5
)

# segments defined on the 3A reference coordinates (1-based inclusive)
SEG_3A = {"N": (1, 225), "SNc": (226, 262), "TM": (263, 289)}
# for 3B the alternative region starts at the same point; define on its own coordinates
SEG_3B = {"N": (1, 225), "SNc": (226, 262), "TM": (263, len(seqs["Q64704-2"]))}


def seg_identity(ref: str, query: str, segs: dict) -> dict:
    al = aligner.align(ref, query)[0]
    m = {}
    for (s, e), (t, u) in zip(*al.aligned):
        for i, j in zip(range(s, e), range(t, u)):
            m[int(i)] = int(j)
    out = {}
    for name, (a, b) in segs.items():
        idx = range(a - 1, b)
        paired = [i for i in idx if i in m]
        ident = sum(ref[i] == query[m[i]] for i in paired)
        out[name] = {
            "ref_len": len(idx),
            "paired": len(paired),
            "identity_pct": round(100 * ident / len(idx), 1),
            "query_segment": "".join(query[m[i]] for i in paired),
        }
    return out


results = {}
for acc in ACCS:
    results[acc] = {
        "length": len(seqs[acc]),
        "vs_mouse_3A": seg_identity(seqs["Q64704-1"], seqs[acc], SEG_3A),
        "vs_mouse_3B": seg_identity(seqs["Q64704-2"], seqs[acc], SEG_3B),
    }

(HERE / "results_rereview.json").write_text(json.dumps(results, indent=2))
lines = ["accession\tlength\tsegment\tid_vs_3A\tid_vs_3B\tclosest"]
for acc, r in results.items():
    for seg in ("N", "SNc", "TM"):
        a = r["vs_mouse_3A"][seg]["identity_pct"]
        b = r["vs_mouse_3B"][seg]["identity_pct"]
        closest = "3A" if a > b else ("3B" if b > a else "equal")
        lines.append(f"{acc}\t{r['length']}\t{seg}\t{a}\t{b}\t{closest}")
print("\n".join(lines))
