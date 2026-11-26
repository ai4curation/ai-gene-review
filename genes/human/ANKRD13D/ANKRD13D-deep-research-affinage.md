---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKRD13D
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q6ZTN6
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 2
citation_count: 1
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANKRD13D (human)

## Current model (mechanistic narrative)

ANKRD13D is a ubiquitin-interacting motif (UIM)-containing scaffold protein that operates in the endocytic sorting of ligand-activated EGFR [PMID:31985874]. Its UIMs recognize Lys-63-linked ubiquitin chains on activated EGFR and mediate assembly of a transient ANKRD13D/RNF11/EGFR complex during early receptor endocytosis [PMID:31985874]. The same UIMs are required for the in vivo interaction with the E3 ligase RNF11, which occurs through an atypical binding mode that does not depend on ubiquitin modification of RNF11 itself [PMID:31985874]. Within this pathway, the ubiquitination state of ANKRD13 family members is set by ITCH and RNF11, which in turn tunes their ability to engage activated EGFR [PMID:31985874]. Beyond this scaffolding role in EGFR endocytosis, no further mechanistic detail for ANKRD13D has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport
- **partners:** RNF11, EGFR, ITCH
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2020 | Medium | ANKRD13D forms a complex with RNF11 (RING finger protein 11) in vivo, and the ubiquitin-interacting motifs (UIMs) of ANKRD13D are required for this complex formation; notably, ubiquitin modification of RNF11 is not required for the interaction with ANKRD13 family members (atypical UIM binding mode). | PMID:31985874 | The FEBS journal |
| 2020 | Medium | ANKRD13D (along with ANKRD13A and ANKRD13B) acts as a molecular scaffold in the endocytic pathway: its UIMs recognize Lys-63-linked ubiquitin chains on ligand-activated EGFR, and the ANKRD13/RNF11/EGFR complex is transiently assembled during early receptor endocytosis; loss of ITCH or RNF11 respectively abrogates or increases ubiquitination of ANKRD13A, altering its ability to bind activated EGFR. | PMID:31985874 | The FEBS journal |

## Citations

- PMID:31985874
