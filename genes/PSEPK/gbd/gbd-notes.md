# gbd evidence notes

## 2026-08-11

The exact Q88JJ9 record is an unreviewed submitter-name assignment to
4-hydroxybutyrate dehydrogenase/EC 1.1.1.61. Independent biochemical work on a
Group III Fe-dependent gamma-hydroxybutyrate dehydrogenase establishes
NAD-dependent alcohol-to-aldehyde chemistry, but it is not an assay of Q88JJ9.
[PMID:31981617 "forward direction (alcohol -> aldehyde) reaction of a Group III ADH"]

KT2440 can route 4-hydroxybutyrate toward succinate, alongside alternative
CoA-activation and beta-oxidation routes. The published KT2440 study does not
identify Q88JJ9 as the operative enzyme. [PMID:32256468 "The resulting
4-hydroxybutyrate can be metabolized through three possible pathways"]

The specific Q88JJ9 assignment remains a family/EC prediction pending direct assay.


## 2026-10-26 — complete target and source audit

PP_2650/Q88JJ9 is distinct from PP_2049/Q88L86. The old refinement to exact 4HB dehydrogenase relied on a submitter EC/name and a broad Fe-ADH family; these are insufficient to settle substrate specificity. Retain NAD-linked alcohol dehydrogenase as an independent domain/functional-family inference, keep catalytic metal binding at its warranted precision, and leave the existing exact 4HB row UNDECIDED. This supersedes the earlier core assignment, without claiming the reaction is absent. PMID:31981617 assays Cupriavidus Q59104, not PP_2650. PMID:32256468 tests PP_2049 and explicitly reports unsuccessful direct 4HB assays. The updated manual source assessments preserve PR4748's valid contextual boundary; no patch was blindly applied.

The current source record independently identifies `Pfam; PF00465; Fe-ADH; 1.` and `InterPro; IPR018211; ADH_Fe_CS.` These support enzyme class and a catalytic metal site. The ARBA-only Fe cofactor sentence is not used to prove exact iron occupancy. No cellular location or new process is inferred merely from soluble-looking chemistry.

Workflow: all original annotation fields, order and flags and both raw source hashes were captured before changes. Actual Falcon and fallback provider attempts failed; no provider report was fabricated. Normal publication caching and bacterial fitness retrieval were attempted; FEBA was unreachable and no fitness artifact was created. Manual primary/domain review supplies the decisions. No new annotation row was added.


## PR #5591 source and cofactor follow-up — 2026-10-26

Removed curation commentary from the standalone PP_2650 summary. The biological distinction from PP_2049 and unresolved substrate specificity remain intact; no action or core changed. All original annotation payloads, qualifiers, actions and raw UniProt/GOA bytes are preserved. No NEW annotation was added. Independent bounded consultation agreed that NAD capacity does not imply NADP exclusion. Focused validation, source checks, renders and preservation checks are recorded in the PR #5591 follow-up report.

## 2026-11-02 — GO:0047577 marked over-annotated

Nothing new about PP_2650 turned up, so this follows the audit recorded above
rather than overturning it. The substrate-specific 4HB assignment rests on the
EMBL submitter name and the EC number derived from it; the independent
signatures (`Pfam; PF00465; Fe-ADH`, `InterPro; IPR018211; ADH_Fe_CS`) establish
a broad group III iron alcohol dehydrogenase, a family whose members differ
widely in substrate; and the one KT2440 study that looked for this chemistry
tested other loci and reports unsuccessful direct 4HB dehydrogenase assays on
extracts [PMID:32256468 "Attempts to obtain direct biochemical evidence for the oxidation hypothesis with"].
Within PTHR11496:SF102 the reaction is established only for the assayed
Cupriavidus GHBDH (Q59104), not for the subfamily.

MARK_AS_OVER_ANNOTATED rather than REMOVE, because the enzyme class is right and
a 4HB activity has not been excluded for this protein; the true class-level
claim stays in the GO:0004022 row. The same judgement is now recorded at family
level as a `member_exceptions` entry on the GO:0047577 scope in
`interpro/panther/PTHR11496/PTHR11496-review.yaml`, so the gene and the family
say the same thing. The module continues to use PP_2650 only as an optional
comparator with the alcohol-dehydrogenase class term, never as the enzyme of the
pathway step. No other row, action or core function was changed.
