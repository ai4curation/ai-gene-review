# CHAC2 review notes

## 2026-11-28

- `just deep-research-falcon human CHAC2 --fallback perplexity-lite` could not run because the configured deep-research providers were unavailable in this environment. I used the cached UniProt record, the GOA seed, the cached Kaur et al. PMID:27913623 abstract, the existing `PTHR12192` PAINT review, the completed `CHAC1` review, and cached Reactome events instead.
- CHAC2 is a compact follow-on to the reviewed CHAC1 member of `PTHR12192`. The PANTHER node `PTN004341755` asserts the three rows present on CHAC2 by IBA (`GO:0005737`, `GO:0006751`, `GO:0061928`), and `just paint-losses human CHAC2` reported no IRD or IKR losses on Q8WUX2.
- Kaur et al. report purified human CHAC2 activity against reduced glutathione (`kcat of 15.9 +/- 1.0 min-1 toward glutathione for human ChaC2`) and say ChaC2 degrades glutathione in the mammalian cytosol, with 10- to 20-fold lower catalytic efficiency than CHAC1 and constitutive rather than stress-inducible expression.
- No `NEW` annotation is needed: the GOA rows already cover the cytosolic EC 4.3.2.7 activity and the specific glutathione catabolic process. The two `GO:0006749` rows are true but too broad beside `GO:0006751`; the `GO:0005737` PAINT row is sound but refines to the direct `GO:0005829` cytosol row.
