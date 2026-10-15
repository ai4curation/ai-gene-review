---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AXDND1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q5T1B0
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 4
citation_count: 4
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AXDND1 (human)

## Current model (mechanistic narrative)

AXDND1 is a testis-enriched, dynein-related protein essential for spermiogenesis, where it governs the morphological remodeling that converts round spermatids into motile sperm [PMID:34759295, PMID:38997255]. Expressed from mid-pachytene spermatocytes through early spermatids, it localizes to the manchette and is required for the elongation step of spermiogenesis, controlling manchette dynamics and nuclear (head) shaping [PMID:34759295, PMID:35386379]. Beyond differentiated germ cells, AXDND1 maintains the balance between self-renewing and differentiation-committed spermatogonial populations, and its loss drives disproportionate commitment to differentiation, progressive depletion of the seminiferous epithelium, loss of blood-testis barrier integrity, and immune cell infiltration [PMID:38997255]. AXDND1 is also required for flagellar axoneme assembly: its loss produces disorganized axonemes with deficient outer doublet and central-pair microtubules, defective outer dense fibres, ectopic vesicles, spermiation and individualization defects, and abolishes flagellar localization of the axonemal proteins SPAG6 and DNALI1, rendering sperm immotile [PMID:34759295, PMID:38997255, PMID:40457935]. A homozygous frameshift mutation (c.1399_1402del; p.Gln468ArgfsTer2) that abolishes AXDND1 protein establishes it as a causative gene for multiple morphological abnormalities of the sperm flagellum (MMAF) and male sterility in humans [PMID:40457935].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** *(none)*
- **localization:** GO:0005856 cytoskeleton, GO:0005929 cilium
- **pathway (Reactome):** R-HSA-1474165 Reproduction, R-HSA-1266738 Developmental Biology
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2021 | High | AXDND1 localizes to the manchette in spermatids, and its knockout in mice causes head deformation, outer doublet microtubule deficiency in the axoneme, and loss of outer dense fiber (ODF) and mitochondria sheath, establishing that AXDND1 regulates manchette dynamics, spermatid head shaping, and sperm flagellum assembly. | PMID:34759295 | Cell death discovery |
| 2022 | High | AXDND1 protein is expressed from mid-pachytene spermatocytes to early spermatids and is required for the elongation step of spermiogenesis, particularly for normal nuclear shaping and manchette structure. | PMID:35386379 | Reproductive medicine and biology |
| 2024 | High | AXDND1 maintains the balance between self-renewing and differentiation-committed spermatogonial populations; its loss causes disproportionate commitment to differentiation, progressive depletion of the seminiferous epithelium, loss of blood-testis barrier integrity, and immune cell infiltration. Additionally, sperm produced in the absence of AXDND1 are immotile due to abnormal axoneme structure including ectopic vesicles and defects in outer dense fibres and microtubule doublets, a severe spermiation defect, and abnormal sperm individualisation. | PMID:38997255 | Cell death & disease |
| 2025 | Medium | A homozygous frameshift mutation in AXDND1 (c.1399_1402del; p.Gln468ArgfsTer2) abolishes AXDND1 protein expression in sperm and causes disorganized flagellar axoneme with missing central pair microtubules, and loss of SPAG6 and DNALI1 signals from sperm flagella, establishing AXDND1 as essential for flagellar axoneme organization and a causative MMAF gene in humans. | PMID:40457935 | Asian journal of andrology |

## Citations

- PMID:34759295
- PMID:35386379
- PMID:38997255
- PMID:40457935
