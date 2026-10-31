---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ATP5ME
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: P56385
self_evaluation_pairwise: win
faith_pct: 75.0
n_discoveries: 7
citation_count: 7
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ATP5ME (human)

## Current model (mechanistic narrative)

ATP5ME (subunit e, ATP5I) is a membrane subunit of the mitochondrial F1F0-ATP synthase that maintains the stability of ATP synthase dimers and is thereby required for proper shaping of mitochondrial cristae [PMID:42138716]. Loss of ATP5ME by CRISPR knockout disrupts ATP synthase oligomerization, causing accumulation of vestigial assembly intermediates, altered mitochondrial morphology, a fall in the NAD+/NADH ratio, and inhibition of oxidative phosphorylation with compensatory glycolysis [PMID:42138716]. ATP5ME is the mechanistic target of the biguanides metformin and phenformin: it binds a biguanide analogue in vitro, its knockout phenocopies biguanide treatment and confers resistance to their antiproliferative effects, reintroduction rescues both metabolic and antiproliferative responses, and genome-wide epistasis profiles for metformin resemble those of the ATP synthase inhibitor oligomycin rather than the complex I inhibitor rotenone [PMID:42138716]. Consistent with a role in mitochondrial energetics, ATP5ME expression modulates cellular oxidative stress and apoptosis: it acts as a downstream effector in a Gm11874/TRESK pathway in spinal cord neurons where elevated ATP5ME drives oxidative stress, DNA damage, and apoptosis [PMID:33973102], whereas in high-glucose-stressed cardiomyocytes its overexpression preserves mitochondrial membrane potential and limits apoptosis and oxidative damage [PMID:38320353].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0005198 structural molecule activity
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-1852241 Organelle biogenesis and maintenance
- **partners:** *(none)*
- **complexes:** F1F0-ATP synthase

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2026 | High | ATP5I (subunit e of F1F0-ATP synthase) maintains the stability of F1F0-ATP synthase dimers, which is crucial for shaping mitochondrial cristae morphology. CRISPR-Cas9 knockout of ATP5I in pancreatic cancer cells phenocopies biguanide treatment: mitochondrial morphology alterations, reduction of NAD+/NADH ratio, inhibition of oxidative phosphorylation (OXPHOS), rescue of respiration by uncouplers, and compensatory increase in glycolysis. Metformin disrupts F1F0-ATP synthase oligomerization and causes accumulation of vestigial assembly intermediates, a phenotype also observed upon ATP5I inactivation. ATP5I KO cells are resistant to antiproliferative effects of biguanides, and reintroduction of ATP5I rescues both metabolic and antiproliferative effects of metformin and phenformin. Genome-wide CRISPR screening showed metformin genetic interaction profiles resemble oligomycin (F1F0-ATP synthase inhibitor), not rotenone (complex I inhibitor), supporting ATP5I as the relevant metformin target. | PMID:42138716 | eLife |
| 2024 | High | ATP5I (subunit e of F1F0-ATP synthase) maintains the stability of F1F0-ATP synthase dimers and shapes cristae morphology; ATP5I interacts with a biguanide analogue in vitro. This is the preprint version of the eLife study (same findings). | PMID:bio_10.1101_2024.09.20.614047 | bioRxiv |
| 2021 | Medium | In cultured spinal cord neurons, TRESK silencing upregulates LncRNA Gm11874, which positively regulates ATP5I expression. Elevated ATP5I promotes oxidative stress (increased MitoSOX, MDA, 8-OHdG), DNA damage (increased γ-H2AX, PARP-1), and apoptosis. Knockdown of ATP5I by siRNA reduced ATP-induced oxidative stress, DNA damage, and apoptosis, establishing ATP5I as a downstream effector in this pathway. | PMID:33973102 | Neurochemical research |
| 2024 | Medium | ATP5me overexpression in high glucose-treated H9C2 cardiomyocyte cells alleviates high glucose-induced decrease in cell proliferation, mitochondrial membrane potential, BCL2 and SOD, and attenuates increase in apoptosis, MDA, ROS, cleaved-caspase-3, and BAX. ATP5me is under-expressed in type 1 GDM offspring hearts and in high-glucose-treated H9C2 cells, indicating a protective role of ATP5me in maintaining mitochondrial integrity and reducing oxidative stress in cardiomyocytes. | PMID:38320353 | International immunopharmacology |
| 2023 | Medium | A novel MFSD7-ATP5I gene fusion transcript, detected in 58% of sarcoma samples, promotes cell migration and invasion. Knockdown of MFSD7-ATP5I significantly reduced migration and invasion, while overexpression increased them. A phosphokinase assay demonstrated that the MFSD7-ATP5I fusion activates the GSK-3 pathway. | PMID:37782287 | Journal of orthopaedic research |
| 2021 | Low | ATP5I/L (components of mitochondrial F1F0-ATP synthase) were specifically downregulated in the kidney cortex of low-birth-weight rats at four weeks, as identified by untargeted quantitative proteomics and validated by immunohistology, suggesting ATP5I is a component of the mitochondrial respiratory chain whose reduced expression marks early LBW nephropathy. | PMID:34638634 | International journal of molecular sciences |
| 2025 | Low | In kidney transplant candidates undergoing resistance-based muscle therapy, ATP5I immunohistology score in muscle biopsies increased significantly (mean difference 0.74, p<0.001) after one year of intervention, correlating with improved mitochondrial oxidative function alongside improved physical performance metrics. | PMID:40201398 | Kidney medicine |

## Citations

- PMID:33973102
- PMID:34638634
- PMID:37782287
- PMID:38320353
- PMID:40201398
- PMID:42138716
- PMID:bio_10.1101_2024.09.20.614047
