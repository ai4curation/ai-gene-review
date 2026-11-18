# Additive PSEPK MesD-like zinc correction

Only `existing_annotations[1].review.action` in PSEPK/metE changes, from `KEEP_AS_NON_CORE` to `ACCEPT`. The unchanged evidence and reason identify zinc coordination as a conserved catalytic feature. Native occupancy remains unmeasured; inference scope is preserved and is not expressed as peripheral function.

The review's original SHA256 was `3d0b630decf83f4c4f5b27e113914a54d2facc83504d4437cc3c54c0a68e2e08`. `check_preservation.py` both compares the complete parsed document against that exact one-field change and reverses the single action token to recover the original byte hash. All source payloads, row order, qualifiers, proposal lifecycle, references, evidence and core functions remain exact. Notes are append-only; HTML is regenerated; the new history was scaffolded with `just new-history` and validated.

`supersession.json` names the immutable original PSEPK handoff and its hash, and maps exactly three old/new hashes: review, notes and render. Every other prior handoff file (71) and all 37 protected sources remain unchanged. The old handoff is neither rewritten nor relabeled as current. A final closure should apply this explicit overlay when verifying the old manifest and then verify the additive handoff itself.

Focused validation, history validation, rendering, preservation and Ruff pass. Two existing advisories remain: supporting annotations do not quote available provider reports, and the core methionine-biosynthesis context has no additional process annotation. No scientific assertion is added merely to silence either advisory. No other gene, family, module, project, raw source or prior history was edited; no full-corpus run, commit or push was performed.
