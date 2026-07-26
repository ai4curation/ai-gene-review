---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/BRCA2
affinage_run_date: 2026-06-09T22:02:45
uniprot_accession: P51587
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 27
citation_count: 27
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for BRCA2 (human)

## Current model (mechanistic narrative)

BRCA2 is a central mediator of homologous recombination (HR) that loads and stabilizes the RAD51 recombinase on resected DNA to drive error-free repair of double-strand breaks, with loss of function producing chromosomal instability, checkpoint defects, and crosslinker hypersensitivity [PMID:9660919, PMID:11756561]. A large C-terminal domain binds single-stranded DNA through three OB folds (with an HTH motif implicated in dsDNA binding) and stimulates RAD51-mediated recombination in vitro [PMID:12228710]. Full-length BRCA2 binds RAD51 and selectively assembles it onto ssDNA over dsDNA, displaces RPA, and stabilizes the resulting filament by blocking RAD51 ATP hydrolysis [PMID:20729832]; at the molecular level it accelerates RAD51 nucleation on RPA-coated ssDNA to rates approaching those on naked ssDNA, overcoming the kinetic barrier RPA imposes [PMID:36976771]. The eight BRC repeats engage RAD51 non-equivalently to control filament assembly versus disruption [PMID:15937124], while the C-terminal TR2 motif braces adjacent RAD51 protomers across the filament interface via an acidic-patch contact [PMID:37919288]. BRCA2 is brought to damage sites through the BRCA1–PALB2 axis, which places BRCA1 upstream of BRCA2 in HR [PMID:19268590], and through FANCD2/Fanconi-pathway interactions that promote its chromatin loading [PMID:15199141, PMID:12915460]. Beyond canonical HR, BRCA2 protects reversed replication forks from MRE11-, PTIP-, and RAD52-mediated nucleolytic degradation by assembling stable RAD51 filaments on regressed arms [PMID:29038466], and it limits DNA:RNA hybrid (R-loop) accumulation at breaks and at G/C-rich chromatin by recruiting RNase H2 in S/G2 phase [PMID:30560944, PMID:35715464]. Its activity is governed by phosphoregulation and proteostasis: ATM/ATR phosphorylation recruits PP2A-B56 to promote RAD51 filament formation [PMID:34593815], a PLK1-T207 phosphorylation event builds a PP2A–BUBR1 complex required for mitotic chromosome alignment [PMID:32286328], DSS1 and ssDNA control BRCA2 oligomeric state [PMID:32609828], and reactive metabolites such as formaldehyde and methylglyoxal trigger its proteasomal degradation to cause transient functional haploinsufficiency and mutagenesis [PMID:28575672, PMID:38608703]. BRCA2 additionally functions as a meiotic recombination mediator, stimulating DMC1 strand exchange through DMC1-preferring BRC repeats and acting within meiosis-specific complexes [PMID:26976601, PMID:31242413, PMID:32609828].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0003677 DNA binding, GO:0140096 catalytic activity, acting on a protein, GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005634 nucleus, GO:0005694 chromosome, GO:0000228 nuclear chromosome
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-69306 DNA Replication, R-HSA-1640170 Cell Cycle, R-HSA-1474165 Reproduction
- **partners:** RAD51, DMC1, PALB2, DSS1, FANCD2, RNASEH2, HSF2BP, PLK1
- **complexes:** BRCA1-PALB2-BRCA2, BRCA2-PP2A-B56, BRCA2-MEILB2-BRME1, BRCA2-PLK1-PP2A-BUBR1

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2002 | High | Crystal structure of a ~90 kDa BRCA2 C-terminal domain bound to DSS1 reveals three OB folds and a helix-turn-helix (HTH) motif; the domain binds single-stranded DNA (ssDNA) via the OB folds; the HTH motif is implicated in dsDNA binding; and this BRCA2 domain stimulates RAD51-mediated recombination in vitro. | PMID:12228710 | Science |
| 2010 | High | Full-length purified human BRCA2 binds RAD51 and promotes assembly of RAD51 onto ssDNA over dsDNA, displaces RPA from ssDNA, and stabilizes RAD51-ssDNA filaments by blocking ATP hydrolysis; BRCA2 does not anneal RPA-coated ssDNA, indicating it does not function in ssDNA-annealing repair pathways. | PMID:20729832 | Nature |
| 2023 | High | Cryo-EM structure and structure-guided mutagenesis reveal that the BRCA2 TR2 motif at the C-terminus binds across the protomer interface of the RAD51 nucleoprotein filament, acting as a molecular brace for adjacent RAD51 molecules and stabilizing the filament; TR2 targets an acidic-patch motif on human RAD51. | PMID:37919288 | Nature Communications |
| 2023 | High | Single-molecule visualization shows that BRCA2 accelerates RAD51 nucleation on RPA-coated ssDNA to rates approaching association with naked ssDNA, overcoming the kinetic barrier imposed by RPA; a dimer of RAD51 is minimally required for spontaneous nucleation; BRCA2 can chaperone a preassembled short RAD51 filament onto RPA-coated ssDNA. | PMID:36976771 | Proceedings of the National Academy of Sciences |
| 2005 | Medium | BRCA2 BRC repeats (BRC3 and BRC4) bind RAD51-DNA nucleoprotein filaments at low molar ratios, with BRC3 contacting the N-terminal domain of RAD51 and BRC4 contacting the nucleotide-binding core; at high concentrations the BRC repeats disrupt filaments. The eight BRC repeats are non-equivalent in their mode of RAD51 interaction. | PMID:15937124 | Proceedings of the National Academy of Sciences |
| 2016 | High | BRCA2 BRC repeats interact directly with the meiosis-specific recombinase DMC1; BRC1-3 bind RAD51 preferentially while BRC6-8 bind DMC1 preferentially; individual BRC repeats (except BRC4) stimulate DMC1-ssDNA complex formation; full-length BRCA2 stimulates DMC1-mediated DNA strand exchange between RPA-ssDNA and duplex DNA, identifying BRCA2 as a mediator of DMC1 recombination. | PMID:26976601 | Proceedings of the National Academy of Sciences |
| 1998 | Medium | BRCA2 is a ~460 kDa nuclear phosphoprotein that forms in vivo complexes with both p53 and RAD51; exogenous BRCA2 expression inhibits p53 transcriptional activity, and RAD51 co-expression enhances this inhibitory effect. | PMID:9811893 | Proceedings of the National Academy of Sciences |
| 1998 | High | Cells with a targeted truncation of murine Brca2 show proliferative impediment, G1 and G2/M arrest with elevated p53/p21, hypersensitivity to UV and MMS, spontaneous chromosomal breaks and aberrant chromatid exchanges, establishing Brca2 function in DNA repair. | PMID:9660919 | Molecular Cell |
| 2009 | High | BRCA1 associates with BRCA2 through PALB2/FANCN; in PALB2-deficient cells the BRCA1-BRCA2 interaction is abrogated; BRCA1 promotes concentration of PALB2 and BRCA2 at DNA-damage sites; the BRCA1-PALB2 interaction is required for homologous recombination repair, placing BRCA1 upstream of BRCA2 in the DNA-damage response. | PMID:19268590 | Current Biology |
| 2004 | High | Monoubiquitination of FANCD2 (activated by DNA damage) is required for targeting FANCD2 to chromatin where it interacts with BRCA2 and promotes BRCA2 chromatin loading; the C-terminus of BRCA2 is required for functional colocalization of BRCA2 and FANCD2 in chromatin complexes. | PMID:15199141 | Molecular and Cellular Biology |
| 2003 | Medium | FANCG directly binds BRCA2 at two separate sites flanking the BRC repeats (by yeast two-hybrid); FANCG co-immunoprecipitates with BRCA2 from human cells and co-localizes with BRCA2 and RAD51 in nuclear foci after mitomycin C treatment. | PMID:12915460 | Human Molecular Genetics |
| 2003 | Medium | EMSY protein binds BRCA2 within an exon 3-encoded region deleted in cancer, silences the transcriptional activation potential of BRCA2 exon 3, associates with chromatin regulators HP1β and BS69, and localizes to sites of DNA repair following DNA damage. | PMID:14651845 | Cell |
| 2002 | High | BRCA2 deficiency in XRCC11-complementation group hamster cells (V-C8) causes radioresistant DNA synthesis (checkpoint defect), extreme sensitivity to interstrand crosslinking agents, chromosomal instability, abnormal centrosomes, and reduced nuclear localization of RAD51. | PMID:11756561 | Molecular and Cellular Biology |
| 2017 | High | Reversed replication forks are entry points for nucleolytic fork degradation in BRCA2-defective cells; MRE11, PTIP, and RAD52 promote stalled fork degradation and chromosomal breakage in BRCA2-deficient cells; impairing fork reversal prevents fork degradation but increases chromosomal breakage; BRCA2 assembles stable RAD51 nucleofilaments on regressed arms to protect them from degradation. | PMID:29038466 | Nature Communications |
| 2020 | High | PLK1 phosphorylates BRCA2 at a conserved T207 site in mitosis, creating a PLK1 docking site; BRCA2 bound to PLK1 forms a complex with phosphatase PP2A and phosphorylated BUBR1; breast cancer variants S206C and T207A reduce BRCA2-PLK1 binding, destabilize this tetrameric complex, and cause unstable kinetochore-microtubule interactions, misaligned chromosomes, and aneuploidy. | PMID:32286328 | Nature Communications |
| 2021 | High | ATM and ATR kinases phosphorylate a conserved region in BRCA2 in response to DSBs; these phosphorylations recruit the phosphatase PP2A-B56 to BRCA2 via a conserved binding motif; the BRCA2-PP2A-B56 complex is required for efficient RAD51 filament formation at DNA damage sites and HR-mediated repair; cancer-associated BRCA2 mutations that deregulate this interaction sensitize cells to PARP inhibition. | PMID:34593815 | Nature Communications |
| 2018 | Medium | BRCA2 directly interacts with RNase H2 and mediates RNase H2 localization to DSBs specifically in S/G2 phase, controlling DNA:RNA hybrid (R-loop) levels at DSBs; damage-induced lncRNAs contribute to recruitment of BRCA1, BRCA2, and RAD51 to DSBs without affecting DNA-end resection. | PMID:30560944 | Nature Communications |
| 2017 | High | Formaldehyde selectively depletes BRCA2 via proteasomal degradation; heterozygous BRCA2 truncations sensitize cells to BRCA2 haploinsufficiency induced by formaldehyde or acetaldehyde, causing replication fork stalling, chromosomal aberrations, and R-loop accumulation; Ribonuclease H1 ameliorates these replication defects, linking BRCA2 inactivation to spontaneous mutagenesis via aberrant RNA-DNA hybrids. | PMID:28575672 | Cell |
| 2019 | Medium | HSF2BP interacts with a specific 68-amino acid region of BRCA2 (Gly2270–Thr2337, between BRC repeats and the DNA-binding domain) via armadillo repeats; this interaction is constitutive in mouse embryonic stem cells; Hsf2bp knockout mice are male infertile due to a severe HR defect during spermatogenesis. | PMID:31242413 | Cell Reports |
| 2020 | Medium | BRCA2 forms a ternary complex with MEILB2 and BRME1 in meiosis; BRME1 stabilizes MEILB2 by preventing its self-association; BRCA2 binds the C-terminus of MEILB2; Brme1 knockout mice show defects in DSB repair, homolog synapsis, and crossover formation; ectopic expression of MEILB2-BRME1 in somatic cancer cells impairs mitotic HR. | PMID:32345962 | Nature Communications |
| 2020 | Medium | DSS1 and ssDNA counteract BRCA2 oligomerization; three self-interacting regions and two types of self-association (N-to-C and N-to-N terminal) were identified; the N-to-C interaction is sensitive to DSS1 and ssDNA, while the N-to-N interaction is modulated by ssDNA; defining a regulatory mechanism for BRCA2 oligomeric state. | PMID:32609828 | Nucleic Acids Research |
| 2022 | Medium | ZFP281 interacts with BRCA2 and is required for BRCA2 recruitment to bivalent chromatin (with PRC2); depletion of ZFP281 or BRCA2 causes R-loop accumulation over bivalent regions and impairs DNA replication progression; ZFP281 cooperates with BRCA2 to prevent persistent R-loops at G/C-rich promoters. | PMID:35715464 | Nature Communications |
| 2024 | Medium | The glycolytic metabolite methylglyoxal (MGO) triggers BRCA2 proteolysis, transiently disabling BRCA2 tumor suppressive functions in DNA repair and replication and causing functional haploinsufficiency; this generates a cancer-associated mutational signature (SBS) in non-malignant mammary cells without biallelic BRCA2 inactivation; BRCA2 monoallelic mutations predispose to these changes. | PMID:38608703 | Cell |
| 2008 | Medium | PARP-1 binds a silencer region (-582 to -516) of the BRCA2 promoter in vitro and in vivo and down-regulates BRCA2 expression; PARP-1 inhibitors or PARP-1 siRNA increase endogenous BRCA2 expression; inhibition of PARP-1 activity reduces histone H3K9 acetylation and blocks PARP-1 binding to the BRCA2 promoter. | PMID:18990703 | Journal of Biological Chemistry |
| 2005 | Medium | BRCA2 binds and stabilizes MAGE-D1 protein; BRCA2 and MAGE-D1 synergistically suppress cell proliferation independently of the p53 pathway; MAGE-D1 expression is required for BRCA2-mediated suppression of cell proliferation (shown by RNAi), establishing MAGE-D1 as a downstream effector of BRCA2 in growth suppression. | PMID:15930293 | Cancer Research |
| 2006 | Medium | FANCC gene disruption in brca2ΔCTD (C-terminal domain truncation) cells reveals epistasis between FANCC and the BRCA2 CTD for X-ray sensitivity; however, combined fancc/brca2ΔCTD cells show additive sensitivity to cisplatin and increased MMC-induced chromosomal aberrations relative to either single mutant, indicating the FA pathway has a CTD-independent role in interstrand crosslink repair separate from BRCA2-RAD51-mediated HR. | PMID:16687415 | Journal of Biological Chemistry |
| 2017 | High | In non-transformed human mammary epithelial cells, BRCA2 loss causes replication stress associated with DNA under-replication, leading to mitotic abnormalities, 53BP1 nuclear body formation in the subsequent G1 phase, and G1 arrest; the HR function of BRCA2 (not stalled-fork protection) is primarily responsible for supporting cell viability in this context. | PMID:28904335 | Nature Communications |

## Citations

- PMID:11756561
- PMID:12228710
- PMID:12915460
- PMID:14651845
- PMID:15199141
- PMID:15930293
- PMID:15937124
- PMID:16687415
- PMID:18990703
- PMID:19268590
- PMID:20729832
- PMID:26976601
- PMID:28575672
- PMID:28904335
- PMID:29038466
- PMID:30560944
- PMID:31242413
- PMID:32286328
- PMID:32345962
- PMID:32609828
- PMID:34593815
- PMID:35715464
- PMID:36976771
- PMID:37919288
- PMID:38608703
- PMID:9660919
- PMID:9811893
