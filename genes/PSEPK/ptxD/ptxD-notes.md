# ptxD (PP_3376, Q88HI1) evidence notes

## 2026-10-15 — re-review after OpenScientist TreeGrafter control batch

The blinded OpenScientist stress test of GO:0030267
[file:PSEPK/ptxD/ptxD-hypotheses/function-hypothesis-go-0030267/openscientist.md
"By independent global pairwise alignment the 320-aa query is **53.4% identical to the biochemically characterized *E. coli* GhrB**"]
judged the TreeGrafter graft sound and recommended keeping GO:0030267 and
adding GO:0016618. It was blinded to gene context.

Checks made in this re-review (scratch alignments, Biopython PairwiseAligner,
global, BLOSUM62, gap open -10 / extend -0.5; identities as % of the 320-aa
query; sequences from UniProt REST):

- Q88HI1 vs E. coli GhrB P37666: 170/320 = 53.1%
- Q88HI1 vs human GRHPR Q9UBQ7: 128/320 = 40.0%
- Q88HI1 vs P. stutzeri PtxD O69054: 123/320 = 38.4% (report: 35.1%)
- PtxD residue mapping onto Q88HI1: Lys76 -> Val75, Tyr139 -> Phe139,
  Arg237 -> Arg237, Glu266 -> Glu266, His292 -> His285. GMGRIG begins at
  Q88HI1 position 152.
- O69054 position 314 is Gln, and O69054 has Trp only at 92, 134, 167, 268,
  so the report's "PtxD Trp314 -> Ser307" claim is not reproduced.

UniProt P37666 (GhrB, Swiss-Prot) lists EC 1.1.1.79, EC 1.1.1.81 and
EC 1.1.1.215 (2-ketogluconate reductase, RHEA:16653), so the subfamily is
promiscuous across 2-oxoacids including a 2-ketoaldonate.

KEGG (rest.kegg.jp, ppu): PP_3376 is K00032 phosphogluconate 2-dehydrogenase
(EC 1.1.1.43); PP_3377 putative 2-ketogluconate transporter; PP_3378 putative
2-ketogluconokinase (K11441); PP_3379 putative epimerase; PP_3380
2-ketogluconate utilization repressor (PtxS). This is the kguEKTD-ptxS
arrangement described for Pseudomonas [PMID:29607620 "kguT, kguK and kguD that
form another operon with ptxS"].

Decision: the report and the earlier review agree on the facts (GhrB-type,
active, not PtxD) and differ on interpretation (glyoxylate/hydroxypyruvate
reductase vs KguD). GO:0030267 and GO:0016618 stay UNDECIDED; the GO:0050609
REMOVE is reinforced. No new MF term is needed: GO:0008114 already covers the
KguD reaction (EC 1.1.1.43, synonym "2-keto-6-phosphogluconate reductase
activity").

## 2026-11-21: trusted-cutoff follow-up (no action change)

The Enzyme Specificity cutoff check placed the hydroxypyruvate and glyoxylate reductase
rows below cutoff, but it scored only NCBIfam's GhrA model (80.8 / 403), and Q88HI1
resembles GhrB, not GhrA (53.1% identity to E. coli GhrB P37666 and PANTHER subfamily
PTHR10996:SF283; the identity is recorded above and the subfamily in the review
YAML). A follow-up scored the GhrB model NF011938.0, which carries no EC number and
so was never a target: Q88HI1 scores 418.1 against a trusted cutoff of 492,
E. coli GhrB passes at 690.3, and no KT2440 protein passes it, with Q88HI1 the closest
[file:projects/ENZYME_SPECIFICITY/cutoff-check/followup.yaml "flagged_protein_score: 418.1"].
So Q88HI1 is GhrB-related but outside the GhrB equivalog, and there is no other KT2440
GhrB that would make it a paralog. The scores do not decide between the KguD role and a
GhrB-type glyoxylate or hydroxypyruvate side activity; both rows stay UNDECIDED pending
the substrate panel already proposed.
