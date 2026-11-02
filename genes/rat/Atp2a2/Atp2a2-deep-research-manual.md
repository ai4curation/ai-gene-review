# Atp2a2 (rat, P11507) - manual literature synthesis

No deep-research API was available for this review, so this summary was assembled
by hand from the cached publications in `publications/`, the UniProt record
(`Atp2a2-uniprot.txt`) and PubMed metadata. Every claim carries its source.

## Identity and family

- Rat Atp2a2 encodes SERCA2, a P-type type IIA Ca2+-ATPase (EC 7.2.2.10) of the
  ER/SR membrane, with ten predicted transmembrane helices and the phosphorylated
  Asp351 active site (UniProt P11507, FT ACT_SITE 351; "Belongs to the cation
  transport ATPase (P-type) (TC 3.A.3) family. Type IIA subfamily").
- UniProt function (by similarity to human P16615 and mouse O55143): "This
  magnesium-dependent enzyme catalyzes the hydrolysis of ATP coupled with the
  translocation of calcium from the cytosol to the sarcoplasmic reticulum lumen."
- Two splice isoforms: SERCA2b (isoform 1, displayed, ubiquitous ER pump) and
  SERCA2a (isoform 2, heart and slow-twitch muscle). UniProt: "Isoform 2 is highly
  expressed in heart and slow twitch skeletal muscle. Isoform 1 is widely expressed."
  The SERCA2b-encoding transcript was cloned from rat brain
  [PMID:2844797, cited in UniProt RN [1]].

## Pump activity, measured in rat material

- Diabetic rat heart: "Total ventricular SERCA2a protein remained unchanged, but its
  ability to hydrolyze ATP and transport Ca(2+) was significantly reduced"
  [PMID:21300842]. Full text: thapsigargin-sensitive Ca2+ uptake and Ca2+-ATPase
  (malachite green Pi release) assays on rat heart vesicles and on recombinant
  SERCA2a in HEK-293T cells.
- Transgenic overexpression of SERCA2a in mouse heart (BHF-UCL annotated to rat
  P11507): "The maximum velocity of Ca2+ uptake (Vmax) was increased by 37%,
  demonstrating that increased pump levels result in increased SR Ca2+ uptake
  function" and faster relaxation [PMID:9851937, abstract only].
- Rat skeletal muscle SR vesicles: Ca2+-ATPase Vmax and Ca2+ uptake rise after
  exercise; FITC and NCD-4 probes of the "nucleotide-binding and Ca(2+)-binding
  sites" unchanged [PMID:12409282, abstract only]. These vesicles come from fast
  gastrocnemius, where SERCA1 dominates, so the assay is not SERCA2-specific.

## Regulation

- Phospholamban (PLN): rat heart supramolecular complex of "SERCA2, its negative
  regulator phospholamban (PLN), the A-kinase anchoring protein AKAP18delta and PKA";
  PKA phosphorylation of PLN releases it from SERCA2 and speeds SR Ca2+ re-uptake
  [PMID:17901878, abstract only]. Mouse genetics show PLN-SERCA2a inhibition as the
  Ca2+ cycling defect in dilated cardiomyopathy [PMID:10555147].
- Transcriptional regulation: ER stress (UPR) induces SERCA2b in PC12 cells
  [PMID:10748035]; ATF6 activates the rat SERCA2 promoter through an ERSE after SR
  Ca2+ depletion in cardiac myocytes [PMID:11595740]; TNF-alpha/NF-kB represses
  SERCA2a, and LPS in rats lowers myocardial SERCA2a and diastolic Ca2+ reuptake
  [PMID:25712896]. These describe regulation OF the gene, not functions of the protein.
- Post-translational: carbonylation of basic residues reduces SERCA2a activity
  [PMID:21300842]; TLR9 stimulation reduces SERCA2 activity in cardiomyocytes, with
  TLR9-SERCA2 co-immunoprecipitation [PMID:24610369]; VMP1 promotes SERCA activity
  by preventing SERCA/PLN/SLN inhibitory complexes [PMID:28890335].

## Localization

- ER membrane / SR membrane (UniProt CC, by similarity). Measured in rat: SR
  [PMID:8447366, PMID:17901878, PMID:12409282].
- Rat pulmonary arterial smooth muscle (full text): "Almost all SERCA2a and RyR3
  labeling was restricted to a region within 1.5 microm of the nucleus. In marked
  contrast, SERCA2b labeling was primarily found within 1.5 microm of the plasma
  membrane" - i.e. two SR compartments, perinuclear (SERCA2a) and subplasmalemmal
  (SERCA2b) [PMID:20177054]. SERCA2b remains an integral SR-membrane pump; the
  study gives no evidence for a plasma-membrane-associated (extrinsic) form.
- Rat Sertoli cells: "SERCA2 is present at ESs" (ER of apical ectoplasmic
  specializations) [PMID:28486663, abstract only].

## Peripheral roles reported for the family/orthologs

- Autophagy: VMP1 "controls contact formation by promoting SERCA ... activity"
  at ER-isolation membrane contacts [PMID:28890335]. This is ER-IM contact control
  during autophagosome formation, not docking of autophagosomes to lysosomes.
- GPCR biogenesis: SERCA2b associates with newly synthesized family A GPCRs,
  including endogenous LH receptor in rat ovary [PMID:17588601].

## Physiology

- SERCA2a is the cardiac SR pump that removes cytosolic Ca2+ during diastole;
  its activity sets relaxation rate and SR load, hence contractility
  [PMID:9851937, PMID:21300842, PMID:25712896].
- In rat gastrocnemius, SERCA activity (thapsigargin) determines fatigue resistance
  [PMID:21993782].
