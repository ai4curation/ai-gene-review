# Additive six-atom Gallate coverage successor

This successor consumes the current intracellular module and the unchanged curated reaction-evidence table. The original `modules/bacterial_gallate_catabolism-source-analysis/check_coverage.py`, `coverage-evidence.yaml`, `coverage-results.yaml` and scientific handoff remain byte-identical. No prior result is relabeled as a test of the new module.

`check_coverage.py` uses the production `compile_module`, `iter_atoms` and `is_satisfied` APIs. It retains all 23 original catalytic case expectations. The original `galp_outer_membrane_porin / Q88JX6` case becomes `GalP retained as porin comparator`, which verifies the existing reviewed porin core without putting it back into the reaction circuit. The successor has 38 cases total.

Additional controls establish that GalP alone cannot complete chemistry, cannot replace any omitted Pseudomonas catalyst, and does not change otherwise complete catalytic coverage. Each catalyst in the synthetic sphingomonad panel is also omitted separately. Mutation controls expose false capacity when reaction gating is disabled for the shared isomerase family or when terminal aldol cleavage is deleted. A separate mutation forces GalP into the required model, incorrectly rejecting the complete catalytic panel until the porin is supplied; its positive control isolates that modeling error.

Family membership and manually reviewed reaction IDs are separate predicates. The actual compiler still does not enforce chemical substrate/product descriptors. The test therefore retains the original explicit reaction gate, checks descriptor consistency, and deliberately demonstrates the false positives produced when that gate is removed. This is not proof of native flux, whole-cell uptake, or same-strain pathway completeness. KA1/SYK-6 remains a synthetic chemical panel; the unresolved BURL3 hydratase and partial SYK-6 panel remain incomplete without claiming biological absence.

`run_checks.py` records the exact sequential commands, statuses, UTC times, free-space measurements and per-command logs. It runs the successor, seven `just validate ORGANISM GENE` commands, focused module schema validation and the one-file module semantic validator. Environment overrides are `PYTHONDONTWRITEBYTECODE=1` and `UV_NO_SYNC=1`. The recorded run cannot be restarted by rerunning this script. It stops on a failed command, an ENOSPC marker or insufficient pre-command headroom. The coverage checker itself is read-only and can be reproduced independently:

```
.venv/bin/python -B analysis/module_audits/bacterial_gallate_catabolism/review-20261107/coverage-successor/check_coverage.py
```

The scientific handoff and all of its current outputs/dependencies are hash-checked before and after this sequence, alongside the original checker/results/evidence. No full corpus validation, member-index refresh, rendering, source refresh, staging, commit or remote publication is part of this successor.

Warnings are reported in the final manifest, not silenced by fabricated source quotations or NEW rows. In particular, the C7570 process-core coverage advisory is an expected consequence of leaving its unresolved secondary-metabolism row undecided; the three BURL3 notes explicitly justify not manufacturing a process annotation.
