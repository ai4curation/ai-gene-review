---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARHGEF16
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q5VV41
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 6
citation_count: 6
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARHGEF16 (human)

## Current model (mechanistic narrative)

ARHGEF16 is a Rho-family guanine nucleotide exchange factor that couples receptor and signaling inputs to actin-dependent processes including apoptotic cell clearance and tumor cell migration and proliferation [PMID:21139582, PMID:30305138]. Its core biochemical activity is direct guanine nucleotide exchange on Cdc42, demonstrated by in vitro kinetic analysis of recombinant protein; this GEF activity is enhanced by Tip-1, to which ARHGEF16 binds through its carboxyl-terminal PDZ-binding motif, and by HPV16 E6, with Cdc42 co-immunoprecipitating with ARHGEF16 in the presence of E6 [PMID:21139582]. In efferocytosis, ARHGEF16 acts together with Elmo1 in a RhoG-dependent, Dock1-independent manner to drive engulfment of apoptotic cells, with engulfment lost in the absence of Elmo1 [PMID:25063526]. ARHGEF16 is a transcriptional target of GLI2, which binds its promoter to place it downstream of Hedgehog signaling; in this context ARHGEF16 promotes glioma migration and proliferation through interaction with the cytoskeleton-associated protein CKAP5 [PMID:30305138]. The non-receptor tyrosine kinase FYN binds ARHGEF16 and is required for its pro-proliferative and migratory functions in colon cancer, with FYN knockdown reducing ARHGEF16 protein levels and abolishing its effects [PMID:32811808].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0098772 molecular function regulator activity
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-162582 Signal Transduction
- **partners:** TAX1BP3, ELMO1, CKAP5, FYN, CDC42
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2010 | High | ARHGEF16 directly activates Cdc42: in vitro kinetic analysis of recombinant ARHGEF16 confirmed guanine nucleotide exchange factor (GEF) activity toward Cdc42, and this activity was enhanced by addition of recombinant Tip-1 and HPV16 E6. ARHGEF16 was also shown to interact with Tip-1 via its carboxyl PDZ binding motif, and Cdc42 was co-immunoprecipitated by ARHGEF16 in the presence of HPV16 E6. | PMID:21139582 | British journal of cancer |
| 2014 | Medium | ARHGEF16 (Arhgef16) interacts with Elmo1 and functions synergistically with Elmo1 to promote clearance of apoptotic cells (efferocytosis). This process is dependent on RhoG but independent of Dock1, and requires Elmo1 — engulfment activity is abrogated in the absence of Elmo1. | PMID:25063526 | Biochimica et biophysica acta |
| 2018 | Medium | GLI2 transcriptionally activates ARHGEF16 by directly binding to its promoter, placing ARHGEF16 downstream of Hedgehog/GLI2 signaling. ARHGEF16 overexpression promotes glioma cell migration and proliferation, and ARHGEF16 interacts with cytoskeleton-associated protein 5 (CKAP5), which is required for ARHGEF16's stimulatory effects on migration and proliferation. | PMID:30305138 | Journal of experimental & clinical cancer research : CR |
| 2020 | Medium | FYN, a non-receptor tyrosine kinase, is a binding partner of ARHGEF16. FYN is required for ARHGEF16-induced proliferation and migration in colon cancer cells; knockdown of FYN decreased ARHGEF16 protein levels and abolished ARHGEF16-induced proliferation and migration. | PMID:32811808 | Cell death & disease |
| 2009 | Low | ARHGEF16 (Rho guanidine exchange factor 16) overexpression is sufficient to transform NIH3T3 cells (focus formation assay), consistent with its activity as an oncogenic GEF, and this transformation can be suppressed by ROCK inhibitor analogues. | PMID:19707205 | British journal of cancer |
| 2011 | Low | A single missense mutation disrupting the conserved PDZ binding domain of ARHGEF16 was identified in one oligodendroglioma sample, but no common somatic mutations or deletions in ARHGEF16 were found across a larger oligodendroglioma cohort, indicating that PDZ domain integrity may be functionally relevant but that ARHGEF16 is not a common driver in this tumor type. | PMID:21760942 | PloS one |

## Citations

- PMID:19707205
- PMID:21139582
- PMID:21760942
- PMID:25063526
- PMID:30305138
- PMID:32811808
