# TP53BP2 notes

- Manual research substituted for automated deep research because no configured
  deep-research provider keys were available in this child checkout.
- Core function: ASPP2 binds p53-family transcription factors and stimulates
  apoptosis-selective p53/p63/p73 transcriptional programs
  [PMID:11684014; PMID:14729977; PMID:18275817].
- The TP53BP2 `GO:0005515 protein binding` rows are direct interaction rows
  from low-throughput and high-throughput studies. They are removed only under
  the unqualified-protein-binding policy; the decisions do not dispute the
  reported interactors or the preserved WITH/FROM values.
- `GO:0045786 negative regulation of cell cycle` is kept for TP53BP2 because
  ASPP2 inhibits APP-BP1/NAE1-dependent NEDD8 conjugation to CUL1 and reduces
  APP-BP1-driven proliferation [PMID:12694406]. The same term is not kept for
  PPP1R13B, whose direct p53-family evidence is apoptosis-selective rather than
  cell-cycle inhibitory.
- The perinuclear rows are retained for ASPP2 based on APCL-driven
  translocation [PMID:10646860] and the UniProt subcellular summary. The HPA
  cytosol and cell-junction rows are kept as non-core localization evidence.
- `GO:0008157 protein phosphatase 1 binding` is proposed as the informative
  molecular-function term for ASPP2 rows that only asserted bare PP1 catalytic
  subunit binding [PMID:21998301].
- ASPP2 also has a non-core epithelial tight-junction role, where it scaffolds
  protein phosphatase 1 and YAP in an apical-lateral polarity complex
  [PMID:25360797]. This review uses that paper to support junctional
  localization and leaves detailed polarity/Hippo signaling as a candidate
  module or GO-CAM rather than adding a broad process term.
