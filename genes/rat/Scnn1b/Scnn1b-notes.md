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

## 2026-10-28 Harmonization across ENaC subunit reviews (Scnn1a/Scnn1b/Scnn1g)

Shared GO terms were aligned with the alpha and gamma reviews where the evidence is the same. Changes here: cell
surface MODIFY -> KEEP_AS_NON_CORE (surface-labelling assays support it; plasma membrane is not a refinement of
cell surface); sensory perception of salty taste UNDECIDED -> KEEP_AS_NON_CORE (ENaC is the sodium taste receptor
in mice, PMID:20107438; support for beta is indirect, via the obligate heteromer); response to aldosterone
MARK_AS_OVER_ANNOTATED -> KEEP_AS_NON_CORE and response to vasopressin MARK_AS_OVER_ANNOTATED -> KEEP_AS_NON_CORE
(both entailed by the kept cellular response rows; the beta aldosterone row notes that its only paper reports a
decrease in Dahl salt-sensitive rats). Renal system process (GO:0003014) MODIFY -> KEEP_AS_NON_CORE and renal sodium
ion absorption (GO:0070294) dropped from core_functions, matching removal of the GO:0070294 NEW row from Scnn1a; the
question of whether ENaC subunits should carry GO:0070294 is now a suggested question. The NOT response to
dexamethasone row stays KEEP_AS_NON_CORE, differing from gamma, because neither beta transcript nor protein rose in
PMID:16263802. Other shared terms (plasma membrane, intracellular sodium ion homeostasis, external side of plasma
membrane, neuron projection development, cellular response to acidic pH) already matched the settled action; their
reasons were unified.

## 2026-10-28 review-fix pass

- The negated GO:0071548 response to dexamethasone row (PMID:16263802) changed from KEEP_AS_NON_CORE to MARK_AS_OVER_ANNOTATED, matching the four other GO:0071548 rows on Scnn1a and Scnn1g: an IEP expression-response term does not describe channel function in either polarity. The factual point stands that beta transcript and protein did not rise in PMID:16263802.
- GO:0015280 IMP row (PMID:11773057): removed the apical-localization quote, which says nothing about gating; PMID:8107805 support remains.
- Removed supported_by self-citations of the gene's own -deep-research-manual.md where a primary citation in the same block already supports the row (the reviewer's own conclusion is not independent evidence). The validator now warns that no annotation cites the deep-research file; that warning is accepted deliberately, which sets the status to DRAFT.
