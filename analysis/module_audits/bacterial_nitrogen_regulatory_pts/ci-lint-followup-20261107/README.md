# CI lint follow-up

The test-suite job 128446560831 on commit 50adec523337490be91a5ef99ae0f1844aaba66e failed on 39 Ruff findings in three audit helpers. This successor formats those helpers, splits grouped imports, and removes one unused csv import. It does not change curation or evidence. Original helper bytes are preserved as .py.txt files, and all prior manifests remain unchanged.

Run this directory’s check.py to verify the successor chain and all 1,209 recorded hash entries. Both PSEPK read-only audits pass after formatting; their new outputs are retained here. Ruff passes across the materialized checkout. Full remote validation is still pending and must be associated with the exact new commit.
