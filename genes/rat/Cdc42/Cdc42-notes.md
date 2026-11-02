# Cdc42 (rat, Q8CFN2) review notes

## Session 2026-10-28

- `just fetch-gene rat Cdc42` resolved Q8CFN2 (CDC42_RAT, reviewed; RGD:71043; GeneID 64465).
  155 GOA rows seeded (158 GOA lines; the three SynGO Schaffer-collateral lines collapse to one
  IDA and one IMP row).
- No deep-research API keys; literature synthesis written by hand to
  `Cdc42-deep-research-manual.md` from cached papers.
- Full text read: PMID:20525016 (Golgi positioning, NRK cells), PMID:21423166 (spine
  plasticity, rat CA1), PMID:21763307 (cytokinesis, NRK), PMID:25498153 (ArhGAP44 GAP assays),
  PMID:9487126 (hepatocyte JNK/DNA synthesis), PMID:20472934 (RhoGDIalpha Ser34; REF cells).
  Abstract only: PMID:12610628, 15147909, 15537656, 17161586, 17855387, 18448434, 18562481,
  18784978, 21844200.

### Key decisions

- Core MF: G protein activity (GO:0003925) plus GTPase activity and GTP binding; effector
  binding via GBD domain binding / GTP-dependent protein binding.
  [UniProtKB:Q8CFN2 "Plasma membrane-associated small GTPase which cycles between an active
  GTP-bound and an inactive GDP-bound state"]
- Core BPs: actin filament organization, positive regulation of filopodium assembly,
  establishment of cell polarity; Rho protein signal transduction as the refinement of the IBA
  signal transduction row.
- PMID:20472934 (key paper requested): Cdc42 from rat embryo fibroblast lysate is pulled down by
  RhoGDIalpha and its binding is unaffected by the S34D phosphomimetic
  [PMID:20472934 "When Ser-34 was mutated to Asp, there was significantly reduced RhoGDIα binding
  to RhoA (by around 75%) but not Rac1 or Cdc42."]. Added as NEW GO:0051022 Rho
  GDP-dissociation inhibitor binding (IPI). Not a process term, so the NEW process bar does not
  apply; it records the inactive-state partner of the switch. Non-core.
- Rat-specific counter-evidence: in NRK cells Cdc42 depletion did not impair cytokinesis or
  chromosome congression [PMID:21763307 "Our results indicate that Cdc42 activity per se is
  dispensable for cytokinesis in NRK cells"]. The ISO/ISS rows for positive regulation of
  cytokinesis and for regulation of kinetochore attachment (from HeLa work) were marked
  over-annotated for rat.
- Stress fibre regulation rows (human donor) marked over-annotated: in rat microvascular
  endothelial cells active Cdc42 lowered RhoA activity [PMID:18562481 "Activation of Cdc42 was
  sufficient to decrease RhoA activity."].
- Ubiquitin protein ligase activity (ISO from human AgBase IDA, PMID:21435037): REMOVE with
  source defect; the human review found the experiments show Cdc42-dependent SopB
  ubiquitination, not Cdc42 catalysis.
- COG complex (ISO from human CAFA IMP, PMID:16380373): MODIFY to Golgi membrane, with a
  source defect (Golgi localization, not COG subunit).
- Storage vacuole (ISO from mouse MGI IDA PMID:21828338, insulin granules): MODIFY to secretory
  granule; source defect WRONG_TERM.
- Schaffer collateral - CA1 synapse IMP row (SynGO): a phenotype cannot establish a location;
  kept with the same action as the IDA row, WRONG_EVIDENCE_CODE source defect with CHECK.
- Expression-only IEP row (submandibular gland formation, PMID:18784978): MARK_AS_OVER_ANNOTATED.
- No NEW process terms proposed.
