# PP_4348 curation notes

## GO term status verification

Checked the EMBL-EBI QuickGO API on 2026-07-19:

- `GO:0004121` returned `isObsolete: true` with the comment: "The reason for obsoletion is that this term is equivalent to GO:0047804 cysteine-S-conjugate beta-lyase activity."
- `GO:0047804` returned `isObsolete: false` and lists "cystathionine beta-lyase activity" as a related synonym.

API request: `https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0004121,GO%3A0047804`
