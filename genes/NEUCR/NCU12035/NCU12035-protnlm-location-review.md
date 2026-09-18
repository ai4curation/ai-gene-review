# NCU12035: ProtNLM localization review

Accession: V5ILC0; original locus: NCU12035. Source method: ProtNLM2. Source version: live API snapshot 2026-09-09T03:00:51.831347+00:00.

The complete prediction record is preserved in [NCU12035-protnlm-source.json](NCU12035-protnlm-source.json); claim metadata are also preserved in [NCU12035-protnlm-provenance.json](NCU12035-protnlm-provenance.json). Original UniProt SL identifiers are retained; these are not substituted with GO terms.

## Claim 1: SL-0191

Original text: **Nucleus**

Original evidence:

```json
[
  {
    "evidenceCode": "ECO:0008006",
    "id": "ProtNLM2",
    "properties": [
      {
        "key": "model_score",
        "value": "0.06"
      },
      {
        "key": "tmalign_accession",
        "value": "P61599"
      },
      {
        "key": "tmalign_score_chain_1",
        "value": "0.58824"
      },
      {
        "key": "tmalign_score_chain_2",
        "value": "0.74341"
      }
    ],
    "source": "Google"
  }
]
```

Assessment: **UNC** (confidence score 1).

The source structural donor P61599 is human NAA20, the NatB catalytic subunit, while NCU12035 is assigned only to the generic GNAT domain. GNAT enzymes modify diverse proteins and small molecules, and a shared fold does not establish NAA20 orthology or nuclear recruitment (PMID:33362253). No target localization assay or supported nuclear-targeting/subfamily evidence was recovered. Nuclear residence is therefore neither validated nor refuted; the low source model score is recorded but is not itself the biological rationale.

Evidence:

- [file:NEUCR/NCU12035/NCU12035-uniprot.txt](NCU12035-uniprot.txt): “DR   InterPro; IPR000182; GNAT_dom.”
- [PMID:33362253](https://pubmed.ncbi.nlm.nih.gov/33362253/): “GNAT enzymes transfer an acyl moiety from acyl coenzyme A to a
wide range of substrates including aminoglycosides, serotonin,
glucosamine-6-phosphate, protein N-termini and lysine residues of histones and
other proteins.”

COR denotes a biologically supported location newly specified relative to the frozen target annotation snapshot. LSP denotes a less precise location than an established target annotation. Neither category establishes model training-set membership.
