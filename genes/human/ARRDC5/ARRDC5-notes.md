# ARRDC5 review notes

## Sources
- Affinage: trust gates clear.
- All functional data are from mouse:
  - PMID:37069147 (full text): knockout; male sterility; spermiogenesis defect.
  - PMID:37997706 (abstract): SUN5/NDC1, SEC22A.
  - PMID:41420860 (full text): TEX38; cytoplasmic droplet.
  - PMID:40783453 (full text): TEX38/CLGN/PDILT; ADAM3.
- Mouse Arrdc5 (Q497K5) donor rows: IDA/EXP membrane and IMP spermatogenesis (QuickGO).
- The endosome and plasma membrane IBAs come from the ARRDC3-only node PTN008513893. ARRDC5 has no localization data for these compartments, and its biology is testis-specific, so they are non-core with an UNRESOLVED propagation review.

## Decisions
- ACCEPT: membrane (IEA, ISS).
- MODIFY:
  - Molecular adaptor activity (IBA) → protein-macromolecule adaptor activity.
  - Spermatogenesis (ISS) → spermatid development.
- KEEP_AS_NON_CORE: cytoplasm (IBA); endosome and plasma membrane (IBA from ARRDC3).

## 2026-10-04 review round (PR #4211)

- ARRDC5 lacks PY motifs [PMID:23236378 "With the exception of ARRDC5, all mammalian aArrs have a pair of PY motifs."]. Location IBAs seeded only by ARRDC3 are UNDECIDED.
- Mouse Arrdc5 membrane (UniProt IDA PMID:37069147, EXP PMID:37997706): the full text of 37069147 has no ARRDC5 membrane statement, and 37997706 is abstract-only. UNDECIDED.
- ZDHHC19 S-palmitoylates ARRDC5 (PMID:40030029, not cached). This is ZDHHC19 activity, so there is no ARRDC5 annotation.

## 2026-11-23 ORGANELLES endosome batch 1

- Endosome IBA (is_active_in, PTN008513893, seeded only by ARRDC3): UNDECIDED kept, dated reason added.
- ARRDC5 has no localisation data: UniProt only "Membrane" by similarity to mouse Q497K5; PMID:37069147 (full text) could not detect the protein reliably with antibodies and used Arrdc5-eGfp mice for cell-type expression only.
- Added a WRONG_QUALIFIER CHECK source defect (GO_CENTRAL): no ARRDC5 activity shown in endosomes.
