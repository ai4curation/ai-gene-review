# cyk-4 (C. elegans, Q9XUS9) - manual literature research

No deep-research API keys were available, so this summary was compiled by hand from the cached
publications in `publications/` and PubMed searches. Every claim below has inline provenance.

## Identity and domains
- K08E3.6 / WBGene00000875, 681 aa, unreviewed TrEMBL entry Q9XUS9; ortholog of human RACGAP1
  (MgcRacGAP) and Drosophila tumbleweed (PANTHER PTHR46199:SF3).
- Architecture: N-terminal coiled coil, C1 (phorbol-ester/DAG-type) domain, C-terminal RhoGAP
  domain [PMID:10871280 "Adjacent to the COOH-terminal GAP domain is a C1 domain that is predicted
  to bind to diacylglycerol or phorbol esters. At the NH2 terminus of the protein is a 90–amino acid
  region predicted to form a coiled-coil domain."]

## GAP activity
- In vitro GAP on RhoA, Rac1, Cdc42 [PMID:10871280 "in vitro, stimulates GTP hydrolysis by Rho,
  Rac, and Cdc42"].
- R459A abolishes activity toward RhoA and CED-10/Rac1 [PMID:26252513 "While CYK-4 GAP exhibits GAP
  activity towards both RhoA and CED-10/Rac1, CYK-4R459A GAP lacks detectable GAP activity towards
  either GTPase"].
- Rac as functional target [PMID:19056985 "inactivation of Rac by centralspindlin functions in
  parallel with RhoA activation to drive contractile ring constriction during cytokinesis"].
- Non-canonical promotion of RhoA activation with ECT-2 [PMID:26252513 "Thus, counterintuitively,
  CYK-4 RhoGAP activity promotes RhoA activation."]; C-termini of CYK-4 and ECT-2 interact directly
  [PMID:26252513 "We found that the catalytic C-termini of CYK-4 and ECT-2 directly interact"], but GEF
  stimulation not reconstituted [PMID:26252513 "we have not yet been able to detect stimulation of GEF
  activity (data not shown)"].
- NOP-1 acts in parallel [PMID:22918944 "NOP-1, that functions in parallel with CYK-4 to promote RhoA
  activation"].

## Centralspindlin
- CYK-4/ZEN-4 complex, heterotetramer, bundles microtubules [PMID:11782313 "Centralspindlin, but not
  its individual components, strongly promotes microtubule bundling in vitro."].
- Coiled-coil dimerization and cooperative assembly [PMID:17942600 "each of the two subunits of
  centralspindlin dimerize via a parallel coiled coil"].
- CYK-4 reconfigures ZEN-4 neck [PMID:25875822 "CYK4 binds to a globular mass in the atypically long
  MKLP1 neck domain"].

## Membrane association
- C1 domain required for membrane accumulation on furrows [PMID:26252513 "CYK-4 membrane accumulation
  requires the C1 domain"]; regulated by PAR-5 and Aurora B [PMID:25898168 "Membrane localization of
  centralspindlin oligomers is globally inhibited by PAR-5/14-3-3."].
- Human MgcRacGAP C1 binds phosphoinositides [PMID:23235882 "interacting with polyanionic
  phosphoinositide lipids"]; no DAG binding demonstrated for the family.

## Phenotypes and localization
- cyk-4(t1689ts): furrow regresses, no central spindle, polar body extrusion defects
  [PMID:10871280 "defects in polar body extrusion are frequently observed (data not shown)"].
- Localization: interphase cytoplasm/nucleus, central spindle, division remnants [PMID:10871280 "In
  interphase cells, CYK-4 is present in the cytoplasm and slightly concentrated in the nucleus."].
- Recruits midbody factors: CDC-14 [PMID:12213836 "CeCDC-14 and the ZEN-4/CYK-4 complex are mutually
  dependent on each other for localization"] and LEM-3 [PMID:29463814 "Midbody localization of LEM-3
  depends on the central spindle component CYK-4"].
