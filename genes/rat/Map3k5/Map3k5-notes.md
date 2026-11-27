# Map3k5 (rat) review notes

## Session 1 (initial review)

- `just fetch-gene rat Map3k5` resolved UniProt A0A8I6AEL0 (TrEMBL, RGD:1306565,
  GeneID 365057); GOA file keyed to the same accession, 68 rows.
- No deep-research provider available; literature summary in
  `Map3k5-deep-research-manual.md`.
- Full text read: PMID:20550965 (perfused rat heart, ASK1 immune-complex kinase
  assay; "during cardiac ischaemia ASK1 couples preferentially to p38 rather than
  JNK") and PMID:20716917 (rat RIE-1 cells, ASK1 siRNA reduces JNK and p38
  phosphorylation). Other rat papers abstract-only.
- Ontology checks (OAK, sqlite:obo:go):
  - GO:0004709 MAPKKK is_a GO:0004674 protein Ser/Thr kinase activity, under
    GO:0004672 / GO:0016301 / GO:0016740; it is NOT under GO:0106310 protein serine
    kinase activity.
  - GO:0004706 JUN kinase kinase kinase activity is_a GO:0004709.
  - GO:0007254 JNK cascade and GO:0038066 p38MAPK cascade are is_a GO:0000165 MAPK
    cascade, but NOT descendants of GO:0051403 stress-activated MAPK cascade in the
    current ontology (whose only children are fungal cascades).
  - GO:0070059 is_a GO:0034976 response to ER stress; GO:0008631 and GO:0070059 are
    descendants of GO:0097190 apoptotic signaling pathway.
  - GO:0043065 and GO:0010666 are descendants of GO:0043067; GO:0046330 and
    GO:1900745 are descendants of GO:0043410.
  - GO:1902911 protein kinase complex is_a GO:0032991. GO:1990604 IRE1-TRAF2-ASK1
    complex is under GO:0032991 but not under GO:1902911.
  - GO:0042803 is_a GO:0042802.
- Decisions:
  - Core: MAPKKK activity (ACCEPT on IDA/IBA/ISO/IEA), JUNKKK activity, JNK cascade,
    p38MAPK cascade, intrinsic apoptotic signalling in response to oxidative stress
    and to ER stress.
  - Generic kinase/transferase/nucleotide-binding rows -> MODIFY to the specific
    MAPKKK activity or ATP binding.
  - GO:0009897 external side of plasma membrane (RGD IDA, PMID:12786973,
    abstract-only): ASK1 is a cytoplasmic kinase; the abstract says it colocalised
    with Daxx/TRAF2 "at the outer membrane of injured CA3 neurons", which most
    plausibly means the cell periphery (cytoplasmic face). Marked over-annotated, not
    removed, and a WRONG_TERM / CHECK source defect recorded for RGD.
  - positive regulation of DNA-templated transcription (from QRS paper reporter assay):
    indirect via AP-1; over-annotation.
  - Tissue phenotypes (cardiomyocyte apoptosis, VSMC proliferation, endothelial
    apoptosis, myoblast differentiation): KEEP_AS_NON_CORE.
- No NEW terms proposed.
