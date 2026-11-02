# FMOGS-OX1 (Q9SS04, At1g65860) review notes

## Session 2026-09-30

No falcon deep-research file was present during review; notes are based on cached
publications and the UniProt record.

### Function
- FMO GS-OX1 is the flavin monooxygenase that S-oxygenates methylthioalkyl to
  methylsulfinylalkyl glucosinolates [PMID:17461789 "We report the identification of an
  Arabidopsis flavin-monooxygenase (FMO) enzyme, FMO(GS-OX1), which catalyzes the
  conversion of methylthioalkyl GSLs into methylsulfinylalkyl GSLs."]
- Overexpression gives near-complete conversion and ~5-fold more glucoraphanin in seeds
  [PMID:17461789 "with an approximately fivefold increase in 4-methylsulfinylbutyl GSL in seeds"]
- Substrate requires the S-glucosyl group; acts on desulfo and intact GSLs but not Met or
  aldoxime [PMID:18799661 "FMO GS-OX1 S -oxygenated desulfo and intact GSLs, but not the
  structurally related Met and aldoxime that do not contain an S -Glc group."]
- Chain-length independent (4-MTB and 8-MTO) [PMID:18799661 "Interestingly, all five
  recombinant proteins converted 8-MTO to 8-MSO"]
- Redundant crucifer-specific subclade FMO GS-OX1-5; GS-OX1 and GS-OX2 control 8-MSO in
  planta [PMID:18799661 "both FMO GS-OX1 and FMO GS-OX2 control 8-MSO production in planta"]
- UniProt: EC 1.14.13.237, RHEA:42208; FAD cofactor (by similarity); knockout accumulates
  methylthiobutyl, -pentyl, -heptyl GSLs in leaves.

### Curation decisions
- All S-oxygenase MF terms (GO:0080102-0080107) accepted. Note GO labels for C4-C8 terms
  say "methylthiopropyl" (label error in GO; raised as a suggested question).
- N,N-dimethylaniline monooxygenase (InterPro2GO) -> MODIFY to GO:0080103.
- Nucleus (AtSubP ISM) -> REMOVE: no support.
- NEW: GO:0019761 glucosinolate biosynthetic process. Participation: FMO catalyzes a
  pathway step. Comparator: AOP2 carries GO:0019761 (IDA, PMID:11251105).
- Core MF: GO:0080103; BP: GO:0019761. Subcellular location unknown (not asserted).


## Module-member evidence audit — 2026-10-25

Reviewed every original row (14) and core function using review/annotation-reviewer instructions, current cached primary publications and the existing research. Preserved all source annotation fields and all pre-existing proposed rows. Reused the existing genuine Falcon provider report and its artifacts. These plant targets do not require bacterial FEBA retrieval.

Correct original target paper is PMID17461789 (Hansen2007). Full18799661 also directly re-assays GSOX1 as comparator in Fig4B on desulfo4-MTB and Fig5B on seed-derived substrates including8-MTO; not merely extrapolation from paralogs2–5. It accepts desulfo and intact glucosinolates, so sulfation-before-S-oxygenation is not an exclusive biochemical order. Current QuickGO definitions GO0080103–107 themselves contain longer-chain methylthiopropyl wording; original rows/labels preserved. Authored core now uses a supported proposed substrate-class MF (EC1.14.13.237;RHEA42208, checked in curated CC:CATALYTIC ACTIVITY), not the chemically malformed longer-chain term. Nuclear location is unresolved rather than biologically impossible.

Broad and substrate-specific terms were assessed consistently across evidence codes. No NEW rows were added. Previously proposed rows were evaluated for direct participation rather than filled from pathway adjacency. Experimental cohort calls whose protein-level data were not verified were left UNDECIDED; full-text availability alone was not treated as proof of a target-specific assay. Original sources and provider reports were not hand-edited.
