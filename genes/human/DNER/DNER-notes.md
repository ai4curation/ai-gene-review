# DNER review notes

## Review scope and source availability

This review was completed without a generated deep-research-provider report because the
configured providers were quota-blocked. I therefore used the fetched human UniProt and
GOA records, the two GOA-cited publications, and additional primary papers cached under
`publications/`. PMID:11950833, PMID:15965470, PMID:16298139, PMID:18474614, and
PMID:20367751 are abstract-only in the local cache; PMID:27622512 and PMID:32296183 have
full text. Assertions below are limited accordingly.

## Protein architecture and localization

DNER is a 737-aa type-I single-pass transmembrane glycoprotein with an N-terminal signal
peptide, ten extracellular EGF-like repeats, one transmembrane segment, and a cytoplasmic
tail containing sorting motifs. The reviewed human UniProt record describes brain-enriched
expression and a somatodendritic membrane/endosomal distribution, but its NOTCH1-pathway
function is explicitly assigned only "by similarity" [file:human/DNER/DNER-uniprot.txt,
"Activator of the NOTCH1 pathway. May mediate neuron-glia interaction during
astrocytogenesis (By similarity)."].

The discovery study directly supports dendritic plasma-membrane and endosomal localization
and an interaction with AP-1, not direct binding to clathrin [PMID:11950833,
"DNER protein is localized to the dendritic plasma membrane and endosomes and is excluded
from the axons, even when overexpressed."] [PMID:11950833, "Direct in vivo binding of DNER
to the coat-associated protein complex AP-1 strongly suggests that DNER undergoes
AP-1-dependent sorting to the somatodendritic compartments from the trans-Golgi network
and subsequent passage through the endosomal system."]. The abstract does not identify the
endosomes as early endosomes, so the experimental GO:0005769 annotation cannot be fully
verified from the local source.

A later rat-neuron study provides the more precise AP-2 interaction and shows that DNER is
itself endocytic cargo whose polarized distribution depends on endocytosis [PMID:20367751,
"The DNER cytoplasmic domain binds to a clathrin adaptor protein complex-2 via a proximal
tyrosine motif and a 40 amino acid stretch in the mid-domain, but not by the C-terminal
tail."] [PMID:20367751, "Our data suggest that clathrin-independent endocytosis is critical
for the polarized targeting of somatodendritic proteins."]. This distinction matters for GO
review: DNER participates in its own endocytic sorting, but these data do not make DNER a
general regulator of endocytosis.

PTPRZ/PTP-zeta and pleiotrophin regulate DNER phosphorylation and surface residence. In
mouse Purkinje cells and Neuro-2A cells, phosphorylated DNER accumulated at the plasma
membrane, whereas normal DNER was actively endocytosed and inhibited neurite outgrowth
[PMID:18474614, "Several tyrosine residues in and adjacent to the tyrosine-based and the
second C-terminal sorting motifs of DNER were phosphorylated and were dephosphorylated by
PTPzeta, and phosphorylation of these tyrosine residues resulted in the accumulation of
DNER on the plasma membrane."] [PMID:18474614, "These observations suggest that
pleiotrophin-PTPzeta signaling controls subcellular localization of DNER and thereby
regulates neuritogenesis."].

## Cerebellar phenotype and the disputed Notch mechanism

The 2005 study established a Dner-dependent Purkinje-cell/Bergmann-glia developmental
phenotype in mouse cerebellum. It reported DNER at Purkinje dendrites, interaction with
Notch1-expressing Bergmann glia, and a gamma-secretase- and Deltex-dependent but
RBP-J-independent response [PMID:15965470, "DNER specifically binds to Bergmann glia in
culture and induces process extension by activating gamma-secretase- and Deltex-dependent
Notch signaling."] [PMID:15965470, "Inhibition of Deltex-dependent, but not
RBP-J-dependent, Notch signaling in Bergmann glia suppresses formation and maturation of
radial fibers in organotypic slice cultures."] [PMID:15965470, "Additionally, deficiency
of DNER retards the formation of radial fibers and results in abnormal arrangement of
Bergmann glia."]. Thus the reported response was noncanonical and should not be rewritten
as generic canonical RBP-J-dependent Notch signaling.

The phenotype is independently reinforced by the Dner-knockout study: mutant mice had
motor discoordination, delayed cerebellar morphogenesis, abnormal fissures, persistent
multiple climbing-fiber innervation, reduced Bergmann-glial GLAST, and impaired glutamate
clearance [PMID:16298139, "The cerebellum from the knockout mice showed significant
retardation in morphogenesis and persistent abnormality in fissure organization."]
[PMID:16298139, "Our results indicate that DNER takes part in stimulation of BG maturation
via intercellular communication and is essential for precise cerebellar development."].

However, a 2016 full-text replication study directly contradicted the proposed molecular
mechanism. With DLL1 as a positive control, DNER failed to activate NOTCH1, block C2C12
myoblast differentiation, or bind NOTCH1-Fc [PMID:27622512, "The established Notch ligand
Delta-like 1 (DLL1), but not DNER, activated Notch1 in a luciferase assay, prevented the
differentiation of myoblasts through Notch signaling, and bound Notch-fc in a cell-based
assay."] [PMID:27622512, "DNER is not a Notch ligand and its true function remains
unknown."]. DNER also lacks the DSL domain shared by established canonical Notch ligands.
Accordingly, the cerebellar/Bergmann-glial phenotype is retained as real ortholog evidence,
but direct NOTCH1 binding/ligand activity is left unresolved and is not asserted as a core
molecular function.

## Annotation decisions

- Retain plasma-membrane and dendrite localization; the discovery abstract verifies both.
- Retain calcium-ion binding as non-core structural/domain-level activity based on the
  calcium-binding EGF repeats, not as DNER's defining signaling activity.
- Replace generic AP1G1 `protein binding` and `clathrin binding` interpretations with
  AP-1 adaptor complex binding. The primary paper reports AP-1 complex binding, not
  clathrin binding.
- Add AP-2 adaptor complex binding by orthology from the rat-neuron trafficking study.
- Treat DNER's own endocytosis as cargo trafficking, not a general causal role in the
  endocytosis process.
- Do not accept transmembrane signaling receptor activity: no ligand-triggered receptor
  activity has been demonstrated for DNER.
- Treat neuron migration and synapse assembly as over-annotations. The cited 2002 source
  establishes expression/localization/sorting, not causal roles in those processes. The
  later mouse knockout supports cerebellar maturation and synaptic refinement phenotypes,
  but not the broad claims as written.
- Add Bergmann glial cell differentiation by orthology from the direct mouse cerebellar
  phenotype, without asserting a canonical Notch mechanism.

