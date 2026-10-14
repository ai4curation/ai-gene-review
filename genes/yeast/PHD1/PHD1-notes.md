# PHD1 re-review notes

## 2026-09-28 IBA and cached-publication pass

- Reviewed `PHD1-ai-review.yaml`, `PHD1-uniprot.txt`, the Falcon and Perplexity deep-research reports, and the cached publications for PMID-backed rows.
- Current PAINT in `interpro/panther/PTHR47792/PTHR47792-paint.tsv` places all four PHD1 IBA terms at `PANTHER:PTN000917459`: `GO:0005634`, `GO:0003700`, `GO:0043565`, and `GO:0045944`. PHD1 (`P36093`) is in `PTHR47792:SF1`, the only PTHR47792 subfamily; the PAINT node is a broad fungal APSES-family placement rather than a recent PHD1/SOK2-only placement.
- Several of the IBA donor lists include SGD:S000001526, the PHD1 target itself. That is valid for IBA: PHD1's experimental nuclear-localization, DNA-binding transcription factor, and positive regulation of Pol II transcription rows were descendant evidence used to place APSES-family IBDs.
- No IBA row needed action changes. The 2024 Cromie et al. structured-colony paper shows background-dependent redundancy of single `phd1` deletion in F13 colonies, but it does not contradict the gain-of-function and cascade evidence that PHD1 positively regulates pseudohyphal growth.

Cached publications checked:

- `PMID:8114741` is abstract-only locally and directly supports PHD1 overexpression-induced pseudohyphal growth, the SWI4/MBP1-like DNA-binding motif, and nuclear localization by indirect immunofluorescence.
- `PMID:16449570` is abstract-only locally and reports global mapping of Phd1 and other pseudohyphal-development transcription factors, with PHD1 and MGA1 acting as master-regulator target hubs.
- `PMID:11046133` is abstract-only locally and places PHD1 in the Sok2 transcription-factor cascade regulating FLO11-dependent cell-cell adhesion and filamentation.
- `PMID:19111667` and `PMID:19158363` are abstract-only high-throughput yeast transcription-factor DNA-binding studies that support sequence-specific DNA binding.
- `PMID:22124158` is abstract-only locally and supports Cdk8-dependent Phd1 turnover as a regulatory gate for pseudohyphal differentiation.
- `PMID:30271894` has full text locally and supports synthetic PHD1/FLO8 induction of pseudohyphal growth.
- `PMID:34280314` is abstract-only locally; the cached abstract does not mention Phd1, so the existing review correctly records the full-text cascade claim as unsourced to cached text.
- `PMID:39637084` has full text locally and supports the 2024 note that `phd1` deletion had little effect on the F13 day-5 structured-colony morphology tested there.

Newer literature search:

- PubMed query for `(Saccharomyces OR yeast) AND (PHD1 OR Phd1 OR YKL043W)` in 2024-2026 returned no direct PHD1 abstracts.
- Web searches for `Saccharomyces PHD1 Phd1 pseudohyphal 2024 2025 2026`, `YKL043W Phd1 yeast 2024 transcription factor PHD1`, and exact PHD1/pseudohyphal terms found the 2024 Cromie et al. structured-colony paper already captured in the review, older primary papers, and database/background hits, but no newer PHD1-specific evidence requiring a different annotation decision.

## 2026-10-01 current-GOA refresh

- Forced `just fetch-gene yeast PHD1 --force`. Current GOA has 12 rows. The four IBA assertions are unchanged biologically but the `GO:0005634` nucleus IBA now includes `UniProtKB:A0A0D1CVS5` as another descendant support.
- Re-fetched the PTHR47792 PAINT cache. The current node table still has one annotated node, `PANTHER:PTN000917459`, carrying the same four IBDs for `GO:0005634`, `GO:0003700`, `GO:0043565`, and `GO:0045944`; no `propagation_review` action change was needed.
- Preserved two rows that disappeared from current GOA as `retired: true`: the old UniProt combined-methods `GO:0003677` DNA-binding row from `GO_REF:0000120`, and the old UniProt keyword `GO:0006351` DNA-templated transcription row from `GO_REF:0000043`.
- Reviewed the new InterPro `GO:0003677` DNA-binding IEA from `GO_REF:0000002` and `InterPro:IPR036887` as `KEEP_AS_NON_CORE`: the APSES/HTH-family mapping is correct for PHD1 but generic compared with the existing `GO:0043565` and `GO:0003700` molecular-function rows.
- `just fetch-gene-pmids yeast PHD1` confirmed all nine PMID-backed references are cached. Web/PubMed searches for 2025-2026 Saccharomyces `PHD1`/`Phd1`/`YKL043W` functional literature found no newer direct PHD1 paper that changes the annotation decisions.
