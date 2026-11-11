# Il1rl1 (rat) review notes

- 2026-10-28: Created review. fetch-gene resolved Q62611 (ILRL1_RAT, RGD:2894, GeneID 25556) as
  expected; GOA keyed to Q62611 (40 rows).
- No deep-research API; see `Il1rl1-deep-research-manual.md`.
- Key decisions:
  - Core MF = interleukin-33 receptor activity (GO:0002114, ISO from human/mouse) plus IL-33
    binding; soluble isoform B acts as IL-33 decoy [PMID:17492053 "sST2 functions in myocardium
    as a soluble decoy receptor"].
  - GO:0004908 interleukin-1 receptor activity (InterPro2GO IPR004074) is a family-level mapping;
    ST2 does not bind IL-1. GO:0002114 is not a descendant of GO:0004908 (OLS ancestors checked),
    so MODIFY laterally to GO:0002114 and log a source defect.
  - GO:0061809 NAD+ nucleosidase activity, cyclic ADP-ribose generating (EC 3.2.2.6 mapping from
    PROSITE TIR rule): no evidence any IL-1R-family TIR is an NADase; REMOVE + source defect.
  - IEP rows (mechanical stimulus, endothelin, nutrient levels) are expression responses of the
    gene; kept as non-core.
  - Many ISO immune-regulation BP rows from mouse (Th2 skewing, IL-5, IFN-gamma) are downstream
    consequences of IL-33 signalling; kept as non-core.
- Comparator for NEW: none proposed.
