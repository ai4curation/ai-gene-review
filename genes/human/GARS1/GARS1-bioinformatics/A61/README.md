# Reproduce the historical A61 comparison

This self-contained, offline comparison uses three unmodified official records. It tests a historical mouse clone against one current mouse Gars1 transcript. It does not identify the protein purified in PMID:8939962 or assign a new human GARS1 function. See [RESULTS.md](RESULTS.md) for the findings and limits.

Use Python with **Biopython 1.85** already installed. No download or package installation occurs in these scripts. From this directory:

```sh
mkdir -p replay
python map_exact.py inputs/U64446.1.gb inputs/NM_180678.3.gb replay/mapping.json
python fit_query_v2.py inputs/U64446.1.gb inputs/NM_180678.3.gb replay/fitting-v2.json
python map_exact.py inputs/NM_180678.3.gb inputs/NM_180678.3.gb replay/positive-control.json
python verify_literals.py inputs/U64446.1.gb inputs/NM_180678.3.gb inputs/Q9CZD3.json replay/fitting-v2.json replay/literal-replay-v2.json
```

The checked outputs are in [results](results/). With the pinned Biopython version and these exact commands, the four JSON outputs are byte-identical to the corresponding checked outputs. A different dependency version may change alignment ordering; compare all optimal alignments rather than assuming a new biological difference.

The fitting parameters are explicit command-line options: match +2, substitution -3, gap opening -7 and gap extension -1, with free transcript flanks and every query base included. Both orientations are tested; up to 16 reverse optima are enumerated. Source accessions, translations, exact blocks, differences and coordinate conventions are retained in the computed outputs. The scripts make no network requests.
