# rfc3: ProtNLM2 function-description review

Source: **pre-release `post-processed-2026_02_28k.xml`**, accession `O14003`. The exact entry is preserved in [rfc3-protnlm-source.xml](rfc3-protnlm-source.xml); all original evidence elements and model scores are retained in [rfc3-protnlm-source.json](rfc3-protnlm-source.json). This record is currently Swiss-Prot and is absent from the published 26,856-record TrEMBL pilot list. The current public ProtNLM endpoint returns this record; API availability is distinct from membership in the published pilot list. No training-membership inference is made.

## Original paragraph 1

> May be involved in DNA replication and thus regulate cell proliferation.

Original evidence key(s): `2`.

| Atomic claim | Assessment | Evidence and limit |
|---|---|---|
| Participation in DNA replication | CNN | Target rfc3-1 mutants show DNA-replication defects (PMID:10588638), and RFC supports processive Pol delta synthesis (PMID:10748208). The cautious phrase “May be” understates the established process role. |
| Consequent regulation of cell proliferation | CNN | The same target study establishes an essential growth role and defects in replication and damage checkpoints. Interpreted as coupling proliferation to successful genome replication, the statement is supported; it does not identify Rfc3 as an independent mitogenic signaling factor. |

## Primary evidence

- [PMID:10588638](https://pubmed.ncbi.nlm.nih.gov/10588638/) (cached as `publications/PMID_10588638.md`).
- [PMID:10748208](https://pubmed.ncbi.nlm.nih.gov/10748208/) (cached as `publications/PMID_10748208.md`).
- [PMID:16040599](https://pubmed.ncbi.nlm.nih.gov/16040599/) (cached as `publications/PMID_16040599.md`).

Family and feature provenance: [rfc3-uniprot.txt](rfc3-uniprot.txt).
