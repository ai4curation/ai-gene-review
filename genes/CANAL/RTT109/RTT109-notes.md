# RTT109 notes

## 2026-11-21

- `PTHR31571` splits cleanly into an active `PTHR31571:SF2` RTT109 branch and
  an orphan `PTHR31571:SF1` AIM6 branch. `CANAL/RTT109` is in SF2 with
  `yeast/RTT109`, `SCHPO/rtt109`, and `NEUCR/NCU09825`.
- An initial local QuickGO fetch returned only a header row for `Q5AAJ8`, but a
  refreshed QuickGO snapshot recovered the GO-Central PAINT, UniProt/Rhea,
  InterPro and CGD rows for C. albicans RTT109.
- The family PAINT file places `GO:0032931 histone H3K56 acetyltransferase
  activity`, `GO:0006974 DNA damage response`, and `GO:0005634 nucleus` at
  `PANTHER:PTN001586545`. Candida RTT109 is an unproblematic descendant of
  that node; Lopes da Rosa et al. and Wurtele et al. directly connect C.
  albicans RTT109 to H3K56ac and genotoxic stress.
- The CGD filamentation and white-opaque switching IMP rows are species-specific
  phenotypic outputs of the H3K56ac chromatin pathway, not new molecular
  functions, and are kept as direct Candida process annotations in this pass.
