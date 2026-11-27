# PR6198 six-gene follow-up completion

The received twelve uncommitted gene YAML/notes edits were independently reviewed against the current PR6198 review, existing primary publications, deposited structures and original source records. They are retained. This completion additionally supplies missing record-section metadata, six helper-generated histories, six refreshed renders and repeatable preservation/source checks. No module, family, project, raw/provider or publication files were changed.

## Scientific decisions

- BP3760 now cites measured E. coli MlaA-assisted carrier loading rather than MlaC headgroup composition. Target location and pathway participation remain qualified ortholog/architecture inferences. B213 derivative genetics is not recast as five Tohama I target assays.
- PAO1 Ttg2D gains two IDA proposals: phospholipid binding and outer-membrane-bounded periplasmic location. The tagged, complementing native-host preparation is distinguished from heterologous crystallography; binding/reloading does not measure complete directional transport.
- BP3761 gains one IDA proposal for PE binding and its binding core is refined accordingly. Exact 11HY/11IF mature-target sequence matches and DPPE ligand identity were independently rechecked. This says that PE binds, not that PE is preferred/exclusive or that native directional flux was assayed. Depositions remain marked To be published.
- No process annotation was added. The three proposals rest on independent positive evidence and absence of redundant MF/CC rows, not on a blanket rule for zero-annotation genes. The earlier no-NEW tally remains historical in append-only notes.

## Preservation and checks

All 115 ordered original rows across 18 reviews retain exact non-review payloads, source qualifiers and actions. All 16 historical NEW rows are entirely unchanged and active. Three new rows yield 118 current rows, 19 active NEW and zero retired NEW. Sixty protected raw/provider/family sources and eight prior receipts remain exact. Every used local source is unchanged from published head ced73fcd43a383c9d27257a571d7fcf1f9e715de; 73 scoped quotations match their source text. Notes retain the published bytes as a prefix.

Six focused gene validations, six generated-history validations and six renders pass. Eleven annotation-coverage warnings remain: BP3757 1, BP3759 2, BP3761 5, PAO1 ttg2D 3. They identify core claims without matching row proposals and do not themselves establish missing annotations. No rows were added to silence them. BP3758 and BP3760 have zero curation warnings. The environment emits a pkg_resources deprecation notice. Ruff and scoped git diff --check pass.

The earlier ENOSPC BP3757 log is preserved and not counted as a pass. Current command/exit/log receipts are under logs/; final checks supersede preliminary checks only where record-section metadata was subsequently completed. The FT-block section helper could not automatically locate pasted multiline FT blocks; exact source matching and manual section confirmation resolve that tooling limitation.

## Reproduction and closure

Run the existing venv Python on check_preservation.py from the repository root. It checks all original row payloads and historical proposals, the three exact additions, source hashes, 73 quotes and both structure identity bridges. run_focused.py is an audit record of the commands and intentionally refuses to overwrite existing receipts; use the explicit commands in validation-summary.json for new runs and new output locations.

handoff.json maps exact released files and source_dependencies; supersession-map.json maps each of the 18 changed gene YAML/notes/HTML files from the published head and, for YAML/notes, from received uncommitted edits. The existing baseline, prior handoffs and old logs remain unchanged. No full-corpus run, staging, commit, push or source download occurred. Module/capacity consumers should recognize BP3761's supported PE-binding descendant without treating it as a native-transport assay.
