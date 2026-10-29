---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARL15
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9NXU5
self_evaluation_pairwise: 
faith_pct: 100.0
n_discoveries: 11
citation_count: 12
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARL15 (human)

## Current model (mechanistic narrative)

ARL15 is a small Arf-like GTPase that regulates membrane trafficking, divalent cation homeostasis, and TGFβ signaling from the Golgi and endomembrane compartments [PMID:34089346, PMID:35834310, PMID:40241309]. It is a bona fide nucleotide-binding enzyme: it possesses intrinsic GTPase activity, binds GTP and GDP with distinct affinities, and undergoes an N-terminal conformational change upon nucleotide loading [PMID:37939768]. Membrane targeting is achieved through triple S-acylation at N-terminal cysteines (Cys17, Cys22, Cys23) catalyzed redundantly by the Golgi S-acyltransferases ZDHHC7 and ZDHHC3; loss of acylation redistributes ARL15 to the cytosol [PMID:41999893]. From the Golgi, ARL15 directs trafficking of selective cargoes including caveolin-2 and STX6, and its depletion alters cell adhesion, spreading, and traction force generation [PMID:40241309]. In its GTP-bound state ARL15 binds the CBS-pair domain of CNNM magnesium transporters—a structurally defined interaction (R95 critical)—to inhibit both CNNM-mediated Mg2+ efflux and TRPM7-mediated divalent cation influx, in competition with PRL phosphatases [PMID:34089346, PMID:37449820, PMID:36711628]. Active ARL15 also binds the MH2 domain of Smad4 to relieve its autoinhibition and promote Smad complex assembly, with Smad4 in turn acting as a GAP that dissociates ARL15, positioning ARL15 as a positive effector of TGFβ family signaling [PMID:35834310]. Physiologically, ARL15 supports adiponectin secretion and adipogenesis [PMID:29242557], and germline knockout in mice is postnatally lethal with complete cleft palate [PMID:37773757].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0003924 GTPase activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005794 Golgi apparatus, GO:0005886 plasma membrane, GO:0005764 lysosome, GO:0005783 endoplasmic reticulum, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-162582 Signal Transduction, R-HSA-5653656 Vesicle-mediated transport, R-HSA-382551 Transport of small molecules, R-HSA-392499 Metabolism of proteins
- **partners:** CNNM1, CNNM2, CNNM3, CNNM4, SMAD4, ARL6IP5, STX6
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2017 | Medium | ARL15 knockdown in differentiated murine 3T3-L1 adipocytes impaired adiponectin secretion (but not adipsin secretion or insulin action), and knockdown in preadipocytes impaired adipogenesis. GFP-tagged ARL15 localized predominantly to the Golgi with lower levels at the plasma membrane and intracellular vesicles, suggesting involvement in intracellular trafficking. | PMID:29242557 | Scientific reports |
| 2021 | High | ARL15 directly interacts with CNNM family magnesium transporters (CNNM1-4) at their carboxyl-terminal CBS domains, co-localizes with CNNM2 in kidney cells at the ER, Golgi, and plasma membrane, and is required for complex N-glycosylation of CNNMs. ARL15 knockdown significantly increased 25Mg2+ uptake in kidney cancer cell lines, establishing ARL15 as a negative regulator of Mg2+ transport. | PMID:34089346 | Cellular and molecular life sciences : CMLS |
| 2022 | High | Active (GTP-bound) ARL15 specifically binds the MH2 domain of Smad4 and co-localizes with Smad4 at the endolysosome. This binding relieves Smad4 autoinhibition (imposed by intramolecular MH1-MH2 interaction), enabling Smad4 to interact with phosphorylated receptor-regulated Smads to form the Smad complex. Assembly of the Smad complex enhances Smad4's GAP activity toward ARL15, leading to ARL15 dissociation before nuclear translocation. ARL15 thus positively regulates TGFβ family signaling and functions as a Smad4 effector while Smad4 acts as its GAP. | PMID:35834310 | eLife |
| 2021 | Medium | Endogenous ARL15 is palmitoylated and localizes to the Golgi of mouse liver. Expression of palmitoylation-deficient ARL15 resulted in redistribution to the cytoplasm and mild reduction in adipogenesis-related gene expression. ARL15 undergoes Golgi translocation during adipocyte differentiation (from cis-Golgi in preadipocytes to other Golgi compartments after differentiation). Co-immunoprecipitation and mass spectrometry identified ARL6IP5 (an ER-localized protein) as an interacting partner. | PMID:34779483 | Biology open |
| 2023 | High | Crystal structure of the ARL15 GTPase domain in complex with the CNNM2 CBS-pair domain was solved, revealing the molecular basis for binding. ARL15 inhibits both CNNM2-mediated Mg2+ efflux and TRPM7-mediated divalent cation influx. An ARL15 binding-deficient mutant (R95A) failed to inhibit CNNM and TRPM7 transport. PRL2 (PTP4A2) competes with ARL15 for binding to CNNM, indicating antagonistic regulation. ARL15 was confirmed as a GTP-binding protein with low micromolar affinity for the CNNM CBS-pair domain. | PMID:37449820, PMID:36711628 | eLife |
| 2023 | Medium | ARL15 exhibits GTPase enzymatic activity (Km ~100 μM, Vmax ~1.47 μmole/min/μL). GTP binding affinity (Kd) is ~8-fold lower than GDP binding. SAXS analysis revealed that apo monomeric ARL15 adopts a globular shape (Dmax 6.1 nm) and undergoes conformational change upon GTP or GDP binding (Dmax ~7.6-7.7 nm), with the N-terminal region toggling open upon nucleotide binding. | PMID:37939768 | International journal of biological macromolecules |
| 2025 | Medium | ARL15 localizes primarily to the Golgi and cell surface in HeLa cells. Depletion of ARL15 causes mislocalization of selective Golgi cargoes caveolin-2 and STX6. Expression of GTPase-independent dominant-negative ARL15 mutants (V80A,A86L,E122K and C22Y,C23Y) also caused mislocalization of these cargoes. ARL15 Golgi localization is dependent on palmitoylation and Arf1-dependent Golgi integrity. ARL15-depleted cells display enhanced cell spreading, adhesion strength, higher traction forces, and multiple focal adhesion points during initial cell adhesion. | PMID:40241309 | Traffic (Copenhagen, Denmark) |
| 2023 | Medium | Global homozygous Arl15 knockout in mice is lethal postnatally and causes complete cleft palate. Arl15 knockout mouse embryonic fibroblasts show decreased cell migration. Heterozygous females show reduced fat mass and transiently lower adiponectin levels. | PMID:37773757 | FASEB journal |
| 2026 | High | ARL15 is triply S-acylated (palmitoylated) at three conserved N-terminal cysteine residues (Cys17, Cys22, Cys23) in HEK293T cells. Single Cys-to-Ser mutations substantially reduced S-acylation; triple mutation abolished it entirely. Loss of S-acylation disrupted membrane association of ARL15 (shown by confocal imaging and subcellular fractionation). The Golgi-localized S-acyltransferases ZDHHC7 and ZDHHC3 mediate ARL15 S-acylation in a partially redundant manner; dual inhibition caused marked reduction in S-acylation and redistribution from membranes to cytosol. | PMID:41999893 | The Journal of biological chemistry |
| 2026 | Low | ARL15 knockdown in ex vivo RA synovial fibroblasts (RASF) led to downregulation of COMP (extracellular matrix stabilizer) and upregulation of adiponectin and IFN response genes (IFI6, USP18, NPTX1, MX1), and downregulation of CTGF, CD248, and PTX3, implicating ARL15 in connective tissue architecture and inflammation regulation. | PMID:42087570 | International journal of rheumatic diseases |
| 2019 | Low | Overexpression of ARL15 in HUVECs under high-glucose conditions increased insulin-stimulated NO production and phosphorylation of the IR/IRS1/AKT/eNOS pathway, decreased ROS and MDA, increased SOD, and reduced ERK1/2 phosphorylation and NOX2/NOX4 expression, indicating ARL15 promotes insulin signaling and reduces oxidative stress in endothelial cells. | PMID:30682341 | Life sciences |

## Citations

- PMID:29242557
- PMID:30682341
- PMID:34089346
- PMID:34779483
- PMID:35834310
- PMID:36711628
- PMID:37449820
- PMID:37773757
- PMID:37939768
- PMID:40241309
- PMID:41999893
- PMID:42087570
