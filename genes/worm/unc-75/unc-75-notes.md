# unc-75 review notes

## Session 1 (initial review)

- `just fetch-gene worm unc-75` resolved G5EE68 (TrEMBL, 514 aa), WormBase WBGene00006807,
  GeneID 182722. GOA has 20 rows keyed to G5EE68. No accession switch.
- Papers read in full: PMID:23468662 (Kuroyanagi 2013, EMSA, PY-NLS, unc-32 splicing),
  PMID:24910101 (Norris 2014, RNAcompete motif, splicing networks, synaptic phenotypes).
  Abstract only: PMID:12906792 (Loria 2003), PMID:7498734 (Nguyen 1995).
- The ISS rows from PMID:12906792 use Drosophila Bruno (UniProtKB:O02374, bru1) as With/From;
  checked by UniProt REST: O02374 is "Bruno", gene bru1, D. melanogaster. Consistent.
- Core MF: sequence-specific pre-mRNA intronic binding (GO:0097157). OLS: GO:0097157 is_a
  GO:0036002 pre-mRNA binding is_a GO:0003723 RNA binding. Pre-mRNA binding is NOT under
  GO:0003729 mRNA binding, so the mRNA-binding MODIFYs are lateral corrections, not refinements.
- Core BP: GO:0000381 regulation of alternative mRNA splicing, via spliceosome.
- GO:0006376 mRNA splice site recognition: per OLS its ancestors are protein-RNA complex
  assembly (spliceosome assembly lineage); UNC-75 binds regulatory intronic elements rather
  than recognizing splice sites as part of the spliceosome -> over-annotation.
- GO:0045202 synapse (IEA, GO_REF:0000108) is inferred from the cholinergic synaptic
  transmission process row. UNC-75 is a nuclear protein; a process inference cannot establish
  a synaptic location -> REMOVE + source_defects.
- Synaptic-transmission rows are downstream consequences of splicing regulation of synaptic
  genes (unc-64 etc.); kept as non-core (positive regulation terms) / over-annotated
  (bare process term).
- GO:0045664 regulation of neuron differentiation (IMP, PMID:24910101): the paper shows
  neuron-subtype-specific splicing ("specialization of neural cell types"), not an effect on
  differentiation, and Loria 2003 states unc-75 is not required for neuronal development.
  Full text read -> MARK_AS_OVER_ANNOTATED.
- Cytoplasm (IBA/IEA ARBA): no UNC-75 evidence; NLS mutants mislocalize, wild-type is nuclear.
  Family-level (CELF1/2 cytoplasmic roles) -> MARK_AS_OVER_ANNOTATED.
