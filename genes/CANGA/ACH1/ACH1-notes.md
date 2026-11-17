# ACH1 notes

## 2026-11-17 review

QuickGO returned no rows for C. glabrata ACH1/Q6FPF3 through `just fetch-gene`, but this was a local fetch edge case rather than a genuinely unannotated entry: the QuickGO search endpoint returns the current Q6FPF3 annotations when queried directly without the `includeFields=taxonName` expansion that fails for taxon 284593. UniProt and the fetched PANTHER member table place Q6FPF3 in `PTHR43609:SF1`, the same single-subfamily Ach1/CoaT family that contains S. cerevisiae ACH1, C. albicans ACH1, N. crassa acu-8 and A. nidulans CoaT.

PAINT has a single root transferase node, `PTN000484586`, carrying both `GO:0003986 acetyl-CoA hydrolase activity` and `GO:0008775 acetate CoA-transferase activity`. The S. cerevisiae re-characterization paper reports that Ach1p's highest activity is CoASH transfer from succinyl-CoA to acetate and that acetyl-CoA hydrolase activity is minor, so the transferase term is the better core molecular function while the hydrolase row should be kept as non-core.

Carman et al. support Candida ACH1 conservation: C. albicans ACH1 complemented the S. cerevisiae ach1 deletion on acetate medium. That is not direct evidence for C. glabrata ACH1, but it supports the PAINT placement across Saccharomycetales/Candida alongside the direct S. cerevisiae and A. nidulans seeds.

I searched PubMed/web for `"Q6FPF3" ACH1 "Candida glabrata"` and `"CAGL0J04268g" ACH1` on 2026-11-17. I found product pages and Swiss-Prot/EnsemblFungi-derived records but no newer primary C. glabrata ACH1 biochemical or localization paper.

The Q6FPF3 UniProt function and cytoplasm comments are electronically inferred and carry two caveats seen on sibling Ach1 records: the old EC 3.1.2.1 hydrolase framing is now secondary to CoA transfer, and the cholesterol-synthesis wording is a mammalian carryover that does not fit an ergosterol-producing fungus.
