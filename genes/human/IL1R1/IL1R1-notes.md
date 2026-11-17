# IL1R1 notes

## Literature search (manual; no deep-research provider available)

Sources checked (2026-11-04):
- UniProt P14778 record (`IL1R1-uniprot.txt`): curated FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, PTM,
  DISEASE (CRMO3) and the PROSITE-ProRule-derived TIR NADase catalytic activity.
- All GOA-cited publications cached via `just fetch-gene-pmids human IL1R1` (abstracts for most;
  full text for PMID:33391283, PMID:23847621, PMID:33961781).
- Context only, not evidence: GO-CAM gomodel:59cc772c00000000 types the IL1R1 activity as GO:0004908,
  part_of GO:0070498, at the plasma membrane. (IL-1 signalling module/GO-CAM review proposed in
  ai4curation/ai-gene-review#5904.) After PR review this review refines IL1R1's MF to the child term
  GO:0004909 interleukin-1, type I, activating receptor activity, which separates the signalling type I
  receptor from the IL1R2 decoy.

## Key findings

- Cloned type I IL-1 receptor: single-pass integral membrane protein, three extracellular Ig-like
  domains binding IL-1, large cytoplasmic region [PMID:2530587 "Both are integral membrane proteins
  possessing a single membrane-spanning segment."].
- Binds both agonists; pro-IL-1alpha binds without processing, pro-IL-1beta does not
  [PMID:2950091].
- With IL1RAP forms the signalling complex; TIR domains recruit MYD88, IRAK, TOLLIP (UniProt
  FUNCTION).
- IL1RN binds IL1R1 and blocks IL1RAP recruitment [PMID:9062194 crystal structure; UniProt].
- Tyr-496 phosphorylation recruits PIK3R1 (UniProt PTM); IL-1beta/PDGF-BB costimulation induces
  IL1R1-PDGFRB association and PI3K/Akt signalling in aortic SMCs [PMID:16477012].
- Th1 cells express IL1R1 and produce IFN-gamma in response to IL-1beta plus IL-12 [PMID:10653850].
- Shed soluble form (sIL1R1) [UniProt PTM, PubMed:8142597].

## Curation observations

- The NAS rows from ComplexPortal (ECO:0005547, complex membership) for negative regulation of
  inflammatory response (PMID:33391283) and negative regulation of IL-1 signalling (PMID:23847621)
  derive from antagonist/decoy complexes (IL1RN:IL1R1). The inhibition is done by IL1RN (or IL1R2);
  IL1R1 is the blocked receptor. Removed.
- The NAD+ nucleosidase IEA comes from the TIR-domain ProRule. No experimental NADase activity has
  been reported for IL1R1; its TIR domain acts as a signalling scaffold. Marked as over-annotation.
