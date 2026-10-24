# NCU06005: ProtNLM function-paragraph review

Accession: Q7S2F2; source method: ProtNLM2; source version: live API snapshot 2026-09-09T03:00:51.831347+00:00.

Complete source: [NCU06005-protnlm-source.json](NCU06005-protnlm-source.json).

## Original paragraph

> Key enzyme in the regulation of glycerol uptake and metabolism. Catalyzes the phosphorylation of glycerol to yield sn-glycerol 3-phosphate

Original evidence:

```json
[
  {
    "evidenceCode": "ECO:0008006",
    "id": "ProtNLM2",
    "properties": [
      {
        "key": "model_score",
        "value": "0.92"
      },
      {
        "key": "tmalign_accession",
        "value": "P9WPK0"
      },
      {
        "key": "tmalign_score_chain_1",
        "value": "0.84709"
      },
      {
        "key": "tmalign_score_chain_2",
        "value": "0.95438"
      }
    ],
    "source": "Google"
  }
]
```

## Atomic assessments

| Exact claim fragment | Assessment | Biological rationale |
|---|---|---|
| Key enzyme in the regulation of glycerol uptake | UNC | Glycerol phosphorylation can trap glycerol metabolically, but target uptake-control, flux-control, or regulatory assays were not recovered. A glycerol-kinase-family assignment alone does not establish a key regulatory role in uptake. |
| and metabolism | CNN | The specific glycerol-kinase family and classical N. crassa glycerol-dissimilation experiments support a central biochemical entry step in glycerol metabolism. This is a catalytic pathway role, not transport across a membrane. |
| Catalyzes the phosphorylation of glycerol to yield sn-glycerol 3-phosphate | CNN | IPR005999 and the glycerol-kinase subfamily distinguish the target from other FGGY kinases; characterized fungal glycerokinase chemistry grounds transfer of the established reaction. A purified NCU06005 assay was not recovered. |

## Evidence and synthesis

- [file:NEUCR/NCU06005/NCU06005-uniprot.txt](NCU06005-uniprot.txt): “DR   InterPro; IPR005999; Glycerol_kin.”
- [PMID:6284716](https://pubmed.ncbi.nlm.nih.gov/6284716/): “Evidence from the enzymatic characterization of these
mutants indicated that glp-2 and glp-4 were the structural genes encoding the
mitochondrial glycerol-3-phosphate dehydrogenase and cytosolic glycerokinase,
respectively.”

The reaction and glycerol-metabolism role are supported as conserved biology. The stronger phrase about regulation of uptake remains uncertain. The source donor P9WPK0 is a mycobacterial glycerol kinase; its structural similarity supports the fold but does not establish fungal uptake regulation or cellular location. No training-membership claim follows from known biological agreement.
