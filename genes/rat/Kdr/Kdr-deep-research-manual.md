# Kdr (rat VEGFR-2 / Flk-1; UniProt O08775) - manual literature synthesis

No deep-research provider was available for this review. This file was written by hand
from the cached publications in `publications/`, the rat UniProt record
(`Kdr-uniprot.txt`) and QuickGO look-ups of the human (P35968) and mouse (P35918)
orthologs, which are the donors for most ISO/ISS rows. Provenance is given inline.

## Identity

- Rat Kdr (RGD:2965, GeneID 25589) encodes vascular endothelial growth factor receptor 2,
  a 1343-aa single-pass type I receptor tyrosine kinase of the CSF-1/PDGF receptor
  subfamily [UniProtKB:O08775 "Belongs to the protein kinase superfamily. Tyr protein
  kinase family. CSF-1/PDGF receptor subfamily."].
- Seven extracellular Ig-like domains (D2-D3 bind ligand), a transmembrane helix, a split
  tyrosine kinase domain with a kinase insert, and a C-terminal tail carrying docking
  phosphotyrosines [UniProtKB:O08775 "The second and third Ig-like C2-type
  (immunoglobulin-like) domains are sufficient for VEGFC binding"].

## Molecular function

- VEGF receptor activity: ligand (VEGFA, VEGFC, VEGFD) binding drives dimerization and
  trans-autophosphorylation [UniProtKB:O08775 "Binding of VEGFA, VEGFC or VEGFD leads to
  dimerization and activation by autophosphorylation on tyrosine residues"].
- Rat-specific experiments: cloning of rat Flk-1 from retina; both the full-length and a
  short form lacking the C-terminal half of the kinase domain bind VEGF and signal Ca2+
  [PMID:9442048 "VEGF induced a biphasic increase of cytoplasmic calcium with both forms
  in HK 293 transfected cells, indicating that both forms of the VEGF receptor-2/Flk-1 are
  functional"].
- Maturation and substrate: only the mature, fully glycosylated 230 kDa cell-surface form
  is tyrosine phosphorylated on VEGF stimulation, and PLC-gamma is the major substrate
  [PMID:9160888 "Only this 230 kDa form was rapidly and transiently phosphorylated on
  tyrosine residues in the presence of VEGF"; "As a major substrate of KDR/Flk-1,
  PLC-gamma was found to be rapidly tyrosine-phosphorylated and associated with
  KDR/Flk-1"]. (Assay cells in the abstract are endothelial and NIH3T3; species of the
  receptor not stated in the abstract.)

## Signalling outputs

- PLCG1 -> DAG/IP3/PKC; ERK1/2 MAPK; PI3K-AKT; FAK; eNOS/NO (UniProt FUNCTION, by
  similarity to human P35968).
- In rat neurons VEGF raises cytosolic Ca2+ and activates CaMKII, CREB, ERK and mTOR in a
  VEGFR2-dependent way and enhances long-term synaptic transmission [PMID:18221855].
- Rat spinal motor neuron survival under hypoxia needs Flk-1 (antisense knock-down) acting
  via PI3K/Akt and MEK/ERK [PMID:15780476].
- VEGF neurite outgrowth from rat cortical neurons via VEGFR2 and Rho/ROK [PMID:16329123].
- Dominant-negative KDR blocks hippocampal neurogenesis and learning in adult rats
  [PMID:15258583]; Flk-1 signalling required for antidepressant-induced proliferation
  [PMID:17360578].

## Vascular physiology (rat)

- KDR is the predominant receptor for VEGF-induced vasodilation and hypotension in
  conscious rats [PMID:12052848 "KDR is the predominant receptor mediating this effect"].
- KDR kinase inhibitors block laser-induced choroidal and oxygen-induced retinal
  neovascularization in rats [PMID:15951738]; anti-VEGFR2 antibody TTAC-0001 blocks
  sprouting of rat aortic rings [PMID:25942475].
- Testis: VEGFR inhibitors disrupt seminiferous cord formation and vascularization in
  cultured E13 rat testes; KDR protein in germ and interstitial cells [PMID:16672722].

## Expression-only papers

- Flk-1 up-regulated in vessels and neurons after VEGF infusion trauma / brain contusion
  [PMID:11934468; PMID:15785231].
- Retinal ganglion cell layer Vegfr-2 mRNA is high at baseline and essentially unchanged
  after optic nerve transection except for a decrease at 6 h [PMID:20187850].
- PMID:15885787 is a human pterygium/conjunctiva study (patient tissue), not rat.
- PMID:20097747 (hyaluronan butyric/retinoic ester, HBR, infarcted rat heart): HBR
  raises kdr mRNA in rat cardiomyocytes and Stro-1 cells [PMID:20097747 "significantly
  enhanced the gene expression of VEGF, kdr (encoding a major VEGF receptor), HGF, akt,
  and pim-1"]. This is expression regulation of Kdr, not a function of the Kdr protein.

## Ortholog donor provenance (QuickGO, 2026-10-28)

- Mouse Kdr: coreceptor activity and semaphorin-plexin signalling rest on an IGI with
  SEMA3E (PMID:25985275); cytokine binding is an IPI with gremlin-1 (Grem1, O70326,
  PMID:20660291); calcium ion homeostasis IDA PMID:8356051; surfactant homeostasis and
  cell maturation IMP PMID:12053176; lung/epithelial branching IMP PMID:16375885.
- Human KDR: cytosol is an HPA immunofluorescence IDA; macroautophagy, mitochondrial
  depolarization and mitochondrial fission are MGI IGI rows from PMID:23798385;
  negative regulation of gene expression and cellular response to H2S from PMID:26879375.
