# Creb1 (rat) review notes

## Session 2026-10-28

- `just fetch-gene rat Creb1` resolved P15337 (CREB1_RAT, RGD:620218, GeneID 81646); 178 GOA rows.
- No deep-research keys; literature synthesis written by hand to `Creb1-deep-research-manual.md`.
- Key paper PMID:21367864 (Davies et al. 2011, full text): FRA-2 represses Rgs4 at a CRE half-site
  (AP-1R tgcgtca); CREB is a constituent of both EMSA complexes on this element and binds
  constitutively [PMID:21367864 "indicates constitutive CREB binding to this sequence"], with night
  phosphorylation [PMID:21367864 "CREB protein binding to the Rgs4 promoter appears to be
  phosphorylated at night"]. Supports the IDA GO:0000976 row (refined to CRE binding) and the IEP
  circadian rhythm row (day/night phospho-CREB in pineal).

## Decisions

- Core MF: GO:0001228 (activator, Pol II-specific) + GO:0035497 CRE binding + GO:0001223
  transcription coactivator binding (pKID-KIX, PMID:9413984). General MF/DNA-binding rows refined to
  these by MODIFY.
- General transcription BP rows (GO:0006355, GO:0006357, GO:0045893, GO:0042789, GO:0010467)
  refined to GO:0045944.
- Physiology/response rows kept as non-core. Rows from PMID:22523357 (DHEA, hypobaric hypoxia) are
  UNDECIDED: the abstract does not mention CREB and the full text is not cached.
- PMID:16687181 memory row is IMP but the abstract only reports correlated changes in pCREB after D1
  ligands; recorded a WRONG_EVIDENCE_CODE CHECK source defect.
- Lactation and mammary gland development (mouse ISO via PMID:16141355) are remote endocrine
  consequences of hypothalamic GHRH deficiency: MARK_AS_OVER_ANNOTATED.
- Bare protein binding (TOX3, PMID:19196971) modified to transcription coactivator binding,
  because TOX3 acts as a CRE-dependent co-activator associated with the CREB-CBP complex.
- No NEW rows: the existing annotation set already covers the core activities.

## Curation gaps (not knowledge gaps)

- Rat GOA has no direct row for GO:0035497 from rat experiments even though many rat EMSA/ChIP
  papers show CRE binding; the refined rows cover it.
