# PR6199 additive capacity and complete reference closure

This supplement supersedes no historical receipt. The original capacity artifacts and the accepted 53-path scientific correction seal remain unchanged. Current science is identified by `current-science-seal.json`; its two quote-only successors are explained and reversibly verified below.

The existing independently specified biological oracle needs no altered expectations. `check_capacity.py` imports the historical checker and reruns its 59 cases, nine graph mutations, eight sensitivity controls and three real counterexample proteins. All case diagnostics, assignments, routes, mutation detections and sensitivity outcomes are identical to the previous results. The production graph still has ten atoms and four formal routes. The explicit cluster-binding proposal and module cofactor metadata do not imply native cluster occupancy, and the donor cores retain desulfurase activity without unqualified native U34-process assertions. The oracle already uses activity and assay-context requirements rather than requiring those process annotations.

`check_closure.py` checks the complete contents of all 19 member reviews, eight family reviews and the module, including reference-list entries without quotations. It resolves 135 distinct explicit local/PMID reference edges, verifies 189 distinct literal quotations after whitespace normalization, and incorporates every one of the accepted 41 source dependencies. The expanded source set contains 196 files including immutable acquisition artifacts and baseline raw records. These are a preservation inventory, not a claim that every acquisition artifact is primary biological evidence. External URLs and database identifiers are not downloaded or represented as locally cached sources.

All 162 original machine rows and all four historical NEW rows are preserved in order. The only authored addition is THET2 MnmA GO:0051539, IDA, supported by exact HB27 recombinant/reconstituted protein measurements. The resulting total is 167 rows, including five active NEW rows. Historical consultation manifests are checked with an explicit list of accepted science successors; a mismatched path outside that list fails. The old status-only module receipt remains historical and is not misrepresented as describing the substantive current revision.

## Production quotation correction

The integrating agent's focused production validation detected that the literal figure suffix `[c]` in the long U34A-control quote was treated as an editorial insertion. The lightweight literal-substring checks had not detected that normalization issue. At the integrating agent's request, eight gene quotation objects and one module quotation were shortened to the exact source substring `A tRNALys U34A mutant was not a MnmA substrate`. No source, action, biological assertion or seeded field changed.

`quote-supersession.json` records both hashes and the exact text replacement. `accepted_seal.py` restores the old quote in memory and reconstructs the exact predecessor bytes, proving that the two successor files differ only in the specified quotation. The original 53-path hash receipts are preserved. Two new helper-generated codex histories validate; `quote-history-checks.json` records them. The single requested `just validate THET2 mnmA` run passes, with terminal output in `THET2-mnmA-validation.log`. No unchanged gene was revalidated in this supplement. Literal quote closure is distinct from the production validation recorded here.

## Reproduction and limits

Run the checkers into temporary outputs; do not overwrite frozen receipts:

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python analysis/module_audits/bacterial_mnma_trna_thiolation/review-round1-capacity/check_capacity.py > /tmp/mnma-round1-capacity.json
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python analysis/module_audits/bacterial_mnma_trna_thiolation/review-round1-capacity/check_closure.py > /tmp/mnma-round1-closure.json
```

Repeated runs produce byte-identical results, recorded in `determinism.json`. The capacity result remains evidence-qualified capacity, not measured native flux, universal donor substitution or physiological Tus dispensability. Compiler limitations and the independent biological expectations remain as described in the historical capacity README. This supplement performs no downloads, rendering, full-corpus validation, staging, commits or shared-project edits. Root integration owns the remaining validation and publication steps.
