# PR6193 current publication/source closure

This additive closure retains the 339-input published capacity closure, the original 375-file publication manifest, all released handoff manifests and their files, the frozen raw/provider/publication preservation pool, all old capacity receipts, and every local/PMID reference found recursively in the nine current gene reviews, two family reviews and module. It does not overwrite or relabel any earlier proof as current.

`input-map.json` records each current scientific input hash and its origins. `supersession-chain.json` records explicit version edges: the already-published three-file ManX follow-up and the current nine STRMU review/notes/render files. The current publication manifest deviates scientifically only at those nine STRMU paths. Historical expected hashes remain in the original receipts and in the new edge map; no input was silently dropped to obtain a passing closure.

Four shared project/inventory/render paths differ between the original full-run science manifest and published PR head38d5cbd2. `project-metadata-provenance.json` proves this is pre-existing publication metadata, not a new scientific edit. These four paths remain represented in the historical union but are deliberately excluded from the immutable scientific map. Root's later metadata closeout must have its own frozen receipt.

The broad preservation pool includes pre-existing publication caches not cited by this module. Inclusion verifies their immutability; it does not claim they are biological evidence or instruct staging unrelated files. The release manifest lists only this new closure's artifacts. `required-ignored-source-paths.json` identifies the separately acquired evidence dependencies retained from the earlier audit. Their original paths/hashes and literature ledger provenance remain authoritative; full acquired articles remain ignored, while scoped excerpts are already in the released consultations.

The current 60 cases, 13 model mutations and nine sensitivities are rerun using the unchanged published checker with outputs redirected here. Case outputs, mutation witnesses, sensitivity witnesses, compiled atoms and the documented bare-boolean false positives must equal both the old published result and the current gene-follow-up result. This preserves the actual prior expectations and their limits, including the need for a source-aware same-candidate role/domain oracle.

Ordered source payloads for all nine reviews remain exact: 93 rows, two historical NEW rows, both active, no additions or retirements. The three STRMU reviews retain their reviewed action changes; those changes do not affect their core transporter contributions. Every current supporting quotation is verified against its resolved source. The original full run passed at its recorded earlier head; no current full-corpus result is claimed here.

## Reproducible source and closure check

Run from `/Users/cjm/orca/workspaces/ai-gene-review/aigr-mannose-pts-taxon-audit`:

```sh
uv run python analysis/module_audits/bacterial_mannose_pts/review-followup/final-closure/check_closure.py
uv run ruff check analysis/module_audits/bacterial_mannose_pts/review-followup/final-closure/check_closure.py
```

The checker never invokes the old closure's main function or writes old capacity outputs. It imports reusable quote/capacity functions, redirects new capacity outputs here, and refuses to overwrite a changed frozen input map. Original closure path: `analysis/module_audits/bacterial_mannose_pts/capacity-consultation/inputs.json`. Original full-run proof: `analysis/module_audits/bacterial_mannose_pts/full-validation-proof.json`; old full log: `.cache/module-audit-logs/mannose-20261107/validate-all.log`. The old `.cache/module-audit-logs/mannose-20261107/run-full.py` is a historical mutator and must not be rerun for this follow-up.

## Root publication/full-validation preparation

After root verifies and commits the current science/metadata, record that exact head and a new publication manifest. Use a fresh log directory, leaving the original full run untouched. The actual repository-wide command is:

```sh
mkdir -p .cache/module-audit-logs/mannose-20261107/round1-full
just validate-all > .cache/module-audit-logs/mannose-20261107/round1-full/validate-all.log 2>&1
```

Root must record the actual exit status, terminal counts, log SHA256 and committed input manifest after this command finishes. This consultation does not execute it. The source checker and focused validation proof are readiness evidence, not a substitute for that terminal result.
