"""Scan Arabidopsis lower mevalonate-pathway enzymes for peroxisomal targeting signals.

Reproducible check of the PTS1/PTS2 claims made for Arabidopsis MK (P46086),
PMK (Q9C6T1), MVD1 (O23722) and MVD2 (F4JCU3), and of whether the segments that
UniProt annotates as PTS2 motifs are conserved in cytosolic human and yeast
orthologs of the same families.

Sequences are downloaded from the UniProt REST API at run time.  Nothing in the
report below is hard-coded: every number is computed from the sequences.

Motif definitions:
  * PTS1: C-terminal tripeptide matching the plant major/minor PTS1 consensus
    [SACPG][KRHNQS][LMIVY] (a permissive form of the Reumann 2004 consensus).
  * PTS2: [RK][LVIQ]x5[HQ][LAF] anywhere in the first 60 residues (plant PTS2
    nonapeptides lie in the N-terminal region).

Usage:
    python targeting_signals.py > RESULTS-raw.txt
"""

from __future__ import annotations

import re
import sys
import urllib.request

from Bio import Align
from Bio.Align import substitution_matrices

ARABIDOPSIS = {
    "MK": "P46086",
    "PMK": "Q9C6T1",
    "MVD1": "O23722",
    "MVD2": "F4JCU3",
}

# UniProt-annotated "Peroxisomal targeting signal PTS2" MOTIF features
# (positions as given on the UniProt records; ECO:0000305/ECO:0000250).
ANNOTATED_PTS2 = {
    "PMK": (57, 65),
    "MVD1": (40, 48),
    "MVD2": (40, 48),
}

# Cytosolic orthologs in the same PANTHER family (human and yeast members).
ORTHOLOGS = {
    "MK": {"human MVK": "Q03426", "yeast ERG12": "P07277"},
    "PMK": {"yeast ERG8": "P24521"},
    "MVD1": {"human MVD": "P53602", "yeast MVD1": "P32377"},
    "MVD2": {"human MVD": "P53602", "yeast MVD1": "P32377"},
}

PTS1 = re.compile(r"[SACPG][KRHNQS][LMIVY]$")
PTS2 = re.compile(r"(?=([RK][LVIQ].{5}[HQ][LAF]))")


def fetch_fasta(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url, timeout=60) as handle:
        text = handle.read().decode()
    return "".join(line.strip() for line in text.splitlines() if not line.startswith(">"))


def aligner() -> Align.PairwiseAligner:
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -10
    al.extend_gap_score = -0.5
    al.mode = "global"
    return al


def map_segment(query: str, target: str, start: int, end: int) -> tuple[str, float]:
    """Return the target segment aligned to query[start-1:end] and its % identity."""
    aln = aligner().align(query, target)[0]
    qmap: dict[int, int] = {}
    for (qs, qe), (ts, te) in zip(*aln.aligned):
        for offset in range(qe - qs):
            qmap[qs + offset] = ts + offset
    seg = []
    ident = 0
    for qpos in range(start - 1, end):
        tpos = qmap.get(qpos)
        if tpos is None:
            seg.append("-")
            continue
        seg.append(target[tpos])
        if target[tpos] == query[qpos]:
            ident += 1
    return "".join(seg), 100.0 * ident / (end - start + 1)


def global_identity(query: str, target: str) -> float:
    aln = aligner().align(query, target)[0]
    matches = 0
    for (qs, qe), (ts, te) in zip(*aln.aligned):
        matches += sum(1 for i in range(qe - qs) if query[qs + i] == target[ts + i])
    return 100.0 * matches / min(len(query), len(target))


def main() -> int:
    seqs = {name: fetch_fasta(acc) for name, acc in ARABIDOPSIS.items()}
    print("# Peroxisomal targeting-signal scan, Arabidopsis MVA-pathway enzymes\n")
    for name, acc in ARABIDOPSIS.items():
        s = seqs[name]
        print(f"## {name} ({acc}), {len(s)} aa")
        tail = s[-3:]
        print(f"- C-terminal tripeptide: {tail}; PTS1 consensus match: {bool(PTS1.search(s))}")
        hits = [(m.start() + 1, m.group(1)) for m in PTS2.finditer(s[:60])]
        print(f"- PTS2 consensus matches in residues 1-60: {hits if hits else 'none'}")
        if name in ANNOTATED_PTS2:
            a, b = ANNOTATED_PTS2[name]
            seg = s[a - 1 : b]
            print(f"- UniProt-annotated PTS2 segment {a}-{b}: {seg}; "
                  f"matches PTS2 consensus: {bool(re.fullmatch(r'[RK][LVIQ].{5}[HQ][LAF]', seg))}")
        for oname, oacc in ORTHOLOGS[name].items():
            o = fetch_fasta(oacc)
            gid = global_identity(s, o)
            line = f"- vs {oname} ({oacc}, {len(o)} aa): global identity {gid:.1f}%"
            if name in ANNOTATED_PTS2:
                a, b = ANNOTATED_PTS2[name]
                oseg, pid = map_segment(s, o, a, b)
                line += f"; aligned segment for {a}-{b}: {oseg} ({pid:.0f}% identical)"
            ohits = [(m.start() + 1, m.group(1)) for m in PTS2.finditer(o[:60])]
            line += f"; ortholog PTS2-consensus matches 1-60: {ohits if ohits else 'none'}"
            line += f"; ortholog C-terminus {o[-3:]} (PTS1 match: {bool(PTS1.search(o))})"
            print(line)
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
