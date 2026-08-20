# puuD / PP_3099 curation notes

## 2026-08-19

- The imported `puuD` name and EC 1.7.3.3 assignment are contradicted by the
  sequence classification: Q88IA0 is a 500-aa TssC1/VipB-family protein with
  IPR010269, IPR044031, IPR044032, PF05943, and PF18945. The independently
  generated report records that `Every InterPro/Pfam signature on the protein
  is a Type VI secretion sheath domain`
  [file:PSEPK/puuD/puuD-deep-research-openscientist.md].
- The authentic PuuD architecture is a COG3748 integral membrane domain fused
  to a C-terminal cytochrome c domain [PMID:26349049 "the identified gene
  (puuD) encodes a membrane protein with a C-terminal cytochrome c"]. In
  KT2440, Q88F11/PP_4289 has that architecture and lies with the downstream
  urate-oxidation genes; it is curated separately as the PuuD candidate.
- The OpenScientist boundary report independently identifies Q88IA0 as TssC1
  and explicitly notes the absence of a PP_3099-specific structural or
  biochemical study
  [file:PSEPK/puuD/puuD-deep-research-openscientist.md "No PP_3099-specific
  experimental structure or biochemistry."]. Its statement that the legacy
  name is specifically a "pre-2017" artifact was not imported because the
  available EMBL provenance establishes the source of the annotation, not that
  date-specific history.
- The canonical gene review and type VI module ownership remain in open draft
  PR #2515 (review approved). This urate batch preserves the independent
  provider report and the pathway-boundary rationale without creating a second
  competing review.
