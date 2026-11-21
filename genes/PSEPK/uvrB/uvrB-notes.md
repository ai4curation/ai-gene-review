# uvrB (Pseudomonas putida KT2440, Q88LF9, PP_1974) review notes

Reviewer: Claude (AI-assisted). Session date: 2026-11-10.

## Sources

- `uvrB-deep-research-falcon.md` (provider report). It found no KT2440-specific experimental work on
  uvrB: "While direct *P. putida* KT2440 uvrB knock-out phenotypes were not retrieved in the available corpus".
  Its mechanistic content is family-level (reviews of E. coli/thermophile UvrB).
- UniProt Q88LF9: all functional text is HAMAP rule MF_00204 (curated UniRule).
- E. coli UvrB primary literature, reviewed in `genes/ECOLI/uvrB/uvrB-notes.md` (ATPase:
  PMID:2974538, PMID:10713125, PMID:8035457; damaged DNA recognition: PMID:11689453; incision
  chemistry in UvrC: PMID:10671556).
- Own analysis: `uvrB-bioinformatics/RESULTS.md` (72.5% identity to E. coli UvrB over 659 aligned
  columns; Walker A and all mutagenised beta-hairpin residues conserved).
- PubMed search "Pseudomonas putida lexA regulon" returned PMID:17933893 (KT2440 LexA1/LexA2
  regulons; cached text is abstract-level and does not list uvrB). PMID:8808952 shows the
  P. aeruginosa uvrB lacks a LexA box and is not DNA-damage inducible
  [PMID:8808952 "contrary to what happens with the homologous gene of E. coli, the P. aeruginosa uvrB gene is not DNA damage inducible"].

## Verdict changes from the earlier draft

- GO:0006281 DNA repair: KEEP_AS_NON_CORE -> MODIFY to GO:0006289 (the draft argued "correct but
  general", which by project rules is MODIFY).
- GO:0016787 hydrolase activity: MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0016887 (same rule).
- GO:0009432 SOS response: KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED. The UniRule transfers the
  E. coli SOS assignment; the closest characterised Pseudomonas uvrB is not SOS-inducible and there
  is no KT2440 evidence that uvrB is LexA-regulated. (E. coli uvrB keeps the term as non-core.)
- Core functions now cite publications/UniProt rather than a GO_REF; GO:0016887 is the first core
  function (module function), with GO:0003684 damaged DNA binding as the second.
- Other verdicts kept, now with supporting quotes on every row.
