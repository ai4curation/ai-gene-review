# CAR2 (YLR438W, P07991) notes

Evidence journal (no paid deep research run; built from UniProt and cached publications).

- Ornithine aminotransferase (OTAse), EC 2.6.1.13, class-III PLP-dependent aminotransferase; transaminates L-ornithine with 2-oxoglutarate to L-glutamate 5-semialdehyde + L-glutamate, the second step of arginine degradation [UniProt:P07991].
- Gene identity: "The cargB or CAR2 gene, coding for ornithine aminotransferase, was isolated by functional complementation of a cargB- mutation in Saccharomyces cerevisiae" [PMID:3036506].
- Regulation: inducible; "The cargB transcript was not detected in the wild-type strain grown under non-induced conditions"; Ty1 insertions upstream give constitutive, mating-type-dependent expression [PMID:3036506]. UniProt: regulated by arginine and urea.
- Location: soluble (cytosolic) fraction [PMID:205532 "the two first catabolic enzymes, arginase and ornithine aminotransferase, were in the"]. Contrast with mammalian/plant OAT (mitochondrial matrix).

## Curation decisions
- Core MF GO:0004587; BP GO:0006527; CC GO:0005829.
- Mitochondrion IBA (PTN000241155, animal/plant mitochondrial OATs; no fungal seed): REMOVE - yeast OAT is soluble/cytosolic by fractionation in which mitochondrial matrix enzymes of the acetylated cycle sedimented with mitochondria.
- L-proline biosynthetic process (UniPathway IEA): KEEP_AS_NON_CORE. The GSA/P5C product can in principle be reduced to proline, but in yeast arginine nitrogen is routed via P5C to glutamate (PUT2); the arginase-2 MetaCyc framing (to proline) is the YeastCyc pathway context.


## 2026-10-26 systematic arginase-pathway audit

Reviewed every one of the 19 original annotations and all core functions using the review and annotation-reviewer workflows. Machine payloads, row order, evidence codes, qualifiers, source identifiers and WITH/FROM values were preserved. No NEW rows were added.

Native PMID:205532 fractionation directly separates soluble OAT from particulate acetylated-pathway enzymes, supporting cytosol and rejection of the inherited mitochondrial location specifically for budding yeast. No argument rests on donor count or lack of fungal donors. Broad cytoplasm is refined to cytosol. PMID:6997271 demonstrates the proline intermediate in the tested arginine-degradation conditions, making the existing proline-biosynthesis role a real secondary route rather than a hypothetical side reaction. This result must not be transferred to every fungus without target evidence.

Normal publication caching passed. Genuine Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota errors prevented a report. Manual source review is recorded here, with no fabricated provider-named research file. Abstract-only and bibliographic-only access are distinguished from full text; unknown target supplementary details are not treated as a contradiction. Logs are under `.cache/module-audit-logs/arginase-yeast-CAR2-*`.

The initial focused validation passed. Record sections are backfilled, and final schema/term/reference validation, rendering and helper-history checks are recorded in the same log directory. Actions: ACCEPT 13, KEEP_AS_NON_CORE 2, MODIFY 3, REMOVE 1.
