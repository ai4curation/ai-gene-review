# MTMR12 (human, Q9C0I1) review notes

## Deep research status

2026-10-20: `just deep-research-falcon human MTMR12 --fallback perplexity-lite` failed for both
providers (falcon: "Failed to authenticate"; perplexity-lite: HTTP 401 insufficient quota). No
deep-research file exists. The review is based on the cached primary literature listed below,
the UniProt record, the Reactome entries, and the PANTHER/PAINT data for PTHR10807.

## Evolutionary placement

- PANTHER PTHR10807:SF37 (MYOTUBULARIN-RELATED PROTEIN 12). Mouse Q80TA6 (Mtmr12) and the
  zebrafish mtmr12 protein are the experimentally studied orthologs used below; mouse Q80TA6 is
  in the same subfamily.
- PAINT: Q9C0I1 is a seed of IBD node PTN000743854 (cytoplasm). It inherits GO:0016020
  membrane from PTN000086845, but the PTN000086845 catalytic assertions (GO:0004438
  phosphatidylinositol-3-phosphate phosphatase activity, GO:0046856 phosphatidylinositol
  dephosphorylation) do not appear among MTMR12's IBA annotations. This is consistent with
  catalytic inactivity and is treated as a deliberate curator decision.
- UniProt CAUTION (ECO:0000305|PubMed:11504939): lacks the active-site Cys of the CX5R
  dsPTPase loop and has no phosphatase activity.

## Literature

- [PMID:11504939 "insect cell-expressed 3-PAP recombinant protein was catalytically inactive"]
  Human 3-PAP (MTMR12) cloned; recombinant protein inactive, but immunoprecipitates from
  platelet cytosol carry PtdIns(3)P 3-phosphatase activity (abstract only cached).
- [PMID:12847286 "studies 3-PAP coimmunoprecipitated with MTM1 and MTMR2 but not MTMR6"]
  Human cells (K562, COS-7). Endogenous 3-PAP co-purifies MTM1 (mass spec). 3-PAP localizes to
  cytosolic punctate vesicles; coexpression relocates MTM1 from plasma membrane to cytosol.
  Region 449-558 (absent in isoform 3, "3-PAPdeltaSID") needed for MTM1 association.
- [PMID:23818870 "MTM1-GST protein pulled down MTMR12-B10 protein whereas no interaction was observed with the GST alone"]
  Direct binding (human proteins, in vitro). Endogenous Mtm1-Mtmr12 co-IP from mouse muscle;
  co-localization at triads and partial with RyR (SR marker) in mouse muscle. Mtmr12 siRNA in
  mouse C2C12 lowers MTM1 protein; zebrafish morphants lose myotubularin protein; human MTMR12
  mRNA partially rescues mtm1 morphants. Authors: "MTMR12 primarily regulates the function of
  myotubularin protein by affecting protein levels instead of modulating the enzymatic activity".
  In human XLMTM patient myotubes, destabilizing MTM1 mutations also lower MTMR12.

## What is experimentally established in human vs inferred

Established with human protein / human cells:
- Binding to MTM1 (direct, in vitro, and endogenous in K562) and to MTMR2 (co-IP).
- Cytoplasmic/cytosolic, punctate-vesicle localization (overexpression in COS-7; native cytosolic
  fraction from platelets).
- Catalytic inactivity of recombinant protein.
- Reciprocal: MTMR12 level falls with destabilizing MTM1 mutations in patient myotubes.

Inferred from orthologs in the same subfamily (mouse Q80TA6, zebrafish mtmr12):
- Stabilization of MTM1 protein (C2C12 knockdown, zebrafish morphant).
- Triad / SR localization in skeletal muscle.
- Muscle phenotypes (morpholino; not annotated as process participation).

## Decisions

- Protein binding rows -> MODIFY to GO:0019902 phosphatase binding (partners MTM1, MTMR2 are
  active PI 3-phosphatases).
- GO:0019211 phosphatase activator activity -> MODIFY to GO:0019208 phosphatase regulator
  activity; no evidence that MTMR12 raises MTM1 specific activity, effect is on abundance and
  localization.
- GO:0006661 PI biosynthetic process (Reactome) -> MARK_AS_OVER_ANNOTATED; reaction is a
  dephosphorylation catalysed by MTM1, and PAINT withheld the dephosphorylation process.
- Sarcomere (IEA, from mouse) -> MODIFY to GO:0030314 junctional membrane complex (triads;
  explicitly not Z-line).
- NEW GO:0050821 protein stabilization. Participation: MTMR12 binding itself protects MTM1.
  Comparator: MTMR9, the inactive partner of MTMR6/8, carries GO:0050821 by IDA.
