# ANAPC7 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- **Key paper:** PMID:34942119 (full text). APC7 loss causes an intellectual disability syndrome.
  - Without APC7 the APC/C keeps its structure but cannot stably recruit and ubiquitinate substrates.
  - In neurons, APC7 is needed for Cdh1-APC degradation of Ki-67.
  - APC7 loss does **not** lengthen mitosis in human cells.
- **Enzyme-substrate adaptor activity (IDA, IBA):** accepted and used as the core MF.
- **Heterochromatin IMP:** MARK_AS_OVER_ANNOTATED. The paper places the substrate Ki-67 in heterochromatin and shows APC7 is nuclear-enriched; it does not show APC7 itself in heterochromatin.
- **Kept as non-core:**
  - Mitotic IBAs (GO:0045842, GO:0051301) and the mitotic-regulation NAS, because APC7 loss does not delay mitosis.
  - Brain development IMP (downstream outcome).
  - Spindle, microtubule and midbody locations; PTEN binding; meiotic NAS.
- **Affinage: trust gate tripped** (pairwise loss). It misses PMID:34942119, so nothing is used.

## 2026-10-04 round 2 (reviewer comments on #4061)

- **Heterochromatin IMP:** MARK_AS_OVER_ANNOTATED changed to MODIFY → GO:0120261 regulation of heterochromatin organization (verified in OLS). The IMP is functional evidence: APC7 loss reduces pericentromeric major satellite transcription (Fig. 7F), and Cdh1-APC with APC7 degrades the heterochromatin-associated Ki-67. Added to core_functions.directly_involved_in.
- **Reactome location rows:** kept ACCEPT, following the CDC27 precedent and my other APC/C reviews. Cytosol and nucleoplasm are now in core_functions.locations, which resolves the inconsistency the reviewer found. (ANAPC2 marks the same rows KEEP_AS_NON_CORE, so the repo is split.)
- **Cytoskeletal rows:** now supported by UniProt's location note (from PMID:18445686): spindle in metaphase, cytoplasmic microtubules in interphase. The HPA-only intercellular bridge row says it has no quotable source. GO:0005856 is noted as an ancestor of GO:0015630.
- **Other fixes:** the PMID:29033132 catabolism row quotes its own paper, and PMID:15678131 has a reference_review.
