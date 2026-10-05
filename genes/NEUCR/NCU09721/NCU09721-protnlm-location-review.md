# NCU09721: ProtNLM localization review

Accession: Q7S2Q5; original locus: NCU09721. Source method: ProtNLM2. Source version: live API snapshot 2026-09-09T03:00:51.831347+00:00.

The complete prediction record is preserved in [NCU09721-protnlm-source.json](NCU09721-protnlm-source.json); claim metadata are also preserved in [NCU09721-protnlm-provenance.json](NCU09721-protnlm-provenance.json). Original UniProt SL identifiers are retained; these are not substituted with GO terms.

## Claim 1: SL-0088

Original text: **Cytoplasmic vesicle**

Original evidence:

```json
[
  {
    "evidenceCode": "ECO:0008006",
    "id": "ProtNLM2",
    "properties": [
      {
        "key": "model_score",
        "value": "0.51"
      },
      {
        "key": "phmmer_accession",
        "value": "O35643"
      },
      {
        "key": "phmmer_score",
        "value": "797.0"
      }
    ],
    "source": "Google"
  }
]
```

Assessment: **COR** (confidence score 2).

Curated AP1 membership places this beta-adaptin in the Golgi/endosomal cargo-adaptor machinery. Aspergillus AP1 is experimentally involved in sorting secretory vesicles and recycling endosomes (PMID:29925567), grounding conserved recruitment to cytoplasmic carriers. This broad location is supported by AP1 family transfer; no particular N. crassa vesicle cargo or native imaging experiment is asserted.

The frozen target annotations specify AP1 membership, TGN, and membrane coat, but not this carrier-membrane location. COR records the supported added localization relative to that target snapshot.

Evidence:

- [file:NEUCR/NCU09721/NCU09721-uniprot.txt](NCU09721-uniprot.txt): “DR   InterPro; IPR026739; AP_beta.”
- [PMID:36836259](https://pubmed.ncbi.nlm.nih.gov/36836259/): “FgAP1β interacts with FgAP1σ, FgAP1γ, and FgAP1μ”
- [PMID:29925567](https://pubmed.ncbi.nlm.nih.gov/29925567/): “its role in clathrin-dependent maintenance of polar traffic of
specific membrane cargoes toward the apex of growing hyphae. We provide evidence
that AP-1 is involved in both anterograde sorting of RabERab11-labeled SVs and
RabA/BRab5-dependent endosome recycling.”
## Claim 2: SL-0134

Original text: **Golgi apparatus membrane**

Original evidence:

```json
[
  {
    "evidenceCode": "ECO:0008006",
    "id": "ProtNLM2",
    "properties": [
      {
        "key": "model_score",
        "value": "0.31"
      },
      {
        "key": "phmmer_accession",
        "value": "Q22498"
      },
      {
        "key": "phmmer_score",
        "value": "48.3"
      }
    ],
    "source": "Google"
  }
]
```

Assessment: **LSP** (confidence score 2).

Fusarium graminearum AP1 beta-GFP colocalizes with the Golgi marker FgKex2-mCherry (PMID:36836259). The target AP1 IBA, supported beta-adaptin architecture, and conservation within filamentous fungi ground peripheral Golgi-membrane recruitment. The existing target trans-Golgi-network annotation is more precise than Golgi apparatus membrane, making this LSP. ProtNLM donor Q22498 is a worm coatomer gamma subunit, so that donor alone would not establish beta-adaptin localization; the independent AP1 experiment supports the emitted location.

Evidence:

- [file:NEUCR/NCU09721/NCU09721-uniprot.txt](NCU09721-uniprot.txt): “DR   InterPro; IPR026739; AP_beta.”
- [PMID:36836259](https://pubmed.ncbi.nlm.nih.gov/36836259/): “FgAP1β interacts with FgAP1σ, FgAP1γ, and FgAP1μ”
- [PMID:36836259](https://pubmed.ncbi.nlm.nih.gov/36836259/): “FgAP1β-GFP, FgAP1γ-GFP, and FgAP1μ-GFP also localize to the Golgi apparatus.”
## Claim 3: SL-0071

Original text: **Clathrin-coated vesicle membrane**

Original evidence:

```json
[
  {
    "evidenceCode": "ECO:0008006",
    "id": "ProtNLM2",
    "properties": [
      {
        "key": "model_score",
        "value": "0.52"
      },
      {
        "key": "phmmer_accession",
        "value": "O35643"
      },
      {
        "key": "phmmer_score",
        "value": "797.0"
      }
    ],
    "source": "Google"
  }
]
```

Assessment: **COR** (confidence score 2).

Aspergillus AP1 supports clathrin-dependent secretory and recycling traffic (PMID:29925567), providing independent fungal experimental support for conserved clathrin-coated-carrier association of the target AP1 complex. Loss of the canonical beta appendage does not refute this complex location: fungal AP1 remains associated with clathrin and can use alternative tail motifs. The location concerns peripheral coat association, not membrane insertion or proof of direct NCU09721-clathrin binding.

The frozen target annotations specify AP1 membership, TGN, and membrane coat, but not this carrier-membrane location. COR records the supported added localization relative to that target snapshot.

Evidence:

- [PMID:29925567](https://pubmed.ncbi.nlm.nih.gov/29925567/): “its role in clathrin-dependent maintenance of polar traffic of
specific membrane cargoes toward the apex of growing hyphae. We provide evidence
that AP-1 is involved in both anterograde sorting of RabERab11-labeled SVs and
RabA/BRab5-dependent endosome recycling.”

COR denotes a biologically supported location newly specified relative to the frozen target annotation snapshot. LSP denotes a less precise location than an established target annotation. Neither category establishes model training-set membership.
