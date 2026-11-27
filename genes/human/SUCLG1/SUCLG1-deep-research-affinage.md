---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/SUCLG1
affinage_run_date: 2026-06-10T10:51:54
uniprot_accession: P53597
self_evaluation_pairwise: win
faith_pct: 100.0
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

# Affinage mechanistic annotation for SUCLG1 (human)

## Current model (mechanistic narrative)

SUCLG1 encodes the alpha subunit of the mitochondrial matrix succinate-CoA ligase (SUCL), a heterodimer that catalyzes the reversible conversion of succinyl-CoA to succinate and thereby contributes to mitochondrial substrate-level phosphorylation [PMID:20693550, PMID:30470562]. SUCLG1 is structurally indispensable to the complex: loss of SUCLG1 protein leads to concurrent loss of the partner beta subunits SUCLA2 and SUCLG2, abolished SCS enzyme activity, mtDNA depletion, and respiration defects, all of which are reversed by ectopic wild-type SUCLG1, establishing SUCLG1 as required for SUCL stability and function [PMID:27484306]. Pathogenic SUCLG1 mutations cause this loss of SUCL, impairing mitochondrial substrate-level phosphorylation and producing SUCLG2 mislocalization with increased mitochondrial fragmentation [PMID:30470562]. Beyond its catalytic role, SUCLG1 governs the succinyl-CoA pool to restrict succinylation of mitochondrial RNA polymerase POLRMT at K622; by keeping POLRMT hyposuccinylated it preserves POLRMT engagement with mtDNA and transcription factors, sustaining mtDNA transcription and mitochondrial biogenesis—a circuit exploited by FLT3-mutant leukemia, which upregulates SUCLG1 to drive mitobiogenesis and disease progression [PMID:38649537]. SUCLG1 enzymatic activity is itself subject to acyl-lysine regulation, with hyperbutyrylation at K90 impairing TCA flux and SIRT4 acting as the debutyrylase that restores activity [PMID:41991142]. SUCLG1 supports mitochondrial fusion, mitochondrial quality, and aerobic respiration in proliferating tumor cells [PMID:39749698].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0016874 ligase activity, GO:0140096 catalytic activity, acting on a protein
- **localization:** GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-1430728 Metabolism, R-HSA-74160 Gene expression (Transcription)
- **partners:** SUCLA2, SUCLG2, POLRMT, SIRT4
- **complexes:** succinate-CoA ligase (SUCL)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2010 | Medium | SUCLG1 encodes the alpha subunit of succinate-CoA ligase (SUCL), a heterodimer in the mitochondrial matrix that catalyzes the reversible conversion of succinyl-CoA to succinate; in the absence of SUCLG1 protein, SUCLA2 protein is also absent in fibroblasts (by western blot), consistent with degradation of the beta subunit when its heterodimer partner is missing. | PMID:20693550 | Journal of medical genetics |
| 2018 | Medium | Pathogenic mutation in SUCLG1 (p.Ala209Glu) abolishes SUCLG1 protein, strongly reduces SUCLA2 and SUCLG2 protein levels, impairs mitochondrial substrate-level phosphorylation (mSLP) in fibroblasts, and causes mislocalization of SUCLG2 away from the mitochondrial network along with increased mitochondrial fragmentation, without changes in mtDNA levels or respiratory complex activities when standard substrates are used. | PMID:30470562 | Molecular genetics and metabolism |
| 2016 | High | Loss of SUCLG1 protein in patient fibroblasts leads to significantly reduced SUCLA2 and SUCLG2 protein levels, essentially undetectable SCS enzyme activity, mtDNA depletion, and cellular respiration defects; ectopic expression of wild-type SUCLG1 rescues all these abnormal phenotypes, functionally confirming SUCLG1 as necessary for SUCL complex stability and activity. | PMID:27484306 | Molecular genetics and metabolism |
| 2024 | High | SUCLG1 restricts succinyl-CoA levels to suppress succinylation of mitochondrial RNA polymerase (POLRMT) at lysine 622; this succinylation disrupts POLRMT interaction with mtDNA and mitochondrial transcription factors, while SUCLG1-mediated POLRMT hyposuccinylation maintains mtDNA transcription and mitochondrial biogenesis. FLT3 mutations upregulate SUCLG1 expression to reduce succinyl-CoA and POLRMT succinylation, enhancing mitobiogenesis and leukemia progression. | PMID:38649537 | The EMBO journal |
| 2026 | Medium | SUCLG1 is hyperbutyrylated at lysine K90 in a mouse HFpEF model, which impairs its enzymatic function in the TCA cycle, resulting in reduced succinate and ATP production. SIRT4 acts as a debutyrylase for SUCLG1-K90, and downregulated SIRT4 leads to SUCLG1 hyperbutyrylation; restoration of SIRT4 activity (by ginsenoside Rb3 binding) reverses SUCLG1 hyperbutyrylation and restores TCA cycle flux. | PMID:41991142 | Pharmacological research |
| 2025 | Medium | SUCLG1 promotes mitochondrial quality, mitochondrial fusion, aerobic respiration (without affecting glycolysis), and proliferation/migration of plexiform neurofibroma cells; knockdown reduces these effects, and elevated SUCLG1 upregulates SLC25A1 expression. | PMID:39749698 | International journal of oncology |
| 2017 | Low | In silico and computational analysis predicted that the SUCLG1 p.M14T mutation (located at the mitochondrial targeting sequence) alters protein stability and mitochondrial translocation; mtDNA copy number was reduced in patients' peripheral blood leukocytes. | PMID:29217198 | Biochemical and biophysical research communications |

## Citations

- PMID:20693550
- PMID:27484306
- PMID:29217198
- PMID:30470562
- PMID:38649537
- PMID:39749698
- PMID:41991142
