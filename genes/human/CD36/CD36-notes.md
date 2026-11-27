# CD36 curation notes

Deep research was attempted for CD36 with the configured Falcon and Perplexity fallback command, but the local
`deep-research-client` only exposed the `claude_code` provider in this checkout. The review was therefore
grounded manually in the UniProt record, GOA rows, cached PAINT rows for PTHR11923, cached Reactome summaries,
and the publication cache fetched for the existing GOA references.

## Functional outline

- CD36 is a class B scavenger receptor with two transmembrane segments and a large extracellular loop. It is a
  plasma-membrane and cell-surface receptor for oxidized LDL, long-chain fatty acids, thrombospondins, bacterial
  diacylated lipopeptides, amyloid-beta, and additional multivalent ligands.
- Its core molecular roles are long-chain fatty-acid transmembrane transport, oxLDL/scavenger-receptor binding,
  TSP1/TSP2 antiangiogenic signaling, and co-receptor function for TLR4:TLR6 and TLR2:TLR6 ligand sensing.
- The CD36 branch of PAINT, PTN002629882, cleanly separates CD36-like fatty-acid/oxLDL receptors from the SCARB1
  HDL-receptor branch and the SCARB2 lysosomal cargo-receptor branch.
- Many mouse-derived Ensembl rows describe CD36-dependent tissue outcomes: cold-induced thermogenesis, taste,
  energy homeostasis, epithelial cholesterol absorption, and epileptic excitability. Those rows were weighed
  as contextual or over-annotated unless the gene product itself was the receptor or transporter for that process.
- The Ensembl GO_REF:0000107 rows for transcription, gene-expression control, oxidative stress, hydroperoxide,
  stilbenoid response, nuclear import, amyloid-fibril formation, superoxide removal, blood microparticle formation
  and ROS metabolism all trace to mouse Cd36 and ENSMUSP00000133008 rather than to direct human CD36 assays. Rows
  were kept only where the CD36 protein is the receptor, transporter or co-receptor executing the process;
  downstream gene-expression, oxidative-stress, amyloid-fibril and other tissue-readout rows were marked
  over-annotated.

## Existing module and GO-CAM coverage

- `modules/intestinal_retinoid_absorption.yaml` already models SCARB1/CD36 carotenoid uptake at the enterocyte
  brush border as one of several routes in intestinal vitamin A absorption. CD36 did not need a module edit in
  this PR because the module already names CD36 as a candidate carotenoid-uptake variant and the reviewed CD36
  rows here are centered on fatty-acid, lipoprotein, thrombospondin, and TLR co-receptor functions.
- The GO-CAM index contains several human CD36 annotons: fatty-acid transport by CD36 via LYN-mediated
  endocytosis, ARF6-dependent delivery of CD36 to the plasma membrane, oxLDL:CD36/TLR4 sterile inflammation,
  TSP1/CD36 inhibition of angiogenesis, and CD36 transport to the plasma membrane for muscle regeneration. These
  production models cover distinct CD36-centered contexts rather than a single reusable CD36/SCARB1 family module.
