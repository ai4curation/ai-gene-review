# NCU04637: ProtNLM2 location review

Source method: ProtNLM2. Source version: live API snapshot 2026-09-09T03:00:51.831347+00:00. Accession: Q7S3B9. Raw source: [NCU04637-protnlm-source.json](NCU04637-protnlm-source.json).

## Exact location claims

- Original identifier: `SL-0086`. Original text: **Cytoplasm**.

Assessment: **LSP (2)**. The Rvs167 subfamily and BAR/SH3 architecture support a cytoplasmic adaptor acting at cortical actin patches, as established for fungal Rvs proteins (PMID:20610658; PMID:35976707). That more precise location is already in GOA. The source hydrates Cytoplasm from GO:0031097 (medial cortex); exact medial distribution remains unresolved in this fungus but is unnecessary for the broad cytoplasmic inference. This SL claim is distinct from the separately emitted GO:0005737 record.

## Inspected evidence

- file:NEUCR/NCU04637/NCU04637-uniprot.txt: “DR   PANTHER; PTHR47174:SF1; REDUCED VIABILITY UPON STARVATION PROTEIN 167; 1.”
- PMID:20610658: “We show that the purified Rvs161-Rvs167 complex binds to liposomes in a curvature-independent manner and promotes tubule formation in vitro.”
- PMID:20610658: “Rvs161 consists solely of a BAR domain, whereas Rvs167 is composed of a BAR domain followed by a region rich in glycine, proline, and alanine (GPA), and an SH3 (Src-homology 3) domain at its C-terminus”

## Complete location evidence objects

```json
{
  "commentType": "SUBCELLULAR LOCATION",
  "subcellularLocations": [
    {
      "location": {
        "evidences": [
          {
            "evidenceCode": "ECO:0008006",
            "id": "ProtNLM2",
            "properties": [
              {
                "key": "model_score",
                "value": "0.99"
              },
              {
                "key": "string_match_text",
                "value": "GO:0031097"
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
        ],
        "id": "SL-0086",
        "value": "Cytoplasm"
      }
    }
  ]
}
```
