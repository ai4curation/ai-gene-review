---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ABHD10
affinage_run_date: 2026-06-09T22:02:37
uniprot_accession: Q9NUJ1
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 8
citation_count: 8
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ABHD10 (human)

## Current model (mechanistic narrative)

ABHD10 is a serine hydrolase that operates as a protein S-depalmitoylase in the mitochondrial matrix, controlling mitochondrial redox homeostasis and lipid-related function across multiple tissues [PMID:31740833, PMID:41285782]. Its catalytic mechanism rests on a serine nucleophile, established by covalent serine-directed inhibitors and activity-based protein profiling that classify it as an active serine hydrolase [PMID:22400490]. In its depalmitoylase role, ABHD10 removes palmitoyl groups from peroxiredoxin-5 (PRDX5) at the active-site cysteine (Cys100), thereby preserving PRDX5 antioxidant capacity and limiting mitochondrial oxidative stress [PMID:31740833, PMID:37400491]. In testis, ABHD10 is a mitochondrial matrix depalmitoylase essential for sperm mitochondrial sheath formation and male fertility, acting on substrates including SPATA19, GK2, PDHX, NDUFV1, and SDHB, with direct physical interactions demonstrated for SPATA19, GK2, and PDHX [PMID:41285782]. Beyond its depalmitoylase activity, ABHD10 also functions in human liver as an acyl-glucuronide hydrolase, deglucuronidating mycophenolic acid acyl-glucuronide and probenecid acyl-glucuronide [PMID:22294686, PMID:25217485]. ABHD10 expression is transcriptionally repressed by ELK-3 downstream of TGFβ1/EGF signaling, linking signaling-driven loss of ABHD10 to increased PRDX5 palmitoylation and hepatocyte oxidative damage [PMID:37400491].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016787 hydrolase activity
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-8953897 Cellular responses to stimuli
- **partners:** PRDX5, SPATA19, GK2, PDHX, KCMF1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2019 | High | ABHD10 is a resident mitochondrial S-depalmitoylase that removes palmitoyl groups from peroxiredoxin-5 (PRDX5) at its nucleophilic active site cysteine residue, directly regulating PRDX5 antioxidant capacity and mitochondrial redox homeostasis. | PMID:31740833 | Nature chemical biology |
| 2012 | High | ABHD10 is the enzyme responsible for deglucuronidation (hydrolysis) of mycophenolic acid acyl-glucuronide (AcMPAG) in human liver; purified from human liver cytosol by column chromatography, confirmed by amino acid sequence analysis, and recombinant ABHD10 expressed in Sf9 cells demonstrated this activity with Km of ~100.7 µM. Activity was inhibited by PMSF, AgNO3, CdCl2, CuCl2, bis-p-nitrophenylphosphate, and DTNB, consistent with a serine hydrolase mechanism. | PMID:22294686 | The Journal of biological chemistry |
| 2014 | Medium | ABHD10 substantially catalyzes deglucuronidation of probenecid acyl glucuronide (PRAG) in human liver, whereas carboxylesterases do not; recombinant ABHD10 showed activity matching inhibition profiles of human liver homogenates, and ABHD10 suppresses net PRAG formation from probenecid via multiple UGT enzymes (UGT1A1, UGT1A9, UGT2B7). | PMID:25217485 | Drug metabolism and disposition: the biological fate of chemicals |
| 2012 | Medium | ABHD10 is a serine hydrolase; activity-based protein profiling (ABPP) identified it as a serine hydrolase target, and the aza-β-lactam ABL303 potently and selectively inactivated ABHD10 (IC50 ≈ 30 nM) in vitro and in living cells via covalent acylation of the enzyme's serine nucleophile. | PMID:22400490 | Journal of the American Chemical Society |
| 2023 | Medium | The transcription factor ELK-3 directly binds to the ABHD10 promoter to inhibit its transactivation; TGFβ1 and EGF signaling induce ABHD10 downregulation via ELK-3, leading to enhanced S-palmitoylation of PRDX5 Cys100, increased oxidative stress, and disrupted hepatocyte function. Ectopic Abhd10 overexpression ameliorated liver damage in ALD model mice. | PMID:37400491 | Communications biology |
| 2025 | High | ABHD10 is a mitochondrial matrix S-depalmitoylase specifically expressed in testis that is essential for sperm mitochondrial sheath formation and male fertility; ABHD10 deficiency causes hyper-palmitoylation of SPATA19, GK2, PDHX, NDUFV1, and SDHB, and ABHD10 physically interacts with SPATA19, GK2, and PDHX as identified by co-immunoprecipitation and proximity labeling. | PMID:41285782 | Nature communications |
| 2026 | Medium | ABHD10 interacts with KCMF1 as shown by co-immunoprecipitation, forming a complex that may regulate mitochondrial lipid metabolism; silencing ABHD10 in senescent cochlear cells reduced P21 and P16 levels, decreased ROS, improved mitochondrial membrane potential, and lowered lipid droplet formation and triglyceride/fatty acid levels. | PMID:42206676 | Journal of cellular physiology |
| 2014 | Low | A rocaglate-derived β-lactone inhibited serine hydrolase activity of ABHD10 both in vitro and in intact PC3 cells, as determined by activity-based protein profiling, confirming ABHD10 is an active serine hydrolase. | PMID:24447064 | Journal of the American Chemical Society |

## Citations

- PMID:22294686
- PMID:22400490
- PMID:24447064
- PMID:25217485
- PMID:31740833
- PMID:37400491
- PMID:41285782
- PMID:42206676
