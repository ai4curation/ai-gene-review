
## 2026-11-06: complete annotation review

Reviewed all 8 pristine seeded rows; non-review payloads/order and raw sources are preserved. Default Falcon research was attempted and returned HTTP403 authentication failure. No provider report was fabricated; this is manual research.

Identity: current P23354 is ATCC33913; primary PMID1655739 and PMID7496537 use NRRL B1459/ATCC13951. Frozen UniProt CONFLICT features record differences for all three proteins. This supports explicit strain-qualified inference, not an exact-assayed-protein assertion. Full papers were read through the URLs in ../fruB/fruB-source-analysis/primary-scope.md; the abstract-only publication caches were not rewritten. PMID1650911 was normally fetched once, remaining abstract-only.

- GO:0004747 IBA: UNDECIDED. The ribokinase reaction has not been established for Xanthomonas FruK.
- GO:0005829 IBA: ACCEPT. FruK acts on intracellular fructose 1-phosphate in the cytosol.
- GO:0005975 IEA: MODIFY. The carbohydrate-metabolic step is specifically fructose catabolism.
- GO:0008443 IEA: MODIFY. The supported kinase reaction is 1-phosphofructokinase activity.
- GO:0008662 EXP: ACCEPT. FruK phosphorylates fructose 1-phosphate at position6 using ATP.
- GO:0008662 IEA: ACCEPT. FruK phosphorylates fructose 1-phosphate at position6 using ATP.
- GO:0016301 IEA: MODIFY. The supported kinase reaction is 1-phosphofructokinase activity.
- GO:0016773 IEA: MODIFY. The supported kinase reaction is 1-phosphofructokinase activity.

No NEW rows are needed: specific refinements preserve existing participation claims without manufacturing process coverage. No generic binding proposal is added. PAINT losses were checked; FruA/FruB have no reported lineage loss, while FruK is absent from the available tree and its losses remain unassessed. The transport mechanism does not require importing an external standalone EI/HPr where the actual FruB fusion supplies those modules.
