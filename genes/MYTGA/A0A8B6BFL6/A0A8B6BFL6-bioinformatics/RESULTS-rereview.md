# A0A8B6BFL6 re-review: sequence comparison with PTHR33050:SF7 members

Script: `compare_sequences_rereview.py` (run with `uv run compare_sequences_rereview.py`);
raw output in `compare_sequences_rereview.out`. Sequences were downloaded from the UniProt
REST API on 2026-10-21 into this folder.

## Comparators and why they were chosen

UniProt places A0A8B6BFL6 in PANTHER PTHR33050:SF7. The same subfamily contains the
Dictyostelium discoideum DIRS-1 ORF2 product (O96849 / Q23898, 608 aa, CDD cd03714
RT_DIRS1 + cd09275 RNase_HI_RT_DIRS1) and the hepadnavirus polymerase P proteins (e.g. DHBV
P03162). The DIRS-1 tyrosine recombinase (ORF3, O96848) is a separate protein in another
PANTHER family (PTHR31660) and is included as a negative control.

## Results (Smith-Waterman, BLOSUM62, gap open -11 / extend -1; 50 shuffled-subject controls)

| Subject | Score | Target span | Subject span | Identity | z vs shuffle |
|---|---|---|---|---|---|
| O96849 DIRS-1 ORF2 RT/RNase H | 283 | 159-577 | 37-447 | 26.4% over 397 columns | 51.7 |
| P03162 DHBV polymerase P | 65 | 236-395 | 496-656 | 22.2% over 158 columns | 6.8 |
| O96848 DIRS-1 ORF3 tyrosine recombinase | 36 | 199-246 | 213-256 | 38.1% over 42 columns | -0.7 (noise) |

Motif scan of the target:

- RT motif C (Y-x-D-D): `YLDD` at 300-303, inside the Pfam RVT_1 domain (174-349).
  A second match (`FPDD`, 135) lies outside the RT domain and is not interpreted.
- A candidate first RNase H carboxylate in an `SDA` context at 463-465, inside the region that
  aligns to the DIRS-1 ORF2 RNase H.

## Interpretation

- The target aligns with DIRS-1 ORF2 continuously across both the RT and the RNase H regions
  (target 159-577 vs DIRS-1 ORF2 37-447). That is the DIRS-1 RT-RNase H unit. The hepadnavirus
  polymerase match is weaker and covers only the RT core.
- The C-terminal Dam-like methyltransferase region of DIRS-1 ORF2 (Pfam PF05869, after residue
  ~450) has no aligned counterpart in the target, and UniProt records no methyltransferase
  signature for it.
- The target has no detectable similarity to the DIRS-1 tyrosine recombinase. Because DIRS
  elements encode the YR as a separate ORF, this protein is not expected to carry recombinase
  or integration activity itself.
- The YLDD motif C in the RT palm is intact, so the polymerase active site is plausibly
  retained. This is a sequence-level observation, not an activity assay.
- These alignments do not show whether the encoding element is intact or mobile.
