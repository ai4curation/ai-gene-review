# rhlE curation notes

## 2026-09-01 annotation-reviewer pass

All 11 seeded GOA rows were reviewed against Q88D48 UniProt/HAMAP evidence and
same-genus literature. RNA helicase activity, ATP binding and hydrolysis,
ribosome biogenesis/assembly, and cytosolic localization are retained as core
or specific annotations. Broad nucleotide/nucleic-acid binding, hydrolase
activity, and cytoplasm are retained as non-core. The inferred temperature
response is `UNDECIDED` because no target-specific evidence was available.

The P. syringae study identifies RhlE in an active RNase E-RNase R complex
[PMID:15705581 "Additionally, the DEAD-box helicase RhlE was identified as part
of this protein complex."]. This supports a reusable RhlE variant, not direct
membership of Q88D48 in a KT2440 complex.

## 2026-11-10 module-completion pass

Harmonised with the new E. coli K-12 exemplar review (`genes/ECOLI/` same
symbol) for the RNase E degradation module: every row now carries a vetted
quote (HAMAP-derived UniProt text, or the E. coli experimental literature
for homology support); broad parent terms entailed by an accepted specific term
in this review are TOO_GENERAL rather than KEEP_AS_NON_CORE; ancillary binding
and cofactor rows are KEEP_AS_NON_CORE. No new provider deep research was run
(no API keys available in this session).
The formerly UNDECIDED ARBA row for response to temperature stimulus is now
MARK_AS_OVER_ANNOTATED: the only characterised temperature link (E. coli) is the
ribosome-assembly role already captured, not a response process.
