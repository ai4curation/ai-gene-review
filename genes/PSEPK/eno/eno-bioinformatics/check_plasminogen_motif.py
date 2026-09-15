#!/usr/bin/env python3
"""Is the pneumococcal plasminogen-binding motif present in P. putida KT2440 enolase?

Background. UniProt attaches "Secreted"/"Cell surface" to essentially every
bacterial enolase through the HAMAP family rule MF_00318, because enolase
moonlights as a surface plasmin(ogen) receptor in numerous pathogens. The
PSEPK eno review flags the resulting GO:0005576 annotation as an over-annotation
on the grounds that no organism-specific evidence exists -- an argument from
absence.

This script replaces that with a positive test. Bergmann et al. 2003
(PMID:12828639) identified an *internal* nine-residue plasmin(ogen)-binding
motif in surface-displayed alpha-enolase of Streptococcus pneumoniae, distinct
from the C-terminal lysines that had previously been assumed to be the whole
story. If surface display is a clade-specific accessory role rather than a
family-wide property, the motif should be recognisable in the pathogen enolases
that carry the role and degenerate or absent in P. putida.

The script fetches sequences from UniProt, locates the pneumococcal motif in the
reference, maps the aligned region onto each other enolase, and reports the
residues found. It also reports the C-terminal residues, the other feature
commonly invoked for plasminogen binding.

No conclusion is hardcoded: the script prints what it finds, including "motif
not locatable", and the interpretation lives in RESULTS.md.

    uv run --with biopython python check_plasminogen_motif.py
"""

from __future__ import annotations

import json
import urllib.request

# Q97QS2 is the S. pneumoniae TIGR4 enolase, the organism the motif was defined in.
REFERENCE = ("Q97QS2", "S. pneumoniae TIGR4")
QUERIES = [
    ("Q88MF9", "P. putida KT2440 (the gene under review)"),
    ("P99088", "S. aureus N315 (second pathogen control)"),
]
# The internal plasmin(ogen)-binding motif reported for pneumococcal enolase.
MOTIF = "FYDKERKVYD"


def fetch(accession: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.json"
    with urllib.request.urlopen(url) as handle:
        return json.load(handle)["sequence"]["value"]


def main() -> None:
    from Bio import Align

    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.match_score = 2
    aligner.mismatch_score = -1
    aligner.open_gap_score = -5
    aligner.extend_gap_score = -0.5

    ref_acc, ref_label = REFERENCE
    ref = fetch(ref_acc)
    start = ref.find(MOTIF)
    print(f"Reference {ref_acc} ({ref_label}); length {len(ref)}")
    if start < 0:
        print(f"  MOTIF {MOTIF} NOT FOUND in the reference -- cannot map. Stopping.")
        return
    print(f"  motif {MOTIF} found at residues {start + 1}-{start + len(MOTIF)}")
    print(f"  reference C-terminal 6 residues: {ref[-6:]}")
    print()

    for acc, label in QUERIES:
        seq = fetch(acc)
        alignment = aligner.align(ref, seq)[0]
        ref_idx, seq_idx = alignment.aligned
        mapped = []
        for (r0, r1), (s0, s1) in zip(ref_idx, seq_idx):
            for offset in range(r1 - r0):
                rpos = r0 + offset
                if start <= rpos < start + len(MOTIF):
                    mapped.append((rpos, s0 + offset))
        identity = sum(
            1
            for (r0, r1), (s0, s1) in zip(ref_idx, seq_idx)
            for o in range(r1 - r0)
            if ref[r0 + o] == seq[s0 + o]
        )
        aligned_len = sum(r1 - r0 for r0, r1 in ref_idx)
        print(f"{acc} ({label}); length {len(seq)}")
        print(f"  identity to reference: {identity}/{aligned_len} = {100 * identity / aligned_len:.1f}%")
        if not mapped:
            print("  motif region: no aligned residues (gapped out)")
        else:
            found = "".join(seq[s] for _, s in mapped)
            expect = "".join(ref[r] for r, _ in mapped)
            matches = sum(1 for a, b in zip(expect, found) if a == b)
            lo = mapped[0][1] + 1
            hi = mapped[-1][1] + 1
            print(f"  motif region maps to residues {lo}-{hi}")
            print(f"    reference : {expect}")
            print(f"    query     : {found}")
            print(f"    identical : {matches}/{len(expect)}")
            print(f"    lysines in query region: {found.count('K')} (reference has {expect.count('K')})")
        print(f"  C-terminal 6 residues: {seq[-6:]}")
        print()


if __name__ == "__main__":
    main()
