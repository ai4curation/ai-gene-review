# dgcB curation notes

- Q88R23 has five N-terminal transmembrane helices and a C-terminal 4Fe-4S-binding region. [file:PSEPK/dgcB/dgcB-uniprot.txt, "DR   InterPro; IPR017896; 4Fe4S_Fe-S-bd."]
- Pseudomonas isotope tracing supports DgcB-dependent conversion of dimethylglycine to sarcosine. [PMID:17951379, "mutations in the dgcAB (PA5398-PA5399) genes"]
- The DgcB-to-ETF transfer is inferred from the conserved four-gene locus and
  has not been reconstituted; no quinone intermediate is asserted.

## 2026-11-04 completion session

No provider deep research was generated in this session (no API keys).
- DgcB is 72.2% identical to Csal_0991 over its full length and keeps both
  CxxCxxCxxxC [4Fe-4S] motifs, at 245 and 319 (`../dgcA/dgcA-bioinformatics/RESULTS.md`).
- The top-level proposed_new_terms entry was removed. That NTR is a
  dehydrogenase activity carried out by DgcA. DgcB is the ferredoxin substrate
  of the reaction, not the catalyst, so its MF is electron transfer activity.
- The 4Fe-4S binding core function was folded into the electron-transfer core
  function. NEW glycine betaine catabolic process (ISS).
