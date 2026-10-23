# PDIA4 (horse, A0A3Q2IEH6) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

New review (no prior file). Horse partner of the donkey DONKEY40 target
(genes/EQUAS/PDIA4, A0A8C4LTV9). ProtNLM2 output was not opened or used.

### Identity
- A0A3Q2IEH6 (TrEMBL, 645 aa, Ensembl ENSECAP00000046265, VGNC:56044 PDIA4) is a
  full-length PDIA4 gene model, not a fragment or isoform. Same length as human
  PDIA4 P13667 (645 aa).
- Global alignment to human P13667: 90.08% identity over 645 paired residues, 100%
  coverage of both sequences [file:HORSE/PDIA4/PDIA4-bioinformatics/RESULTS.md].
- All three human redox-active CGHC sites (91-94, 206-209, 555-558) are conserved
  at the same positions; signal peptide present (horse 1-24 predicted); C-terminal
  ER retrieval motif REEL (human KEEL).
- PANTHER: PTHR18929:SF210 PROTEIN DISULFIDE-ISOMERASE A4 (from UniProt DR line), the
  same subfamily as human P13667, mouse P08003, rat P38659 and bovine Q29RV1
  (interpro/panther/PTHR18929/PTHR18929-entries.csv). Functions characterised for human
  ERp72 can therefore be transferred within the orthologous subfamily.

### Evolutionary evidence (PAINT, PTHR18929-paint.tsv)
- PTN000432607 (deep PDI-family node): IBD for protein disulfide isomerase activity,
  ER, protein folding, response to ER stress. Negations (IRD/IKR) at other lineages show
  curators actively judged placement; horse PDIA4 is inside the PDI clade inheriting them.
- PTN001448731 (taxon 6072, Eumetazoa): IBD cell surface, seeded by mouse Pdia4 and human
  PDIA4 only.

### Literature (cached)
- PMID:16677074: human ERp72 recombinant, peptide thiol-disulfide oxidase activity similar
  to PDI.
- PMID:12475965: ERp72 is in a large ER multichaperone complex (BiP, GRP94, PDI, ERdj3,
  CypB, GRP170, UGGT, SDF2-L1) bound to unassembled Ig heavy chains.
- PMID:7916014: ERp72 associates with thyroglobulin during maturation; described as an ER
  stress protein.
- PMID:19995400: ERp72 released by activated platelets and relocated to the cell surface.
- PMID:17081065: melanosome proteomics (source of human melanosome location).

### Deep research
`just deep-research-falcon HORSE PDIA4 --fallback perplexity-lite` failed: Edison API
returned 403 "Failed to authenticate" and the perplexity-lite fallback also failed. No
deep-research file was produced; review is based on the cached literature above, UniProt
and PAINT.

### Decisions
- Accept PDI activity (IBA + IEA), ER lumen, protein folding (core).
- ER (IBA, IEA) -> MODIFY to ER lumen; catalytic activity acting on a protein -> MODIFY
  to protein disulfide isomerase activity (verified ancestor via OLS).
- Cell surface, response to ER stress: KEEP_AS_NON_CORE.
- Melanosome (proteomic fraction, likely ER carry-over) and cell redox homeostasis
  (UniRule; thiol oxidoreductases acting on client proteins, not a homeostatic role):
  MARK_AS_OVER_ANNOTATED.

### Relative
- Closest characterised relative by phylogeny: human PDIA4 (P13667), same PANTHER
  subfamily SF210. No review exists under genes/human/ (checked); needs review.
- Modules mentioning PDI-family members: modules/chylomicron_assembly_secretion.yaml and
  modules/glutathione_thioredoxin_redox_systems.yaml mention PDI/P4HB, not PDIA4; no module
  specific to PDIA4.
