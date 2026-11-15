# Durable LPS source packaging

`replacement-map.json` is an additive resolution layer for the nine tracked cache dependencies named in `index-removal-paths.txt`. All original local files remain unchanged. No earlier consultation, cache, publication, checker or receipt is rewritten.

Five replacements preserve every byte: the ENA H44/76 genome record and four compressed PANTHER tree projections. The tree files are the repository's compact projection of the official `treeinfo` response, not untouched HTTP bodies. Existing acquisition and transformation provenance remains the authority for their origin. The current checker reparses the genome and the actual copied trees.

Four article files are replaced by bounded excerpts and explicit provenance. These support the checked literature-ledger quotations; the existing Neisseria primary-evidence file additionally preserves the previously curated assay excerpts. Complete original article hashes, URL, title, access record and replacement scope are retained. **Excerpts cannot reconstruct the full articles.** Earlier full-text judgments beyond these excerpts remain historical source attestations, not fully repeatable reading from the packaged excerpts. No full review is newly redistributed here.

The actual consulted texts show FEMS reserved rights (2015), an exclusive Microbiological Society of Korea licence (2024), CC BY-NC-ND 4.0 (Nature 2026), and ASBMB copyright (2011). These differing terms were not treated as blanket full-text republication permission. The [ENA/INSDC policy](https://ena-browser-docs.readthedocs.io/en/latest/about/policies.html), checked 2026-11-07, allows redistribution/use of public data without licensing fees or restrictions. An explicit standalone PANTHER data licence was not verified: the official downloads request returned HTTP403. Public tree attribution and exact provenance are retained; no CC licence is invented from a database paper's licence.

Run from the repository root:

```sh
uv run python analysis/module_audits/bacterial_lps_transport/review-followup/source-packaging/verify.py
```

Optional custody check while the original files are still local:

```sh
uv run python analysis/module_audits/bacterial_lps_transport/review-followup/source-packaging/verify.py --originals
```

`prepare.py` documents the one-time capture; it refuses to overwrite any output and is not a routine rerun command. `verify.py` is read-only. Only the parent integration owner may remove the nine original paths from Git's index, after checking this map. Index removal must leave the local source files intact. No index operation was performed by this consultation.

The 2015 boundary-data JSON preserves the selected factual Table 2 entries used for the family controls. It is an attributed manual data transcription, with original-text token checks and explicit interpretation limits. The final replacement map adds this bounded transcription to the initial one-time capture; routine verification uses the frozen map rather than rerunning `prepare.py`.
