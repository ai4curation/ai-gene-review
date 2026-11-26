# rtt109 notes

## 2026-11-21

- `SCHPO/rtt109` is the fission-yeast `PTHR31571:SF2` RTT109-family member and
  is one of the PomBase seeds behind the fungal `PANTHER:PTN001586545`
  H3K56-acetyltransferase / DNA-damage PAINT node.
- An initial local QuickGO fetch returned no UniProt GOA rows for `Q9Y7Y5`, but
  a refreshed QuickGO snapshot recovered the GO-Central PAINT, PomBase and
  UniProt rows for chromatin, nucleus, histone acetyltransferase activity,
  H3K56 acetyltransferase activity, protein-lysine acetyltransferase activity
  and DNA damage response.
- PMID:17369611 is abstract-only locally and was not overinterpreted beyond
  direct H3K56ac cell-cycle / DNA-damage framing. PMID:17690098 is also
  abstract-only but explicitly says the S. pombe Rtt109 homolog has
  Asf1-dependent H3K56 HAT activity in vitro.
- PMID:20656950 was added for the UniProt experimental EC/H3K56 rows. It is a
  Pneumocystis Rtt109 paper, but the full text directly uses recombinant S.
  pombe Rtt109 as the H3K56 acetyltransferase comparator.
