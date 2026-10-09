# Fer1HCH (CG2216, Q7KRU8) notes

## 2026-10-09 review session (module dmel_ferritin_complex)

- Deep research (falcon) timed out on first attempt; rerun pending at time of review.
- Secreted 24-mer with Fer2LCH, loaded in Golgi, secreted to hemolymph
  [PMID:17603097 "In vivo expression of GFP-tagged holoferritin confirmed that iron-loaded ferritin molecules traffic through the Golgi organelle and are secreted into hemolymph."];
  [PMID:26192321 "inside a protein cage formed by 24 ferritin subunits of two types (Fer1HCH and Fer2LCH) in a 1:1 stoichiometry"].
- Ferroxidase center essential in vivo
  [PMID:17603097 "Thus, the ferroxidase activity of Fer1HCH provides an essential function in vivo and is likely required for iron loading of the ferritin shell."].
- Dietary iron absorption = export from enterocytes, plus tissue detoxification
  [PMID:23064556 "These results suggest an essential role of ferritin in removing iron from enterocytes across the basolateral membrane."].
- Iron-loaded ferritin as mitogen in culture; mutants arrest at L1
  [PMID:20628369 "iron-loaded ferritin acts as an essential mitogen for cell proliferation and postembryonic development"].

## Decisions
- `iron ion import across plasma membrane` (IMP, PMID:23064556) -> MODIFY to GO:0160179 intestinal iron
  absorption: the abstract describes efflux from enterocytes, ferritin is not a plasma membrane importer.
- `sleep` (IEP microarray) -> MARK_AS_OVER_ANNOTATED.
- proliferation, post-embryonic development, fusome, response to fungus -> KEEP_AS_NON_CORE.
- Core: ferroxidase (GO:0004322) and iron ion sequestering activity (GO:0140315, used for human FTH1
  by IDA) within ferritin complex, Golgi and extracellular region.
