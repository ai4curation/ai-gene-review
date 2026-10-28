# Slc12a1 (rat) - manual literature research

No deep-research API was available for this session; this file was compiled manually from
cached publications (publications/PMID_*.md) and PubMed searches. Each statement carries
inline provenance.

## Identity

- Reviewed entry: UniProt F7EUW9 (TrEMBL, unreviewed; "Slc12a1 protein", 1095 aa), RGD:3685,
  GeneID 25065. The same gene has a Swiss-Prot entry, P55016 (S12A1_RAT, also 1095 aa, RGD:3685),
  which carries the experimental GO annotations for rat NKCC2 (EXP/IDA from PMID:8021284,
  PMID:16291577, PMID:19592485, PMID:16275913). F7EUW9 itself has only electronic (IEA) GOA rows.
- Common names: NKCC2, BSC1 (bumetanide-sensitive cotransporter 1), renal Na-K-2Cl cotransporter.
- Family: SLC12A cation-chloride cotransporter family; InterPro IPR002445 (Slc12a1), IPR002443
  (SLC12A1/SLC12A2), IPR004842 (SLC12A family); PANTHER PTHR11827:SF93; NCBIfam TIGR00930
  (file:rat/Slc12a1/Slc12a1-uniprot.txt). Phobius predicts multiple TM helices (TM domain
  ~187-623), with cytoplasmic N-terminus (~1-180) and large C-terminal domain (690-1095).

## Function

- Cloning and functional expression of rat NKCC2: Gamba et al. 1994 isolated cDNAs for the
  "bumetanide-sensitive Na(+)-K(+)-Cl- symporter and thiazide-sensitive Na(+)-Cl- cotransporter"
  from rat kidney and "characterized their functional activity in Xenopus laevis oocytes"; the
  transporters "are expressed predominantly in kidney"
  [PMID:8021284 "Molecular cloning, primary structure, and characterization of two members of the mammalian electroneutral sodium-(potassium)-chloride cotransporter family expressed in kidney"; abstract only].
- Glycosylation: N442/N452 glycosylation required for full activity and surface insertion; Cl-
  affinity and bumetanide sensitivity were measured by 86Rb+ influx in oocytes
  [PMID:16291577 "Our data demonstrate that NKCC2 is glycosylated"; abstract only].
- NaCl reabsorption by the TAL: "The thick ascending limb of Henle loop reabsorbs ≈ 30% of filtered
  NaCl via the apical Na-K-2Cl cotransporter (NKCC2)" [PMID:23108645, abstract only].

## Location

- Apical plasma membrane and subapical vesicles of rat thick ascending limb (TAL). Surface
  biotinylation and apical immunolabeling with an extracellular-epitope antibody in isolated
  perfused rat TALs [PMID:19592485 "NKCC2 is located in the apical membrane and subapical vesicles of TALs."; full text].

## Regulation

- cAMP/PKA (vasopressin V2 receptor signalling) increases apical NKCC2 by stimulating exocytic
  insertion [PMID:19592485, full text].
- VAMP2 (not VAMP3) mediates cAMP-stimulated exocytic delivery; NKCC2 co-immunoprecipitates
  with VAMP2 in rat TALs [PMID:25008321, full text].
- Constitutive endocytosis via dynamin-2, clathrin and lipid rafts sets steady-state surface
  levels [PMID:22977238 "constitutive endocytosis of NKCC2 controls NaCl absorption in native THALs"].
- Phosphorylation: Thr96/Thr101 by SPAK/OSR1 (enhanced in Dahl salt-sensitive rats)
  [PMID:23108645]; Ser126 by AMPK [PMID:17341212, abstract only]; WNK3 increases NKCC2 surface
  expression and phosphorylation [PMID:16275913]. Dephosphorylation by calcineurin A-beta,
  modulated by SORLA (mouse) [PMID:25967121].

## Physiology

- NKCC2 is the loop-diuretic (furosemide/bumetanide) target and its loss causes type I Bartter
  syndrome in humans [PMID:16291577 abstract]. It drives the countercurrent urinary-concentrating
  mechanism [PMID:25967121 "is crucial for NaCl reabsorption in kidney thick ascending limb (TAL) and drives the urine concentrating mechanism"].
- In the medullary TAL, NKCC2 can transport NH4+ in place of K+ (Swiss-Prot P55016 statement,
  by similarity to mouse P55015); not independently verified here.
