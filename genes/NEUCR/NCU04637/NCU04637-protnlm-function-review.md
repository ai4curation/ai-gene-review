# NCU04637: ProtNLM2 function review

Source method: ProtNLM2. Source version: live API snapshot 2026-09-09T03:00:51.831347+00:00. Accession: Q7S3B9. Raw source: [NCU04637-protnlm-source.json](NCU04637-protnlm-source.json).

## Exact emitted paragraph

> Required presynaptically at the neuromuscular junction. Implicated in synaptic vesicle endocytosis

## Atomic claims

| Exact claim span | Assessment | Rationale |
|---|---|---|
| Required presynaptically | NPI (0) | Presynaptic function requires a nervous-system context absent in Neurospora. |
| at the neuromuscular junction | NPI (0) | The fungus has no neuromuscular junction. This literal anatomical context is incompatible with the target taxon. |
| Implicated in synaptic vesicle endocytosis | NPI (0) | Endocytosis is conserved, but synaptic vesicles specify neuronal trafficking and are not fungal endocytic vesicles. |

All literal atoms carry TAXON_CONSTRAINT_VIOLATION. The broader, separately assessed proposition “participates in endocytosis” is CNN (2): current PAINT supports it and characterized fungal Rvs proteins substantiate the transfer. It is not an additional emitted prediction and is excluded from the atomic claim count.

## Evidence and provenance

The 467-residue target contains BAR residues 17–269 and SH3 residues 407–467, and PANTHER assigns PTHR47174:SF1, “REDUCED VIABILITY UPON STARVATION PROTEIN 167.” [PMID:20610658](https://pubmed.ncbi.nlm.nih.gov/20610658/) explicitly distinguishes Rvs167’s BAR-plus-SH3 architecture from Rvs161, which consists solely of BAR, and demonstrates fungal Rvs complex membrane binding/tubulation. [PMID:35976707](https://pubmed.ncbi.nlm.nih.gov/35976707/) studies Rvs-dependent endocytic scission. These findings justify fungal endocytosis, not neuronal anatomy.

The paragraph donor Q8I1C0 is Drosophila pseudoobscura Endophilin-A, whose own text is transferred by similarity from Q8T390. The source phmmer score 39.2 does not justify transferring the fly’s anatomical context. The donor chain is preserved in [NCU04637-donor-Q8I1C0.json](NCU04637-donor-Q8I1C0.json).

## Complete paragraph evidence object

```json
{
  "commentType": "FUNCTION",
  "texts": [
    {
      "evidences": [
        {
          "evidenceCode": "ECO:0008006",
          "id": "ProtNLM2",
          "properties": [
            {
              "key": "model_score",
              "value": "0.39"
            },
            {
              "key": "phmmer_accession",
              "value": "Q8I1C0"
            },
            {
              "key": "phmmer_score",
              "value": "39.2"
            }
          ],
          "source": "Google"
        }
      ],
      "value": "Required presynaptically at the neuromuscular junction. Implicated in synaptic vesicle endocytosis"
    }
  ]
}
```
