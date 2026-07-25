---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/PALB2
affinage_run_date: 2026-06-10T05:19:53
uniprot_accession: Q86YC2
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 35
citation_count: 35
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for PALB2 (human)

## Current model (mechanistic narrative)

PALB2 (Partner and Localizer of BRCA2) is the central scaffold of homologous recombination (HR) repair of DNA double-strand breaks, physically bridging BRCA1 and BRCA2 so that the recombinase machinery can be assembled at sites of damage [PMID:19268590, PMID:19584259]. Through its N-terminal coiled-coil it binds BRCA1 (residues L21/L24/L35) and through its C-terminus it binds BRCA2, thereby relaying BRCA1-mediated recruitment to BRCA2-RAD51 organization and strand invasion [PMID:17287723, PMID:19584259]; structurally the coiled-coil forms an antiparallel leucine-zipper that exists as a homodimer or as a BRCA1 heterodimer, and the switch from PALB2 homodimer to PALB2-BRCA1 heterodimer acts as the regulatory gate that activates HR [PMID:22941656, PMID:30289697]. PALB2 recruitment to breaks proceeds through an ubiquitin signaling cascade (MDC1, RNF8, RAP80, Abraxas upstream of BRCA1, and RNF168-generated ubiquitylated H2A read by BARD1-BRCA1), with the BRCA1-PALB2 heterodimer rather than the homodimer mediating RAD51 loading [PMID:23038782, PMID:28240985, PMID:34408138]. PALB2 carries intrinsic chromatin- and DNA-binding activities: a chromatin-association motif (ChAM) that engages the nucleosome acidic patch—an interaction antagonized by 53BP1 in BRCA1-deficient cells—and an N-terminal DNA-binding domain that stimulates RAD51 and possesses RAD51-independent strand-exchange activity [PMID:22193777, PMID:31017574, PMID:32041954]. Steady-state localization to actively transcribed genes occurs via MRG15 recognition of SETD2-deposited H3K36me3, protecting these regions during replication, and PALB2 is additionally recruited to stalled forks by phosphorylated RPA and sustains DNA polymerase η-dependent synthesis at blocked forks [PMID:28673974, PMID:25113031, PMID:24485656]. ATM/ATR-dependent phosphorylation of N-terminal S/Q sites is required for proper RAD51 foci formation and HR, and PALB2 also contributes to the G2/M checkpoint independently of CHK1/CHK2 [PMID:27113759, PMID:26420486, PMID:30337689]. Beyond DNA repair, PALB2 binds KEAP1 through a shared ETGE motif to promote NRF2-mediated antioxidant responses [PMID:22331464]. Patient-derived and systematic variant analyses establish that disruption of the BRCA1-PALB2 or BRCA2-PALB2 interactions, or destabilization of the WD40 domain, abolishes HR and confers sensitivity to platinum and PARP inhibitors, and mouse models disrupting these interactions produce Fanconi anemia-like and tumor-prone phenotypes [PMID:28319063, PMID:25016020, PMID:32732220, PMID:31636395, PMID:31757951].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0003677 DNA binding, GO:0140097 catalytic activity, acting on DNA, GO:0042393 histone binding, GO:0003723 RNA binding, GO:0098772 molecular function regulator activity
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome, GO:0005654 nucleoplasm
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-69306 DNA Replication, R-HSA-1640170 Cell Cycle, R-HSA-4839726 Chromatin organization, R-HSA-8953897 Cellular responses to stimuli, R-HSA-74160 Gene expression (Transcription)
- **partners:** BRCA2, BRCA1, MRG15, KEAP1, RNF168, RAD51C, USP22, RAD52
- **complexes:** BRCA1-PALB2-BRCA2 HR complex, PALB2-MRG15 complex, PALB2-RAD52 complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2007 | High | PALB2 directly interacts with BRCA2 and this interaction is crucial for BRCA2 DNA damage response functions and tumor suppression activity. A truncated PALB2 protein caused by the c.1592delT frameshift mutation retained little BRCA2-binding capacity and was deficient in homologous recombination and crosslink repair. | PMID:17287723 | Nature |
| 2009 | High | PALB2 physically links BRCA1 and BRCA2 in the DNA-damage response. BRCA1 associates with BRCA2 through PALB2; this interaction is abrogated in PALB2-deficient cells. BRCA1 promotes concentration of PALB2 and BRCA2 at DNA-damage sites, and the BRCA1-PALB2 interaction is required for homologous recombination repair. | PMID:19268590 | Current biology : CB |
| 2009 | High | PALB2 independently interacts with BRCA1 through its N-terminus (via coiled-coil domain residues L21 and L24) and with BRCA2 through its C-terminus. PALB2 mediates the physical interaction of BRCA2 with a C-terminal fragment of BRCA1. BRCA1 recruits PALB2, which in turn organizes BRCA2 and RAD51. Both PALB2-BRCA1 and PALB2-BRCA2 interactions are required for resistance to mitomycin C and homologous recombination repair of DNA double-strand breaks. | PMID:19584259 | Molecular cancer research : MCR |
| 2010 | High | PALB2 binds directly to MRG15, a chromodomain protein component of histone acetyltransferase-deacetylase complexes. MRG15 interacts with the entire BRCA complex (BRCA1, PALB2, BRCA2, RAD51). MRG15 deficiency, like PALB2 or BRCA2 deficiency, reduces homology-directed DNA repair efficiency and causes hypersensitivity to DNA interstrand crosslinking agents. Knockdown of MRG15 diminishes recruitment of PALB2, BRCA2, and RAD51 to DNA damage sites and reduces chromatin loading of PALB2 and BRCA2. | PMID:20332121, PMID:19553677 | Journal of cell science |
| 2009 | High | MRG15 directly interacts with PALB2 through an evolutionarily conserved region. Loss of the PALB2-MRG15 interaction does not impair RAD51 foci formation or mitomycin C sensitivity but leads to hyper-recombination, specifically increased gene conversion rates and elevated sister chromatid exchange frequencies, suggesting MRG15 suppresses aberrant recombination via PALB2. | PMID:19553677 | The Journal of biological chemistry |
| 2012 | High | PALB2 interacts directly with KEAP1, an oxidative stress sensor that normally binds and represses the NRF2 transcription factor. PALB2 shares a conserved ETGE-type KEAP1-binding motif with NRF2 and competes with NRF2 for KEAP1 binding. PALB2 promotes NRF2 nuclear accumulation and function, lowers cellular reactive oxygen species levels, and regulates the rate of NRF2 nuclear export following oxidative induction. | PMID:22331464 | Molecular and cellular biology |
| 2012 | High | The N-terminal coiled-coil motif of PALB2 mediates its self-association (homodimerization), and monomeric PALB2 shows higher efficiency to bind DNA and promote RAD51 filament formation. Overexpression of the PALB2 coiled-coil domain severely affects RAD51 loading at DNA damage sites by competing with the PALB2-BRCA1 interaction. Upon DNA damage, a switch from PALB2-PALB2 homodimerization to PALB2-BRCA1 interaction activates homologous recombination. | PMID:22941656 | Nucleic acids research |
| 2012 | High | The chromatin-association motif (ChAM), an evolutionarily conserved region of PALB2, is necessary and sufficient to mediate intrinsic chromatin binding of PALB2 in both unperturbed and damaged cells. ChAM is distinct from previously described DNA-binding regions. Deletion of ChAM decreases PALB2 and RAD51 accumulation at DNA damage sites and confers cellular hypersensitivity to mitomycin C. | PMID:22193777 | EMBO reports |
| 2012 | High | MDC1 and RNF8 function upstream of BRCA1 in a pathway that directs BRCA1-dependent localization of PALB2 to DNA double-strand breaks. Bypassing BRCA1 by fusing PALB2 to BRCA1 BRCT repeats restores RAD51 foci formation and HR repair in PALB2-deficient cells even when PALB2 cannot bind BRCA1, demonstrating the critical role of PALB2 localization. The BRCA1-PALB2 heterodimer (not the PALB2-PALB2 homodimer) mediates these HR responses. PALB2 localization requires MDC1, RNF8, RAP80, and Abraxas upstream of BRCA1. | PMID:23038782 | Journal of cell science |
| 2014 | High | Phosphorylated RPA (phosphorylated by Cdk2 and ATR during replication fork stalling) recruits PALB2 to stalled replication forks. RPA phosphorylation increased localization of PALB2 and BRCA2 to RPA-bound nuclear foci during replication stress, and phosphorylated RPA stimulated recruitment of PALB2 to single-stranded DNA in a cell-free system. Loss of PALB2 or expression of phosphorylation-defective RPA2 led to significant DNA damage after replication stress, exacerbated by PARP inhibitors. | PMID:25113031 | The Journal of cell biology |
| 2014 | High | PALB2 and BRCA2 interact with DNA polymerase η (Polη) and colocalize with Polη at stalled or collapsed replication forks after hydroxyurea treatment. PALB2 and BRCA2 are required to sustain the recruitment of Polη at blocked replication forks and stimulate Polη-dependent DNA synthesis on D-loop substrates, implicating PALB2 in the initiation of recombination-associated DNA synthesis. | PMID:24485656 | Cell reports |
| 2014 | Medium | PALB2 recruitment to DNA double-strand breaks is via a ubiquitin-dependent signaling pathway involving RAP80, Abraxas, and BRCA1. PALB2 also interacts with RAD51C and DNA polymerase η, forming a network of tumor suppressors required for homologous recombination. | PMID:24998779 | Biochimica et biophysica acta |
| 2016 | High | PALB2 is phosphorylated at three N-terminal S/Q sites by ATM and ATR kinases in response to ionizing radiation and hydroxyurea. A phospho-deficient PALB2 mutant is unable to support proper RAD51 foci formation and is less potent in homology-directed repair, whereas a phospho-mimicking PALB2 supports RAD51 foci formation. The PALB2-dependent checkpoint response is unaffected by phospho-deficient PALB2, revealing a separation of PALB2 functions. | PMID:27113759 | EMBO reports |
| 2015 | High | ATM phosphorylates PALB2 at Ser-157 and Ser-376 in response to ionizing radiation. Full phosphorylation also requires BRCA1, highlighting the importance of the BRCA1-PALB2 interaction in orchestrating DNA damage responses. Dysregulated PALB2 phosphorylation results in sustained activation of DNA damage responses. | PMID:26420486 | The Journal of biological chemistry |
| 2017 | High | RNF168 contains a PALB2-interacting domain (PID) that directly binds the WD40 domain of PALB2. PALB2 indirectly recognizes H2A ubiquitylation by physically associating with ubiquitin-bound RNF168. This RNF168-PALB2 interaction facilitates assembly of PALB2-containing HR complexes at DSBs in S/G2 cells, coupling PALB2-dependent homologous recombination to H2A ubiquitylation. | PMID:28240985 | eLife |
| 2017 | High | The PALB2-BRCA1 interaction (via PALB2 N-terminal coiled-coil domain residue L35P in patients) is required for breast cancer suppression. The L35P variant abrogates the PALB2-BRCA1 interaction and completely disables PALB2's ability to promote HR and confer resistance to platinum salts and PARP inhibitors. Multiple additional germline variants in the PALB2 N-terminal BRCA1-binding domain affect HR function to varying degrees. | PMID:28319063 | Oncogene |
| 2017 | High | PALB2 associates with active genes through MRG15, which recognizes histone H3 trimethylated at lysine 36 (H3K36me3) via the SETD2 methyltransferase. PALB2-MRG15 interaction mutations confer elevated sensitivity to the topoisomerase inhibitor camptothecin and increased DNA stress in gene bodies during replication. The steady-state presence of PALB2 at active genes via the SETD2/H3K36me3/MRG15 axis protects these regions during DNA replication. | PMID:28673974 | Proceedings of the National Academy of Sciences of the United States of America |
| 2018 | High | PALB2 connects BRCA1 and BRCA2 in the G2/M DNA damage checkpoint response. The BRCA1-PALB2 interaction contributes to checkpoint activation while the PALB2-BRCA2 complex is more critical for checkpoint maintenance. PALB2 checkpoint function is independent of CHK1 and CHK2 phosphorylation. Cells with disengaged BRCA1-PALB2 interaction show greatly increased chromosomal abnormalities after ionizing radiation due to combined defects in HR and checkpoint control. | PMID:30337689 | Oncogene |
| 2018 | High | The PALB2 N-terminal coiled-coil domain forms an antiparallel coiled-coil leucine zipper homodimer as determined by solution NMR spectroscopy. PALB2cc also forms heterodimers with the BRCA1 coiled-coil segment. Mutation of Leu24 in PALB2cc significantly reduces homodimer stability but has a more modest effect on PALB2cc/BRCA1cc heterodimer stability. Leu24 mutation leads to genomic instability and reduced cell viability after DNA double-strand break-inducing agents. | PMID:30289697 | Biochemistry |
| 2019 | High | PALB2 possesses a major DNA-binding site in its N-terminal DNA-binding domain (N-DBD). Mutations in this site reduce RAD51 foci formation and overall HDR efficiency in cells by ~50%. The N-DBD stimulates RAD51 recombinase function and also possesses strand exchange activity without RAD51, including the ability to use RNA substrates and stimulate inverse strand exchange. | PMID:31017574 | eLife |
| 2019 | Medium | USP22, a deubiquitinase, directly interacts with PALB2 through the C-terminal WD40 domain of PALB2. This interaction stimulates USP22 catalytic deubiquitinase activity in vitro. USP22 is required for BRCA2, PALB2, and RAD51 recruitment to DNA double-strand breaks, partly through USP22 stabilizing BRCA2 and PALB2 protein levels. | PMID:31685642 | Molecular cancer research : MCR |
| 2020 | High | In BRCA1-null/53BP1-depleted cells, PALB2 recruitment to resected DSBs is mediated by an interaction between PALB2's chromatin associated motif (ChAM) and the nucleosome acidic patch region. In 53BP1-expressing cells, this acidic patch is occupied by 53BP1's ubiquitin-directed recruitment (UDR) domain, blocking PALB2 access. Loss of 53BP1 in BRCA1-deficient cells restores PALB2 accrual at DSBs in a PALB2- and BRCA2-dependent manner, partially restoring HR. | PMID:32041954 | Nature communications |
| 2021 | High | RNF168-generated mono-ubiquitinated H2A (mUb-H2A) recruits BARD1 through a BRCT domain ubiquitin-dependent recruitment motif (BUDR). Subsequently, BARD1-BRCA1 accumulate PALB2-RAD51 at DNA breaks via the coiled-coil domain-mediated BRCA1-PALB2 interaction. Epistatic analysis in mice harboring a Brca1CC mutation (blocking Brca1-Palb2 interaction) combined with Rnf168 loss disrupted development and reduced Palb2-Rad51 localization. | PMID:34408138 | Nature communications |
| 2021 | Medium | BRCA1 and RNAi factors promote sdRNA (single-stranded DNA-damage-associated small RNA)-mediated DNA repair at transcriptional termination pause sites via the PALB2-RAD52 complex. sdRNAs promote DNA repair driven by PALB2-RAD52 at R-loop-rich sites with single-stranded DNA breaks, operating in both quiescent (G0) and proliferating cells. | PMID:33536619 | Nature |
| 2022 | Medium | Disruption of the BRCA1-PALB2 interaction causes persistent high levels of DNA damage in HCC cells, leading to activation of the cGAS-STING signaling pathway in both malignant hepatocytes and M1 macrophages. The activated cGAS-STING pathway induces PD-L1 expression via STING-IRF3-STAT1, causing immunosuppression, while also recruiting T lymphocytes through the STING-IRF3 pathway. | PMID:35006619 | Hepatology (Baltimore, Md.) |
| 2014 | High | Disruption of the BRCA1-PALB2 interaction in mice (hypomorphic Palb2 allele expressing BRCA1-binding-deficient PALB2) causes Fanconi anemia-like phenotype including hypersensitivity and chromosomal breakage with mitomycin C, reduced male fertility due to impaired meiosis, increased germ cell apoptosis, and significant defect in sex chromosome synapsis in meiocytes. | PMID:25016020 | The Journal of biological chemistry |
| 2016 | High | The BRCA2-PALB2 interaction (mediated by the N-terminal region of BRCA2) is essential for maintaining genomic integrity. Knock-in mice carrying Brca2G25R (a single amino acid change disrupting BRCA2-PALB2 interaction) show defects in body size, fertility, meiotic progression, genome stability, and increased tumor susceptibility. Severity increased with decreasing interaction, demonstrating that BRCA1-PALB2-BRCA2 complex formation and BRCA2's DNA-binding domain have overlapping roles in BRCA2 recruitment to DNA damage sites. | PMID:27490902 | PLoS genetics |
| 2013 | High | The N-terminal segment of BRCA2 (PALB2-binding domain) and the DNA-binding domain (DBD) of BRCA2 play substantially overlapping roles in BRCA2 function. Loss of both domains (BRCA2ΔN+ΔDBD) phenocopies BRCA2-null cells, while single deletions show moderate phenotypes. Formation of the BRCA1-PALB2-BRCA2 complex and the DBD are both required for efficient BRCA2 recruitment to DNA damage sites. | PMID:24285729 | Cancer research |
| 2014 | Medium | BRCA1 and PALB2 co-occupy chromatin at actively transcribed genes genome-wide and are required for transcriptional responsiveness to NF-κB and retinoic acid. PALB2 plays a role in transcriptional co-activation in breast epithelial cells. | PMID:24591564 | The EMBO journal |
| 2010 | High | Homozygous deletion of Palb2 in mice causes embryonic lethality at E9.5 with defective mesoderm differentiation after gastrulation and increased p21 expression. Palb2-/- blastocysts show growth defect in vitro. The phenotype resembles Brca1 and Brca2 knockout mice, supporting the in vivo functional relationship of PALB2 with BRCA1 and BRCA2. | PMID:20484223 | Human molecular genetics |
| 2020 | High | Ablation of the Brca1-Palb2 interaction in mice (Brca1L1363P knock-in) causes Fanconi anemia-like phenotypes: hypersensitivity to DNA-damaging agents, failure to recruit Rad51 to DSBs, growth retardation, hyperpigmentation, skeletal abnormalities, male/female infertility, macrocytosis, and death from bone marrow failure or lymphoblastic lymphoma/leukemia. | PMID:32732220 | Cancer research |
| 2022 | High | Pentagalloylglucose (PGG) disrupts the PALB2-BRCA2 protein-protein interaction by occupying a binding groove in the WD40 domain of PALB2 (tips of the fourth and fifth blades). PGG reduces BRCA2 recruitment to DNA damage sites and inhibits RAD51 foci formation, suppressing homologous recombination repair, and sensitizes cancer cells to PARP inhibitors and radiotherapy. | PMID:35926819 | Cancer letters |
| 2019 | High | Functional analysis of 84 PALB2 missense variants of uncertain significance identified four variants (L24S, L35P, I944N, L1070P) that disrupt PALB2-mediated homology-directed repair. L24S and L35P disrupt BRCA1-PALB2 protein complexes; I944N causes protein instability; both I944N and L1070P mislocalize PALB2 to the cytoplasm. All four variants confer sensitivity to cisplatin and PARP inhibitors and reduce RAD51 foci formation. | PMID:31636395 | Genetics in medicine : official journal of the American College of Medical Genetics |
| 2019 | High | Functional analysis of 48 PALB2 VUS using cDNA-based HR rescue in Palb2 knockout mouse ES cells identified three VUS in the coiled-coil domain that abrogate BRCA1 interaction and several VUS in the WD40 domain that dramatically reduce protein stability. | PMID:31757951 | Nature communications |
| 2022 | Medium | Loss of PALB2 in prostate cancer cell lines leads to decreased homologous recombination function (measured by loss of radiation-induced RAD51 foci and HR reporter assay) and significantly increased sensitivity to PARP inhibitors olaparib and rucaparib. | PMID:35768576 | NPJ precision oncology |

## Citations

- PMID:17287723
- PMID:19268590
- PMID:19553677
- PMID:19584259
- PMID:20332121
- PMID:20484223
- PMID:22193777
- PMID:22331464
- PMID:22941656
- PMID:23038782
- PMID:24285729
- PMID:24485656
- PMID:24591564
- PMID:24998779
- PMID:25016020
- PMID:25113031
- PMID:26420486
- PMID:27113759
- PMID:27490902
- PMID:28240985
- PMID:28319063
- PMID:28673974
- PMID:30289697
- PMID:30337689
- PMID:31017574
- PMID:31636395
- PMID:31685642
- PMID:31757951
- PMID:32041954
- PMID:32732220
- PMID:33536619
- PMID:34408138
- PMID:35006619
- PMID:35768576
- PMID:35926819
