# Psmc6 (rat) review notes

## 2026-10-28 session

- `just fetch-gene rat Psmc6` resolved G3V6W6 (TrEMBL, RGD:1308825, GeneID 289990);
  as requested. GOA has 20 rows. No IBA rows are present (unlike rat Psmc4), so the
  base-subcomplex, proteasome-activating and ubiquitin-dependent catabolism terms are
  reached through MODIFY replacements and one NEW contributes_to row.
- Literature compiled manually in `Psmc6-deep-research-manual.md` (no API keys).
- Key paper PMID:18986984 read in full: rat data = endogenous Rpt4 staining at Htt
  inclusions in rat hippocampal neurons and siRNA knockdown reducing inclusions
  [PMID:18986984 "Rpt4 and Rpt3 co-localize with poly(Q) inclusions."]. Gradient work
  (26S vs APIS) is in 293T cells.
- Rpt4 lacks an HbYX tail (ends ...DYKPV) and its tail is not seen in an alpha pocket
  [PMID:29636472 "with the exception of Rpt4"]; it contributes to the hexamer's
  proteasome-activating activity (unfolding/translocation) rather than gate opening
  by docking.
- Decisions:
  - Complex rows (proteasome complex, proteasome accessory complex) MODIFY to
    GO:0008540 base subcomplex. Cytosolic proteasome complex IDA ACCEPT.
  - nucleus -> nucleoplasm, cytoplasm -> cytosol (MODIFY).
  - ATP binding, ATP hydrolysis ACCEPT; NEW contributes_to GO:0036402.
  - proteasomal protein catabolic process NAS -> GO:0043161.
  - inclusion body IDA and positive regulation of inclusion body assembly IMP:
    KEEP_AS_NON_CORE (genuine rat data, disease model).
  - synaptic vesicle IDA/NAS and regulation of AMPA receptor activity IDA:
    UNDECIDED (abstract-only paper, 19S-wide claim, DUB-dependent effect).
  - identical protein binding ISO/IEA: MARK_AS_OVER_ANNOTATED (untraceable, no
    biological support for homo-oligomerisation).
