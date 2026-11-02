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

No localization experiment exists for NCU06296 or for any member of its PANTHER subfamily (PTHR23023:SF292, a Pezizomycotina clade in which every member is uncharacterised). The donor P49109 is mammalian FMO5, a co-ortholog of the whole fungal clade at speciation distance, and the phmmer score of 37.5 is modest. Mammalian FMOs reach the ER membrane through a hydrophobic C-terminal anchor; Q7SAD4 has no predicted anchor of that type, and its C-terminus is charged, so the mammalian mechanism of ER-membrane association does not transfer. Q7SAD4 is the only product of the gene and spans the full FMO-like domain, so this is not a truncation relative to a canonical product. Yeast FMO1, which sits peripherally on the cytoplasmic face of the ER (PMID:10077572), belongs to a different PANTHER family (PTHR43539) and does not ground transfer either. The absence of an anchor does not exclude peripheral ER association, so the claim is neither supported nor refuted.

Evidence:

- [file:NEUCR/NCU06296/NCU06296-uniprot.txt](NCU06296-uniprot.txt): “DR   InterPro; IPR020946; Flavin_mOase-like.”
- [file:NEUCR/NCU06296/NCU06296-bioinformatics/RESULTS.md](NCU06296-bioinformatics/RESULTS.md): “No member of SF292 or of the fungal clade has experimental GO annotation; every leaf in the
  Fungi node is an uncharacterised genome-project entry.”
- [file:NEUCR/NCU06296/NCU06296-bioinformatics/RESULTS.md](NCU06296-bioinformatics/RESULTS.md): “No 19-residue Kyte-Doolittle window reaches 1.6 in Q7SAD4 (mammalian FMO3 has a C-terminal
  membrane anchor that does reach this threshold); the Q7SAD4 C-terminus is charged.”
- [file:NEUCR/NCU06296/NCU06296-bioinformatics/RESULTS.md](NCU06296-bioinformatics/RESULTS.md): “Yeast FMO1 (P38866, the yFMO of PMID:10077572) is classified by PANTHER 19 in a different
  family, PTHR43539:SF78”
- [PMID:10077572](https://pubmed.ncbi.nlm.nih.gov/10077572/): “The flavin-containing monooxygenase from yeast (yFMO) catalyzes the O2- and NADPH-dependent oxidations of biological thiols, including oxidation of glutathione to glutathione disulfide (GSSG).”
- [PMID:10077572](https://pubmed.ncbi.nlm.nih.gov/10077572/): “Here we show that yFMO is localized to the cytoplasmic side of the ER membrane.”

COR denotes a biologically supported location newly specified relative to the frozen target annotation snapshot. LSP denotes a less precise location than an established target annotation. Neither category establishes model training-set membership.
