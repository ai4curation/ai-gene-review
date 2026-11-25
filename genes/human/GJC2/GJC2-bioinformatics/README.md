# GJC2 deposited-sequence comparison

Run from this directory with Python 3; no packages or network calls are needed:

```sh
python3 compare_constructs.py > results.json
```

The script parses the annotated CDS translations in the two unmodified NCBI records and the sequence section in `../GJC2-uniprot.txt`. It reports their lengths and hashes, the exact interval matching AY285161.1 in the current sequence, differences between the two historical translations, and the mapping of historical residue 33. Values are computed from the inputs rather than supplied as expected results.

Inputs were retrieved on 2026-11-05:

- [AY285161.1](https://www.ncbi.nlm.nih.gov/nuccore/AY285161.1), protein AAP37488.1: `inputs/AY285161.1.gb`.
- [AF014643.1](https://www.ncbi.nlm.nih.gov/nuccore/AF014643.1), protein AAB94511.1: `inputs/AF014643.1.gb`.
- [UniProt Q5T442](https://www.uniprot.org/uniprotkb/Q5T442/entry): the adjacent cached UniProt record. The generated report fingerprints its actual bytes.

The deposited sequences do not establish the sequence of an experimental plasmid that was not published, endogenous translation initiation, or another natural isoform. This analysis does not reconstruct the historical mouse construct. Its reported length and unresolved equivalence remain source limitations in the manual evidence page.
