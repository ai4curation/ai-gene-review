---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AGFG2
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: O95081
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 4
citation_count: 4
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for AGFG2 (human)

## Current model (mechanistic narrative)

AGFG2 (HRBL) is a nucleoporin-related adaptor protein that links the endocytic machinery to nucleocytoplasmic transport and functions as a cellular co-factor in HIV-1 biology [PMID:10613896, PMID:26701340]. In the cytoplasm it binds the EH-domain proteins Eps15 and Eps15R, and this interaction is required for the synergistic enhancement of HIV-1 Rev-mediated nuclear export of viral RNAs, coupling endocytic adaptor proteins to the Rev export pathway [PMID:10613896]. AGFG2 also acts at the plasma membrane and early endosomes to promote HIV-1-mediated CD4 downregulation: its knockdown raises CD4 surface levels in infected T cells [PMID:25496667], and pathway dissection establishes that AGFG2 serves as a co-factor for both Nef- and Vpu-mediated CD4 downregulation, distinguishing it from the paralog AGFG1/HRB, which supports only the Nef-dependent route [PMID:26701340]. Beyond its role as an EH-protein-binding adaptor in these HIV-1 co-factor activities, no further enzymatic or structural mechanism for AGFG2 has been characterized in the available corpus.

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** GO:0005829 cytosol, GO:0005886 plasma membrane, GO:0005768 endosome
- **pathway (Reactome):** R-HSA-1643685 Disease
- **partners:** EPS15, EPS15R
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1999 | Medium | AGFG2 (Hrbl) binds to EH (Eps15 homology) domain-containing proteins Eps15 and Eps15R in the cytoplasm; this EH-mediated interaction is required for synergistic enhancement of HIV-1 Rev-mediated nuclear export of RNAs, connecting the endocytic machinery to the nucleocytoplasmic transport (Rev export) pathway. | PMID:10613896 | The Journal of cell biology |
| 2014 | Medium | Knockdown of AGFG2 (HRBL) by shRNA significantly increases CD4 surface levels in HIV-1-infected T cells, identifying AGFG2 as a cellular co-factor for HIV-1-mediated CD4 downregulation at the level of the plasma membrane and early endosomes. | PMID:25496667 | Retrovirology |
| 2015 | Medium | AGFG2 (HRBL) knockdown increases CD4 surface levels specifically in HIV-1 Vpu-expressing cells but not in Nef-expressing cells, distinguishing AGFG2's role from the related protein HRB (AGFG1), which acts as a co-factor for Nef-mediated (but not Vpu-mediated) CD4 downregulation. This identifies AGFG2 as a co-factor for both HIV-1 Nef- and Vpu-mediated CD4 downregulation. | PMID:26701340 | The Journal of general virology |
| 2011 | Low | AGFG2 molecules are present in mammals only and emerged later in evolution, likely from a duplication of AGFG1. AGFG2 contains an additional module of ~50 coding nucleotides ahead of the conserved core module (which encodes nucleoporin-related Arf-GAP domain and FG repeats), and this additional module is less conserved than the core (54% vs 67% identity from Drosophila to primates for AGFG1). | PMID:21284487 | Immunopharmacology and immunotoxicology |

## Citations

- PMID:10613896
- PMID:21284487
- PMID:25496667
- PMID:26701340
