# rpa49: ProtNLM2 function-description review

Source: **pre-release `post-processed-2026_02_28k.xml`**, accession `O14086`. The exact entry is preserved in [rpa49-protnlm-source.xml](rpa49-protnlm-source.xml); all original evidence elements and model scores are retained in [rpa49-protnlm-source.json](rpa49-protnlm-source.json). This record is currently Swiss-Prot and is absent from the published 26,856-record TrEMBL pilot list. The current public ProtNLM endpoint returns this record; API availability is distinct from membership in the published pilot list. No training-membership inference is made.

## Original paragraph 1

> DNA-dependent RNA polymerase catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates.

Original evidence key(s): `1`.

| Atomic claim | Assessment | Evidence and limit |
|---|---|---|
| The associated DNA-dependent RNA polymerase transcribes DNA using ribonucleoside triphosphates | CNN at holoenzyme level | The grammatical subject is DNA-dependent RNA polymerase, and Rpa49 is an experimentally established Pol I subunit. The chemistry describes that associated enzyme. The paragraph omits Rpa49’s informative role in maximizing rDNA transcription. |
| Independent Rpa49 polymerase activity | Not asserted; would be incorrect | Rpa49/RPA51 is an accessory A49-family subunit: Pol I lacking it retains nonspecific transcription. No intrinsic RNA-polymerase catalytic center or isolated-subunit synthesis is established. The GO process/complex predictions remain valid because participation in transcription does not require independent catalysis. |

## Primary evidence

- [PMID:12893961](https://pubmed.ncbi.nlm.nih.gov/12893961/) (cached as `publications/PMID_12893961.md`).

Family and feature provenance: [rpa49-uniprot.txt](rpa49-uniprot.txt).
