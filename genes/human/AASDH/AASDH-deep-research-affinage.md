---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AASDH
affinage_run_date: 2026-06-09T22:02:35
uniprot_accession: Q4L235
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 2
citation_count: 1
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for AASDH (human)

## Current model (mechanistic narrative)

AASDH (ACSF4-U26) is a β-alanine-activating enzyme that catalyzes an ATP-dependent reaction forming a covalent acyl-enzyme thioester intermediate with β-alanine, with near-absolute substrate specificity for β-alanine among the standard amino acids and a KM of ~5 µM [PMID:24467666]. Catalysis depends on a phosphopantetheine cofactor: a point mutant lacking the phosphopantetheine attachment site fails to form the thioester bond [PMID:24467666]. The β-alanine transfer activity resides in the adenylation domain, since deletion of the C-terminal PQQDH-related domain does not abolish transfer onto thiol acceptors; the physiological function of this C-terminal domain has not been characterized in the available corpus [PMID:24467666]. Beyond this in vitro activation and transfer chemistry, no downstream pathway or in vivo role for AASDH has been established in the available corpus.

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140657 ATP-dependent activity, GO:0016874 ligase activity
- **localization:** *(none)*
- **pathway (Reactome):** *(none)*
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2014 | High | Vertebrate AASDH (ACSF4-U26) is a β-alanine-activating enzyme: purified recombinant mouse ACSF4-U26 formed a covalent thioester bond with β-alanine in an ATP-dependent reaction, with a KM of ~5 µM for β-alanine. A point mutant lacking the phosphopantetheine attachment site failed to form this bond, confirming that the phosphopantetheine cofactor is required for catalysis. Competition experiments showed near-absolute specificity for β-alanine among the 20 standard amino acids. | PMID:24467666 | The FEBS journal |
| 2014 | Medium | The PQQDH-related C-terminal domain of AASDH (ACSF4-U26) is not required for β-alanine transfer onto thiol acceptors (cysteine, cysteamine, DTT), indicating that this transfer activity resides in the adenylation domain rather than the C-terminal domain. However, this thiol-transfer activity was judged physiologically irrelevant based on its non-specific nature. | PMID:24467666 | The FEBS journal |

## Citations

- PMID:24467666
