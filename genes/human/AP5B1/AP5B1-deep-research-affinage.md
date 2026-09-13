---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AP5B1
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q2VPB7
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

# Affinage mechanistic annotation for AP5B1 (human)

## Current model (mechanistic narrative)

AP5B1 encodes the β subunit of AP-5, an evolutionarily ancient heterotetrameric adaptor protein complex that assembles in a stoichiometric (~1:1:1:1:1:1) complex with SPG11 and SPG15 on late endosomes/lysosomes and mediates retrieval of cargoes back to the Golgi [PMID:23825025]. AP-5 functions as a backup to the retromer pathway: CRISPR knockout of an AP-5 subunit impairs retrieval of CIMPR, GOLIM4, and GOLM1 from endosomes to the Golgi, the phenotype is exacerbated by retromer knockdown, and CIMPR and sortilin bind the AP-5-associated protein SPG15 [PMID:29381698]. Recruitment of the AP-5/SPG11/SPG15 complex to late endosomes/lysosomes requires coincidence detection of PI3P (via the SPG15 FYVE domain) and Rag GTPases, with GDP-locked RagC promoting and GTP-locked RagA preventing recruitment, and is enhanced upon starvation, linking the complex to the mTORC1 pathway [PMID:33464297]. Loss of AP-5 function produces accumulation of aberrant multilamellar endolysosomal storage structures, defining AP-5 deficiency as a lysosomal storage disorder [PMID:26085577]. Bi-allelic loss-of-function variants in AP5B1 cause recessive inherited macular dystrophy, with AP5B1 localizing to puncta marked by late endosome and Golgi markers in retinal pigment epithelium [PMID:40081374].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity
- **localization:** GO:0005768 endosome, GO:0005764 lysosome, GO:0005794 Golgi apparatus
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport, R-HSA-9609507 Protein localization
- **partners:** SPG11, SPG15, AP5Z1
- **complexes:** AP-5 adaptor complex, AP-5/SPG11/SPG15 complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2013 | High | AP-5 forms a stoichiometric (~1:1:1:1:1:1) complex with SPG11 and SPG15, co-immunoprecipitated from both cytosol and detergent-extracted membranes. Knockdowns of SPG11 or SPG15 phenocopy knockdowns of AP-5 subunits, all causing the cation-independent mannose 6-phosphate receptor (CIMPR) to become trapped in clusters of early endosomes. AP-5, SPG11, and SPG15 colocalize on a late endosomal/lysosomal compartment. The N-terminal β-propeller-like domain of SPG11 interacts in vitro with AP-5. | PMID:23825025 | Molecular biology of the cell |
| 2018 | High | AP-5 functions in a late endosome-to-Golgi retrieval pathway. CRISPR-Cas9 knockout of AP5Z1 in HeLa cells leads to impaired retrieval of CIMPR, GOLIM4, and GOLM1 from endosomes back to the Golgi. The retromer complex shows altered steady-state distribution in AP-5 KO cells, and retromer knockdown exacerbates the AP-5 KO phenotype, placing AP-5 as a backup pathway for retromer. Both CIMPR and sortilin interact with the AP-5-associated protein SPG15 in pull-down assays. | PMID:29381698 | PLoS biology |
| 2015 | High | Loss of AP-5 ζ protein (and reduction of AP-5 µ5) in patient-derived fibroblasts causes accumulation of abundant multilamellar endolysosomal structures filled with aberrant storage material (multilamellar whorls, striated belts, fingerprint bodies). This phenotype is replicated by siRNA knockdown of AP-5 ζ in HeLa cells, defining AP-5 deficiency as a new type of lysosomal storage disease. | PMID:26085577 | Human molecular genetics |
| 2021 | High | Recruitment of the AP-5/SPG11/SPG15 complex to late endosomes/lysosomes requires coincidence detection of phosphatidylinositol 3-phosphate (PI3P) and Rag GTPases. PI3P binding is mediated by the SPG15 FYVE domain. GDP-locked RagC promotes recruitment of the complex, while GTP-locked RagA prevents its recruitment. Recruitment is enhanced in starved cells, revealing interplay between AP-5/SPG11/SPG15 and the mTORC1 pathway. | PMID:33464297 | The Journal of cell biology |
| 2016 | Medium | HIV-2 Gag particle release is dependent on AP-5 (and AP-3), but not AP-1 or AP-2, whereas HIV-1 Gag release requires AP-1 and AP-3 but not AP-5. This differential requirement demonstrates that AP-5 participates in an intracellular trafficking pathway used by HIV-2 Gag. | PMID:27392064 | PloS one |
| 2025 | Medium | Bi-allelic loss-of-function variants in AP5B1 (encoding the β subunit of the AP-5 complex) cause recessive inherited macular dystrophy. Immunostaining of retinal pigment epithelium (RPE) cells shows a punctate pattern of AP5B1 staining co-localizing with markers of late endosomes and the Golgi, supporting a role for AP-5 in RPE lysosomal/endosomal homeostasis. | PMID:40081374 | American journal of human genetics |
| 2012 | Low | AP-5 is an evolutionarily ancient heterotetrameric adaptor protein complex associated with endosomal dynamics. Its deficiency (mutations in AP5Z1) causes hereditary spastic paraplegia, implicating AP-5 in neuronal endosomal trafficking and homeostasis. | PMID:23167973 | Traffic (Copenhagen, Denmark) |

## Citations

- PMID:23167973
- PMID:23825025
- PMID:26085577
- PMID:27392064
- PMID:29381698
- PMID:33464297
- PMID:40081374
