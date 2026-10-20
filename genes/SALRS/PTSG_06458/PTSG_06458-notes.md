# PTSG_06458 (Salpingoeca rosetta, F2UFV3) - curation notes

**Automated deep research was unavailable** (no deep-research provider key in this
environment), so no `-deep-research-*.md` file exists. These notes were written on
2026-10-02 from the cached publications, the UniProt record and the shared analysis in
`genes/MONBE/MBCDH12/MBCDH12-bioinformatics/`. This protein was reviewed together with
PTSG_05882, PTSG_11235 and MONBE MBCDH12.

## Identity and architecture

- F2UFV3, TrEMBL, 3697 aa, ORF PTSG_06458, EMBL EGD75381.1. UniProt name "Cadherin".
- Signal peptide 1-20. 23 cadherin repeats (595-3160). Fibronectin type II domain 3517-3563.
  TM 3613-3635. 62-aa cytoplasmic tail with no domain.
- **Correction:** the domain list in the project brief and propagation audit gives "cadherin
  repeats + laminin G". InterPro and UniProt show a fibronectin type II domain (PF00040) and
  no laminin G domain
  [file:MONBE/MBCDH12/MBCDH12-bioinformatics/RESULTS.md "F2UFV3 has a fibronectin type II domain, not a laminin G domain."].
- Canonical calcium motifs are present: 7 PROSITE CADHERIN_1 matches, 13 DXNDN-type and 10
  LDRE-type motifs.
- FunFam matches for individual repeats: CELSR3, Dachsous 1b, FAT1 and protocadherin 8. These
  are repeat-level similarities, not an orthology call.
- No PF01049 (Cadherin_C).

## Literature

- No experimental literature on this protein.
- The general choanoflagellate cadherin background is as in the PTSG_05882 notes
  [PMID:22837400; PMID:27189570].
- The only localized choanoflagellate cadherin is on the collar
  [PMID:22837400 "one cadherin (MBCDH1) has been shown to localize to the microvillar collar of M. brevicollis"].

## Track C

- The same 10 TreeGrafter rows from PTN000616280 (Bilateria) are present, with the same
  actions as PTSG_05882.
- Calcium ion binding: ACCEPT (canonical motifs).
- Plasma membrane: ACCEPT. Cell adhesion: KEEP_AS_NON_CORE.
- No laminin G or FN2-derived GO rows exist.
