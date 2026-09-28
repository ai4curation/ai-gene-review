# PHD1 re-review notes

## 2026-09-28 IBA and cached-publication pass

- Reviewed `PHD1-ai-review.yaml`, `PHD1-uniprot.txt`, the Falcon and Perplexity deep-research reports, and the cached publications for PMID-backed rows.
- Current PAINT in `interpro/panther/PTHR47792/PTHR47792-paint.tsv` places all four PHD1 IBA terms at `PANTHER:PTN000917459`: `GO:0005634`, `GO:0003700`, `GO:0043565`, and `GO:0045944`. PHD1 (`P36093`) is in `PTHR47792:SF1`, so these are direct SOK2/PHD1 APSES-family transfers.
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
