# lys9 (SPBC3B8.03, O59711) notes

## 2026-10-24

Re-reviewed S. pombe `lys9` after the `PTHR11133` LYS1/lys3 branch and the
S. cerevisiae `LYS9` pass. The fungal `PANTHER:PTN000875327` IBA is the
correct LYS9/lys9 sister placement to the `PTN000875292` LYS1/lys3 branch.
The broad `PANTHER:PTN000123605` `GO:0004753 saccharopine dehydrogenase
activity` placement is true at the mixed family node but over-generic for
`O59711`, which sits in `PTHR11133:SF22` and carries the exact NADP(+),
L-glutamate-forming saccharopine reductase reaction.

Deep research: `just deep-research-falcon SCHPO lys9` could not run because
the deep-research provider API keys are unavailable in this environment. Manual
searches for `Schizosaccharomyces pombe lys9`, `O59711`, `SPBC3B8.03`, and
saccharopine reductase found gene pages, pathway/product records, CRISPR/vector
resources, and broad fission-yeast screens that mention lys9, but no newer
paper changed the PTHR11133 placement, exact EC 1.5.1.10/GO:0004755 activity,
or cytosolic L-lysine-biosynthesis role.

Cached `PMID:16823372` is abstract-only; it supports the ORFeome localization
source for the cytoplasm and cytosol rows. `PMID:20537132` is full text, but
the cached text does not include the supplement naming the individual lys9
growth score; the paper does document the rich/minimal/lysine-supplemented
fitness screen, and the PomBase IMP call agrees with the exact activity, PAINT,
UniProt pathway, and PomBase GO-CAM evidence.
