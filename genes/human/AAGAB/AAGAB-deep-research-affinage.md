---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/AAGAB
affinage_run_date: 2026-06-09T22:02:35
uniprot_accession: Q6PD74
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 12
citation_count: 10
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for AAGAB (human)

## Current model (mechanistic narrative)

AAGAB (p34) is an assembly chaperone for heterotetrameric clathrin adaptor protein complexes, nucleating the formation of AP1, AP2, and AP4 that drive clathrin-mediated membrane trafficking [PMID:31353312, PMID:34494650, PMID:35976721]. It uses two functionally distinct modules: an N-terminal type I pseudoGTPase domain (catalytically inactive) that engages and stabilizes the small σ subunits of AP1 and AP2 through an interface distinct from conventional GTPase contacts, and a C-terminal dimerization domain that recognizes the γ subunit of AP1 and the α subunit of AP2 using a shared surface; AAGAB exists as a homodimer that transitions to monomer upon binding adaptor subunits [PMID:36598941]. By guiding the sequential, ordered association of adaptor subunits and stabilizing partially assembled intermediates, AAGAB prevents the degradation that otherwise destroys unassembled subunits [PMID:31353312, PMID:34494650]. For AP2, AAGAB initiates assembly by forming an AAGAB:α:σ2 complex that is then handed off to CCDC32, which completes tetramer assembly before release [PMID:39145939]. Loss of AAGAB collapses adaptor assembly, broadly remodeling surface protein homeostasis, impairing endocytic recycling of growth factor receptors such as EGFR, and causing accumulation of the AP4 cargo ATG9A at the trans-Golgi network [PMID:23064416, PMID:34494650, PMID:35976721]. Nonsense and CTD-truncating mutations in AAGAB destabilize the protein and abolish chaperone function, causing punctate palmoplantar keratoderma (PPKP1) [PMID:23000146, PMID:36598941]. AAGAB additionally supports clathrin-mediated synaptic vesicle recycling and neurotransmitter release in neurons [PMID:38253235], and in hypoxic-ischemic injury models acts upstream of the E3 ligase NEDD4-1 to control ubiquitination of PTEN and SHIP2 [PMID:33712741, PMID:41412220].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0044183 protein folding chaperone, GO:0098772 molecular function regulator activity
- **localization:** GO:0005829 cytosol, GO:0005794 Golgi apparatus
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport, R-HSA-9609507 Protein localization, R-HSA-392499 Metabolism of proteins
- **partners:** AP1G1, AP2A1, AP2S1, AP1S3, AP4E1, CCDC32, NEDD4-1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2012 | Medium | AAGAB (p34) binds both α- and γ-adaptin clathrin adaptor protein complexes (AP1 and AP2), indicating a role in membrane trafficking. Knockdown of AAGAB in keratinocytes led to increased cell division linked to elevated EGFR protein expression and tyrosine phosphorylation, suggesting p34 deficiency impairs endocytic recycling of growth factor receptors. | PMID:23064416 | Nature genetics |
| 2012 | Medium | Nonsense mutations in AAGAB cause premature translation termination; the disease allele mRNA is absent or at low levels (nonsense-mediated decay). In affected individual keratinocytes, AAGAB immunofluorescence staining shifts from cytoplasmic granular distribution to perinuclear accumulation. | PMID:23000146 | American journal of human genetics |
| 2019 | High | AAGAB controls AP2 adaptor complex assembly in clathrin-mediated endocytosis. AAGAB guides the sequential association of AP2 subunits and stabilizes assembly intermediates; without AAGAB, AP2 subunits fail to form the complex and are degraded. A disease-causing PPKP1 mutation abrogates this function. | PMID:31353312 | Developmental cell |
| 2021 | High | AAGAB also regulates assembly of AP1 (involved in trans-Golgi network to endosome transport) by binding and stabilizing the γ and σ subunits of AP1. AAGAB mutation abolishes AP1 assembly and disrupts AP1-mediated cargo trafficking. AAGAB is not involved in AP3 complex formation. Loss of AAGAB massively alters surface protein homeostasis reflecting synergistic AP1 and AP2 deficiency. | PMID:34494650 | Journal of cell science |
| 2021 | Medium | AAGAB acts as a novel regulator of NEDD4-1, controlling the level of NEDD4-1 protein, which in turn mediates mono-ubiquitination of PTEN at lysine 13 (K13) and promotes PTEN nuclear translocation during hypoxic-ischemic conditions. Genetic upregulation of Aagab reduced PTEN nuclear translocation and alleviated neurological deficits in HIBD model rats. | PMID:33712741 | Cell death and differentiation |
| 2022 | High | AAGAB binds to and stabilizes the AP-4 ε and σ4 subunits, promoting AP-4 complex assembly. AAGAB-knockout cells show reduced levels of AP-4 subunits and accumulation of ATG9A at the TGN, phenocopying AP-4 subunit mutations. | PMID:35976721 | Molecular biology of the cell |
| 2023 | High | AAGAB exists as a homodimer before AP1/2 binding, mediated by its C-terminal domain (CTD). The CTD undergoes an oligomer-to-monomer transition upon binding AP subunits, using the same CTD surface to recognize both the γ subunit of AP1 and the α subunit of AP2. Disease-causing PPKP1 mutations truncate the CTD, destabilizing AAGAB and abolishing chaperone function. Crystal structure of the dimerization CTD reveals an antiparallel dimer of bent helices. | PMID:36598941 | Proceedings of the National Academy of Sciences of the United States of America |
| 2024 | High | AP2 assembly proceeds by an AAGAB-to-CCDC32 handover mechanism: AAGAB initiates AP2 assembly by stabilizing its α and σ2 subunits, forming an AAGAB:α:σ2 complex that cannot recruit further subunits. CCDC32 recognizes this complex and is handed off to form an α:σ2:CCDC32 ternary complex, which sequentially recruits µ2 and β2 subunits to complete AP2 assembly, with CCDC32 then released. A disease-causing mutation disrupts CCDC32's AP2-regulating function. | PMID:39145939 | Proceedings of the National Academy of Sciences of the United States of America |
| 2024 | High | The N-terminal region of AAGAB is a type i pseudoGTPase (catalytically inactive). The AAGAB pseudoGTPase domain (psGD) interacts with the σ subunits of AP1 and AP2 via a unique interface distinct from conventional GTPase-interacting regions. Crystal structure of the AAGAB psGD:AP1σ3 complex was solved, revealing the structural basis of σ subunit stabilization during adaptor complex assembly. | — | bioRxiv |
| 2024 | Medium | Loss of aagab in zebrafish causes impaired calcium responses and reduced local field potential in optic tectal neurons, reduced neurotransmitter (norepinephrine) release, and defective clathrin-mediated synaptic vesicle recycling (delayed FM 1-43 release in AAGAB-knockdown neuroblastoma cells). Overexpression of aagab mRNA restores neurotransmitter release, calcium responses, and swimming ability. | PMID:38253235 | Journal of genetics and genomics |
| 2025 | Medium | AAGAB overexpression increases NEDD4-1 protein levels, promotes SHIP2 ubiquitination, and accelerates SHIP2 degradation; NEDD4-1 knockdown reverses these effects, placing AAGAB upstream of NEDD4-1 in a regulatory axis that controls SHIP2 levels. This Aagab-NEDD4-1-SHIP2 axis alleviates mitochondrial oxidative stress in hypoxic-ischemic encephalopathy. | PMID:41412220 | Mitochondrion |
| 2025 | Medium | CCDC32 interacts with the appendage domain of the AP-2 α subunit using canonical endocytic regulator binding sites plus a novel conserved pocket on α. CCDC32 amphipathic helices bind the α/σ2 heterodimer and also mediate binding to PIP2-containing membranes. In solution, CCDC32 prevents AP-2 complex assembly and actively disassembles AP-2 tetramers; the presence of PIP2-containing membrane acts as a molecular switch releasing inhibitory interactions to allow full assembly. Cryo-EM visualizes an assembly intermediate with CCDC32 bound at both cargo-binding and membrane-binding sites, mimicking vesicle-associated AP-2 conformation. | — | bioRxiv |

## Citations

- PMID:23000146
- PMID:23064416
- PMID:31353312
- PMID:33712741
- PMID:34494650
- PMID:35976721
- PMID:36598941
- PMID:38253235
- PMID:39145939
- PMID:41412220
