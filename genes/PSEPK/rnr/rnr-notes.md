# rnr curation notes

## 2026-09-01 annotation-reviewer pass

All nine seeded GOA rows were reviewed against Q88DE6 UniProt/HAMAP evidence
and Pseudomonas literature. Exoribonuclease II activity, RNA binding, mRNA
catabolism, and cytosolic localization are accepted. Broad nucleic-acid/nuclease
parents, RNA metabolism, and cytoplasm are retained as non-core.
GO:0006396 RNA processing is added from the target UniProt statement that RNase
R participates in maturation of structured RNAs, and is included in the core
function alongside mRNA catabolism.

Direct KT2440 work included RNase R among tested exoribonuclease deletions
[PMID:33089610 "Each mutant lacked either one exoribonuclease (PNPase, RNase R)
or one endoribonuclease (RNase E, RNase III, RNase G)."]. Same-genus biochemical
work found RNase R co-purifying with RNase E [PMID:15705581 "Most surprisingly,
the hydrolytic exoribonuclease RNase R was found to co-purify with RNase E."].
The latter grounds a reusable RNase R variant but not a KT2440 complex claim.

## 2026-11-10 module-completion pass

Harmonised with the new E. coli K-12 exemplar review (`genes/ECOLI/` same
symbol) for the RNase E degradation module: every row now carries a vetted
quote (HAMAP-derived UniProt text, or the E. coli experimental literature
for homology support); broad parent terms entailed by an accepted specific term
in this review are TOO_GENERAL rather than KEEP_AS_NON_CORE; ancillary binding
and cofactor rows are KEEP_AS_NON_CORE. No new provider deep research was run
(no API keys available in this session).
