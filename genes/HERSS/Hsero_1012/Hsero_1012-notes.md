# Hsero_1012 notes

## 2026-11-04 session (Claude, AI-assisted)

- Fetched with `just fetch-gene HERSS <accession> --alias Hsero_1012`: the gene-name lookup
  failed because the UniProt stream endpoint returned 503, so the accession route was used.
- No provider deep-research file was generated (no provider API keys in this session).
  The review rests on the UniProt record, the cached pathway papers
  [PMID:27059806] (abstract only) and, for fdeE, [PMID:39107441] (full text), the
  KEGG queries in `genes/HERSS/Hsero_1007/Hsero_1007-bioinformatics/`, and the P.
  putida ortholog reviews (PSEPK PP_3195-PP_3206) with their committed alignments.
- Literature search: PubMed/abstract terms "fde naringenin Herbaspirillum",
  "fdeE", "Hsero_1007" find only PMID:27059806 (genetics, fdeE/fdeC/fdeG mutants) and
  PMID:39107441 (biochemistry of purified FdeE). No other Fde protein has been assayed.
- Context: written for the module `modules/bacterial_flavonoid_degradation.yaml`.
