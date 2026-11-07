# Native E. coli nitrogen-PTS review

Three seeded reviews are complete: ptsP/P37177, ptsO/P0A9N0 and ptsN/P69829. All25 original ordered annotation payloads (8/7/10), qualifiers and six raw UniProt/GOA files are preserved. No NEW row or retirement was introduced. No other gene, module, family, publication or project file was edited by this consultation.

The supported core activities are PtsP PEP-to-protein phosphotransfer (GO0008965), NPr nitrogen-acceptor phosphotransfer (GO0016775), and PtsN transporter inhibition (GO0141110) plus KdpD kinase activation (GO0030295). The NPr refinement specifies histidine-nitrogen acceptor chemistry; it does not reject kinase merely because the donor is not ATP. PtsN's TrkA inhibition is a transporter-regulation claim, not an independently demonstrated catalytic-enzyme inhibition. The older enzyme-inhibitor row is therefore laterally refined. Its kinase output remains E. coli-specific; no Pseudomonas or Caulobacter output is transferred.

All bare PtsN binding rows are refined to their demonstrated target functions. NPr–LpxD bare binding is removed under the uninformative-binding policy while preserving the explicitly positive interaction in biology/reason: the abstract is sufficient to establish binding, but the unavailable full text does not justify manufacturing a purified catalytic-inhibition activity. This is not a rejection of the experimental interaction.

Four sugar-process annotations remain UNDECIDED because native physiological participation is not established by in-vitro cross-reactivity alone; no absolute cross-system insulation is asserted. PtsN's electronic coupled-sugar-transporter MF is MARK_AS_OVER_ANNOTATED, with explicit separation of reversible protein phosphotransfer from membrane uptake chemistry. These judgments do not infer nonexistent catalytic residues or ancestral losses.

The exact PANTHER trees were retrieved by root and joined to immutable cached IBD assertions in `paint-join.json`: P37177/PTN000532526 descends from PTN000532509; P0A9N0/PTN002135339 from PTN002135312; P69829/PTN002021088 from PTN002021052. The cached slices contain no negative rows. Positive self-source evidence is legitimate. Ancestry is established; uncertain native sugar-process scope is not justified by donor counts or missing ancestry. No MSA-based residue-loss claim was made.

Primary access is explicit in each reference assessment. PMID10473571/7876255/19400808 have positive biochemical abstracts and are not represented as fully inspected experimental methods. PMID23517463 provides full E. coli entry-enzyme regulation, distinguishing the PtsN K75D reporter and GAF-deletion constructs. PMID17289841 and39742999 provide full TrkA and YcgO studies; target binding, native genetic effects, overexpression and everted-vesicle antiport are not conflated. The MC4100 cytosol IDA is retained with curator attribution; a cohort quote is not presented as a separately re-extracted target peptide row. The2026 review is mechanistic synthesis, not a new target experiment.

The shared real Falcon attempt failed HTTP403 authentication; original sanitized receipt/log remain untouched and are dependencies. Manual notes are named as such. The existing root virtual environment was reused with no sync, `PYTHONPATH` pointing to this worktree, and bytecode writing disabled. No new environment, whole-corpus run or PANTHER member-index build occurred.

Final focused validations for all three reviews pass without curation warnings. The earlier ptsP run's structured-IBA warning was addressed using the actual tree join and the final rerun passes. All three helper-generated codex histories validate, all three HTML renders were produced,62 quoted-support instances match their actual sources, and the exact preservation checker and Ruff pass. `focused-checks.json` records helper/history/render execution; `validation-summary.json` ties the final gene logs to current input hashes. No commit, staging or push occurred.

Run the read-only check using the configured root environment:

```sh
PYTHONPATH="$PWD/src" PYTHONDONTWRITEBYTECODE=1 /Users/cjm/orca/workspaces/ai-gene-review/aigr-modules-taxon/.venv/bin/python -P analysis/module_audits/bacterial_nitrogen_regulatory_pts/ecoli-native-review-20261107/check.py
```

The checker is scoped to source preservation, exact quotes, titles and tree/assertion joins. Full gene validation logs provide the separate schema/term/reference checks. Ownership is released after the exact handoff seal.
