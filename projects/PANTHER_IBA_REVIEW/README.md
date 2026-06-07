# PANTHER IBA family review

Family-level (PANTHER/PAINT) review of the IBA annotations on the 40 reviewed
S. pombe genes. Reviews the *source* of the IBAs — the phylogenetic
propagation — rather than re-judging gene by gene.

- `extract_iba_propagation.py` — reproducible extractor: for each IBA, resolves
  the ancestral PANTHER node, the seed genes, and the subfamilies of our gene
  and its seeds (from the cached `interpro/panther/<FAM>/` tables); flags
  cross-subfamily and localization propagations and joins our curation action.
- `iba_propagation.tsv` — the resulting per-IBA table (regenerate with the script).
- `REVIEW.md` — the written review and findings.

Regenerate:

```bash
uv run python projects/PANTHER_IBA_REVIEW/extract_iba_propagation.py
```

Scope: the 151 IBAs in the 40 reviewed genes (38 PANTHER families, all cached
locally). Note the cross-subfamily flag is deliberately sensitive and
over-fires on broadly conserved functions — it is triage, not a verdict.
