# Publication/source closure after review 5812414716

Captured science head: `b05ebf8a63b180882c7251efe0d549b62fa91c2d`. This is an additive source/publication closure, not a new full-corpus or capacity result.

`source-closure.json` freezes **645 inputs**, including the union of the prior published path manifests, both sealed follow-up handoffs, **46 member/comparator reviews**, **12 relevant family reviews**, the module, source inventories and **164 normal publication caches**. It records **720 recursive PMID/file citation edges**; the same scan supports Reactome citations, but none occur in this document set. Notes citations and comma-grouped PMID lists are included. Entire primary-paper bibliographies and provider-report bibliographies are source leaves, not an unrelated repository-wide source pool.

All **483 current ordered annotation payloads and actions** match published head `462ff344a425348aa3e9518cf3a55598cb1e69d1`. The **52 active current NEW rows** retain their source fields and lifecycle. The earlier archived retired proposal and the separately archived refined proposal remain untouched; no new lifecycle decision occurs here. **92 original raw sources and 22 provider artifacts** match the original captured hashes. PSEPK **cheR2 is explicitly checked byte-for-byte against the published review**, and remains unchanged. The only panel review bytes differing from that head are the already sealed CheW/CheY wording/convention corrections.

Historical manifest hashes remain associated with their own snapshots. `latest_manifest_authorized_successors` identifies the eight current differences from the latest preceding 371-path integration map: the sealed gene/note/module changes and module render, plus two root-owned audit metadata files committed at the captured head. Both new gene renders are included through the sealed validation handoff. Earlier manifest subject versions are retained explicitly, rather than overwritten. Four shared project metadata files are observations outside immutable science inputs, allowing root-owned integration metadata to proceed separately.

Thirteen notes-linked private files lacked a tracked byte-identical equivalent. The authorized `private-source-aliases/` package preserves their exact bytes, with original paths/hashes in `private-alias-map.json`: one ontology ancestor snapshot, eight genuine Falcon-failure logs, and four old seed/baseline captures, totaling **428,006 bytes**. The ontology snapshot is current evidence; the logs and baselines preserve historical provenance and are not biological support. Two references to cache directories remain explicitly historical directory references; no directory was recursively copied. A checkout with only these durable aliases can reproduce the checks without those private paths.

Three previously absent normal bibliographic records were fetched without refreshing existing sources:

- PMID37790397: CheA domain-architecture **preprint**, mentioned to distinguish the published PMID38038435. The full normal cache supports that provenance role, not a universal catalytic grant.
- PMID15299315: E. coli Tar ligand-binding-domain structure; the abstract describes a sulfate pseudoligand. This is context for an old unproposed binding-term question, not a new direct aspartate-binding assertion.
- PMID9315712: E. coli Tar apo-domain structure/comparison, likewise abstract-only and retained in that historical context.

`new-publication-source-roles.json` records access and claim limits. Root's two fetch receipts/logs were copied byte-exact; the separately authorized normal fetch of 9315712 has its own exact command/exit/hash receipt. No full copyrighted paper was copied into the alias package, and no license was assumed.

The minimal checker is reproducible with:

```sh
.venv/bin/python -B analysis/module_audits/bacterial_chemotaxis_signal_transduction/review-5812414716-source-closure/check_closure.py
.venv/bin/ruff check --no-cache analysis/module_audits/bacterial_chemotaxis_signal_transduction/review-5812414716-source-closure/check_closure.py
```

Both pass; missing cited sources: **zero**. The checker writes only this new directory's result. No science, shared metadata, old receipt, render or existing cache was edited; no validation corpus, commit or push was run. Root owns subsequent integration and publication.
