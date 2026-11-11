# smoI (Atu3285, A9CEZ0) notes

## Deep research
- 2026-11-10: perplexity deep research fails in this environment (no provider credentials;
  "All providers failed", tried on smoA). Review built from UniProt and cached literature.
- Fetched PMID:30276262 (full text from PMC) with `ai-gene-review fetch-pmid`.

## Literature
- PMID:30276262: AtSQase (RefSeq WP_035199431) GH31 SQase with ERWY motif; PNPSQ kcat 22.3 s-1,
  KM 0.21 mM; no PNPGlc activity; hydrolyzes both SQGro epimers, prefers 2'R; structures 5OHS/5OHY;
  E270/K245 second-shell pair needed for catalysis
  [PMID:30276262 "AtSQase exhibited high specificity for 4-nitrophenyl α-d-sulfoquinovoside (PNPSQ)"]
- PMID:35074914: identifies Atu3285 (smoI) as that SQase; SmoI-D455N/SQGro complex (7OFX)
  [PMID:35074914 "We previously reported that Atu3285 (smoI) encodes an SQase that preferentially hydrolyzes 2'R-SQGro, the natural stereoisomer of this glycoside"]
  and SmoC cannot use SQGro, so SmoI must act first.

## PAINT
- PTHR46959 PAINT: PTN002333608 GO:1990929 IBD seeded by E. coli YihQ (P32138); A9CEZ0 is not in
  the PAINT leaf GAF (no IBA row on SmoI). PTN000510055 GO:0016787 (taxon Eukaryota, seed P32138).

## Decisions
- GO:0004553 -> MODIFY GO:1990929; NEW GO:1990929 IDA PMID:30276262.
- GO:0005975 -> MODIFY GO:1902777.
- GO:0030246 carbohydrate binding (IPR011013) -> MARK_AS_OVER_ANNOTATED.
- PANTHER PTHR46959:SF2 (with YihQ).

## 2026-11-11 PR review follow-up
- GO:0005975 replacement changed from GO:1902777 to GO:0016139 glycoside catabolic process, to agree
  with the E. coli YihQ review: SmoI hydrolyses the glycoside SQGro and produces SQ, but does none
  of the work of SQ breakdown (participation test), so GO:1902777 is not proposed.
