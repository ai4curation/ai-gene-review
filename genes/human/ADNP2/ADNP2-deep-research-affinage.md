---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADNP2
affinage_run_date: 2026-06-09T22:02:42
uniprot_accession: Q6IQ32
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 6
citation_count: 6
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ADNP2 (human)

## Current model (mechanistic narrative)

ADNP2 is a chromatin-associated transcriptional repressor that governs retrotransposon silencing and developmental gene programs [PMID:38960717, PMID:41822989]. It serves as the defining subunit of the ChAHP2 complex, a paralog of ADNP-containing ChAHP in which ADNP2 substitutes for ADNP alongside CHD4 and HP1β; this complex is targeted predominantly to endogenous retroviruses and LINE elements through HP1β-mediated recognition of H3K9me3, and its loss de-represses these elements in a manner that is synthetically worsened by concurrent ADNP depletion, establishing complementary control by the two complexes [PMID:38960717]. Beyond retrotransposon control, ADNP2 acts as a direct transcriptional repressor of BMP-pathway ventralizing homeobox genes (ved/vent/vox), occupying these loci to exclude their expression from dorsal territories and thereby promoting neural induction upstream of BMP signaling [PMID:41822989]. ADNP2 also physically interacts with the Brg1 chromatin remodeler and is required for erythroid maturation, where its depletion blocks differentiation in zebrafish and mouse erythroleukemia cells and is rescued by exogenous ADNP2 [PMID:23071114]. Consistent with broad neurodevelopmental roles, loss of ADNP2 in zebrafish reduces pan-neuronal and neuronal fiber markers and alters expression programs spanning synaptic transmission, autophagy, and microtubule dynamics [PMID:39273418], and ADNP2 contributes to cellular survival under oxidative stress [PMID:18179478].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140110 transcription regulator activity, GO:0003677 DNA binding
- **localization:** GO:0005634 nucleus, GO:0005694 chromosome
- **pathway (Reactome):** R-HSA-74160 Gene expression (Transcription), R-HSA-4839726 Chromatin organization, R-HSA-1266738 Developmental Biology
- **partners:** CHD4, CBX1, BRG1, ADNP
- **complexes:** ChAHP2

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2024 | High | ADNP2 is a component of the ChAHP2 complex, which is homologous to ChAHP (ADNP-CHD4-HP1). In ChAHP2, ADNP2 replaces ADNP. ChAHP2 is predominantly targeted to endogenous retroviruses (ERVs) and long interspersed elements (LINEs) via HP1β-mediated binding of H3K9 trimethylated histones. Genetic ablation of ADNP2 alleviates ERV and LINE1 repression, which is synthetically exacerbated by additional depletion of ADNP, demonstrating complementary retrotransposon control by ChAHP and ChAHP2. | PMID:38960717 | Genes & development |
| 2012 | High | ADNP2 interacts with Brg1, an ADNP-interacting chromatin-remodeling protein involved in erythropoiesis through regulation of the globin locus. Knockdown of ADNP2 in zebrafish embryos and mouse erythroleukemia (MEL) cells inhibited erythroid maturation, and exogenous ADNP2 RNA rescued the undifferentiated state. ADNP (but not explicitly ADNP2) was recruited to the mouse β-globin locus control region by chromatin immunoprecipitation. | PMID:23071114 | The Journal of biological chemistry |
| 2026 | High | Zebrafish ADNP2 orthologs (adnp2a and adnp2b) are required for neural induction during gastrulation. ADNP2 functions as a transcriptional repressor that directly occupies and suppresses BMP-related ved/vent/vox homeobox genes, thereby excluding their expression from dorsal territories including the dorsal mesoderm and presumptive neural plate. Behavioral deficits in adnp2-deficient larvae are partially rescued by BMP antagonist Dorsomorphin or dominant-negative Bmpr1 mRNA, placing ADNP2 upstream of BMP signaling in neural induction. | PMID:41822989 | Development (Cambridge, England) |
| 2007 | Medium | ADNP2 deficiency (via siRNA knockdown) significantly changed the toxicity induced by hydrogen peroxide in P19 embryonic carcinoma cells, indicating a role for ADNP2 in cellular survival pathways under oxidative stress. | PMID:18179478 | Journal of neurochemistry |
| 2024 | Low | Cocaine decreased Adnp2 (and Adnp) mRNA expression 2 hours after injection in the nucleus accumbens and ventral tegmental area of male mice, with levels returning to baseline after 24 hours, implicating ADNP2 in cocaine-induced neuroadaptations. | PMID:39251453 | Journal of molecular neuroscience : MN |
| 2024 | Medium | Loss of adnp2 in zebrafish mutants resulted in significant downregulation of pan-neuronal HuC and neuronal fiber network α-Tubulin signals, and RNA-seq of adnp2a;adnp2b larval brains revealed altered gene expression profiles affecting synaptic transmission, autophagy, apoptosis, microtubule dynamics, hormone signaling, and circadian rhythm regulation. | PMID:39273418 | International journal of molecular sciences |

## Citations

- PMID:18179478
- PMID:23071114
- PMID:38960717
- PMID:39251453
- PMID:39273418
- PMID:41822989
