# PP_1969 curation notes

## 2026-07-20 OpenScientist report assessment

The generated OpenScientist report is retained unchanged as provider output but is
assessed as `MISCITED` for target-level curation. It declares Q88LG4 canonical MoaA
and an exact GTP 3',8'-cyclase despite the absence of a PP_1969 assay
[file:PSEPK/PP_1969/PP_1969-deep-research-openscientist.md, "PP_1969 encodes **MoaA**"];
that catalytic conclusion is not propagated.

The report also states `moaB = PP_1294` and `mogA = PP_3457`. Local target records
show that PP_1294 is `moaE`, the molybdopterin synthase catalytic subunit
[file:PSEPK/moaE/moaE-uniprot.txt, "GN   Name=moaE"] and that PP_3457 is reviewed
`mobA`, the molybdenum cofactor guanylyltransferase
[file:PSEPK/mobA/mobA-uniprot.txt, "GN   Name=mobA"]. The report's residue-numbered
motif analysis was not saved as a reproducible local analysis and is not used as
evidence.

The curation decision remains conservative: Q88LG4 is a divergent MoaA-like
radical-SAM candidate. Its exact substrate, GTP 3',8'-cyclase activity, and pathway
necessity remain `UNDECIDED`, grounded in the target UniProt record and the saved
local sequence comparison rather than the provider's catalytic claims.

## 2026-10-15 Re-review of GO:0061798 after OpenScientist control batch

A blinded OpenScientist hypothesis run (batch openscientist-controls-2026-10-14,
local bioinformatics withheld) judged GO:0061798 supported
[file:PSEPK/PP_1969/PP_1969-hypotheses/function-hypothesis-go-0061798/openscientist.md,
"**Verdict: SUPPORTED.** PP_1969 (UniProt Q88LG4, *Pseudomonas putida* KT2440) is a"].

Checked against repository data:

- UniProt Q88LG4 carries PTHR22960:SF0, PF06463 Mob_synth_C and IPR010505
  MoaA_twitch, the same PANTHER subfamily as reviewed Q88E69
  [file:PSEPK/PP_1969/PP_1969-uniprot.txt, "DR   PANTHER; PTHR22960:SF0; MOLYBDENUM COFACTOR BIOSYNTHESIS PROTEIN 1; 1."].
- The run's cluster cysteines (C36/C40/C43, C268/C271/C285) match the local motif
  table in `genes/PSEPK/moaA/moaA-bioinformatics/moaA_features.tsv` (36; 40;268).
- New analysis `PP_1969-bioinformatics/` maps every UniProt binding residue of
  Q88E69 onto the paralogs: all seven GTP, four SAM and six cluster positions are
  identical, except V266, which is Leu here as in E. coli MoaA
  [file:PSEPK/PP_1969/PP_1969-bioinformatics/RESULTS.md, "The divergence of PP_1969 and PP_2482 from canonical KT2440 MoaA does not touch the annotated GTP-, SAM- or cluster-binding residues."].
  The PROSITE PS01305 miss is two substitutions at non-ligand positions (CNYAC).
- The earlier analysis and the run agree on the facts; they differed on how much
  weight the missing MoaA-specific signatures (TIGR02666, HAMAP MF_01225,
  PS01305) carry. Why TIGR02666/HAMAP do not match was not examined.

Decision: GO:0061798 UNDECIDED -> ACCEPT; GO:0006777 UNDECIDED -> ACCEPT (follows
from the activity); GO:0003824 UNDECIDED -> TOO_GENERAL. GO:0061799 stays REMOVE.

Not verified / leads only: the run's literature (PMID:16632608, PMID:41183211) is
not cached; its AlphaFold SG-SG distances were not re-run. In-vivo division of
labour between the three MoaA paralogs remains unknown.

## 2026-10-16 Re-examination of GO:0061798 against TIGR02666 / MF_01225

Reviewer objection: both paralogs lack NCBIfam TIGR02666 and HAMAP MF_01225, the
models behind the GTP 3',8-cyclase name and EC 4.1.99.22 of Q88E69; the ACCEPT
leaned on shared PANTHER PTHR22960:SF0, which the PP_3571, gabD-II and PP_4594
re-reviews treated as non-discriminative; and the previous RESULTS.md had not
examined why the models fail.

New analysis (`PP_1969-bioinformatics/model_scores.py`, `context_lookups.py`,
outputs in `model_scores_out/` and `model_scores.out`; dated section in RESULTS.md):

- TIGR02666 (TC 284.05, NC 270.95): Q88E69 375.6 bits; Q88LG4 269.2; Q88K11 268.1;
  reviewed E. coli, S. aureus, both P. aeruginosa MoaA and human MOCS1 370-403;
  KT2440 PqqE 81.0 [file:PSEPK/PP_1969/PP_1969-bioinformatics/RESULTS.md, "Both paralogs score just below the noise cutoff and about 15-16 bits below the trusted cutoff."].
- HAMAP MF_01225_B (level 0 N_SCORE 35.254): Q88E69 39.9; Q88LG4 30.5; Q88K11 30.6;
  all reviewed MoaA pass; the rule's 14 Bacteria FT conditions and size range are
  met by both paralogs [file:PSEPK/PP_1969/PP_1969-bioinformatics/RESULTS.md, "So the HAMAP non-match is a profile-score failure only."].
- Position mapping: all 17 Q88E69 ligand positions on confident match states and
  identical (except V266/Leu); the score loss is spread along the protein, largest
  in model 1-60 and 281-336, with eight positions conserved in all canonical MoaA
  and replaced in both paralogs (Q88E69 F29, R30, E52, V56, R78, P254, K287, H315)
  [file:PSEPK/PP_1969/PP_1969-bioinformatics/RESULTS.md, "None of the score loss is at an annotated ligand position."];
  [file:PSEPK/PP_1969/PP_1969-bioinformatics/RESULTS.md, "The TIGR02666 and MF_01225 non-matches are not explained by a missing non-catalytic segment."].
- InterPro API: TIGR02666, MF_01225_B, PS01305 and CDD cd21117 match Q88E69 and
  E. coli MoaA only.
- Gene context (KEGG, +/- 6 loci): no molybdenum-cofactor or molybdoenzyme gene
  near PP_1969 [file:PSEPK/PP_1969/PP_1969-bioinformatics/RESULTS.md, "PP_1969: no molybdenum-cofactor or molybdoenzyme gene in the window"].

Decision: GO:0061798 ACCEPT -> UNDECIDED; GO:0006777 ACCEPT -> UNDECIDED;
GO:0003824 TOO_GENERAL -> UNDECIDED. GO:0061799 stays REMOVE. The non-match is not
explained as benign, ligand-site conservation does not discriminate a MoaA-derived
paralog [file:PSEPK/PP_1969/PP_1969-bioinformatics/RESULTS.md, "Ligand-site conservation is expected of a MoaA-derived paralog whatever its present substrate, so it cannot by itself separate a GTP 3',8-cyclase from a diverged MoaA-like enzyme."],
and PANTHER SF0 membership is treated as non-discriminative as for PP_3571, gabD-II
and PP_4594. The blinded OpenScientist verdict did not consider these models and is
not adopted. Not done: phylogeny, structure comparison of the eight divergent
positions, any wet-lab test.
