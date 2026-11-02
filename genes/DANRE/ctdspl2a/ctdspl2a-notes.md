# ctdspl2a notes

## Provenance and setup

- Record: Q08BB5 (Swiss-Prot CTL2A_DANRE, 469 aa), ZFIN ZDB-GENE-061013-647, Ensembl ENSDARG00000061587 (chr25).
- Paralog: ctdspl2b (A4QNX6). DANRE_DUPLICATION batch 4 random pair (PANTHER `TGD_tree`; Ensembl
  Compara duplication node Osteoglossocephalai).
- Deep research was not available for this gene (Edison returned 402 Payment Required; the OpenAI
  key is invalid). Literature was searched by hand through Europe PMC (queries: `ctdspl2a OR ctdspl2b`;
  `(CTDSPL2 OR SCP4) AND zebrafish`; title search `SCP4 OR CTDSPL2`).
- No zebrafish study of either copy exists. The only hits for the zebrafish symbols are gene lists in
  a toxicology transcriptome paper and a human interactome paper; neither is informative.

## Mammalian CTDSPL2 (SCP4)

- CTD phosphatase, chromatin-associated
  [PMID:26920047 "SCP4 exhibited Ser5-preferential CTD phosphatase activity in vitro, while small interfering RNA-mediated SCP4 knockdown in HeLa cells increased phosphorylation levels of Pol II at Ser5 and Ser7, but not at Ser2."]
- FoxO1/3a phosphatase in liver; gluconeogenesis
  [PMID:28851713 "In this study, we discovered a nuclear phosphatase, SCP4/CTDSPL2 (SCP4), that dephosphorylated FoxO1/3a and promoted FoxO1/3a transcription activity."]
  [PMID:28851713 "Moreover, we demonstrated that gene ablation of SCP4 led to hypoglycemia in neonatal mice."]
- Domain organization; Smad1/5/8
  [PMID:28506762 "SCP4 consists of a regulatory domain (amino acids 1–262), which contains two nuclear locations signaling (NLS), and a catalytic phosphatase domain (amino acids 263–466) that reportedly dephosphorylates Smad1/5"]
  [PMID:28506762 "Our interest in SCP4 (also called CTDSPL2) was stimulated by the finding that SCP4 specifically dephosphorylates transcription factor Smad1/5/8; these reactions attenuate BMP-induced transcriptional activities [26;27]."]
- Catalytic motif; D293/D295
  [PMID:35021089 "In addition, we cloned point mutations of SCP4 that changed aspartate residues in the putative DxDx(V/T) catalytic motif to alanine."]
  [PMID:35021089 "Despite similar expression levels to the wild-type protein, SCP4D293A, SCP4D295A, and SCP4D293A/D295A mutants were unable to support MOLM-13 growth (Figures 3G and 3H)."]
- Histone H3 Thr3 phosphatase
  [PMID:42315649 "Here, we identify the nuclear phosphatase SCP4 as a novel H3T3 phosphatase through a systematic phosphatase library screening."]
- Cartilage (mouse, FoxO3a) [PMID:38886174] and a 2026 review [PMID:42208850] were read for
  background; not cited in the review.

## My analysis (file:DANRE/ctdspl2a/ctdspl2a-bioinformatics/RESULTS.md)

- Protein: 70.9% identity between copies; FCP1-homology domain 97.5% (a) / 96.2% (b) identical to human;
  DxDx(T/V) motif DLDET conserved in both, aligned exactly to human D293-T297. The copies differ mainly in
  the N-terminal regulatory region. No relative-rate asymmetry (38 vs 38 changes).
- Expression: both maternal and ubiquitous; ctdspl2a two- to three-fold higher at every stage in
  E-ERAD-475; Bgee calls in the same 20+ tissues for both copies; gar CTDSPL2 also broad. No ZFIN records.

## Annotation decisions

- MF IBA/IEA rows accepted (catalytic motif conserved). Nucleus IEA accepted.
- Positive regulation of gluconeogenesis (ARBA) kept as non-core: mammalian evidence is direct
  (FoxO dephosphorylation) but single-lab, and untested in fish.
