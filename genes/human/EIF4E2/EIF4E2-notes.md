# EIF4E2 / 4EHP (O60573) research notes

eIF4E homologous protein (4EHP). Class II eIF4E-family cap-binding protein.

## Core function: non-canonical cap binding that REPRESSES initiation
4EHP binds the m7G cap but cannot recruit eIF4G, so it competes with eIF4E and blocks
eIF4F assembly, repressing cap-dependent translation initiation.

- UniProt FUNCTION: "Recognizes and binds the 7-methylguanosine-containing mRNA cap during
  an early step in the initiation. Acts as a repressor of translation initiation ... In
  contrast to EIF4E, it is unable to bind eIF4G (EIF4G1, EIF4G2 or EIF4G3), suggesting that
  it acts by competing with EIF4E and block assembly of eIF4F at the cap"
- Cap binding structurally confirmed [PMID:17368478 "Structures of the human eIF4E homologous
  protein, h4EHP, in its m7GTP-bound and unliganded forms."]
- Original cloning [PMID:9582349 "Cloning and characterization of 4EHP, a novel mammalian
  eIF4E-related cap-binding protein."]

## 4EHP-GIGYF2 module + RQC
UniProt: "Component of the 4EHP-GYF2 complex ... In association with GIGYF2, assists
ribosome-associated quality control (RQC) by sequestering the mRNA cap, blocking ribosome
initiation and decreasing the translational load on problematic messages."
[PMID:32726578 RQC; PMID:22751931 development].

## miRNA silencing via CCR4-NOT / P-body
[PMID:28487484 "Here we show that the cap-binding eIF4E-homologous protein 4EHP is an integral
component of the miRNA-mediated silencing machinery. We demonstrate that the cap-binding
activity of 4EHP contributes to the translational silencing by miRNAs through the CCR4-NOT
complex."] Also controls IFNB1 via miR-34a negative feedback. P-body localization.

## SARS-CoV-2
nsp2-GIGYF2 enhances GIGYF2-EIF4E2 binding to repress IFNB1 translation [PMID:35878012].

## Ubiquitylation by HHARI
[PMID:14623119 "Human homologue of ariadne promotes the ubiquitylation of translation
initiation factor 4E homologous protein, 4EHP."] -> GO:0031625 ubiquitin protein ligase
binding (HHARI/ARIH1). Real interaction.

## IMPORTANT annotation caveats
- IBA/IEA "translation initiation factor activity" (GO:0003743) and "part of eIF4F complex"
  (GO:0016281) and "translational initiation" (GO:0006413) are MISLEADING: 4EHP does NOT
  promote initiation and is NOT a functional eIF4F component (cannot bind eIF4G). It is a
  REPRESSOR. These are phylogenetic/electronic transfers from the eIF4E family and should be
  MARK_AS_OVER_ANNOTATED or MODIFY toward repressor terms.
- A hypoxia-specific report (Uniacke) proposes 4EHP can support cap-dependent translation of
  specific mRNAs under hypoxia, but the dominant, well-established function is repression.
- Many protein binding IPI = HT interactome -> KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED.
- GO:1990261 pre-mRNA catabolic process (NAS ComplexPortal) -> MODIFY (mature mRNA decay).

## Core MF/BP for review
- MF: GO:0000340 RNA 7-methylguanosine cap binding (ACCEPT); GO:0045182 translation regulator /
  repressor; cap binding underlies repression.
- BP: GO:0045947 negative regulation of translational initiation (ACCEPT, core);
  GO:0072344 rescue of stalled cytosolic ribosome (ACCEPT, RQC); GO:0035278 miRNA silencing.


## Evidence re-review, 2026-09-20

Reviewed all 44 annotation rows against available primary interaction, cap-binding, translation, localization and quality-control studies and PAINT PTHR11960/PTN000238660. The earlier notes' assertion that EIF4E2 cannot recruit eIF4G was too broad. PMID:22678294 and full-text PMID:26854219 establish hypoxic translation and an EIF4E2/eIF4A/eIF4G3 complex. Restored translation-initiation factor, initiation process and eIF4F-complex rows; updated description and core functions. These roles coexist with GIGYF/4E-T-mediated repression. Current GO:0072344 requires release of an already stalled ribosome, whereas PMID:32726578 demonstrates suppressing additional rounds of initiation alongside RQC; its annotation was modified to negative regulation of initiation. The generated PN notes are historical context and were not rewritten. A neutral independent adjudication of the dual initiation/repression roles was requested through the coordinator; no duplicate report was launched. New primary source: [PMID:26854219](https://pubmed.ncbi.nlm.nih.gov/26854219/).


## 2026-09-21: focused eIF4F report incorporated; older categorical statements superseded

The earlier statements that EIF4E2 cannot form a productive eIF4F complex or cannot associate with any eIF4G paralog are too broad. PMID:26854219 full-text Results and Fig2C/S2D report endogenous human EIF4E2/eIF4A/eIF4G3 pull-downs, with eIF4G3 depletion impairing hypoxic translation and polysome recruitment. PMID:22678294 explicitly reports eIF4A recruitment. These primary observations support the retained GO:0016281 complex annotation and hypoxic initiation function alongside GIGYF-mediated repression; no new ribosome-binding claim is inferred from polysome association.

Read the entire `eif4f-complex-under-hypoxia/openscientist.md` report and its plot provenance JSON. It supports context-dependent initiation and repression but incorrectly treats complex composition as untested. Lack of a separately curated Complex Portal entry or experimental GO row is not a negative assay. PMID:28698298 analyzes GIGYF/4E-BP interfaces and cites earlier work for lack of eIF4G interaction; it does not test hypoxic EIF4G3 complex assembly. Its dorsal partner-binding surface lies opposite the cap pocket, contrary to the report's conflation of cap-stacking Trp/Tyr with a proposed dorsal binding defect. Binary binding and complex membership are separate questions.

Delivered plot code hard-codes claimed alignment identities and labels IBA/ISS 'weak'; it supplies no reproducible alignment supporting those numerical claims. They are not adopted as independently verified sequence results. The report is marked DISPUTED, while its supported dual-function findings are incorporated. The complex annotation stays ACCEPT; no new broad or redundant process annotation is added.
