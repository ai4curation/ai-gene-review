# NCU04937: ProtNLM2 location review

Source method: ProtNLM2. Source version: live API snapshot 2026-09-09T03:00:51.831347+00:00. Accession: Q7S3T0. Raw source: [NCU04937-protnlm-source.json](NCU04937-protnlm-source.json).

## Exact location claims

- Original identifier: `SL-0191`. Original text: **Nucleus**.

Assessment: **UNC (1)**. No target localization experiment, reliable nuclear-targeting feature or supported nuclear family placement was identified. The current sequence is only 114 residues and largely glutamine-rich. Its donor Q96EK4 is human THAP11, a 314-residue transcription factor; the recorded phmmer score 29.1 supplies no alignment showing conservation of its functional DNA-binding region. Neither a predicted coiled coil nor small size establishes nuclear enrichment. The nuclear claim is plausible but not validated or refuted. Donor record: [NCU04937-donor-Q96EK4.json](NCU04937-donor-Q96EK4.json).

## Inspected evidence

- file:NEUCR/NCU04937/NCU04937-uniprot.txt: “FT   COILED          52..104”

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
                "value": "0.91"
              },
              {
                "key": "phmmer_accession",
                "value": "Q96EK4"
              },
              {
                "key": "phmmer_score",
                "value": "29.1"
              }
            ],
            "source": "Google"
          }
        ],
        "id": "SL-0191",
        "value": "Nucleus"
      }
    }
  ]
}
```
