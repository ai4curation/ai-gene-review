# PR 6184 round 1 gene consultation

Nine gene reviews were revised after source-level adjudication of comment
6704242580. No new annotation rows were created, removed, or retired. The valid
core molecular-function genera remain unchanged. All 14 published reviews retain
88 ordered annotation rows, including 16 historical NEW proposals (all active).

**Explicit source-payload exception:** `BACCR/BC_1526` row index 2, GO:0005886,
PMID:34253723, action NEW: `evidence_type: IDA` → `IC`. This is an authorized
correction to an authored inference, not a GOA evidence-code rewrite. Its term,
reference, row order, action and lifecycle are unchanged. The exact exception is
machine-readable in `preservation.json`; no broad evidence-code exemption applies.

## Reviewer adjudications

| Item | Decision and evidence scope |
| --- | --- |
| 1. ECOLI Lgt GO:0009898 | KEEP_AS_NON_CORE → UNDECIDED. The original 2008 full article used pT7GT-overexpressing BL21(DE3) inverted membrane vesicles and reported extensive water extraction, while acknowledging preparation/overexpression artifacts. Full PMID:22287519 directly supports seven spans and challenges the soluble-fraction interpretation. Current GO:0009898 includes embedded proteins, so multipass architecture is not a negative assay; a cytoplasmic terminus also does not resolve the legacy whole-protein interpretation. The self-authored ontology quotation was removed from row support. Plasma-membrane core retained. |
| 2. PSEPK LspA proteolysis | ACCEPT → MODIFY to GO:0016485 protein processing, an `is_a` child of GO:0006508. The enzyme itself cleaves the precursor, consistently with the ECOLI/BACSU reviews. Target inference remains distinct from direct KT2440 assay evidence. |
| 4. BACSU ypjA coverage | No change. Its supported acetylation process already appears in the core. A coverage advisory does not justify another NEW row. Approved gene bytes remain unchanged. |
| 7. Lnb location | Both Lnb core locations refine GO:0016020 to GO:0005886 as an explicitly labeled inference from alpha-helical multipass architecture and the predicted extracytoplasmic domain/reaction. This is not a native fractionation claim. The paper's inner/outer ambiguity concerns lipoprotein clients. BF reporter rescue and native BT mutant/complementation retain their distinct scopes; existing BT construct-length limitations remain documented. No localization NEW was added. |
| 8. Lit localization evidence | The exact authorized IDA→IC change above reflects structural/pathway inference of the native compartment. Direct purified Lit chemistry remains direct evidence; all other original codes are preserved. |
| 9. Specific activity proposals | Five machine-readable proposals were added alongside valid GO genera: donor-agnostic Lnb terminal N-acylation (two genes), Lit intramolecular sn-2 O-to-N transfer (two-chain lyso product), and phospholipid-dependent LnsAB N-acylation (two genes). LnsB remains contributory, not an autonomous acyltransferase/protease. Donor identity is not imported from Lnt into Lnb. No core MF/BP assertions or original annotations changed for this advisory. |
| 10. LspA proposal parent | ECOLI and BACSU proposals now use substrate-defined GO:0009003, matching PSEPK. GO:0004190 is the independent catalytic-mechanism class and remains retained. |

Items 3, 5, and 6 concern module/family scope and are owned by the parent/family
consultation. This consultation did not edit those files.

## Primary and ontology checks

- `quickgo-terms.json` records exact official term queries and current definitions/
  child relations. GO:0009898 includes embedded proteins; GO:0016485 is under
  proteolysis. GO:0009003 and GO:0004190 describe different dimensions of LspA.
- PMID:18602442 remains an immutable abstract-only cache. The full primary was
  read through the public [Academia rendering](https://www.academia.edu/99693874/Localization_and_characterization_of_prolipoprotein_diacylglyceryl_transferase_Lgt_critical_in_bacterial_lipoprotein_biosynthesis),
  checked 2026-11-07. S. aureus supplied lipid donor, not the assayed Lgt. The
  original protocol used recombinant BL21(DE3) IMVs, not native K-12 sided
  localization. The review quotes the protected abstract for extraction and
  full PMID:22287519 for the later aggregate interpretation.
- Full PMID:39495918 establishes Lnb-dependent cellular product chemistry and
  predicts topology. It does not establish purified Lnb turnover or its donor.
- Full PMID:34253723 establishes the exact Lit sn-2 intramolecular transfer by
  purified-enzyme product analysis and NMR. Total product acyl-chain number is two.
- Full PMID:42580408 establishes recombinant LnsA/LnsB phospholipid-dependent
  N-acylation. Partner compatibility, LnsA catalytic role, and unresolved detailed
  LnsB chemistry remain distinct; existing directional cross-species controls
  are preserved.

The three scoped UniProt `record_section` backfills add evidence metadata only.
No raw/provider/publication file was edited. Existing failed provider acquisition
records remain intact; no fabricated provider report was created.

## Reproduction and limits

Run from the worktree root:

```sh
uv run python analysis/module_audits/bacterial_lipoprotein_maturation/round1/gene-consultation/check_preservation.py
uv run ruff check analysis/module_audits/bacterial_lipoprotein_maturation/round1/gene-consultation/check_preservation.py
```

The preservation checker permits only the named semantic fields and the exact Lit
code exception. It verifies all 88 protected sources and all 188 previously
published history/audit artifacts byte-for-byte. `preservation.json` records every
semantic delta and source hash. `validation.json` records nine focused gene
validations, nine renders, nine generated histories and nine history validations.
All 36 commands passed. `handoff.json` hashes the released files.

Warnings are advisory: uncited existing research reports, a PSEPK LspA core
signal-peptidase coverage warning, BACSU LspA process coverage, and the two inferred
Lnb plasma-membrane core locations lacking separate annotation rows. They do not
justify manufacturing NEW rows. No whole-corpus validation, commit, push, module
edit, family edit, or project edit was performed by this consultation.
