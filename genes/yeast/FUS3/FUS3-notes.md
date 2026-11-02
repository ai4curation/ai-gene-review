# FUS3 (YBL016W, P16892) curation notes

## Identity
- Mating-pheromone-response MAP kinase of *S. cerevisiae*; CMGC Ser/Thr kinase, TEY activation loop (Thr180/Tyr182), EC 2.7.11.24 [file:yeast/FUS3/FUS3-uniprot.txt "Dually phosphorylated on Thr-180 and Tyr-182 by STE7 in response"].
- Paralog: KSS1 (partially redundant; filamentation MAPK). Reviewed in parallel in genes/yeast/KSS1/ — binding-term choices kept consistent (Ste7 -> GO:0031434, Ste11 -> GO:0031435, Kss1-Fus3 and Bck2 rows removed).

## Activation (MAPK tier of Ste11 -> Ste7 -> Fus3 on Ste5)
- Thr180/Tyr182 phosphorylation required, STE11/STE7-dependent, not autocatalytic [PMID:1628831 "this modification occurs at two amino acids of FUS3, threonine-180 and tyrosine-182"].
- Ste7 is a dual-specificity kinase that activates Fus3 in vitro [PMID:8384702 "STE7 is a dual-specificity kinase that modifies FUS3 at the appropriate sites and stimulates its catalytic activity in vitro"].
- Reconstituted cascade Ste11 -> Ste7 -> Fus3 [PMID:8159759 "reconstituted a kinase cascade in which STE11 phosphorylates and activates STE7, which in turn phosphorylates the mitogen-activated protein kinase FUS3"].
- High-affinity Ste7 docking [PMID:8668180 "Kss1 and Fus3 could each form a tight complex (Kd of approximately 5 nM) with Ste7 in the absence of any additional yeast proteins"].
- Ste5 scaffold: two-hybrid binding with Ste11/Ste7/Fus3 [PMID:7851759, PMID:8062390]; Ste5-VWA/ms domain catalytically unlocks Fus3 for Ste7 [PMID:19303851 "We identify and structurally characterize a domain in Ste5 that catalytically unlocks Fus3 for phosphorylation by Ste7"].
- Ste5 FBD allosterically triggers Fus3 autophosphorylation (monophosphorylated Fus3), promoting Ste5 phosphorylation and dampening output (negative feedback) [PMID:16424299 "autoactivated Fus3 appears to have a negative regulatory role, promoting Ste5 phosphorylation and a decrease in pathway transcriptional output"].
- Fus3 activity is highest in 350-500 kDa Ste5 complex [PMID:10233162 "Fus3 has highest specific activity within a 350- to 500-kDa complex previously shown to contain Ste5, Ste11, and Ste7."].

## Substrates/outputs
- In vitro kinase assay: STE12 and FAR1 candidates [PMID:8334305 "FUS3 mediates transcription and G1 arrest by direct activation of STE12 and FAR1"].
- Dig1/Dig2 (Rst1/Rst2) are Fus3 substrates/partners that repress Ste12 [PMID:9094309 "Rst1 and Rst2 were prominent substrates in kinase reactions of Fus3 immune complexes from pheromone-treated cells"].
- Fus2 S84 phosphorylation drives Fus2 nuclear export (cell fusion) [PMID:22588722 "the mitogen-activated protein kinase Fus3p phosphorylates Ser 84 in Fus2p to drive nuclear export"].
- Tec1 T273 phosphorylation -> SCF-dependent degradation -> signaling specificity [PMID:15620357 "active Fus3 phosphorylates Tec1 on T273 in vitro"]; second site T276 needed for Cdc4 binding [PMID:19897738].
- Limits Kss1 activation [PMID:11583629 "active Fus3 limits the extent of Kss1 activation"].
- Kinase-independent inhibition of invasion crosstalk [PMID:9393860 "Fus3 has a different inhibitory activity that prevents the inappropriate activation of invasion by the pheromone response pathway"].

## Invasive growth
- Fus3 is a NEGATIVE regulator of haploid invasive growth [PMID:10652102 "Fus3 also inhibits haploid invasive growth by blocking cross-activation of invasive growth gene expression by the pheromone response signal cascade"]; fus3 deletion causes erroneous invasive growth [PMID:15620357]. So GO:0001403 (positive process) annotations are MODIFIED to GO:2000218.

## Ty1
- Fus3 suppresses Ty1 transposition post-translationally, requiring basal activation [PMID:9566871 "These findings suggest that Fus3 suppresses Ty1 transposition by destabilizing viruslike particle-associated proteins."]. Kept non-core under GO:0010526 (regulation-of-transposition terms are obsolete).

## Localization
- Nucleus and cytoplasm, shuttles; mating projection tips [PMID:11781566 "Ste5p, Ste7p and Fus3p also localized to tips of mating projections in pheromone-treated cells."].
- Gradient of active Fus3 emanating from shmoo tip [PMID:17952059].
- Nuclear shift during filamentous growth [PMID:18417610].
- UniProt "Periplasm" (-> GO:0042597) is an erroneous mapping (cites PMID:11781566 which shows projection tips). Removed.
- Mitochondrion from organelle proteomics only; stress granule from Jain 2016 core proteome — non-core/over-annotated.

## Interaction rows with doubtful sources
- PMID:23267104 (Meier et al., Streptococcus pneumoniae interactome) supports a Fus3-Tim12 IPI; the cached text has no yeast content. Removed as uninformative protein binding; not asserting the interaction is false.
- A7TJH8 is Vanderwaltozyma polyspora Ste5 (xeno interaction, PMID:23953117 evolution study).
