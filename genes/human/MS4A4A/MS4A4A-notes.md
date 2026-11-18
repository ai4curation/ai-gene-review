# MS4A4A notes

Automated deep research was attempted with `just deep-research-falcon human MS4A4A --fallback perplexity-lite`, but the run timed out before producing a deep-research file. This review therefore uses cached GOA publications, the UniProt record, and the PANTHER family fetch.

MS4A4A encodes a four-pass membrane protein in the MS4A/CD20-like family. UniProt describes it as a "Membrane-spanning 4-domains subfamily A member 4A" with four predicted transmembrane helices, and GOA contains only localization and generic interaction annotations. The strongest curated localization evidence places MS4A4A at plasma membrane, plasma membrane raft, Golgi apparatus, and endoplasmic reticulum.

The primary Alzheimer-relevant evidence is the 2019 MS4A/TREM2 study. It found a genome-wide significant association between an MS4A-region SNP near MS4A4A and CSF soluble TREM2, and an independent missense signal in MS4A4A [PMID:31413141 "The top SNP was rs1582763, an intergenic variant nearest MS4A4A"; PMID:31413141 "Rs6591561 (MS4A4A p.M159V) was associated with CSF sTREM2"]. The same study reports that MS4A4A expression and TREM2 biology are linked in macrophage models: "MS4A4A and TREM2 colocalized on lipid rafts at the plasma membrane" and sTREM2 increased with MS4A4A overexpression while MS4A4A silencing reduced sTREM2 [PMID:31413141 "MS4A4A and TREM2 colocalized on lipid rafts at the plasma membrane"; PMID:31413141 "sTREM2 increased with MS4A4A overexpression, and that silencing of MS4A4A reduced sTREM2 production"].

The B-cell expression paper supports the MS4A-family context but does not establish a normal B-cell function for MS4A4A. It reports that MS4A4A was investigated because MS4A proteins can potentially hetero-oligomerize, but also found that normal B cells did not detect MS4A4A transcripts [PMID:23874341 "MS4A4A and MS4A8B transcripts were not detected in any normal B-cell sample"]. That paper remains useful for plasma-membrane localization in transfected cells but should not drive B-cell process annotations.

For curation, retain the subcellular-localization annotations as the high-confidence functional surface: MS4A4A is a multi-pass membrane protein at plasma membrane/raft and secretory pathway compartments. The generic `protein binding` annotations from high-throughput interactome studies should be marked over-annotated rather than accepted as a core molecular function. There is good evidence that MS4A4A modulates sTREM2 in macrophage models, but GOA does not contain a precise molecular-function or biological-process term for this; treat it as a suggested question/experiment rather than inventing a new GO annotation.

## 2026-06-20 second-pass audit

The second-pass audit confirmed the existing MS4A4A review and manual reference metadata. No annotation action changes were needed: MS4A4A remains curated conservatively as a four-pass membrane/raft and secretory-pathway protein with TREM2/sTREM2 modulation as the main unresolved functional question, while generic high-throughput protein-binding annotations remain over-annotated.

## 2026-11-18 ORGANELLES Golgi batch 3 (Golgi apparatus rows)

- Two GO:0005794 rows: IBA GO_REF:0000033 (`is_active_in`) and IDA PMID:31413141 (`located_in`,
  ARUK-UCL, 2020-09-16). Changed ACCEPT -> MARK_AS_OVER_ANNOTATED on both.
- Check: the cached full text of PMID:31413141 states the opposite of the row. Human macrophages were
  stained with KDEL, giantin and caveolin-1 markers: "We also detected partial colocalization of TREM2
  with both endoplasmic reticulum (KDEL) and Golgi (Giantin). In contrast, MS4A4A did not colocalize
  with these intracellular markers" (Fig. S9G, supplementary, not seen). MS4A4A was "primarily
  expressed on the plasma membrane". The Golgi (and ER) observation is TREM2's. TREM2's own GOA has
  only the raft row from this paper (same curator, same date) - a lead consistent with a swap.
- Source defect: WRONG_GENE_PRODUCT, ARUK_UCL, CHECK, PROBABLE, candidate TREM2 (Q9NZC2).
- IBA: PAINT node PTN000594777 (PTHR23320, Golgi IBD) has a single seed, UniProtKB:Q96JQ5 itself, so
  it rests wholly on the contradicted IDA; propagation_review SOURCE_BAD. The is_active_in qualifier
  is not supported (no MS4A4A activity at the Golgi).
- Golgi removed from core_functions.locations and from the description. REMOVE was the close
  alternative on both rows.
- Not changed (outside this batch): the GO:0005783 ER IDA from the same paper rests on the same
  sentence and should be revisited in an ER pass, together with the ER entries in the description and
  core_functions.locations.

- Follow-up after the #6521 review (2026-11-18): the GO:0005783 ER IDA from PMID:31413141 rests on the same sentence as the Golgi IDA [PMID:31413141 "We also detected partial colocalization of TREM2 with both endoplasmic reticulum (KDEL) and Golgi (Giantin). In contrast, MS4A4A did not colocalize with these intracellular markers"], so it also moved from ACCEPT to MARK_AS_OVER_ANNOTATED, and the ER was removed from core_functions.locations and the description. No other source places MS4A4A in the ER.
