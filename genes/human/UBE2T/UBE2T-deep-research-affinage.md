---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/UBE2T
affinage_run_date: 2026-06-10T10:51:56
uniprot_accession: Q9NPD8
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 35
citation_count: 37
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for UBE2T (human)

## Current model (mechanistic narrative)

UBE2T is the dedicated E2 ubiquitin-conjugating enzyme of the Fanconi anemia (FA) DNA interstrand crosslink repair pathway, pairing with the E3 ligase FANCL to catalyze monoubiquitination of FANCD2 and FANCI on chromatin [PMID:16916645, PMID:19111657]. In vitro reconstitution established that FANCD2 monoubiquitination minimally requires UBE2T plus the FANCL RWD-like domain, with FANCI both stimulating the reaction and restricting it to the physiological substrate lysine K561, while FANCI itself is monoubiquitinated at K523 [PMID:19111657, PMID:19589784]. A crystal structure of the FANCL RING–UBE2T complex defined an extensive electrostatic and hydrophobic interface beyond the generic E2–E3 contact that determines selective recognition of UBE2T over other E2 enzymes [PMID:24389026]. This activity is governed by DNA damage-induced recruitment of UBE2T and FANCD2 to chromatin to form an active E2/E3 holoenzyme rather than by stable assembly of the core complex, and is negatively autoregulated by FANCL-stimulated UBE2T automonoubiquitination [PMID:16916645, PMID:17938197]. Biallelic loss-of-function mutations in UBE2T cause Fanconi anemia (FA-T subtype): patient cells lack FANCD2/FANCI monoubiquitination, fail to form FANCD2 foci, and are hypersensitive to crosslinkers, defects complemented by wild-type UBE2T [PMID:26119737, PMID:26046368, PMID:26085575]. Beyond crosslink repair, UBE2T contributes to nucleotide excision repair and to the resolution of R-loops and transcription-replication conflicts to maintain genome stability [PMID:22615860, PMID:36928776]. UBE2T protein abundance is controlled post-translationally by CaMKII-δ9-mediated phosphorylation-dependent degradation and by NEDD4L-directed proteasomal turnover [PMID:31481791, PMID:34838005]. In cancer, UBE2T acts as an oncogenic ubiquitin conjugator that ubiquitinates diverse substrates—including p53, RACK1, Akt, RPL6, CDC42, FOXO1, and CBX6—frequently through K48- or K63-linked chains and often independently of or in cooperation with various E3 ligases, thereby activating Wnt/β-catenin, PI3K/AKT, and related signaling outputs [PMID:33323973, PMID:35169125, PMID:36156329, PMID:39915000, PMID:39716485].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140096 catalytic activity, acting on a protein, GO:0016740 transferase activity
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-392499 Metabolism of proteins, R-HSA-1643685 Disease, R-HSA-162582 Signal Transduction
- **partners:** FANCL, FANCD2, FANCI, RNF8, NEDD4L, TRIM25, TRIM28, MULE
- **complexes:** Fanconi anemia core complex (FANCL E2/E3 holoenzyme)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2006 | High | UBE2T is the E2 ubiquitin-conjugating enzyme essential for the Fanconi anemia pathway; it binds to FANCL (the E3 ubiquitin ligase subunit of the FA core complex) and is required for monoubiquitination of FANCD2 in vivo. UBE2T also undergoes automonoubiquitination stimulated by FANCL, which inactivates UBE2T, providing a self-inactivation/negative regulatory mechanism. | PMID:16916645 | Molecular cell |
| 2008 | High | In vitro reconstitution of FANCD2 monoubiquitination requires minimally UBE2T and FANCL. A conserved RWD-like domain in FANCL stimulates monoubiquitination. Addition of FANCI enhances monoubiquitination and restricts it to the in vivo substrate lysine residue on FANCD2 (K561). | PMID:19111657 | Molecular cell |
| 2007 | High | UBE2T and FANCD2 are each recruited to chromatin independently of the FA core complex. The E3 ligase activity of the FA core complex is determined not by its stable assembly but by its DNA damage-induced localization to chromatin. Therefore, FANCD2 monoubiquitination is regulated by formation of an active E2/E3 holoenzyme on chromatin rather than by multiprotein complex assembly. | PMID:17938197 | Molecular and cellular biology |
| 2009 | High | FANCI is monoubiquitinated on Lys-523 by the UBE2T–FANCL pair in vitro. FANCI and its C-terminal fragment possess a DNA binding activity that prefers branched DNA structures. | PMID:19589784 | The Journal of biological chemistry |
| 2014 | High | Crystal structure of the FANCL RING domain in complex with UBE2T revealed a specific and extensive network of electrostatic and hydrophobic interactions beyond the generic E2–E3 interface that determines selective recognition of UBE2T over other E2 enzymes by FANCL. | PMID:24389026 | Structure |
| 2012 | Medium | UBE2T (and FANCM) are required for nucleotide excision repair (NER) in addition to their role in ICL repair. UBE2T-deficient DT40 cells are unexpectedly sensitive to UV-induced DNA damage; genetic epistasis experiments indicate UBE2T collaborates to promote NER rather than translesion bypass, and UBE2T deficiency impairs efficient removal of UV-induced cyclobutane pyrimidine dimers. | PMID:22615860 | PloS one |
| 2015 | High | Biallelic loss-of-function mutations in UBE2T cause Fanconi anemia (FA-T subtype). Patient fibroblasts lack FANCD2 and FANCI monoubiquitination, fail to form FANCD2 foci after MMC treatment, and are hypersensitive to crosslinking agents; these defects are complemented by wild-type UBE2T expression. A missense mutation (p.Gln2Glu) abolishes FANCD2 monoubiquitination and FANCL interaction. | PMID:26119737, PMID:26046368, PMID:26085575 | Cell reports / American journal of human genetics |
| 2019 | High | CaMKII-δ9 phosphorylates UBE2T and targets it for degradation, thereby disrupting UBE2T-dependent DNA repair, causing accumulation of DNA damage and genome instability in cardiomyocytes, and promoting cardiomyopathy and heart failure. | PMID:31481791 | Nature cell biology |
| 2011 | Medium | Hypoxia rapidly and potently reduces UBE2T mRNA levels in cancer cell lines through reduced promoter activity (HIF-independent, not due to mRNA or protein stability changes), correlating with increased sensitivity to interstrand crosslinking agents and disruption of the FA pathway. | PMID:21722982 | Radiotherapy and oncology |
| 2017 | Medium | A novel allosteric binding pocket on UBE2T was identified through fragment screening; fragments binding to this site inhibit ubiquitin conjugation in vitro. | PMID:28437106 | Journal of medicinal chemistry |
| 2017 | Medium | A zinc ion from a fragment library contaminant binds the active-site cysteine of UBE2T and induces a domain swap leading to cyclic trimerization in an open-ended linear assembly, revealing structural plasticity of the UBE2T active site. | PMID:28933844 | Journal of medicinal chemistry |
| 2019 | Medium | A small-molecule inhibitor of UBE2T/FANCL-mediated FANCD2 monoubiquitylation was identified that sensitizes cells to the DNA cross-linking agent carboplatin, establishing UBE2T enzymatic activity as pharmacologically targetable. | PMID:31525021 | ACS chemical biology |
| 2020 | Medium | UBE2T forms an E2–E3 pair with RNF8 and monoubiquitinates histone variant H2AX/γH2AX upon radiation exposure. This monoubiquitination facilitates CHK1 phosphorylation/activation and CHK1 release from chromatin to cytosol. E2-enzyme-deficient mutation C86A of UBE2T and monoubiquitination-site-deficient mutation K119/120R of H2AX both abrogate CHK1 activation. | PMID:33087136 | Journal of experimental & clinical cancer research |
| 2020 | Medium | UBE2T promotes Wnt/β-catenin signaling hyperactivation in gastric cancer by mediating ubiquitination and proteasomal degradation of RACK1 at lysine residues K172, K225, and K257, independently of an E3 ligase. | PMID:33323973 | Oncogene |
| 2020 | Low | UBE2T promotes ubiquitination and degradation of FOXO1 in non-small cell lung cancer, activating Wnt/β-catenin signaling, and promoting EMT and radiation resistance. | PMID:32590022 | Cancer letters |
| 2017 | Low | UBE2T promotes ubiquitination and degradation of p53, decreasing p53, p21, and Noxa levels, thereby facilitating hepatocellular carcinoma cell growth. | PMID:28935368 | Biochemical and biophysical research communications |
| 2022 | Medium | UBE2T promotes K63-linked ubiquitination of Akt, activating Akt/β-catenin signaling; E2-enzyme-deficient mutation C86A of UBE2T and ubiquitination-site-deficient mutation K8/14R of Akt impair downstream pathway activation and pyrimidine enzyme upregulation in HCC. | PMID:35169125 | Cell death & disease |
| 2021 | Medium | UBE2T physically binds the E3 ubiquitin ligase Mule and regulates its protein level via ubiquitination, thereby preventing Mule-mediated degradation of β-catenin and promoting liver CSC functions. This effect requires the E2 catalytic activity of UBE2T. | PMID:33542213 | Cell death & disease |
| 2021 | Medium | NEDD4L is an E3 ligase that ubiquitinates UBE2T and targets it for proteasomal degradation, reducing UBE2T protein half-life; NEDD4L-mediated UBE2T degradation represses PI3K-AKT signaling and suppresses lung adenocarcinoma cell progression. | PMID:34838005 | Cancer cell international |
| 2020 | Low | SENP1 deSUMOylates UBE2T, increasing UBE2T protein expression and activating the Akt pathway, promoting HCC progression. UBE2T is thus identified as a SUMOylation substrate regulated by SENP1. | PMID:31969492 | Aging |
| 2023 | Medium | UBE2T catalyzes RING1-mediated ubiquitination of p53, relieving transcriptional repression of ribonucleotide reductase subunits RRM1 and RRM2, resulting in unrestrained pyrimidine biosynthesis and alleviation of replication stress in pancreatic cancer, conferring gemcitabine resistance. | PMID:36842710 | Gastroenterology |
| 2022 | Low | UBE2T directly binds FANCI and regulates its monoubiquitination; overexpression of UBE2T reversed effects of FANCI knockdown in NSCLC cells, placing UBE2T upstream of FANCI monoubiquitination in a cancer context. | PMID:35703356 | Oncology reports |
| 2022 | Low | UBE2T mediates K48-linked polyubiquitination and degradation of ribosomal protein L6 (RPL6) in an E3 ligase-independent manner in glioblastoma, reducing wild-type p53 and enhancing gain-of-function mutant p53. | PMID:36156329 | Cancer science |
| 2023 | Medium | UBE2T resolves R-loops and stabilizes replication forks at transcription-replication conflict sites and common fragile sites in primordial germ cells (PGCs), and promotes mitotic DNA synthesis to maintain genome stability; Ube2t knockout mice show defects in PGC proliferation with DNA damage accumulation and p53 pathway activation. | PMID:36928776 | Cellular and molecular life sciences |
| 2019 | Medium | CRISPR/Cas9-mediated knockout of UBE2T in HeLa and U2OS cells only partially reduced homologous recombination (HR), demonstrating that UBE2T-independent pathways can compensate for the recombination defect in UBE2T/FANCT null cells. | PMID:30715513 | Nucleic acids research |
| 2024 | Medium | Fragment screening by 19F-NMR and 1H-15N-HSQC, validated by X-ray crystallography, identified two new binding pockets on UBE2T distinct from the active site; compounds binding these sites show inhibitory activity on UBE2T ubiquitination. | PMID:38358126 | Protein science |
| 2025 | Medium | UBE2T mediates K48-linked polyubiquitination and proteasomal degradation of CDC42, thereby preventing CDC42-mediated autophagic lysosomal degradation of CD276 (B7-H3), leading to CD276 upregulation, impairment of CD8+ T cell function, and immune escape in triple-negative breast cancer. | PMID:39915000 | Journal for immunotherapy of cancer |
| 2024 | Medium | UBE2T collaborates with E3 ligase TRIM25 to perform K48-linked polyubiquitination and degradation of CBX6 at K214, relieving transcriptional repression of pluripotency genes SOX2 and NANOG and enhancing breast cancer stem cell stemness. | PMID:39716485 | Cancer letters |
| 2025 | Low | UBE2T mediates ubiquitination-dependent degradation of HP1α via the proteasome pathway in IDH1/TP53-mutant glioma, leading to release of suppressive effects of R-2-hydroxyglutarate on nucleolar function and increased rDNA transcription. | PMID:40627452 | Clinical cancer research |
| 2021 | Low | UBE2T mediates ubiquitination of BIRC5 (survivin) through interaction with DEPDC1B in chordoma cells; simultaneous downregulation of BIRC5 and DEPDC1B exacerbates the inhibitory effects, and BIRC5 overexpression reverses the inhibitory effects of DEPDC1B knockdown. | PMID:34330893 | Cell death & disease |
| 2026 | Low | Betulinic acid (BA) selectively suppresses UBE2T expression at the transcriptional level via MAPK/ERK pathway inhibition (pharmacological reactivation of ERK reverses UBE2T suppression), thereby blocking FANCL-UBE2T-mediated FANCI/FANCD2 monoubiquitination, impairing ICL repair, and sensitizing glioma to cisplatin. | PMID:41486508 | Journal of cellular and molecular medicine |
| 2025 | Low | UBE2T cooperates with E3 ligase TRIM28 to facilitate K48-linked ubiquitination and degradation of phospho-GSK3β (pGSK3β), disrupting the β-catenin destruction complex and promoting nuclear translocation of β-catenin, thereby activating prostate cancer stem cell self-renewal. | PMID:42070337 | Phytomedicine |
| 2024 | Low | UBE2T mediates ubiquitination of the transcription factor PBX1, which then affects transcriptional regulation of RORA in lung adenocarcinoma; luciferase reporter assay, ChIP, and Co-IP established the UBE2T–PBX1–RORA regulatory axis. | PMID:39289660 | BMC cancer |
| 2024 | Low | UBE2T mediates ubiquitination and degradation of SORBS3, thereby enhancing IL-6/STAT3 signaling and promoting lung adenocarcinoma progression; validated in vitro and in vivo. | PMID:38816989 | Journal of biochemical and molecular toxicology |
| 2025 | Low | UBE2T promotes papillary thyroid carcinoma progression by co-immunoprecipitating with SOCS2 and promoting its destabilization, thereby relieving SOCS2-mediated inhibition of STAT3 phosphorylation and activating JAK-STAT3 signaling. | PMID:41330207 | Seminars in oncology |

## Citations

- PMID:16916645
- PMID:17938197
- PMID:19111657
- PMID:19589784
- PMID:21722982
- PMID:22615860
- PMID:24389026
- PMID:26046368
- PMID:26085575
- PMID:26119737
- PMID:28437106
- PMID:28933844
- PMID:28935368
- PMID:30715513
- PMID:31481791
- PMID:31525021
- PMID:31969492
- PMID:32590022
- PMID:33087136
- PMID:33323973
- PMID:33542213
- PMID:34330893
- PMID:34838005
- PMID:35169125
- PMID:35703356
- PMID:36156329
- PMID:36842710
- PMID:36928776
- PMID:38358126
- PMID:38816989
- PMID:39289660
- PMID:39716485
- PMID:39915000
- PMID:40627452
- PMID:41330207
- PMID:41486508
- PMID:42070337
