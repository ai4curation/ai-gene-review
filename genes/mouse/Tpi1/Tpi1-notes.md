# Tpi1 curation notes

## 2026-11-25

- `just fetch-gene mouse Tpi1` seeded 41 GOA rows for reviewed UniProtKB:P17751 and cached the cited MGI/UniProt publications.
- `just fetch-gene-pmids mouse Tpi1` found the seeded PMIDs already cached after `fetch-gene`.
- `just paint-losses mouse Tpi1` reported no IRD or IKR loss on the mouse lineage.
- `just deep-research mouse Tpi1 --provider falcon --fallback perplexity-lite` could not run because Falcon and Perplexity were unavailable in this environment, so this review uses `Tpi1-deep-research-manual.md`.

## Review decisions

- Accepted `GO:0004807`, `GO:0006096`, and `GO:0006094`: triose-phosphate isomerase activity is the core TIM reaction in glycolysis and gluconeogenesis, and the PTHR21139 family review marks the shared PAINT nodes sound.
- Modified broad parent rows to the supported specific functions: `GO:0006006` to `GO:0006096`, `GO:0016853` to `GO:0004807`, and obsolete `GO:0061621` to `GO:0006096`.
- Marked `GO:0008929` and `GO:0019242` over-annotated because the methylglyoxal reaction is a slow elimination side reaction of the TIM intermediate rather than a separate evolved methylglyoxal synthase function.
- Removed bare `GO:0005515` protein binding from the Caspr2 proteomics row under the protein-binding policy.
- Marked Parkin `GO:0031625` transfers over-annotated because the human donor row comes from a weak TAP/MS candidate interactor screen.
- Kept `GO:0042803` and `GO:0046166` as non-core contextual rows: the functional homodimer is real, and GAP biosynthesis is the product direction of the isomerase reaction, but neither should outrank the EC 5.3.1.1 molecular function plus glycolysis/gluconeogenesis.

## GO-CAM comparison

The `61e0e55600001225` gluconeogenesis model asserts mouse `Tpi1` enabled by MGI:MGI:98797 with `GO:0004807`, part_of `GO:0006094`, and occurs_in `GO:0005829`. Those three claims are consistent with this gene review. The activity-level enabled_by reference `PMID:19289113` is a morphine/hippocampus 2-DE paper, but MGI curated it as a `GO:0004807` IDA for P17751 and the term itself matches the independently supported mouse TPI activity.
