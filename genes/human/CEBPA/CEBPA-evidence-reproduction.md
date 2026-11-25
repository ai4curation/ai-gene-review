# Reproducing the CEBPA source extract

This file documents extraction of published table cells and database record fields. It is not a sequence analysis or a function-prediction pipeline. `CEBPA-source-evidence.json` remains the durable, directly inspectable output used by the review.

Install Python 3.10+, `uv`, and Poppler's `pdftotext`. From this gene directory:

```sh
uv run CEBPA-extract-source-evidence.py \
  --seed CEBPA-ai-review.yaml \
  --manifest CEBPA-evidence-inputs.json \
  --inputs ./primary-inputs --fetch-inputs \
  --output ./reproduced-evidence.json
```

The script declares PyYAML through PEP723 metadata. It downloads the real public URLs listed in the input manifest, checks every SHA256 against the reviewed snapshot, and derives the two text files using `pdftotext -layout`. It never manufactures a missing supplement. If retrieval fails or a mutable database response has changed, it stops with the exact input name and hash discrepancy. A reader who already has the verified files may supply them in `--inputs` and omit `--fetch-inputs`.

The manifest records the original URLs, hashes, sizes and available retrieval dates. IntAct, ComplexPortal and QuickGO endpoints are live services: continued availability of the historical bytes is not guaranteed. A failure to retrieve those bytes does not invalidate the literal extracted records, but it prevents claiming a fresh byte-identical reproduction. The reviewed target measurements remain readable in the output, with source IDs, methods, source scopes and public record URLs.

The seed contributes immutable source fields, not review judgments. Rows are selected and joined by term ID, reference ID and exact supporting entities, with a digest of the complete source object to distinguish otherwise similar events. The output and assertion hash do not depend on annotation-list order. Unknown bZIP accessions, malformed partner lists, missing table headers and hash mismatches fail explicitly. No source action is changed by this script.

The 2010 supplement contains background-corrected fluorescence measurements. The 2012 thesis supplies separately identified affinity values; these are not relabeled as the unrecovered 2013 supplemental table. Database links are source-linked curation, not independent replication. The computed MD5 is retained as a digest rather than a precomputed true/false verdict.

A fresh empty-directory retrieval on 2026-10-10 downloaded all 14 manifest inputs, verified their SHA256 hashes, derived the two PDF text files and reproduced the committed JSON byte for byte. The local regression checks also reverse the annotation order without changing the output and confirm that an unknown partner fails explicitly. These checks establish the recorded run; they do not promise that live database snapshots will remain unchanged.
