---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AGFG1
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: P52594
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 2
citation_count: 2
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for AGFG1 (human)

## Current model (mechanistic narrative)

AGFG1 (HRB) is a nucleocytoplasmic adaptor protein that links the clathrin-dependent endocytic machinery to nucleocytoplasmic transport [PMID:18819912, PMID:10613896]. In the cytoplasm it colocalizes with clathrin-, AP-2-, EPS15-, and transferrin receptor-containing vesicles and binds the vesicular SNARE TI-VAMP (VAMP7); its depletion strongly reduces endocytosis of transferrin and TI-VAMP, establishing it as a required component of clathrin-dependent endocytosis [PMID:18819912]. AGFG1 also associates with the EH-domain proteins Eps15 and Eps15R through its EH-binding motifs, an interaction that occurs in the cytoplasm and that synergizes with AGFG1 to enhance Rev-mediated nuclear export [PMID:10613896]. Beyond these endocytic and Rev-export roles, no further mechanistic detail has been characterized in the available corpus.

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** GO:0005829 cytosol, GO:0005634 nucleus, GO:0031410 cytoplasmic vesicle
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport
- **partners:** VAMP7, EPS15, EPS15R
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2008 | High | HRB (AGFG1) was identified as a binding partner of the vesicular SNARE TI-VAMP (VAMP7) by yeast two-hybrid screening and confirmed by biochemical assays. In HeLa cells, HRB localized to the nucleus and cytoplasm, with cytoplasmic HRB colocalizing with clathrin-, AP-2-, EPS15-, and transferrin receptor-containing vesicles. Knockdown of HRB strongly reduced endocytosis of fluorescent transferrin and pHLuorin-TI-VAMP as measured by FACS, establishing HRB as a required component of clathrin-dependent endocytosis. | PMID:18819912 | The Journal of biological chemistry |
| 1999 | Medium | HRB (AGFG1) interacts with the EH (Eps15 homology) domain-containing proteins Eps15 and Eps15R via its EH-binding motifs, and this interaction occurs in the cytoplasm. Eps15 and Eps15R synergize with HRB to enhance Rev-mediated nuclear export function, and the EH-mediated Eps15–HRB interaction is required for this synergistic effect, connecting the endocytic molecular machinery to nucleocytoplasmic transport. | PMID:10613896 | The Journal of cell biology |

## Citations

- PMID:10613896
- PMID:18819912
