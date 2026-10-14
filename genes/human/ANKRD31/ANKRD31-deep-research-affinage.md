---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKRD31
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q8N7Z5
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 10
citation_count: 9
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANKRD31 (human)

## Current model (mechanistic narrative)

ANKRD31 is a meiotic scaffold protein that assembles with DSB-promoting factors on chromosome axes to control the number, timing, and genomic distribution of programmed meiotic DNA double-strand breaks (DSBs) [PMID:31003867, PMID:31000436]. Loss of ANKRD31 dysregulates DSBs genome-wide — delaying recombination initiation, reducing selectivity for hotspots, and paradoxically increasing total DSBs — while abolishing the specialized PAR-axis domain that normally makes the pseudoautosomal regions of the sex chromosomes the hottest DSB segment in the male genome [PMID:31003867, PMID:31000436, PMID:32461690]. Mechanistically, ANKRD31 binds directly to the pleckstrin homology (PH) domain of REC114, anchoring REC114 and associated DSB machinery to the PAR and to axis sites in vivo; this same REC114 PH surface is engaged competitively by IHO1 and TOPOVIBL, casting REC114 as a regulatory platform for mutually exclusive partner binding [PMID:31003867, PMID:37431931]. The ANKRD31–REC114 interaction is functionally central: complete disruption phenocopies the null (delayed DSBs, repair defects, loss of PAR targeting), whereas partial disruption only delays DSB timing, defining a dosage-dependent requirement [PMID:37976262]. ANKRD31 acts in a complementary, partially redundant route to the IHO1–HORMAD1 axis-seeding pathway, enhancing the seeding and growth of DSB-machinery clusters on axes [PMID:38580643]. Heterozygous ANKRD31 variants cause premature ovarian insufficiency through haploinsufficiency by disrupting the ANKRD31–REC114 interaction [PMID:34257419]. Beyond meiosis, ANKRD31 also interacts with epithelial cell-cell junction proteins in the epididymis, where its loss disrupts the blood-epididymal barrier and causes infertility [PMID:34820371].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-1474165 Reproduction, R-HSA-73894 DNA Repair
- **partners:** REC114, IHO1, MEI4, MEI1, TOPOVIBL
- **complexes:** meiotic DSB-promoting complex (REC114-MEI4-IHO1)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2019 | High | ANKRD31 controls number, timing, and location of meiotic DNA double-strand breaks (DSBs). Spermatocytes lacking ANKRD31 have altered DSB locations, fail to target DSBs to the pseudoautosomal regions (PARs) of sex chromosomes, and show delayed and/or fewer recombination sites but paradoxically more DSBs overall, indicating DSB dysregulation. | PMID:31003867, PMID:31000436 | Molecular cell |
| 2019 | High | A crystal structure reveals that REC114 contains a pleckstrin homology (PH) domain that directly contacts ANKRD31 through intermolecular interactions. ANKRD31 stabilizes REC114 association with the PAR and elsewhere in vivo, functioning as a scaffold that anchors REC114 and other DSB-promoting factors to specific genomic locations. | PMID:31003867 | Molecular cell |
| 2019 | High | ANKRD31 is a key component of complexes of DSB-promoting proteins that assemble on meiotic chromosome axes. ANKRD31 deficiency causes genome-wide delayed recombination initiation, reduced selectivity for DSB hotspot sites, and loss of a specialized PAR-axis domain highly enriched for DSB-promoting proteins. | PMID:31000436 | Molecular cell |
| 2020 | High | MEI4 and ANKRD31 proteins are required for the hyperaccumulation of DSB-promoting factors in the PAR, elongation of PAR chromosome axes, and separation of sister chromatids prior to DSB formation — processes linked to heterochromatic mo-2 minisatellite arrays. These events make the PAR the hottest DSB segment in the male mouse genome. | PMID:32461690 | Nature |
| 2021 | Medium | ANKRD31 physically interacts with epithelial cell-cell junction proteins in the epididymis. Loss of ANKRD31 in knockout male mice disrupts the blood-epididymal barrier (BEB) due to cell-to-cell junction anomalies, resulting in oligo-astheno-teratozoospermia and infertility. | PMID:34820371 | Frontiers in cell and developmental biology |
| 2021 | Medium | Pathogenic heterozygous variants in ANKRD31 identified in premature ovarian insufficiency (POI) patients disrupt the interaction between ANKRD31 and the DSB-formation factor REC114, exerting their pathogenic effect via haploinsufficiency, indicating dosage-dependent control of ovarian function. | PMID:34257419 | Genetics in medicine |
| 2023 | High | The REC114 PH domain interacts with ANKRD31 and with IHO1 and TOPOVIBL at the same surface, indicating mutually exclusive interactions. REC114 acts as a regulatory platform where ANKRD31 competes with other partners for binding. | PMID:37431931 | The EMBO journal |
| 2023 | High | Complete disruption of the ANKRD31-REC114 interaction (by C-terminal truncation of ANKRD31) mimics the Ankrd31 null phenotype: delayed global DSB formation, defects in DSB repair, and failure to target DSBs to the PARs. Substantial but incomplete disruption (missense mutation) delays DSB formation but leaves recombination, repair, and DSB locations near normal. A dosage effect was observed when combining partial-loss and null alleles. | PMID:37976262 | Proceedings of the National Academy of Sciences of the United States of America |
| 2024 | High | When the IHO1-HORMAD1 axis-seeding pathway is disrupted, residual meiotic DSBs become dependent on ANKRD31, which enhances both the seeding and growth of DSB-machinery clusters on chromosome axes, demonstrating that ANKRD31 and the IHO1-HORMAD1 pathway act in complementary, partially redundant routes for DSB-machinery condensation. | PMID:38580643 | Nature communications |
| 2023 | Medium | MEI1 variants identified in non-obstructive azoospermia patients disrupt MEI1 interactions with ANKRD31 (as well as IHO1, REC114, and MEI4) as detected by co-immunoprecipitation, consistent with ANKRD31 being a component of the MEI1-containing DSB-promoting complex. | PMID:41706353 | Journal of assisted reproduction and genetics |

## Citations

- PMID:31000436
- PMID:31003867
- PMID:32461690
- PMID:34257419
- PMID:34820371
- PMID:37431931
- PMID:37976262
- PMID:38580643
- PMID:41706353
