# CD276 (B7-H3) notes

Deep research providers were unavailable in this environment (`just deep-research-falcon human CD276
--fallback perplexity-lite` failed: no provider). Research done from cached publications, UniProt and
PubMed lookups.

## Structure and localization
- UniProt Q5ZPR3: signal 1-28, extracellular 29-466 (Ig-like V-type 1, C2-type 1, V-type 2, C2-type 2),
  transmembrane 467-487, cytoplasmic 488-534. "SUBCELLULAR LOCATION: Membrane; Single-pass type I membrane protein."
- Conclusion: plasma membrane, type I, large 4Ig ectodomain exposed on the external side. Four annotated
  isoforms (4Ig-B7-H3 = isoform 1, 2Ig-B7-H3 = isoform 2); soluble shed forms are reported in the literature.

## Function
- Original description: [PMID:11224528 "Soluble B7-H3 protein binds a putative counter-receptor on activated T cells
  that is distinct from CD28, cytotoxic T lymphocyte antigen 4 (CTLA-4), inducible costimulator (ICOS) and PD-1"];
  costimulation of CD4+/CD8+ proliferation and selective IFN-gamma induction.
- Murine TREML2/TLT-2 was reported as a counter-receptor [PMID:18650384], but human work found
  [PMID:19544488 "We demonstrate in binding and functional studies that human TREML2 does not serve as a
  costimulatory receptor for human B7-H3"] and instead [PMID:19544488 "Our results point to a potent and
  consistent inhibitory role of human B7-H3 in T cell activation"].
- Net: receptor unidentified in human; direction of the T-cell effect disputed/context-dependent. Review uses
  unsigned regulation terms as core and keeps the signed IDA rows as non-core rather than overruling curators.

## Curation decisions
- GO:0005515 protein binding (TREML2, PMID:18650384) removed per the protein-binding policy; not upgraded to a
  receptor-binding term because the human interaction is contradicted.
- GO:0016020 membrane rows modified to plasma membrane.
