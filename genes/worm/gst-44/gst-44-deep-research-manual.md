# gst-44 (F13A7.10; UniProt O45352) -- manual literature research

No deep-research API was available for this session; this summary was compiled manually from
PubMed searches (query `(gst-44 OR F13A7.10) AND elegans`, 4 hits on 2026-10-28) and the cached
full texts of PMID:40186509 and PMID:23593298.

## Identity and family

- gst-44 (WormBase WBGene00001792, ORF F13A7.10, chromosome V; GeneID 184405) encodes a 254-aa
  omega-class glutathione S-transferase (GSTO). UniProt O45352 is an unreviewed TrEMBL entry
  (PE 3) whose name, EC numbers and catalytic activities come from UniRule RU368071 / ARBA.
- InterPro IPR005442 (GST omega), PRINTS PR01625, PANTHER PTHR43968:SF12; GST N-terminal
  (thioredoxin-like) domain 25-105 and GST C-terminal domain 110-247.
- C. elegans has five GSTO genes: gsto-1, gsto-2, gsto-3, C02D5.4 and gst-44; GST-44 is closest to
  GSTO-1 and GSTO-2 and conserves the active-site cysteine of the G-site
  [PMID:40186509 "The alignment and construction of a neighbor‐joining tree (Fig. 1B,C), based on the protein sequences of all GST from C. elegans, clearly demonstrate that GST‐44 belongs to the omega class."].
- My reading of the sequence: the catalytic-cysteine motif S-M-R-F-C-P is present with Cys35
  (equivalent to Cys32 of human GSTO1).

## Biochemistry (PMID:40186509, Kaiser et al. 2025, FEBS J, full text)

- Recombinant His-tagged GST-44 purified from E. coli.
- No conjugating activity with the classical GST substrates CDNB and ethacrynic acid
  ["For the typical GST substrates 1‐chloro‐2,4‐dinitrobenzene (CDNB) and ethacrynic acid, no GSH‐conjugating activity could be shown (data not shown)."].
- Glutathione peroxidase activity with cumene hydroperoxide (0.37 umol/min/mg), about ten-fold
  higher than C. elegans GSTO-1.
- Thioltransferase (HEDS) activity 5.08 umol/min/mg, KM 0.16 mM.
- GSH-dependent dehydroascorbate reductase 6.35 umol/min/mg and monomethylarsonate (MMA-V)
  reduction 0.635 umol/min/mg
  ["Furthermore, the enzyme was capable of using GSH as an electron donor to reduce dehydroascorbate (DHA) (6.35 ± 0.15 μmol·min−1·mg−1) and monomethylarsenate (MMAv) (0.635 ± 0.13 μmol·min−1·mg−1)."].
- Note: the abstract and the Fig. 2A legend call this "arsenate reductase activity", but the
  substrate assayed was MMA(V); reduction of inorganic arsenate itself is not shown.
- E. coli expressing GST-44 had smaller inhibition halos with cumene hydroperoxide.

## Expression and localization (PMID:40186509)

- Translational reporter gst-44p::GST-44::GFP: intestine from L1, excretory (H-shaped canal) cell
  from L3; cytoplasm with weaker nuclear signal
  ["In adult worms, a robust signal is observed in the cytoplasm of the anterior and posterior intestinal cells, accompanied by a weaker signal in the intestinal nuclei and in the excretory canal cell."].
- Induced by arsenite (strongly in excretory cell and pharyngeal gland cells), by
  Penicillium brevicompactum, cyanobacteria with trypsin inhibitors, and dimethyl fumarate;
  not by NaCl, cadmium, rapamycin or Serratia. Arsenite induction requires SKN-1 and PHA-4.

## Genetics

- gst-44(tm6133) deletion: shorter lifespan (15 vs 18 days), reduced survival under arsenite
  (AsIII) and arsenate (AsV), juglone (25% reduction), TCEP (~20%) and NaCl; not cadmium, heat or
  selenite. gsto-1, gsto-2 and gsto-3 CRISPR deletions were not arsenic-sensitive
  ["While the GST‐44 showed a significantly reduced survival rate under arsenic, this was not observed in the deletion mutants gsto‐1(eva301) III, gsto‐2(eva302) III, and gsto‐3(eva303) III (Fig. 9B)."].
- gst-44 RNAi did not alter A-beta or alpha-synuclein models; slight motility reduction in polyQ.
- PMID:23593298 (Luersen et al. 2013, PLoS One; small-scale RNAi screen of 67 GSH-metabolism
  genes): gst-44(RNAi) reduced survival on 3 mM arsenite (15.0 +/- 6.4% vs 90% control) but did
  not affect juglone survival (90.0 +/- 3.3%)
  ["Furthermore, knockdown of an alpha-class related GST (gst-32), an omega-class GST (gst-44) and an extracellular glutathione peroxidase (C11E4.1) less profoundly affected the survival rate under arsenite stress"].
  This paper is the reference for the WormBase IMP to GO:0000302 response to reactive oxygen
  species; the phenotype it reports is arsenite sensitivity, not ROS (juglone) sensitivity.

## Transcriptomic mentions (low relevance)

- PMID:39095841, PMID:34037943, PMID:32681860 list gst-44 among differentially expressed genes after
  probiotic or cinnamaldehyde exposure; no functional data on GST-44.
