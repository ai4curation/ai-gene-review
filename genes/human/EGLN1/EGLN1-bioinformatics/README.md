# EGLN1 reproducible evidence

Use Python 3.10 or later with the dependency in requirements.txt. The database archive is bundled; the approximately 21 MB original PDZ supplement is **not bundled**.

```bash
python -m pip install -r requirements.txt
python fetch_supplement.py /tmp/egln1-pdz-supplement.zip
python replay.py --pdz-supplement /tmp/egln1-pdz-supplement.zip --check
```

A previously downloaded supplement can be supplied directly. Its exact SHA256 and size, workbook member/hash, source URL and sheet are recorded in input-manifest.json. The source was genuinely acquired and verified before this analysis; live availability is not promised. Missing or changed inputs produce explicit errors. The downloader does not overwrite existing files or accept changed content.

The parser verifies the bundled archive and every member before reading in memory. It reconstructs natural products, PAINT target ancestry/IBDs/MSA columns, exact source-specific IntAct joins, deposited target sequence and metal identity, donor records and Reactome paths. It then independently selects every Q9GZT9 row from the original workbook and joins PDZ domain names to official human gene names/synonyms and numbered features. Source assertions are configuration inputs; curation decisions are not outputs or hardcoded results. --output writes recomputed JSON; --check compares the complete result to results.json.

Binding intensity is thresholded at 0.05. A censored pKd does not prove nonbinding; a positive on one domain does not make another domain positive. The three imported positive partners each have one DAPF measurement and estimated affinity, without independent row-level FP measurements. Exact IntAct features retain their original participant side. Database identity is not experimental insert sequencing, model membership is not a new experiment, and conserved residues do not establish every tissue response.

The archive contains original public database responses, including the failed/empty ARBA query as access provenance, not primary article bodies. input-manifest.json records acquisition URLs when available and checksums for the captured versions. [RESULTS.md](RESULTS.md) and [the source guide](../EGLN1-source-evidence.yaml) describe interpretation and limits.
