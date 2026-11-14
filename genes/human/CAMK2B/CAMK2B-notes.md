# CAMK2B review notes

## Literature search (manual; no deep-research provider available)

Sources checked, 2026-11-04:

- UniProt Q13554 record (`CAMK2B-uniprot.txt`): FUNCTION, ACTIVITY REGULATION, SUBUNIT,
  SUBCELLULAR LOCATION, DISEASE sections.
- All GOA publications cached with `just fetch-gene-pmids human CAMK2B` (12 papers).
- Additional papers fetched: PMID:14722083 (isoform comparison of alpha/beta/gamma/delta
  holoenzymes), PMID:16690701 (CaMKII in human skeletal muscle during exercise),
  PMID:19996366 (CaMKII and F-actin in spine structural plasticity), PMID:29560374
  (CAMK2A/CAMK2B de novo variants), PMID:11972023 (CaMKII and STAT1 Ser727).
- Context only: the `genes/human/CAMK2A` review, and the STAT1 module and GO-CAM review proposed
  in ai4curation/ai-gene-review#5904 (not used as evidence here).
- Fetched after PR review: PMID:9768845 (Shen et al. 1998, CaMKIIbeta as an F-actin targeting
  module) and PMID:17404223 (Okamoto et al. 2007, CaMKII as an F-actin-bundling protein), the
  primary rodent papers behind the actin rows.

## Findings

### Catalytic activity and regulation
- CaMKII beta is a Ca2+/calmodulin-activated Ser/Thr kinase; CaM binding relieves
  autoinhibition and allows Thr287 autophosphorylation (UniProt ACTIVITY REGULATION,
  ECO:0000269 PubMed:14722083).
- All four isoforms are dodecamers; they differ in CaM affinity and CaM dependence of
  autophosphorylation [PMID:14722083 "all four isoforms were dodecamers with similar but highly
  unusual architecture"; "the rank order of CaM binding affinity (gamma > beta > delta > alpha)"].
- Human CAMK2B phosphorylates the ER-phagy receptor FAM134B/RETREG1 under ER stress
  [PMID:31930741 "Under ER-stress conditions, activated CAMK2B phosphorylates the
  reticulon-homology domain of FAM134B, which enhances FAM134B oligomerization"].
- Crystal structure of the autoinhibited CaMKII beta kinase domain is among the four human
  isoform structures in PMID:20668654 [PMID:20668654 "we determined the structures of all human
  CaMKII isozymes in their autoinhibited state"].

### Non-catalytic actin bundling
- The beta subunit's variable-region insert binds and bundles F-actin, independently of kinase
  activity [PMID:18817731 "an insert in the β subunit of CaMKII specifically binds to and bundles
  F-actin to promote isoform-specific neurite outgrowth (Fink et al., 2003) and maintain dendritic
  spines (Okamoto et al., 2007)"; "This effect of βCaMKII does not require kinase activity, as a
  kinase-dead mutant is able to rescue the RNAi eff[ect]"].
- [PMID:19996366 "CaMKII plays a structural role via direct interaction with actin filaments,
  thus coupling functional and structural plasticity in dendritic spines"].
- These primary data are rodent (rat hippocampal neurons); the human annotations rest on ISS
  from rat Camk2b and on reviews. No actin binding/bundling annotation is in GOA for human
  CAMK2B, so the review adds NEW actin filament binding (ISS, PMID:9768845) and actin filament
  bundle assembly (ISS, PMID:17404223) rows, both with rat Camk2b UniProtKB:P08413 as donor
  [PMID:9768845 "CaMKIIbeta is bound to F-actin in dendritic spines and cell cortex while
  CaMKIIalpha is largely a cytosolic enzyme"]. Participation test: the beta subunit itself crosslinks the filaments (it does the
  work), so this is not a substrate/necessity case.

### Neuronal development and disease
- De novo CAMK2B variants cause intellectual disability (MRD54); variants alter Thr287
  autophosphorylation and in utero neuronal migration [PMID:29100089 "For both CAMK2A and
  CAMK2B , we identified mutations that decreased or increased CAMK2 auto-phosphorylation at
  Thr286/Thr287"; "increased as well as decreased levels of CAMK2B during neuronal development
  caused migration defects"].

### Skeletal muscle
- UniProt records CAMK2B on the cytoplasmic face of the sarcoplasmic reticulum membrane
  (ECO:0000269 PubMed:21529938) and roles in SR Ca2+ handling via triadin and phospholamban.
- PMID:15294044 (review) reports CaMKII gamma, not beta, upregulated in atrophy, so the
  skeletal-muscle adaptation TAS row is only weakly specific to beta.

### Location rows from Reactome
- R-HSA-9948087 places CAMK2 on the ER membrane by assumption ("We assume the interaction
  happens in the ER"); for CAMK2B the experimentally supported membrane is the SR membrane,
  a subtype of ER membrane.
- Endocytic vesicle membrane rows (ARBA IEA and Reactome TAS): MARK_AS_OVER_ANNOTATED (revised
  from UNDECIDED after PR review, matching CAMK2G); the Reactome compartment is that of the GluA1
  substrate, not the kinase. The nucleoplasm Reactome row stays UNDECIDED.

### STAT1 (module context)
- PMID:11972023 identifies the ubiquitous gamma/delta isoforms as the STAT1-interacting
  kinases; alpha/beta from brain were only a positive control. No STAT1 row is proposed for
  CAMK2B.
