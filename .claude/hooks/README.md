# Claude Code Hooks

This directory contains hooks that integrate with Claude Code to provide automated validation and other features.

## validate_ai_review_hook.py

This hook automatically validates any `-ai-review.yaml` files when they are written or edited using Claude Code.

### Features
- Automatically runs validation when saving ai-review.yaml files
- Blocks file modifications if validation fails
- Shows detailed validation output in the Claude Code interface
- Filters out noise from warning messages for cleaner output

### How it works
1. Intercepts Write, Edit, and MultiEdit operations on files ending with `-ai-review.yaml`
2. Runs the validation command: `uv run ai-gene-review validate <file>`
3. Displays validation results
4. Returns exit code 2 to block the operation if validation fails

### Testing
Run the test script to verify the hook is working:
```bash
python3 .claude/hooks/test_validation_hook.py
```

## validate_rule_review_hook.py

This hook automatically validates rule review YAML files (`*-review.yaml` in the `rules/` directory) when they are written or edited.

### Features
- Automatically runs validation when saving rule review files
- Blocks file modifications if validation fails (exit code 2)
- Shows detailed validation output including enum errors
- Distinguishes between gene reviews and rule reviews by path

### How it works
1. Intercepts Write, Edit, and MultiEdit operations on files ending with `-review.yaml` in the `rules/` directory
2. Runs the validation command: `uv run ai-gene-review rules-validate <file>`
3. Displays validation results
4. Returns exit code 2 to block the operation if validation fails

### What it validates
- Schema compliance (RuleReview LinkML class)
- Valid enum values for assessment fields:
  - `parsimony`: PARSIMONIOUS, ACCEPTABLE, REDUNDANT, OVERLY_COMPLEX
  - `literature_support`: STRONG, MODERATE, WEAK, NONE, CONTRADICTED
  - `condition_overlap`: NONE, MINOR, SIGNIFICANT, COMPLETE
  - `go_specificity`: TOO_BROAD, APPROPRIATE, TOO_NARROW, MISMATCHED
  - `taxonomic_scope`: TOO_BROAD, APPROPRIATE, TOO_NARROW, MISSING, UNNECESSARY
- Supporting text substring validation against referenced documents

## protect_files_hook.py

The `protect_files_hook.py` prevents modifications to certain protected paths including:
- publications/
- genes/ directories (except ai-review.yaml files)
- deep-research.md files
- goa.tsv files
- .uniprot.txt files