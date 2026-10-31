# Pak (DROME, Q9VI13) review notes

## Setup
- `just fetch-gene DROME Pak` resolved Q9VI13 (PAK_DROME, FlyBase FBgn0267698), 64 GOA rows.
- `just fetch-gene-pmids DROME Pak` cached 13 papers; PMID:21690310 cached on request. Extra papers
  cached for context: PMID:12588847, PMID:17383630, PMID:18996366, PMID:21098722, PMID:27736876.
- No deep-research provider; literature synthesis in `Pak-deep-research-manual.md`.

## Key judgments
- Core MF: protein serine/threonine kinase activity (GO:0004674), with Rac/Cdc42 effector binding
  (small GTPase binding, GO:0031267) and Dock SH3-domain binding (GO:0017124) as the recruitment
  /activation interfaces [PMID:10399914 "Normal patterns of R cell connectivity require Pak's kinase
  activity and binding sites for both Dock and Cdc42/Rac"].
- IEA protein kinase activity (GO:0004672) MODIFIED to GO:0004674.
- Bare protein binding rows with Rac1/Rac2 MODIFIED to small GTPase binding (GDP/GTP-bound Rac
  binding is reported by PMID:8628256 and the Rac-Pak activation link by PMID:10847683); the Robo1
  row REMOVED (Pak reaches Robo through Dock; no specific MF).
- Cytoskeleton (GO:0005856) IMP row: a mutant phenotype (disrupted leading-edge cytoskeleton)
  cannot establish a location; Pak colocalizes with actin (separate IDA colocalizes_with row) rather
  than being a cytoskeletal component. MARK_AS_OVER_ANNOTATED + source_defects (CHECK evidence code).
- NMJ is_active_in IMP row: accepted alongside the IDA row (claim is true), with a source_defects
  CHECK on the IMP code.
- Regulation of MAPK cascade IBA: over-annotation; fly Pak does not signal through JNK in dorsal
  closure [PMID:15581872 "did not affect the JNK cascade"].
- Cellular response to starvation IBA: fungal/Dictyostelium-seeded node, no fly evidence.
- Ecdysone/cell-death rows (PMID:24374353, PMID:18757938): kept non-core; Pak acts upstream as a
  secondary response gene. Autophagic cell death marked over-annotated (Pak does not execute the
  autophagic death; regulation row already present).
- PMID:18757938 abstract does not name pak; deferred to curators (full text unseen) but the same
  role is shown in the PMID:24374353 full text.
- Broad ARBA terms (post-embryonic development, animal organ morphogenesis) over-annotated;
  embryonic morphogenesis MODIFIED to dorsal closure; cell junction assembly to septate junction
  assembly; cell junction to focal adhesion and NMJ; plasma membrane to lateral plasma membrane;
  regulation of synapse structure or activity to regulation of synapse maturation.
- No NEW rows proposed: candidate processes (muscle attachment/myotube guidance, follicle-cell
  polarity) rest on mutant phenotypes only.
