# ASPFU pptA notes

## 2026-11-06 PTHR12215 audit

- Family context: `pptA`/Q4X1W0 is in `PANTHER:PTHR12215:SF10`, the Sfp-type phosphopantetheinyl transferase subfamily that also contains budding-yeast `LYS5`, fission-yeast `lys7`, and *Emericella nidulans* `npgA`.
- PAINT context: `PTN000259224` asserts cytosol, holo-[acyl-carrier-protein] synthase activity, and protein maturation at the broad root; `PTN000954835` asserts L-lysine biosynthesis at a fungal node and is seeded by `UniProtKB:Q4X1W0` plus SGD/PomBase descendants.
- The core PptA reaction is protein phosphopantetheinylation. It modifies AarA, the lysine-biosynthesis alpha-aminoadipate reductase, and multiple NRPS/PKS carrier-domain enzymes. The individual PHI-base annotations to DHN-melanin, TAFC, fumiquinazoline C, fumigaclavine C, fumagillin, and gliotoxin biosynthesis are direct carrier-domain natural-product pathway assertions rather than distant phenotypes, and only the older broad pigment row needs refinement to DHN-melanin biosynthesis.
- Deep research using `falcon` with `perplexity-lite` fallback was attempted but failed because this checkout only exposed the `claude_code` provider.
- Literature search found no newer direct PptA biochemical paper that supersedes Neville 2005 or Johns 2017. Song et al. 2026 (PMID:41498629) is relevant to fumiquinazoline C biology and virulence, but it studies CsdA-LaeB regulation rather than PptA function directly.
