---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/PFAS
affinage_run_date: 2026-06-10T05:19:53
uniprot_accession: O15067
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 5
citation_count: 4
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for PFAS (human)

## Current model (mechanistic narrative)

PFAS (phosphoribosylformylglycinamidine synthase) is the enzyme catalyzing the fourth step of de novo purine (IMP) synthesis, converting FGAR to FGAM and thereby supplying nucleotide building blocks for RNA and DNA synthesis during cell growth [PMID:10548741]. Its catalytic identity in human cells was established by complementation of purine-auxotrophic CHO mutant cells with the human gene [PMID:10548741]. PFAS activity is acutely controlled by RAS-ERK signaling: ERK2, but not ERK1, directly phosphorylates PFAS at threonine 619, boosting de novo purine synthesis flux, and a nonphosphorylatable T619A mutant reduces purine synthesis, impairs RAS-dependent colony formation, and slows tumor growth — establishing this modification as functionally required for anabolic proliferation downstream of oncogenic RAS-ERK signaling [PMID:32485148]. PFAS expression is additionally tuned post-transcriptionally, with NSUN2-deposited m5C methylation on PFAS mRNA read by ALYREF to stabilize the transcript and raise PFAS protein levels, fueling purine biosynthesis in retinoblastoma oncogenesis [PMID:37228185]. Beyond its metabolic role, cellular PFAS is hijacked by gammaherpesvirus vFGARAT tegument proteins, which oligomerize with PFAS to deamidate RIG-I and suppress inflammatory cytokine production [PMID:26256000].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0016874 ligase activity, GO:0140096 catalytic activity, acting on a protein
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-162582 Signal Transduction
- **partners:** MAPK1, NSUN2, ALYREF, RIGI
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2020 | High | ERK2 (but not ERK1) directly phosphorylates PFAS (phosphoribosylformylglycinamidine synthase) at threonine 619 (T619) in cells, stimulating de novo purine synthesis flux and increasing building block availability for RNA and DNA synthesis required for cell growth and proliferation. | PMID:32485148 | Molecular cell |
| 2020 | High | Expression of nonphosphorylatable PFAS T619A decreases de novo purine synthesis, impairs RAS-dependent cancer cell colony formation, and reduces tumor growth, establishing that ERK2-mediated T619 phosphorylation of PFAS is functionally required for anabolic cell growth downstream of oncogenic RAS-ERK signaling. | PMID:32485148 | Molecular cell |
| 2023 | High | NSUN2-mediated m5C RNA methylation of PFAS mRNA is recognized by the m5C reader protein ALYREF, which enhances PFAS mRNA stability and increases PFAS protein expression, thereby fueling purine biosynthesis during retinoblastoma oncogenesis. Reintroduction of PFAS rescued the inhibitory phenotype caused by NSUN2 knockdown, confirming PFAS as a functional downstream target of the NSUN2/ALYREF axis. | PMID:37228185 | Clinical and translational medicine |
| 1999 | High | The human FGARAT (PFAS) gene encodes the enzyme catalyzing the fourth step of de novo IMP (inosine monophosphate) synthesis; a genomic P1 clone containing the intact human gene corrected both the enzymatic activity deficiency and purine auxotrophy of Chinese hamster ovary (CHO) AdeB mutant cells, functionally validating the human PFAS/FGARAT gene product. | PMID:10548741 | Gene |
| 2015 | Medium | Gammaherpesvirus tegument proteins carrying sequence homology to the cellular PFAS (FGARAT) enzyme oligomerize with cellular PFAS to deamidate RIG-I, thereby repressing inflammatory cytokine production. These viral FGARAT-homology proteins (vFGARATs) themselves lack enzymatic activity but exploit the cellular PFAS interaction to disarm host innate immunity. | PMID:26256000 | Current opinion in virology |

## Citations

- PMID:10548741
- PMID:26256000
- PMID:32485148
- PMID:37228185
