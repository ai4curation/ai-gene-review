# MAP2K1 (MEK1, human, UniProt Q02750) — curation notes

## Identity and family

- Dual-specificity MAP kinase kinase 1; STE Ser/Thr kinase family, MAP kinase kinase subfamily
  [file:human/MAP2K1/MAP2K1-uniprot.txt "Belongs to the protein kinase superfamily. STE Ser/Thr"].
- PANTHER (UniProt DR line): PTHR47448:SF2 "MITOGEN-ACTIVATED PROTEIN KINASE KINASE 1". The IBA rows
  descend from PAINT node PANTHER:PTN000684494 (listed in WITH/FROM of the IBA rows). Note that
  modules/erk_cascade.yaml declares PTHR48013 for the MEK1/MEK2 tier; the repo's PANTHER member index
  (interpro/panther/panther-members.tsv) places Q02750 in PTHR48013:SF5, consistent with the module. The
  cached UniProt DR line lists PTHR47448:SF2, reflecting a different PANTHER release (no action needed).
- Paralog: MAP2K2/MEK2 (P36507); the two are the only ERK1/2-specific MAP2Ks.

## Core molecular function

- MEK1 catalyses concomitant Thr and Tyr phosphorylation of the ERK1/ERK2 TEY activation motif
  [file:human/MAP2K1/MAP2K1-uniprot.txt "concomitant phosphorylation of a threonine and a tyrosine residue in a"];
  "function specifically in the MAPK/ERK cascade".
- Reactome: [Reactome:R-HSA-109860 "MAP2K1 (also known as MEK1) phosphorylates the critical Thr202 and Tyr204 on MAPK3 (ERK1), converting two ATP to ADP."]
- Original cloning: recombinant MEK1 activates human ERK1 in vitro
  [PMID:8388392 "Both MEK1 and MEK2 were expressed in Escherichia coli and shown to be able to activate recombinant human ERK1 in vitro."]
- Reconstituted assays with purified ERK2, MEK1 variants and ATP [PMID:28166211 "we reconstituted a biochemical system comprising purified ERK2, variants of MEK1, and ATP"].
- Coupled RAF->MEK1->ERK2 assays [PMID:10644344 "phosphorylated recombinant MEK-1, which in turn phosphorylated kinase-inactive recombinant ERK-2"].
- Substrate specificity is very narrow: ERK1/2 are the established physiological substrates
  (deep research, falcon; citing Barbosa et al. 2021 review).

## Regulation

- Activated by RAF (and MOS, MEKK1 etc.) phosphorylation of Ser218/Ser222
  [file:human/MAP2K1/MAP2K1-uniprot.txt "Activation occurs through phosphorylation of Ser-218"].
- ERK negative feedback on MEK1-specific Thr292 [Reactome:R-HSA-5674496 "phosphorylating MAP2K1 at T292, a residue that is not present in MAP2K2"].
- CDK1 phosphorylation (Reactome:R-HSA-112342), anthrax lethal factor cleaves the N-terminal docking site (Reactome:R-HSA-5211340).

## Non-catalytic role: allosteric BRAF activation via KSR

- MEK1 binding to KSR1/2 releases KSR autoinhibition and drives KSR–BRAF heterodimerization, independent of MEK catalysis
  [PMID:29433126 "Intriguingly, MEK promoted BRAF-KSR1 dimerization independent of its catalytic function (Fig."];
  [PMID:29433126 "Using yeast two-hybrid (Y2H) screening, we identified the F311S mutation in MEK1 that abrogated KSR1, BRAF and CRAF binding"].
- This is the basis for UniProt's IMP "MAP kinase scaffold activity" (GO:0005078) and for GO:0043539
  "protein serine/threonine kinase activator activity" being biologically defensible for MEK1 (as a non-catalytic activator of BRAF).
- BRAF–MEK1 face-to-face complex [PMID:25155755 "The crystal structure of the BRAF(KD) in a complex with MEK1 reveals a face-to-face dimer"].

## Scaffolds / partners (for protein-binding MODIFY decisions)

- KSR1 (scaffold) [PMID:10409742 "suggest that KSR may act as a scaffolding protein for the Ras-mitogen-activated protein kinase pathway"] -> GO:0097110 scaffold protein binding.
- RAF1/BRAF/MOS (MAP3Ks) -> GO:0031435 MAPKKK binding (consistent with MAP2K2 review).
  MOS: [PMID:34779126 "Since MOS directly interacts and phosphorylates MEK1/2 to activate ERK1/2"].
- ERK1/ERK2 (substrates and cytoplasmic anchoring) -> GO:0051019 mitogen-activated protein kinase binding.
  [PMID:17255949 "unphosphorylated ERK1/2 are primarily located in the cytoplasm, largely as a consequence of their interaction with cytoplasmic anchors, including MEK1"].
- VRK2A anchors KSR1–MEK1 at the ER [PMID:22752157 "VRK2A can form a high molecular size (600-1,000 kDa) stable complex with both MEK1 and KSR1"].
- PPARG: MEK1 binds and exports PPARG from nucleus [PMID:17101779 "MEK1 exports PPARgamma from the nucleus"].
- Other partners (TRIB1/3, CFLAR, BIRC6, PIN1, YAP1, BTRC, BANP, TCP11, PLEKHF2) come from single studies or
  binary/AP-MS screens; no informative MF term can be derived -> REMOVE generic protein binding (interaction not disputed).

## Localization

- Predominantly cytoplasmic/cytosolic, with NES-driven nuclear export; shuttles into the nucleus on stimulation
  [PMID:17101779 "This unanticipated role for the stimulation-induced nuclear shuttling of MEKs"].
- Peripheral membrane via KSR [PMID:10409742 "this results in the appearance of MEK in membrane-associated fractions"].
- Centrosome / spindle pole / midbody during mitosis (UniProt SubCell from PMID:14737111).
- Endosome (LAMTOR3/MP1 scaffold; Reactome R-HSA-5674132, R-HSA-5674130), Golgi (IL17RD/Sef; R-HSA-5674373), ER (VRK2).
- Mitochondrion, focal adhesion: only TAS from a review (PMID:19565474, abstract only) and ARBA; left UNDECIDED.

## Miscitation found

- GOA rows (MGI, 2014) "protein binding" IDA and "endoplasmic reticulum" IDA cite PMID:22572157, which is a
  platelet-alloantibody biosensor paper with no MEK1 content. PMID:22752157 (VRK2 anchors KSR1-MEK1 to ER)
  differs by a two-digit transposition (57<->75) and exactly matches both claims (ER; MEK1–KSR1–VRK2 complex).
  The same PMID:22572157 is also on CALR and CANX in this repo (MGI, likely ER markers in the same paper).
  Recorded as WRONG_IDENTIFIER with replacement PMID:22752157 (inferred, not confirmed by MGI).
- PMID:19593445 (the known batch miscitation) is NOT among MAP2K1 GOA rows.

## Processes

- Core: ERK1 and ERK2 cascade (GO:0070371) / MAPK cascade (GO:0000165).
- MEK1-specific (not MEK2) role in G2 Golgi fragmentation and mitotic entry via Myt1
  [PMID:23241949 "MEK1 is required for Golgi fragmentation in G2 and for the entry of cells into mitosis."] -> Golgi inheritance kept non-core.
- Oncogene-induced senescence with constitutively active MEK1 (PMID:9765203; only title cached).
- Many rat-derived (Q01986) IEA process terms are pharmacological (MEK inhibitor) readouts downstream of ERK
  (muscle contraction, glucocorticoid response, triglyceride homeostasis, etc.) -> over-annotation.
- Mouse-derived (P31938) Schwann cell / myelination / ERBB / NMJ terms come from Mek1/2 conditional knockout genetics
  -> non-core developmental roles via ERK signaling.

## Disease

- Germline activating variants: cardiofaciocutaneous syndrome 3 (CFC3); somatic mosaic: melorheostosis; somatic cancer
  alleles in three RAF-dependence classes (deep research, Gao et al. 2018).
