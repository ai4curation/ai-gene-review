# ARMC6 review notes

## Sources
- Affinage: trust gates clear; all four findings are in vitro or overexpression.
- Human Protein Atlas (checked 2026-10-04): main location cytosol. This is the only localization source, behind both cytosol rows.
- The hematopoietic IBA (PTN000527910) has a single seed: mouse Armc6 (Q8BNU0, MGI:1924063), IGI from PMID:24029230. That is a SAMD9L knockout study whose cached abstract does not mention Armc6, and no full text is available. → UNDECIDED.
- UniProt DR: BioGRID 209 and IntAct 247 interaction records; BioGRID-ORCS 105 CRISPR screen hits, none characterized.

## Decisions
- Cytosol (IBA, IDA) → ACCEPT.
- Hematopoietic progenitor cell differentiation (IBA) → UNDECIDED.
- No NEW terms. The in vitro G-quadruplex binding (PMID:39029558, abstract: "The protein binds G-quadruplex structures and does so preferentially to RNA over DNA") is declined as an MF pending in-cell evidence.
- core_functions records the cytosolic location only (no MF). The knowledge gap is MF_DARK.

## Review round 1 (PR #4189)
- The GO:0002244 reason now states the reasoning, and its SAMD9L-only supported_by is dropped.
- PMID:24029230 reference_review no longer says VERIFIED. Correctness is left unset, because no enum value fits: the identifier is right, but its support could not be checked. UNVERIFIED means "not yet manually checked".
- Added a location-only core function (cytosol).
- The cytosol IBA summary notes the is_active_in caveat.
- The two PTN nodes are labelled distinctly.
- The G4 MF is now framed as "declined pending in-cell evidence".
- MGI:1924063 = mouse Armc6 (UniProt Q8BNU0) and its IGI to PMID:24029230 were confirmed in QuickGO during the original review.
