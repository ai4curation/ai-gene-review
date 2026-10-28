# Scnn1b (rat, P37090) review notes

## Session 1 (create review)

- fetch-gene resolved P37090 (SCNNB_RAT, RGD:3640, GeneID 24767) - matches the task.
- No deep-research API keys; literature synthesis in `Scnn1b-deep-research-manual.md`.
- 103 GOA rows. Key decisions:
  - MF: ENaC beta is a pore-forming subunit of a constitutively active, amiloride-sensitive
    Na+ channel [PMID:8107805 "Here we identify two other subunits (beta and gamma) by
    functional complementation of the alpha-subunit of the rat epithelial Na+ channel"].
    `sodium channel activity` (GO:0005272) accepted. `ligand-gated sodium channel activity`
    (GO:0015280) modified to GO:0005272: ENaC has no physiological ligand gate; its activity
    is set by open probability, proteolysis and surface number [PMID:24419567]. The family
    placement (DEG/ENaC also contains ASICs and FaNaC) explains the IBA/InterPro mapping.
    `sodium ion transmembrane transporter activity` modified to GO:0005272 (more specific).
  - BP: `sodium ion import across plasma membrane` (GO:0098719) is the core process;
    `sodium ion transport` and `sodium ion transmembrane transport` modified to it.
    `renal system process` modified to `renal sodium ion absorption` (GO:0070294).
    `intracellular sodium ion homeostasis` marked over-annotated: ENaC serves
    transepithelial/whole-body Na+ balance; PMID:17562820 is a stoichiometry paper.
  - Expression-response IEP rows (hypoxia, ischemia, salt stress, aldosterone, vasopressin,
    testosterone, NGF) marked over-annotated - they report changes in Scnn1b expression or
    surface abundance, not activities of the protein.
  - Mouse ISO rows from the Scnn1b-Tg airway overexpression model (mucus secretion,
    neutrophil activation, neutrophil-mediated killing, gene expression) removed:
    gain-of-function transgenic phenotypes, not normal beta-ENaC functions; UniProt notes
    beta is not essential for airway surface liquid homeostasis and mucus clearance.
  - `cytosol` IDA (PMID:18024548) marked over-annotated: integral multipass membrane protein;
    intracellular pool is vesicular [PMID:11352848].
  - Taste: salty taste UNDECIDED (NAS from a delta-ENaC review whose abstract does not
    discuss taste; alpha-ENaC is the established salt-taste subunit in mouse); sour taste
    marked over-annotated (no evidence ENaC mediates sour taste).
  - WW domain binding kept as non-core (well supported: PMID:8665844, PMID:9923703) - it is
    the regulatory interaction with NEDD4/NEDD4L that controls channel retrieval.
- Added PMID:18308722 (CK2 phosphorylation of beta S631 required for ENaC activity; full
  text read) as reference for regulation.
- No NEW process terms proposed (NEW-term bar).
