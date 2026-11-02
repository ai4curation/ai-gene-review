# Psmc5 (rat, P62198) - manual literature summary

No deep-research API was available for this session. This summary was compiled
by hand from the cached publications in `publications/` and the UniProt record
(`Psmc5-uniprot.txt`). Each statement carries its provenance.

## Identity

- Rat Psmc5 (P62198, PRS8_RAT, 406 aa; RGD:708376; GeneID 81827) is the 26S
  proteasome regulatory subunit 8, also called Rpt6, SUG1, p45, TRIP1 and
  FZA-B. The rat, mouse (P62196) and human (P62195) sequences are identical in
  length and near-identical in sequence.
- UniProt: "PSMC5 belongs to the heterohexameric ring of AAA (ATPases associated
  with diverse cellular activities) proteins that unfolds ubiquitinated target
  proteins that are concurrently translocated into a proteolytic chamber and
  degraded into peptides." [file:rat/Psmc5/Psmc5-uniprot.txt, CC FUNCTION]
- Domain content: AAA ATPase core (IPR003959, Pfam PF00004), AAA lid
  (PF17862), N-terminal coiled coil and OB fold (IPR032501). ATP-binding P-loop
  at 190-197 (GPPGTGKT) [Psmc5-uniprot.txt, FT BINDING]. Walker B motif
  "IIFMDEID" is intact in the sequence (residues ~245-252).

## Position in the 26S proteasome

- "The six ATPases adopt a single arrangement in normal cells:
  Rpt1-Rpt2-Rpt6-Rpt3-Rpt4-Rpt5" [PMID:23495936]. Rpt6 is the partner of Rpt3 in
  the Rpt3-Rpt6 dimer of the base.
- In substrate-engaged human 26S structures "the carboxyl (C)-terminal tails of
  Rpt subunits, with the exception of Rpt4, were inserted into the corresponding
  α-pockets" [PMID:29636472]; so the Rpt6 tail docks into the 20S alpha ring,
  although Rpt6 lacks the canonical HbYX motif (rat tail ends ...SIKKLWK).
- As one of six ATPases in the ring, Rpt6 contributes to the hexamer's
  proteasome-activating activity; it cannot perform unfolding/gate opening
  alone.

## Biochemistry of rat Psmc5

- Recombinant rat SUG1 is an ATPase: "The rSUG1 exhibited a Mg2+-dependent
  ATPase activity." Km for ATP 35 uM [PMID:9287326, abstract only]. The same
  paper reported stimulation by poly(U)/poly(C) RNA and speculated about mRNA
  metabolism; this has not been substantiated and is not treated as a function.
- Wang et al.: "In rat liver and in HeLa cells, FZA-B is present in the 26S
  proteasome complex" and "FZA-B is found predominantly in the nuclear fraction
  of COS cells ... and in the nuclear 26S proteasome of HeLa cells"
  [PMID:8710853, abstract only].

## Non-proteolytic / transcription-related literature

- SUG1/TRIP1 was first isolated as a ligand-dependent thyroid hormone receptor
  interactor that could substitute for yeast Sug1 [PMID:7870181; PMID:7776974].
  The partner is the thyroid hormone (T3) receptor, not the thyrotropin-releasing
  hormone receptor.
- Mouse mSUG1 binds RARalpha, TR, ER and VDR, but "RXR alpha efficiently
  interacts with TIF1, but not with mSUG1" [PMID:8598193].
- SUG1 binds the XPB subunit of TFIIH; "overexpression of SUG1 in normal
  fibroblasts induced arrest of transcription and a chromatin collapse in vivo"
  [PMID:9173976].
- Human Sug1 binds Sp1 and stimulates its proteasome-dependent degradation, with
  ATP hydrolysis by hSug1 necessary [PMID:10816420].
- Proteasomal ATPases including SUG1 associate with TBP in an ~800 kDa complex
  that lacks the 20S proteasome; SUG1 binds TBP directly by far-Western
  [PMID:10526239, abstract only].
- These are mostly binding results; the transcription effects are best
  explained as proteasome-related or as activities of free 19S/ATPase
  sub-assemblies, and are treated as non-core.

## Neuronal studies in rat

- Rousseau et al. (full text read): endogenous Rpt6 co-localises with mutant
  huntingtin inclusions in rat primary neurons and in HD patient brain ("100% of
  inclusions were labeled with Rpt6"); siRNAs "directed against the target rat
  Rpt6" in rat hippocampal neurons reduced inclusion formation; Rpt6 and Rpt4 are
  in both 26S proteasomes and the free ATPase complex APIS (gradients in 293T
  cells) [PMID:18986984].
- Djakovic et al.: CaMKII "directly phosphorylates Rpt6" and stimulates proteasome
  activity in hippocampal neurons [PMID:19638347]; Rpt6 Ser120 phosphorylation by
  CaMKIIalpha is activity-dependent and S120D/S120A mutants alter mEPSC amplitude
  and homeostatic scaling [PMID:22496558] (abstracts only).
- Sun et al.: free 19S particles are abundant near synapses in rat cortical
  neurons and deubiquitylate K63-ubiquitin; inhibiting the 19S deubiquitylase
  reduced synaptic AMPA receptor availability [PMID:37228199, abstract only].
  The abstract does not mention synaptic vesicles or Psmc5 individually.
- Kury et al. 2025 (full text): PSMC5 variants cause a neurodevelopmental
  proteasomopathy; "Psmc5 KD by shRNA significantly increased ubiquitin-positive
  protein levels throughout the cells, particularly in the soma" in primary rat
  hippocampal neurons, with reduced vGlut-positive excitatory synapse density
  [PMID:41298377].
