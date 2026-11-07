# Bounded follow-up to PR #6100 review 5812414716

Implemented C1 and C2, plus S3 and the evidence-scope clarification in S5. `response-ledger.md` adjudicates every current suggestion without mechanically changing historical codes, source defects, family scope or proposal lifecycle.

The five edited curated/note files are ECOLI CheW review/notes, BACSU CheY review/notes, and the chemotaxis module. Three matching histories were scaffolded through `just new-history` with actor `codex`. Original bytes/parsed documents and source hashes were captured before any edit.

Lightweight checks pass: 33 ordered annotation payloads, actions and structured replacements are exact; no NEW row is present in these two reviews and none was added. No supporting quotation was added or altered. Notes are append-only, 89 captured raw/provider/publication and historical audit inputs are byte-identical, and the module's parsed changes are confined to top-level notes and three role descriptions. Its selectors, term IDs, required activities, exemplars and circuit logic are unchanged. File-scoped Ruff passes.

The preserved 65-case result is historical evidence for its recorded model and context, not a fresh execution on these wording edits. No source acquisition, heavy validation, render, staging, commit or push was performed. Root still needs focused validation of both genes and the module, validation of three helper histories, and current renders. Root may decide whether to rerun capacity even though all non-prose module fields are exact.

Reproduce the lightweight check with `.venv/bin/python -B analysis/module_audits/bacterial_chemotaxis_signal_transduction/review-5812414716-followup/check_preservation.py`. It writes only this new directory's `preservation.json`; it never rewrites old audit receipts or source files.
