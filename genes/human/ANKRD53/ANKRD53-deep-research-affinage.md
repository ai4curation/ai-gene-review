---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKRD53
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q8N9V6
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 6
citation_count: 2
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANKRD53 (human)

## Current model (mechanistic narrative)

ANKRD53 is an ankyrin repeat scaffold protein with distinct roles in mitotic spindle regulation and adipocyte lipid metabolism [PMID:26820536, PMID:41654016]. In mitosis, it was identified as a DDA3-interacting protein that is recruited to the mitotic spindle by DDA3 [PMID:26820536], where it functionally antagonizes DDA3 to control spindle microtubule polymerization [PMID:26820536]; its depletion delays mitotic progression, produces unaligned chromosomes, reduces spindle MT polymerization, activates the spindle assembly checkpoint, and causes bi-nucleate and polylobed nuclei, indicating a requirement for proper chromosome alignment and cytokinesis [PMID:26820536]. In adipocytes, ANKRD53 binds ACSL1 and promotes its mitochondrial localization, thereby channeling lipolysis-derived free fatty acids into β-oxidation; loss of ACSL1 abolishes ANKRD53's metabolic effects [PMID:41654016], and ANKRD53 levels bidirectionally regulate forskolin-stimulated lipolysis and mitochondrial respiration in human primary adipocytes and in mouse adipose tissue [PMID:41654016]. Beyond these two contexts, no further mechanistic detail has been characterized in the available corpus.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0008092 cytoskeletal protein binding
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-1640170 Cell Cycle, R-HSA-1430728 Metabolism
- **partners:** DDA3, ACSL1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2016 | Medium | ANKRD53 was identified as a novel DDA3-interacting protein through proteomic analysis, and is recruited to the mitotic spindle by DDA3. | PMID:26820536 | Biochemical and biophysical research communications |
| 2016 | Low | ANKRD53 is phosphorylated by mitotic kinases during mitosis, as indicated by expression profile analysis during mitotic progression. | PMID:26820536 | Biochemical and biophysical research communications |
| 2016 | Medium | Depletion of ANKRD53 in HeLa cells delayed mitotic progression, increased unaligned chromosomes, decreased spindle MT polymerization, activated the spindle assembly checkpoint (SAC), and increased bi-nuclei and polylobed nuclei, establishing a role in spindle dynamics and cytokinesis. | PMID:26820536 | Biochemical and biophysical research communications |
| 2016 | Medium | Although ANKRD53 is recruited to the mitotic spindle by DDA3, it counteracts DDA3 activity for spindle MT polymerization, placing ANKRD53 as a functional antagonist of DDA3 in this pathway. | PMID:26820536 | Biochemical and biophysical research communications |
| 2026 | Medium | ANKRD53 overexpression enhanced forskolin-stimulated lipolysis and mitochondrial respiration in human primary adipocytes, while silencing impaired these processes; adipose-targeted overexpression in mice increased lipolysis in vivo. | PMID:41654016 | Molecular metabolism |
| 2026 | Medium | ANKRD53 interacts with ACSL1 (identified by immunoprecipitation-mass spectrometry) and promotes ACSL1 mitochondrial localization, thereby channeling lipolysis-derived free fatty acids into β-oxidation; silencing ACSL1 abrogated ANKRD53's metabolic effects. | PMID:41654016 | Molecular metabolism |

## Citations

- PMID:26820536
- PMID:41654016
