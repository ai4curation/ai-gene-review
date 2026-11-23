---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACCS
affinage_run_date: 2026-06-09T22:02:38
uniprot_accession: Q96QU6
self_evaluation_pairwise: win
faith_pct: 66.66666666666667
n_discoveries: 1
citation_count: 1
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ACCS (human)

## Current model (mechanistic narrative)

Human ACCS is a pyridoxal-phosphate-dependent enzyme that, despite its annotation as a 1-aminocyclopropane-1-carboxylate synthase homolog, lacks canonical ACC synthase activity and instead catalyzes cysteine conjugate sulfoxide β-lyase activity [PMID:39876065]. Active-site residues required for this β-lyase activity were identified through AlphaFold2-guided mutagenesis combined with in vitro enzymatic assays [PMID:39876065]. Beyond [PMID:39876065], no further mechanistic detail — including cellular localization, physiological substrates, or pathway context — has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0016829 lyase activity
- **localization:** *(none)*
- **pathway (Reactome):** *(none)*
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2025 | Medium | Human ACCS (1-aminocyclopropane-1-carboxylate synthase homolog) possesses cysteine conjugate sulfoxide β-lyase activity, not canonical ACC synthase activity. Structure-function analysis guided by an AlphaFold2 model identified key active-site residues required for this β-lyase activity. | PMID:39876065 | The FEBS journal |

## Citations

- PMID:39876065
