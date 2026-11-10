# HDAC5 (human, Q9UQL6) review notes

**Deep research status:** falcon (Edison) deep research failed with an authentication
error on 2026-10-24, and no other provider key was available. No `-deep-research-*.md`
file exists for this gene. The notes below come from the cached publications in
`publications/`, the UniProt record (`HDAC5-uniprot.txt`), and targeted web searches
(used only to resolve PMIDs, which were then cached with `just fetch-pmid`).

## Why this gene was reviewed

The rule-based screen `projects/FUNCTION_REQUIREMENT_RULES.md` (FRR:0009) flagged
HDAC5's experimental `GO:0001216 DNA-binding transcription activator activity` (IMP,
PMID:19071119) because HDAC5 has no sequence-specific DNA-binding domain. Related rows
that assert DNA binding: `GO:0000978` (IDA, PMID:24413532) and `GO:0000976`
contributes_to (IDA, PMID:19351956).

## Identity and domain architecture

- Class IIa histone deacetylase, HD type 2 subfamily; 1122 aa; N-terminal extension
  with the MEF2-binding motif and the signal-responsive 14-3-3 sites (Ser259, Ser498),
  C-terminal HDAC catalytic domain from about residue 832
  [PMID:10220385 "HDAC5 is highly homologous to HDAC4 (51% identity, 63% similarity), with 1,123 aa and a catalytic region beginning at amino acid 832"].
- UniProt: "Belongs to the histone deacetylase family. HD type 2 subfamily."
- No DNA-binding domain anywhere in the protein (UniProt features list only the
  deacetylase domain, NLS/NES, disordered and coiled-coil regions).

## Catalytic activity: weak, probably not the main mechanism

- Original cloning paper: recombinant HDAC5 immunoprecipitates deacetylate all four
  core histones but less well than HDAC1/HDAC6, and HDAC5 co-purifies with HDAC3
  [PMID:10220385 "HDAC1 and HDAC6 possess comparable activity, whereas that of HDAC4 and HDAC5 is somewhat reduced."]
  [PMID:10220385 "HDAC5 associates only with HDAC3, though it is possible that the expression levels were too low to detect other associated factors."]
- Activity of class II HDAC immunoprecipitates depends on the associated
  SMRT/N-CoR-HDAC3 complex
  [PMID:11804585 "In vitro reconstitution experiments indicate that HDAC4 and other class II HDACs are inactive in the context of the SMRT/N-CoR-HDAC3 complex and do not contribute to its enzymatic activity."]
- Vertebrate class IIa HDACs carry His in place of the catalytic Tyr; the reverse
  mutation boosts activity about 1000-fold in HDAC4, and HDAC5 behaves the same way
  [PMID:17956988 "A catalytic Tyr is conserved in all HDACs except for vertebrate class IIa enzymes where it is replaced by His."]
  [PMID:17956988 "this \"gain of function phenotype\" could be extended to HDAC5 and -7"].
- Non-histone deacetylation reported: GCM1 (placenta) [PMID:23867755 "The interaction between HDAC5 and GCM1 facilitates GCM1 deacetylation and suppresses its transcriptional activity."]
  and alpha-tubulin in injured sensory axons [PMID:26157139 "We have previously identified HDAC5 as an injury-regulated tubulin deacetylase that functions at the injury site to promote axon regeneration."].
  Neither study separates intrinsic HDAC5 catalysis from activity recruited through HDAC3.
- Judgement: the histone deacetylase activity rows are kept as over-annotations
  (`MARK_AS_OVER_ANNOTATED`): measurable in vitro activity of uncertain physiological
  relevance. Protein lysine deacetylase activity is kept as non-core.

## Core mechanism: signal-regulated corepressor of MEF2 and other TFs

- Binds MEF2 and represses MEF2-dependent myogenesis
  [PMID:10983972 "These HDACs do not interact directly with MyoD, yet they suppress its myogenic activity through association with MEF2."].
- Signal-dependent nucleocytoplasmic shuttling: CaMK phosphorylation and 14-3-3 binding
  export HDAC5 from the nucleus and derepress MEF2 targets
  [PMID:11081517 "Here we show that HDAC5 shuttles from the nucleus to the cytoplasm when myoblasts are triggered to differentiate."]
  [PMID:10869435 "The association of 14-3-3 with HDAC4 and HDAC5 results in the sequestration of these proteins in the cytoplasm."]
  [PMID:15923258 "Phosphorylation of a set of conserved serine residues in the N-terminal extensions of class II HDACs creates binding sites for 14-3-3 chaperone proteins"].
- Kinases: CaMK, AMPK (Ser259/Ser498; GLUT4 regulation) [PMID:18184930 "Here, we report that AMP-activated protein kinase (AMPK) regulates GLUT4 transcription through the histone deacetylase (HDAC)5 transcriptional repressor."],
  PKN1/2 at Thr292 in the NLS [PMID:20188095], GRK5 in cardiomyocytes [PMID:18711143].
- Other corepressor partners: HDAC3 / N-CoR / SMRT, HP1 [PMID:12242305], BCoR
  [PMID:10898795], RFXANK/ANKRA2 (MHC II repression) [PMID:16236793], GATA3 (FUT7
  repression) [PMID:17075044 "GATA-3 represses FUT7 transcription through phosphorylation-dependent interaction with HDAC-3 and HDAC-5"],
  GCM1 [PMID:23867755], XBP1s [PMID:20408817].
- Endothelium: HDAC5 represses FGF2 and SLIT2 and restrains sprouting angiogenesis,
  independent of MEF2 binding and of deacetylase activity
  [PMID:19351956 "The antiangiogenic activity of HDAC5 was independent of myocyte enhancer factor-2 binding and its deacetylase activity but required a nuclear localization"].
- Brain: loss of HDAC5 in mice sensitises to chronic cocaine and stress
  [PMID:17988634 "This regulation is behaviorally important, as loss of HDAC5 causes hypersensitive responses to chronic, not acute, cocaine or stress."].

## The flagged DNA-binding/TF rows

- `GO:0001216` (IMP, PMID:19071119, ARUK-UCL). The paper (abstract-only in cache) shows
  HDAC4/5 *enhance HIF-1alpha transactivation* by binding HIF-1alpha's inhibitory domain,
  displacing FIH-1 and favouring p300 binding
  [PMID:19071119 "These results indicate that HDAC4 and HDAC5 increase the transactivation function of HIF-1alpha by promoting dissociation of HIF-1alpha from FIH-1 and association with p300."].
  That is a coactivator mechanism; HDAC5 does not bind DNA. Decision: MODIFY to
  `GO:0003713 transcription coactivator activity` (same as the HDAC4 review), with a
  `WRONG_TERM` source defect. This is not overruling the experiment: the experiment is
  accepted; only the activity class is corrected.
- `GO:0000978` (IDA, PMID:24413532, UniProt). Abstract-only. HDAC5 is recruited to the
  ESR1 locus within an MTA1 complex; there is no evidence of direct, sequence-specific
  DNA binding. Decision: MODIFY to `GO:0003712 transcription coregulator activity`
  (direction of the effect differs between cell lines in that paper), with a source
  defect.
- `GO:0000976` contributes_to (IDA, PMID:19351956). ChIP shows HDAC5 at the FGF2 and
  SLIT2 promoters, where it represses. Note `GO:0000976` is_a `GO:0043565`
  sequence-specific DNA binding (checked with oaklib), so even with contributes_to the
  term implies DNA binding by the complex. Decision: MODIFY to `GO:0003714 transcription
  corepressor activity`. This deliberately differs from the HDAC4 review, which proposed
  `GO:0000976` as the replacement for HDAC4's `GO:0000978` row; that choice may be worth
  revisiting for HDAC4 (not edited here).
- `GO:0140297` IPI (PMID:12242305, BHF-UCL) has WITH = mouse CBX5 (HP1alpha, Q61686,
  checked against UniProt REST). HP1 is a chromodomain adaptor, not a DNA-binding
  transcription factor. The claim "HDAC5 binds DNA-binding TFs" is true (MEF2, HIF1A,
  GCM1, GATA3), so the row is accepted as a claim, but a `WRONG_TERM` source defect is
  recorded for the evidence.

## Localization

Nucleus (repressive state) and cytoplasm (after phosphorylation/14-3-3 binding); UniProt
"Shuttles between the nucleus and the cytoplasm." In cultured DRG neurons
[PMID:26157139 "Under vehicle treatment conditions, GFP-HDAC5 was mostly nuclear, whereas, upon stimulation of the PKC pathway with I3A, GFP-HDAC5 relocalized to the cytoplasm"].

## Open questions

- Does HDAC5 have a physiological substrate efficiently processed by its His-containing
  active site, as Lahm et al. proposed for class IIa enzymes?
- Is the HIF-1alpha coactivation seen in overexpression reproduced at endogenous levels?
