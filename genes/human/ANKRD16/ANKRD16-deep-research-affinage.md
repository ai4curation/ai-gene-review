---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKRD16
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q6P6B7
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

# Affinage mechanistic annotation for ANKRD16 (human)

## Current model (mechanistic narrative)

ANKRD16 is a vertebrate ankyrin-repeat protein that functions as a proofreading safeguard against translational errors arising from defective alanyl-tRNA synthetase (AlaRS) editing [PMID:29769718]. It binds directly to the catalytic domain of AlaRS and, through its lysine side chains, captures serine that has been misactivated by AlaRS, thereby preventing serine from being charged onto tRNA-Ala and subsequently misincorporated into nascent peptides [PMID:29769718]. Genetically, ANKRD16 acts as a downstream suppressor of the neurodegeneration caused by editing-defective AlaRS: deletion of Ankrd16 in the brains of Aars^sti/sti mice produces widespread protein aggregation and neuron loss [PMID:29769718]. Beyond this serine-capture role at the AlaRS catalytic site, no further mechanistic detail has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140313 molecular sequestering activity, GO:0098772 molecular function regulator activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins
- **partners:** AARS
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2018 | High | ANKRD16 binds directly to the catalytic domain of AlaRS (alanyl-tRNA synthetase), and serine misactivated by AlaRS is captured by the lysine side chains of ANKRD16, thereby preventing charging of serine adenylates to tRNAAla and precluding serine misincorporation in nascent peptides. | PMID:29769718 | Nature |
| 2018 | High | ANKRD16 acts epistatically with the Aars^sti mutation: deletion of Ankrd16 in brains of Aars^sti/sti mice causes widespread protein aggregation and neuron loss, establishing ANKRD16 as a downstream suppressor of neurodegeneration caused by editing-defective AlaRS. | PMID:29769718 | Nature |

## Citations

- PMID:29769718
