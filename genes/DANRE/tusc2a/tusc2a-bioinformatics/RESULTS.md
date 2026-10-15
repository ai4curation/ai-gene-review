# tusc2a / tusc2b protein, expression and synteny comparison

Script: `pair_analysis.py` (run from the repo root with
`uv run python genes/DANRE/tusc2a/tusc2a-bioinformatics/pair_analysis.py > genes/DANRE/tusc2a/tusc2a-bioinformatics/output.txt`).
Raw output: `output.txt` (run 2026-09-28). Gar-bridge synteny: `gar_bridge.py`, run as
`uv run python genes/DANRE/tusc2a/tusc2a-bioinformatics/gar_bridge.py ENSLOCG00000014230 ENSDARG00000099817 ENSDARG00000025340 > genes/DANRE/tusc2a/tusc2a-bioinformatics/gar_bridge_output.txt`. Zebrafish sequences come from the cached UniProt records
(tusc2a Q08BH0, 111 aa; tusc2b Q6DH03, 111 aa). Human TUSC2 (O75896) comes from UniProt; gar and
medaka proteins are the Ensembl canonical proteins of the orthologues Ensembl Compara assigns (gar
ENSLOCG00000014230, one gar gene for both copies; medaka ENSORLG00000027802 for tusc2a and
ENSORLG00000027402 for tusc2b, each one-to-one). Alignments are Biopython global, BLOSUM62, gap open
-10 / extend -0.5; identity = identical columns / alignment length.

## Protein

| Comparison | Identity |
|---|---|
| tusc2a vs tusc2b | 80.2% (111 columns) |
| tusc2a / tusc2b vs human TUSC2 (O75896, 110 aa) | 70.3% / 65.8% |
| tusc2a / tusc2b vs gar TUSC2 | 81.2% / 77.7% |
| tusc2a vs its medaka orthologue / vs the other medaka copy | 77.5% / 76.6% |
| tusc2b vs its medaka orthologue / vs the other medaka copy | 79.3% / 75.7% |

The protein is short (about 110 residues), so these differences between orthologue and paralogue
distances are only a few residues and do not by themselves resolve the tree.

**Functional features** (from UniProt O75896 and the calcium-binding motif described in
PMID:42314984):

- The N-myristoylation site (Gly2 of human TUSC2) is kept in both copies: both start MGGSGSK.
  The Ensembl gar model starts with one extra residue (KMGGSGSK), so the Gly is at position 3
  there, but it aligns to human Gly2.
- The calcium-binding motif DEDGDLAHEFYEE is present, exactly, in both zebrafish copies (starting
  at residue 55), in human TUSC2, in gar and in both medaka copies.
- The phosphoserine at human Ser50 aligns to Ser in both copies and in gar.
- Over the mature chain (human residues 2-110), tusc2a is 70.6% and tusc2b 66.1% identical to human.

Both copies keep the myristoylation site and the exact calcium-binding motif.

**Relative rate (gar outgroup):** of 111 aligned gar positions, 5 changed only in tusc2a and 9 only
in tusc2b (chi2 = 1.14, not significant).

## Expression

**Whole-embryo time course (E-ERAD-475, median TPM).**

| Stage | tusc2a | tusc2b |
|---|---|---|
| zygote | 26 | 10 |
| 2-cell | 13 | 13 |
| blastula (128-cell to dome) | 5-6 | 31-38 |
| gastrula (50% to 75% epiboly) | 1-2 | 26-38 |
| segmentation | 4-9 | 47-51 |
| pharyngula | 7-11 | 42-45 |
| hatching to larval day 5 | 14-18 | 37-45 |

tusc2a is the larger maternal transcript (26 vs 10 TPM in the zygote) but falls to 1-2 TPM by
gastrulation and recovers only partly (14-18 TPM in larvae). tusc2b is the main zygotic copy,
at 26-51 TPM from blastula to larva.

**Bgee calls** (only "expressed" calls are returned; absence is not proven absence). tusc2a has 25
calls, tusc2b 31. All 22 RNA-Seq-supported entities of tusc2a are also called for tusc2b; RNA-Seq
calls for tusc2b only are heart, ovary and tail. Of 25 entities called for both, tusc2a scores
higher in 4 (median difference tusc2a minus tusc2b = -16.9). tusc2a's highest scores are testis
(89.7) and mature ovarian follicle (87.3); tusc2b's are muscle (91.8), somite and liver.
Gar TUSC2 has 14 calls across adult tissues, embryo and larva, highest in eye, muscle and brain, so
broad expression is the ancestral state.

**ZFIN curated expression.** tusc2a has no curated wild-type expression. tusc2b has one row: whole
organism by in situ hybridization from zygote to pec-fin stage (ZDB-PUB-040907-1), with no
restricted domain recorded.

## Interpretation

- Protein: both copies keep the two features known to matter for TUSC2 (N-myristoyl glycine and
  the calcium-binding motif), and neither is evolving faster. No evidence of protein divergence.
- Expression: overlapping and broad in adults, with tusc2b higher in most tissues. The difference
  is in timing and level: tusc2a is mainly a maternal transcript and a lower-level adult copy with
  its highest calls in gonads; tusc2b carries zygotic expression through development. This is a
  quantitative difference, not a tissue partition. No gar developmental time course was available,
  so whether the maternal/zygotic split is derived cannot be tested here.

## Synteny

**Direct comparison (`pair_analysis.py`, section 7 of `output.txt`).** tusc2a is on chr6 (54.1 Mb)
and tusc2b on chr22 (10.7 Mb). Of 72 protein-coding neighbours of tusc2a (within 1.5 Mb) 30 have a
teleost-level zebrafish paralogue, and of 102 neighbours of tusc2b 16 do, but none of these
paralogue partners lies near the other copy or on the other copy's chromosome. Neighbour-to-neighbour
paralogy therefore gives no signal, probably because most duplicated neighbours were lost from one
side.

**Gar bridge (`gar_bridge.py`; output in `gar_bridge_output.txt`).** Gar TUSC2 is on LG5. Of 52
protein-coding gar genes within 1 Mb, 47 have zebrafish orthologues.

- Near tusc2a (chr6, within 3 Mb): orthologues of 5 gar neighbours, including hyal1 and hyal2a
  (54.06 and 54.09 Mb, next to tusc2a at 54.12 Mb), cacna2d2a and mst1.
- Near tusc2b (chr22, within 3 Mb): orthologues of 6 gar neighbours, including bap1, rad54l2,
  cyb561d2, rassf1, hyal2b and abhd14a (10.59-10.70 Mb, around tusc2b at 10.66 Mb).
- One gar neighbour, hyal2b, has zebrafish orthologues next to both copies (hyal2a beside tusc2a,
  hyal2b beside tusc2b).
- The largest block of gar-neighbour orthologues (24) is on zebrafish chr8, away from both copies.

The gar TUSC2 neighbourhood maps onto two separate zebrafish regions, each holding one tusc2 copy
and a different subset of the ancestral neighbours (a HYAL gene next to each copy, RASSF1 and BAP1
next to tusc2b). This is double conserved synteny, the signature expected of a whole-genome
duplication, and supports a TGD origin of the pair.
