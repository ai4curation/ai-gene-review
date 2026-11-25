# phaC1: GPo1 review, 2026-11-07

Identity and evidence: see `analysis/module_audits/bacterial_mcl_pha_synthesis_and_mobilization/gpo1-consultation/primary-scope.md` and the frozen literature consultation. PMID1989978 is abstract-only with publication-linked curated UniProt function; PMID11133449 full institutional copy was read for native turnover. Exact M58445 sequence equality is recorded in the literature identity proof. No data from KT2442 or PAO1 is represented as a direct GPo1 assay.

All seeded annotation payloads and order are preserved. No NEW row is added. The standalone description and core distinguish catalytic role from downstream survival and distinguish PHA chemistry from substrate-specific PHB or glycerolipid predictions. Proposed terms add vocabulary requests, not new source annotations.

Actual Falcon request via `just deep-research ECTOL phaC1 --provider falcon` failed with HTTP403 authentication. The failure log is in `.cache/module-audit-logs/mcl-pha-20261107/gpo1-consultation/falcon-phaC1.log`; no provider report was fabricated. Manual primary/curated-source review supplies the evidence.

`just paint-losses ECTOL phaC1` found the target absent from the cached reference tree; lineage losses cannot be assessed. The generic no-loss footer is not evidence of a resolved negative. Source membership is verified independently from UniProt/archive records; no PTN placement or loss is invented.

## 2026-11-07 — PR6194 second review follow-up

Add CC:FUNCTION metadata to the existing curated UniProt quotation; no function, action, source text or ordered annotation payload changes.
