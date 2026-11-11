# DYNC2I1 saved-source evidence audit

This portable analysis reconstructs database joins used in the DYNC2I1 review. It does not generate annotation verdicts. Python 3.9 or later is the only dependency; no third-party package, network, credentials or repository checkout is needed.

```sh
python3 replay.py --check
python3 replay.py --output /tmp/DYNC2I1-results.json
python3 replay.py --paint-target Q8C761 --output /tmp/mouse-paint.json
```

`just check` is an optional wrapper for the first command. `--check` reads all inputs and compares the recomputed result with `results.json`; it does not rewrite files. The alternate target exercises the same generic tree/alignment/sequence join on the independently saved mouse record. It is a parser check, not a separate gene review.

`source-manifest.json` lists every ZIP member, its original URL, exact SHA-256 and size. `source-inputs.zip` contains unaltered database responses, the complete reused official IBD GAF, and the 56 inherited source dictionaries exported without their review fields. The latter is explicitly marked as a derived selector, linked to the source commit. The archive has deterministic member order, timestamps and modes. The saved IBD header records its release; reused downloads are not represented as freshly captured. Live URLs may now return different bytes, so the content hashes identify the actual evidence boundary.

The script computes the target tree path and official-sequence match; joins literal IBD rows to the inherited IBA nodes and terms; selects source-specific IntAct records and reconstructs participant ROGIDs; preserves the direction and all incident target edges in the original NDEx AP-MS network; follows saved Reactome component edges to the target; and evaluates typed `is_a`/`part_of` ancestry. Results include source line numbers and full matched records. IntAct physical lines are one-based. Annotation indexes are zero-based indexes in the inherited 56-row review. NDEx identifiers are graph identifiers, not line numbers.

The raw source inventory is intentionally broader than the selected records: it permits checking selection and unmatched contexts. Missing matches are not negative experiments. AP-MS, coimmunoprecipitation and LUMIER observations do not by themselves establish purified binary interfaces or physiological mechanisms. A sequence checksum match does not establish every post-translational feature or historical reagent lot. Reactome pathways are models, not additional independent human imaging experiments. No paper body or supplementary PDF is republished in this bundle.

See [RESULTS.md](RESULTS.md) for the actual executed outputs and biological limits, and [the source guide](../../DYNC2I1-source-guide.md) for the primary literature.
