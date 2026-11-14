# KT2440 Lpt consultation

Seven PSEPK reviews were reassessed against current GO definitions, target-specific UniProt classification/rule support, cached primary literature and the new P. aeruginosa structural source. All 46 original ordered annotation payloads, actions, qualifiers and core functional assertions are preserved. The two historical LptD/LptE `NEW` molecular-function proposals remain active; no new row or retirement was introduced.

| Component | Exact target | Supported core and limit |
|---|---|---|
| LptA | Q88P98 | LPS binding/transfer in the periplasmic bridge; inferred peripheral OM association is non-core, not integral membrane insertion. |
| LptB | Q88P99 | ATP hydrolysis by the membrane-associated motor; TIGR04406/IPR030921 distinguish LptB from generic ABC ATPases. Cytoplasmic localization remains a bounded homolog-based soluble/peripheral claim. |
| LptC | Q88P97 | LPS transfer through the periplasm-facing domain of an IM-anchored protein; failed cross-species complementation does not establish native role loss. |
| LptD | A0A140FVZ0 | Structural contribution to LptDE-mediated transmembrane LPS insertion; exact E. coli disulfides are not transferred across the target HAMAP feature-residue caution. |
| LptE | Q88DN0 | LPS binding/remodeling and structural contribution to the LptDE translocon; not autonomous complete transport. |
| LptF | Q88P71 / PP_0982 | Distinct membrane cavity component, TIGR04407/IPR030922/PTHR33529:SF7; contributes to LPS transfer without ATP hydrolysis. |
| LptG | Q88P70 / PP_0983 | Distinct membrane cavity component, TIGR04408/IPR030923/PTHR33529:SF2; shared family membership alone does not substitute for LptF. |

The changes improve source scope and review reasons. The GO:0043165 reasons for A/C now describe positive assembly work through LPS delivery rather than treating a downstream envelope phenotype as sufficient participation. The F/G generic topology-method quotation was removed from row support; Lpt-specific studies and target signatures remain. Full original reference identities are preserved with new manual findings and accurate cached-access metadata.

Important reference corrections:

- PMID24990744's linked structure PDB4N4R contains **Salmonella Typhimurium LT2** LptD/E expressed in E. coli. Official RCSB entity responses with URL/access date are archived here. The prior blanket description as an E. coli-ortholog experiment was incorrect; no negative activity conclusion follows.
- PMID26370939 is a **review**, not an additional primary experiment.
- PMID41407669 uses **P. aeruginosa PAO1-LAC** source genes expressed in E. coli for structural/biochemical work and tagged LptB complementation in P. aeruginosa. Its Pa-LptC/Ec-LptC incompatibility statement summarizes earlier studies. These data do not constitute KT2440 assays, universal partner compatibility, or target-specific residue phenotypes.
- UniProt CC assertions for B/F/G are ARBA-derived. Support instead uses their specialized NCBIfam/InterPro signatures and independent homolog experiments; broad ABC classification cannot establish LPS cargo specificity.

All seven actual Falcon attempts failed HTTP403. Exact logs are retained in `provider-attempts/`; no provider report was fabricated. `paint-checks/` records all seven mandatory lineage checks. Each exact KT2440 accession is absent from the cached tree, so losses were **not resolved**. The command's generic “No IRD or IKR” footer is not treated as a successful loss-free ancestry determination. No IBA donor-count or self-donor argument was used.

`reference-assessments.yaml` records source-specific statements and verbatim quotes. `quickgo-terms.json` records official term definitions. `before.json` freezes the parent's seven-review baseline and all 82 protected source hashes. `check_preservation.py` checks ordered payloads, unchanged actions/core assertions/reference identities, source hashes, 110 distinct per-review quotations and immutable preexisting history. `action-ledger.yaml` records every decision.

Validation:

```sh
uv run python analysis/module_audits/bacterial_lps_transport/psepk-consultation/check_preservation.py
uv run ruff check analysis/module_audits/bacterial_lps_transport/psepk-consultation/check_preservation.py
```

All seven `just validate`, `just render`, and generated `just new-history` / `just validate-history` checks pass. Scoped standard record-section backfill dry-run finds zero additions or mismatches. No gene-level warnings were produced; the environment prints a dependency deprecation notice. No module/family/project edits, source-cache rewrites, commits, pushes or whole-corpus run were performed. The final handoff freezes owned artifacts and sources, and releases ownership to root.
