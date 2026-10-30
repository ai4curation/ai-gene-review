# BT_3328 (Q8A2H7, BtCDH, PL29) notes

## 2026-10-30 origin

Reviewed from the KBase Dark Protein Atlas (gene-annotate dashboard), query
`CAKXSP010000006.1_105`, an environmental *B. thetaiotaomicron* protein that
eggNOG and InterPro annotate only as DUF4955. It is 98.8% identical to BT_3328
over its full 868 aa (see `BT_3328-bioinformatics/RESULTS.md`). The
dashboard's LLM call was "PL29 glycosaminoglycan endolyase cleaving hyaluronic
acid, chondroitin sulfate, and dermatan sulfate by beta-elimination, with a
physiological role in hyaluronic acid utilization", with GO:0030340,
GO:0034000 and GO:0030214. UniProt Q8A2H7 is unreviewed ("DUF4955
domain-containing protein") and GOA has no annotations at all.

## Literature

- Ndeh et al. 2018 [PMID:30262663]: founding member of PL29. Recombinant
  BtCDH degrades CS, DS and HA; on HA it gives Delta4,5-unsaturated di- to
  octasaccharides and is classed as endo-acting. Proteinase K shaving and
  immunofluorescence show it on the cell surface; it has an N-terminal
  lipidation sequence. Only slightly affected by EDTA and divalent metals.
  The deletion mutant still degrades CS outside the cell, so other surface CS
  lyases exist.
- Ndeh et al. 2020 [PMID:32005816]: in the CS/DS/HA PUL, BT3328 is the
  surface lyase; activity and affinity CS-A > CS-C > HA "and little activity
  on DS, differing from previous data". It cleaves HA oligosaccharides only
  at DP >= 8 and "cleaves glycans from the reducing end". Co-IP shows it
  interacting with the SGBPs BT3329 and BT3330 at the cell surface.
- Liu et al. 2021 [PMID:33657378]: RB-TnSeq; BT3328 "was only important for
  fitness on HA, despite the activity of this enzyme against both HA and CS
  in vitro".
- Overbeeke et al. 2022 [PMID:36523841]: all tested HA-degrading
  *Bacteroides* strains carry BT_3328 and all non-degraders lack it.

## Decisions

- **MF.** The DS activity is contested between the two Ndeh papers, so I did
  not use GO:0034000 chondroitin-sulfate-ABC endolyase activity, whose
  definition explicitly covers iduronate (DS) linkages. GO:0030341
  chondroitin AC lyase activity (hexosaminyl-glucuronate linkages: CS-A, CS-C
  and HA) matches the substrate set both papers agree on. GO:0030340
  hyaluronate lyase activity is added as well, because HA is the
  physiologically relevant substrate. Neither EC-style definition captures the
  endo-acting mode exactly; that is a limitation of the terms.
- **BP.** GO:0030214 hyaluronan catabolic process, supported by the enzyme's own
  catalysis of HA at the cell surface (IDA), not by a growth requirement. The
  pooled RB-TnSeq HA signal [PMID:33657378] conflicts with the clean deletion
  strain, which grows normally on HA in pure culture [PMID:30262663, and
  PMID:32005816 "no impact on growth was observed, consistent with Δbt3328
  mutant growth data"]; PMID:32005816 assigns the required HA lyase role to
  BT4410. Recorded as an open question; it does not affect participation.
  GO has no "chondroitin sulfate catabolic process"
  (only the proteoglycan term GO:0030207, which is wrong for dietary free CS
  chains), and GO:0006027 glycosaminoglycan catabolic process is an ancestor of
  the HA term, so I did not add it. Raised as a question.
- **CC.** GO:0009986 cell surface by IDA. GO:0009279 cell outer membrane by IC:
  a lipoprotein with a surface-exposure signal that proteinase K can reach
  from outside, which in Bacteroidetes means anchored in the outer leaflet of
  the outer membrane.

## 2026-10-30 correction

An earlier draft of this review said the gene is "required for growth on
hyaluronan" and annotated GO:0030214 by IMP from the RB-TnSeq fitness data. That
overstated the genetics: both Ndeh papers report that the clean ΔBtCDH strain
grows like wild type on HA, CS-A, CS-C and DS in pure culture. The term is kept,
now by IDA on the enzyme's own catalysis, and the discrepancy with the pooled
fitness screen is recorded as an open question.

## DUFMech

PF16315 (DUF4955) and PF16378 (DUF4988) were both SEEDED/UNSCORED stubs in
DUFMech with no curation overlay. Contributed an overlay for PF16315:
https://github.com/CultureBotAI/DUFMech/pull/385. One MECHANISTIC causal graph
for BtCDH, with no edge assigning the chemistry to the DUF4955 interval, because
the assayed construct is the mature full-length protein and residues 200-715
carry no Pfam match. PF16378 got no edge: it also matches the non-enzymatic
surface glycan-binding protein BT3329 (Q8A2H6, 25-207, 3.7e-92), so it reads as
a shared surface module.
