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

The direct evidence for CPR6 itself is real, if modest. The abstract of PMID:10942767
(Mayr et al. 2000 J Biol Chem) states that this protein family, of which Cpr6 and Cpr7
are the two yeast members, comprises PPIases "which catalyze the cis/trans isomerization
of prolyl peptide bonds in proteins and possess chaperone activity", and reports that for
CPR6 specifically the activity is weaker than its paralog's:
[PMID:10942767 "In contrast, the chaperone activity of Cpr6 is much lower than that of
Cpr7."].

**Important caveat about the refolding claim.** The cached record for PMID:10942767 is
abstract-only (`full_text_available: false`) and the abstract never uses the word
"refolding" — it says only "chaperone activity", without characterizing the assay. The
refolding claim for CPR6 therefore rests on a different source: SGD's `GO:0042026`
(protein refolding) **IDA** on this same paper (`CPR6-goa.tsv`, ECO:0000314,
PMID:10942767), i.e. an assertion by a curator who read the full text. This review
ACCEPTs that row. Do not read the abstract as itself stating refolding.

This distinction matters for term choice: a Buchner-lab "chaperone activity" assay can be
in-situ aggregation suppression (holdase, GO:0140309) rather than active refolding
(foldase, GO:0044183), and the abstract cannot settle which. GO:0044183 is chosen here on
the strength of the curator-asserted GO:0042026 refolding annotation plus consistency with
the CPR7 decision below; the foldase/holdase discrimination is deferred pending full text
and has been recorded as a `suggested_questions` entry in the review.

**Precedent.** The strongest precedent is the direct paralog: `genes/yeast/CPR7/CPR7-ai-review.yaml`
already has *both* its IEA (GO_REF:0000117) and IDA (PMID:10942767) `GO:0051082` rows as
`action: MODIFY` with `proposed_replacement_terms: GO:0044183` — same protein family, same
paper, same batch. CPR6 was the outlier, marking the obsolete term as over-annotated
(discarding it without a valid successor term) instead of pointing to its GO-designated
replacement.

The same obsolete-term/MODIFY→GO:0044183 handling also appears for CHS7, CNE1 and COX20
in this batch, so the pattern is project-wide — but note that none of those three is a
PPIase (CHS7 is a chitin-synthase ER export chaperone, CNE1 is the yeast calnexin ER
lectin, COX20 is a Cox2 assembly factor). An earlier draft of this note described them as
"other PPIase-family reviews", which is wrong; they are precedent for the term handling
only, not for family membership.

**Fix:** Changed both GO:0051082 entries (IEA GO_REF:0000117 and IDA PMID:10942767) from
`MARK_AS_OVER_ANNOTATED` to `MODIFY` with `proposed_replacement_terms: [GO:0044183
protein folding chaperone]`, and corrected the reasoning text to drop the incorrect
ATP-dependence claim (the ATP-dependent foldase term is the separate GO:0140662) and
instead cite the actual (obsolete) QuickGO record, the PMID:10942767 quotes about the
family's and CPR6's chaperone activity, the SGD GO:0042026 refolding IDA, and the CPR7
paralog precedent. Added the full-text-unavailable caveat to both blocks. `core_functions`
was left unchanged — GO:0003755 (PPIase activity) remains CPR6's sole core molecular
function, consistent with CPR6's role as the higher-PPIase-activity, lower-chaperone-
activity paralog relative to CPR7.

Verified via QuickGO API:
- `GO:0051082`: `{"isObsolete": true, "name": "obsolete unfolded protein binding", ...}`
- `GO:0044183`: `{"isObsolete": false, "name": "protein folding chaperone", "definition":
  {"text": "Binding to a protein or a protein-containing complex to assist the protein
  folding process."}}`
