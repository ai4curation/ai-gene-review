# ClpP (CG5045, Q9VKY3) notes

## 2026-10-09 review session (module dmel_mitochondrial_clpxp)

- Deep research: ClpP-deep-research-falcon.md (first run completed after wrapper timeout).
- Matsushima et al. 2017 (S2 cells, full text):
  - [PMID:28814717 "ClpXP is composed of a proteolytic subunit, ClpP, and a chaperone-like subunit, ClpX, which carries an ATPase associated with diverse cellular activities (AAA+) domain6, 7."]
  - catalytic mutant: [PMID:28814717 "we established a copper-inducible cell line expressing a catalytically inactive ClpP mutant (S124A) in which the conserved serine in the proteolytic active site was replaced with alanine."]
  - substrate: [PMID:28814717 "Collectively, our results strongly suggest that DmLRPPRC1 is a specific substrate of ClpXP in Drosophila cells."]
  - complex: [PMID:28814717 "FLAG-tagged ClpX is co-immunoprecipitated with ClpP and DmLRPPRC1 but not DmSLIRP1."]
- Pareek et al. 2018: [PMID:30374414 "overexpression of another matrix protease, ClpP, partially rescued the defects associated with Lon inactivation, possibly by reducing the burden of unfolded mitochondrial proteins."]
- Per deep research (not cached): ClpP knockout is lethal; tissue loss gives cristae defects and
  photoreceptor degeneration [ClpP-deep-research-falcon.md "whole-animal ClpP knockout is **lethal**"].

## Decisions
- Core MF: serine-type endopeptidase activity in mitochondrial endopeptidase Clp complex.
- ATP-dependent peptidase activity (IBA/IEA): KEEP_AS_NON_CORE; ATP dependence is supplied by ClpX
  (holoenzyme-level activity). ClpX core function uses contributes_to GO:0004176.
- serine hydrolase activity (HDA) and ATPase binding (IBA): KEEP_AS_NON_CORE.
