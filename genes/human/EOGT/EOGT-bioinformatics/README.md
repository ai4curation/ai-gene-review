# EOGT product reconstruction

This standard-library analysis reconstructs natural alternative products from official UniProt alternative-sequence features, compares every residue with independently retrieved UniProt FASTA, and compares the translation of the experimentally used KC347596.1 clone with those products. Feature projection describes retained sequence; it does not establish protein expression, stability, localization, or activity.

Run `just replay` in this directory, or use Python directly:

```sh
python3 reconstruct_products.py --uniprot inputs/UniProt-Q5NDL2.json --fasta inputs/Q5NDL2-isoforms.fasta --clone-embl inputs/KC347596.1.embl --output products.json
```

Tested with Python 3.12.9, with no third-party dependencies. The script accepts input/output paths and contains no gene-specific coordinates, expected product lengths, or biological verdicts. The same script reconstructed all six natural ENTPD1 products against an independent official FASTA as a second real-input check. That unrelated input is not required to replay EOGT.

The captured inputs are reproducible snapshots from 2026-10-24:

- [UniProt Q5NDL2 JSON](https://rest.uniprot.org/uniprotkb/Q5NDL2.json)
- [UniProt Q5NDL2 and alternative-product FASTA](https://rest.uniprot.org/uniprotkb/stream?query=accession:Q5NDL2&format=fasta&includeIsoform=true)
- [ENA KC347596.1 EMBL record](https://www.ebi.ac.uk/ena/browser/api/embl/KC347596.1?download=false)

`input-manifest.json` records the original snapshot and script/result hashes. Network access is unnecessary for replay; new downloads may reflect later database changes.
