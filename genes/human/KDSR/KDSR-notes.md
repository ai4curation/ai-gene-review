# KDSR (Q06136) review notes

Gene: KDSR / FVT1 / SDR35C1, human. 332 aa, ER membrane, short-chain dehydrogenase/reductase (SDR) family.

## Core biology (verified)
KDSR catalyses the **second step of de novo sphingolipid biosynthesis**: the NADPH-dependent
reduction of 3-ketodihydrosphingosine (3-ketosphinganine / 3-oxosphinganine, "3KDS") to
dihydrosphingosine (sphinganine). This follows the SPT-catalysed condensation of L-serine +
palmitoyl-CoA and precedes N-acylation by the ceramide synthases (CERS).
- EC 1.1.1.102; RHEA:22640; the physiological direction is reduction (right-to-left in the UniProt
  Rhea reaction `sphinganine + NADP(+) = 3-oxosphinganine + NADPH + H(+)`).
- The only KDS reductase in mammals; silencing directly reduces cellular reductase activity
  [PMID:19141869 "FVT1 is the principal 3-ketosphinganine reductase in mammalian cells"].
- Human FVT-1 rescues TSC10-null yeast and purified recombinant hFVT-1 has NADPH-dependent KDS
  reductase activity in vitro [PMID:15328338].

## Localization / topology (verified)
ER membrane, multi-pass; the large hydrophilic catalytic domain (with the active-site residues)
faces the cytosol [PMID:15328338; PMID:1317856]. UniProt: two C-terminal TM helices (271-291,
294-314), cytoplasmic catalytic domain 26-270. GO:0098554 (cytoplasmic side of ER membrane) is
therefore the most precise CC.

## Disease (verified)
- Erythrokeratodermia variabilis et progressiva 4 (EKVP4, MIM:617526), a recessive keratinization
  disorder [PMID:28575652; PMID:28774589 (not cached)].
- A spectrum of keratinization disorders with/without thrombocytopenia; loss of functional KDSR
  impairs proplatelet formation -> thrombocytopenia [UniProt DISEASE notes; PMID:30467204 (not cached)].
- Was originally cloned as FVT-1 at a t(2;18) follicular-lymphoma translocation [PMID:8417785].

## Cancer relevance
In some cancers KDSR clears the toxic intermediate 3KDS; KDSR loss causes 3KDS accumulation,
ER dysfunction and proteotoxic stress -> potential therapy target [PMID:36170811 (full text cached)].

## Annotation-level notes / issues
- GOA MF term carried = **GO:0047560 "3-dehydrosphinganine reductase activity"** (current label
  confirmed via OLS). Multiple EXP/IDA/IMP/IBA/IEA/TAS lines all converge on this MF -> core.
- Core BP = GO:0030148 sphingolipid biosynthetic process (verified: EXP/IMP PMID:19141869, IBA,
  TAS Reactome R-HSA-1660661). GO:0006666 (3-keto-sphinganine metabolic process) is a valid
  precise BP for the substrate metabolism.
- GO:0006686 sphingomyelin biosynthetic process (IDA PMID:36170811) and GO:0006688
  glycosphingolipid biosynthetic process (IDA PMID:34080016) are downstream pathway products of
  the sphinganine KDSR makes; KDSR is genuinely upstream and required, but these are pathway-level
  over-annotations (KDSR does not itself make SM/GSL). 34080016 is a review that never mentions
  KDSR -> MARK_AS_OVER_ANNOTATED.
- GO:0005576 extracellular region (TAS PMID:8417785, ProtInc): based on the 1993 "putatively
  secreted protein" prediction, superseded by the multi-pass ER-membrane topology. REMOVE
  (demonstrably wrong legacy prediction, not an experimental localization).
- PMID:15364918 (IP3R1 lateral-diffusion paper, MGI-assigned to 3 KDSR lines) is an evident
  wrong-PMID mis-citation: abstract is entirely about IP3R1/actin/4.1N in neurons, no KDSR.
  Flagged via reference_review WRONG_IDENTIFIER; the underlying MF/CC/BP are correct and
  well-supported elsewhere, so kept ACCEPT/KEEP but not relied on this ref.
- The 4x GO:0005515 protein binding IPIs (Y2H interactome PMID:32814053: KIF1B, HSPB1, TTR, WFS1)
  are uninformative high-throughput interactions -> MARK_AS_OVER_ANNOTATED (per policy, not REMOVE).
- GO:0016020 membrane (HDA proteomics PMID:19946888) correct but redundant with ER membrane -> non-core.
