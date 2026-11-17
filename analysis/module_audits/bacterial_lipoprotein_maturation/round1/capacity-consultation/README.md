# PR6184 round 1 capacity and preservation consultation

This additive audit checks the reviewed module and frozen gene/family handoffs without modifying any published audit, source, review, module, or project file. It does not claim full-corpus validation.

## Capacity result

All 39 cases pass. The 35 published cases retain their complete published result vectors, including conditional donor and assembly expectations. All 10 published mutation controls remain detected. Four additional negative cases and one additional mutation test the exact LhaT selector: a generic PTHR40042/GO:0008080 match cannot replace P54392; missing P54392, absence of reviewed activity on that target, and a synthetic inactive-homolog assay context do not qualify. The latter is explicitly a synthetic challenge, not an invented accession or family placement.

The checker invokes the production compiler and satisfaction machinery through the unchanged published checker. Seven compiled activity atoms remain; only the shared Lgt/LspA maturation core is required. The five terminal routes remain optional and distinguish terminal-product capacity from completion of the upstream maturation route. LnsAB requires a supported pair, including the experimentally bounded asymmetric cross-species combinations. Donor, acceptor, activity qualification, and pairing constraints remain external evidence-oracle gates. GO:0042160 is checked on the four edited terminal annotons as process context, not substituted for catalytic function.

A negative test means this evidence-qualified panel does not establish the requested profile. It does not prove absence of every alternative activity, reject all cross-species compatibility, or establish native flux. Exact-member selection protects the measured LhaT claim without granting family-wide activity. Generic GO activity, family membership, or a physiological name alone is insufficient.

## Preservation result

The 14 current reviews retain all 88 ordered source payloads except the single explicitly authorized BACCR/BC_1526 annotation at zero-based index 2: evidence_type IDA to IC. Its term GO:0005886, PMID:34253723, historical NEW action and remaining payload are preserved. All 16 historical NEW rows remain active; there are no additions, deletions, or retirements. All 88 protected source files are unchanged.

Both frozen round 1 handoffs are checked file by file (42 gene files and 21 family files). The old 302-input capacity closure has exactly 29 authorized changed inputs: nine gene YAML/notes/render triplets, the PTHR38686 family review, and the module YAML. Nine original consultation manifests remain immutable; their superseded files are individually enumerated. All 188 historical analysis/history artifacts in the 341-path published manifest remain byte-identical.

The 341-path manifest originated at the earlier full-run science snapshot. Four project/inventory/render files differ from that older manifest but are byte-identical to both pinned round 1 baseline commit 209d07bd1efe2e5cd8e04fd8025d42b22662cef6 and HEAD. They were pre-existing closeout differences at capture, not round 1 scientific changes. The checker validates this historical receipt against pinned Git blobs; it deliberately excludes only these four mutable project metadata paths from the scientific input closure, so root can update and separately freeze their new metadata/history without rewriting this receipt. The remaining manifest deviation beyond the 29 scientific inputs is the root-rendered module HTML. Exact hashes and comparisons are in project-deviation-provenance.json and closure-results.json.

The current module SHA256 is 0baadae89cee21b3824638eeba6a8caa4aab6e33b82982c39d3ef4025b170961. Its 11 references comprise three reviews and eight primary articles, with 23 checked findings/quotes. Seven retained mechanistic quotations are also checked against unchanged source hashes. The additive scientific closure captures 394 input hashes, excluding exactly the four mutable project metadata paths. This is a scoped quotation and preservation check, not a new independent re-review of every source or a corpus-validation result.

## Reproduction

From the repository root:

```sh
uv run python analysis/module_audits/bacterial_lipoprotein_maturation/round1/capacity-consultation/check_capacity.py
uv run python analysis/module_audits/bacterial_lipoprotein_maturation/round1/capacity-consultation/check_closure.py
uv run ruff check analysis/module_audits/bacterial_lipoprotein_maturation/round1/capacity-consultation
uv run ruff format --check analysis/module_audits/bacterial_lipoprotein_maturation/round1/capacity-consultation
```

These commands write only this new consultation directory. Published expectations/results are read as immutable inputs. checks.json records actual exit codes and log hashes; the six deterministic JSON outputs are byte-identical on repeat execution. handoff.json lists every released file and its SHA256, excluding itself and transient Python bytecode.
