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
