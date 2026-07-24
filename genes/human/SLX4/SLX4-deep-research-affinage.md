---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/SLX4
affinage_run_date: 2026-06-10T07:46:35
uniprot_accession: Q8IY92
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 57
citation_count: 57
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for SLX4 (human)

## Current model (mechanistic narrative)

SLX4 (BTBD12/FANCP) is a multidomain scaffold that assembles and activates a modular toolkit of structure-specific endonucleases—XPF-ERCC1, MUS81-EME1, and SLX1—to process branched DNA intermediates arising during replication, recombination, and interstrand crosslink (ICL) repair [PMID:19596235, PMID:19595721]. Through direct contacts it stimulates each partner nuclease and directs substrate specificity: the SLX1-SLX4 module is a Holliday junction resolvase and 5'-flap endonuclease [PMID:19596236, PMID:12832395], the N-terminal SLX4-XPF-ERCC1 interaction enhances XPF-ERCC1 activity up to 100-fold and executes the unhooking incisions of replication-coupled ICL repair [PMID:24726326, PMID:24726325], and CDK1-driven phosphorylation of the MUS81-binding region folds an SAP domain that recruits MUS81-EME1 into a stable SLX-MUS holoenzyme providing efficient HJ resolution at G2/M [PMID:24076221, PMID:36288699]. Structural work shows SLX4 activates SLX1 by displacing its autoinhibitory homodimer and that the SLX4 SAP domain positions 5'-flap substrates for accurate cleavage [PMID:25753413, PMID:34181713]. SLX4 itself dimerizes via its BTB domain, an event required for foci formation and telomeric localization [PMID:27131364]. Damage-site recruitment is multi-modal: the UBZ1 domain reads K63-linked polyubiquitin deposited by RNF168 and ubiquitylated FANCD2 at ICLs [PMID:24794496, PMID:21464321, PMID:34706224], while SUMO-interacting motifs (cooperating with PARylation) target SLX4 to resected/laser damage, fragile sites, PML bodies, and ALT telomeres [PMID:25533185, PMID:25722289]. At telomeres SLX4 docks on the shelterin subunit TRF2 via an HxLxP motif to deliver its nucleases and regulate telomere length and fragility [PMID:24012755, PMID:23994477], and it drives recombination-based ALT telomere processing in opposition to the BLM-TOP3A-RMI dissolution pathway [PMID:28877996]. SLX4 additionally functions as a SUMO E3 ligase that SUMOylates itself and XPF [PMID:25533188], forms SUMO/dimerization-driven nuclear condensates that compartmentalize the SUMO-RNF4 pathway and promote topoisomerase-1 DPC extraction [PMID:37059091], interacts with the helicase RTEL1 to prevent replication-transcription conflicts [PMID:32398829], and binds MSH2 through a SHIP box to suppress MutSα-dependent mismatch repair [PMID:35166826]. SLX4 protein levels are buffered by RNF4-mediated ubiquitin-dependent degradation counterbalanced by USP7 within PML nuclear bodies, preventing unscheduled nuclease activity [PMID:41002028]. Biallelic SLX4 mutations cause Fanconi anemia subtype FA-P, and its essential ICL-repair function maps to the N-terminal XPF-ERCC1-binding region [PMID:21240275, PMID:21240277, PMID:21240276].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0140097 catalytic activity, acting on DNA, GO:0060090 molecular adaptor activity, GO:0016740 transferase activity, GO:0003677 DNA binding, GO:0098772 molecular function regulator activity
- **localization:** GO:0005634 nucleus, GO:0000228 nuclear chromosome, GO:0005654 nucleoplasm
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-1640170 Cell Cycle, R-HSA-1643685 Disease, R-HSA-392499 Metabolism of proteins
- **partners:** SLX1, MUS81, XPF/ERCC4, TRF2, RTEL1, MSH2, FANCD2, TOPBP1
- **complexes:** SLX1-SLX4 endonuclease, SLX-MUS holoenzyme (SLX1-SLX4-MUS81-EME1), SLX4-XPF-ERCC1, Slx4-Rtt107-Dpb11 (yeast)

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2009 | High | Human SLX4 (BTBD12) acts as a scaffold that assembles a multiprotein complex with three structure-specific endonucleases: XPF-ERCC1, MUS81-EME1, and SLX1, as well as MSH2/MSH3, TRF2-RAP1, PLK1, and C20orf94. The SLX1-SLX4 module promotes symmetrical cleavage of static and migrating Holliday junctions, identifying SLX1-SLX4 as a Holliday junction resolvase. SLX4 complexes also cleave 3' flap, 5' flap, and replication fork structures. Depletion of SLX4 causes sensitivity to mitomycin C and camptothecin and reduces DSB repair efficiency in vivo. | PMID:19596235 | Cell |
| 2009 | High | Human SLX1-SLX4 displays robust Holliday junction resolvase activity and 5' flap endonuclease activity. SLX4 binds the XPF (ERCC4) and MUS81 subunits of the XPF-ERCC1 and MUS81-EME1 endonucleases and is required for DNA interstrand crosslink repair. SLX4 acts as a docking platform for multiple structure-specific endonucleases. | PMID:19596236 | Cell |
| 2009 | High | Human SLX4 coordinates three DNA repair nucleases (XPF-ERCC1, MUS81-EME1, SLX1); SLX4 immunoprecipitates show SLX1-dependent nuclease activity toward Holliday junctions and MUS81-dependent activity toward other branched DNA structures. SLX4 enhances the nuclease activity of SLX1, MUS81, and XPF. Depletion of SLX4 causes hypersensitivity to genotoxins causing DSBs and defects in resolution of ICL-induced DSBs, and decreases DSB-induced homologous recombination. | PMID:19595721 | Molecular cell |
| 2009 | High | Drosophila MUS312 is the ortholog of human BTBD12/SLX4. BTBD12 interacts with SLX1 (conserved interaction from yeast Slx4) and with DNA structure-specific endonucleases including MEI-9-ERCC1, and is required for interstrand crosslink repair in mammalian cells. | PMID:19595722 | Molecular cell |
| 2003 | High | Budding yeast Slx1 and Slx4 form a heteromeric structure-specific endonuclease active on branched DNA substrates (simple-Y, 5'-flap, replication fork structures). Slx1 is stimulated ~500-fold by Slx4 and requires its PHD finger for activity. Slx1-Slx4 cleaves the strand bearing the 5' nonhomologous arm at the branch junction and generates ligatable nicked products. Both subunits are required for MMS resistance. | PMID:12832395 | Genes & development |
| 2003 | High | Fission yeast Slx1-Slx4 forms a structure-specific endonuclease that maintains rDNA copy number by introducing single-strand cuts in duplex DNA on the 3' side of junctions with single-strand DNA. Slx1 associates with chromatin at rDNA repeat loci. Simultaneous loss of Slx1-Slx4 and Rqh1 (RecQ helicase) is lethal. | PMID:14528010 | Molecular biology of the cell |
| 2013 | High | SLX1-SLX4 and MUS81-EME1 define a second pathway (SLX-MUS) of Holliday junction resolution in human cells distinct from GEN1. In response to CDK-mediated phosphorylation at the G2/M transition, SLX1-SLX4 and MUS81-EME1 associate to form a stable SLX-MUS holoenzyme that can be reconstituted in vitro. SLX-MUS is a more efficient HJ resolvase than SLX1-SLX4 alone, coordinating the active sites of two distinct endonucleases. | PMID:24076221 | Molecular cell |
| 2014 | High | XPF-ERCC1 cooperates with SLX4/FANCP to carry out the unhooking incisions during replication-coupled ICL repair in Xenopus egg extracts. Efficient recruitment of XPF-ERCC1 and SLX4 to the ICL depends on FANCD2 and its ubiquitylation. | PMID:24726325 | Molecular cell |
| 2014 | High | Mouse mini-SLX4 (N-terminal domain that only binds XPF-ERCC1) is sufficient to confer resistance to DNA crosslinking agents. Recombinant mini-SLX4 enhances XPF-ERCC1 nuclease activity up to 100-fold and directs specificity toward DNA forks. Mini-SLX4-XPF-ERCC1 stimulates dual incisions around a DNA crosslink embedded in a synthetic replication fork. | PMID:24726326 | Molecular cell |
| 2014 | High | The SLX4 complex acts as a SUMO E3 ligase that SUMOylates SLX4 itself and the XPF subunit of XPF-ERCC1. This activity is mediated by interaction between SLX4 and UBC9 (SUMO-charged E2 conjugating enzyme), requires SUMO-interacting motifs (SIMs) and the BTB domain of SLX4. SLX4 SIMs are dispensable for ICL repair but critical to prevent mitotic catastrophe following common fragile site expression. | PMID:25533188 | Molecular cell |
| 2014 | High | SLX4 binds SUMO-2/3 chains via SUMO-interacting motifs (SIMs). SLX4 SIMs are dispensable for ICL repair but required for processing CPT-induced replication intermediates, suppressing fragile site instability, and localizing SLX4 to ALT telomeres. SUMO binding of SLX4 enhances interactions with RPA, MRE11-RAD50-NBS1, and TRF2. Localization to laser-induced DNA damage requires SIMs, DNA end resection, UBC9, and MDC1. | PMID:25533185 | Molecular cell |
| 2013 | High | SLX4 assembles an endonuclease toolkit at telomeres via direct interaction with TRF2. Crystal structure of the SLX4 TRF2-binding motif (TBM) in complex with TRF2 TRFH domain reveals that TRF2 recognizes a unique HxLxP motif on SLX4. Telomeric localization of SLX4 and its nucleases depends on SLX4-endonuclease and SLX4-TRF2 interactions. SLX4 negatively regulates telomere length via SLX1-catalyzed nucleolytic resolution of telomere DNA structures. | PMID:24012755 | Cell reports |
| 2011 | High | SLX4's UBZ domain is required for interaction with ubiquitylated FANCD2 and for SLX4 recruitment to DNA-damage foci generated by ICL-inducing agents. UBZ-deficient SLX4 cells are selectively sensitive to ICL-inducing agents, demonstrating that ubiquitylated FANCD2 recruits SLX4 to damage sites to mediate resolution of recombination intermediates during ICL processing. | PMID:21464321 | Proceedings of the National Academy of Sciences of the United States of America |
| 2012 | High | SLX4-dependent XPF-ERCC1 activity is essential for ICL repair but dispensable for repairing TOP1 inhibitor-induced lesions. MUS81-SLX4 interaction is critical for resistance to TOP1 inhibitors but less important for ICL repair. Mutation of SLX4 abrogating SLX1 interaction results in partial sensitivity to both crosslinking agents and TOP1 inhibitors. | PMID:23093618 | Blood |
| 2007 | High | Budding yeast Slx4 is phosphorylated by Mec1 and Tel1 kinases after DNA damage. This phosphorylation is essential for single-strand annealing (SSA) repair. Slx4 is required for Rad1-dependent SSA but not for nucleotide excision repair. Slx4 associates physically with two structure-specific endonucleases, Rad1 and Slx1, in a mutually exclusive manner. | PMID:17636031 | Molecular and cellular biology |
| 2010 | High | Mec1 (ATR) mediates a key interaction between the fork protein Dpb11 and the DNA repair scaffolds Slx4-Rtt107. Slx4 phosphorylation by Mec1 is required for Slx4-Dpb11 interaction. Mutation of Mec1 phosphorylation sites in Slx4 disrupts interaction with Dpb11 and compromises cellular response to replication stress. | PMID:20670896 | Molecular cell |
| 2014 | High | Cell cycle-dependent phosphorylation of Slx4 by Cdk1 promotes the Dpb11-Slx4 interaction in yeast. In mitosis, additional phosphorylation of Mms4 by Polo-like kinase Cdc5 promotes association of Mus81-Mms4 with the Dpb11-Slx4 complex, thereby activating joint molecule resolution. The DNA damage checkpoint counteracts Mus81-Mms4 binding to the Dpb11-Slx4 complex. | PMID:25030699 | Genes & development |
| 2015 | High | Crystal structure of Candida glabrata Slx1 alone and in complex with the C-terminal region of Slx4 reveals: (1) Slx1 has a compact GIY-YIG nuclease and RING domain arrangement reinforced by a long α-helix; (2) Slx1 forms a stable homodimer that blocks its active site; (3) Slx1-Slx4 interaction is mutually exclusive with Slx1 homodimerization, suggesting a mechanism for Slx1 activation by Slx4 through displacement of the inhibitory homodimer. | PMID:25753413 | Cell reports |
| 2021 | High | The SAP domain of SLX4 is critical for efficient and accurate processing of 5'-flap DNA. The SAP domain binds the minor groove of DNA about one turn away from the flap junction, and the 5'-flap is implicated in binding the core domain of SLX1. This binding mode accounts for specific recognition of 5'-flap DNA and specification of cleavage site. | PMID:34181713 | Nucleic acids research |
| 2022 | High | CDK1-cyclin B phosphorylates SLX4 residues T1544, T1561, and T1571 in the MUS81-binding region (SLX4MBR). Phosphorylated SLX4MBR relaxes substrate specificity of MUS81-EME1 and stimulates cleavage of replication and recombination structures. Phosphorylation drives folding of an SAP domain in SLX4MBR, which underpins high-affinity interaction with MUS81. Crystal structure of phosphorylated SLX4MBR bound to MUS81 was determined. | PMID:36288699 | Cell reports |
| 2016 | High | SLX4 dimerizes via its BTB domain. Crystal structure of SLX4 BTB dimer was solved, identifying key dimerization contacts F681 and F708. Disruption of BTB dimerization abrogates nuclear foci formation and telomeric localization of SLX4 and its associated nucleases, and causes defective response to ICL agents and telomere maintenance. | PMID:27131364 | Nucleic acids research |
| 2013 | High | SLX4 forms foci that localize to telomeres in a range of human cell lines. SLX1 is recruited to telomeres by SLX4, and SLX4 is recruited by a motif that binds the shelterin subunit TRF2 directly. TRF2-dependent recruitment of SLX4 prevents telomere damage. SLX4 prevents telomere lengthening and fragility in a manner partially independent of telomere association. | PMID:23994477 | Cell reports |
| 2015 | High | SLX4's first UBZ domain (UBZ-1) binds ubiquitin polymers with a preference for K63-linked chains, while UBZ-2 does not bind ubiquitin in vitro. UBZ-1 is required for SLX4 recruitment to ICL sites and for efficient ICL repair. UBZ-2 is required for Holliday junction resolution in vivo but not ICL repair. | PMID:24794496 | Journal of cell science |
| 2010 | High | Mec1/Tel1-dependent phosphorylation of Slx4 at Thr113 is required for efficient cleavage of 3' non-homologous (NH) DNA tails by Rad1-Rad10 during single-strand annealing and homologous recombination. Slx4 is recruited to 3' NH tails during DSB repair independently of its phosphorylation. Deletion of both Mec1 and Tel1 severely reduces NH DNA tail cleavage during HR. | PMID:20382573 | DNA repair |
| 2005 | High | Budding yeast Slx4 forms a complex with the BRCA1 C-terminal domain protein Rtt107 (Esc4). SLX4 (but not SLX1) is required for Mec1-dependent phosphorylation of Rtt107 in vivo following DNA damage. Slx4 acts as a mediator of DNA damage-dependent phosphorylation of Rtt107 and is required for recovery from alkylation damage independently of Slx1. | PMID:16267268 | Molecular biology of the cell |
| 2014 | High | HIV-1 Vpr directly interacts with SLX4 and induces premature activation of the SLX4 complex, including recruitment of VPRBP-DDB1-CUL4 E3 ligase and kinase-active PLK1, enhancing DNA cleavage by SLX4-associated MUS81-EME1 endonucleases, resulting in G2/M arrest. Knockdown of SLX4, MUS81, or EME1 inhibits Vpr-induced G2/M arrest. The SLX4 complex also suppresses spontaneous and HIV-1-mediated induction of type 1 interferon. | PMID:24412650 | Cell |
| 2015 | High | Budding yeast Slx4 is recruited to chromatin behind stressed replication forks in a region spatially distinct from the replication machinery. Slx4 complex formation is nucleated by Mec1 phosphorylation of histone H2A, which is recognized by the constitutive Slx4 binding partner Rtt107. Slx4 is essential for recruiting the Mec1 activator Dpb11 behind stressed replication forks, and Slx4 complexes promote full Mec1 activity. | PMID:26113155 | The EMBO journal |
| 2013 | High | Human SLX4-null cells are synthetically lethal with BLM depletion or GEN1 depletion, due to unprocessed Holliday junctions causing dysfunctional mitosis. In vivo HJ resolution depends on both SLX4-associated MUS81-EME1 and SLX1 acting in concert within the SLX4 scaffold context. | PMID:24080495 | Cell reports |
| 2019 | High | SLX4 directly interacts with the DNA helicase RTEL1. Both proteins are recruited to nascent DNA and co-localize with active RNA pol II. SLX4 in complex with RTEL1 promotes FANCD2/RNA pol II co-localization. Disrupting the SLX4-RTEL1 interaction leads to DNA replication defects rescued by transcription inhibition, demonstrating that SLX4-RTEL1 interaction prevents replication-transcription conflicts. | PMID:32398829 | Nature structural & molecular biology |
| 2023 | High | SLX4 dimerization and SUMO-SIM interactions drive the assembly of SLX4 membraneless condensates (nanocondensates) in the nucleus. SLX4 compartmentalizes the SUMO-RNF4 signaling pathway. SENP6 and RNF4 regulate assembly and disassembly of SLX4 condensates, respectively. SLX4 condensation triggers SUMOylation and ubiquitylation of selected proteins and induces ubiquitylation and chromatin extraction of topoisomerase 1 DNA-protein cross-links and nucleolytic degradation of newly replicated DNA. | PMID:37059091 | Molecular cell |
| 2015 | High | SLX4 associates with telomeres throughout the cell cycle, peaking in late S phase and under genotoxic stress. Disruption of SLX4's interaction with TRF2 or SLX1 independently causes telomere fragility. The SLX1-SLX4 complex processes a variety of telomeric joint molecules in vitro. SLX1-SLX4 nucleolytic activity is negatively regulated by telomeric DNA-binding proteins TRF1 and TRF2, and suppressed by BLM helicase in vitro. | PMID:25990736 | Nucleic acids research |
| 2015 | Medium | SLX4 is recruited to sites of ICL induction in human cells. The first UBZ domain (UBZ-1) but not UBZ-2 is required for recruitment to ICL sites. SLX4 recruitment to ICLs does not require ubiquitylation of FANCD2 or the E3 ligases RNF8, RAD18, or BRCA1 (based on individual depletions). | PMID:24794496 | Journal of cell science |
| 2021 | Medium | RNF168 E3 ligase is a critical factor for mitomycin C-induced SLX4 foci formation. RNF168 and SLX4 co-localize in MMC-induced ubiquitin foci. Accumulation of SLX4 at psoralen-laser ICL tracks or of endogenous SLX4 at ICL sites is dependent on RNF168. RNF168 is epistatic with SLX4 in promoting MMC tolerance. | PMID:34706224 | Cell reports |
| 2019 | Medium | SLX4IP acts as a regulatory factor binding SLX4 and XPF-ERCC1 simultaneously; disruption of one interaction also disrupts the other. SLX4IP-SLX4-XPF-ERCC1 binding maintains SLX4IP protein stability and promotes SLX4-XPF-ERCC1 interaction after DNA damage. Depletion of SLX4IP sensitizes cells to ICL-inducing agents. | PMID:31495888 | Nucleic acids research |
| 2019 | Medium | In vitro structural and biochemical analysis of fungal Slx1-Slx4: A new protein interface on Slx1 binds the non-cleaved arm of branched DNAs. DNA binding at this site promotes a disorder-to-order transition near the active site, acting as a safety mechanism ensuring cleavage only when the interface is occupied. This binding mode explains how Slx1 cuts toward the 3' end away from branch points and cleaves various DNA structures. | PMID:31584081 | Nucleic acids research |
| 2016 | Medium | Crystal structure of S. pombe Slx1 C-terminal zinc finger domain in complex with the C-terminal helix-turn-helix domain of Slx4 was determined. The structure reveals a conserved Slx1-Slx4 binding mechanism. Slx1 C-terminal domain is an atypical RING finger required for Slx1-Slx4 interaction. The C-terminal tail of S. pombe Slx1 contains a SUMO-interacting motif (SIM) that recognizes Pmt3 (S. pombe SUMO), suggesting SUMO-dependent recruitment. | PMID:26787556 | Scientific reports |
| 2015 | Medium | SUMOylation and PARylation cooperate to recruit and stabilize SLX4 at DNA damage sites. Three SIMs in SLX4 are required for SUMO-2 binding and covalent SLX4 SUMOylation; SIM mutants fail to accumulate at laser-induced DNA damage sites and are absent from PML nuclear bodies. PARylation additionally participates in SLX4 recruitment to DNA damage. | PMID:25722289 | EMBO reports |
| 2025 | Medium | RNF4 ubiquitin E3 ligase is associated with SLX4 and is responsible for ubiquitin-dependent proteasomal degradation of excessive SLX4 under normal conditions. PML nuclear bodies promote SLX4 stability, where the deubiquitinase USP7 maintains SLX4 protein levels. This RNF4/USP7 balance within PML NBs regulates SLX4 protein homeostasis to prevent uncontrolled nuclease activity in the absence of DNA damage. | PMID:41002028 | Nucleic acids research |
| 2025 | Medium | Human TopBP1 promotes MiDAS (mitotic DNA synthesis) through recruitment of SLX4 to sites of underreplicated DNA marked by FANCD2. TopBP1-K704 and SLX4-T1260 residues, along with SLX4 SUMO-interaction motifs, are required for SLX4 recruitment to TopBP1 foci in mitosis. Recruitment of SLX4 to TopBP1 foci is important to prevent transmission of DNA damage to daughter cells. | PMID:40615546 | Communications biology |
| 2019 | Medium | WRNIP1 protects reversed replication forks from SLX4-mediated endonucleolytic cleavage at the junction point. This function is specific to the shorter WRNIP1 variant and is independent of BRCA2-dependent fork protection. | PMID:31654852 | iScience |
| 2021 | Medium | CIP2A-TOPBP1 form filamentous structures at sites of incomplete DNA replication during mitosis and facilitate recruitment of the SMX tri-nuclease complex members SLX4, MUS81, and XPF-ERCC1 to these structures. The unstructured C-terminal domain of CIP2A is essential for CIP2A-TOPBP1 filament formation and SMX recruitment. SLX4 is crucial for genome stability in BRCA2-deficient cells. | PMID:41330930 | Nature communications |
| 2022 | Medium | SLX4-XPF is required for Tus-Ter-induced homologous recombination at a site-specific chromosomal DNA-protein replication fork barrier, but not for error-free HR induced by a replication-independent DSB. SLX4-XPF also contributes to DSB-induced long-tract gene conversion (break-induced replication). SLX4-XPF can process DNA-protein replication fork barriers. | PMID:35941380 | Nature structural & molecular biology |
| 2021 | Medium | Abraxas restricts SLX4/MUS81 recruitment to CPT-induced damage sites by counteracting K63-linked ubiquitin modification. Uncontrolled SLX4/MUS81 loading due to Abraxas deficiency leads to excessive end resection and increased break-induced replication via RAD52- and POLD3-dependent, RAD51-independent BIR. | PMID:34272385 | Nature communications |
| 2019 | Medium | The SLX4 complex promotes resolution of recombination intermediates that counteracts BLM-TOP3A-RMI (BTR) complex-mediated dissolution during ALT telomere synthesis. SLX4-SLX1-ERCC4 promotes resolution of recombination intermediates resulting in telomere exchange without telomere extension, opposing BTR-dependent conservative synthesis. | PMID:28877996 | The EMBO journal |
| 2019 | Medium | RAD52 and SLX4 mediate distinct post-replicative DNA repair processes at ALT telomeres; RAD52 is dispensable for DSB-induced telomere synthesis while SLX4 is dispensable for RAD52-mediated ALT telomere synthesis in G2. Combined SLX4 and RAD52 loss results in elevated telomere loss, unresolved telomere recombination intermediates, and mitotic infidelity, demonstrating non-epistatic roles. | PMID:30692206 | Genes & development |
| 2024 | Medium | Polyubiquitinated PCNA (polyUb-PCNA) accumulates SLX4 at ALT telomeres through SLX4's ubiquitin-binding domain, increasing telomere damage. This polyUb-PCNA-SLX4 axis triggers break-induced replication at telomeres and common fragile sites. SLX4 depletion reduces ALT-associated PML bodies and mitotic DNA synthesis at telomeres. | PMID:39291733 | Nucleic acids research |
| 2011 | High | Biallelic mutations in SLX4 cause Fanconi anemia subtype FA-P. The cellular defects in patient cells (hypersensitivity to ICL-inducing agents, chromosomal instability) are complemented by wild-type SLX4, establishing SLX4 as an essential component of the FA-BRCA genome maintenance pathway. | PMID:21240275, PMID:21240277 | Nature genetics |
| 2011 | High | Mouse Btbd12/Slx4 knockout phenocopies Fanconi anemia. Genetic complementation reveals a crucial requirement for Btbd12 to interact with Xpf-Ercc1 to promote crosslink repair, placing SLX4-XPF-ERCC1 interaction as essential for ICL repair in vivo. | PMID:21240276 | Nature genetics |
| 2022 | Medium | SLX4 interacts with MSH2 via an MSH2-interacting peptide (SHIP box) that drives interaction with both MutSβ (MSH2-MSH3) and MutSα (MSH2-MSH6). The MSH2 binding domain is dispensable for ICL repair but mediates inhibition of MutSα-dependent mismatch repair by SLX4. | PMID:35166826 | Nucleic acids research |
| 2015 | Medium | Budding yeast Slx4 limits checkpoint signaling at persistent DSBs and uncapped telomeres by reducing Rad9 binding near irreparable DSBs, requiring Rtt107 and Dpb11 interaction. In slx4Δ cells, Rad9 binding near the DSB is increased, causing robust checkpoint signaling and slower 5' strand resection. | PMID:26490958 | Nucleic acids research |
| 2019 | Medium | In Xenopus egg extracts, SLX1 is not required for ICL repair. The MLR domain of SLX4 is crucial for XPF-ERCC1 recruitment and also has an unanticipated function in recruiting SLX4 itself to the site of ICL damage. All essential SLX4 domains for ICL repair are located in the N-terminal half of the protein. | PMID:30576517 | Nucleic acids research |
| 2015 | Medium | Physical interaction between SLX4 and XPF requires a specific SLX4 region. The global minor SLX4 allele Y546C is defective in XPF interaction and cannot complement Fancp knockout cells for ICL-induced cytotoxicity or chromosomal aberrations. Several atypical XP phenotype-causing XPF missense mutations in the SLX4-interacting region cause XPF protein instability. | PMID:26453996 | DNA repair |
| 2014 | Medium | MUS81 point mutations that abolish interaction with SLX4 scaffold were identified. These MUS81 mutants fully rescued MMC hypersensitivity in MUS81 knockout murine cells but failed to rescue two human cell lines defective in MUS81, supporting an SLX4-dependent role for MUS81 in ICL repair in human cells. | PMID:25224045 | DNA repair |
| 2012 | Low | hSNM1B/Apollo co-immunoprecipitates with SLX4 (FANCP). SLX4 depletion reduces hSNM1B/Apollo nuclear foci formation and cellular TRF2 levels. Double knockdown of hSNM1B/Apollo and FANCP/SLX4 demonstrates epistatic interaction in ICL repair. | PMID:22907656 | Human molecular genetics |
| 2021 | Low | SLX4 cooperates with MUS81 to introduce DSBs after replication stress but also counteracts pathological targeting of demised replication forks by GEN1. This SLX4 function preventing GEN1 access to fork intermediates is independent of SLX4 interaction with endonucleases; ectopic expression of the HJ-binding protein RuvA inhibits DSBs in SLX4-deficient cells by preventing GEN1 chromatin association. | PMID:28290553 | Scientific reports |
| 2021 | Medium | SLX4-XPF functions as an upstream factor for accumulation of DDR proteins (ATR, FANCD2) at lacO/LacI-induced replication fork barriers on human chromosomes. The SLX4-ATR axis represses anaphase abnormalities induced by LacI binding. ATR and FANCD2 are interdependently recruited downstream of SLX4-XPF. | PMID:33347546 | The Journal of cell biology |
| 2021 | Low | PARP1 controls SLX4 recruitment to telomeres through its poly(ADP-ribosyl)ation activity; PARP1 depletion reduces SLX4 telomeric localization, which is rescued by wild-type but not catalytically inactive PARP1. SLX4 depletion elongates telomere length, and combined SLX4/PARP1 insufficiency further elongates telomeres and reduces telomere sister chromatid exchange. | PMID:33945829 | Life sciences |

## Citations

- PMID:12832395
- PMID:14528010
- PMID:16267268
- PMID:17636031
- PMID:19595721
- PMID:19595722
- PMID:19596235
- PMID:19596236
- PMID:20382573
- PMID:20670896
- PMID:21240275
- PMID:21240276
- PMID:21240277
- PMID:21464321
- PMID:22907656
- PMID:23093618
- PMID:23994477
- PMID:24012755
- PMID:24076221
- PMID:24080495
- PMID:24412650
- PMID:24726325
- PMID:24726326
- PMID:24794496
- PMID:25030699
- PMID:25224045
- PMID:25533185
- PMID:25533188
- PMID:25722289
- PMID:25753413
- PMID:25990736
- PMID:26113155
- PMID:26453996
- PMID:26490958
- PMID:26787556
- PMID:27131364
- PMID:28290553
- PMID:28877996
- PMID:30576517
- PMID:30692206
- PMID:31495888
- PMID:31584081
- PMID:31654852
- PMID:32398829
- PMID:33347546
- PMID:33945829
- PMID:34181713
- PMID:34272385
- PMID:34706224
- PMID:35166826
- PMID:35941380
- PMID:36288699
- PMID:37059091
- PMID:39291733
- PMID:40615546
- PMID:41002028
- PMID:41330930
