# AVPR2 curation notes

`just deep-research-falcon human AVPR2 --fallback perplexity-lite` failed in this workspace because the Falcon and Perplexity providers were both unavailable to the `deep-research-client`, so this review is based on the GOA/UniProt seed, cached publications, cached Reactome records, the vasopressin receptor and generic GPCR-cAMP-PKA modules, and the local GO-CAM review for `gomodel:67e5e74400004286`.

## Core function

AVPR2 is the human V2 vasopressin receptor, a seven-transmembrane GPCR cloned from human kidney that mediates the antidiuretic response to AVP: antidiuretic hormone binds receptors on renal collecting-tubule cells, "stimulates adenylyl cyclase and promotes the cyclic AMP-mediated incorporation of water pores" [PMID:1534149]. The receptor couples the extracellular Arg-vasopressin ligand to Gs and adenylyl cyclase. Later structural papers directly visualized human AVP-bound V2R in a Gs-coupled active state: one solved a "cryo-EM structure of human AVP-V2R-Gs signaling complex" [PMID:33664408], and the companion structure described a full-length, Gs-coupled human V2R bound to AVP [PMID:33742150].

The renal physiology is likewise core. Mammalian V2R "regulates aquaporin-2-mediated water reabsorption via activation of the Gs protein/adenylyl cyclases/cAMP pathway" [PMID:19440390]. The reviewed GO-CAM `67e5e74400004286` is a compact instance of this same branch: extracellular Arg-vasopressin activates plasma-membrane AVPR2, AVPR2 directly activates GNAS, and GNAS directly stimulates ADCY6 to make cAMP.

## Location and trafficking

The receptor is a plasma-membrane multipass protein as a prerequisite for its ligand-binding function. Activated AVPR2 also internalizes through beta-arrestin-positive endosomes: V2R and V1aR are "endocytosed by way of beta-arrestin-dependent processes" and beta-arrestin remains associated with V2R in endosomes [PMID:14757828]. Those endosomal and clathrin-coated-vesicle locations are real trafficking states, but they are non-core compared with receptor activity at the plasma membrane.

ER and Golgi rows come from ProtInc/TAS evidence on a plasma-membrane receptor. AVPR2 traverses the secretory pathway, but these root-organelle locations are not established as native resident compartments for endogenous receptor, so the ER and Golgi rows are over-annotations under the organelle-transit policy.

## Process specificity

The V2 receptor's core pathway is `GO:0007189` adenylate cyclase-activating G protein-coupled receptor signaling pathway. Broader `G protein-coupled receptor signaling pathway`, `adenylate cyclase-modulating G protein-coupled receptor signaling pathway`, and `activation of adenylate cyclase activity` rows are kept or refined only when their own evidence supports AVPR2 coupling to Gs/cAMP. Broad or indirect physiological rows from rodent AVPR2, such as regulation of blood pressure, gene expression, intracellular signaling, and urine volume, are downstream renal consequences rather than the molecular work AVPR2 itself performs.

The `PMID:10880054` hemostasis row is a special non-core branch. The abstract reports that DDAVP stimulates von Willebrand factor secretion in V2R-transfected HUVECs and that human lung microvascular endothelial cells express endogenous V2R; the effect is cAMP/PKA dependent and V2R-antagonist sensitive [PMID:10880054]. This supports a V2R-mediated endothelial secretory response, but not the receptor's main renal function.

## Questionable rows

The `PMID:9322919` annotations require caution. The paper is foregrounded as a human V3/AVPR1B receptor study, and its abstract states that V3 pharmacology is "clearly distinct from that exhibited by the human V1R and V2R" [PMID:9322919]. The paper may have used AVPR2 as a comparator in the full text, so the receptor-activity row is kept because the term is well established independently; the negative-proliferation IDA row is left undecided because the abstract attributes the thymidine and cAMP assays to CHO-V3 cells rather than V2R.

Bare `GO:0005515` rows from GIP, TMEM147, alpha-arrestin/ARRDC4 and HuRI interactome papers are removed under the project protein-binding policy. The named interactions may be useful leads for trafficking or folding, but `protein binding` is not an informative molecular-function annotation for AVPR2.
