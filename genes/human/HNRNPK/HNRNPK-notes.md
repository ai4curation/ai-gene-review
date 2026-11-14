# HNRNPK notes

Deep research providers unavailable; research from UniProt (P61978), cached publications, Reactome.

## Identity / function
- Heterogeneous nuclear ribonucleoprotein K: a poly(C)-binding protein with three KH domains and a
  K-interactive (KI) docking region. [UniProt "One of the major pre-mRNA-binding proteins. Binds
  tenaciously to poly(C) sequences."] Also binds poly(C) single-stranded DNA.
- Multifunctional: pre-mRNA processing/splicing (spliceosome C complex), mRNA stability and
  translation, transcriptional co-regulation (p53/TP53 response, LDLR transactivation,
  circZNF827 repressive complex), ncRNA-mediated chromatin regulation (Xist/X-inactivation),
  and acts as a signaling docking platform via its KI region.

## Localization (cell-surface benchmark)
- INTRACELLULAR: predominantly nucleus/nucleoplasm and chromatin; shuttles to the cytoplasm
  (UniProt: Cytoplasm; Nucleus). Also stress granules. NOT a cell-surface protein.
- Several GOA rows are high-throughput proteomic (HDA) co-enrichments inconsistent with a nuclear
  RNA-binding protein's genuine localization: extracellular exosome (PMID:20458337, 23533145),
  membrane (PMID:19946888), focal adhesion (PMID:21423176), cadherin binding (PMID:25468996) ->
  treated as over-annotations. Podosome (IEA/SubCell) and stress granule kept as non-core
  cytoplasmic locations.

## Curation
- Bare protein binding (very large IPI set): REMOVE per policy; informative binding kept as
  identical protein binding (self), protein domain specific binding (KI/SH3 docking).
- nucleic acid binding -> MODIFY to RNA binding; RNA processing / regulation of transcription
  (DNA-templated) / regulation of apoptotic process -> TOO_GENERAL (specific children asserted).
