# daf-7 review notes

## Session 1

- `just fetch-gene worm daf-7` resolved UniProt P92172 (DAF7_CAEEL); 46 GOA rows.
- Literature: see `daf-7-deep-research-manual.md` (no provider deep research was
  available). Most GOA-cited papers before 2005 are abstract-only in the cache;
  full text was available for PMID:17900898, 15840165, 25303524, 26218657,
  18680713, 27799655, 34260587, 30024377 and 23705068.
- PMID:23705068 was flagged as a key paper, but it is about the sphingolipid-TORC1
  pathway; daf-7 is used only as an epistasis control [PMID:23705068 "Our
  additional analysis also suggests that the GlcCer/TORC1 pathway is DAF-7/TGF-β
  pathway independent"]. It is listed as a LOW-relevance reference.

### Decisions

- MF: cytokine activity (IBA), growth factor activity (IEA) and TGF-beta receptor
  binding (ISS) accepted: DAF-7 is a secreted TGF-beta-family ligand acting
  through DAF-1/DAF-4. Direct biochemical ligand-receptor binding is not shown;
  this is noted as a question.
- CC: extracellular region accepted for all four rows. The IDA rests on
  coelomocyte uptake of DAF-7::mCherry [PMID:26218657].
- Dauer: daf-7 is a negative regulator of dauer entry (Daf-c on loss). The rows
  that use the plain process terms "dauer entry" (involved_in) and "dauer larval
  development", and the general term "regulation of dauer larval development", are
  MODIFY to negative regulation of dauer entry or development (terms the gene
  already carries).
- "Detection of bacterium" and "detection of molecule of bacterial origin" are
  over-annotations. The detection step is performed by GPA-2/GPA-3 signalling in
  ASJ, and daf-7 is induced downstream [PMID:25303524]. The defense/avoidance rows
  are kept as non-core.
- "Cellular response to cGMP" is over-annotated: daf-7 is a transcriptional output
  of DAF-11/cGMP signalling in ASI, and the secreted ligand does not itself respond
  to cGMP.
- "Positive regulation of transcription by RNA polymerase II" (PMID:9834189) is
  over-annotated. It is an indirect pathway output: DAF-7 signalling inhibits DAF-3
  repressor activity on the myo-2 C subelement.
- Lifespan, feeding/pumping, eating behaviour, pheromone response, temperature
  response and gene-expression rows are kept as non-core phenotypic outputs of
  the neuroendocrine signal.
- No NEW terms. Further phenotypes (germline proliferation, autophagy, mate
  searching, CO2 avoidance) are pleiotropic pathway outputs and do not meet the
  NEW bar.
