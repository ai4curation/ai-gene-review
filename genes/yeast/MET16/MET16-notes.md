# MET16 (YPR167C, P18408) notes

Evidence journal (UniProt, Reactome and cached publications).

- PAPS reductase (thioredoxin), EC 1.8.4.8. Purified enzyme [PMID:3060034 "reduces 3'-phosphoadenylyl sulphate to adenosine-3',5'-bisphosphate and free sulphite at a stoichiometry of 1:1. Reduced thioredoxin is required as cosubstrate."].
- MET16 is the structural gene; its single Cys is dispensable in vivo [PMID:2203779 "we show that MET16 is the structural gene for PAPS reductase"]. Met4 is needed for MET16 transcription [PMID:2203779 "A mutation in the MET4 gene abolishes transcription of both genes MET16 and MET25."].
- PAPSe reduction to selenite [Reactome:R-SCE-2408518]: non-core.
- Glutathione biosynthetic process IMP from an overexpression/engineering study [PMID:22234534]: marked over-annotated, because Met16 supplies sulfite upstream and performs no step of GSH synthesis.


## 2026-10-26 complete fungal-member reassessment

Reassessed all 22 existing rows, core functions, biological summary and references under the current review and annotation-reviewer guidance. Original term, evidence, reference, qualifier and supporting-entity payloads are preserved; no annotation row was added in this session. Correct claims are assessed holistically across evidence codes. Generic protein-binding removals implement the uninformative-binding policy and do not deny the measured association or transfer a partner's activity.

Purified yeast PAPS reductase converts PAPS to PAP and sulfite and requires reduced thioredoxin (PMID:3060034). Its early steady-state interpretation does not establish an obligatory thioredoxin-first molecular sequence. The PAP-bound yeast structure (PMID:18991405; abstract cached) identifies the PAPS phosphate pocket and C-terminal Cys245 geometry. PMID:2203779 is the structural-gene study and reports an early cysteine-mutant interpretation; it should not be silently reconciled into modern direct mutagenetic proof. PMID:16008502 full text provides bacterial sulfonucleotide-reductase mechanistic context, not a native yeast assay. The description now distinguishes these levels of evidence. The existing selenate-reductase non-core assertion is supported by Reactome:R-SCE-2408518, explicitly describing MET16 reduction of PAPSe. PMID:22234534 glutathione engineering effects are retained as over-annotation of direct glutathione biosynthesis, not declared false. Other localization, regulation, and interaction assertions were considered across the complete row set.

Research provenance: the existing real research reports and curated primary/publication caches were read. The requested normal Falcon run with perplexity-lite fallback was attempted in parallel with publication caching; Falcon returned HTTP 403 and the fallback returned HTTP 401 insufficient quota. No provider report was fabricated. `just fetch-gene-pmids yeast MET16` completed successfully. Manual primary-source assessment and source-access limits are documented above and in the review; abstract-only evidence was not used to overturn experimental assertions as wrong-gene errors. Run logs are under `.cache/module-audit-logs/fungal-yeast-MET16-*.log`.
