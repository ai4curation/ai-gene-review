# Hspa8 (rat, P63018) notes

## Re-review 2026-10-10

GOA changes since the original review (234 rows in total):
- 26 new rows were seeded as PENDING. 11 are donor-split duplicates of reviewed rows: the same
  term and evidence with a different WITH/FROM (MGI:105384 mouse vs UniProtKB:P11142 human), or
  a different qualifier. The other 15 are new terms or new evidence. All 26 are resolved: 16
  ACCEPT, 10 KEEP_AS_NON_CORE.
- GO:0051082 unfolded protein binding: the IEA, ISO and IDA (PMID:11133993) rows are retired.
  QuickGO confirms the term is obsolete ("this binding term should be replaced by an activity
  term such as protein folding chaperone (GO:0044183) or unfolded protein holdase activity
  (GO:0140309)"). GOA now carries GO:0044183 by IDA from the same paper, plus IEA (ARBA) and
  ISO (mouse). The earlier reviews had already recommended MODIFY to GO:0044183, and the new
  rows are ACCEPTed [PMID:11133993 "The results show that Hsc70 binds to exosomal TfR with
  characteristics expected of a chaperone/peptide interaction."]. Handled the same way as the
  St13 and Uggt1 re-reviews. No proposed_new_terms entry is needed, because the core activity
  has a GO term (GO:0044183).
- 24 rows are retired in total. Their reviews are kept, and a retirement sentence was added to
  each.

Action changes (from -> to):
- GO:0005515 protein binding (8 IPI rows, MARK_AS_OVER_ANNOTATED is no longer allowed):
  - PMID:15708368 (SGTA) -> MODIFY to GO:0051087 protein-folding chaperone binding
    [PMID:15708368 "The tetratricopeptide repeat (TPR) domain in SGT is responsible for
    interacting with Hsc70."]
  - PMID:9528774 (Hsp40/Hop/Hip; retired) -> MODIFY to GO:0051087 [PMID:9528774 "mediates the
    interaction of Hsc70 with Hsp40 and Hop"]
  - PMID:23159318, 18307834, 19457116, 17877381, 10198213 and 12514190 -> REMOVE. The abstracts
    do not support a more specific MF, and removal does not mean the interactions are false.
    PMID:12514190's abstract does not mention Hsc70 at all.
- GO:0046777 protein autophosphorylation (IDA PMID:8420978, retired): REMOVE ->
  MARK_AS_OVER_ANNOTATED. The old review wrongly said the paper has no autophosphorylation
  data. In fact [PMID:8420978 "Purified hsc70 and its mutants autophosphorylate in vitro at a
  substoichiometric level."], but at <1% stoichiometry and uncoupled from ATPase activity.
- GO:1904593 prostaglandin binding (IPI PMID:21445266): REMOVE -> MARK_AS_OVER_ANNOTATED. The
  full text does identify Hspa8 as a 15d-PGJ2 target, but the "binding" is covalent Michael
  addition to free thiols [PMID:21445266 "can form covalent adducts with free thiols in proteins
  by Michael addition"].
- GO:0001664 GPCR binding (ISO from human P11142): REMOVE -> KEEP_AS_NON_CORE. The human source
  is a real IPI with GPR37/Pael-R [PMID:12150907 "CHIP, Hsp70, Parkin, and Pael-R formed a
  complex in vitro and in vivo"], and rat has its own direct evidence for GPCR binding
  [PMID:10866672 "purified A(1)Rs interact specifically with hsc73 with a dissociation constant
  in the nanomolar range"]. propagation_review updated.
- GO:0048018 receptor ligand activity (ISO from human): REMOVE -> MARK_AS_OVER_ANNOTATED. The old
  propagation comment called the human IDA a likely misannotation, which is unfounded
  [PMID:17785435 "human heat shock protein A8 (HSPA8), a member of the hsp70 family, was
  identified as the ligand for EWI-2."]. It is a single, cell-type-specific study, so it is
  marked over-annotated for rat rather than removed.
- GO:0005886 plasma membrane: IEA MARK_AS_OVER_ANNOTATED -> KEEP_AS_NON_CORE, and the retired IBA
  row the same, for consistency with the new ISS row. The old rationale ("not the core site")
  supports non-core status, not over-annotation. UniProt lists Cell membrane, and rat hsc73
  assembles with A1 receptors at the cell membrane (PMID:10866672).
- IEP rows for processes other than "response to X" -> MARK_AS_OVER_ANNOTATED, because a change
  in expression is not participation (same reasoning as the St13 re-review):
  - kidney development, cerebellum development, forebrain development, skeletal muscle tissue
    development, estrous cycle and G1/S transition.
  - For skeletal muscle development, the abstract itself says HSC73 is not developmentally
    regulated [PMID:12909603 "the expression of HSP72, but not HSC73, is influenced by both
    endogenous and exogenous factors"].
  - forebrain development (PMID:9878698) comes from an adult-brain localization study.
- GO:1990832 slow axonal transport and GO:0008088 axo-dendritic transport (IEP PMID:11933046):
  KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED. Hsc73 is cargo here [PMID:11933046 "labeled in
  "slow component b" of axonal transport along with the molecular chaperone Hsc73 and actin"].
- GO:0006606 protein import into nucleus (IMP PMID:8892974): KEEP_AS_NON_CORE ->
  MARK_AS_OVER_ANNOTATED. hsc70 is the import substrate in this study [PMID:8892974 "were
  labeled with 125I and used as transport substrates"].
- GO:0046034 ATP metabolic process (ISO): KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED. Using ATP
  to power the chaperone cycle is already captured by ATP hydrolysis activity.
  propagation_review added.
- Legacy rows: about 200 rows had boilerplate reasons and no supported_by.
  Verbatim support was added to every ACCEPT and KEEP_AS_NON_CORE row, from UniProt P63018
  CC-lines, the falcon deep research, or cached abstracts. 18 donor-side papers were cited and
  added to references; PMID:37767704 was newly cached.
- core_functions: GO:0061738 late endosomal microautophagy was added to the CMA/cargo-selector
  function, keeping the eMI ACCEPT rows consistent with the core
  [PMID:21238931 "Protein cargo selection is mediated by the chaperone hsc70"].
- description: the closing sentence about "annotated processes" was replaced with plain biology.

Open questions:
- GO:0005102 signaling receptor binding (IPI PMID:11133993) is kept as non-core. The transferrin
  receptor is bound as a chaperone client, so a curator may prefer a different framing.
- GO:0035651 AP-3 adaptor complex binding (mouse IDA PMID:19010779): the abstract does not name
  Hsc70. This is deferred to the curator's full-text reading.
- GO:0019899 enzyme binding (IPI PMID:21958194, alpha-enolase) and GO:0031686 A1 adenosine
  receptor binding are both kept as non-core. Neither is clearly a client versus regulatory
  interaction.
