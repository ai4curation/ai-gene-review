# STX1B (syntaxin-1B, P61266) review notes

## Evidence base

Human-specific experimental data are limited to disease genetics, a splice-isoform localization study and
interaction screens. Function rests on mouse Stx1b genetics and on structural work with the ~84%-identical
paralog syntaxin-1A.

- Mouse Stx1b is the paralog that matters for central fast transmission: "STX1B null mutant mice died within 2
  weeks of birth" and "the frequency of spontaneous quantal release was lower" [PMID:24587181 "STX1A and 1B share
  a basic function as neuronal t-SNAREs"].
- Loss of both paralogs: "loss of Stx1 completely abolished fusion-competent vesicles and severely impaired
  vesicle docking"; "complete SNARE complex formation is required for vesicle fusion and priming" [PMID:27466336].
- Closed/open switch shown directly on syntaxin-1B: "the closed conformation of syntaxin-1 gates the initiation of
  the synaptic vesicle fusion reaction, which is then mediated by SNARE-complex/Munc18-1 assemblies"
  [PMID:18703708].
- Titration: "smaller readily releasable pool size, slower refilling rate of primed vesicles, and lower release
  probability" [PMID:24133272].
- NMJ: "it is required to maintain the efficiency of neurotransmission at the nerve-muscle synapse"
  [PMID:26203110].
- Disease: "mutations in STX1B, encoding syntaxin-1B, that are associated with both febrile seizures and
  epilepsy" [PMID:25362483].
- Isoform 2 (STX1B-DeltaTMD) "lacked the classical C-terminal transmembrane domain and localized to the nucleus"
  [PMID:18691641]; this is the sole source of the nucleus/centrosome/spindle IEA rows.

## Decisions

- Core MF GO:0005484 (GOA label "helical-bundle zippering fusogenic activity"; the local ontology still reports
  the old label "SNAP receptor activity", producing a label warning). Processes GO:0031629, GO:0016082,
  GO:0016079; location presynaptic active zone membrane / plasma membrane; complex GO:0031201. Second core:
  GO:0160321 vesicle docking activity, as in the STXBP1 review.
- "regulation of" terms transferred from mouse titration/knockout (positive regulation of NT secretion,
  regulation of SV priming, positive regulation of spontaneous release) MODIFIED to the direct process terms:
  syntaxin-1 is part of the machinery, not a regulator of it.
- Downstream readouts (EPSP, regulation of synaptic activity from zebrafish morphants, SV recycling, regulation of
  gene expression) marked over-annotated.
- Chick growth-cone study [PMID:21593320 "syntaxin 1B (Syx1B), a membrane trafficking protein, is a negative
  regulator of macropinocytosis"]: macropinocytosis kept non-core; "negative regulation of neuron projection
  development" marked over-annotated (suppressing collapse is not negative regulation of outgrowth).
- Synaptic vesicle membrane NAS from the syntaxin-1A SUMOylation paper marked over-annotated: the paper says
  syntaxin-1 and SNAP-25 "are anchored to the presynaptic membrane, whereas VAMP-2 is located on the SV membrane"
  [PMID:26635000]. SNAP25 review REMOVEd the same NAS claim; I chose MARK_AS_OVER_ANNOTATED because a minor
  vesicle-associated syntaxin-1 pool is plausible.
- Protein binding: rows with SNARE partners (VAMP1/2/5, SNAP29, SNAP47, STX2, STX4) MODIFIED to GO:0000149 SNARE
  binding; the rest REMOVED as uninformative. Note the AlphaFold-interface paper abstract names an FBXO23-STX1B
  interface while GOA/IntAct records the partner as FBXO28 (Q9NVF7); not resolved here (row removed either way).
- Cytosol (Reactome TAS) marked over-annotated: tail-anchored membrane protein.
