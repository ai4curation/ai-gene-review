# HBB source checks

These standard database/table lookups retain the protein-specific observations
behind urinary-exosome and granule localization, and the HBB abundance row from
the MDS platelet study. They do not infer a function from a table hit. The gene
review separately evaluates what each experiment supports.

Run with Python 3's standard library; no environment or package installation is
needed. Use a fresh output directory to preserve the committed evidence:

```sh
python verify_sources.py --gene HBB --refseq NP_000509 --uniprot P68871 \
  --platelet-protein HBB_HUMAN --tertiary-entity R-HSA-6800191 \
  --ficolin-entity R-HSA-6801015 --output-dir /path/to/new-output
```

The script retrieves the primary NIH table, official Reactome entity JSON and
PMC's primary article table. It verifies requested identities, checks a second
NIH row through the same selector, and emits only selected records plus URL,
timestamp, response hashes and normalized-record hashes. No full source page or
API payload is retained. Changing upstream HTML may change the response hash
without changing the extracted evidence. A failed request or identity check is
reported as inconclusive with a nonzero exit status; expected results are never
used as substitutes. `checks.json` and `RESULTS.md` are generated outputs.
