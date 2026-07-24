---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/FANCD2
affinage_run_date: 2026-06-09T23:54:43
uniprot_accession: Q9BXW9
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 60
citation_count: 60
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for FANCD2 (human)

## Current model (mechanistic narrative)

FANCD2 is the central effector of the Fanconi anemia (FA) DNA repair pathway, originally identified by positional cloning as the FA-D2 gene product whose reintroduction complements mitomycin C sensitivity in patient cells [PMID:11239453]. Its activation is governed by a regulated cycle of post-translational modification: ATR/ATM kinases phosphorylate FANCD2 (T691, S717) and its partner FANCI, priming the complex [PMID:16943440, PMID:36050501], after which the FA core complex — minimally the FANCB-FANCL-FAAP100 module using UBE2T as E2 — monoubiquitinates FANCD2 on K561 during S phase and in response to DNA damage [PMID:12239151, PMID:24905007, PMID:31873223]. This modification drives translocation from soluble nucleoplasm to chromatin, where FANCD2 forms damage-induced foci with BRCA1 and RAD51 [PMID:12239151, PMID:15454491]. FANCD2 functions as an obligate heterodimer with its paralog FANCI, and DNA engagement by the ID2 complex is required for efficient monoubiquitination [PMID:17412408, PMID:22287633, PMID:24623813]. Structural studies establish that the unmodified ID2 complex is recruited to DNA and that monoubiquitination triggers a conformational closure into a sliding clamp that encircles dsDNA, with ubiquitin acting as a molecular pin at the I-D interface; the clamp diffuses on duplex DNA and stalls at ssDNA-dsDNA junctions found at stalled replication forks [PMID:21764741, PMID:32066963, PMID:32510829, PMID:39085614]. Activated FANCD2 coordinates interstitial crosslink repair by recruiting the XPF-ERCC1/SLX4 nucleases for unhooking incisions, FAN1 and CtIP for end processing and resection, and by stabilizing RAD51 filaments and mediating strand exchange while protecting DNA ends from DNA2, MRE11, and EXO1 nucleases [PMID:20603015, PMID:24726325, PMID:24794430, PMID:24794434, PMID:27694619, PMID:37526271]. The cycle is reversed by USP1-UAF1, which deubiquitinates K561 in a DNA- and FANCI-contact-dependent manner requiring a FANCD2-specific sequence in the USP1 N-terminus [PMID:18082605, PMID:31253762, PMID:33795880]. Beyond crosslink repair, FANCD2 — including its non-ubiquitinated form — restrains replication fork progression at common fragile sites and in BRCA1/2-deficient cells where its loss is synthetic lethal, suppresses R-loop accumulation by recruiting RNA-processing factors and collaborating with SRSF1 for mRNA export, activates TAp63 transcription to suppress skin carcinogenesis, and localizes to mitochondria where it supports homeostasis through ATAD3 and TUFM [PMID:23806336, PMID:26797144, PMID:27768874, PMID:27264184, PMID:28378742, PMID:30431240, PMID:38165804].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0003677 DNA binding, GO:0003723 RNA binding, GO:0031386 protein tag activity, GO:0140096 catalytic activity, acting on a protein, GO:0060090 molecular adaptor activity, GO:0140110 transcription regulator activity
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome, GO:0005654 nucleoplasm, GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-69306 DNA Replication, R-HSA-1640170 Cell Cycle, R-HSA-8953854 Metabolism of RNA
- **partners:** FANCI, FANCL, USP1, UAF1, FAN1, CTIP, RAD51, BRCA2
- **complexes:** FANCI-FANCD2 (ID2) complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2001 | High | FANCD2 encodes a novel 1451 amino acid nuclear protein with two isoforms; retroviral transduction of FANCD2 cDNA into FA-D2 cells complemented MMC sensitivity, establishing it as the FA-D2 gene product functioning in DNA crosslink repair. | PMID:11239453 | Molecular cell |
| 2002 | High | FANCD2 undergoes monoubiquitination on K561 during S phase and in response to DNA damage; monoubiquitinated FANCD2 colocalizes with BRCA1 and RAD51 in S-phase nuclear foci, and this monoubiquitination is required for normal cell-cycle progression after MMC treatment. | PMID:12239151 | Blood |
| 2002 | High | FANCD2 and NBS1 colocalize in subnuclear foci after MMC treatment; ionizing radiation activates ATM- and NBS1-dependent phosphorylation of FANCD2, establishing an S-phase checkpoint function, and NBS1 cells are hypersensitive to MMC. | PMID:12447395 | Nature cell biology |
| 2003 | High | BRCA1/BARD1 complex can reconstitute FANCD2 monoubiquitination in vitro, but siRNA knockdown of BRCA1 or ablation of BRCA1/BARD1 RING finger domains in DT40 cells does not impair FANCD2 ubiquitination; BRCA1 affects chromatin targeting of FANCD2 but is not the essential E3 ligase for FANCD2 monoubiquitination. | PMID:12887909 | Molecular cell |
| 2003 | Medium | Menin (MEN1 product) specifically interacts with FANCD2, and this interaction is enhanced by gamma-irradiation; loss of menin in mouse embryonic fibroblasts increases sensitivity to DNA damage, placing menin in the FANCD2-dependent DNA repair pathway. | PMID:12874027 | Cancer research |
| 2004 | High | ATR kinase and RPA1 are required for efficient FANCD2 monoubiquitination; deficiency of ATR (Seckel syndrome cells or siRNA silencing) results in radial chromosomes after MMC treatment, mimicking FA chromosome instability. | PMID:15314022 | Genes & development |
| 2004 | Medium | FANCD2 directly interacts with BRCA2 via a conserved C-terminal site also bound by FANCG/XRCC9; this interaction was confirmed by co-immunoprecipitation from human and hamster cell extracts. FANCD2 focus formation is independent of BRCA2. FANCD2 colocalizes with RAD51 after MMC or hydroxyurea treatment and very tightly with PCNA after hydroxyurea. | PMID:15115758 | Human molecular genetics |
| 2004 | High | Monoubiquitination of FANCD2 on K561 is required for its translocation from the soluble nuclear compartment to chromatin; the C-terminal residue D1428 (encoded by exon 44) is independently required for functional complementation of FA-D2 cells even when monoubiquitination and chromatin binding are intact. | PMID:15454491 | Blood |
| 2004 | High | In Xenopus egg extracts, linear and branched double-stranded DNA (but not single-stranded or Y-shaped DNA) rapidly triggers FANCD2 monoubiquitination in an FA core complex-dependent but ATRIP-independent manner, and monoubiquitinated FANCD2 associates with these DNA structures. | PMID:17420278 | Molecular and cellular biology |
| 2005 | High | FANCD2-disrupted DT40 cells are defective in HR-mediated DSB repair and immunoglobulin gene conversion; they show increased sister chromatid exchange and intact Rad51 foci, indicating FANCD2 promotes a subpathway of HR that mediates gene conversion via a mechanism avoiding crossovers. | PMID:15601828 | Molecular and cellular biology |
| 2006 | High | ATR phosphorylates FANCD2 on T691 and S717; these phosphorylations promote FANCD2 monoubiquitination and enhance cellular resistance to DNA crosslinking agents and intra-S-phase checkpoint establishment. ATM also phosphorylates these sites in response to IR. | PMID:16943440 | Molecular and cellular biology |
| 2006 | Medium | Drosophila FANCD2 and FANCL function in a linear pathway in which FANCL is necessary for FANCD2 monoubiquitination; FANCD2 mutants show defects in the IR-inducible S-phase checkpoint and elevated mutation rates after nitrogen mustard, establishing conservation of FA pathway function. | PMID:16860002 | DNA repair |
| 2007 | High | FANCI is a monoubiquitinated paralog of FANCD2 that forms the FANCI-FANCD2 (ID) complex; the two proteins associate and localize together to chromatin in response to DNA damage. Monoubiquitination of each protein is important for maintaining ubiquitin on the other (dual ubiquitin-locking mechanism), and FANCI mutation causes FA complementation group I. | PMID:17412408 | Cell |
| 2007 | High | USP1 ablation in DT40 cells results in constitutively chromatin-bound monoubiquitinated FANCD2 and DNA crosslinker sensitivity, demonstrating that FANCD2 deubiquitination (not just ubiquitination) is required for efficient DNA crosslink repair; persistent PCNA monoubiquitination has negligible impact on DNA repair. | PMID:18082605 | Molecular cell |
| 2007 | Medium | The FA core complex and UBE2T are independently recruited to chromatin; E3 ligase activity is regulated by DNA damage-induced chromatin localization of the complex, not by complex assembly; FANCD2 accesses chromatin independently of the FA core complex. | PMID:17938197 | Molecular and cellular biology |
| 2007 | High | FANCL interacts with FANCD2 via its PHD domain (yeast two-hybrid and Co-IP); FANCL is required for FANCD2 monoubiquitination and focus formation; FANCL and monoubiquitination of FANCD2 K563 are both required for HR repair of I-SceI-induced DSBs at equivalent quantitative levels. | PMID:17352736 | Genes to cells |
| 2008 | Medium | FANCG phosphorylation on serine 7 is required for co-precipitation of a BRCA2-FANCD2-FANCG-XRCC3 (D1-D2-G-X3) complex; direct BRCA2-FANCD2 interaction requires FANCG and its S7 phosphorylation; FANCG and XRCC3 are epistatic for sensitivity to DNA crosslinking agents in DT40 cells. | PMID:18212739 | Oncogene |
| 2009 | High | FANCI directly binds DNA and forms a stable complex with FANCD2 via FANCI's C-terminal region (aa 1001–1328); the FANCI-FANCD2 complex preferentially binds branched DNA structures compared to each protein alone, suggesting recognition of damaged replication forks. | PMID:19561358 | The Journal of biological chemistry |
| 2009 | Medium | Inhibition of MRE11, NBS1, or RAD50 destabilizes FANCD2; purified FANCD2 is a ring-like particle by EM that preferentially binds ssDNA; inhibition of MRE11 nuclease activity decreases FANCD2 foci, indicating MRN complex is a crucial regulator of FANCD2 stability and promotes FANCD2 binding to ssDNA at MRN-processed DSBs. | PMID:19609304 | The EMBO journal |
| 2009 | Medium | In Xenopus egg extracts, FANCM chromatin binding and DNA damage-induced phosphorylation are controlled in part by the downstream FA pathway protein FANCD2, as well as by ATR and ATM kinases. | PMID:19633289 | The Journal of biological chemistry |
| 2010 | High | Monoubiquitinated FANCD2 recruits FAN1 (KIAA1018) to sites of DNA damage; FAN1 is a nuclease with 5' flap endonuclease and 5' exonuclease activities mediated by a VRR_nuc domain; FAN1 depletion causes ICL hypersensitivity and genome instability. | PMID:20603015 | Cell |
| 2011 | High | Crystal structure of the ~300 kDa FANCI-FANCD2 (ID) complex at 3.4 Å reveals that monoubiquitination and regulatory phosphorylation sites map to the I-D interface, suggesting these modifications occur on monomeric proteins or an opened complex and may stabilize heterodimerization. Each protein has binding sites for both ssDNA and dsDNA, suggesting the ID complex recognizes DNA structures at replication fork-ICL encounters. | PMID:21764741 | Science |
| 2011 | Medium | RAD18 binds FANCD2 (RING domain-dependent) and is required for efficient monoubiquitylation and chromatin localization of both FANCD2 and FANCI; RAD18 knockout cells show delayed FANCD2 foci formation and ICL sensitivity. FANCD2 ubiquitylation is normal in PCNA ubiquitylation-resistant cells, indicating RAD18 acts independently of PCNA ubiquitylation. | PMID:21355096 | Blood |
| 2012 | High | Various forms of DNA (ssDNA, dsDNA, branched DNA) robustly stimulate FANCD2 monoubiquitylation in vitro up to near-in-vivo levels; this DNA stimulation strictly requires FANCI and FANCI's DNA-binding activity, demonstrating that FANCD2 monoubiquitination occurs within the FANCI-FANCD2 complex and requires DNA engagement. | PMID:22287633 | Nucleic acids research |
| 2012 | Medium | FANCD2 contains a CUE ubiquitin-binding domain that mediates noncovalent ubiquitin binding in vitro; the CUE domain is required for interaction with FANCI, chromatin retention of monoubiquitinated FANCD2 and FANCI, and efficient ICL repair, suggesting FANCD2 CUE domain noncovalently binds the ubiquitin on FANCI to stabilize the complex on chromatin. | PMID:22855611 | Blood |
| 2013 | High | FANCD2 directly interacts with MCM2-MCM7 replicative helicase; ATR signaling promotes transient association of endogenous FANCD2 with MCM2-7 independently of FANCD2 monoubiquitination; FANCD2 restrains DNA synthesis under nucleotide-limiting conditions and prevents ssDNA accumulation and senescence entry. | PMID:23993743 | Molecular cell |
| 2013 | High | Monoubiquitinated FANCD2 activates transcription of the tumor suppressor TAp63, promoting cellular senescence and blocking skin tumorigenesis; Usp1-deficient mice with elevated FANCD2-Ub are resistant to skin tumors while Fancd2-deficient mice are prone to Ras-driven skin carcinogenesis. | PMID:23806336 | Molecular cell |
| 2013 | Medium | mTOR regulates FANCD2 expression via NF-κB; mTOR deficiency or inhibition increases NF-κB nuclear translocation, enhancing NF-κB binding to the FANCD2 promoter to suppress FANCD2 expression; exogenous FANCD2 rescues the DNA damage response defect in mTOR-inhibited cells. | PMID:23538752 | Leukemia |
| 2014 | High | Biochemical reconstitution of FANCD2 monoubiquitination using purified native avian FA core complex demonstrates that FANCL must be embedded in the complex for maximal activity and site specificity; a minimal subcomplex of FANCB-FANCL-FAAP100 is sufficient as the monoubiquitination module; cells defective in other subunits retain residual activity. | PMID:24905007 | Molecular cell |
| 2014 | High | XPF-ERCC1 cooperates with SLX4/FANCP to perform the DNA unhooking incisions during replication-coupled ICL repair in Xenopus egg extracts; efficient recruitment of XPF-ERCC1 and SLX4 to the ICL depends on FANCD2 and its ubiquitylation. | PMID:24726325 | Molecular cell |
| 2014 | High | CtIP directly interacts with FANCD2; monoubiquitination of FANCD2 and CtIP residues 166-273 are both required for the FANCD2-CtIP interaction and MMC-induced CtIP foci; FANCD2 and CtIP cooperate to promote RPA2 hyperphosphorylation accompanying DNA end resection at ICL-induced DSBs. | PMID:24794430, PMID:24794434 | Cell reports |
| 2014 | High | Monoubiquitinated FANCD2 tethers CtIP to damaged chromatin; CtIP mutants defective in FANCD2 binding fail to associate with damaged chromatin, leading to increased non-homologous end-joining and ICL hypersensitivity; CtIP depletion aggravates genomic instability in FANCD2-deficient cells. | PMID:24794434, PMID:24794430 | Cell reports |
| 2014 | Medium | CtIP is recruited by FANCD2 to stalled replication forks on chromatin independently of FANCD2 monoubiquitination; CtIP cooperates with FANCD2 to promote fork restart and suppress new origin firing in a BRCA1-dependent manner. | PMID:24556218 | Human molecular genetics |
| 2014 | High | Regulation of FANCD2 and FANCI monoubiquitination by DNA: duplex or branched DNA strongly stimulates FANCD2 monoubiquitination in the ID2 complex, but unstructured ssDNA or chromatinized DNA is not effective; FANCI DNA-binding mutants compromise FANCD2 ubiquitination; FANCL interaction with the ID2 complex is indispensable for E3 ligase efficacy. | PMID:24623813 | Nucleic acids research |
| 2015 | Medium | UHRF1 acts upstream of FANCD2 in the FA pathway: UHRF1 directly binds ICLs in vitro and in vivo, is rapidly recruited to chromatin before FANCD2, and its knockdown drastically reduces FANCD2 foci formation, indicating UHRF1 senses ICLs and recruits FANCD2. | PMID:25801034 | Cell reports |
| 2015 | Medium | FANCD2 promotes replication fork restart and suppresses new origin firing independently of FA core complex-mediated monoubiquitination after aphidicolin treatment; FANCJ and BRCA2 share this replication fork recovery role with non-ubiquitinated FANCD2, independently of the FA core complex. | PMID:25659033 | Cell cycle |
| 2016 | High | FANCD2-FANCI (ID) complex adopts a closed conformation when FANCD2 is monoubiquitinated, forming a channel that encloses dsDNA; ubiquitin acts as a covalent molecular pin at the FANCD2-FANCI interface to trap the complex on DNA; unmodified FANCD2 forms a homodimer unable to bind DNA, suggesting an autoinhibitory mechanism. | PMID:32066963 | Nature structural & molecular biology |
| 2016 | High | The FANCD2-FANCI complex is recruited to stalled replication forks (as detected at ICLs) before monoubiquitination; cryo-EM structure of the human FANCD2-FANCI complex shows an inner cavity large enough for dsDNA and a Tower domain; disease-causing mutations in the Tower domain impair FA pathway activation. | PMID:27405460 | Nature communications |
| 2016 | High | Ubiquitinated FANCD2 recruits FAN1 to stalled replication forks to restrain fork progression and prevent chromosome abnormalities, even in the absence of ICLs; FAN1 nuclease-defective knockin mice are cancer-prone; a cancer-associated FAN1 variant abolishing Ub-FANCD2 binding causes genetic instability without affecting ICL repair. | PMID:26797144 | Science |
| 2016 | High | FANCD2 acts as a trans-acting facilitator of common fragile site (CFS) replication; in FANCD2-deficient cells, replication forks stall within AT-rich CFS cores leading to dormant origin activation; FANCD2 deficiency is associated with DNA:RNA hybrid formation at CFS-FRA16D, and inhibition of DNA:RNA hybrids suppresses replication perturbation. | PMID:27768874 | Molecular cell |
| 2016 | High | FANCD2 is required for fork protection and restart in BRCA1/2-deficient tumors; FANCD2 promotes Polθ recruitment at sites of damage and alt-EJ repair; loss of FANCD2 in BRCA1/2-deficient tumors results in synthetic lethality. | PMID:27264184 | Cell reports |
| 2016 | Medium | Monoubiquitinated FANCD2 antagonizes the BLM helicase to restrain telomere replication and recombination in ALT cells; FANCD2 depletion causes a hyper-ALT phenotype with increased extrachromosomal telomeric repeat DNAs suppressed by BLM but not RAD51 loss. | PMID:27427384 | Human molecular genetics |
| 2016 | High | FANCI-FANCD2 complex directly binds RAD51 and stabilizes the RAD51-DNA filament; this DNA end protection from FAN1 nucleolytic degradation requires FANCI's DNA-binding activity (not FANCD2's), and is abolished by the RAD51 mutant from FANCR patient cells. | PMID:27694619 | Nucleic acids research |
| 2017 | Medium | FANCD2 binds HPV genomes preferentially over cellular chromosomes and is required for maintenance of HPV episomes in undifferentiated basal epithelial cells; HPV-dependent FANCD2 foci colocalize with ATM pathway components (γH2AX, BRCA1) but not p-SMC1. | PMID:28196964 | mBio |
| 2017 | Medium | FANCD2 interacts with the spliceosomal protein SF3B1 (U2 snRNP component); replication stress induces ATR-dependent release of SF3B1 from nuclear speckles in a FANCI-dependent manner; both FANCD2 and FANCI associate with SF3B1 on chromatin and prevent accumulation of postcatalytic intron lariats. | PMID:29030393 | The Journal of cell biology |
| 2017 | Medium | FANCD2 localizes to mitochondria where it associates with nucleoid complex components ATAD3 and TUFM; ATAD3-TUFM complex is disrupted in Fancd2-/- and Fanca-/- mice; FANCD2 mitochondrial localization requires ATAD3, suggesting a role in mitochondrial homeostasis. | PMID:28378742 | Scientific reports |
| 2017 | Low | Monoubiquitinated FANCD2 (but not K561R mutant) interacts with ATP5α; monoubiquitination-dependent localization of ATP5α within mitochondria is required for normal mitochondrial ATP production; loss of monoubiquitinated FANCD2 causes mislocalization of ATP5α and reduced mitochondrial ATP output. | PMID:28687786 | Scientific reports |
| 2018 | Medium | FANCD2 accumulates at the central regions of large transcribed genes (common fragile sites) during replication stress in an R-loop-dependent manner (as shown by ChIP-seq and PLA); however, FANCD2 monoubiquitination and RPA foci formation are still induced in R-loop-depleted cells, indicating R-loops are needed for FANCD2 retention at chromatin but not for upstream FA pathway activation. | PMID:29394375 | Nucleic acids research |
| 2018 | Medium | FANCD2 interacts with RNA processing factors hnRNP U and DDX47 and recruits them to R-loop-containing chromatin; this reduces transcription-replication collisions and lowers R-loop levels, contributing to genome stability during mild replication stress. | PMID:30431240 | The FEBS journal |
| 2019 | High | Purified human FANCI-FANCD2 (ID2) complex binds ssRNA and R-loop substrates with high affinity (preferring G-rich sequences) via recognition of displaced ssDNA and ssRNA; RNA and R-loop substrates strongly stimulate ID2 monoubiquitination in vitro with activity corresponding to binding affinity. | PMID:30650351 | Cell reports |
| 2019 | High | Efficient FANCD2 deubiquitination by the USP1-UAF1 complex is DNA-dependent and requires DNA binding by UAF1; the DNA-binding activity of the UAF1-associated protein RAD51AP1 can substitute for UAF1 DNA binding in FANCD2 deubiquitination in reconstituted biochemical systems. | PMID:31253762 | Nature communications |
| 2019 | High | CK2 phosphorylates a cluster of FANCD2 sites to inhibit FANCD2 binding to DNA and thereby prevent FANCD2 recruitment to ICLs and its monoubiquitination in the absence of DNA damage, functioning as a molecular off-switch for the FA pathway. | PMID:31167143 | Cell reports |
| 2019 | High | FANCL allosterically activates UBE2T via rewiring its intraresidue network to influence the active site, enabling site-specific FANCD2 monoubiquitination; a basic triad unique to UBE2T engages an acidic patch near the target lysine on FANCD2; this three-dimensional E2-substrate complementarity induced by FANCL is central to site-specific FA pathway ubiquitination. | PMID:31873223 | Nature chemical biology |
| 2020 | High | ATR directly phosphorylates FANCI on S556, S559, and S565 to stabilize its association with DNA and FANCD2; this increased association stimulates ubiquitin conjugation to both FANCI and FANCD2 but also inhibits USP1-UAF1-mediated deubiquitination; S559 and S565 are particularly important for protecting the complex from deubiquitination. | PMID:32117957 | Frontiers in cell and developmental biology |
| 2020 | High | Ubiquitination of FANCD2 promotes a conformational change in the ID2 complex that increases affinity for dsDNA via formation of a secondary 'Arm' ID2 interface that encircles DNA; ubiquitination of FANCI protects ubiquitin on FANCD2 from USP1-UAF1 deubiquitination via hydrophobic residues of FANCI's ubiquitin. | PMID:32510829 | EMBO reports |
| 2021 | High | Crystal structures of USP1-UAF1 and cryo-EM reconstruction of USP1-UAF1 bound to monoubiquitinated FANCI-FANCD2 reveal that UAF1 makes an extensive interface with FANCI (confirmed by mutagenesis) driving conformational changes in the substrate; the N-terminus of USP1 harbors a FANCD2-specific binding sequence required for deubiquitination of K561 on FANCD2 but not required for PCNA or FANCI deubiquitination. | PMID:33795880 | Nature structural & molecular biology |
| 2022 | High | ATR-mediated phosphomimetic substitutions in FANCI cause FANCD2-FANCI to close around DNA independently of the FA core complex; phosphomimetic mutations destabilize the open state and alter conformational dynamics without substantially altering DNA binding affinity, demonstrating that phosphorylation primes the clamp for ubiquitination. | PMID:36050501 | Nature structural & molecular biology |
| 2023 | High | Purified FANCD2 N-terminal domain directly binds and inhibits DNA2 nuclease activity; independently of FANCI dimerization, FANCD2 stabilizes RAD51 filaments to inhibit DNA2, MRE11, and EXO1; FANCD2-stabilized RAD51 filaments stimulate RAD51 strand exchange activity, revealing FANCD2 as a RAD51 mediator. | PMID:37526271 | Nucleic acids research |
| 2024 | High | FANCD2-FANCI is a sliding clamp that diffuses on dsDNA; it stalls specifically at ssDNA-dsDNA junctions (structures present at stalled replication forks); cryo-EM structures show stalled D2-I makes distinct interactions with ss-dsDNA junctions compared to sliding D2-I, providing a unified mechanism for how D2-I surveys DNA and identifies stalled fork structures. | PMID:39085614 | Nature |
| 2024 | Medium | SRSF1 physically interacts with FANCD2 and together they suppress R-loop formation via mRNA export regulation; SRSF1 stimulates FANCD2 monoubiquitination in an RNA-dependent fashion; FANCD2 monoubiquitination is required for assembly of the SRSF1-NXF1 nuclear export complex; cancer-associated SRSF1 mutants fail to interact with FANCD2, leading to impaired monoubiquitination, decreased mRNA export, and R-loop accumulation. | PMID:38165804 | Cell reports |

## Citations

- PMID:11239453
- PMID:12239151
- PMID:12447395
- PMID:12874027
- PMID:12887909
- PMID:15115758
- PMID:15314022
- PMID:15454491
- PMID:15601828
- PMID:16860002
- PMID:16943440
- PMID:17352736
- PMID:17412408
- PMID:17420278
- PMID:17938197
- PMID:18082605
- PMID:18212739
- PMID:19561358
- PMID:19609304
- PMID:19633289
- PMID:20603015
- PMID:21355096
- PMID:21764741
- PMID:22287633
- PMID:22855611
- PMID:23538752
- PMID:23806336
- PMID:23993743
- PMID:24556218
- PMID:24623813
- PMID:24726325
- PMID:24794430
- PMID:24794434
- PMID:24905007
- PMID:25659033
- PMID:25801034
- PMID:26797144
- PMID:27264184
- PMID:27405460
- PMID:27427384
- PMID:27694619
- PMID:27768874
- PMID:28196964
- PMID:28378742
- PMID:28687786
- PMID:29030393
- PMID:29394375
- PMID:30431240
- PMID:30650351
- PMID:31167143
- PMID:31253762
- PMID:31873223
- PMID:32066963
- PMID:32117957
- PMID:32510829
- PMID:33795880
- PMID:36050501
- PMID:37526271
- PMID:38165804
- PMID:39085614
