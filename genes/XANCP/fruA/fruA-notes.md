
## 2026-11-06: complete annotation review

Reviewed all 14 pristine seeded rows; non-review payloads/order and raw sources are preserved. Default Falcon research was attempted and returned HTTP403 authentication failure. No provider report was fabricated; this is manual research.

Identity: current P23355 is ATCC33913; primary PMID1655739 and PMID7496537 use NRRL B1459/ATCC13951. Frozen UniProt CONFLICT features record differences for all three proteins. This supports explicit strain-qualified inference, not an exact-assayed-protein assertion. Full papers were read through the URLs in ../fruB/fruB-source-analysis/primary-scope.md; the abstract-only publication caches were not rewritten. PMID1650911 was normally fetched once, remaining abstract-only.

- GO:0005351 IEA: REMOVE. FruA performs phosphoryl-transfer-coupled uptake, not carbohydrate:proton symport.
- GO:0005886 IBA: ACCEPT. FruA acts in the cytoplasmic membrane.
- GO:0005886 IEA: ACCEPT. FruA acts in the cytoplasmic membrane.
- GO:0005886 ISS: ACCEPT. FruA acts in the cytoplasmic membrane.
- GO:0008982 IEA: MODIFY. The phosphohistidyl-donor PTS reaction can be specified for fructose.
- GO:0009401 IBA: ACCEPT. FruA performs the membrane transport and terminal sugar-phosphorylation step of the PTS.
- GO:0009401 IEA: ACCEPT. FruA performs the membrane transport and terminal sugar-phosphorylation step of the PTS.
- GO:0009401 ISS: ACCEPT. FruA performs the membrane transport and terminal sugar-phosphorylation step of the PTS.
- GO:0015755 IEA: ACCEPT. FruA mediates transmembrane fructose uptake coupled to phosphorylation.
- GO:0016020 IEA: MODIFY. The supported membrane is the plasma membrane.
- GO:0022877 IEA: ACCEPT. The net phosphohistidyl-donor fructose PTS transporter reaction is supported.
- GO:0090563 IBA: MODIFY. The EIIB phosphocysteine transfers phosphate to D-fructose.
- GO:0090582 ISS: ACCEPT. FruA couples the terminal phosphocysteine transfer to fructose uptake.
- GO:1902600 IEA: REMOVE. The proton-transport inference inherits the unsupported symporter mapping.

No NEW rows are needed: specific refinements preserve existing participation claims without manufacturing process coverage. No generic binding proposal is added. PAINT losses were checked; FruA/FruB have no reported lineage loss, while FruK is absent from the available tree and its losses remain unassessed. The transport mechanism does not require importing an external standalone EI/HPr where the actual FruB fusion supplies those modules.
