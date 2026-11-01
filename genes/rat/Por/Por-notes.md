# Por (rat) review notes

## Session 1 (2026-10-28)

- `just fetch-gene rat Por` resolved P00388 (NCPR_RAT, RGD:68335, GeneID 29441); 63 GOA rows.
- Literature work is in `Por-deep-research-manual.md` (no deep-research API keys available).
- Key paper PMID:19152507 read in full: brain NO consumption depends on CYPOR, but purified
  CYPOR needs Trolox [PMID:19152507 "Hence, it appears that, during the purification process, CYPOR becomes separated from a partner needed for NO consumption."]
  and P450 inhibitors block it. So the NO dioxygenase MF is a property of the POR/P450
  system; POR's own contribution is NADPH-hemoprotein reductase activity. Marked the GO:0008941
  row over-annotated; kept NO catabolic process as non-core (POR does supply electrons).
- PTHR19384 family review (`interpro/panther/PTHR19384/PTHR19384-review.yaml`) already judged
  PTN002322100 (GO:0006809 NO biosynthesis, GO:0009725 response to hormone) TOO_DEEP: POR has no
  oxygenase domain. Removed the NO biosynthesis IBA.
- Cytosol (IBA PTN000453956, HPA-derived ISO/IEA) and nucleoplasm (HPA-derived) conflict with
  the membrane anchor [PMID:15823091 "NADPH-cytochrome P450 reductase (CPR) is a membrane-bound flavoprotein that interacts with the membrane via its N-terminal hydrophobic sequence (residues 1-56)."].
- Term mapping errors recorded as source_defects: iron-cytochrome-c reductase (EC 1.16.2.1)
  used for NADPH-cytochrome c reduction; hydrolase activity for an H2O2-mediated oxidative
  deformylation; carnitine metabolic process for an induction by L-carnitine; enzyme activator
  activity (human BHF-UCL donor) for electron donation to P450.
- Chondrocyte phenotypes (PMID:19264869) are indirect via cholesterol/Ihh: over-annotated.
- No NEW terms proposed. A cholesterol/sterol biosynthesis process term would pass the
  "does the work" test (POR reduces CYP51 and squalene monooxygenase), but human POR does not
  carry it either and the evidence here is a knockdown phenotype; raised as a question instead.
