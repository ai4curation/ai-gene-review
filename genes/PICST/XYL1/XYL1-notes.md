# XYL1 (Scheffersomyces stipitis) notes

## 2026-10-01 re-review (GOA refresh)

- Nine IEA rows are no longer present in the current GOA snapshot and were marked
  `retired: true` (reviews retained): GO:0016616 (GO_REF:0000117), GO:0042732 D-xylose
  metabolic process (GO_REF:0000043), the six Ensembl Compara ortholog-transfer rows
  (GO_REF:0000107: GO:0003729 mRNA binding, GO:0004032 aldose reductase (NADPH) activity,
  GO:0019388 galactose catabolic process, GO:0019568 arabinose catabolic process,
  GO:0034599 cellular response to oxidative stress, GO:0071470 cellular response to osmotic
  stress) and GO:0042843 D-xylose catabolic process (GO_REF:0000120).
- GO:0042843 D-xylose catabolic process is now delivered via UniPathway mapping
  (GO_REF:0000041, UPA00810); reviewed and ACCEPTed.
- GO:0016491 oxidoreductase activity (GO_REF:0000120): REMOVE -> KEEP_AS_NON_CORE (general
  but not wrong; REMOVE was paired with a replacement term, which is a MODIFY pattern).
- Dropped NEW GO:0045014 carbon catabolite repression of transcription by glucose: XYL1 is
  the target of glucose repression, not a participant in the repression mechanism (fails the
  participation test). Removed the matching core_functions entry.
- Dropped NEW GO:0044577 D-xylose fermentation: it is_a GO:0042843 D-xylose catabolic process,
  which the gene already carries (ancestor/descendant redundancy).
- Dropped proposed term "intracellular xylitol accumulation" (a pathway-imbalance phenotype,
  not a gene-product process).
- Replaced non-verbatim supporting_text in core_functions and the cytoplasm NEW row with
  verbatim quotes.
