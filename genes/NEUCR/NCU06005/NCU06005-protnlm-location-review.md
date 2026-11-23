# NCU06005: ProtNLM localization review

Accession: Q7S2F2; original locus: NCU06005. Source method: ProtNLM2. Source version: live API snapshot 2026-09-09T03:00:51.831347+00:00.

The complete prediction record is preserved in [NCU06005-protnlm-source.json](NCU06005-protnlm-source.json); claim metadata are also preserved in [NCU06005-protnlm-provenance.json](NCU06005-protnlm-provenance.json). Original UniProt SL identifiers are retained; these are not substituted with GO terms.

## Claim 1: SL-0086

Original text: **Cytoplasm**

Original evidence:

```json
[
  {
    "evidenceCode": "ECO:0008006",
    "id": "ProtNLM2",
    "properties": [
      {
        "key": "model_score",
        "value": "1.00"
      },
      {
        "key": "string_match_text",
        "value": "GO:0005739"
      },
      {
        "key": "string_match_location",
        "value": "GO"
      },
      {
        "key": "string_match_type",
        "value": "hydrated"
      }
    ],
    "source": "Google"
  }
]
```

Assessment: **LSP** (confidence score 2).

Cytoplasm is supported by the glycerol-kinase-specific target family and by classical N. crassa enzymology identifying a cytosolic glycerokinase in glycerol dissimilation, distinct from mitochondrial glycerol-3-phosphate dehydrogenase (PMID:6284716). NCU06005 is the sole glycerol kinase gene in the reference proteome, so that cytosolic activity is attributable to this locus. Q7S2F2 is the only product of the gene and carries both FGGY kinase domains, so no feature is missing. The curated gene review already carries the more specific cytosol for this gene, and GOA carries mitochondrion (IBA) as a minor inherited location; the emitted Cytoplasm is therefore correct but less precise than the established cytosol location. An exclusive cytosolic location and absence of a mitochondrial pool are not claimed. The source evidence hydrates Cytoplasm from GO:0005739, which denotes mitochondrion; that mismatch is retained as a provenance issue and is not treated as biological validation.

Evidence:

- [file:NEUCR/NCU06005/NCU06005-uniprot.txt](NCU06005-uniprot.txt): “DR   InterPro; IPR005999; Glycerol_kin.”
- [PMID:6284716](https://pubmed.ncbi.nlm.nih.gov/6284716/): “Evidence from the enzymatic characterization of these
mutants indicated that glp-2 and glp-4 were the structural genes encoding the
mitochondrial glycerol-3-phosphate dehydrogenase and cytosolic glycerokinase,
respectively.”
- [file:NEUCR/NCU06005/NCU06005-bioinformatics/RESULTS-rereview.md](NCU06005-bioinformatics/RESULTS-rereview.md): “NCU06005 is therefore the sole glycerol kinase gene in the reference proteome.”

COR denotes a biologically supported location newly specified relative to the frozen target annotation snapshot. LSP denotes a less precise location than an established target annotation. Neither category establishes model training-set membership.
