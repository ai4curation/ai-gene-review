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
