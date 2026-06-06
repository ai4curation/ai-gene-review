# CACYBP (Calcyclin-Binding Protein / SIP / Siah-Interacting Protein) — research notes

UniProt: Q9HB71 (CYBP_HUMAN). Synonyms: S100A6BP, SIP, S100A6-binding protein, Siah-interacting protein.
HGNC. Aliases SIP = Siah-Interacting Protein.

## Core molecular/cellular function: adaptor/bridge in a Siah1-based E3 ubiquitin ligase complex
- CACYBP/SIP serves as a molecular bridge in ubiquitin E3 complexes, participating in calcium-dependent ubiquitination and proteasomal degradation of target proteins, notably beta-catenin (CTNNB1).
  [file:human/CACYBP/CACYBP-uniprot.txt "May be involved in calcium-dependent ubiquitination and subsequent proteasomal degradation of target proteins. Probably serves as a molecular bridge in ubiquitin E3 complexes. Participates in the ubiquitin-mediated degradation of beta-catenin (CTNNB1)."]
- Component of a large E3 complex composed of UBE2D1, SIAH1, CACYBP/SIP, SKP1, APC and TBL1X; interacts directly with SIAH1, SIAH2 and SKP1.
  [file:human/CACYBP/CACYBP-uniprot.txt "Component of some large E3 complex at least composed of UBE2D1, SIAH1, CACYBP/SIP, SKP1, APC and TBL1X. Interacts directly with SIAH1, SIAH2 and SKP1."]
- Siah1 is the central component of a multiprotein E3 ubiquitin ligase complex that targets beta-catenin for destruction in response to p53; the complex comprises Siah1, SIP, Skp1, and the F-box protein Ebi.
  [PMID:16085652 "Siah1 is the central component of a multiprotein E3 ubiquitin ligase complex that targets beta-catenin for destruction in response to p53 activation. The E3 complex comprises, in addition to Siah1, Siah-interacting protein (SIP), the adaptor protein Skp1, and the F-box protein Ebi."]
- Structural basis: SIP engages Siah1 by an N-terminal dimerization domain and a consensus PXAXVXP motif; its C-terminal domain binds Skp1 and protrudes to form the scaffold bringing substrate and E2 into apposition.
  [PMID:16085652 "An N-terminal dimerization domain of SIP sits across the saddle-shaped upper surface of Siah1... The C-terminal domain of SIP, which binds to Skp1, protrudes from the lower surface of Siah1, and we propose that this surface provides the scaffold for bringing substrate and the E2 enzyme into apposition in the functional complex."]
- Both the N-terminal dimerization element and the Siah-binding element are required for mediating beta-catenin destruction.
  [PMID:16085652 "SIP engages Siah1 by means of two elements, both of which are required for mediating beta-catenin destruction in cells."]

## S100/calcyclin binding (calcium-dependent)
- Homodimer; interacts with S100 family proteins S100A1, S100A6 (calcyclin), S100B, S100P, S100A12 in a calcium-dependent manner.
  [file:human/CACYBP/CACYBP-uniprot.txt "Homodimer. Interacts with proteins of the S100 family S100A1, S100A6, S100B, S100P and S100A12 in a calcium-dependent manner"]
- The name derives from binding to calcyclin (S100A6). High-throughput S100 interaction profiling (PMID:31837246) characterized S100 family PPIs quantitatively.

## Localization
- Nucleus and cytoplasm. Cytoplasmic at low calcium; upon retinoic acid induction and calcium increase in neuroblastoma cells, localizes to both nucleus and cytoplasm; nuclear fraction may be phosphorylated.
  [file:human/CACYBP/CACYBP-uniprot.txt "Cytoplasmic at low calcium concentrations. In neuroblastoma cells, after a retinoic acid (RA) induction and calcium increase, it localizes in both the nucleus and cytoplasm."]

## Homodimerization
- X-ray crystallography and structural studies show SIP/CACYBP forms a homodimer via its N-terminal dimerization domain. [PMID:16085652]

## High-throughput / contextual annotations (protein binding IPI)
- PMID:25036637 (chaperone-cochaperone interaction network LUMIER) — generic high-throughput PPI.
- PMID:31837246 (S100ome FP assay) — supports S100 protein binding specifically.
- PMID:31980649 (EGFR network rewiring in CRC, membrane Y2H) — generic interactome.
- PMID:33961781 (BioPlex dual proteome interactome) — generic high-throughput PPI.
- PMID:36115835 (fragmentomics PDZ affinity mapping) — generic interactome.
- These collapse to generic "protein binding" (GO:0005515) and are uninformative individually.

## Exosome
- PMID:20458337 (B-cell exosome proteome) — high-throughput MS localization; not a functional localization for a nucleocytoplasmic adaptor.

## Orthology-transferred developmental/process terms (GO_REF:0000107, Ensembl Compara)
- heart development, cardiac muscle cell differentiation, response to growth hormone, positive regulation of DNA replication, cellular response to calcium ion, nuclear envelope lumen, cell body, protein domain specific binding, tubulin binding. These are automatically transferred from orthologs and are not supported by direct human mechanistic evidence; mostly over-annotations relative to the core E3-adaptor role. Cellular response to calcium ion is consistent with the calcium-dependent S100 binding mechanism but remains a broad transferred term.

## Assessment summary (core vs non-core)
- CORE: SCF/Siah1 E3 ubiquitin ligase complex membership (part_of); molecular adaptor activity (bridge); ubiquitin protein ligase binding (Siah1/Siah2); S100 protein binding (calcium-dependent, basis of the protein's named function); protein homodimerization activity; beta-catenin destruction complex; nucleus/cytoplasm localization.
- NON-CORE / contextual: heart development, cardiac muscle cell differentiation, response to growth hormone, positive regulation of DNA replication (orthology-transferred phenotypes); cellular response to calcium ion (broad).
- OVER-ANNOTATED / uninformative: protein binding (GO:0005515) generic IPI x several; extracellular exosome; tubulin binding (InterPro IEA, no direct human evidence); protein domain specific binding; nuclear envelope lumen; cell body.
