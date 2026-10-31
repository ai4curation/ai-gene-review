# GGAT2 (At1g70580, Q9S7E9) curation notes

**Deep research could not be run** in this environment (no provider API keys). These notes are a
literature summary built only from cached publications (`publications/PMID_*.md`), the UniProt
record (`GGAT2-uniprot.txt`) and PubMed searches. No `*-deep-research-*.md` file exists for this
gene.

## Literature search

- PubMed searches for `GGAT2`, `GGT2`, `AOAT2`, `At1g70580` and "glutamate:glyoxylate
  aminotransferase Arabidopsis" (2026-10-20) return only three papers that study this locus:
  Liepman & Olsen 2003 (PMID:12529529), Igarashi et al. 2003 (PMID:12631323) and Igarashi et al.
  2006 (PMID:16950862). The Arabidopsis Book review (PMID:22303256) summarizes them.
- Name collision: most PubMed hits for "GGT2" in Arabidopsis are the unrelated apoplastic
  gamma-glutamyl transpeptidase GGT2 (At4g39650; e.g. PMID:17316175, PMID:17545509,
  PMID:20959624). These say nothing about At1g70580 and are not used.
- No ggat2 single mutant, ggat1 ggat2 double mutant, GGAT2 reporter-fusion localization or GGAT2
  overexpression study was found.

## What is known for GGAT2 itself (GGAT2-specific evidence)

- **Enzyme activity of the recombinant protein.** GGT2 cDNA was cloned, expressed in E. coli and
  purified; the purified protein catalyses GGT, GPT and AKT reactions with measured kinetics
  [PMID:12529529 "Recombinant GGT2 was soluble when expressed in E. coli ; lysates of bacteria
  expressing this construct exhibited significantly increased levels of GGT, GPT, and AKT activity
  compared with empty vector controls"]; [PMID:12529529 "Both purified recombinant proteins
  catalyzed GGT, GPT, and AKT reactions"]. AGT activity was detected but not characterized
  kinetically [PMID:12529529 "Both recombinant proteins and the purified plant protein displayed
  AGT activity (data not shown), but this activity was not characterized kinetically because of
  technical limitations of the AGT assay."]. No SGT or AspAT activity [PMID:12529529 "Neither of
  the purified recombinant GGTs nor the purified Arabidopsis protein exhibited SGT or AspAT
  activity (data not shown)."].
- UniProt kinetics for GGAT2 (from PMID:12529529): Km 3.32 mM glutamate, 3.56 mM alanine,
  0.14 mM glyoxylate, 0.51 mM 2-oxoglutarate, 0.36 mM pyruvate [file:ARATH/GGAT2/GGAT2-uniprot.txt
  "KM=0.14 mM for glyoxylate"].
- **Sequence.** 93% identical to GGAT1, 481 aa, class-I aminotransferase with a C-terminal PTS1
  [PMID:12529529 "Analysis of the GGT1 and GGT2 sequences revealed that these proteins are 93%
  identical and 99% similar at the amino acid level."]; UniProt motif 479..481 "Peroxisomal
  targeting signal" (C-terminus ...GYSRM; GGAT1 ends ...GYSKM).
- **Localization.** No GGAT2-specific fusion-protein localization exists. The GGAT2-specific
  evidence is proteomic: in purified mature leaf peroxisomes the second GGT isoform was identified
  from isoform-specific peptides [PMID:17951448 "Of the two isoforms each of Glu-glyoxylate
  aminotransferase (GGT) and peroxisomal malate dehydrogenase (pMDH), GGT1 (At1g23310; SKM>) and
  pMDH2 (At5g09660; RIx 5 HL) dominated over the second isoform, both of which were identified as
  well and are thus not restricted to nonphotosynthetic tissue"]. Seedling GGT activity is
  exclusively peroxisomal and is taken to be the sum of both isoforms [PMID:12529529 "The GGT
  activity observed in Arabidopsis peroxisomes is likely the sum of the contributions from GGT1 and
  GGT2 because both catalyze this reaction."]. The GFP-PTS1 targeting experiment was done with
  AOAT1 only [PMID:12631323 "When AOAT1 fused to green fluorescent protein (GFP) was expressed in
  BY-2 cells, it was found to be localized to peroxisomes depending on PTS1."].
- **Expression.**
  - EST abundance is far lower than for GGAT1 [PMID:12529529 "Only two potential EST sequences
    corresponding to GGT2 were discovered, including a single potential full-length cDNA."], and
    Igarashi 2003 judged AOAT1 the major leaf isoform [PMID:12631323 "The expression analysis of
    mRNA encoding AOATs and EST information suggested that AOAT1 was the major protein in green
    leaves."].
  - RT-PCR: GGT2 transcripts in light-grown seedlings, leaves, siliques and roots, but not in 4-d
    dark-grown seedlings [PMID:12529529 "GGT2 transcripts were not detected in 4-d-old dark-grown
    seedlings"]. Note the conflict on roots: Liepman & Olsen found only GGT2 transcripts there
    [PMID:12529529 "only GGT2 transcripts were detected in roots, where GGT1 transcripts were not
    observed"], whereas Igarashi 2006 saw strong root GUS for GGAT1 [PMID:16950862 "In GGAT1 - GUS
    seedlings, GUS signals were also strongly detected in roots"].
  - Promoter-GUS: strong leaf expression for GGAT2 [PMID:16950862 "GUS stain was strongly detected
    in leaves of both GGAT1 - and GGAT2-GUS seedlings ( Fig. 1A ), which suggests that GGAT1 and
    GGAT2 function as photorespiratory GGAT enzymes."].
  - Diurnal/light: GGAT2 mRNA rises on illumination while GGAT1 falls, and leaf GGAT activity stays
    constant [PMID:16950862 "After light exposure, the levels of GGAT1 mRNA decreased and those of
    GGAT2 mRNA increased rapidly"]; [PMID:16950862 "However, the enzymatic activity of GGAT remained
    constant during the day ( Fig. 2A ), suggesting that GGAT1 and GGAT2 may function redundantly
    in leaf photorespiration."]; review: [PMID:22303256 "Whereas Ggat 2 is induced at the beginning
    of the photoperiod, Ggat 1 is rather repressed."].
- **Mutants.** None for GGAT2. Its in vivo contribution is inferred indirectly from the ggat1
  knockout, which retains a little GGAT activity [PMID:22303256 "Residual GGAT activity can be
  detected in mutant leaf extracts ( Igarashi et al., 2003 )."], and whose weak phenotype "might not
  be fully explained by the residual low activity of GGAT2" [PMID:22303256]. ggat1 mutants in air
  still accumulate glyoxylate [PMID:26216646 "When compared to wild-type (WT) plants, air-grown
  ggt1 plants exhibited glyoxylate accumulation"], so GGAT2 cannot substitute for GGAT1 at normal
  expression levels.

## What is inferred from GGAT1 (not shown for GGAT2)

- PTS1-dependent peroxisomal import (GFP shown only for AOAT1).
- Genetic necessity for photorespiration and the high-CO2-rescuable growth phenotype (ggat1 only).
- Homodimer, PLP Lys291 (UniProt ECO:0000250, by similarity).

## Judgements

- Core MF: GO:0047958 glycine:2-oxoglutarate transaminase activity (the GGT reaction, written in
  reverse) — directly shown on purified recombinant GGAT2. Ala:2-oxoglutarate (GO:0004021) and
  Ala:glyoxylate (GO:0008453) are genuine, non-core (same as GGAT1).
- Location: peroxisome (GGAT2-specific peptides in leaf peroxisome proteome; PTS1; activity
  fractionation). Chloroplast, stroma, mitochondrion and crude-cytosol proteomics hits are
  marked over-annotated per projects/ARATH/organelle-audit.md rule 3.
- Process: GOA carries no photorespiration annotation for GGAT2 (GGAT1 has a TAS). The
  GGAT2-specific evidence is the enzyme catalysing the step itself, isoform-specific detection in
  mature leaf peroxisomes, strong leaf promoter activity and light induction, plus constant leaf
  GGAT activity during the day while GGAT1 mRNA falls. This passes the participation test (GGAT2
  catalyses the photorespiratory transamination itself; it is not a substrate) and the
  comparator test (photorespiration is carried by the other enzymes of the cycle, including
  GGAT1). Proposed as NEW (IC). Genetic proof is lacking (no ggat2 or double mutant), so the
  contribution is described as minor and partially redundant with GGAT1.
- mRNA binding (RBPome hit) and L-alanine catabolic process (UniPathway) are marked
  over-annotated, as for GGAT1.

## Module comparison (modules/photorespiration_c2_cycle.yaml, ggat_step)

GGAT2 is listed as a second representative member of the GGAT step (GO:0047958, GO:0009853,
GO:0005777). GGAT2-specific evidence supports the activity (purified recombinant enzyme) and the
location (isoform-specific peroxisome proteomics). Participation in photorespiration rests on
expression and biochemical evidence, not genetics; listing it as a minor/secondary representative
is reasonable, but the module text already notes GGAT1 as the main isoform.
