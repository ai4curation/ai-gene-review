# NCU06296: ProtNLM localization review

Accession: Q7SAD4; original locus: NCU06296. Source method: ProtNLM2. Source version: live API snapshot 2026-09-09T03:00:51.831347+00:00.

The complete prediction record is preserved in [NCU06296-protnlm-source.json](NCU06296-protnlm-source.json); claim metadata are also preserved in [NCU06296-protnlm-provenance.json](NCU06296-protnlm-provenance.json). Original UniProt SL identifiers are retained; these are not substituted with GO terms.

## Claim 1: SL-0097

Original text: **Endoplasmic reticulum membrane**

Original evidence:

```json
[
  {
    "evidenceCode": "ECO:0008006",
    "id": "ProtNLM2",
    "properties": [
      {
        "key": "model_score",
        "value": "0.72"
      },
      {
        "key": "phmmer_accession",
        "value": "P49109"
      },
      {
        "key": "phmmer_score",
        "value": "37.5"
      }
    ],
    "source": "Google"
  }
]
```

Assessment: **UNC** (confidence score 1).

ER association is biologically plausible: characterized yeast FMO localizes to the cytoplasmic face of the ER (PMID:10077572), as do several mammalian FMOs. However, the target is resolved only as a broad FMO-like protein, and the donor P49109 is mammalian FMO5 with a modest phmmer score of 37.5. No supported target subfamily/targeting feature or localization experiment establishes transfer of that compartment. The absence of an annotated transmembrane helix does not refute peripheral ER association; exact localization remains unresolved.

Evidence:

- [file:NEUCR/NCU06296/NCU06296-uniprot.txt](NCU06296-uniprot.txt): “DR   InterPro; IPR020946; Flavin_mOase-like.”
- [PMID:10077572](https://pubmed.ncbi.nlm.nih.gov/10077572/): “The flavin-containing monooxygenase from yeast (yFMO) catalyzes the O2- and NADPH-dependent oxidations of biological thiols, including oxidation of glutathione to glutathione disulfide (GSSG).”
- [PMID:10077572](https://pubmed.ncbi.nlm.nih.gov/10077572/): “Here we show that yFMO is localized to the cytoplasmic side of the ER membrane.”

COR denotes a biologically supported location newly specified relative to the frozen target annotation snapshot. LSP denotes a less precise location than an established target annotation. Neither category establishes model training-set membership.
