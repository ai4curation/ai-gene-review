# HAC1 (S. cerevisiae, P41546) review notes

Deep research: not run (falcon times out in this environment; perplexity-lite unavailable).
Review based on cached GOA-cited publications and the UniProt entry.

## Key findings
- bZIP transcription factor of the yeast UPR; binds UPRE and activates transcription
  [PMID:9077435 "The ERN4 gene encodes a basic-leucine zipper protein (Ern4p) that specifically binds to UPRE in vitro and activates transcription in vivo."]
- Required for the UPR; protein made only in UPR-activated cells via Ire1-dependent mRNA splicing
  [PMID:8898193 "Surprisingly, Hac1p is found in UPR-activated cells only, and its level is controlled by regulated splicing of its mRNA."]
- Hac1i represses early meiotic genes via Rpd3-Sin3 HDAC
  [PMID:15141165 "Spliced Hac1p (Hac1ip) is a negative regulator of differentiation responses to nitrogen starvation, pseudohyphal growth, and meiosis."]

## Curation decisions
- `meiotic cell cycle` (IDA/IMP) -> MODIFY to GO:0051447 negative regulation of meiotic cell cycle.
- Repression of Pol II transcription kept as non-core.
- Core MF: GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific.
