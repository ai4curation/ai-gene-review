# BioReason-Pro Web Export Converter

Script: `~/.openclaw/workspace/scripts/bioreason_to_yaml.py`

## Usage

```bash
source .venv/bin/activate
python ~/.openclaw/workspace/scripts/bioreason_to_yaml.py --model rl [--dry-run] [--overwrite]
```

## What it does

1. Reads `*-deep-research-bioreason.md` from `~/worktrees/agr-bioreason/genes/`
2. Parses GO terms from the `### GO Terms` section (raw GO-GPT output)
3. Filters to leaf terms via OAK IS_A ancestor removal (~65% reduction)
4. Writes PredictionReview-conformant YAML with `source_method: GO-GPT`
5. References the raw md via `source_documents` field

## Options

| Flag | Description |
|------|-------------|
| `--model rl\|sft` | BioReason-Pro model version (default: rl) |
| `--dry-run` | Print stats without writing |
| `--overwrite` | Replace existing files |
| `--no-leaf-filter` | Skip OAK ancestor filtering |
| `--output-dir DIR` | Custom output directory |

## Output

`{GENE}-bioreason-{rl|sft}-predictions.yaml` in the gene directory.

## Note

These YAMLs contain GO-GPT predictions (the input to reasoning), not BioReason-Pro's post-reasoning GO terms. They are useful for bulk comparison but lower-value than the reasoning traces themselves.
