# SPA1 (Q9SYX2; At2g46340) curation notes

Session 2026-10-05/06 (phytochrome_photomorphogenesis module curation).

- Falcon deep research (`just deep-research-falcon ARATH SPA1`): the first attempt timed out after 600 s, but a retry produced `SPA1-deep-research-falcon.md`. It pointed to additional SPA1 kinase substrates, which were verified in primary papers (below).
- Identity check: SPA1_ARATH, Q9SYX2, At2g46340/At2g46350, 1029 aa.

## Domain architecture and complex
- N-terminal kinase-like domain, central coiled-coil, C-terminal WD40 [PMID:10205059 "SPA1 is a WD (tryptophan-aspartic acid)-repeat protein that also shares sequence similarity with protein kinases"].
- Coiled-coil binds COP1 coiled-coil [PMID:11461903 "the putative coiled-coil domain of SPA1 is necessary and sufficient for binding to COP1"].
- CUL4-DDB1-COP1-SPA complexes via WDXR motifs [PMID:20061554 "The interactions between DDB1 and COP1, SPA1, and SPA3 were disrupted by mutations in the WDXR motifs of MBP-COP1, His-SPA1, and His-SPA3"].
- SPA proteins self-associate / heteromerize [PMID:18812498 "The SPA proteins can self-associate or interact with each other"].

## Activity
- Stimulates COP1 E3 activity [PMID:12827204 "SPA1 stimulates the E3 activity of residual nuclear COP1 to ubiquitinate LAF1"]; [PMID:14597662 "the alteration of that activity by SPA1"]. Chosen MF: GO:0097027 ubiquitin-protein transferase activator activity.
- Kinase activity on PIF1 [PMID:31527679 "SPA1 acts as a serine/threonine kinase and directly phosphorylates PIF1 in vitro and in vivo"]. Caveat: Holtkotte et al. 2016 [PMID:27310313 "We therefore hypothesize that the sequence of the kinase-like domain has been conserved during evolution because it carries structural information important for the activity of SPA1 in darkness"]. Added as NEW (IDA) GO:0004674.
- Further substrates: HY5 [PMID:33686674 "SPAs can directly phosphorylate HY5 in vitro, and the phosphorylated HY5 is absent in the spaQ background in vivo"]; eIF2alpha C-terminus [PMID:38658612 "SPA1 directly phosphorylates the eIF2α C-terminus under light conditions"]. All of these reports involve the Huq group; no independent replication found.

## Photoreceptor inhibition
- phyA/phyB bind SPA1 and disrupt COP1-SPA [PMID:25627066 "light-activated phyA and phyB disrupt the interaction between COP1 and SPAs"]; [PMID:25744387 "the photoactivated phyB represses the association of SPA1 with COP1"].
- CRY1/CRY2 similar in blue light [PMID:21511871, PMID:21511872, PMID:21514160]. Context only for module.

## Decisions
- Protein binding rows: COP1 rows -> MODIFY to GO:0097027; other partners (HFR1, CO/COL1, SPA3/4, CRY1/2, phyB) REMOVE per policy (interactions real, captured in text).
- photomorphogenesis -> MODIFY to negative regulation of photomorphogenesis.
- nuclear speck (IEA) -> MODIFY to nuclear body.
- chloroplast organization (end mutant screen) -> over-annotated.
- Flowering / blue light rows kept as non-core.
