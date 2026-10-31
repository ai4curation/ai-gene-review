---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ANAPC10
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q9UM13
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 12
citation_count: 12
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ANAPC10 (human)

## Current model (mechanistic narrative)

ANAPC10 (APC10/DOC1) is a core, stoichiometric subunit of the anaphase-promoting complex/cyclosome (APC/C) E3 ubiquitin ligase that is required for substrate degron recognition and the metaphase-to-anaphase transition [PMID:10318877, PMID:11247669]. Its structure is a beta-sandwich jellyroll DOC domain, and its C-terminus directly binds the TPR-repeat APC subunit CDC27/APC3 to anchor it within the complex [PMID:11524682, PMID:11884135]. Functionally, APC10 together with the co-activator Cdh1 forms a co-receptor for the destruction-box (D-box) degron: cryo-EM positions Cdh1 adjacent to Apc10 in the central APC/C cavity, and NMR demonstrates direct D-box–Apc10 contacts, explaining why APC10 is needed for processive substrate ubiquitylation rather than for complex assembly [PMID:21107322, PMID:31562243]. Loss of APC10 inactivates APC/C ubiquitination activity without destabilizing the complex, causing cell-autonomous metaphase arrest and accumulation of the substrate cyclin B across yeast, fly, and mouse systems [PMID:10318877, PMID:9736616, PMID:18297794]. Beyond its constitutive APC/C role, APC10 interacts with Smad3 to recruit the APC/C–CDH1 ligase for degradation of HEF1/NEDD9 [PMID:15144564], and during interphase binds NLRP3 to promote inflammasome activation, dissociating during mitosis—a cell-cycle-gated function in innate immune signaling [PMID:34407203].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0060090 molecular adaptor activity
- **localization:** GO:0005815 microtubule organizing center, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-1640170 Cell Cycle, R-HSA-392499 Metabolism of proteins
- **partners:** CDC27, CDH1, SMAD3, NEDD9, NLRP3
- **complexes:** APC/C (anaphase-promoting complex/cyclosome)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2010 | High | Cryo-EM structure of APC/C(Cdh1) bound to a D-box peptide at ~10 Å resolution revealed that Cdh1 and Apc10 together form a co-receptor for the D-box degron motif. Cdh1 repositions toward Apc10 within the central cavity of the APC/C, and NMR spectroscopy demonstrated direct D-box–Apc10 interactions, establishing that Apc10 directly contributes to D-box recognition alongside the co-activator. | PMID:21107322 | Nature |
| 2001 | High | Crystal structure of human APC10/DOC1 at 1.6 Å resolution revealed a beta-sandwich jellyroll fold homologous to ligand-binding domains of galactose oxidase and coagulation factor Va. Biochemical experiments further demonstrated that the C-terminus of APC10 directly binds CDC27/APC3, a TPR-repeat-containing APC subunit. | PMID:11524682 | Nature structural biology |
| 2002 | High | Crystal structure of S. cerevisiae Doc1/Apc10 at 2.2 Å resolution showed a beta-sandwich homologous to the galactose-binding domain of galactose oxidase, the C2 domain of coagulation factor, and XRCC1. Residues invariant across Doc1/Apc10 sequences, including a temperature-sensitive mitotic arrest mutant, map to a beta-sheet region proposed to mediate biomolecular interactions and APC ubiquitination function. | PMID:11884135 | Journal of molecular biology |
| 1999 | High | Doc1/Apc10 was shown to be a stoichiometric subunit of the yeast APC throughout the cell cycle. Mutation of Doc1/Apc10 inactivates APC ubiquitination activity without destabilizing the complex. The orthologous human APC10 protein is also a genuine APC subunit in vertebrates (human and frog), and its cellular levels and APC association are not cell-cycle-regulated, as determined by biochemical fractionation and mass spectrometric analysis. | PMID:10318877 | The Journal of biological chemistry |
| 1998 | High | In fission yeast, apc10+ is essential for viability and required for ubiquitination and degradation of mitotic B-type cyclins. apc10 mutants show temperature-sensitive growth with defects in chromosome segregation and fail to arrest at G1 upon nitrogen starvation. A subpopulation of Apc10 co-immunoprecipitates with the APC, though it does not co-sediment with the 20S complex, suggesting a regulatory association. | PMID:9736616 | The EMBO journal |
| 1999 | Medium | Human APC10/Doc1 binds APC core subunits throughout the cell cycle and localizes to centrosomes and mitotic spindles during mitosis, to kinetochores from prophase to anaphase, and to the midbody during telophase/cytokinesis, as determined by co-immunoprecipitation and immunofluorescence localization studies. | PMID:10498862 | Oncogene |
| 2004 | Medium | ANAPC10 physically interacts with Smad3 (via the MH2 domain), and together with CDH1 forms a complex with HEF1 (NEDD9). Domain mapping showed distinct Smad3 MH2 subdomains bind APC10 and HEF1. Overexpression of APC10 and CDH1 regulated HEF1 protein levels, suggesting Smad3 recruits the APC/C to HEF1 for ubiquitination and proteasomal degradation via direct Smad3–APC10 interaction. | PMID:15144564 | BMC cell biology |
| 2019 | Medium | The pseudosubstrate APC/C inhibitor Acm1 from budding yeast suppresses APC/C activity by combining high-affinity Cdh1 binding with a C-terminal D-box extension that specifically disrupts the normal interaction with Doc1/Apc10, thereby perturbing reaction processivity in ubiquitylation. Mutation of the conserved D-box converted Acm1 into an ABBA-motif-dependent APC/CCdh1 substrate, and biochemical analysis confirmed the extension's role in inhibiting processivity via Doc1/Apc10. | PMID:31562243 | The Journal of biological chemistry |
| 2001 | Medium | Disruption of the mouse Apc10/Doc1 gene underlies the oligosyndactylism (Os) radiation-induced mutation and two transgene-induced alleles (94-A and 94-K), all exhibiting a cell-autonomous block in metaphase-to-anaphase transition, establishing that Apc10/Doc1 is required for this cell cycle transition in vivo. | PMID:11247669 | Genomics |
| 2007 | Medium | In Drosophila, loss-of-function mutations in Apc10/Doc1 cause metaphase-like arrest, chromosome overcondensation, high mitotic index, and accumulation of cyclin B (an APC/C substrate) in larval neuroblasts, establishing that Apc10/Doc1 is essential for APC/C E3 ubiquitin ligase activity and cyclin B ubiquitination in vivo. | PMID:18297794 | Acta biologica Hungarica |
| 2021 | Medium | During interphase, APC10 interacts with NLRP3 and promotes NLRP3 inflammasome activation; during mitosis, APC10 dissociates from NLRP3 to repress inflammatory responses, establishing a cell-cycle-dependent switch role for APC10 in innate immune signaling. | PMID:34407203 | FEBS letters |
| 2012 | Low | ANAPC10 protein is mainly expressed in the cytoplasm of spermatogonia and leptotene/pachytene spermatocytes in the developing mouse testis, as established by immunofluorescence and in situ hybridization. | PMID:22190705 | Biology of reproduction |

## Citations

- PMID:10318877
- PMID:10498862
- PMID:11247669
- PMID:11524682
- PMID:11884135
- PMID:15144564
- PMID:18297794
- PMID:21107322
- PMID:22190705
- PMID:31562243
- PMID:34407203
- PMID:9736616
