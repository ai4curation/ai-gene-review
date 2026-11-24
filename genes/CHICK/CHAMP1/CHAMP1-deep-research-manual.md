# CHAMP1 (Gallus gallus, UniProt A0A8V0YM97) - manual literature research

No deep-research provider was run (no API keys in this environment). This file
summarizes literature work done manually from cached publications and PubMed searches.

## Identity

- UniProt A0A8V0YM97 (TrEMBL, unreviewed), gene CHAMP1, GeneID 418733, chicken
  chromosome 1; 948 aa. Human ortholog Q96JM3 (812 aa; Ensembl Compara source of all
  chicken GOA rows: ENSP00000354730).
- Family: PANTHER PTHR37354 (CHROMOSOME ALIGNMENT-MAINTAINING PHOSPHOPROTEIN 1);
  InterPro IPR039330 (CAMP), IPR063396 (CHAMP1_N), IPR063349 (Znf-C2H2_CHAMP1_1).
  All UniProt free-text (function, subunit, location) in the chicken entry is ARBA-derived
  and is not used as evidence.

## Literature

PubMed search `(CHAMP1 OR ZNF828 OR C13orf8) AND (chicken OR Gallus OR avian)` returned one
paper, PMID:26703087 (Bluhm et al. 2016, Proteomics, abstract-only in cache):
histone-peptide pull-downs with chicken and zebra finch nuclear extracts; "we found ZNF462,
ZNF828 and POGZ enriched at H3K9me3". This is the only chicken experimental datum on
CHAMP1/ZNF828; it parallels the human CHAMP1-POGZ-HP1 complex (PMID:20850016, PMID:39962076).

All functional characterization is in human cells:

- PMID:21063390 (Itoh et al. 2011 EMBO J; abstract only in cache, full text not returned by
  PMC tool). CAMP "localizes to chromosomes and the spindle including kinetochores", is
  phosphorylated in mitosis in a CDK1-dependent manner; depletion causes misalignment with
  "poor resistance of K-fibres to the tension exerted upon establishment of sister kinetochore
  bi-orientation"; FPE region needed for spindle/kinetochore localization; CENP-E and CENP-F
  kinetochore localization affected by depletion.
- PMID:28887307 (Hara et al. 2017 JBC): MAD2L2-CAMP crystal structure; human CAMP W334/K335/P341
  WK motif required for MAD2L2 binding; "Wild-type MAD2L2 was co-localized with full-length
  CAMP in the mitotic spindle and mitotic chromosomes"; MAD2L2 mutants still localize to the
  spindle, implying other spindle partners.
- PMID:36044844 (Li et al. 2022 Cell Rep): "CHAMP1 binds directly to REV7" and promotes HR by
  competing with SHLD3; REV7 and CHAMP1 colocalize "in nuclear foci".
- PMID:39962076 (Li et al. 2025 Nat Commun): CHAMP1-POGZ-HP1alpha complex "is enriched in
  heterochromatin"; promotes heterochromatin assembly and HDR at ALT telomeres.
- PMID:41481470 (Li et al. 2026 PNAS): complex with SETDB1 recruited to stalled forks,
  reduces replication stress.
- PMID:41540007: CHAMP1 coactivates MyoD at the MYMK enhancer in human myoblasts.

## Key paper requested by the workflow

PMID:22448145 (Bayat et al. 2012 PLoS Biol) was requested as a key CHAMP1 paper. It was
read: it is about mitochondrial methionyl-tRNA synthetase (Drosophila Aats-met / human
MARS2) and ARSAL ataxia, and contains no mention of CHAMP1, CAMP, ZNF828, C13orf8 or
kinetochores (grep count 0). It is not relevant to CHAMP1 and is not cited in the review.

## Sequence comparison (own analysis)

See `CHAMP1-bioinformatics/RESULTS.md`: 56.9% identity to human over human length;
N-terminal (78%) and C-terminal zinc-finger (92%) windows conserved; the central WK/SPE/FPE
repeat region diverged (6 WK motifs in chicken vs 13 in human; no exact counterpart of the
human REV7-binding WK motif in a simple scan).
