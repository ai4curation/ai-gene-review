# RIPK3 (human, Q9Y572) — curation notes

**Provenance note.** Provider deep research for this gene FAILED (Falcon returned
HTTP 402 Payment Required; Perplexity was not configured). No
`RIPK3-deep-research-<provider>.md` file exists. The synthesis below replaces it and
was built from the UniProt record (`RIPK3-uniprot.txt`), the cached publications in
`publications/`, and cached Reactome entries. Quotes are verbatim from the cached
files.

## Identity and architecture

- Receptor-interacting serine/threonine-protein kinase 3; 518 aa; N-terminal kinase
  domain and a unique C-terminal region containing the RIP homotypic interaction motif
  (RHIM; core tetrad VQVG).
  [PMID:10358032 "RIP3 is a novel gene product containing a N-terminal kinase domain
  that shares extensive homology with the corresponding domain in RIP
  (receptor-interacting protein) and RIP2."]
- Three isoforms (1, 2/beta, 3/gamma) per UniProt.

## Core function: necroptotic kinase

- RIPK3 is required for TNF-induced programmed necrosis and its kinase activity is
  essential. [PMID:19524512 "A genome wide siRNA screen revealed another member of the
  RIP kinase family, RIP3, to be required for necrosis."] [PMID:19524512 "The kinase
  activity of RIP3 is essential for necrosis execution."]
- RIPK3 is recruited to RIPK1 to form the necrosis-inducing complex (necrosome).
  [PMID:19524512 "Upon induction of necrosis, RIP3 is recruited to RIPK1 to form a
  necrosis-inducing complex."] Reciprocal phosphorylation stabilises the complex.
  [PMID:19524513 "The phosphorylation of RIP1 and RIP3 stabilizes their association
  within the pronecrotic complex, activates the pronecrotic kinase activity, and
  triggers downstream reactive oxygen species production."]
- Substrate: MLKL, phosphorylated on T357/S358 (human). [PMID:22265413 "MLKL was
  phosphorylated by RIP3 at the threonine 357 and serine 358 residues, and these
  phosphorylation events were critical for necrosis."] Reactome R-HSA-5218906 ("RIPK3
  phosphorylates MLKL") records the same reaction.
- RIPK3 also phosphorylates RIPK1 (reciprocal auto/trans-phosphorylation; UniProt,
  citing PMID:19524513). [PMID:19524513 "RIP3 regulates necrosis-specific RIP1
  phosphorylation."]
- Activation-loop-region phosphorylation (T182) is needed for kinase activity and also
  creates a PELI1 degron. [PMID:29883609 "This same phosphorylation event is also
  important for RIP3 kinase activity; thus, PELI1 preferentially targets kinase-active
  RIP3 for degradation."]

## RHIM-mediated functional amyloid (necrosome scaffold)

- RIPK1 and RIPK3 RHIMs form hetero-amyloid fibrils required for kinase activation and
  necroptosis. [PMID:22817896 "Here, we report that the RIP homotypic interaction motifs
  (RHIMs) of RIP1 and RIP3 mediate the assembly of heterodimeric filamentous
  structures."] [PMID:22817896 "Mutations in the RHIMs of RIP1 and RIP3 that are
  defective in the interaction compromise cluster formation, kinase activation, and
  programmed necrosis in vivo."]
- Solid-state NMR structure of the human RIPK1-RIPK3 core. [PMID:29681455 "The
  RIPK1-RIPK3 necrosome is an amyloid signaling complex that initiates TNF-induced
  necroptosis"] [PMID:29681455 "RIPK1 and RIPK3 alternately stack (RIPK1, RIPK3, RIPK1,
  RIPK3, etc.) to form heterotypic β sheets."]
- RIPK3 also forms homo-amyloid; cryo-EM structure of the RIPK3 RHIM fibril.
  [PMID:33790016 "Receptor-interacting protein kinases 3 (RIPK3), a central node in
  necroptosis, polymerizes in response to the upstream signals and then activates its
  downstream mediator to induce cell death."] Monomeric RHIM is intrinsically
  disordered. [PMID:36870681 "Our results establish that the RHIM of RIPK3 is an
  intrinsically disordered protein motif, contrary to prediction"]
- Upstream RHIM partners besides RIPK1: ZBP1/DAI (UniProt; PMID:19590578) and TRIF
  (TLR3/4 pathway). Viral RHIM proteins (HSV-1 ICP6/R1, HSV-2 ICP10, MCMV M45) engage
  the RIPK3 RHIM and block necroptosis in human cells. [PMID:26559832 "The RHIM domain of
  R1 was essential for its association with human RIP3 and RIP1, leading to disruption
  of the RIP1/RIP3 complex."] [PMID:33348174 "the ICP6 RHIM is amyloidogenic and can
  interact with host RHIM-containing proteins to form heteromeric amyloid complexes"]

## Localisation

- Mainly cytosolic; forms punctae on necroptosis induction. [PMID:22265413 "Treating
  cells with necrosulfonamide or knocking down MLKL expression arrested necrosis at a
  specific step at which RIP3 formed discrete punctae in cells."]
- Shuttles through the nucleus; nuclear RIPK3 is kinase-active and contributes to
  cytosolic necrosome formation. [PMID:30271893 "We report that RIPK3 and MLKL
  continuously shuttle between the nucleus and the cytoplasm, whereas RIPK1 is
  constitutively present in both compartments."] [PMID:30271893 "Following necroptosis
  induction, RIPK3 and MLKL are activated in the nucleus, and after their cooperative
  nuclear export, they contribute to cytosolic necrosome formation."]

## Ripoptosome / apoptosis / NF-kB (secondary)

- In cIAP-depleted cells, the ripoptosome switches to RIP3-dependent necroptosis when
  caspase activity is low. [PMID:21737330 "Thus, loss of RIP3 disables TLR3-mediated
  necroptosis without affecting the apoptotic response."]
- Early overexpression studies: RIPK3 C-terminus induces apoptosis and NF-kB
  activation; kinase domain dispensable for these. [PMID:10339433 "The carboxy-terminal
  domain of RIP3, like that of RIP, could activate the transcription factor NFkappaB and
  induce apoptosis when expressed in mammalian cells."] Conflicting: [PMID:10358032
  "RIP3, however, attenuates both RIP and TNF receptor-1-induced NF-kappaB
  activation."] Its NF-kB activity is weak. [PMID:21931591 "Because RIP3 is a weak
  inducer of NF-κB"] These are overexpression phenotypes and are treated as non-core.

## Antiviral defence

- RIP3-/- mice: impaired vaccinia-induced necrosis, inflammation, viral control.
  [PMID:19524513 "Consequently, RIP3(-/-) mice exhibited severely impaired virus-induced
  tissue necrosis, inflammation, and control of viral replication."]

## Curation judgements (summary)

- Core: protein serine/threonine kinase activity (MLKL, RIPK1 substrates); necroptotic
  signaling pathway / necroptotic process; component of ripoptosome/necrosome
  (GO:0097342, synonym "necrosome"); RHIM-driven amyloid assembly.
- Protein binding (GO:0005515) rows: all REMOVE per project policy (uninformative); the
  informative content (RIPK1 binding, self-association) is already captured by
  GO:0120283 and GO:0042802 rows.
- Mouse-derived IEA/ISS immune-development terms (thymus/spleen/lymph node development,
  T cell homeostasis, etc.) are phenotypes of compound mutants or indirect immune
  effects; marked as over-annotated.
- protein serine kinase activity (GO:0106310): RIPK3 phosphorylates both Thr and Ser on
  MLKL, so per the GO term's own usage note the dual term GO:0004674 is appropriate;
  MODIFY.
- "execution phase of necroptosis": RIPK3 acts upstream of the MLKL-driven execution
  phase; MODIFY to necroptotic signaling pathway.

## Disease context

- RIPK3-dependent necroptosis is implicated in inflammatory tissue injury
  (pancreatitis model in PMID:19524512) and in neurodegeneration (PMID:29681455 abstract
  mentions neurodegenerative diseases). Not used for GO annotation.
