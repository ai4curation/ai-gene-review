# betT-I review notes

## Identity and scope

- Target: `betT-I`, PP_5061, UniProt Q88CW9, *Pseudomonas putida* KT2440.
- Reviewed files: `betT-I-ai-review.yaml`, `betT-I-goa.tsv`, and `betT-I-uniprot.txt`.
- Retrieval date for external sources: 2026-07-26.

## Exact provenance

### UniProt record

Source: `file:PSEPK/betT-I/betT-I-uniprot.txt`.

- `"DE   SubName: Full=Choline transporter"`
- `"GN   OrderedLocusNames=PP_5061"`
- `"CC   -!- SUBCELLULAR LOCATION: Cell membrane"`
- `"CC       Multi-pass membrane protein"`
- `"DR   GO; GO:0022857; F:transmembrane transporter activity; IEA:InterPro."`
- Twelve transmembrane segments are predicted between residues 20 and 506.

The protein name is submission-derived and the GO rows are electronic; the record contains no substrate assay.

### KT2440 locus and paralog specificity

Source: Belda et al., 2016, PMID:26913973, DOI:10.1111/1462-2920.13230.

- The cached publication record is abstract-only and does not contain a
  BetT-I-specific substrate statement.
- Earlier working notes attributed choline transport to BetT-I and BetT-III
  and glycine-betaine transport to BetT-II, but no directly checkable passage
  or target-specific transport assay is currently available.
- The adjacency and divergent orientation of betT-I relative to betIBA make
  choline uptake a useful hypothesis, not sufficient evidence for a
  choline-specific GO annotation.

## Curation conclusions

- Accept plasma-membrane localization.
- Accept generic transmembrane transporter activity and transmembrane transport.
- Do not promote choline specificity into the reviewed annotations or core
  function until a directly checkable source or substrate assay is available.
- Keep choline uptake as the leading locus-based hypothesis.
