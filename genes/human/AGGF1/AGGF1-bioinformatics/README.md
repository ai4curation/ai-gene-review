# AGGF1 bioinformatics

Reproducible analyses supporting the human AGGF1 (Q8N302) GO review. Everything
is fetched live from UniProt, QuickGO, IntAct and NCBI E-utilities; responses are
cached under `cache/` (gitignored, disposable — delete it and every number is
re-derived).

```bash
uv run python resolve_withfrom.py    # resolve every GOA WITH/FROM token + donor evidence
uv run python gap_by_reference.py    # QuickGO by reference; G-patch MF reference class
uv run python intact_partners.py     # IntAct paginated; per-partner independent experiments
uv run python domain_residues.py     # FHA + G-patch residue conservation -> domain_residues.json
uv run python retraction_check.py    # retraction / erratum / expression-of-concern
uv run python check_terms.py         # QuickGO obsoletion + secondaryIds for every term used
uv run python reconcile_goa.py       # GOA rows <-> existing_annotations, asserted
uv run python term_choice_checks.py  # the two MODIFY targets vs GO's own usage
uv run python lab_independence.py    # how many groups produced this literature
uv run python audit_claims.py        # the reported numbers match what the scripts produce
uv run python audit_claims.py --self-test
```

Findings are written up in `RESULTS.md`. `audit_claims.py` is the guard that keeps
`RESULTS.md`, `AGGF1-notes.md` and `AGGF1-ai-review.yaml` from drifting away from
`domain_residues.json` and from each other; its `--self-test` mutates each claim
in turn and requires a guard to fire. A passing self-test shows the guards that
were written work — it cannot show which guard was never written.

Two design notes worth keeping:

- `domain_residues.py` aligns **domain windows**, never full-length sequences. An
  earlier version globally aligned 714-aa AGGF1 to 543-aa CHEK2 and mapped every
  FHA anchor into AGGF1 residues 112–169, producing a clean-looking
  "0/8, the FHA is degenerate" result that was pure alignment noise.
- Every anchor transfer requires **both** residue identity **and** that the aligned
  position land inside the target's own annotated domain. Identity alone
  manufactures conserved sites out of alignment noise.
