# benC (Q93HW3, Rhodococcus jostii RHA1) notes

## Provenance of this review

- Created as a cross-genus representative member of
  `modules/benzoate_upper_pathway.yaml`, so the module is grounded beyond
  Pseudomonas putida KT2440.
- Deep research: `just deep-research-falcon RHOJR benC` was attempted and failed with
  "Failed to authenticate" (provider credentials rejected), so there is no
  `-deep-research-*.md` file and none was written by hand. The review rests on
  the UniProt entry and the cached publications: PMID:11673430.
- Every quotation is verbatim from those cached sources; several are
  abstract-only, flagged with `full_text_unavailable` on the reference.

## This gene

- The structurally odd member of the family. RHA1 BenC is 512 aa against 336-348
  aa for the KT2440 and ADP1 proteins, and InterPro matches a C-terminal
  FadR/GntR C-terminal-like region (IPR011711, IPR008920) on top of the expected
  ferredoxin, FAD- and NAD-binding domains. The same pattern appears in the
  Rhodococcus sp. 19070 homologue [PMID:11375157 "The reductase components of
  these latter dioxygenases, BenC and XylZ, are 201 residues shorter than the
  deduced BopZ sequence."].
- Whether that extension is a real domain of the native protein or an artefact of
  the gene model is unresolved, so it is recorded as a `suggested_questions`
  entry with a truncation experiment rather than asserted either way. It is also
  the evidence behind the module note that the reductase is the most
  architecturally variable component of the pathway.
- The generic GO:0016491 and GO:0051536 rows are MODIFYed to the specific
  children the entry already carries (GO:0008860, GO:0051537).
