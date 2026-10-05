# mek-1: ProtNLM2 location review

Source method: ProtNLM2. Source version: live API snapshot 2026-09-09T03:00:51.831347+00:00. Accession: Q7RYZ6. Raw source: [mek-1-protnlm-source.json](mek-1-protnlm-source.json).

## Exact location claims

- Original identifier: `SL-0086`. Original text: **Cytoplasm**.

Assessment: **LSP (2)**. Cytoplasm is supported by the fungal MAPKK context and current ortholog-derived GOA, and direct target microscopy provides a more precise prior localization: MEK-1-GFP accumulates at contact sites of fusing Neurospora germlings (PMID:41071819, Figure 7B). Thus the broad compartment prediction loses known spatial detail. This is not evidence that MEK-1 is uniformly cytosolic, or that it resides at division septa. The emitted evidence is an exact sanitized match to GO:0005737, preserved below.

## Inspected evidence

- PMID:18849472: “The MAK-1 MAPK was not phosphorylated in Δ mik-1 and Δ mek-1 mutants, consistent with the involvement of MIK-1, MEK-1, and MAK-1 in the same signaling cascade.”
- PMID:41071819: “In a first step, we confirmed the accumulation of the kinase MAK-1 at the contact sites and showed the same localization pattern for both its upstream kinases (Fig 7).”

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
                "value": "GO:0005737"
              },
              {
                "key": "string_match_location",
                "value": "GO"
              },
              {
                "key": "string_match_type",
                "value": "exact_sanitized"
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
