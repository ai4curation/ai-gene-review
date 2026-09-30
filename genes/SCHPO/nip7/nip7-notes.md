# nip7 (Q1MTQ9) — evidence and prediction assessment

Nip7 is an RNA-binding ribosome-biogenesis factor with pre-PUA and PUA domains. It associates with nascent 60S ribosomal subunits in the nucleolus and supports assembly of the large-subunit preribosome. The fission-yeast protein is present in structurally characterized early pre-60S particles; it is an assembly factor rather than a constitutive structural protein of the mature ribosome.

## Evidence and family boundary

The [2022 primary paper](https://pubmed.ncbi.nlm.nih.gov/36423630/) focuses on Fkbp39/nucleophosmin but reports multiple fission-yeast pre-60S particles. The [RCSB8ESQ metadata](https://www.rcsb.org/structure/8ESQ) explicitly identifies Q1MTQ9 as entity43, author chainl; the downloaded [entity response](nip7-8ESQ-entities.json) preserves the identity mapping. This directly supports the target’s occurrence in an early large-subunit precursor even though the article prose does not prominently name Nip7.

The PUA/pre-PUA architecture supports an RNA-binding assembly factor. It neither confers an RNA-cleavage or methyltransferase reaction nor turns Nip7 into a mature ribosomal constituent. PANTHER PTHR23415 has a mixed CKS/Nip7 name; that broad label is not evidence for kinase regulation by this protein. Falcon misses the target structural deposit and HDA nucleolar/cytosolic annotation and consequently understates the direct target evidence.

## External ProtNLM statements

[Exact retained output](nip7-protnlm-source.json). These are name/location claims, not emitted GO/EC predictions. CNN denotes overlap with existing supported annotation; it does not establish literal membership in the training set.

| Claim type | Verbatim output | Assessment | Evidence and interpretation |
|---|---|---|---|
| name | 60S ribosome subunit biogenesis protein NIP7 | CNN | The exact Q1MTQ9 protein is author chain l/entity43 in deposited pre-60S structure8ESQ linked to PMID:36423630. The name accurately identifies an assembly factor, not a mature ribosomal structural constituent. |

## Source quotations

## Research provenance

The genuine [Falcon report](nip7-deep-research-falcon.md) is retained with its provider metadata and artifact. Its conclusions were checked against the target record, exact accession and primary sources described above. Scientific uncertainties are recorded as UNC/UNDECIDED findings rather than a request for another reviewer to perform this assessment.
