# Br140 (Q7JVP4) review notes

- BRPF homolog; scaffold of the Enok complex. [PMID:27198229 "MudPIT analysis of Flag affinity purifications of Flag-HA-tagged Enok, Br140, Eaf6, and Ing5 showed copurification of these four components."]
- Required for H3K23ac. [PMID:27198229 "Depletion of any of the four subunits led to reductions in the H3K23ac levels without affecting the H3K14ac levels"]
- Br140 purifications recovered Elg1 complex subunits. [PMID:27198229 "four subunits of the Elg1 complex (Elg1, Rfc4, Rfc38, and Rfc3) were identified by affinity purification using Br140 as the bait"]
- Decisions: shared Enok complex conventions (see enok-notes.md); histone reader IBA accepted at general level (specific marks unknown in fly); transcription/chromatin-remodeling IBAs kept non-core.

## Deep research (falcon, added after initial review)
- `Br140-deep-research-falcon.md` agrees: Br140 is the non-catalytic scaffold/regulatory subunit of the Enok complex ["Br140 supports Enok abundance and activity and broadens its substrate specificity *in vitro*."], supporting the acetyltransferase activator annotation. It also reports embryonic Br140 co-purification with PRC1 and Ash1 and co-binding with Pc at >2,000 genes (Kang 2017, not in GOA), and a PWWP-domain allele with an axon-targeting phenotype; the specific histone marks Br140 reads remain unmeasured. No annotation decisions changed.

## PR 4481 review fixes
- Core function now carries GO:0010698 acetyltransferase activator activity as molecular_function alongside contributes_to GO:0043994, with the PMID:27198229 quotes.
