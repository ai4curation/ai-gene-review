# SLC38A2 (SNAT2 / ATA2) curation notes

UniProt: Q96QD8 (S38A2_HUMAN), 506 aa, 11-TM, SLC38 / amino acid-polyamine-organocation
(APC) superfamily, "amino acid/polyamine transporter 2" family. HGNC:13448, chr 12.

## Core biology
SNAT2 is the **ubiquitously-expressed System A transporter**: a Na+-coupled, electrogenic,
pH-sensitive, Li+-intolerant symporter of small **neutral** amino acids, with a 1:1
Na+:amino-acid stoichiometry. It is the molecular correlate of the classic, adaptively
regulated "System A" activity.

- [PMID:10930503 "hATA2 mediates Na+-dependent transport of alpha-(methylamino)isobutyric acid, a specific model substrate for system A. The transporter is specific for neutral amino acids. It is pH-sensitive and Li+-intolerant. The Na+:amino acid stoichiometry is 1:1."]
- [PMID:10930503 "hATA2-specific mRNA is ubiquitously expressed in human tissues."]
- UniProt CC:FUNCTION: [file:human/SLC38A2/SLC38A2-uniprot.txt "Symporter that cotransports neutral amino acids and sodium ions from the extracellular to the intracellular side of the cell membrane"]

Substrates (UniProt CATALYTIC ACTIVITY, each as `AA(in) + Na(+)(in) = AA(out) + Na(+)(out)`,
ECO:0000250 from mouse Q9JHE5): Ala, Gly, Ser, Pro, Met, His, Asn, Gln, Thr, and weakly
Leu, Phe. MeAIB (N-methyl-AIB) is the diagnostic System A substrate. **Acidic amino acids
(Glu/Asp) are NOT substrates** — System A is strictly neutral. Glutamine is the
physiologically dominant cargo (links to mTORC1 via SLC7A5 antiport, glutamine/glutamate
cycle).

## Localization and regulation
- Plasma membrane (multi-pass), with an intracellular reserve pool in the TGN/endosomes;
  insulin recruits SNAT2 to the PM. Enriched in the somatodendritic compartment of neurons;
  at the axonal shaft but excluded from the nerve terminal. [file:human/SLC38A2/SLC38A2-uniprot.txt "Insulin promotes recruitment to the plasma membrane from a pool localized in the trans-Golgi network or endosomes."]
- Adaptively upregulated by **amino-acid starvation** (ATF4/AARE transcription + eIF2alpha-P
  / IRES cap-independent translation) and by **hypertonic (osmotic) stress** (cell-volume
  recovery). [PMID:16621798 "Both a starvation-dependent and a hypertonic increase of system A transport activity are due to the induction of SNAT2, the ubiquitous member of SLC38 family."]
- [PMID:15922329 "the up-regulation of SNAT2 is essential for the rapid restoration of cell volume after hypertonic stress."]
- Turnover controlled by NEDD4L (UniProt PTM) and by RNF5 ubiquitination under ER stress
  [PMID:25759021 "We identify regulation of the L-glutamine carrier proteins SLC1A5 and SLC38A2 (SLC1A5/38A2) by the ubiquitin ligase RNF5."].

## Physiological contexts (non-core / pleiotropic)
- Placental maternal-fetal amino-acid supply (By similarity); BBB amino-acid transport;
  glutamine supply for the neuronal glutamine/glutamate cycle; muscle (sarcolemma);
  mediator of arsenite-induced ER stress via glutamine/mTOR [PMID:22215663 "SNAT2 expression and activity are up-regulated by arsenite, in a manner dependent on activating transcription factor 4 (ATF4)"].

## Review decisions (summary)
- ACCEPT: all neutral-AA / Na+-symporter MF and the corresponding neutral-AA import BP terms,
  plasma membrane, sodium ion transmembrane transport.
- REMOVE: GO:0005515 bare protein binding (x3 IPI; RNF5, TMEM237, DCDC2 — uninformative,
  interactions real but term carries no function). GO:0015172 acidic amino acid transmembrane
  transporter activity (x2) and GO:0015800 acidic amino acid transport — biologically wrong
  for a strictly neutral System A transporter (over-propagated electronic mappings; source
  defect recorded on the ISS row).
- KEEP_AS_NON_CORE: cytoplasm (TGN/endosomal reserve pool), neuronal compartments
  (axon/dendrite/cell body), sarcolemma, female pregnancy (placenta), BBB transport,
  neurotransmitter transport / regulation of glutamate secretion (glutamine-glutamate cycle),
  cellular response to amino acid starvation, response to muscle activity, regulation of
  cellular response to stress / cellular response to arsenite (arsenic ER-stress role).
- MARK_AS_OVER_ANNOTATED: brush border (System A is basolateral, not apical), cerebral cortex
  development (expression != developmental role), glycine betaine transport (not a documented
  System A substrate; betaine = BGT1/SLC6A12), cellular response to mechanical stimulus
  (documented stimulus is osmotic/hypertonic, not mechanical), positive regulation of gene
  expression (CHOP) and positive regulation of RNA splicing (XBP1) — downstream UPR effects of
  the arsenite screen, not direct functions of a transporter.
