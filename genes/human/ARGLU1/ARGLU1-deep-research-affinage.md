---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARGLU1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9NWB6
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 11
citation_count: 11
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARGLU1 (human)

## Current model (mechanistic narrative)

ARGLU1 is a bifunctional nuclear protein that couples alternative pre-mRNA splicing to transcriptional regulation [PMID:30698747, PMID:27899669]. Its arginine-rich N-terminus binds RNA and splicing factors, while its glutamate-rich C-terminus coactivates nuclear receptors including the glucocorticoid receptor [PMID:30698747]; the latter activity is executed in part through direct interaction with the Mediator subunit MED1, with which ARGLU1 colocalizes and is recruited in a ligand-dependent manner to estrogen receptor target gene promoters to regulate transcription [PMID:21454576]. ARGLU1 autoregulates its own expression by promoting intron retention and NMD-susceptible isoforms of its own transcript through an ultraconserved element in the retained intron, a feedback circuit that is relieved by an ARGLU1-derived stable intronic sequence RNA that binds the protein and sequesters it in nuclear speckles [PMID:27899669, PMID:36533631]. Loss of ARGLU1 drives genome-wide splicing changes and is embryonic lethal in mice, and in developing cortex its ablation mis-splices Mdm2 and Mdm4 to remove their p53-binding domains, relieving p53 repression and causing radial glial detachment, apoptosis, and microcephaly that is rescued by p53 removal [PMID:30698747, PMID:37612280]. ARGLU1 also enhances promoter-proximal RNA polymerase II pausing, by inhibiting the JMJD6–BRD4 interaction, and promotes DNA damage repair, contributing to genotoxic-drug resistance in cancer cells [PMID:38520408]. Its protein levels are controlled by K11-linked ubiquitination and degradation via the DTL/CRL4A E3 ligase [PMID:38218284].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0003723 RNA binding, GO:0140110 transcription regulator activity, GO:0060090 molecular adaptor activity
- **localization:** GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-8953854 Metabolism of RNA, R-HSA-74160 Gene expression (Transcription), R-HSA-73894 DNA Repair, R-HSA-1266738 Developmental Biology
- **partners:** MED1, JMJD6, BRD4, DTL, E1A, SP1, YY1
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2011 | High | ARGLU1 directly interacts with the far C-terminal region of MED1 (Mediator subunit 1), colocalizes with MED1 in the nucleus, cooperates with MED1 to regulate estrogen receptor-mediated gene transcription, and is recruited in a ligand-dependent manner to estrogen receptor target gene promoters. | PMID:21454576 | The Journal of biological chemistry |
| 2019 | High | The glutamate-rich C-terminus of ARGLU1 coactivates multiple nuclear receptors including the glucocorticoid receptor (GR), while the arginine-rich N-terminus interacts with splicing factors and binds RNA. ARGLU1 depletion causes significant changes in gene expression and alternative splicing in neural cells, and loss of ARGLU1 is embryonic lethal in mice; knockdown in zebrafish causes neurodevelopmental and heart defects. | PMID:30698747 | Nucleic acids research |
| 2017 | High | ARGLU1 autoregulates its own mRNA splicing: overexpression of ARGLU1 protein shifts endogenous ARGLU1 mRNA splicing toward intron retention and NMD-susceptible isoforms (reducing fully spliced isoform), while functional protein knockout shifts splicing toward the fully spliced isoform. This autoregulation is mediated through an Ultraconserved Element (UCE) within the retained intron. | PMID:27899669 | Nucleic acids research |
| 2024 | Medium | ARGLU1 enhances promoter-proximal RNA polymerase II pausing, likely by inhibiting the interaction between JMJD6 and BRD4. ARGLU1 overexpression increases cancer cell resistance to genotoxic drugs and promotes DNA damage repair, while its knockdown leads to growth arrest. | PMID:38520408 | Nucleic acids research |
| 2024 | Medium | The E3 ubiquitin ligase DTL interacts with ARGLU1 and promotes K11-linked ubiquitination-mediated degradation of ARGLU1, thereby activating the CSL-dependent Notch signaling pathway in HNSCC cells. | PMID:38218284 | International journal of biological macromolecules |
| 2023 | High | Ablation of Arglu1 in mouse embryonic cortex causes widespread alternative splicing changes, including mis-splicing of Mdm2 (exon 3) and Mdm4 (exon 5) that removes the p53-binding domain and triggers NMD, thereby relieving p53 inhibition. This leads to radial glial cell detachment, prolonged mitosis, apoptosis, and microcephaly; removal of p53 largely rescues the microcephaly. | PMID:37612280 | Cell death & disease |
| 2022 | Medium | The ARGLU1-derived stable intronic sequence RNA (sisRNA) binds to ARGLU1 protein and promotes its localization to nuclear speckles, away from the Arglu1 gene locus, thereby repressing the splicing-inhibitory activity of ARGLU1 protein on its own host gene. | PMID:36533631 | EMBO reports |
| 2021 | Medium | ARGLU1 enhances the transcriptional levels of mismatch repair genes (MLH3, MSH2, MSH3, MSH6) by potentiating the recruitment of transcription factors SP1 and YY1 to their promoters. | PMID:34157484 | EBioMedicine |
| 2025 | Medium | ARGLU1 directly interacts with adenovirus E1A protein (confirmed by GST pulldown with recombinant proteins), colocalizes with E1A in infected cell nuclei, acts as a transcriptional repressor at viral promoters via enhanced promoter-proximal RNA Pol II pausing, and promotes DNA damage repair; an E1A mutant (dl1102) unable to bind ARGLU1 does not show reduced viral gene expression, confirming specificity. | PMID:41186411 | Journal of virology |
| 2022 | Medium | miR-335-5p directly targets the ARGLU1 3'UTR (confirmed by dual-luciferase reporter assay), negatively regulating ARGLU1 protein levels; overexpression of ARGLU1 partly rescues the anti-proliferative and pro-apoptotic effects of miR-335-5p mimic in uterine leiomyoma cell lines. | PMID:35082911 | Computational and mathematical methods in medicine |
| 2025 | Low | miR-499a-5p directly binds to ARGLU1 (confirmed by luciferase reporter assay) and negatively regulates ARGLU1 protein levels; silencing ARGLU1 enhances hypoxia-induced apoptosis and autophagy in H9c2 cardiomyocytes and reverses the protective effects of miR-499a-5p inhibition. | PMID:40694483 | The Kaohsiung journal of medical sciences |

## Citations

- PMID:21454576
- PMID:27899669
- PMID:30698747
- PMID:34157484
- PMID:35082911
- PMID:36533631
- PMID:37612280
- PMID:38218284
- PMID:38520408
- PMID:40694483
- PMID:41186411
