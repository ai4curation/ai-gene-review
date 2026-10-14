---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AVPI1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q5T686
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

# Affinage mechanistic annotation for AVPI1 (human)

## Current model (mechanistic narrative)

AVPI1 (VIP32) is a small vasopressin-induced protein implicated in two distinct cellular processes downstream of vasopressin signaling: cell cycle G-to-M transition and regulation of epithelial sodium transport [PMID:12356727]. When expressed in Xenopus oocytes, AVPI1 induces meiotic maturation through activation of the maturation promoting factor (Cdc2/cyclin), placing it as an inducer of the G-to-M transition [PMID:12356727]. In the same heterologous system, AVPI1 selectively downregulates epithelial sodium channel (ENaC) activity without altering channel cell surface expression, indicating that it inhibits sodium conductance through a mechanism independent of channel trafficking [PMID:12356727]. Beyond these functional readouts in the Xenopus oocyte system, no biochemical mechanism, direct binding partner, or structural detail for AVPI1 has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-1640170 Cell Cycle, R-HSA-382551 Transport of small molecules
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2002 | Medium | VIP32 (AVPI1), a vasopressin-induced protein of 142 amino acids, when expressed in Xenopus oocytes induces meiotic maturation through activation of the maturation promoting factor (Cdc2/cyclin), indicating a role in G to M phase transition. | PMID:12356727 | The EMBO journal |
| 2002 | Medium | VIP32 (AVPI1) selectively downregulates ENaC (epithelial sodium channel) activity when co-expressed in Xenopus oocytes, without affecting channel cell surface expression, suggesting a functional inhibitory role on sodium transport independent of trafficking. | PMID:12356727 | The EMBO journal |

## Citations

- PMID:12356727
