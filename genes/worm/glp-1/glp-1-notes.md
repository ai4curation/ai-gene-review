# glp-1 (C. elegans) curation notes

UniProt P13508, "Protein glp-1" (contains glp-1/Notch intracellular domain). Second C. elegans Notch receptor
(paralog of lin-12). PANTHER (UniProt DR lines, verbatim): PTHR45836 (SLIT HOMOLOG), PTHR45836:SF23
(NEUROGENIC LOCUS NOTCH HOMOLOG PROTEIN 1). No IBA/PAINT rows in the GOA file for glp-1.

## Receptor

- Receiving cell for the distal tip cell (DTC) signal: [PMID:3677168 "We propose that glp-1 acts as part of
  the receiving mechanism in the interaction between the distal tip cell and germ line."]
- Integral membrane protein in the distal mitotic zone: [PMID:7607080 "GLP-1 is tightly associated with
  membranes of mitotic germline cells, supporting its identification as an integral membrane protein."]
- Ligands LAG-2 (DTC) and APX-1 [PMID:7607081; PMID:19502484 redundant LAG-2/APX-1 in DTC signaling].
- Domain architecture: 10 EGF-like, 3 LNG (LNR), 6 ankyrin repeats [PMID:1457827].

## Nuclear function

- RAM and ANK bind LAG-1; ANK repeats are strong transcriptional activators in yeast [PMID:9003776].
- Ternary complex with LAG-1 and LAG-3 [PMID:10830967].
- Only two primary germline targets, lst-1 and sygl-1 [PMID:32196486 "only lst-1 and sygl-1, the two known
  target genes of GLP-1 in the germline, fulfilled these criteria"]. These encode post-transcriptional
  regulators that act with FBF, so GLP-1's effects on FBF-2 protein are indirect (MARK_AS_OVER_ANNOTATED
  for post-transcriptional regulation of gene expression).

## Variant biology (for the module)

- Maternal glp-1 mRNA is translationally regulated, so GLP-1 protein is restricted to anterior blastomeres
  [PMID:9015263]. APX-1 from P2 signals to ABp. This is a worm-specific use of Notch in early embryonic
  asymmetry.
- Germline stem cell niche signaling (DTC LAG-2 -> germline GLP-1) is a canonical but tissue-specific use of
  the pathway. GLP-1 and LIN-12 are largely interchangeable biochemically [PMID:1769331].
- GLP-1 in dauer neurons maintains dauer [PMID:18599512].

## Deep research

Falcon deep research launched in background; see status note below.
