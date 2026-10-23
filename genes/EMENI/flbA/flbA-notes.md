# flbA (Aspergillus nidulans) — curation notes
UniProt P38093 (FLBA_EMENI). RGS protein; repressive gating tier (attenuates FadA).
- RGS domain protein antagonizing FadA to block proliferation and allow development. [PMID:8895563 "flbA encodes an Aspergillus nidulans RGS (regulator of G protein signaling) domain protein that is required for control of mycelial proliferation and activation of asexual sporulation"]. Overexpression activates brlA prematurely [PMID:7830576].
- Core MF GO:0005096 GTPase activator activity. GO:0045461 ST biosynthetic process over-annotation; GO:0045574 sterigmatocystin catabolic process flagged likely-spurious (contradicts FlbA's positive-regulatory role in ST biosynthesis).

## Re-review 2026-10-01 (GOA refresh)

- No new GOA rows and no vanished rows for flbA in the refreshed snapshot.
- GO:0045574 sterigmatocystin catabolic process (IMP, PMID:9339347): changed
  MARK_AS_OVER_ANNOTATED -> UNDECIDED. The earlier "likely curation artifact"
  call second-guessed an experimental annotation whose paper is cached as abstract
  only; the abstract does not let us see what the curator read, so the row is left
  undecided rather than overruled.
