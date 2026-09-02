# CPR6 review notes

## 2026-09-02 Update: obsolete GO:0051082 handling corrected (MARK_AS_OVER_ANNOTATED -> MODIFY)

**Issue found:** Both `GO:0051082` (unfolded protein binding) annotations on CPR6 (the
ARBA-derived IEA and the direct IDA from PMID:10942767) were reviewed with
`action: MARK_AS_OVER_ANNOTATED`, with reasoning that "CPR6 is not an ATP-dependent
chaperone and GO:0044183 would not be appropriate." Checked GO:0044183 directly via
QuickGO: its definition is "Binding to a protein or a protein-containing complex to
assist the protein folding process" — there is no ATP-dependence requirement, so this
premise was incorrect.

Also confirmed via the QuickGO API that GO:0051082 is indeed obsolete
(`isObsolete: true`, name "obsolete unfolded protein binding"), and its own obsoletion
comment says: "The reason for obsoletion is that this binding term should be replaced
by an activity term such as protein folding chaperone (GO:0044183) or unfolded protein
holdase activity (GO:0140309)."

The direct evidence for CPR6 itself is real, if modest: PMID:10942767 (Mayr et al. 2000
J Biol Chem) reports in the abstract that CPR6 does have refolding/chaperone activity in
vitro, while noting it is weaker than its paralog CPR7's:
[PMID:10942767 "In contrast, the chaperone activity of Cpr6 is much lower than that of
Cpr7."]. This is consistent with the reviewer's own acceptance elsewhere in this same
review of the related, non-obsolete `GO:0042026` (protein refolding, IDA from the same
paper) as ACCEPT — i.e. the review already treats CPR6's refolding activity as real, just
not core.

This exact scenario (obsolete GO:0051082 on a folding-chaperone-adjacent yeast gene,
including direct IDA evidence) is handled consistently elsewhere in this project by
`action: MODIFY` with `proposed_replacement_terms: GO:0044183` — see the CHS7, CNE1, and
COX20 ai-review.yaml files, all reviewed in the same batch. CPR6 was the outlier, marking
the obsolete term as over-annotated (discarding it without a valid successor term)
instead of pointing to its GO-designated replacement.

**Fix:** Changed both GO:0051082 entries (IEA GO_REF:0000117 and IDA PMID:10942767) from
`MARK_AS_OVER_ANNOTATED` to `MODIFY` with `proposed_replacement_terms: [GO:0044183
protein folding chaperone]`, and corrected the reasoning text to drop the incorrect
ATP-dependence claim and instead cite the actual (obsolete) QuickGO record and the
PMID:10942767 quote about CPR6's weaker-than-CPR7 chaperone activity. `core_functions`
was left unchanged — GO:0003755 (PPIase activity) remains CPR6's sole core molecular
function, consistent with CPR6's role as the higher-PPIase-activity, lower-chaperone-
activity paralog relative to CPR7.

Verified via QuickGO API:
- `GO:0051082`: `{"isObsolete": true, "name": "obsolete unfolded protein binding", ...}`
- `GO:0044183`: `{"isObsolete": false, "name": "protein folding chaperone", "definition":
  {"text": "Binding to a protein or a protein-containing complex to assist the protein
  folding process."}}`
