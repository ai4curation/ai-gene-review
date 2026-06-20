# RGA (REPRESSOR OF ga1-3 / RGA1 / GRS; AT2G01570; UniProt Q9SLH3) — curation notes

## Identity and structure
- One of five Arabidopsis DELLA proteins (GAI, RGA, RGL1, RGL2, RGL3); DELLA subfamily of the plant-specific GRAS family of putative transcriptional regulators [PMID:9490740 "RGA was found to be a member of the VHIID regulatory family, which includes the radial root organizing gene SCARECROW and another GA signal transduction repressor, GAI"].
- 587 aa. N-terminal DELLA/VHYNP regulatory region (DELLA motif 44–48, VHYNP 89–93) + C-terminal GRAS domain (212–581: LRI, VHIID, LRII, PFYRE, SAW subdomains) (UniProt features).
- DELLA motif required for GA-induced degradation but NOT for SLY1 binding [PMID:15155881 "the N-terminal DELLA domain ... is not required for protein-protein interaction with SLY1 in yeast ... suggesting that its role is in a GA-triggered conformational change"].

## Core function: nuclear repressor of GA signaling
- Negative regulator of GA signal transduction; recessive rga partially suppresses GA-deficient ga1-3 [PMID:9490740 "the recessive rga mutation is able to partially suppress phenotypic defects of the Arabidopsis gibberellin (GA) biosynthetic mutant ga1-3"].
- RGA + GAI partially redundant; RGA dominant [PMID:11606552 "RGA and GAI have partially redundant functions in maintaining the repressive state of the GA-signaling pathway, but RGA plays a more dominant role than GAI"].
- Nuclear localized (GFP-RGA in onion epidermis and transgenic Arabidopsis) [PMID:9490740 "green fluorescent protein-RGA fusion protein is localized to the nucleus in onion epidermal cells"; PMID:11449051 "The green fluorescent protein (GFP)-RGA fusion protein was localized to nuclei in transgenic Arabidopsis"]. Accumulates in nucleus on cold [PMID:28412546].

## Regulatory switch: GA-GID1-SCF(SLY1) degradation
- GA-bound GID1 receptors bind RGA DELLA region [PMID:16709201 "in vivo interaction in the presence of GA(4) between each AtGID1 and the Arabidopsis DELLA proteins"; PMID:17416730 "the DELLA domain functions as a receiver domain for activated GA receptors"].
- GA-GID1 promotes RGA-SLY1 binding -> SCF(SLY1) ubiquitination -> 26S degradation [PMID:17194763 "the GA-GID1 complex promotes the interaction between RGA and the F-box protein SLY1, a component of the SCF(SLY1) E3 ubiquitin ligase that targets the DELLA protein for degradation"; PMID:15155881; PMID:15161962].
- GA rapidly reduces RGA protein -> derepression [PMID:11449051 "the GA signal appears to derepress the GA signaling pathway by degrading the repressor protein RGA"].
- Lys-29-linked ubiquitin chains dominant for RGA degradation; RGA is the SUBSTRATE here (relevant to rejecting GO:0042176 "regulation of protein catabolic process") [PMID:19717618 "Lys-29-linked ubiquitin chains seem to be the major linkage triggering degradation of DELLA proteins"].
- Proteolysis-independent inactivation also possible via GID1 binding [PMID:18827182 "GA-bound GID1 can block DELLA repressor activity by direct protein-protein interaction with the DELLA domain"].

## KEY mechanistic point: RGA has NO DNA-binding domain — acts as transcriptional cofactor
This is decisive for MF curation. RGA/DELLA cannot be a sequence-specific DNA-binding transcription factor.
- [PMID:24821766 "because DELLA lacks a DNA-binding domain, intermediate protein(s) mediating the DELLA/DNA interaction are believed to be necessary for activating DELLA target genes"].
- [PMID:25035403 "DELLAs associate with the promoters of DELLA-induced genes even though DELLA proteins lack DNA binding motifs"].
- [PMID:21245327 "DELLA and SCL3 are likely to associate with target DNA indirectly by binding to other transcription factors, because these proteins do not contain any known DNA binding domain"].

Therefore GO:0003700 (DNA-binding transcription factor activity, from PMID:17933900 IDA, PMID:11449051 TAS, PMID:11118137 ISS) -> MODIFY to GO:0003712 transcription coregulator activity.
And GO:0000976 (transcription cis-regulatory region binding) from Y1H/eY1H screens (PMID:22037706, 25352272, 25533953, 31806676) -> REMOVE (RGA has no DBD; promoter binding is indirect/artifactual in Y1H).
GO:1990841 (promoter-specific chromatin binding, PMID:29255112) -> MARK_AS_OVER_ANNOTATED (in vivo occupancy real but mediated by CCA1).

## Two arms of transcriptional cofactor activity
1. INHIBITION/titration of DNA-binding TFs (the classic "sequestration" model):
   - PIFs (bHLH): [PMID:18216857 "DELLAs block PIF4 transcriptional activity by binding the DNA-recognition domain of this factor"]; also PIF1/PIF6/SPT [PMID:20093430].
   - BZR1 (BR): [PMID:22820377 "RGA specifically interacts with BZR1 to inhibit its abilities to bind DNA and regulate transcription"].
   - SPL (flowering): [PMID:22942378 "DELLA directly binds to ... SQUAMOSA PROMOTER BINDING-LIKE (SPL) transcription factors"].
   - CCA1 (clock/MYB): [PMID:29255112 "RGA suppressed the ability of CCA1 to activate expression from the DWF4 promoter"].
   - ATML1/PDF2 (HD-ZIP): [PMID:24989044 "DELLA proteins interact directly with ATML1 and its paralogue PDF2"].
   - CO (photoperiod): [PMID:26801684 "the interaction of CO with NF-YB2 is inhibited by the DELLA protein, RGA"].
   - ANAC106 (NAC): [PMID:40755058 "DELLA proteins physically interact with ANAC106 ... inhibiting its transcriptional activation capacity"].
   -> Supports NEW GO:0140297 (DNA-binding transcription factor binding) and GO:0140416 (transcription regulator inhibitor activity).
2. COACTIVATION via IDD scaffolds (the newer "DELLA as coactivator" model):
   - IDDs bridge DELLA to DNA: [PMID:24821766 "a luciferase reporter controlled by the SCL3 promoter was additively transactivated by REPRESSOR of ga1-3 (RGA) and IDDs"].
   - GAF1/IDD2: [PMID:25035403 "DELLAs and TPR act as coactivators and a corepressor of GAF1, respectively"].
   - SCL3 (GRAS, attenuator of DELLA): [PMID:21245327 "SCL3 autoregulates its own transcription by directly interacting with DELLA"].
   -> Supports ACCEPT of GO:0045893 (positive regulation of DNA-templated transcription, PMID:24821766 IDA) and NEW GO:0003712.
- DELLAs do both simultaneously: [PMID:25035403 "DELLAs turn on or off two sets of GA-regulated genes via dual functions, namely titration and coactivation"].

## Pleiotropy (KEEP_AS_NON_CORE for downstream developmental processes)
- Vegetative growth / leaf / trichome / stem (rga gai rescue ga1-3): [PMID:11606552 "Phenotypes rescued include abaxial trichome initiation, rosette radius, flowering time, stem elongation, and apical dominance"]. Note: "negative regulation of developmental vegetative growth" (GO:1905614) is the correctly-signed CORE vegetative annotation; the negated unsigned GO:1905613 is contradictory -> REMOVE.
- Seed germination/dormancy: RGA minor/redundant vs RGL2 [PMID:24989044]. Note PMID:11606552 NOT-annotations: rga gai does NOT rescue germination or flower development defects of ga1-3 -> these negated annotations are correctly ACCEPTed [PMID:11606552 "seed germination and flower development defects were not restored"].
- Anther/pollen (meiotic cytokinesis, tapetum): [PMID:27621423; PMID:33660280 RGAT1; PMID:40755058 ANAC106].
- Cold: [PMID:28412546 "under cold conditions, PFDs accumulate into the nucleus through a DELLA-dependent mechanism"].
- Far-red/red light: RGA transcription controlled by PIL5 [PMID:17449805 "PIL5 increases the expression of two GA repressor (DELLA) genes, GA-INSENSITIVE (GAI) and REPRESSOR OF GA1-3 (RGA/RGA1), in darkness"].

## Action summary rationale
- Generic GO:0005515 protein binding entries -> mostly MARK_AS_OVER_ANNOTATED (genuine interactions but uninformative term), captured instead by NEW GO:0140297 / GO:0140416 / GO:0003712. Two REMOVE: PMID:19429606 (FRIGIDA paper, not about RGA) and the GO:0042176 misassignment.
- GO:0000976 cis-regulatory binding (4x Y1H screens) -> REMOVE (no DBD).
- GO:0003700 DNA-binding TF activity (3x) -> MODIFY to GO:0003712.
- Nucleus (many) -> ACCEPT.
- GA signaling / negative regulation of GA signaling / response to GA -> ACCEPT (core).

## Deep research synthesis (Falcon / Edison Scientific, file:ARATH/RGA/RGA-deep-research-falcon.md)
The Falcon deep-research report (2026) corroborates and extends the core curation calls; it adds no GO IDs but supports several load-bearing decisions:
- Confirms RGA is a nuclear, non-catalytic transcriptional regulator that acts via protein-protein interactions, not direct DNA binding [falcon "RGA does not bind DNA directly; instead, it acts through protein–protein interactions with transcription factors (TFs) and chromatin components, including histone H2A, to reprogram gene expression."; "DELLAs are nucleus-localized regulators that generally do not bind DNA directly and instead control transcription by interacting with many TFs and transcriptional regulators, with chromatin association detectable by ChIP/ChIP-seq"]. This independently supports MODIFY of GO:0003700 -> GO:0003712, the NEW GO:0140297/GO:0003712, and REMOVE of the GO:0000976 Y1H cis-regulatory-region-binding annotations.
- Confirms the canonical GA-GID1-SCF(SLY1) degradation switch [falcon "GA–GID1 signaling inactivates RGA primarily via SCF^SLY1-dependent ubiquitination and proteasomal degradation"; "GA–GID1 binds the **DELLA domain** of RGA (conserved DELLA/LExLE/VHYNP motifs) to form a GA–GID1–RGA complex"]. Supports the GA-signaling ACCEPTs and the receptor-binding proposed term.
- Supports DELLA as a dual coactivator/corepressor (titration + coactivation), consistent with ACCEPT of GO:0045893 and the coregulator MF [falcon "This supports a modern view of DELLAs as context-dependent transcriptional regulators (coactivator/corepressor roles) rather than simple repressors."]. ChIP-seq/RNA-seq: RGA is a direct repressor of 129 genes and direct activator of 280 genes (huang2023).
- New mechanistic context (not yet a GO call): RGA is recruited to promoters by TFs via the GRAS LHR1 subdomain and stabilized on chromatin via histone-H2A binding through the PFYRE subdomain (TF-RGA-H2A complex; huang2023 Nature Plants, huang2024 Nat Commun). Phosphorylation in PolyS/PolyS-T regions enhances H2A binding without changing nuclear localization or GA-induced degradation; O-fucosylation enhances and O-GlcNAcylation inhibits DELLA-TF interactions. Structural work (Dahal 2025 PNAS; Islam 2025) supports a proteolysis-independent suppression arm in which GID1 binding blocks RGA-IDD TF interactions. These could motivate future MF terms (histone binding / chromatin) but lack a verifiable GO ID in the current GOA/UniProt, so no NEW annotation was added.

No UNDECIDED actions existed in the review (all annotations already adjudicated), and the new evidence does not warrant weakening any existing decision.

## Validation
`uv run ai-gene-review validate genes/ARATH/RGA/RGA-ai-review.yaml` -> Valid (1 non-blocking warning about mixed actions on GO:0010029, which reflects the genuine distinction between negated NOT-annotations and the positive non-core germination role).
