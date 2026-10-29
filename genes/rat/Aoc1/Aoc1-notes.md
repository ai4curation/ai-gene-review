# Aoc1 (rat) notes

## Re-review 2026-10-10

GOA refresh (commit a3cf70b6d): 7 new rows, no retired rows.

- Six ISO rows from human AOC1 (UniProtKB:P19801), donor-splits of existing ISO rows from RGD:13918368 (or, for extracellular region, a located_in split of the is_active_in row): GO:0005576 extracellular region and GO:0005886 plasma membrane (KEEP_AS_NON_CORE); GO:0008131 primary methylamine oxidase activity, GO:0009445 putrescine metabolic process, GO:0050232 putrescine oxidase activity, GO:0052597 diamine oxidase activity (ACCEPT).
- GO:0008131 primary methylamine oxidase activity, IBA from PANTHER:PTN000067313 (copper amine oxidase family node; donors span human AOC1/2/3, plant, fungal and yeast CuAOs): ACCEPT. No evidence that rat Aoc1 has diverged from the clade's primary-amine oxidase activity [UniProtKB:P36633 "SIMILARITY: Belongs to the copper/topaquinone oxidase family."].

Action changes:
- GO:0005923 bicellular tight junction (IDA, PMID:18855986): REMOVE -> UNDECIDED. The abstract (full text not cached) reports tight-junction immunostaining of occludin and ZO-1, and measures DAO only as a plasma enzyme activity [PMID:18855986 "Plasma levels of diamine oxidase (DAO) and d-lactate were determined using an enzymatic spectrophotometry."]. Under the current policy an experimental annotation is not removed without the full text; a curator should confirm whether DAO itself was localized.

Other re-audit notes:
- GO:0008201 heparin binding (ISS/ISO from human): KEEP_AS_NON_CORE; support added from the deep-research citation of Gludovacz et al. 2021 ("Heparin-binding motif mutations of human diamine oxidase...").
- GO:0070062 extracellular exosome (ISO): MARK_AS_OVER_ANNOTATED kept.
- GO:0008150 ND row: REMOVE kept (placeholder superseded by specific process annotations).

Quote hygiene: 31 UniProtKB quotes ended "...histamine and 1-methylhistamine." but UniProt's FUNCTION sentence now continues; all were replaced with verbatim current text, and localization/cofactor/subunit/catalytic rows were re-anchored to the matching CC lines.

Description rewritten to remove curation commentary.

Open question: tight-junction IDA (PMID:18855986) needs full-text adjudication.
