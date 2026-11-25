"""Check whether the MES-1 kinase domain keeps the canonical catalytic residues.

Aligns the MES-1 protein kinase domain (UniProt G5EBL2, residues 656-966, from the
local UniProt flat file) with the kinase domains of two active kinases fetched from the
UniProt REST API: human NEK9 (Q8TD19, the PANTHER IBA seed for MES-1) and human SRC
(P12931, a tyrosine kinase, since MES-1 is described as receptor tyrosine kinase-like).
For each reference, the canonical motifs are located in the reference sequence by
pattern (glycine-rich loop G-x-G-x-x-G, beta3 lysine of VAIK, catalytic-loop HRD, DFG,
APE), and the MES-1 residues aligned to them are reported.

Usage (from the repository root, with the project interpreter):
    python genes/worm/mes-1/mes-1-bioinformatics/kinase_motifs.py

Output is printed as plain text; RESULTS.md records one run. Nothing is hard-coded
except the domain boundaries, which come from UniProt feature tables.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
UNIPROT_FILE = HERE.parent / "mes-1-uniprot.txt"
MES1_DOMAIN = (656, 966)  # FT DOMAIN 656..966 "Protein kinase" in mes-1-uniprot.txt
REFERENCES = {"NEK9_HUMAN": "Q8TD19", "SRC_HUMAN": "P12931"}


def read_flatfile_sequence(path: Path) -> str:
    seq, in_sq = [], False
    for line in path.read_text().splitlines():
        if line.startswith("SQ "):
            in_sq = True
            continue
        if line.startswith("//"):
            break
        if in_sq:
            seq.append(line.replace(" ", ""))
    return "".join(seq)


def fetch_uniprot(acc: str) -> tuple[str, tuple[int, int]]:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json"
    with urllib.request.urlopen(url, timeout=60) as fh:
        data = json.load(fh)
    seq = data["sequence"]["value"]
    for feat in data.get("features", []):
        if feat["type"] == "Domain" and "kinase" in feat.get("description", "").lower():
            loc = feat["location"]
            return seq, (loc["start"]["value"], loc["end"]["value"])
    raise SystemExit(f"no kinase domain feature for {acc}")


def motif_positions(domain: str, offset: int) -> dict[str, int]:
    """1-based positions (in the full reference sequence) of key catalytic residues."""
    found: dict[str, int] = {}
    patterns = {
        "Gly-loop G1": (r"G.G..G", 0),
        "Gly-loop G2": (r"G.G..G", 2),
        "Gly-loop G3": (r"G.G..G", 5),
        "beta3 Lys (VAIK)": (r"[AV].[IVLM]K", 3),
        "catalytic Asp (HRD)": (r"H[RNC]D", 2),
        "catalytic Asn (HRDxxxxN)": (r"H[RNC]D....N", 7),
        "DFG Asp": (r"DFG", 0),
        "APE Glu": (r"[AP]PE", 2),
    }
    for name, (pat, idx) in patterns.items():
        m = re.search(pat, domain)
        if m:
            found[name] = offset + m.start() + idx
    return found


def aligned_map(aln) -> dict[int, int]:
    """Map 0-based target index -> 0-based query index over aligned blocks."""
    mapping: dict[int, int] = {}
    for (t0, t1), (q0, q1) in zip(*aln.aligned):
        for i in range(t1 - t0):
            mapping[t0 + i] = q0 + i
    return mapping


def main() -> int:
    mes1 = read_flatfile_sequence(UNIPROT_FILE)
    m_start, m_end = MES1_DOMAIN
    mes1_dom = mes1[m_start - 1 : m_end]
    aligner = Align.PairwiseAligner()
    aligner.mode = "local"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -0.5
    print(f"MES-1 (G5EBL2) kinase domain {m_start}-{m_end}, length {len(mes1_dom)}")
    # Direct motif scan of MES-1 itself, independent of any alignment.
    nlobe = mes1_dom[:105]  # first ~1/3 of the domain, where the Gly-rich loop sits
    gly = [(m_start + m.start(), m.group()) for m in re.finditer(r"(?=(G.G..G))", nlobe)]
    print(f"  MES-1 G-x-G-x-x-G matches in N-lobe {m_start}-{m_start + 104}: {gly or 'none'}")
    for label, pat in [("HRD-type catalytic loop H[RNC]D", r"H[RNC]D"),
                       ("DFG", r"DFG"), ("any D[FLWY]G", r"D[FLWY]G"),
                       ("APE-type [AP]PE", r"[AP]PE")]:
        hits = [(m_start + m.start(), m.group()) for m in re.finditer(pat, mes1_dom)]
        print(f"  MES-1 {label}: {hits or 'none'}")
    for name, acc in REFERENCES.items():
        seq, (r_start, r_end) = fetch_uniprot(acc)
        ref_dom = seq[r_start - 1 : r_end]
        aln = aligner.align(ref_dom, mes1_dom)[0]
        mapping = aligned_map(aln)
        ident = sum(
            1 for t, q in mapping.items() if ref_dom[t] == mes1_dom[q]
        ) / max(len(mapping), 1)
        print(f"\n{name} ({acc}) kinase domain {r_start}-{r_end}; aligned columns "
              f"{len(mapping)}, identity {ident:.2f}, score {aln.score:.1f}")
        for motif, pos in motif_positions(ref_dom, r_start).items():
            t = pos - r_start
            ref_res = seq[pos - 1]
            if t in mapping:
                q = mapping[t]
                print(f"  {motif:28s} {name} {ref_res}{pos} -> MES-1 "
                      f"{mes1_dom[q]}{m_start + q}")
            else:
                print(f"  {motif:28s} {name} {ref_res}{pos} -> MES-1 (gap / unaligned)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
