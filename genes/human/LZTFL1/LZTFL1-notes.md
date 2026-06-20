# LZTFL1 (BBS17) — Gene Review Notes

UniProt: Q9NQ48 | HGNC:6741 | GeneID 54585 | 299 aa | Chr 3p21.3

## Summary of function

LZTFL1 ("Leucine zipper transcription factor-like protein 1") is, despite its name, a
**cytoplasmic, predominantly alpha-helical / coiled-coil protein and NOT a transcription
factor**. It is a **negative regulator of the ciliary trafficking of the BBSome** (the
seven-subunit BBS protein complex) and, through the BBSome, of Smoothened (SMO) ciliary
localization and Sonic hedgehog (SHH) signaling. Loss-of-function mutations cause
**Bardet–Biedl syndrome type 17 (BBS17)**.

## Key evidence

### PMID:22072986 (Seo et al. 2011, PLoS Genet) — the foundational functional paper (full text available)
- LZTFL1 identified as a BBSome-interacting protein by TAP of LAP-BBS4 from mouse testis
  [PMID:22072986 "Mass spectrometry analysis revealed that this protein is Leucine zipper transcription factor-like 1 (Lztfl1)"].
- Interacts with the BBSome specifically through **BBS9**; C-terminal half (aa 145–299) of
  LZTFL1 binds BBS9 [PMID:22072986 "BBS9 is the LZTFL1-interacting subunit of the BBSome ... the C-terminal half of LZTFL1 (amino acid (aa) 145–299) was found to interact with BBS9"].
- **Self-associates / homo-oligomerizes** [PMID:22072986 "endogenous LZTFL1 proteins were co-purified, indicating that LZTFL1 forms homo-oligomers. Homo-oligomerization of LZTFL1 was confirmed by co-IP and in vitro crosslinking"].
- **Cytoplasmic, NOT enriched in cilia or basal body** [PMID:22072986 "LZTFL1 was detected throughout the cytoplasm ... we did not find enrichment of LZTFL1 around the centrosome or within cilia"]. LZTFL1–BBSome interaction occurs in the cytoplasm (in situ PLA).
- Only a **subset** of LZTFL1 associates with the BBSome; it is **not a constitutive component**
  [PMID:22072986 "LZTFL1 is not a constitutive component of the BBSome and only a subset of LZTFL1 is associated with the BBSome"].
- **Negative regulation of BBSome ciliary entry**: knockdown increases ciliary BBS9/BBS4/BBS8;
  overexpression inhibits ciliary BBS9 [PMID:22072986 "over-expression of wild-type LZTFL1 inhibited ciliary localization of BBS9"]. KR→AS mutation at aa 24-25 acts as dominant negative, increasing BBSome ciliary localization.
- **Specific to the BBSome, not general IFT** [PMID:22072986 "LZTFL1 is a specific regulator of BBSome ciliary trafficking but not general IFT"].
- LZTFL1 depletion restores BBSome ciliary trafficking in BBS3/BBS5-depleted cells.
- **SMO / SHH**: LZTFL1 suppresses SMO ciliary localization [PMID:22072986 "LZTFL1 suppresses SMO localization to cilia"]; BBSome facilitates SMO ciliary localization. Contributes to SHH responsiveness.

### PMID:22510444 (Marion et al. 2012, J Med Genet) — disease/BBS17 (abstract/UniProt only)
- Exome sequencing identified LZTFL1 mutations in BBS family with situs inversus and
  insertional polydactyly; established LZTFL1 = BBS17 and role in SHH/SMO trafficking.

### PMID:23692385 (Schaefer et al. 2014) — mesoaxial polydactyly major feature in BBS17; variant L87P.

### PMID:24550735 (Chamling et al. 2014, PLoS Genet) — AZI1/CEP131 paper (abstract only; full_text_available: false)
- About AZI1/CEP131 regulating BBSome trafficking, but the GOA IDA annotation
  GO:0044877 protein-containing complex binding on LZTFL1 (PMID:24550735, assigned by UniProt)
  derives from LZTFL1 being assayed as a BBSome-associated protein in this study. Curator read
  full text; defer.

### Protein-interaction (IPI) annotations
- GO:0005515 protein binding and GO:0042802 identical protein binding come from large-scale
  interactome / IntAct datasets (PMID:25416956, 27107012, 27173435, 28514442, 31515488,
  32296183, 33961781). WITH/FROM partners include BBS9 (Q3SYG4), SDCBP/syntenin (O00560),
  proteasome subunits (PSMA1 P25786, PSMB1 P20618), self (Q9NQ48), etc. GO:0042802 (self-binding)
  is well-supported by the directed homo-oligomerization data in PMID:22072986.

## Localization
- UniProt SUBCELLULAR LOCATION: Cytoplasm (PMID:20233871, PMID:22072986). KW: Cytoplasm.
- GO:0005829 cytosol IDA (HPA, GO_REF:0000052) and TAS (Reactome) — well supported.
- GO:0005737 cytoplasm — supported.
- GO:0005929 cilium (IBA + IEA orthology) — LZTFL1 is NOT enriched in cilia per the primary
  functional study; it acts in the cytoplasm. Cilium location is questionable/over-annotated
  for the human protein, but it acts upon ciliary trafficking; "is_active_in cilium" IBA is weak.
- GO:0002177 manchette (IEA, ECO:0000265 from mouse Q9JHQ5) — spermatid microtubule structure;
  plausible (testis expression, sperm body localization) but orthology-electronic only.

## Tumor-suppressor / other (NOT in GOA being reviewed)
- PMID:20233871 proposed tumor-suppressor function (3p21.3 deletion region); UniProt notes
  "May have tumor suppressor function" and "May play a role in neurite outgrowth" — speculative,
  not in the annotation set under review.
- COVID-19 severity GWAS locus at 3p21.31 (largely genomic/regulatory, separate from ciliary
  protein function). Not a GO molecular/cellular function annotation; out of scope.

## Core function synthesis
1. **Negative regulator of BBSome ciliary trafficking** (cytoplasmic): GO:1903565 / GO:1903568.
2. **BBSome binding** (via BBS9) — protein-containing complex binding GO:0044877; mediator of
   BBSome ciliary localization control.
3. **Self-association / homo-oligomerization** — GO:0042802.
4. Downstream: regulation of SMO ciliary trafficking / SHH signaling responsiveness.
</content>
