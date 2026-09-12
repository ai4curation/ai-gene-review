# GIGYF2 (Q6Y7W6) research notes

GRB10-interacting GYF protein 2 (TNRC15, PARK11). Paralog of GIGYF1. GIGYF family.

## Core function: 4EHP-GIGYF2 translational repressor / RQC
GIGYF2 is the key scaffold of the 4EHP-GYF2 complex (EIF4E2 + GIGYF2 + ZNF598), a
translation-initiation repressor that also couples repression to mRNA decay.

- UniProt FUNCTION: "Key component of the 4EHP-GYF2 complex, a multiprotein complex
  that acts as a repressor of translation initiation ... acts as a factor that bridges
  EIF4E2 to ZFP36/TTP, linking translation repression with mRNA decay ... Also recruits
  and bridges the association of the 4EHP complex with the decapping effector protein DDX6"
- RQC role [PMID:32726578 "This negative feedback loop is mediated by two translation
  inhibitors, GIGYF2 and 4EHP."] and ["In association with EIF4E2, assists ribosome-associated
  quality control (RQC) by sequestering the mRNA cap, blocking ribosome initiation and
  decreasing the translational load on problematic messages." (UniProt)]. GIGYF2/EIF4E2 work
  downstream and independently of ZNF598.
- 4EHP-GIGYF2 essential for mammalian development; direct EIF4E2 interaction required to
  stabilize both proteins [PMID:22751931 "GIGYF2 directly interacts with m4EHP, and this
  interaction is required for stabilization of both proteins. Disruption of the m4EHP-GIGYF2
  complex leads to increased translation and perinatal lethality in mice."]

## miRNA silencing / mRNA destabilization
GIGYF2 binds AGO2 (via GYF domain) and acts as a silencing effector: [PMID:27157137
"upon tethering to a reporter mRNA, GIGYF2 exhibits strong, dose-dependent silencing
activity, involving both mRNA destabilization and translational repression."]

## SARS-CoV-2 nsp2 / interferon repression
nsp2 binds GIGYF2 and enhances GIGYF2-EIF4E2 binding to repress IFNB1 translation:
[PMID:35878012 "Here, we document a mechanism by which the NSP2 protein impedes IFN-β
expression through translational repression of Ifnb1 mRNA by coopting the GIGYF2/4EHP
complex"] -> GO:0060339 negative reg type I IFN, GO:0060090 molecular adaptor activity.

## IGF/GRB10 + neuronal localization
[PMID:20670374 "GIGYF2 is present in endosomal compartments in the mammalian brains and
enhances IGF-1-induced ERK1/2 activation."] Localized in neuronal perikarya and proximal
dendrites; did not localize to Lewy bodies. Basis of perikaryon/proximal dendrite/endosome
and IGF signaling annotations.

## GYF domain / proline-rich binding
[PMID:20696395 "Conserved beta-hairpin recognition by the GYF domains of Smy2 and GIGYF2 in
mRNA surveillance and vesicular transport complexes."] GYF domains recognize proline-rich
sequences -> GO:0070064 proline-rich region binding. Also reports SG/ER/Golgi localization.

## Disease
PARK11 / Parkinson disease 11 susceptibility — UniProt notes association is "however unclear"
and "GIGYF2 does not play a major role in Parkinson disease etiology". Also neurodevelopmental/
neuropsychiatric phenotypes with compromised GIGYF2 (PMID:32726578).

## Annotation plan (highlights)
- Core MF: GO:0000900 mRNA regulatory element binding translation repressor activity (ACCEPT);
  GO:0060090 molecular adaptor activity (ACCEPT, bridges EIF4E2-TTP/DDX6); GO:0008190 eIF4E
  binding could be added as NEW.
- Core BP: GO:0045947 neg reg translational initiation (ACCEPT); GO:0072344 rescue of stalled
  cytosolic ribosome (ACCEPT, RQC); GO:0017148 neg reg translation (ACCEPT); GO:0061157 mRNA
  destabilization, GO:0016441 post-transcriptional gene silencing (ACCEPT non-core/ACCEPT).
- protein binding IPI x many -> KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED (HT interactome).
- GO:0045296 cadherin binding (HDA, BioID proximity) -> MARK_AS_OVER_ANNOTATED (proximity artifact).
- GO:1990261 pre-mRNA catabolic process (NAS ComplexPortal) -> MODIFY (mature mRNA decay).
- Localizations (cytosol, SG, endosome, ER, Golgi, membrane, perikaryon, dendrite, vesicle):
  cytosol/SG/perikaryon/dendrite/endosome ACCEPT; membrane/vesicle/ER/Golgi KEEP_AS_NON_CORE
  or MARK_AS_OVER_ANNOTATED (likely from overexpression/HT).
- IGF receptor signaling (IBA + IMP) -> KEEP_AS_NON_CORE (legacy GRB10 role).
