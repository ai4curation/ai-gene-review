#!/usr/bin/env python
"""Warm the reference cache (publications/) so `just validate-all` stops
re-fetching references on every run.

`linkml-reference-validator` fetches each referenced PMID/DOI and caches it under
publications/ as a side effect of validation. When a cached entry has no full text
yet, the validator re-fetches it every run, which made the full validate-all
reference phase network-bound (~59 min). Running the validator once over the whole
corpus with full-text fetching on (the validator's default) populates the cache so
subsequent runs are cache-bound. Normal validation trusts committed entries;
this explicit warming command opts into retrying and refreshing existing entries.

This processes the corpus in chunks for progress/resumability and ignores
validation pass/fail — the goal here is only to populate the cache. References are
read from the structured YAML fields (not a regex over prose), so no malformed
cache filenames are produced. Raw fetched PDFs land in publications/files/, which
is gitignored; the extracted text is written into each per-reference .md.

Run from the repo root: `just warm-references` (or `uv run python
scripts/warm_reference_cache.py`).
"""

import glob
import subprocess
import sys
import time
from tempfile import NamedTemporaryFile

import yaml

SCHEMA = "src/ai_gene_review/schema/gene_review.yaml"
CONFIG = "conf/reference_validator_config.yaml"
CHUNK = 100


def main() -> int:
    files = sorted(glob.glob("genes/*/*/*-ai-review.yaml"))
    if not files:
        print("no gene-review files found; run from the repo root", file=sys.stderr)
        return 1

    print(f"warming reference cache for {len(files)} gene files (chunks of {CHUNK})", flush=True)
    t0 = time.time()
    # Validation trusts reviewed cache entries; this explicit warming command
    # must still retry cached abstracts and refresh legacy extraction formats.
    with open(CONFIG) as source:
        config = yaml.safe_load(source)
    config["trust_cached_entries"] = False
    with NamedTemporaryFile(mode="w", suffix=".yaml") as config_file:
        yaml.safe_dump(config, config_file)
        config_file.flush()
        for i in range(0, len(files), CHUNK):
            batch = files[i : i + CHUNK]
            # check=False: validation failures (snippet mismatches, flaky fetches) are
            # expected and irrelevant here; we only want the references fetched into the cache.
            subprocess.run(
                [
                    "uv", "run", "python", "-m",
                    "ai_gene_review.validation.reference_cli", "validate", "data", *batch,
                    "--schema", SCHEMA, "--target-class", "GeneReview", "--config", config_file.name,
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False,
            )
            done = i + len(batch)
            elapsed = time.time() - t0
            eta = elapsed / done * (len(files) - done)
            print(f"  warmed {done}/{len(files)}  elapsed={elapsed / 60:.1f}m  eta={eta / 60:.1f}m", flush=True)

    print(f"reference cache warm complete in {(time.time() - t0) / 60:.1f}m", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
