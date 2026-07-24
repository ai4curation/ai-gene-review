---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/FANCM
affinage_run_date: 2026-06-09T23:54:43
uniprot_accession: Q8IYD8
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 41
citation_count: 41
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for FANCM (human)

## Current model (mechanistic narrative)

FANCM is an ATP-dependent DNA translocase and branch-point migrase that recognizes branched DNA intermediates—Holliday junctions, replication forks, and D-loops—and remodels them to preserve genome stability during replication stress [PMID:18206976, PMID:18285517]. Through its N-terminal translocase domain it catalyzes bidirectional branch migration and replication fork reversal in an ATPase-dependent manner [PMID:18206976, PMID:18843105], with the Hel2i subdomain coupling specific branched-DNA engagement to catalytic migration [PMID:39189453, PMID:40447800]. Beyond its enzymatic activity, FANCM serves as a chromatin-targeting scaffold that loads the Fanconi anemia core complex onto chromatin in a cell-cycle-dependent manner and is required for normal FANCD2 monoubiquitination [PMID:18174376, PMID:17289582]; it bridges the FA and Bloom syndrome dissolvasome pathways through two conserved motifs—MM1 binding the core complex via FANCF and MM2 binding RMI1/topoisomerase IIIα—with loss of bridging elevating sister chromatid exchange [PMID:20064461, PMID:22392978]. FANCM functions in a stable heterodimeric module with the histone-fold proteins MHF1-MHF2, which stimulate its DNA binding and fork-remodeling activity and switch its DNA-binding preference toward branched DNA [PMID:20347428, PMID:20347429, PMID:24699063], and it partners with FAAP24, whose DNA-binding (HhH)2 domain targets the complex to chromatin [PMID:17289582, PMID:24003026]. Functionally distinct activities are separable: the translocase activity is dispensable for FA pathway activation but required for replication fork stability, ICL traverse, ATR/CHK1 checkpoint signaling, and recovery of stalled forks [PMID:18285517, PMID:18995830, PMID:22279085, PMID:24207054], and FANCM facilitates ATR checkpoint activation by promoting RPA and TopBP1 chromatin retention [PMID:20670894, PMID:20057355]. FANCM is regulated by ATR-dependent phosphorylation at S1045 and by Plk1/β-TRCP-driven mitotic degradation that releases the core complex from chromatin [PMID:23698467, PMID:19270156]. At ALT telomeres, its translocase activity and BTR-complex interaction suppress TERRA R-loops and BLM-driven break-induced telomere synthesis, rendering FANCM-BTR disruption selectively toxic to ALT cancer cells [PMID:31138795, PMID:31138797], and FANCM loss is synthetic-lethal with BRCA1 hypomorphs and with SMARCAL1 [PMID:33882298, PMID:39510066]. The ortholog studies establish a conserved role in limiting recombination outcomes by dissociating D-loops, including meiotic crossover control [PMID:18851838, PMID:32386601].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140657 ATP-dependent activity, GO:0003677 DNA binding, GO:0140097 catalytic activity, acting on DNA, GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005694 chromosome, GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-69306 DNA Replication, R-HSA-8953897 Cellular responses to stimuli, R-HSA-1643685 Disease
- **partners:** FAAP24, MHF1, MHF2, FANCF, RMI1, BLM, PCNA, AND-1
- **complexes:** FANCM-FAAP24, FANCM-MHF1-MHF2, Fanconi anemia core complex, BLM-TOP3A-RMI (BTR) dissolvasome

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2007 | High | FANCM associates with FAAP24 through its C-terminal region; FAAP24 shares homology with XPF family flap/fork endonucleases and targets FANCM to DNA structures mimicking replication/repair intermediates. FAAP24 is required for normal levels of FANCD2 monoubiquitylation following DNA damage. | PMID:17289582 | Molecular cell |
| 2008 | High | Purified FANCM binds Holliday junctions and replication forks with high specificity and promotes migration of their junction point in an ATPase-dependent manner; FANCM can dissociate large recombination intermediates via branch migration of Holliday junctions through 2.6 kb of DNA. | PMID:18206976 | Molecular cell |
| 2008 | High | FANCM promotes reversal of model replication forks via concerted displacement and annealing of nascent and parental DNA strands (fork reversal); this activity also occurs when the lagging strand template is partially single-stranded and bound by RPA. | PMID:18843105 | Proceedings of the National Academy of Sciences of the United States of America |
| 2008 | High | FANCM possesses ATP-independent DNA binding activity and ATP-dependent bi-directional branch-point translocation on four-way junction DNA. ATP-dependent activities are required for cellular resistance to mitomycin C but not for monoubiquitination of FANCD2/FANCI; the entire helicase domain (ATP-dependent and independent) is required for monoubiquitination. | PMID:18285517 | Human molecular genetics |
| 2008 | High | FANCM and FAAP24 are required for cell-cycle-dependent chromatin loading of the FA core complex; FANCM is exclusively localized to chromatin and undergoes cell-cycle-dependent phosphorylation. Depletion of FAAP24 disrupts chromatin association of FANCM and destabilizes it, preventing FA core complex recruitment to chromatin. | PMID:18174376 | Blood |
| 2008 | High | FANCM and FAAP24 interact with checkpoint protein HCLK2 independently of the FA core complex. Downregulation of FANCM or FAAP24 compromises ATR/Chk1-mediated checkpoint signaling. The DNA translocase activity of FANCM—dispensable for FA pathway activation—is required for its role in ATR/Chk1 signaling. | PMID:18995830 | Molecular cell |
| 2008 | High | The FANCM ortholog Fml1 in fission yeast promotes Rad51-dependent gene conversion at stalled/blocked replication forks and limits crossing over during mitotic double-strand break repair; in vitro Fml1 catalyzes both replication fork reversal and D-loop disruption. | PMID:18851838 | Molecular cell |
| 2009 | High | FANCM connects the FA and Bloom Syndrome pathways via two conserved interaction motifs: MM1 interacts with the FA core complex by binding FANCF, and MM2 interacts with RMI1 and topoisomerase IIIα (components of the BLM/BS dissolvasome complex). Both motifs are independently required to activate their respective pathways, and loss of this bridging causes elevated sister chromatid exchanges. | PMID:20064461 | Molecular cell |
| 2009 | High | FANCM is hyperphosphorylated and degraded during mitosis; β-TRCP and Plk1 are the key regulators of FANCM degradation. Non-degradable FANCM mutants retain the FA core complex in chromatin and disrupt the FA pathway, revealing a mechanism for cell-cycle-dependent regulation. | PMID:19270156 | Genes & development |
| 2009 | Medium | In Xenopus egg extracts, xFANCM binds chromatin in a replication-dependent manner and is phosphorylated in response to DNA damage; chromatin binding and phosphorylation are mediated in part by FANCD2 and by checkpoint kinases ATR and ATM. | PMID:19633289 | The Journal of biological chemistry |
| 2009 | Medium | FANCM controls DNA chain elongation in an ATPase-dependent manner in vivo; in the presence of replication inhibitors that do not damage DNA, FANCM counteracts fork movement, whereas through damaged DNA FANCM promotes replication and recovers stalled forks. Chk1 signaling prevents FANCM degradation by the proteasome after DNA damage, and FANCM stabilizes Chk1 in a feedback loop. | PMID:20010692 | The EMBO journal |
| 2010 | High | FANCM forms a conserved DNA-remodeling complex with the histone-fold heterodimer MHF1-MHF2; MHF stimulates DNA binding and replication fork remodeling by FANCM. FANCM and MHF are rapidly recruited to forks stalled by DNA interstrand crosslinks and are required for cellular resistance. In vertebrates, FANCM-MHF promotes FANCD2 monoubiquitination and suppresses sister chromatid exchanges. | PMID:20347428, PMID:20347429 | Molecular cell |
| 2010 | High | MHF1 and MHF2 assemble into a heterodimer that binds DNA and enhances the DNA branch migration activity of FANCM; suppression of MHF1 destabilizes FANCM and MHF2, impairs FANCD2 monoubiquitination and foci formation, disrupts chromatin localization of FA core complex proteins, and causes chromosomal instability. | PMID:20347429 | Molecular cell |
| 2010 | High | FANCM and FAAP24 are specifically required for recruitment of RPA to ICL-stalled replication forks; ICL-induced RPA foci formation requires the DNA-binding activity of FAAP24 but not the DNA translocase activity of FANCM; FANCM/FAAP24-dependent RPA recruitment is required for efficient ATR-mediated checkpoint activation in response to ICL. | PMID:20670894 | Molecular cell |
| 2010 | High | FANCM promotes replication fork restart and limits accumulation of RPA-ssDNA; in DT40 cells this process is controlled by ATR and PLK1. FANCM promotes chromatin retention of TopBP1, and failure to retain TopBP1 impairs ATR phosphorylation of downstream targets including Chk1 and SMC1. | PMID:20057355 | The EMBO journal |
| 2012 | High | Crystal structures of MHF1-MHF2 alone and bound to FANCM fragment (residues 661-800) show MHF forms a compact tetramer; FANCM binds through a 'dual-V' shaped structure; FANCM and (MHF1-MHF2)2 cooperate to form a new DNA-binding site coupled to the canonical L1L2 region. A disease-associated FANCM mutant alters the MHF-FANCM interaction and subcellular localization. | PMID:22510687 | Nature communications |
| 2012 | High | The X-ray crystal structure of the RMI core complex bound to a conserved FANCM peptide shows FANCM binds both RMI1 and RMI2 through a hydrophobic 'knobs-into-holes' arrangement. Alanine substitutions at key interface residues strongly destabilize the complex and increase SCE levels comparable to BLM- or FANCM-deficient cells. | PMID:22392978 | Proceedings of the National Academy of Sciences of the United States of America |
| 2012 | High | FANCM translocase activity is essential for promoting replication fork stability; cells expressing translocase-defective FANCM show increased stalled forks that degenerate into DSBs leading to ATM activation, CtIP-dependent end resection, and homologous recombination repair. | PMID:22279085 | Human molecular genetics |
| 2013 | High | FANCM/MHF complex translocase and DNA-binding activities promote replication traverse of DNA interstrand crosslinks, allowing DNA synthesis to continue past ICLs without lesion repair; inactivation of translocase or DNA-binding activities strongly reduces traverse frequency. | PMID:24207054 | Molecular cell |
| 2013 | High | FANCM and FAAP24 possess non-overlapping functions: FAAP24 promotes ATR-mediated checkpoint activation in response to DNA crosslinking agents, whereas FANCM participates in recombination-independent ICL repair by facilitating recruitment of lesion incision activities requiring its translocase activity. | PMID:23333308 | Molecular cell |
| 2013 | High | Crystal structure of the C-terminal segment of FANCM in complex with FAAP24 reveals both proteins have a nuclease domain and tandem helix-hairpin-helix (HhH)2 domain; variations in key residues render FANCM's nuclease domain catalytically inactive; the first HhH motif of FAAP24 is a DNA-binding site critical for targeting FANCM-FAAP24 to chromatin. | PMID:24003026 | Nucleic acids research |
| 2013 | High | Structure of FANCM C-terminal domain (FANCMCTD) bound to FAAP24 and DNA reveals the FANCM (HhH)2 domain is buried while FAAP24 (HhH)2 domain engages DNA; a second DNA contact and metal center in the FANCM pseudo-nuclease domain are required for double-stranded DNA binding in vitro and FANCM-FAAP24 function in vivo. EM shows the translocase domain lies in proximity to FANCMCTD. | PMID:23932590 | Structure |
| 2013 | High | ATR-dependent phosphorylation of FANCM at serine 1045 in response to genotoxic stress is required for FANCM functions including FA pathway integrity, recruitment of FANCM to ICL sites, preventing premature mitotic entry, and efficient CHK1 and G2/M checkpoint activation, establishing an ATR-FANCM feedback loop. | PMID:23698467 | Cancer research |
| 2014 | High | Crystal structure of MHF bound to the MHF-interaction domain (MID) of FANCM shows one MHF heterotetramer wrapped by a single MID polypeptide; a zinc atom-liganding structure at the interface stabilizes the complex; MID binding switches MHF DNA-binding preference from duplex DNA to branched DNA. Mutations disrupting the composite DNA-binding surface or protein-protein interface impair FA network activation and genome stability. | PMID:24699063 | Cell research |
| 2016 | High | FANCM interacts with PCNA through a conserved PIP-box motif; the interaction is strongly stimulated by replication stress. A PIP-box mutant FANCM variant is defective in promoting replication traverse of ICLs and inefficient in promoting FANCD2 monoubiquitination. | PMID:26825464 | Nucleic acids research |
| 2016 | High | FANCM recruitment to ICL-stalled replication forks depends on its intrinsic DNA translocase activity, FAAP24 DNA-binding, ATR kinase activity, and direct interaction with the BLM-TOP3A-RMI (BTR) complex including the helicase activity of BLM; this recruitment is independent of the FA core complex and FANCD2-FANCI. The FANCM-BLM interaction is critical for FANCM hyperphosphorylation, FA pathway activation, and ICL traverse. | PMID:28058110 | Cell discovery |
| 2017 | High | FANCM depletion induces replication stress primarily at telomeres of ALT cells; FANCM, BRCA1, and BLM are actively recruited to ALT telomeres experiencing replication stress; BRCA1 and BLM recruitment is interdependent and regulated by ATR and Chk1. In FANCM-depleted ALT cells, BRCA1 and BLM resolve telomeric replication stress by stimulating DNA end resection and homologous recombination. | PMID:28673972 | Proceedings of the National Academy of Sciences of the United States of America |
| 2019 | High | The ATPase/translocase activity of FANCM keeps telomeric replicative stress in check in ALT cells by suppressing BLM-driven telomere stress and by unwinding telomeric R-loops (TERRA R-loops) in vitro; FANCM depletion increases ALT-associated marks, de novo telomeric DNA synthesis, and BLM-dependent telomere dysfunction. RNaseH1 overexpression abrogates residual replication stress in FANCM+BLM co-depleted cells. | PMID:31138795 | Nature communications |
| 2019 | High | FANCM-mediated attenuation of ALT requires its DNA translocase activity and interaction with the BTR (BLM-TOP3A-RMI) complex but does not require the FA core complex. FANCM depletion provokes ALT activity via increased break-induced telomere synthesis. Synthetic inhibition of FANCM-BTR complex formation is selectively toxic to ALT cancer cells. | PMID:31138797 | Nature communications |
| 2019 | High | FANCM (via FAAP24 interaction) disrupts TERRA R-loops at ALT telomeres; depletion of FAAP24 or FANCM induces dramatic increase of C-circle formation driven by ATR/Chk1, BTR complex, HR proteins (BRCA2, PALB2, RAD51), and BIR factors (POLD1, POLD3). RNase H1 overexpression attenuates ALT phenotypes caused by FANCM deficiency. | PMID:31836759 | Scientific reports |
| 2019 | High | FANCM binds the replisome complex following ICL introduction in an ATR- and FANCD2-dependent but FA core protein- and FAAP24-independent manner, with concomitant release of GINS proteins from the CMG helicase. ATR-dependent phosphorylated FANCM promotes this replisome remodeling. | PMID:31067464 | Cell reports |
| 2021 | High | Distinct FANCM repair functions at stalled forks are enacted by molecularly separable scaffolding domains; FANCM ATPase function is required for all its repair functions and its inactivation 'traps' FANCM at stalled forks. Brca1 hypomorphic mutants are synthetic lethal with Fancm null or Fancm ATPase-defective mutants. | PMID:33882298 | Molecular cell |
| 2022 | High | And-1 (a replisome protein) is critical for activation of the FA pathway by sensing ICL-stalled forks and recruiting the FANCM/FAAP24 complex to ICLs; this requires ATR-induced phosphorylation of And-1 at T826, which triggers an intramolecular change promoting And-1 interaction with FANCM/FAAP24. | PMID:35867033 | Cancer research |
| 2024 | High | The Hel2i subdomain within the N-terminal translocase domain is crucial for FANCM's specific branched DNA engagement, coupling DNA binding to catalytic ATP-dependent branch migration. Mutations in Hel2i or key DNA-binding residues diminish junction DNA affinity and abolish branch migration activity, and these mutants fail to rescue ALT cell death or telomere replication stress upon FANCM depletion. | PMID:39189453 | Nucleic acids research |
| 2024 | High | Crystal structures of FANCM's N-terminal translocase domain (2.2 Å) and C-terminal FAAP24-bound region (2.4 Å), both complexed with branched DNA, reveal two distinct mechanisms: (1) ATP-dependent branch migration essential for DNA damage survival, and (2) a branched DNA-binding mode at the C-terminal domain that enhances FANCD2-FANCI monoubiquitination through FA core complex interaction. | PMID:40447800 | The EMBO journal |
| 2024 | High | SMARCAL1 displays a profound synthetic-lethal interaction with FANCM; combined loss causes severe genome instability linked to chromosome breakage at simple repeat loci that challenge replication fork progression. | PMID:39510066 | Molecular cell |
| 2024 | High | FANCM promotes PARP inhibitor resistance independent of the FA core complex by minimizing ssDNA gap formation behind replication forks through counteracting 53BP1; FANCM depletion leads to increased ssDNA gaps (via 53BP1- and PRIMPOL-dependent mechanisms) and reduced resection of collapsed forks, while 53BP1 deletion restores resection and mitigates PARPi sensitivity. | PMID:38985669 | Cell reports |
| 2009 | High | Walker B motif mutation in avian FANCM (DT40 cells) does not affect FA pathway activation or crosslink repair, but results in elevated sister chromatid exchanges; FANCM functions with BLM helicase to suppress spontaneous SCE events, placing them in the same pathway. | PMID:19465393 | Nucleic acids research |
| 2018 | High | FANCM, along with FAAP24 and MHF1/2, is recruited to CFS-derived structure-prone AT-rich sequences and suppresses DSB formation and mitotic recombination there in a manner dependent on FANCM translocase activity; this function is independent of the FA core complex and FANCI-FANCD2 complex. | PMID:30022024 | Nature communications |
| 2018 | Medium | In C. elegans, FANCM/CeFNCM-1 interacts with the histone demethylase LSD1/CeSPR-5; LSD1/CeSPR-5 is required for replication stress-induced S-phase checkpoint activation; FANCM relocalizes upon hydroxyurea exposure and colocalizes with FANCD2/CeFCD-2 and LSD1/CeSPR-5. The FA pathway is required for H3K4me2 maintenance. | PMID:29588287 | Genetics |
| 2020 | High | In budding yeast, Mph1 (FANCM ortholog) prevents precocious DSB strand exchange between sister chromatids before homologs complete pairing by dissociating precocious D-loops between sister chromatids; this ensures high levels of crossovers and non-crossovers between homologs. Later recombination events are protected from Mph1-mediated dissociation by synapsis protein Zip1. | PMID:32386601 | Developmental cell |

## Citations

- PMID:17289582
- PMID:18174376
- PMID:18206976
- PMID:18285517
- PMID:18843105
- PMID:18851838
- PMID:18995830
- PMID:19270156
- PMID:19465393
- PMID:19633289
- PMID:20010692
- PMID:20057355
- PMID:20064461
- PMID:20347428
- PMID:20347429
- PMID:20670894
- PMID:22279085
- PMID:22392978
- PMID:22510687
- PMID:23333308
- PMID:23698467
- PMID:23932590
- PMID:24003026
- PMID:24207054
- PMID:24699063
- PMID:26825464
- PMID:28058110
- PMID:28673972
- PMID:29588287
- PMID:30022024
- PMID:31067464
- PMID:31138795
- PMID:31138797
- PMID:31836759
- PMID:32386601
- PMID:33882298
- PMID:35867033
- PMID:38985669
- PMID:39189453
- PMID:39510066
- PMID:40447800
