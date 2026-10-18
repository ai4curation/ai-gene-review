# GPR50 (Q13585, MTR1L_HUMAN) — curation notes

## What the gene is

617-aa class A (rhodopsin-like) 7TM receptor, cloned from human pituitary as "H9"
and named for its ~45% identity to the MT1/MT2 melatonin receptors
[PMID:8647286 "The cDNA, designated H9, encodes a protein of 613 amino acids that is 45% identical at the amino acid level to the recently cloned human Mel(1a) and Mel(1b) melatonin receptors."].
Unusual features: no N-linked glycosylation sites and an exceptionally long
(>300 aa) cytoplasmic C-terminal tail. Expression is concentrated in hypothalamus
and pituitary (UniProt TISSUE SPECIFICITY), notably in tanycytes and the
dorsomedial hypothalamus.

## The melatonin question — settled, and settled against melatonin

This is the one contested-ligand question for GPR50 that CAN be resolved.

- The founding paper reports the negative result directly:
  [PMID:8647286 "H9 transiently expressed in COS-1 cells did not bind [125I]melatonin or [3H]melatonin."]
- Clement et al. 2017 dissected why: swapping the second extracellular loop (E2)
  residues between MT1 and GPR50 produced reciprocal loss- and gain-of-melatonin
  responses, i.e. GPR50's E2 loop is the reason it is melatonin-blind
  [PMID:28898928 "showing how evolutionary processes appear to have selected for modifications in the E2 loop in order to make GPR50 unresponsive to melatonin."]
- The 2026 cryo-EM paper restates it and provides the structural comparison
  [PMID:41666959 "However, melatonin does not bind to GPR50 (Clement et al., 2017), and GPR50 is not directly involved in the melatonin-related pathways."]
- The Jockers lab states it flatly in the 2025 KO paper
  [PMID:40091563 "GPR50 is an orphan GPCRs belonging to the melatonin receptor subfamily and represents 45% sequence homology with melatonin MT1 and MT2 receptors in humans but does not bind melatonin or any other known ligand"]

**Curation consequence.** GOA carries `GO:0008502 melatonin receptor activity`
(IEA, GO_REF:0000002) with `WITH/FROM = InterPro:IPR000025`. IPR000025 is the
*melatonin receptor family* signature — GPR50 matches it by descent, not by
pharmacology. This is a textbook family-signature over-propagation and the
primary literature, including the paper that first expressed the protein,
contradicts it. Action: **REMOVE**.

## Is GPR50 a G-protein-coupled receptor at all? Yes — constitutively.

- Cryo-EM of the **ligand-free** receptor at 3.4 A plus TRUPATH BRET2 basal-activity
  profiling: [PMID:41666959 "We showed that GPR50 exhibits moderate constitutive activity through interaction with Gα12."]
  and [PMID:41666959 "By contrast to MT1 and MT2, which primarily interact with Gαi/o and inhibits cAMP pathway, GPR50 activates Gα12 but also moderately activates Gαi/o, raising the possibility that it is involved in the multisignaling pathways."]
- Independently, GPR50-KO mice show a ligand-independent G12/13-RhoA output:
  [PMID:40091563 "Collectively, we show that GPR50 acts as an inhibitor of neurite growth and cell migration in the brain by activating the G12/13 protein-RhoA pathway."]

So the *receptor activity* and the *G12/13-RhoA* coupling are supported by two
laboratories using orthogonal methods (structure/BRET vs. KO mice + RhoA assays),
and both describe activity in the **absence** of an added agonist.

## The contested deorphanization: L-LEN

[PMID:41495223 "further deorphanize GPR50 with the neuropeptide Little-LEN (L-LEN) as its endogenous ligand. L-LEN selectively binds GPR50 and modulates cellular activities through downstream Gαi signaling in tissue."]
L-LEN is a 10-aa peptide from the ProSAAS (PCSK1N) precursor, captured from mouse
hypothalamic extract by a genetically-encoded photo-cross-linker sited in the GPR50
binding interface
[PMID:41495223 "Only the top-enriched hit from the cross-linked peptide profiling experiment, a 10-amino-acid-long orphan neuropeptide L-LEN, activated GPR50 in a dose-dependent manner with nanomolar affinity, whereas other candidates, even those from the same precursor (ProSAAS), did not"]
with Gi-type coupling
[PMID:41495223 "suggesting that GPR50 dominantly couples with Gαi. We next applied the fluorescence cAMP sensor G-Flamp2 to directly monitor GPR50-dependent Gi signaling28."]

**Why this is not yet settled.**
1. The cryo-EM paper, published five weeks later, still describes the receptor as
   having no characterized agonist:
   [PMID:41666959 "Although endogenous agonists have not been characterized, GPR50 may have its own signaling activity, which is undefined at present."]
   It does not cite or engage the L-LEN result. Two 2026 papers asserting opposite
   states of knowledge, neither addressing the other, is not consensus.
2. The pathway assignments disagree. L-LEN => Gai/cAMP inhibition; cryo-EM and the
   KO mice => Ga12/13-RhoA (with Gai/o only "moderate"). A single receptor can be
   promiscuous, but nobody has reconciled the two readouts in the same system.
3. L-LEN is a single-laboratory result. No independent replication yet.

Honest action: `UNDECIDED` is not applicable here because there is no GOA row for
an L-LEN pairing — nothing to adjudicate. The point is recorded in
`suggested_questions` and in the top-level `description` as a stated dispute.

## Non-receptor / receptor-adjacent biology that IS well supported

- **Negative regulation of MT1 by heterodimerization.** GPR50 heterodimerizes
  constitutively with MT1 and MT2; in the MT1 heterodimer it abolishes
  high-affinity agonist binding and G-protein coupling
  [PMID:16778767 "Whereas the association between GPR50 and MT(2) did not modify MT(2) function, GPR50 abolished high-affinity agonist binding and G protein coupling to the MT(1) protomer engaged in the heterodimer."].
  Note the irony: GPR50's best-documented connection to melatonin biology is as an
  *inhibitor of a melatonin receptor*, which is the opposite of "melatonin receptor
  activity".
- **Calpain cleavage and nuclear translocation of the C-terminal domain.** CAPN1
  cleaves between Phe-408 and Ser-409; the released CTD enters the nucleus and
  binds GTF2I/TFII-I to regulate FOS transcription
  [PMID:31900622 "Activation of the calcium-dependent calpain protease cleaves off the CTD from the transmembrane-bound GPR50 core domain between Phe-408 and Ser-409 as determined by MALDI-TOF-mass spectrometry."].
  This is what the `GO:0005634 nucleus` EXP annotation records — it is the cleaved
  fragment, not the intact 7TM receptor, that is nuclear.
- **NOGO-A (RTN4) interaction and synaptic enrichment**
  [PMID:19699797 "we identified neurite outgrowth inhibitor NOGO-A as an interacting partner of GPR50 by yeast two-hybrid studies. We confirmed the interaction in mammalian cells and found an enrichment of both Gpr50 and neuronal Nogo-A at the synapse."]
  — the source of `GO:0014069 postsynaptic density`. Note the 2009 paper reported
  GPR50 *increasing* neurite length on overexpression, whereas the 2025 KO paper
  reports GPR50 *restraining* neurite outgrowth; the KO/loss-of-function direction
  is the more reliable one.
- **KAT5/TIP60 and glucocorticoid receptor signalling** [PMID:21858214].
- **ADAM17 interaction / Notch in HCC** [PMID:32405532].

## Actions taken

| Term | Evidence | Action |
|---|---|---|
| GO:0008502 melatonin receptor activity | IEA (InterPro:IPR000025) | **REMOVE** |
| GO:0004930 GPCR activity | IBA, IEA, TAS | ACCEPT (constitutive) |
| GO:0007186 GPCR signaling pathway | IBA, IEA, TAS | ACCEPT |
| GO:0005886 plasma membrane | IBA, IEA, IDA, EXP, TAS | ACCEPT |
| GO:0005634 nucleus | IEA, EXP | ACCEPT (cleaved CTD) |
| GO:0014069 postsynaptic density | IEA, EXP | ACCEPT |
| GO:0016020 membrane | IEA | ACCEPT (redundant with plasma membrane) |
| GO:0005515 protein binding | IPI x3 | MARK_AS_OVER_ANNOTATED |
| GO:0007267 cell-cell signaling | TAS (PMID:8647286) | MARK_AS_OVER_ANNOTATED |

No NOT/negated qualifiers are present in the GOA file.
