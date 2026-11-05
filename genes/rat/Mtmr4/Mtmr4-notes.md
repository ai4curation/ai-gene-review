# Mtmr4 (rat) review notes

## 2026-10-28 session

- Fetched A0A8I6A3Q2 (TrEMBL, RGD:1310306, GeneID 287607); accession matches the
  requested one. 31 GOA rows: ARBA IEA, InterPro/EC/SubCell IEA, RGD ISO from human
  MTMR4 (Q9NYA4), and one rat IEP (PMID:19125695).
- No deep-research key; literature summary in `Mtmr4-deep-research-manual.md`.
- Motif scan (`Mtmr4-bioinformatics/RESULTS.md`): catalytic Cys407 intact, FYVE
  RRHHCR, PY motif PPLY at 1001, GPPSLEY CEP55 motif at 5 - rat Mtmr4 conserves
  every element used in the human experiments, so ISO transfer is well founded.
- Decisions:
  - Core MF: PtdIns3P 3-phosphatase (ACCEPT). PtdIns(3,5)P2 3-phosphatase kept
    non-core (family-level evidence; no MTMR4-specific assay read).
  - PTP activity (EC 3.1.3.48 mapping from PTP signature): over-annotation; no
    phosphotyrosine substrate reported [PMID:20061380 describes serine SXS motif].
  - Ser/Thr protein phosphatase: kept non-core, supported by R-Smad SXS
    dephosphorylation (one lab, two papers).
  - Generic membrane/endomembrane/endosome membrane rows MODIFIED to the specific
    endosome membrane terms the gene carries.
  - metal ion binding -> zinc ion binding (FYVE zinc finger).
  - phosphatidylinositol biosynthetic process: over-annotation (enzyme removes the
    3-phosphate signal; PI formation is incidental).
  - IEP response to denervation...: expression drop only, attributed to Nedd4
    degradation; "involved in regulation of muscle adaptation" not shown ->
    MARK_AS_OVER_ANNOTATED.
  - NEW: phosphatidylinositol-3-phosphate binding (FYVE domain signature + FYVE-
    dependent endosomal targeting).
