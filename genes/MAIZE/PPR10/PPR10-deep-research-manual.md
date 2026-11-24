# PPR10 (Zea mays, B8Y6I0) - manual literature synthesis

No deep-research API was available; this synthesis was compiled by hand from the cached
publications and the UniProt record (B8Y6I0, Swiss-Prot reviewed; GeneID 100302579).

## Identity and architecture
- 786-aa nucleus-encoded chloroplast protein of the P-class PPR family; predicted chloroplast
  transit peptide 1-95; 18-19 tandem PPR motifs forming a right-handed superhelix
  [file:MAIZE/PPR10/PPR10-uniprot.txt "Belongs to the PPR family. P subfamily."]
  [PMID:24162847 "In the absence of RNA binding, the nineteen repeats of PPR10 are assembled into a right-handed superhelical spiral."]

## Sequence-specific binding and RNA stabilisation
- PPR10 binds two similar intergenic elements, in the atpI-atpH and psaJ-rpl33 regions,
  in vivo and in vitro [PMID:19424177 "PPR10 interacts in vivo and in vitro with two intergenic RNA regions of similar sequence."].
- It is required for accumulation of the processed atpH 5'-end and psaJ 3'-end transcripts and acts as a
  bidirectional barrier to decay [PMID:19424177 "PPR10 serves as a barrier to RNA decay from either the 5' or 3' direction"].
- Recombinant PPR10 bound to the atpH site blocks 5'->3' and 3'->5' exoribonucleases and, with a generic
  exonuclease, is sufficient to define the native atpH 5'-terminus; the minimal site is 17 nt
  [PMID:21173259 "blocks both 5'→3' and 3'→ 5 exoribonucleases in vitro"].
- The small RNA "footprint" at the atpH site is absent in ppr10 null mutants, confirming in vivo protection
  [PMID:22156165 "both were missing in ppr10 mutant plants, as predicted if they accumulate due to stabilization by bound PPR10"].
  This paper generalises the PPR10 protein-barrier model to most processed chloroplast mRNA termini.
- PPR10 also stabilises a 3'-end downstream of psaI [PMID:30125002 "also stabilizes a 3'-end downstream from psaI"].

## Translational activation
- Bound PPR10 remodels the atpH ribosome-binding site, accounting for its enhancement of atpH translation;
  unprocessed atpH mRNAs in ppr10 mutants are translated less efficiently
  [PMID:21173259 "PPR10 binding not only stabilizes processed atpH RNAs but also enhances atpH translation"].

## Structure and oligomeric state
- Crystal structures (apo and psaJ-RNA bound) show an antiparallel intertwined homodimer
  [PMID:24162847 "PPR10 forms an antiparallel, intertwined homodimer"], but solution (SAXS) data indicate
  that PPR10 binds atpH RNA as a monomer [PMID:25609698 "PPR10 binds RNA as a monomer"], and dimerisation
  is governed by N-terminal segments [PMID:25231995 "the amino-terminal segments of PPR10 determine the dimerization state of PPR10"].
  Physiological relevance of the dimer is therefore doubtful.
- Six nucleotides of psaJ are recognised by six repeats following the PPR code [PMID:24162847].

## Location and phenotype
- Chloroplast stroma (UniProt, PMID:19424177). ppr10 mutants are yellow-green seedling-lethal with reduced
  photosynthetic complexes (UniProt disruption phenotype).
