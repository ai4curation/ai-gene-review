# let-363 review notes

## Session 1 (initial review)

- Fetched with `just fetch-gene worm let-363`; UniProt Q95Q95 (TOR_CAEEL) confirmed; 33 GOA rows.
- No deep-research provider; manual synthesis in `let-363-deep-research-manual.md`.
- Full text read: PMID:18804378, 21952218, 35479415, 23705068, 23973804, 18282106,
  22278922 (abstract and key sections). Abstract only: PMID:12225660, 12150926,
  17277769, 14668850.

### Key judgments

- Core MF: protein serine/threonine kinase activity. Direct support is the native
  TORC1 IP kinase assay [PMID:35479415 "Among the eighteen candidates tested, four peptides were identified as direct TORC1 targets by this strategy"]. LET-363 is the only kinase in the IP.
- Complex membership TORC1/TORC2 is well supported by reciprocal co-IP
  [PMID:21952218 "the LET-363 IP contained both DAF-15 and RICT-1"].
- `box C/D snoRNP assembly` (IMP, PMID:18804378): the data are FIB-1 mislocalization
  after let-363 RNAi. TOR is an upstream regulator, not a participant in snoRNP
  assembly; marked over-annotated. No "regulation of box C/D snoRNP assembly" term exists (OLS search returned nothing).
- `mesendoderm development` (IGI with skn-1, PMID:23973804): let-363 RNAi rescued only 1.1%
  of skn-1 embryos; the authors call the effect mild and attribute it to TORC2. Marked over-annotated.
- `TOR signaling` rows: modified to the specific TORC1/TORC2 signaling terms the
  gene already carries by IBA.
- `regulation of translation` (IMP): modified to `positive regulation of translation`.
- `kinase activity` (InterPro IEA): modified to protein serine/threonine kinase activity.
- `protein-containing complex binding` (InterPro FRB domain IEA): the mapping reflects
  FKBP12-rapamycin binding, a pharmacological interaction; uninformative. Over-annotated.
- `animal gross anatomical part developmental process` (ARBA): unvetted, vague; over-annotated.
- No NEW rows proposed. Autophagy is already covered by the IBA row on negative
  regulation of macroautophagy, which is consistent with worm data
  [PMID:18282106 "we observed a significant increase in the number of autophagic vesicles in their L3 progeny"].
