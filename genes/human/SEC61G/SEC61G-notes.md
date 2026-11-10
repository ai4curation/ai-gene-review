# SEC61G (human, P60059) curation notes

Deep research providers were unavailable; evidence from cached publications and UniProt.

## Localization (benchmark-relevant)
- Intracellular ER membrane protein, NOT cell surface: UniProt `SUBCELLULAR LOCATION: Endoplasmic
  reticulum membrane {ECO:0000269|PubMed:36261522}; Single-pass membrane protein`.
- The Reactome-derived `GO:0005829 cytosol` row was marked over-annotated (pathway compartment
  bookkeeping, not a cytosolic pool); generic `membrane` modified to ER membrane.

## Function
- Core subunit of the heterotrimeric translocon: UniProt "The SEC61 channel-forming translocon
  complex consists of channel-forming core components SEC61A1, SEC61B and SEC61G"; "Forms a
  ribosome receptor and a gated pore in the ER membrane, both functions required for
  cotranslational translocation of nascent polypeptides"; hands multi-pass substrates to the
  multi-pass translocon [PMID:32820719, PMID:36261522].
- Accepted: Sec61 translocon complex, transmembrane protein transporter activity, ribosome binding,
  SRP-dependent cotranslational translocation, post-translational translocation, protein targeting
  to ER, protein transmembrane transport.
- Generic transport/targeting parents (`GO:0006605`, `GO:0006886`, `GO:0015031`) marked
  TOO_GENERAL.
- `GO:0071261 Ssh1 translocon complex` (IBA) kept as non-core: the yeast gamma subunit Sss1 serves
  both Sec61 and Ssh1, but humans have no Ssh1 complex.
- Nine generic `GO:0005515` rows removed per policy.
