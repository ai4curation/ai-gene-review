---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AMTN
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q6UX39
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 21
citation_count: 21
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AMTN (human)

## Current model (mechanistic narrative)

AMTN (amelotin) is a secreted, O-glycosylated matrix protein that controls calcium phosphate mineralization at specialized epithelial-mineral interfaces, originally identified as a product specifically expressed and secreted by maturation-stage ameloblasts [PMID:16304441, PMID:16787391]. It localizes to the basal lamina between maturation-stage ameloblasts and enamel and to the internal basal lamina of junctional epithelium, where it occupies a subdomain skewed toward the mineral surface [PMID:16787391, PMID:22231912]. AMTN self-associates and engages in direct protein-protein interactions with ODAM and SCPPPQ1—but not with amelogenin, ameloblastin, or enamelin—forming supramolecular aggregates that structure the adhesive extracellular matrix mediating epithelial attachment to the mineral surface [PMID:22243260, PMID:28436474]. Functionally, AMTN binds hydroxyapatite and directly promotes mineral nucleation and growth through a phosphorylatable SSEEL motif whose mutation abolishes most of its mineralizing activity [PMID:25407797]; the phosphorylation state of this motif acts as a molecular switch—the nonphosphorylated form drives dissolution-recrystallization of amorphous calcium phosphate to hydroxyapatite, while the phosphorylated form stabilizes amorphous calcium phosphate and delays transformation [PMID:32036670]. Tight regulation of AMTN level and timing is required for normal enamel: overexpression in secretory-stage ameloblasts disorganizes enamel microstructure [PMID:22539960], and genetic ablation in mice produces hypomineralized, mechanically inferior enamel through a role largely independent of other enamel matrix proteins [PMID:25715379]. A heterozygous in-frame deletion within AMTN causes autosomal dominant hypomineralized amelogenesis imperfecta in humans [PMID:27412008]. Beyond the tooth, AMTN drives pathological hydroxyapatite deposition: it is induced in retinal pigment epithelium under stress and is required for, and sufficient to drive, calcification in models of dry age-related macular degeneration [PMID:32160961, PMID:42134448]. In gingival epithelium, AMTN transcription is induced by proinflammatory cytokines and bacterial LPS through C/EBPβ and YY1 promoter elements and is repressed by SNAI2 during epithelial-mesenchymal transition [PMID:30158339, PMID:29282478, PMID:30488439].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0008289 lipid binding
- **localization:** GO:0005576 extracellular region, GO:0030312 external encapsulating structure
- **pathway (Reactome):** R-HSA-1474244 Extracellular matrix organization, R-HSA-1643685 Disease
- **partners:** ODAM, SCPPPQ1, AMTN
- **complexes:** AMTN-ODAM-SCPPPQ1 supramolecular complex (specialized basal lamina)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2005 | Medium | AMTN (amelotin) encodes a novel secreted protein specifically expressed in maturation-stage ameloblasts; protein is efficiently secreted from transfected cells in culture, establishing its secretory nature. | PMID:16304441 | Journal of dental research |
| 2006 | High | AMTN protein localizes specifically to the basal lamina at the interface between maturation-stage ameloblasts and enamel, and to the internal basal lamina of junctional epithelium, suggesting a role in cell adhesion; it is post-translationally modified via O-linked oligosaccharides on threonine residues. | PMID:16787391 | The Biochemical journal |
| 2011 | High | AMTN and ODAM are bona fide components of the basal lamina associated with maturation-stage ameloblasts, occupying distinct subdomains: AMTN concentrates toward the enamel side while ODAM concentrates toward the cell side at early maturation. Lectin (Helix pomatia agglutinin) competitive incubation significantly reduced AMTN antibody labeling, confirming O-linked glycosylation of AMTN or its close association with O-glycosylated molecules. | PMID:22231912 | Histochemistry and cell biology |
| 2011 | Medium | AMTN interacts with itself (self-interaction) and with ODAM, but does not interact with amelogenin (AMEL), ameloblastin (AMBN), or enamelin (ENAM), as determined by yeast two-hybrid analysis. | PMID:22243260 | European journal of oral sciences |
| 2011 | Medium | Recombinant AMTN protein does not mediate cell attachment in vitro, arguing against a direct cell adhesion role for the secreted protein. | PMID:21912076 | Cells, tissues, organs |
| 2012 | High | Targeted overexpression of AMTN under the amelogenin promoter in secretory-stage ameloblasts disrupts Tomes' process formation and causes completely disorganized enamel hydroxyapatite microstructure and thinner enamel, demonstrating that AMTN expression timing and level is critical for orderly enamel prism growth. | PMID:22539960 | PloS one |
| 2015 | High | Recombinant human AMTN promotes hydroxyapatite (HA) precipitation in a metastable buffer system; AMTN binds to HA crystals (confirmed by colloidal gold immunolabeling); its binding affinity to HA is comparable to that of amelogenin. Site-specific mutagenesis of the SSEEL motif (potential serine phosphorylation site) reduced in vitro mineral precipitation by >75%, establishing this motif as critical for the mineralizing function. A synthetic phosphorylated (P)S(P)SEEL peptide, but not the unphosphorylated form, facilitated mineralization, indicating phosphorylation is required but the motif alone is not sufficient. | PMID:25407797 | Journal of bone and mineral research |
| 2015 | High | Genetic ablation of AMTN in mice causes hypomineralized enamel with delayed mineralization, structural defects in outer enamel, increased surface roughness, and mechanically inferior enamel (chipping/fractures); expression of other enamel matrix proteins (AMEL, AMBN, ENAM, ODAM) and proteases (MMP-20) was not significantly altered, but KLK4 expression was delayed, demonstrating AMTN plays a largely independent and specific role in enamel biomineralization during maturation. | PMID:25715379 | Journal of dental research |
| 2016 | High | A heterozygous 8,678 bp genomic deletion encompassing exons 3-6 of AMTN (resulting in in-frame deletion of 92 amino acids) causes autosomal dominant hypomineralised amelogenesis imperfecta in humans, with enamel of lower mineral density and structural defects. | PMID:27412008 | Human molecular genetics |
| 2017 | High | AMTN, ODAM, and SCPPPQ1 co-localize in the specialized basal lamina (sBL); AMTN and SCPPPQ1 are skewed toward the tooth surface while ODAM is toward the cell. Bacterial two-hybrid analysis and co-immunoprecipitation demonstrated direct protein-protein interactions among AMTN, ODAM, and SCPPPQ1. Gel filtration and electron/atomic force microscopies showed these proteins form supramolecular aggregates, suggesting they structure an extracellular matrix mediating epithelial-to-mineral surface attachment. | PMID:28436474 | Scientific reports |
| 2020 | High | The phosphorylation state of the SSEEL motif in AMTN switches the phase transformation of acidic amorphous calcium phosphate (ACP) to hydroxyapatite on/off: the nonphosphorylated SSEEL promotes HAP formation by accelerating dissolution-recrystallization of acidic ACP, whereas the phosphorylated SSEEL stabilizes ACP and delays its transformation to HAP. Dynamic force spectroscopy showed greater binding energies of nonphosphorylated SSEEL to acidic ACP, explaining enhanced ACP dissolution. | PMID:32036670 | Langmuir |
| 2020 | High | AMTN is expressed in retinal pigment epithelium (RPE) under serum-deprivation conditions; siRNA knockdown of AMTN in RPE cells blocked hydroxyapatite (HAP) formation in culture, establishing a functional role for AMTN in pathological HAP deposition in AMD. AMTN was localized to HAP spherules/nodules in geographic atrophy (dry AMD) donor eyes but not in hard drusen, normal RPE, or wet AMD. | PMID:32160961 | Translational research |
| 2018 | Medium | SNAI2 downregulates AMTN gene expression by binding to E-boxes (E2 and E4) in the mouse AMTN gene promoter during TGFβ1-induced epithelial-mesenchymal transition (EMT) in gingival epithelial cells; this inhibitory effect operates independently of the TGFβ1-Smad3 signaling pathway (SNAI2 siRNA rescued SNAI2-induced downregulation and potentiated TGFβ1-induced AMTN expression). | PMID:30488439 | Journal of cellular physiology |
| 2018 | Medium | IL-1β and TNF-α induce AMTN gene transcription in mouse gingival epithelial GE1 cells via C/EBP1, C/EBP2, and YY1 response elements in the mouse AMTN gene promoter; ChIP assays showed increased C/EBPβ and YY1 binding to these elements upon cytokine treatment; signaling through tyrosine kinase, MEK1/2, and PI3-kinase pathways is required. | PMID:30158339 | Journal of oral science |
| 2018 | Medium | TNF-α induces AMTN gene transcription in human gingival epithelial cells via C/EBP1, C/EBP2, and YY1 elements in the human AMTN gene promoter; C/EBPβ binding to C/EBP elements and YY1 binding to YY1 element were increased by TNF-α as shown by ChIP; transcriptional activation requires PKA, Src-tyrosine kinase, MEK1/2, p38 kinase, NF-κB, and PI3K signaling. | PMID:29282478 | Inflammation research |
| 2018 | Medium | Lipopolysaccharide from Porphyromonas gingivalis induces Amtn gene transcription in mouse gingival epithelial cells via C/EBP1, C/EBP2, and YY1 elements; LPS-induced C/EBPβ and YY1 interact with Smad3 (demonstrated by co-immunoprecipitation), and C/EBPβ-Smad3 and YY1-Smad3 complexes bind to these promoter elements. | PMID:30761253 | FEBS open bio |
| 2018 | Medium | IL-1β induces AMTN gene transcription in human gingival epithelial cells via C/EBP1, C/EBP2, and YY1 elements; signaling requires PKA, tyrosine kinase, MEK1/2, and PI3K; C/EBPβ and YY1 binding to their respective elements increased after IL-1β treatment. | PMID:29928577 | FEBS open bio |
| 2020 | Medium | miR-200b suppresses TNF-α-induced AMTN expression in human gingival epithelial cells by targeting the AMTN 3'-UTR directly and by targeting IKKβ mRNA; NF-κB signaling (via IKKβ) is required for full TNF-α-induced AMTN expression. | PMID:32980912 | Odontology |
| 2022 | Medium | Recombinant human AMTN incorporated into collagen hydrogel promotes hydroxyapatite deposition both onto and within the collagen matrix; AMTN coating on dentin surface promotes mineral precipitation; AMTN-coated barrier membrane adheres to dentin with more than twofold greater tensile strength than AMTN-free membrane, and only 1% of rhAMTN is released, indicating most mineral-promoting activity is surface-bound. | PMID:35611164 | Cellular and molecular bioengineering |
| 2021 | Medium | rhAMTN applied via collagen membrane to murine calvarial defects promoted bone healing, with defect filling by mineralized tissue at 8 weeks; in vitro, rhAMTN increased Spp1 gene expression in osteogenic MC3T3-E1 cells and significantly enhanced cell proliferation. | PMID:34608582 | Annals of biomedical engineering |
| 2026 | Medium | Transgenic mice constitutively expressing human AMTN in RPE develop AMD-like abnormalities and, following moderate laser injury, form AMTN-dependent deposits containing AMTN, cholesterol, and calcium phosphate/HAP in laser lesions that obliterate adjacent photoreceptors and recruit microglia, demonstrating that AMTN expression in RPE is sufficient to drive pathological calcification when coupled with cell stress/injury. | PMID:42134448 | Experimental eye research |

## Citations

- PMID:16304441
- PMID:16787391
- PMID:21912076
- PMID:22231912
- PMID:22243260
- PMID:22539960
- PMID:25407797
- PMID:25715379
- PMID:27412008
- PMID:28436474
- PMID:29282478
- PMID:29928577
- PMID:30158339
- PMID:30488439
- PMID:30761253
- PMID:32036670
- PMID:32160961
- PMID:32980912
- PMID:34608582
- PMID:35611164
- PMID:42134448
