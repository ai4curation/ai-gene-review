# PNOC curation notes (human prepronociceptin, UniProtKB:Q13519)

No deep-research provider was available for this review (no provider keys in the
batch environment). The literature search was done by hand with PubMed (queries:
`(Meunier[Author] AND 1995[pdat] AND ORL1) OR (Reinscheid[Author] AND 1995[pdat]
AND orphanin) OR (Mollereau[Author] AND 1996[pdat] AND prepronociceptin)`;
`orphanin FQ nociceptin gene targeted disruption mice stress`) and OLS for GO terms
(`nociceptin`: only GO:0001626 nociceptin receptor activity and GO:0031853
nociceptin receptor binding exist; there is no nociceptin-specific signalling
pathway term). Cited papers are cached under `publications/`.

## Gene product

- 176-aa precursor: signal peptide 1-19, propeptide 20-95, nocistatin 98-127,
  nociceptin 130-146, orphanin FQ2 149-165, C-terminal propeptide 169-176 (UniProt
  Q13519 FT lines). Processed at paired basic residues.
- The human, mouse and rat genes were cloned by Mollereau et al.; the gene
  organisation matches proenkephalin, prodynorphin and POMC, and is predominantly
  transcribed in brain and spinal cord [PMID:8710928 "Nociceptin is derived from a
  larger precursor, prepronociceptin (PPNOC), whose human, mouse, and rat genes we
  have now isolated."; "Northern blot analysis shows that the PPNOC gene is
  predominantly transcribed in the central nervous system (brain and spinal
  cord)"]. The peptides are conserved between murine and human species
  [PMID:8710928].
- PANTHER: PTHR11438 (proenkephalin/prodynorphin/prepronociceptin), subfamily
  PTHR11438:SF2 (PREPRONOCICEPTIN); PAINT node PTN000153716 seeds opioid peptide
  activity, opioid receptor binding, neuropeptide signalling and pain perception.

## Nociceptin / orphanin FQ: ligand of OPRL1 (NOP)

- Isolated as the endogenous agonist of the orphan ORL1 receptor, which it
  activates to inhibit adenylate cyclase [PMID:7566152 "Taken together, these data
  indicate that the newly discovered heptadecapeptide is an endogenous agonist of
  the ORL1 receptor and that it may be endowed with pro-nociceptive properties."];
  [PMID:7481766 "Nanomolar concentrations of orphanin FQ inhibited
  forskolin-stimulated adenylyl cyclase activity in cells transfected with
  LC132."].
- Not an opioid in the pharmacological sense: its action is insensitive to opioid
  ligands and it does not activate the classical opioid receptors [PMID:7481766
  "This inhibitory activity was not affected by the addition of opioid ligands, nor
  did the peptide activate opioid receptors."]. Reactome likewise calls ORL1 "not a
  typical opioid receptor" (Reactome:R-HSA-374723).
- GO places nociceptin receptor activity (GO:0001626) under G protein-coupled opioid
  receptor activity, and the definition of GO:0038003 counts the nociceptin opioid
  receptor among the opioid receptors (see the GO:0140626 comment), so
  GO:0038003 / GO:0031635 are the right pathway terms for nociceptin signalling.
  But GO:0001515 opioid peptide activity is defined by naloxone-reversible
  opiate-like effect, which nociceptin lacks; the PAINT family-level IBA to that
  term is therefore an over-annotation for PNOC.
- Human data: human neutrophils express and secrete nociceptin, and nociceptin
  lowers cAMP in neutrophils through NociR [PMID:12950177 "freshly isolated PMNs
  were found to express and secrete nociceptin following degranulation"; "nociceptin
  prevented intracellular accumulation of cAMP in fMLP-stimulated PMNs, an effect
  mimicked by the specific NociR synthetic agonist, Ro 64-6198."]; human ORL1
  reporter assay [PMID:10419552].
- Behaviour/physiology: intracerebroventricular nociceptin is hyperalgesic /
  anti-analgesic and reduces locomotion [PMID:7481766 "Thus, orphanin FQ may act as
  a transmitter in the brain by modulating nociceptive and locomotor behavior."].
  Pnoc-null mice show increased anxiety, impaired stress adaptation and an elevated
  basal pain threshold [PMID:10468628 "OFQ/N-null mice show elevated basal pain
  threshold but develop normal stress-induced analgesia."].
- Nocistatin, from the same precursor, opposes nociceptin and does not bind NOP
  [PMID:9521323 "Although nocistatin does not bind to the nociceptin receptor, it
  binds to the membrane of mouse brain and of spinal cord with high affinity."];
  its receptor is unknown (knowledge gap).

## Curation decisions summary

- Core MF: `GO:0005184 neuropeptide hormone activity` (TAS row accepted), a child
  of neuropeptide activity (GO:0160041) and hormone activity, both under receptor
  ligand activity (GO:0048018), following LIGANDS_IN_SIGNALING decision 1.
- `GO:0031628 opioid receptor binding` (IBA) MODIFIED to neuropeptide hormone
  activity (decision 4: receptor-specific binding terms on ligands go to the ligand
  activity term).
- `GO:0001515 opioid peptide activity` (IBA) MARK_AS_OVER_ANNOTATED: definition
  requires naloxone reversibility; nociceptin effects are opioid-insensitive.
  Orphanin FQ2 (rat ortholog evidence only) is reported analgesic; whether that is
  opioid-receptor mediated was not checked here, so REMOVE was not used.
- Pathway: TAS `signal transduction` MODIFIED to `GO:0038003`; NEW
  `GO:0031635 adenylate cyclase-inhibiting opioid receptor signaling pathway` from
  human neutrophil and receptor-assay data (PMID:12950177, PMID:7481766,
  PMID:7566152). The comparator ligands PENK and PDYN carry the same two terms.
- Rat/mouse IEA projections of drug-response and behaviour terms (response to
  morphine, cocaine, nicotine, ethanol; drinking; female pregnancy; GABA secretion)
  are expression or pharmacology phenotypes: MARK_AS_OVER_ANNOTATED. Modulation of
  synaptic transmission terms and stress response are KEEP_AS_NON_CORE.
- Module: `modules/opioid_receptor_signaling.yaml` already contains a PNOC ligand
  step with GO:0038003 / GO:0031635 (correct; no nociceptin-specific pathway term
  exists). Its function was GO:0001515 opioid peptide activity; changed to
  GO:0005184 neuropeptide hormone activity to match this review, and the step's
  generic Reactome Gi evidence was supplemented with the nociceptin-specific papers.
- Not edited: the PTHR11438 family review still states family-wide opioid peptide
  activity including SF2 (PNOC); this should be scoped to SF3/SF4 in a family-review
  pass.
