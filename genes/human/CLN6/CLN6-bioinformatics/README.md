# Reproduce the CLN6 comparator snapshot comparison

This small analysis compares literal QuickGO CC search results, the original saved responses and repository GOA TSV files. It does not classify biological correctness, alter annotations or explain database differences. The code takes URLs, record IDs and paths from `config.yaml`; these are inputs, not conclusions encoded in the script.

Use Python 3.11 or later and PyYAML 6.0.2 (`uv run --project .` resolves the declared dependency). From this directory, run:

```sh
just live
just replay
just pagination
```

Alternatively, without just:

```sh
uv run --project . python check_quickgo.py --config config.yaml --repo-root ../../../.. --output rerun-live
uv run --project . python check_quickgo.py --config config.yaml --repo-root ../../../.. --observations results/manifest.yaml --output rerun-replay
uv run --project . python check_quickgo.py --config config.yaml --repo-root ../../../.. --query lman2 --page-size 5 --output rerun-pagination
```

The script refuses to overwrite an output directory. Every live page is saved before parsing, with URL, HTTP status, headers, UTC observation times, bytes and SHA256 in a YAML receipt. Pagination checks every advertised page, consistent total counts, unique record IDs and the final hit count. Failure produces an INCONCLUSIVE report and a nonzero exit; retained partial pages are not called complete. A changing API during pagination can therefore prevent a completeness claim. The TSV comparison selects the exact gene product and cellular-component aspect. It compares the nine shared fields listed in each report. TSVs do not carry QuickGO record IDs, and their WITH/FROM flattening is deliberately excluded. Missing local TSVs are reported as unavailable rather than as absent annotations.

`results/report.yaml` records the main comparison; `pagination-control/report.yaml` records the distinct LMAN2-only, four-page query. Both folders contain complete raw downloads and manifests. `snapshots/` contains the unaltered original downloads and their original receipts; these are not manually reconstructed JSON. The live response and saved snapshot may legitimately differ on a future date. Neither a shared total count nor an annotation date identifies why files differ. WB, IDA and reference identifiers are reported only as API fields, not validated curator assignments or primary biological evidence.

Source endpoints and observation dates are in the manifests and receipts. The [QuickGO annotation service](https://www.ebi.ac.uk/QuickGO/services/annotation/search) is the source of downloaded records; repository paths and hashes identify the independently compared TSVs. See [RESULTS.md](RESULTS.md) for the actual observed outcome and its limits.
