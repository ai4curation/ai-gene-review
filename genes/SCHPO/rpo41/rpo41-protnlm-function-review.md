# rpo41: ProtNLM2 function-description review

Source: **pre-release `post-processed-2026_02_28k.xml`**, accession `O13993`. The exact entry is preserved in [rpo41-protnlm-source.xml](rpo41-protnlm-source.xml); all original evidence elements and model scores are retained in [rpo41-protnlm-source.json](rpo41-protnlm-source.json). This record is currently Swiss-Prot and is absent from the published 26,856-record TrEMBL pilot list. The current public ProtNLM endpoint returns this record; API availability is distinct from membership in the published pilot list. No training-membership inference is made.

## Original paragraph 1

> DNA-dependent RNA polymerase catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates.

Original evidence key(s): `2`.

| Atomic claim | Assessment | Evidence and limit |
|---|---|---|
| DNA-dependent RNA synthesis | CNN | Purified fission-yeast Rpo41 transcribes DNA templates. The target is the catalytic single-subunit mitochondrial polymerase, unlike an accessory Pol I subunit. |
| Use of the four ribonucleoside triphosphates | CNN | The reconstituted transcription reaction uses ATP, CTP, GTP and UTP. This is established polymerase chemistry, not a new function. |

## Primary evidence

- [PMID:21357609](https://pubmed.ncbi.nlm.nih.gov/21357609/) (cached as `publications/PMID_21357609.md`).

Family and feature provenance: [rpo41-uniprot.txt](rpo41-uniprot.txt).

Decisive excerpt, PMID:21357609: “We show biochemically, that purified Mtf1 and Rpo41 together can bind to the S. pombe mitochondrial promoters and can support transcription from the S. pombe mitochondrial promoters in vitro.”
