# Lol independent capacity consultation

Frozen against COMPLETE module SHA256 `73b62fdede73dcc3362fc4e5e2a5e7ed8fbeef1be61e1a396957d4b7a08c70b0`.

From repository root:

```sh
uv run python analysis/module_audits/bacterial_lol_lipoprotein_trafficking/capacity-consultation/check_capacity.py
uv run python analysis/module_audits/bacterial_lol_lipoprotein_trafficking/capacity-consultation/check_closure.py
uv run ruff check analysis/module_audits/bacterial_lol_lipoprotein_trafficking/capacity-consultation
```

These scripts read curated inputs and write only their deterministic reports in this consultation directory. The original `cases-draft.yaml` is retained as preparatory history; `cases.yaml` is the final evidence-qualified case set, with two additional explicit diagnostic cases in the wrapper. `results.json` records 32 scenarios, five mutations of the actual module, five source-gate sensitivity tests, and production atom/core output. `source-closure.json` verifies seven released manifests, hashes 276 inputs and checks 186 quotations. `member-closure.json` records the 17 exact reviewed gene products, raw source paths, taxa, roles, core functions and family identifiers.

Read `findings.md` for the scientific limits. The original full-text PMC bypass capture is hashed as an external input; `PMID28416660-scoped-excerpts.md` transcribes two verified excerpts with URL/date/source hash. The protected publication cache remains abstract-only. The quote checker uses the repository publication helper and local-source matcher, with fetching disabled and no baseline exemption.

The output is a bounded source-qualified capacity audit, not a claim that the native compiler infers complex assembly, compatibility, proposed insertion functions or construct conditions. It is also not a whole-corpus validation or universal statement about all Lol homologs. No gene/module/family/project/source files were changed by this consultation.

`handoff.json` freezes owned file hashes and input hashes. The parent owns any subsequent status integration, member-index refresh, whole-corpus validation and publication. Ownership is released.
