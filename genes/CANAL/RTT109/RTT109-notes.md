# RTT109 notes

## 2026-11-21

- `PTHR31571` splits cleanly into an active `PTHR31571:SF2` RTT109 branch and
  an orphan `PTHR31571:SF1` AIM6 branch. `CANAL/RTT109` is in SF2 with
  `yeast/RTT109`, `SCHPO/rtt109`, and `NEUCR/NCU09825`.
- The local QuickGO fetch returned only a header row for `Q5AAJ8`, even though
  UniProt lists direct CGD annotations for H3 acetyltransferase / H3K56
  acetyltransferase activity and Candida process annotations for DNA damage
  response, filamentous growth, and white-opaque phenotypic switching.
- The family PAINT file places `GO:0032931 histone H3K56 acetyltransferase
  activity`, `GO:0006974 DNA damage response`, and `GO:0005634 nucleus` at
  `PANTHER:PTN001586545`. Candida RTT109 is an unproblematic descendant of
  that node; Lopes da Rosa et al. and Wurtele et al. directly connect C.
  albicans RTT109 to H3K56ac and genotoxic stress.
- White-opaque switching and filamentation are direct Candida phenotypes, but
  this batch is focused on the compact PAINT assertions. They are worth a
  future CGD-specific curation pass if those CGD rows remain absent from the
  UniProt GOA mirror.
