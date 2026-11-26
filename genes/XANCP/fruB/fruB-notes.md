
## 2026-11-06: complete annotation review

Reviewed all 7 pristine seeded rows; non-review payloads/order and raw sources are preserved. Default Falcon research was attempted and returned HTTP403 authentication failure. No provider report was fabricated; this is manual research.

Identity: current P45597 is ATCC33913; primary PMID1655739 and PMID7496537 use NRRL B1459/ATCC13951. Frozen UniProt CONFLICT features record differences for all three proteins. This supports explicit strain-qualified inference, not an exact-assayed-protein assertion. Full papers were read through the URLs in ../fruB/fruB-source-analysis/primary-scope.md; the abstract-only publication caches were not rewritten. PMID1650911 was normally fetched once, remaining abstract-only.

- GO:0005737 IEA: ACCEPT. FruB is a soluble cytoplasmic phosphorelay protein.
- GO:0008965 IBA: ACCEPT. The enzyme-I module initiates the relay with phosphate from PEP.
- GO:0008965 IEA: ACCEPT. The enzyme-I module initiates the relay with phosphate from PEP.
- GO:0008965 ISS: ACCEPT. The enzyme-I module initiates the relay with phosphate from PEP.
- GO:0009401 IEA: ACCEPT. FruB provides the soluble phosphate relay for the fructose PTS.
- GO:0015764 IBA: UNDECIDED. Participation of this fused FruB in N-acetylglucosamine transport is unresolved.
- GO:0016772 IEA: MODIFY. The broad phosphorus-transfer annotation can be grounded in the defined EI reaction.

No NEW rows are needed: specific refinements preserve existing participation claims without manufacturing process coverage. No generic binding proposal is added. PAINT losses were checked; FruA/FruB have no reported lineage loss, while FruK is absent from the available tree and its losses remain unassessed. The transport mechanism does not require importing an external standalone EI/HPr where the actual FruB fusion supplies those modules.
