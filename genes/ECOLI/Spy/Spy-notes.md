# Spy qualifier-aware annotation audit — 2026-08-29

## Coverage and evidence inventory

- The GOA snapshot contains 12 physical rows but 11 unique qualifier/evidence/reference signatures because GO:0044183 IDA PMID:26619265 is supplied twice, once by UniProt and once by EcoCyc. The review represents that exact duplicate signature once, consistent with qualifier-aware GOA reconciliation.
- Across the 11 unique signatures, qualifiers are 7 `enables`, 2 `located_in`, 1 `is_active_in`, and 1 `involved_in`. Evidence is 7 IDA, 2 IBA, 1 IEA, and 1 IPI.
- PMID:21317898, PMID:24497545, PMID:26619265, and PMID:27239796 have full text in the local cache. PMID:9068658 and PMID:20799348 are abstract-only, so their reviews are limited to claims exposed by those abstracts.

## IBA/PAINT provenance

The public PANTHER wrappers were used to inspect current family PTHR38102. Current PAINT contains one IBD assertion at PANTHER:PTN002445564: GO:0030288, seeded by UniProtKB:P77754 (Spy) and UniProtKB:P0AE85 (CpxP). This supports the periplasmic-localization IBA. Spy's own experimental evidence in the seed set is expected descendant evidence and is not circular.

The historical GO:0051082 IBA has the same GOA WITH/FROM list, but current PAINT no longer contains that molecular-function assertion at PTN002445564. Its propagation review is therefore `SOURCE_STALE_OR_MISSING`. This does not refute Spy's biology: Spy has direct IDA evidence for binding non-native clients and preventing aggregation.

## Holdase, carrier, and refolding decisions

Spy is directly demonstrated to suppress aggregation in situ in the periplasm. [PMID:21317898, “In vitro studies demonstrate that the Spy protein is an effective ATP-independent chaperone that suppresses protein aggregation and aids protein refolding.”] No cached study demonstrates escort to a defined acceptor molecule or destination, so carrier-specific GO:0140309 does not fit. Each obsolete GO:0051082 row is retained as an interim claim but `MODIFY` points to the general `NTR` holdase chaperone activity convention in `projects/UNFOLDED_PROTEIN_BINDING.md`.

Spy also has a separable folding-assistance function. Full-text kinetic analysis found that complete Im7 folding while bound was the only tested mechanism that fit all data. [PMID:26619265, “A good fit was only achieved when we globally fit the data to the kinetic mechanism that allows both folding steps 4 and 5, i.e., complete folding of Im7 while bound to Spy”] GO:0044183 is therefore accepted. The broader GO:0006457 BP is modified to GO:0042026 protein refolding, which more precisely describes recovery of experimentally unfolded clients without implying that Spy catalyzes folding chemistry.

## Other decisions

- GO:0005515 IPI PMID:26619265 is changed from `REMOVE` to `KEEP_AS_NON_CORE`. The exact Q03708/Im7 interaction is directly observed and quantitatively supported, but the generic term is not a core function and is not forced into a single replacement across the physical-interaction row.
- GO:0050821 protein stabilization is added as `NEW`: Spy suppresses aggregation and increases soluble steady-state levels of unstable periplasmic clients by up to 700-fold. [PMID:21317898]
- Both homodimerization signatures and all localization signatures are retained. Protein binding is excluded from `core_functions`; core biology is represented as interim in-situ holdase activity plus GO:0044183-assisted refolding.
