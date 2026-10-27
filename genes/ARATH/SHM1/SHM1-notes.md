# SHM1 (At4g37930, UniProt Q9SZJ5) - curation notes

**Deep research could not be run** in this environment (no provider API keys).
These notes are a manual literature summary built only from the cached
publications in `publications/`, the UniProt record (`SHM1-uniprot.txt`) and
PubMed searches. No `-deep-research-*.md` file exists for this gene.

## Identity

- UniProt Q9SZJ5 (GLYM1_ARATH), "Serine hydroxymethyltransferase 1, mitochondrial";
  gene SHM1, synonyms SHMT1 and STM (the historical `stm`/`shm` mutant); locus At4g37930.
- EC 2.1.2.1, RHEA:15481; PLP cofactor; SHMT family (PANTHER PTHR11680:SF61,
  "SERINE HYDROXYMETHYLTRANSFERASE 1, MITOCHONDRIAL"); N-terminal transit peptide.
- Seven SHM genes in Arabidopsis; SHM1 and SHM2 are predicted to be mitochondrial
  [PMID:16339799 "The Arabidopsis genome harbors seven putative SHM genes, two of which (SHM1 and SHM2) feature predicted mitochondrial targeting signals"].

## Core function: photorespiratory glycine-to-serine conversion

- Mitochondrial SHMT, together with GDC, converts 2 glycine into CO2, NH4+ and
  serine [PMID:16339799 "Mitochondrial serine hydroxymethyltransferase (SHMT), combined with glycine decarboxylase, catalyzes an essential sequence of the photorespiratory C2 cycle, namely, the conversion of two molecules of glycine into one molecule each of CO2, NH4+, and serine"].
- SHM uses the GDC-derived 5,10-methylene-THF to convert another glycine into serine
  [PMID:22303256 "The latter is used by SHM as a substrate for the transfer of an activated C1 moiety to another molecule of glycine resulting in the formation of serine."].
- SHM1 is the photorespiratory isozyme, encoded by a single gene
  [PMID:22303256 "The photorespiratory SHM enzyme (EC. 2.1.2.1) is encoded by a single gene (At4g37930) in Arabidopsis."].
- Genetics: shm1-1 (the classical `stm`) lacks mitochondrial SHMT activity and is
  conditionally lethal in air; the defect maps to SHM1; SHM1 (35S or native
  promoter) complements, SHM2 does not
  [PMID:16339799 "is defective in mitochondrial SHMT activity and displays a lethal photorespiratory phenotype when grown at ambient CO2, but is virtually unaffected at elevated CO2"]
  [PMID:16339799 "Expression of wild-type SHM1 under the control of either the cauliflower mosaic virus 35S or the SHM1 promoter in shm1-1 abrogated the photorespiratory phenotype of the shm mutant"].
- SHM2 is excluded from mesophyll mitochondria, so it cannot replace SHM1 in
  photorespiration; SHM1 and SHM2 act redundantly in one-carbon metabolism of
  vascular cells; the shm1 shm2 double mutant is lethal even at high CO2
  [PMID:21976482 "SHM1 has been identified as the photorespiratory isozyme"]
  [PMID:21976482 "It seems that SHM1 and SHM2 operate in a redundant manner in one-carbon metabolism of nonphotorespiring cells with a high demand of one-carbon units; for example, during lignification of vascular cells."].

## Regulation and partners

- Fd-GOGAT (GLU1) is dual-targeted to mitochondria and physically interacts with
  SHMT1; the interaction is needed for photorespiratory SHMT activity
  [PMID:19223513 "In the mitochondria, Fd-GOGAT interacts physically with SHMT1, and this interaction is necessary for photorespiratory SHMT activity."].
- UBP16 deubiquitinates and stabilizes SHM1; SHM1 is degraded by the 26S
  proteasome [PMID:23232097 "We found that SHM1 is degraded in a 26S proteasome-dependent process, and UBP16 stabilizes SHM1 by removing the conjugated ubiquitin."].
- FERONIA phosphorylates SHM1, affecting its stability, during salt stress
  [PMID:39197037 "Biochemical data show that FER interacts with and phosphorylates SHM1, and this phosphorylation modulates SHM1 stability."].
- Ser31 phosphorylation mimic reduces SHMT1 protein and salt/drought tolerance
  [PMID:31134633 "indicate that SHMT1 S31 phosphorylation could be involved in modulating SHMT1 protein stability"].
- Circadian and light regulation of SHM1 mRNA
  [PMID:10806255 "show that both exhibit circadian oscillations in mRNA abundance that are in phase with those described for other photorespiratory genes"]
  [PMID:10806255 "this response is probably an indirect consequence of the induction of photosynthesis and photorespiration by illumination"].
- SHM transcript is overexpressed in the stm mutant, suggesting feedback regulation
  (PMID:9232907).

## Stress and defence phenotypes (indirect)

- shmt1-1 (weak allele, later called shm1-3): lesion formation, constitutive SA and
  H2O2-detoxification gene expression, higher susceptibility to biotrophic and
  necrotrophic pathogens, salt sensitivity
  [PMID:15659103 "We found that a recessive mutation, shmt1-1, causes aberrant regulation of cell death resulting in chlorotic and necrotic lesion formation under a variety of environmental conditions."]
  [PMID:15659103 "this enzymatic activity plays a critical role in controlling the cell damage provoked by abiotic stresses such as high light and salt and in restricting pathogen-induced cell death"].
  These phenotypes are best explained by impaired photorespiratory flux causing ROS
  accumulation, i.e. they are downstream consequences of the core enzymatic role.
- Photorespiratory mutants including SHMT-deficient lines show accelerated PSII
  photoinhibition through impaired D1 repair (PMID:17400706).

## Localization

- Mitochondrion: multiple proteomics and IDA (PMID:19223513, PMID:23232097),
  predicted matrix targeting [PMID:10806255 "Both SHM1 and SHM2 protein products are predicted to be targeted into the mitochondrial matrix."].
- Cytosol (IDA, PMID:23232097; UniProt "Cytoplasm") might reflect a pre-import or
  degradation pool, which fits proteasome-dependent turnover, but the full text is not
  cached.
- Chloroplast stroma/thylakoid/stromule, nucleus, plasma membrane, apoplast and
  cytosolic ribosome come from proteome datasets and are best treated as
  contamination by an abundant leaf mitochondrial enzyme. The complex I study lists
  "Ser hydroxymethyltransferase" among its contaminants (PMID:20197505), which
  shows that SHMT carries over into other fractions.

## Module cross-check

- `modules/photorespiration_c2_cycle.yaml` step 6 (shmt_step) uses SHM1
  (Q9SZJ5) with GO:0004372, process GO:0009853 and location GO:0005759.
  This review agrees: core MF GO:0004372, photorespiration, mitochondrion /
  mitochondrial matrix. No disagreement.
