# ADGB bioinformatics

Two reproducible scripts supporting `genes/human/ADGB/ADGB-ai-review.yaml`.

## `adgb_sites.py` — does each domain retain the residues its GO term needs?

Androglobin is chimeric, and GOA gives it four InterPro-derived IEA rows, two per
domain. This asks, from sequence alone, whether either domain still has the residues
that would justify its terms.

```bash
uv run python adgb_sites.py --self-test                      # guards, both directions
uv run python adgb_sites.py --json results.json --results-md RESULTS.md
```

`RESULTS.md` is written entirely by the script from the same objects that print the
console tables, so its prose cannot drift from its numbers. Verify with:

```bash
uv run python adgb_sites.py --results-md /tmp/x && diff /tmp/x RESULTS.md
```

Answer, in brief: the calpain domain keeps the nucleophile cysteine (C132) but has lost
the general-base histidine and the asparagine, and MEROPS independently classifies ADGB
as a non-peptidase homologue; the globin domain keeps the proximal heme histidine
(H824) but has a glutamine (Q792), not a histidine, at the distal position.

## `audit_adgb_review.py` — invariants no repo validator checks

```bash
uv run python audit_adgb_review.py --self-test   # 6 mutations + happy direction
uv run python audit_adgb_review.py
```

Catches three defect classes that `just validate` and `checkquotes.py` are structurally
blind to, because both walk the *parsed* document:

- duplicate YAML mapping keys, which PyYAML resolves by silently discarding the earlier
  value — data deleted before any quote gate runs;
- `supporting_entities` / `propagation_review.source_entities` drifting from the GOA
  WITH/FROM column, which is checked by deriving them from the TSV rather than by eye;
- annotation-count reconciliation against *distinct* GOA rows, and the presence of a
  `propagation_review` on every REMOVE/MARK_AS_OVER_ANNOTATED of an IBA/ISS/IEA row.

Both scripts fail loudly on missing or changed inputs (a dead UniProt accession, a
shifted GOA column layout) rather than degrading to an empty result that reads as a
finding.
