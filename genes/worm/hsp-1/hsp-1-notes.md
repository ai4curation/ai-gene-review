# hsp-1 (HSC70 / HSP70A) curation notes

UniProt P09446 (Swiss-Prot), WormBase F26D10.3. Constitutive cytosolic Hsc70 of
C. elegans, orthologous to human HSPA8.

## Identity and expression

- hsp-1 (hsp70A) is one of six C. elegans hsp70 genes and is the constitutively
  expressed, mildly heat-inducible cognate member
  [PMID:2841196 "Transcripts of another gene, hsp70A, are abundant in control worms and are also increased (two- to six-fold) upon heat shock."].
- Localisation is cytosolic with nuclear entry during stress
  [PMID:19858203 "The nuclear export of DAF-16 requires heat shock transcription factor HSF-1 and Hsp70/HSP-1."].

## Chaperone cycle and co-chaperones (core function 1)

- HSP-1 is an ATP-dependent folding chaperone whose ATPase is regulated by BAG
  and J-domain co-chaperones; the C-terminal BAG fragment of UNC-23 regulates
  HSP-1 in muscle
  [PMID:25053410 "The molecular chaperone Hsc70 assists in the folding of non-native proteins together with its J domain- and BAG domain-containing cofactors."]
  [PMID:25053410 "C-terminal fragments of UNC-23 instead perform all Hsc70-related functions, like ATPase stimulation and regulation of folding activity, albeit with lower affinity than BAG-1."].
- STI-1/Hop bridges HSP-1 and Hsp90 (DAF-21)
  [PMID:19467242 "Analysis of proteins immunoprecipitated with anti-STI-1 antibody by mass spectrometry revealed that CeSTI-1 can bind with both Hsp70 and Hsp90 homologs like its mammalian counterpart."]
  [PMID:19559711 "Interestingly, we observed physical interactions with both chaperones Hsp70 and Hsp90, albeit only the interaction with Hsp90 is strong and inhibition of the Hsp90 ATPase activity can be observed upon binding of CeHop."].
- HSP-1 binds the TPR domain of the myosin chaperone UNC-45
  [PMID:23332754 "Accordingly, Hsp70 and Hsp90, which bind to the TPR domain of UNC-45, could act in concert and with defined periodicity on captured myosin molecules."].
- UNC-23 (BAG2 orthologue) recruits HSP-1 to muscle attachment structures
  [PMID:26435886 "We show that a functional GFP-tagged UNC-23 protein is expressed throughout development in several tissues of the animal, including body wall muscle and hypodermis, and associates with adhesion complexes and attachment structures"].

## Clathrin uncoating (core function 2; module synaptic_vesicle_endocytosis)

- Hsc70 is the ATPase that strips clathrin coats, and needs a J-domain
  co-chaperone (auxilin). C. elegans has a single auxilin, dnj-25, whose in
  vitro uncoating co-chaperone activity matches mammalian auxilin; RNAi of the
  worm auxilin blocks yolk endocytosis and freezes clathrin dynamics
  [PMID:11175756 "In vitro, the molecular chaperone Hsc70 uncoats clathrin-coated vesicles in an ATP-dependent process that requires a specific J-domain protein such as auxilin."]
  [PMID:11175756 "Here we show that C. elegans has a single auxilin homologue that is identical to mammalian auxilin in its in vitro activity."]
  [PMID:11175756 "most of these worms arrest during larval development, exhibit defective distribution of GFP-clathrin in many cell types, and show a marked change in clathrin dynamics"].
- Direct worm evidence that HSP-1 controls clathrin dynamics comes from the
  endosomal retromer study: loss of HSP-1 (like loss of the J-domain protein
  RME-8) causes endosomal clathrin to over-accumulate and become static
  [PMID:19763082 "Loss of SNX-1, RME-8, or the clathrin chaperone Hsc70/HSP-1 leads to over-accumulation of endosomal clathrin, reduced clathrin dynamics, and missorting of MIG-14 to the lysosome."].
- No study has yet scored synaptic coated-vesicle accumulation after hsp-1
  perturbation; the synaptic-vesicle uncoating role is inferred from the
  dnj-25 phenotype, the unc-26 (synaptojanin) coated-vesicle phenotype and
  mammalian HSC70 biochemistry. GOA carries no clathrin-coat-disassembly row
  for hsp-1, so this is recorded as a core function (GO:0072318) with the
  above support rather than as a NEW annotation.

## Non-core, evidence-supported roles

- Longevity: chaperone targets of HSF-1, including hsp-1, are required for
  the extended lifespan of insulin-signalling mutants
  [PMID:14668486 "Down-regulation of individual molecular chaperones, transcriptional targets of HSF-1, also decreased longevity of long-lived mutant but not wild-type animals."].
- Retrograde endosome-to-Golgi transport of MIG-14/Wntless is an indirect
  consequence of the endosomal clathrin role [PMID:19763082, quoted above];
  kept as non-core.

## Review decisions (summary)

All 26 GOA rows were reviewed in the earlier COMPLETE review (17 ACCEPT,
3 KEEP_AS_NON_CORE, 5 MODIFY of generic protein binding / chaperone terms).
This pass added: a propagation_review block for the IBA MODIFY row, the
auxilin reference (PMID:11175756), and a clathrin-coat-disassembly core
function grounded in PMID:11175756 and PMID:19763082.
