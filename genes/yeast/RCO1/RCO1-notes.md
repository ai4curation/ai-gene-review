# RCO1 curation notes

## 2026 IBA re-review

Re-checked the two current RCO1 IBA annotations against GOA and the cached
`PTHR47636` PAINT table:

- `GO:0006357 regulation of transcription by RNA polymerase II` traces to
  `PANTHER:PTN001236278`, with budding-yeast RCO1 itself as the curated descendant
  evidence. The term is broad, but it is biologically sound for the Rpd3S subunit that
  helps suppress cryptic intragenic and antisense transcription during Pol II
  transcription, so the review now accepts it rather than proposing duplicate
  replacements to `chromatin organization` and `negative regulation of antisense RNA
  transcription`.
- `GO:0032221 Rpd3S complex` also traces to `PANTHER:PTN001236278`, supported by both
  the SGD Rco1 annotation and the two fission-yeast Rco1-family descendants in PomBase.

Both IBA rows are sound for RCO1, so the YAML now records the GOA `WITH/FROM` lists as
`supporting_entities` and adds `propagation_review.root_cause: NO_FAILURE_CORE` with
the PTN ancestral node as the source entity.

I also rechecked the cached high-throughput interaction publications behind the
`GO:0005515 protein binding` rows. They support physical associations, including Rpd3S
complex partners and chaperone/interactome hits, but not an evidence-backed replacement
molecular-function term. Those rows were changed from `KEEP_AS_NON_CORE` to `REMOVE`
under the current generic-protein-binding policy; that recommendation does not dispute
the reported interactions.

The newer-paper search found the 2023-2024 Rpd3S structural literature already discussed
in the Falcon deep-research report, but no later RCO1 paper that changes these IBA or
generic-protein-binding calls.
