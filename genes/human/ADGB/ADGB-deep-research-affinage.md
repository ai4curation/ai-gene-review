---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ADGB
affinage_run_date: 2026-06-09T22:02:41
uniprot_accession: Q8N7X0
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 9
citation_count: 9
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for ADGB (human)

## Current model (mechanistic narrative)

Androglobin (ADGB) is a chimeric metazoan protein that functions in the assembly of motile cilia/flagella and in spermatid maturation [PMID:35700329, PMID:34083607]. Its unique modular architecture combines an N-terminal calpain-like catalytic domain, a circularly permuted hexacoordinated globin domain, and an IQ calmodulin-binding motif [PMID:22115833]. Calmodulin binds the IQ motif and enhances the nitrite reductase activity of the heme-binding globin domain [PMID:39719941], and ADGB is in turn required for proper calmodulin localization or stability in sperm [PMID:38385883]. In spermatogenesis, ADGB localizes to the acrosome and flagella [PMID:41834962] and is required for sperm head shaping, manchette and annulus formation, and flagellum integrity, acting through interactions with cytoskeletal and ciliary assembly factors including septin 10, CFAP69, SPEF2, TTC29, and CFAP47 [PMID:35700329, PMID:36995441, PMID:41834962]; loss of ADGB drives mislocalization of Sept10 and contributes to its proteolysis in a calmodulin-dependent manner [PMID:35700329]. In the ciliary central apparatus of Tetrahymena, ADGB associates with the C1b/C1f supercomplex [PMID:34083607]. ADGB expression is transcriptionally controlled by the ciliogenic regulators FOXJ1 and RFX3 [PMID:37158461, PMID:41138754]. Bi-allelic pathogenic ADGB variants cause male infertility presenting as asthenozoospermia and oligoasthenoteratozoospermia with acrosome, mitochondrial sheath, and axonemal defects [PMID:36995441, PMID:38385883, PMID:41834962].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016491 oxidoreductase activity, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005929 cilium, GO:0005856 cytoskeleton
- **pathway (Reactome):** R-HSA-1474165 Reproduction, R-HSA-1852241 Organelle biogenesis and maintenance
- **partners:** SEPT10, CFAP69, SPEF2, TTC29, CFAP47, CALM1
- **complexes:** C1b/C1f ciliary central apparatus supercomplex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2011 | Medium | Androglobin (ADGB) is a chimeric protein with a unique modular architecture comprising an N-terminal calpain-like domain homologous to catalytic domain II of human calpain-7, an internal circularly permuted globin domain, and an IQ calmodulin-binding motif. The recombinantly expressed human globin domain exhibits an absorption spectrum characteristic of hexacoordination of the heme iron atom. | PMID:22115833 | Molecular biology and evolution |
| 2022 | High | Adgb knockout mice display male infertility with impaired spermatid maturation, abnormal sperm shape, and ultrastructural defects in microtubule and mitochondrial organization. Immunoprecipitation and mass spectrometry identified septin 10 (Sept10) as an interactor of Adgb, confirmed by reciprocal co-immunoprecipitation both in vivo (testis lysates) and in vitro. Absence of Adgb leads to mislocalization of Sept10 in sperm, indicating defective manchette and sperm annulus formation. In vitro data suggest Adgb contributes to Sept10 proteolysis in a calmodulin-dependent manner. | PMID:35700329 | eLife |
| 2021 | Medium | In Tetrahymena thermophila, Adgb/androglobin localizes to the C1b/C1f supercomplex of the ciliary central apparatus. Deletion of Adgb caused only minor alterations in ciliary motility, whereas loss of other C1b/C1f subunits (Spef2A or Cfap69) caused loss of the entire C1b projection and abnormal cilia motion. | PMID:34083607 | Scientific reports |
| 2023 | Medium | Pathogenic variants in ADGB disrupt binding of ADGB to calmodulin, causing asthenozoospermia and male infertility. Mass spectrometry identified 42 candidate interacting proteins involved in sperm assembly, flagella formation, and sperm motility; CFAP69 and SPEF2 were confirmed to bind ADGB by co-immunoprecipitation. | PMID:36995441 | Human genetics |
| 2023 | Medium | FOXJ1 activates the ADGB promoter in transactivation assays in vitro, establishing ADGB as a downstream transcriptional target of FOXJ1 in ciliated cells. A truncating FOXJ1 variant (p.Glu267Glyfs*12) failed to activate the ADGB promoter. | PMID:37158461 | Human molecular genetics |
| 2024 | Medium | Calmodulin (CaM) interacts with ADGB via its IQ motif, and this interaction enhances the nitrite reductase activity of the ADGB heme-binding globin domain. Fluorescence quenching experiments using CaM mutants labeled at Cys41 (N-lobe) showed greater energy transfer to the heme group upon ADGB binding, consistent with predicted structural models of the Adgb-CaM complex. | PMID:39719941 | RSC chemical biology |
| 2024 | Medium | Bi-allelic deleterious ADGB variants in infertile men cause multiple acrosome and flagellum malformations in spermatozoa. Functional assays revealed structural defects associated with dysregulation of ADGB and multiple spermatogenesis proteins. CaM deficiency (but normal PLCζ) was detected in sperm from ADGB-deficient patients, suggesting ADGB is required for calmodulin localization or stability in sperm. | PMID:38385883 | Andrology |
| 2025 | Medium | RFX3 regulates ADGB promoter-driven luciferase activity and endogenous ADGB expression levels, identifying RFX3 as a transcriptional regulator of ADGB. Stable ADGB overexpression in A549 lung cancer cells caused transcriptomic changes indicative of increased cell motility and extracellular matrix remodeling. | PMID:41138754 | Gene |
| 2026 | Medium | ADGB localizes to the acrosome and flagella of spermatogenic cells in humans and mice, with high expression after puberty. Co-immunoprecipitation experiments confirmed TTC29 and CFAP47 as interacting proteins of ADGB. Compound heterozygous pathogenic ADGB mutations cause oligoasthenoteratozoospermia with acrosome loss, disorganized mitochondrial sheath, and disrupted axonemal '9+2' microtubule structure. | PMID:41834962 | Sichuan da xue xue bao. Yi xue ban |

## Citations

- PMID:22115833
- PMID:34083607
- PMID:35700329
- PMID:36995441
- PMID:37158461
- PMID:38385883
- PMID:39719941
- PMID:41138754
- PMID:41834962
