# Fer2LCH (CG1469, Q9VA83) notes

## 2026-10-09 review session (module dmel_ferritin_complex)

- Deep research: Fer2LCH-deep-research-falcon.md. L chain nucleates the mineral core; H chain has the
  ferroxidase center [Fer2LCH-deep-research-falcon.md "These observations do **not** establish that Fer2LCH itself oxidizes iron."].
- [PMID:17603097 "The H subunit contains a ferroxidase center, which enables the mature heteropolymer to oxidize soluble ferrous iron, whereas the L chain provides the nucleation centers for deposition of the ferrihydrite mineral"]
- LCH predominant subunit; no IRE in its mRNA [PMID:11804801 "Ferritin is abundant in gut and hemolymph of larvae and adults"].
- Same iron absorption/detoxification genetics as Fer1HCH [PMID:23064556 "These results suggest an essential role of ferritin in removing iron from enterocytes across the basolateral membrane."].

## Decisions
- Shared complex/location/process decisions mirror Fer1HCH (same module).
- `iron ion import across plasma membrane` -> MODIFY to GO:0160179 intestinal iron absorption.
- `ferrous iron binding` (IDA) -> KEEP_AS_NON_CORE (complex-level; L chain lacks ferroxidase site).
- No ferroxidase annotation exists for Fer2LCH and none proposed.
- Core MF: GO:0140315 iron ion sequestering activity, in ferritin complex.
