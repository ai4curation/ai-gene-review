# ADPRH bioinformatics

Two committed, self-testing scripts. Both fail loudly on a missing input and name the
command that regenerates it; neither degrades silently.

```bash
uv sync
uv run python catalytic_residue_census.py              # regenerates RESULTS.md + results.json
uv run python catalytic_residue_census.py --self-test
uv run python audit_adprh_review.py                    # invariant checks on the review YAML
uv run python audit_adprh_review.py --self-test
```

## `catalytic_residue_census.py`

Asks whether the annotation route that gives ADPRH `GO:0003875` discriminates on the
residues that actually carry catalysis. It aligns every reviewed Swiss-Prot member of
PANTHER `PTHR16222` to human ADPRH and scores the five positions whose single
substitutions UniProt records as "Complete loss of activity" (S54, D55, D56, D302, S305),
then cross-tabulates against who holds `GO:0003875` in GOA.

Outputs `RESULTS.md` and `results.json`. A fresh run reproduces both byte-identically, so
a hand-edit to the report would be reverted rather than silently kept.

Scope caveat printed in the report itself: the 31 members analysed are the **reviewed
(Swiss-Prot) subset**, 0.104% of the family's 29,860 proteins. No statement here is about
the family as a whole.

Headline: the ADPRH clade retains 5/5 residues and holds the term 5/5; the ADPRHL1 clade
has lost D56 and S305 in **all seven** orthologues and holds the term **7/7** by IEA. The
ADPRS/ARH3 clade holds it 0/7, which is correct and is the negative control showing the
route does discriminate at subfamily level.

The identity-threshold approach was tried and rejected in favour of clade consistency plus
substitution chemistry; the rejection and its reason are recorded in the generated report
rather than only in the code, because a reader of `RESULTS.md` needs to know which method
produced the numbers.

## `audit_adprh_review.py`

Nine invariant checks (A–I) on `../ADPRH-ai-review.yaml` that no repo validator performs:
duplicate YAML keys via a strict loader, anchors/aliases, raw-vs-parsed quote
reconciliation, GOA row reconciliation, the logical-opposite citation cross-product,
summary-opener-vs-action agreement, `core_functions` agreement in both directions,
"a COMPLETE review contains no PENDING rows", and "every row's `supporting_text` set must
mention that row's own term".

The letters are not maintained by hand: `--self-test` asserts that the checks enumerated in
the module docstring are exactly the checks the code implements, crediting the parse-time
check A only after demonstrating that the strict loader really rejects a duplicate key. That
assertion exists because this count drifted onto three prose surfaces at once when check I
was added.

Two of its checks were found not to fire by break-testing rather than by reading, and one
(H) was added only after running the audit against the un-reviewed `fetch-gene` stub, which
it had otherwise almost entirely cleared. A passing self-test proves the guards that were
thought of fire; it says nothing about the guard that was never written.
