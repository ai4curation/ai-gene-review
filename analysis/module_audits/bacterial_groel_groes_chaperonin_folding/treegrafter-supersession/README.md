# PR6164 TreeGrafter audit supersession

The CI run reported one failure: PSEPK/groES GO:0046872 is UNDECIDED in the live review, while the historical batch recorded REMOVE. The existing audit checker supports explicit supersession rather than retrospective rewriting of an adjudication.

Only `superseded_by` was added to that annotation in batch-04.yaml. Its historical action, previous action, row outcome, gene outcome and rationale are unchanged. PR6164's current evidence distinguishes positive mycobacterial GroES metal-binding observations from unresolved transfer of the binding site and affinity to KT2440. Lack of an annotated target metal site does not establish absence of binding. This metadata repair does not adjudicate the science again.

The targeted pytest passes (1 passed); the audit checker reports zero violations, retaining two pre-existing advisory replacement-term observations. Project history validates and git diff --check passes. The proof records the exact CI-log hash and verifies all tracked genes, modules, InterPro family files and publication caches remain identical to the pre-edit HEAD. Unrelated pre-existing untracked files were not touched. No full test or validation run was started.
