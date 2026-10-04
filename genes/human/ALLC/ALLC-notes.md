# ALLC (Q8N6M5) review notes

## 2026-10-04: PAINT/affinage review

UniProt calls ALLC a "Probable inactive allantoicase". The gene is retained even though the activity is gone:
- **Activity absent:** [PMID:12036579 "In mammals, as well as in birds and reptiles, the activity of allantoicase is absent; notwithstanding, we recently cloned human and mouse cDNA sequences with high similarity with previously characterized allantoicases."]
- **Pathway lost:** the uricolytic pathway was dismantled in vertebrates.
- **Affinage:** only fungal (Neurospora) and Dictyostelium findings, none for mammals.

Decisions:
- **Both GOA rows are IEA (allantoicase activity; allantoin catabolic process): REMOVE.**
  - The activity is absent from mammalian tissues.
  - The pathway and substrate are absent from humans.
  - The mouse ortholog used as a source is also "probably inactive".
- **The gene is recorded as WHOLLY_DARK** (top-level gap), with core_functions empty.

## Round 1 (PR #3984 review)

- **Corrected "allantoin is not produced".** Humans lack urate oxidase, but allantoin still forms non-enzymatically from oxidized urate and is excreted, not degraded. The REMOVE of the catabolic-process row stands on "no catabolic pathway".
- **Corrected the species range.** Plants use allantoate amidohydrolase rather than allantoicase. The pathway was lost in amniotes, not in all vertebrates.
- **Added protein-level evidence:** PE 1 / proteomics. Also cited PANTHER's independent "INACTIVE ALLANTOICASE-RELATED" subfamily (PTHR12045:SF3).
- **Fixed a misused quote.** The affinage support quote now cites the record's own "no mechanism known for the human protein" sentence.
