# ubiC (P26602, E. coli K-12) review notes

## Sources
- No deep-research provider output (provider API keys unavailable); built from UniProt, cached abstracts
  (PMID:4595202, PMID:1644758, PMID:8012607, PMID:11825618, PMID:15690043) and the PTHR38683 PAINT file.

## Findings
- First step of UQ synthesis [PMID:1644758 "In Escherichia coli, chorismate lyase catalyzes the first step in
  ubiquinone biosynthesis, the conversion of chorismate to 4-hydroxybenzoate."]
- Sole in vivo 4HB source [PMID:8012607 "A feeding experiment with [1,7-13C2]shikimate confirmed the chorismate
  pyruvate-lyase as the sole enzymic source of 4-hydroxybenzoate in vivo."]
- Product retention, possible delivery to UbiA [PMID:11825618 "may involve a mechanism of directed delivery to
  the membrane-bound enzyme that follows CL in the ubiquinone pathway"].

## Decisions
- All chorismate lyase rows ACCEPT (core MF, matches module annoton GO:0008813).
- Cytoplasm IEA MODIFY to cytosol (has IDA + IBA cytosol).
- Pyruvate biosynthetic process (UniRule IEA) MARK_AS_OVER_ANNOTATED: coproduct, consistent with PSEPK ubiC.
- AceE IPI (high-throughput) REMOVE per protein-binding policy.
