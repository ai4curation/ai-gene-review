# PP_2482 curation notes

## 2026-07-20 OpenScientist report assessment

The generated OpenScientist report is retained unchanged as provider output but is
assessed as `MISCITED` for target-level curation. It declares Q88K11 canonical MoaA,
assigns exact GTP 3',8'-cyclase activity, and calls PP_2482 an essential,
nonredundant gate despite the distinct reviewed canonical KT2440 MoaA Q88E69 and
the unresolved PP_2482/PP_1969 paralog relationship. It also presents unsaved
residue, motif, and neighborhood analyses as decisive evidence. Those claims are
not propagated.

The conservative decision is unchanged: Q88K11 is a divergent MoaA-like
radical-SAM candidate whose physiological substrate, exact catalytic activity, and
necessity remain `UNDECIDED`. This conclusion is grounded in the target UniProt
record and the saved local sequence comparison; the provider report contributes
only its explicit statement that no direct PP_2482 experiment was found.

## 2026-10-15 Re-review of GO:0061798 after OpenScientist control batch

A blinded OpenScientist hypothesis run (batch openscientist-controls-2026-10-14,
local bioinformatics withheld) judged GO:0061798 supported
[file:PSEPK/PP_2482/PP_2482-hypotheses/function-hypothesis-go-0061798/openscientist.md,
"**Verdict: SUPPORTED.** The propagated GO:0061798 annotation is correct and at the appropriate granularity for PP_2482."].

Checked against repository data:

- UniProt Q88K11 carries PTHR22960:SF0, PF06463 and IPR010505, the same PANTHER
  subfamily as reviewed Q88E69.
- The run's cluster cysteines (C21/C25/C28, C253/C256/C270) match the local motif
  table in `genes/PSEPK/moaA/moaA-bioinformatics/moaA_features.tsv` (21; 25;253).
- The site mapping in `genes/PSEPK/PP_1969/PP_1969-bioinformatics/` (covers both
  paralogs) finds all seven GTP, four SAM and six cluster positions of Q88E69
  identical in Q88K11, except V266, which is Leu as in E. coli MoaA
  [file:PSEPK/PP_1969/PP_1969-bioinformatics/RESULTS.md, "The divergence of PP_1969 and PP_2482 from canonical KT2440 MoaA does not touch the annotated GTP-, SAM- or cluster-binding residues."].
- Run errors not imported: it says UniProt annotates binding sites at 21/25/28,
  but the Q88K11 record has no FT BINDING lines; and it calls PP_2483 a MocA,
  whereas the local MobA-like comparison finds PP_2483 closer to E. coli MobA
  despite its K07141 KO.

Decision: GO:0061798 UNDECIDED -> ACCEPT; GO:0006777 UNDECIDED -> ACCEPT (follows
from the activity); GO:0003824 UNDECIDED -> TOO_GENERAL. GO:0061799 stays REMOVE.

Not verified / leads only: the run's literature (PMID:25941396, PMID:30097104,
PMID:26575208, PMID:35480226, PMID:41183211) is not cached; AlphaFold pLDDT values
were not re-run. Paralog division of labour remains unknown.

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
- Gene context (KEGG, +/- 6 loci): PP_2482 ends a same-strand run PP_2477-PP_2481
  (isoquinoline 1-oxidoreductase alpha/beta K07302/K07303, cytochrome c family
  protein, putative xanthine dehydrogenase accessory factor, unknown protein), with
  PP_2483 (K07141) adjacent on the other strand [file:PSEPK/PP_1969/PP_1969-bioinformatics/RESULTS.md, "This is a molybdoenzyme cluster."].
  This is the strongest point for a Moco-related role, but
  [file:PSEPK/PP_1969/PP_1969-bioinformatics/RESULTS.md, "A Moco-related context for PP_2482 is compatible with a dedicated GTP 3',8-cyclase but does not show which reaction it catalyses."]

Decision: GO:0061798 ACCEPT -> UNDECIDED; GO:0006777 ACCEPT -> UNDECIDED (context
noted in the reason); GO:0003824 TOO_GENERAL -> UNDECIDED. GO:0061799 stays REMOVE.
Same reasoning as PP_1969 on the model scores and on PANTHER SF0 being
non-discriminative (as for PP_3571, gabD-II, PP_4594). Added a knockout experiment
testing whether PP_2482 serves its cluster's molybdoenzyme. Not done: phylogeny,
structure comparison, any wet-lab test.
