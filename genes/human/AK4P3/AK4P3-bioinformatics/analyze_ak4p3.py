#!/usr/bin/env python3
"""Is human AK4P3 an over-annotated pseudogene, or a functional AK4 duplicate?

AK4P3 carries 19 GO annotations describing a working mitochondrial adenylate kinase — EC
2.7.4.10 and 2.7.4.6, AMP kinase activity, mitochondrial matrix — every one of them IEA or IBA,
applied by automatic pipelines (chiefly HAMAP-Rule MF_03170) on sequence similarity to AK4.

But HGNC names the locus "adenylate kinase 4 pseudogene 3" with locus_type `pseudogene`.

Those two things cannot both be casually true, so this script asks what the sequence says:

1. How similar is the AK4P3 ORF to genuine human AK4 (P27144), and is the catalytic P-loop intact?
   A pseudogene with a disrupted active site would settle the question immediately.
2. If the protein is near-identical, can mass spectrometry tell the two apart at all? UniProt
   assigns AK4P3 PE=1 ("evidence at protein level") with a PeptideAtlas cross-reference, and
   peptide-to-protein assignment between near-identical paralogs is exactly where that can go
   wrong. The test is whether any fully tryptic peptide is unique to AK4P3.
3. Does AK4P3 carry AK4's inactivating active-site residue? AK4 has no adenylate kinase
   activity in vitro because it has a glutamine at position 159 where other adenylate kinases
   have a conserved arginine, and the Q159R mutation restores activity with GTP (PMID:19130895).
   An intact P-loop says nothing about this residue, so it is checked separately.

Nothing is hardcoded: sequences are fetched live from the UniProt REST API and the comparison and
digest are computed. The script reports what it finds and draws no conclusion the data does not
carry.
"""

from __future__ import annotations

import json
import sys
import urllib.request

AK4P3 = "A0A8I5KW96"   # TrEMBL, gene symbol AK4P3
AK4 = "P27144"         # Swiss-Prot, genuine human AK4
MIN_PEPTIDE_LEN = 7    # below this, a tryptic peptide is not usefully identifying
AK4_Q159 = 159         # AK4's Gln in place of the conserved catalytic Arg (PMID:19130895)


def fetch_seq(accession: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.json"
    with urllib.request.urlopen(url) as fh:
        return json.load(fh)["sequence"]["value"]


def tryptic(seq: str) -> list[str]:
    """Fully tryptic digest: cleave after K or R, but not before P."""
    peptides, current = [], ""
    for i, residue in enumerate(seq):
        current += residue
        if residue in "KR" and not (i + 1 < len(seq) and seq[i + 1] == "P"):
            peptides.append(current)
            current = ""
    if current:
        peptides.append(current)
    return peptides


def p_loop(seq: str) -> tuple[int, str] | None:
    """Locate the Walker A / P-loop motif GxxGxGK."""
    import re
    m = re.search(r"G..G.GK", seq)
    return (m.start() + 1, m.group(0)) if m else None


def main() -> int:
    a, b = fetch_seq(AK4P3), fetch_seq(AK4)
    print(f"{AK4P3} (AK4P3): {len(a)} aa")
    print(f"{AK4}   (AK4)  : {len(b)} aa\n")

    if len(a) != len(b):
        print("Lengths differ; a positional comparison is not meaningful. Stopping.")
        return 1

    diffs = [(i + 1, b[i], a[i]) for i in range(len(a)) if a[i] != b[i]]
    ident = len(a) - len(diffs)
    print(f"Identity: {ident}/{len(a)} ({100 * ident / len(a):.1f}%)")
    print(f"Differences (position, AK4 -> AK4P3): {diffs or 'none'}\n")

    for label, seq in ((f"AK4  ", b), ("AK4P3", a)):
        loc = p_loop(seq)
        print(f"  {label} P-loop: {loc[1]} at {loc[0]}" if loc else f"  {label} P-loop: ABSENT")
    print()

    ctx = slice(AK4_Q159 - 4, AK4_Q159 + 3)
    for label, seq in ((f"AK4  ", b), ("AK4P3", a)):
        print(f"  {label} residue {AK4_Q159}: {seq[AK4_Q159 - 1]} (context {seq[ctx]})")
    print()

    pa, pb = tryptic(a), tryptic(b)
    sa, sb = set(pa), set(pb)
    uniq_a = sorted(p for p in sa - sb if len(p) >= MIN_PEPTIDE_LEN)
    uniq_b = sorted(p for p in sb - sa if len(p) >= MIN_PEPTIDE_LEN)
    print(f"Fully tryptic peptides: AK4P3 {len(pa)}, AK4 {len(pb)}; shared {len(sa & sb)}")
    print(f"Peptides >={MIN_PEPTIDE_LEN} aa unique to AK4P3: {uniq_a or 'NONE'}")
    print(f"Peptides >={MIN_PEPTIDE_LEN} aa unique to AK4  : {uniq_b or 'NONE'}\n")

    print("--- Reading ---")
    if not diffs:
        print("  The two ORFs are identical. Nothing in the protein sequence can distinguish them.")
    elif p_loop(a) and ident / len(a) > 0.95:
        print("  The AK4P3 ORF is near-identical to AK4 with the catalytic P-loop intact, so the")
        print("  sequence gives NO evidence of pseudogenisation at the protein level. Whether the")
        print("  locus is expressed and translated is a separate question this analysis cannot answer.")
    if a[AK4_Q159 - 1] == b[AK4_Q159 - 1] == "Q":
        print(f"  AK4P3 keeps AK4's Gln{AK4_Q159}, the residue that makes AK4 inactive as an adenylate")
        print("  kinase in vitro. The sequence therefore predicts AK4's enzymology, which is NOT an")
        print("  active AMP kinase.")
    elif a[AK4_Q159 - 1] == "R":
        print(f"  AK4P3 has Arg at {AK4_Q159}, the substitution that restores AK4 activity.")
    else:
        print("  See the differences above.")
    if uniq_a:
        print(f"  {len(uniq_a)} tryptic peptide(s) are unique to AK4P3, so proteomic evidence CAN in")
        print("  principle be attributed to it rather than to AK4 — PE=1 is not necessarily a")
        print("  misassignment. Confirming it requires checking whether those specific peptides were")
        print("  the ones observed.")
    else:
        print("  No tryptic peptide is unique to AK4P3, so any proteomic 'evidence at protein level'")
        print("  for it could equally be AK4 peptides. PE=1 would then be unsafe.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
