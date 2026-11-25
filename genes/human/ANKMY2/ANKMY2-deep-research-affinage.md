---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANKMY2
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q8IV38
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

# Affinage mechanistic annotation for ANKMY2 (human)

## Current model (mechanistic narrative)

ANKMY2 is an ankyrin repeat- and MYND domain-containing protein that targets membrane nucleotidyl cyclases to sensory and primary cilia, thereby coupling ciliary cyclic-nucleotide signaling to developmental patterning [PMID:21124868, PMID:32702291]. The conserved nature of this role was first established in C. elegans, where the ortholog DAF-25 localizes the guanylyl cyclase DAF-11 to sensory cilia without affecting cilium structure or intraflagellar transport, and in mouse where ANKMY2 binds photoreceptor guanylyl cyclase GC1 [PMID:21124868]. In mammals, ANKMY2 binds multiple adenylyl cyclases and is required for their maturation and trafficking into primary cilia [PMID:32702291]. Loss of ANKMY2 depletes adenylyl cyclase III from neuroepithelial cilia and reduces ciliary cAMP/PKA-driven GLI2 and GLI3 repressor formation, producing a Smoothened-independent ventralization of the neural tube and embryonic lethality [PMID:32702291, PMID:37943875]. ANKMY2 acts downstream of FKBP38 to control Hedgehog signaling output across neural tube and skeletal morphogenesis [PMID:25077969, PMID:37943875]. In kidney epithelium, ANKMY2 governs ciliary adenylyl cyclase trafficking without altering bulk cellular cAMP, and its loss suppresses cilia-dependent cyst initiation and extends survival in Pkd1-deletion models of polycystic kidney disease [PMID:41474822].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005929 cilium
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-1266738 Developmental Biology, R-HSA-9609507 Protein localization, R-HSA-1643685 Disease
- **partners:** FKBP38, GUCY2D, ADCY3
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2010 | High | C. elegans DAF-25 (ortholog of mammalian ANKMY2) localizes to sensory cilia and is required for proper ciliary localization of the guanylyl cyclase DAF-11; daf-25 mutants show normal cilia structure and normal IFT but mislocalized DAF-11. Mouse ANKMY2 interacts with guanylyl cyclase GC1 from ciliary photoreceptors, indicating evolutionary conservation of this function. | PMID:21124868 | PLoS genetics |
| 2014 | High | ANKMY2 interacts with FKBP38 (co-immunoprecipitation of endogenous proteins in mouse brain) and acts downstream of FKBP38 to activate Sonic Hedgehog (Shh) signaling. Depletion of ANKMY2 reduces Shh signaling; overexpression increases it in mouse embryonic fibroblasts. Combined depletion of FKBP38 and ANKMY2 attenuates Shh signaling, placing ANKMY2 downstream of FKBP38. Antisense morpholino knockdown of zebrafish ankmy2a produces a phenotype consistent with Shh loss of function. | PMID:25077969 | The Journal of biological chemistry |
| 2020 | High | ANKMY2 binds to multiple adenylyl cyclases and is required for their maturation and trafficking to primary cilia. Ankmy2 knockout mice are mid-embryonic lethal with fully open neural tubes showing co-expansion of all ventral neuroprogenitor markers. The ventralization phenotype is completely independent of Smoothened and results from reduced GLI2 and GLI3 repressor formation and early depletion of adenylyl cyclase III from neuroepithelial cilia. | PMID:32702291 | Developmental cell |
| 2023 | High | ANKMY2-mediated cAMP/PKA signaling in cilia promotes GLI repressor (GLI-R) formation during neural tube and skeletal morphogenesis. Genetic epistasis between Ankmy2 mutants and Gli2/Gli3 knockouts, Gli3R knock-in, and Smoothened knockout establishes that ANKMY2 derepression phenotypes arise through three modes: lack of GLI-R only, excess GLI-A formation only, or dual regulation, mostly independent of Smoothened. | PMID:37943875 | PLoS genetics |
| 2025 | High | ANKMY2 controls ciliary trafficking of multiple adenylyl cyclases in mouse and human kidney epithelial cells without disrupting cilia or cellular cAMP pools. Kidney-specific loss of ANKMY2 suppresses early postnatal cystogenesis and extends survival in embryonic-onset Pkd1 deletion mice, and reduces cyst burden in adult inducible Pkd1 knockout mice. Ciliary elongation preceding and accompanying cyst formation is ANKMY2-dependent, while cellular cAMP (phospho-CREB) levels remain unaffected. | PMID:41474822 | PLoS genetics |
| 2025 | Medium | ANKMY2 determines ciliary trafficking of adenylyl cyclases in kidney epithelial cells and ciliary cAMP signaling promotes cilia-dependent cyst initiation in ADPKD distinct from cyst progression involving cellular cAMP (preprint version of the same findings as PMID:41474822). | PMID:40501923 | bioRxiv |
| 2026 | Medium | In Drosophila, loss of dAnkmy2 (the fly ortholog) causes larval lethality, indicating an essential developmental function. Overexpression of dAnkmy2 extends adult lifespan and enhances resistance to oxidative stress without detectable changes in canonical antioxidant gene expression. | PMID:42035399 | Biogerontology |

## Citations

- PMID:21124868
- PMID:25077969
- PMID:32702291
- PMID:37943875
- PMID:40501923
- PMID:41474822
- PMID:42035399
