---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARMC5
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q96C12
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 16
citation_count: 14
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARMC5 (human)

## Current model (mechanistic narrative)

ARMC5 is a cytosolic armadillo repeat- and BTB domain-containing substrate adaptor for a CUL3-RBX1 E3 ubiquitin ligase that directs ubiquitination and proteasomal degradation of selected substrates to control transcriptional capacity and cell fate [PMID:35687106, PMID:35862218]. Its principal substrate is RNA Polymerase II: CRL3-ARMC5 ubiquitinates RPB1/POLR2A and, in fact, all twelve Pol II subunits, restraining the cellular Pol II pool such that ARMC5 loss causes RPB1 accumulation and dysregulation of a defined subset of effector genes [PMID:35687106, PMID:38225631]. ARMC5 selectively recognizes excess and defective promoter-proximal, chromatin-bound Pol II that is CDK9-phosphorylated and SPT5-deficient, engaging this pool through its BTB domain and targeting it for VCP/p97-dependent degradation, while the Integrator gatekeeper INTS8 cooperates to prevent release of transcriptionally incompetent Pol II into elongation [PMID:39667934, PMID:39854452]. Beyond Pol II, ARMC5 uses its armadillo repeat domain to bind and degrade the SCAP-free pool of full-length SREBF/SREBP transcription factors, governing SREBF2 target genes in adrenocortical cells and stearoyl-CoA desaturase-driven fatty acid desaturation in adipocytes, and it controls the half-life of the antioxidant regulator NRF1 [PMID:35862218, PMID:39491648, PMID:36040830]. ARMC5 is itself a CUL3 substrate, interacting with CUL3 via its BTB domain and undergoing CUL3-dependent ubiquitination and degradation, and is stabilized by the deubiquitinase USP7 [PMID:32023208, PMID:33544460]. Functionally, ARMC5 is essential for early mouse embryonic development and gastrulation, supports T-cell proliferation and Th1/Th17 differentiation, and acts as an adrenocortical tumor suppressor by promoting apoptosis and restraining cell-cycle progression, with patient-derived inactivating mutations in the BTB or armadillo domains abrogating CUL3 binding, substrate binding, and degradation activity [PMID:28911199, PMID:28169274, PMID:32023208, PMID:35862218]. Inactivating ARMC5 mutations cause primary bilateral macronodular adrenocortical hyperplasia by enlarging the Pol II pool and dysregulating steroidogenic effector genes [PMID:35687106, PMID:28911199].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0060090 molecular adaptor activity, GO:0016874 ligase activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005829 cytosol, GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-392499 Metabolism of proteins, R-HSA-74160 Gene expression (Transcription), R-HSA-1640170 Cell Cycle, R-HSA-1430728 Metabolism
- **partners:** CUL3, RBX1, POLR2A, USP7, SREBF1, NRF1, INTS8, CDK9
- **complexes:** CUL3-RBX1 E3 ubiquitin ligase (CRL3-ARMC5)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2013 | Medium | ARMC5 inactivation decreased steroidogenesis in vitro, and its overexpression altered cell survival, establishing ARMC5 as a putative tumor suppressor gene in adrenocortical cells. | PMID:24283224 | The New England journal of medicine |
| 2015 | Medium | ARMC5 missense mutants and the p.F700del deletion are unable to induce apoptosis in H295R and HeLa cell lines, unlike wild-type ARMC5, demonstrating that ARMC5 promotes apoptosis and disease-associated mutations abrogate this function. | PMID:25853793 | The Journal of clinical endocrinology and metabolism |
| 2017 | High | Armc5 knockout mice die during early embryonic development around E6.5–E8.5 and fail to undergo gastrulation (absence of mesoderm at E7.5), establishing an essential role for ARMC5 in early embryonic development. | PMID:28911199 | Human molecular genetics |
| 2017 | High | Armc5 haploinsufficiency (Armc5+/- mice) leads to age-dependent decrease in corticosterone associated with decreased PKA catalytic subunit α (Cα) expression, followed later by hypercorticosteronemia with increased PKA/Cα expression and abnormal activation of Wnt/β-catenin signaling in zona fasciculata cells. | PMID:28911199 | Human molecular genetics |
| 2017 | High | Armc5 deletion in mice compromises T-cell proliferation, differentiation into Th1 and Th17 cells, and increases T-cell apoptosis, establishing a role for ARMC5 in T-cell immune responses. | PMID:28169274 | Nature communications |
| 2017 | Low | Yeast 2-hybrid assays identified 16 ARMC5-binding partners, establishing that ARMC5 functions through interaction with multiple signaling pathway proteins. | PMID:28169274 | Nature communications |
| 2017 | Medium | ARMC5 silencing in non-mutated PMAH cell cultures decreased steroidogenesis-related gene expression and increased CCNE1 mRNA expression and proliferative capacity without affecting cell viability, while ARMC5 overexpression induced cell death in PMAH-mutated cell cultures. | PMID:28676429 | Molecular and cellular endocrinology |
| 2020 | High | ARMC5 interacts with CUL3 via its BTB domain; this interaction leads to ARMC5 ubiquitination and proteasomal degradation. ARMC5 alters cell cycle progression (G1/S phases and cyclin E accumulation), and this effect is blocked by CUL3. BTB-domain missense mutations found in patients abolish CUL3 interaction and ARMC5 degradation. | PMID:32023208 | Endocrine-related cancer |
| 2021 | Medium | USP7 interacts with ARMC5 in vivo and in vitro, deubiquitinates ARMC5, and stabilizes it via the ubiquitin-proteasome pathway; USP7-mediated ARMC5 stabilization regulates G1/S cell cycle transition and renal cancer cell proliferation. | PMID:33544460 | Journal of cellular and molecular medicine |
| 2022 | High | ARMC5 functions as a substrate adaptor in a CUL3-RBX1 E3 ubiquitin ligase complex that ubiquitinates RPB1 (the largest subunit of RNA Pol II). ARMC5 deletion reduces RPB1 ubiquitination and causes accumulation of RPB1 and an enlarged Pol II pool, dysregulating a subset of genes. Mutant ARMC5 from PBMAH patients shows altered binding with RPB1. | PMID:35687106 | Nucleic acids research |
| 2022 | High | ARMC5 interacts with full-length SREBF (SREBP) through its Armadillo repeat domain and with CUL3 through its BTB domain, and promotes proteasome-dependent degradation of full-length SREBF via ubiquitination. ARMC5 missense mutations in its Armadillo repeat attenuate SREBF interaction; BMAH-associated mutations abolish SREBF degradation. In H295R cells, ARMC5 silencing increases full-length SREBFs and upregulates SREBF2 target genes; ARMC5-siRNA-mediated cell growth is abrogated by simultaneous SREBF2 knockdown. | PMID:35862218 | JCI insight |
| 2022 | Medium | ARMC5 is involved in NRF1 ubiquitination and controls NRF1 half-life in adrenocortical cells. ARMC5 inactivation increases NRF1 expression, elevates antioxidant enzymes (SODs and peroxiredoxins), alters adrenocortical steroidogenesis via the p38 pathway, decreases cell sensitivity to ferroptosis, and increases cell viability. | PMID:36040830 | Endocrine-related cancer |
| 2024 | High | CRL3ARMC5 targets excessive and defective RNA Pol II at initial stages of the transcription cycle (promoter-proximal zone and free pool). Upon ARMC5 loss, RNA Pol II accumulates in the free pool and promoter-proximal zone but is not released into elongation. Integrator subunit 8 (INTS8) acts as a gatekeeper preventing release of excess Pol II into gene bodies. Combined loss of ARMC5 and INTS8 leads to uncontrolled release of transcriptionally incompetent Pol II into early elongation, with detrimental effects on cell growth. | PMID:39667934 | Molecular cell |
| 2024 | High | ARMC5 controls degradation of not only POLR2A but also most of the other 11 Pol II subunits, indicating ARMC5-dependent E3 ligase activity controls degradation of the entire Pol II complex. ARMC5 knockout dysregulates 106 genes in neural progenitor cells including FOLH1. ARMC5 mutations identified in spina bifida patients impair ARMC5 interaction with Pol II and reduce Pol II ubiquitination. | PMID:38225631 | Genome biology |
| 2025 | High | ARMC5 acts as a CUL3 adaptor targeting promoter-proximal, chromatin-bound Pol II lacking SPT5 for VCP/p97-dependent degradation. ARMC5 targets promoter-proximal Pol II in a BTB domain-dependent manner. Interaction between ARMC5 and Pol II requires CDK9, supporting a phospho-dependent degradation model. | PMID:39854452 | Science advances |
| 2024 | High | ARMC5 selectively degrades SCAP-free full-length SREBF1 (but not SCAP-associated SREBF1) and is essential for fatty acid desaturation in adipocytes. Adipocyte-specific Armc5 KO mice show dramatic downregulation of all stearoyl-CoA desaturases (Scd), decreased unsaturated fatty acids, increased saturated fatty acids, and paradoxically diminished SREBF1 transcriptional activity at Scd1 locus despite increased full-length SREBF1 protein. | PMID:39491648 | The Journal of biological chemistry |

## Citations

- PMID:24283224
- PMID:25853793
- PMID:28169274
- PMID:28676429
- PMID:28911199
- PMID:32023208
- PMID:33544460
- PMID:35687106
- PMID:35862218
- PMID:36040830
- PMID:38225631
- PMID:39491648
- PMID:39667934
- PMID:39854452
