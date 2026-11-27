---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/APOH
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: P02749
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 5
citation_count: 5
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for APOH (human)

## Current model (mechanistic narrative)

APOH (apolipoprotein H / beta-2 glycoprotein I) is a liver-synthesized plasma glycoprotein that links lipid metabolism, hemostasis, and vascular biology [PMID:1582254, PMID:19878946]. It is produced predominantly by hepatocytes, where elevated hepatic synthesis—rather than adipose production—accounts for increased circulating APOH in type 2 diabetics, and its plasma levels track with triglyceride-rich lipoproteins and metabolic syndrome markers [PMID:19878946]. APOH exerts anticoagulant activity by extending thrombin clotting time and suppressing thrombin generation; haplotype-defining missense variants reduce this capacity and lower beta-2-glycoprotein I levels, mechanistically connecting APOH variation to increased thrombin generation and venous thrombosis risk [PMID:25081279]. In antiphospholipid syndrome, APOH packaged within patient-derived exosomes enters endothelial cells and impairs their migration and tube formation, acting through the phospho-ERK pathway and producing APS-like adverse outcomes in a mouse pregnancy model, implicating APOH in impaired vascular development [PMID:34040601].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0008289 lipid binding, GO:0098772 molecular function regulator activity
- **localization:** GO:0005576 extracellular region, GO:0031410 cytoplasmic vesicle
- **pathway (Reactome):** R-HSA-109582 Hemostasis, R-HSA-1430728 Metabolism
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1992 | Medium | APOH (apolipoprotein H / beta-2 glycoprotein I) maps to human chromosome 17q23–qter, and Northern blot analysis of total liver RNA identified a ~1.5 kb transcript, establishing the liver as the major site of APOH biosynthesis. | PMID:1582254 | Cytogenetics and cell genetics |
| 2008 | Low | APOH variants, particularly a nonsynonymous SNP (Cys306Gly) in a region involved in phospholipid binding, are associated with triglyceride and apoE levels, consistent with APOH's role in lipoprotein lipase activation and lipid metabolism. Family-based analyses across three racial groups identified associations with dietary cholesterol transport traits. | PMID:18676959 | Journal of lipid research |
| 2009 | Medium | APOH plasma levels are strongly associated with triglyceride-rich lipoproteins and metabolic syndrome markers in type 2 diabetic patients, and increased APOH in these patients is due to elevated liver synthesis (increased mRNA and protein in liver biopsies), not adipose tissue production (no APOH mRNA or protein detected in adipose tissue). | PMID:19878946 | Atherosclerosis |
| 2014 | Medium | APOH polymorphisms (c.-32C>A, c.422T>C, c.461G>A, c.1004G>C) forming haplotypes H2 and H3 are associated with venous thrombosis risk. H3 individuals have significantly decreased beta-2-glycoprotein I levels, increased thrombin generation, and functional assays showed mutant APOH protein has significantly lower capacity to extend thrombin clotting time and reduce thrombin generation potential, establishing a mechanistic link between APOH variants and thrombosis. | PMID:25081279 | Journal of thrombosis and haemostasis |
| 2021 | Medium | APOH-containing exosomes (APOH-exos) from antiphospholipid syndrome (APS) patients inhibit migration and tube formation of HUVECs in vitro, cause APS-like birth outcomes in a mouse pregnancy model, directly enter HUVECs, and may act through the phospho-ERK pathway, implicating exosomal APOH in impaired vascular development underlying APS pathogenesis. | PMID:34040601 | Frontiers in immunology |

## Citations

- PMID:1582254
- PMID:18676959
- PMID:19878946
- PMID:25081279
- PMID:34040601
