# Scnn1g (rat, P37091) review notes

## Session 1 (2026-10-28)

- Fetched with `just fetch-gene rat Scnn1g`; UniProt id P37091 confirmed (RGD:3641); 87 GOA rows.
- No deep-research API keys were available, so the literature synthesis is in
  `Scnn1g-deep-research-manual.md`. Most cached PMIDs are abstract-only.
- PMID:18308722 (CK2 regulation of ENaC) was read in full. Gamma Thr599 is a CK2 site, and it is
  needed together with beta Ser631 for full rat ENaC current [PMID:18308722 "Expression of a trimeric channel lacking both CK2 sites (alphabeta(S631A)gamma(T599A)) produced a largely attenuated amiloride-sensitive whole cell conductance and rendered the mutant channel insensitive to CK2."].
  The paper supports regulation of the channel, not a new GO term for Scnn1g.

### Key decisions
- Core MF: contributes_to sodium channel activity (GO:0005272), because gamma is inactive alone [PMID:8188647].
- Ligand-gated sodium channel activity (GO:0015280; IBA, IEA, IMP rows): MODIFY to GO:0005272.
  ENaC is constitutively open and gated by proteolysis and Na+ self-inhibition, not by ligand binding.
- General terms (plasma membrane, membrane, sodium ion transport, sodium ion transmembrane transport,
  ion channel activity, Na+ transmembrane transporter activity): MODIFY to the specific terms the gene already carries
  (apical plasma membrane, sodium ion import across plasma membrane, sodium channel activity).
- Intracellular sodium ion homeostasis: MODIFY to sodium ion homeostasis. The role is organismal Na+ balance.
- IEP "response to X" rows (salt, hypoxia, candesartan, testosterone, NGF, dexamethasone):
  MARK_AS_OVER_ANNOTATED, because they rest on expression changes only. Aldosterone and vasopressin responses are
  KEEP_AS_NON_CORE, because ENaC is the hormones' end effector.
- NOT response to dexamethasone (PMID:16263802): UNDECIDED. The abstract reports that dexamethasone increased gamma protein.
- No NEW annotations. Renal sodium ion absorption (GO:0070294) was considered, but no ENaC subunit carries it
  in human, mouse or rat (QuickGO check), so sodium ion homeostasis was kept.
