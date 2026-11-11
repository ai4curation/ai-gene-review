# PR 6089 review 5812319279: bounded gene corrections

Reviewed baseline: a72264e3128543a968a1dd2d3c970a9c4e61f8bd. This is an additive supersession of the five current reviews, not a rewrite of prior receipts. No raw/provider/publication source was changed, no row was added/removed/retired, and no qualifier was added or changed.

- HELPY/HP_0020: GO0003824 now refines to carboxy-lyase GO0016831; the existing GO0016831 row is ACCEPT at the best-supported genus. The precise carboxyspermidine NTR/core is withdrawn and archived in full. The core retains inferred carboxypolyamine decarboxylation and a separately qualified spermidine-process role. The H. pylori WP_000557673 CAPADH result is evidence for upstream agmatine chemistry, not a direct O24865 assay or proof of exclusive CAPADC activity. The module's precise substrate witness must be removed separately by root.
- CAMJE/Cj0172c: the imported saccharopine row is UNDECIDED; its provisional GO0102143 replacement is removed. Neither the target substrate reaction nor an exclusive CAPA replacement is asserted.
- PSEPK/nspC: added the previously prose-cited PMID37878710 reference with bounded family-diversification evidence. Actions and core unchanged.
- AGRFC/Atu4170: preserved conditional GO0045312 NEW/IC and explained the C58 cellular DAP conversion, 100 µM feeding, ΔODC context and Figure 4B product evidence. This is distinct from an isolated-enzyme alternate-substrate assay. The individual step is inferred; a DAP-fed Atu4170 knockout/complementation assay is not claimed.
- 9FIRM/CLOLEP_01502: explicitly retained measured PUT/DAP capacities while explaining why a NEW MF is not manufactured solely for coverage. Similar BfCASDH rates do not alone establish evolved secondary function; the positive Clostridium CAPA reconstruction supplies a different contextual comparison. No measured activity is denied.

The nine omitted qualifiers raised in the review were not changed: the checked-in annotation-reviewer skill explicitly treats those fields as inert and says not to add/edit them, apart from its negation/contributes_to exceptions; the schema field is optional. No proposed process payload was retired here. The top-level HP_0020 specific NTR/core archive is not an annotation-row lifecycle exception.

## Checks actually performed

` .venv/bin/python -B analysis/module_audits/bacterial_carboxyspermidine_biosynthesis/review-5812319279-gene-followup/check.py `

This read-only checker proves 16 ordered annotation payloads and all four active historical NEW actions/lifecycles preserved, append-only notes, 25 protected raw/provider/publication sources unchanged, and 81 locally matching quotation occurrences. It strips UniProt record-column prefixes only for flat-file quote matching and otherwise normalizes whitespace. It neither validates ontology nor fetches anything.

Five histories were scaffolded with `just new-history` using offline/no-sync uv and bytecode disabled. The first helper invocation inherited its default actor in the generated session identifier; its actor metadata was corrected to codex before release, preserving the helper-generated path/session. All five actual actor_tool/name entries are codex. No old history was edited.

## Remaining root checks

Run focused schema, term, reference/title and best-practice validation on each of the five reviews, validate the five new histories, lint check.py, and render the five reviews after disk availability is safe. No full-corpus run, heavyweight validation, render, staging, commit or push was performed by this consultation. Root owns module/capacity/family/project integration and aggregate receipts.
