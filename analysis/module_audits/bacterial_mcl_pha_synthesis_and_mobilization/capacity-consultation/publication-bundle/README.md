# Durable cache-input bundle

This additive bundle makes all **56 `.cache/` inputs (8,550,156 bytes)** in the original capacity `input-closure.json` available as ordinary repository files. Every `sources/*.source` file is a byte-identical copy, including genuine source texts, acquisition metadata, failed-access responses and validation logs. The suffix prevents cache/log/render ignore rules from concealing the files. `mapping.json` records the original cache path, durable publication path, byte count and SHA256 for each input.

The original capacity handoff, its eleven files, all earlier manifests and their recorded paths are unchanged. This bundle does not redefine access scope: failed publisher responses remain failed responses; abstract-only publications do not become full texts. It also does not relocate the historical original-worktree paths described by the preflight provenance receipt.

Before running the original capacity checkers in a checkout, restore the recorded cache paths:

```sh
python3 analysis/module_audits/bacterial_mcl_pha_synthesis_and_mobilization/capacity-consultation/publication-bundle/bootstrap.py
uv run python analysis/module_audits/bacterial_mcl_pha_synthesis_and_mobilization/capacity-consultation/check_capacity.py
uv run python analysis/module_audits/bacterial_mcl_pha_synthesis_and_mobilization/capacity-consultation/check_closure.py
```

The standard-library bootstrap first checks every bundled source and all existing destinations. It restores only missing files, leaves byte-identical files unchanged, and refuses any mismatched existing file or symlink. It never fetches the network. `--root PATH` selects an isolated destination; `--verify-only` verifies an already restored checkout without writes. Repository dependencies and the non-cache inputs in the original closure, including the rendered module, must also be present.

`test_bootstrap.py` restores all files in a temporary directory, checks every byte hash, repeats the operation to prove idempotence, and exercises mismatch and symlink refusal without partial writes. It also verifies that all eleven original release hashes and the original handoff hash remain exact. `verification.json` records these results. The local worktree cache is verified without modification.

All six included logs were inspected: they contain public publication-fetch status, validation output and existing local filesystem provenance, without authentication credentials. A scan of all 56 inputs found no private keys, bearer credentials, OpenAI/GitHub tokens or AWS access keys. One broad assignment-pattern flag in public Springer HTML was checked by parsing the metadata URL: its `api_key` query parameter is empty. Publisher challenge-page fields are retained as public failed-response provenance, not represented as user credentials or successful article access. `secret-inspection.json` records the bounded inspection; no source bytes were redacted or changed.

The additive handoff lists bundle files only. The parent publication manifest can exclude the ignored original cache paths and include these durable files and their mapping; the original local closure continues verifying the restored cache hashes.
