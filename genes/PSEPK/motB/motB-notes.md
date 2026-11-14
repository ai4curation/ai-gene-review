# motB (PP_4904, Q88DC3) notes

## 2026-11-03 re-review
- Deep research: `just deep-research PSEPK motB --provider perplexity` failed (provider 'perplexity' not available); `just mod-description-deep-research` skipped (no MOD provider configured for PSEPK). Existing falcon report used; every falcon quote was checked as a verbatim substring.
- UniProt quotes now cite the local flat file (file:PSEPK/motB/motB-uniprot.txt). ARBA-only, imported (ECO:0000313), DE-name and DR GO lines are not used as support.
- Replaced ARBA/imported UniProt quotes (cell membrane, "Flagellum", PANTHER name) with Phobius TRANSMEM and PROSITE OmpA-like domain lines.
- GO:0016020: REMOVE -> MODIFY to GO:0005886 (true but general). GO:0005886: KEEP_AS_NON_CORE -> ACCEPT.
- Added NEW rows for the core-function terms that had no annotation row: GO:0071973 (IMP, PMID:36409076 motAB deletion), GO:0120101 stator complex (IC), GO:0042834 peptidoglycan binding (IC, OmpA-like domain; subunit MF), GO:0015078 contributes_to (IC; module MF, complex level) [PMID:35572622 "MotB/PomB have a single TM segment at their N-termini and a large periplasmic C-terminal region that is anchored to the peptidoglycan (PG) layer."]. Status remains COMPLETE.


## Taxon/module audit, 2026-11-06

Remove the stale MotA4MotB2 claim from the description and review summaries/reasons. This 2020 paper directly solved other species; do not replace it with an alleged KT2440 stoichiometry measurement. The KT2440 study identifies PP_4904 as MotB and distinguishes fluid swimming from semisolid spreading. Remove the transferred claim that MotCD dominates at high viscosity: ΔmotCD cells were indistinguishable from wild type in the tested fluids. Retain the MotB peptidoglycan-binding inference and complex-level proton contribution.

Source anchor: [PMID:32929189 "The structures reveal an unexpected asymmetric A5B2 subunit assembly where the five A subunits enclose the two B subunits."]

All existing annotations were reassessed. Machine annotation fields, inherited NEW rows, UniProt/GOA files and provider reports were preserved. No new annotation rows were added; unchanged actions reflect retained biological judgments, not skipped review. Existing provider/manual research was consulted; this focused audit creates no provider-authored report. Current ontology definitions and primary literature take precedence over module completeness.



## 2026-11-06 comparative flagellar audit

Reviewed every existing annotation and the biological summary/core functions. Original annotation payloads, including historical NEW proposals, are preserved. Family/domain evidence supports conserved structural assignments; comparative Salmonella or other bacterial assays are not presented as KT2440 experiments. Exact subunit counts and interaction geometries are not transferred as target measurements.

PMID:36409076 uses KT2440 FliC S267C as its stated wild type, reporting that the substitution does not affect motility. MotAB pair deletion tests conditional cellular function; it is not isolated-subunit proton flux. MotAB is important in fluid, whereas MotCD affects semisolid spreading. PMID:39766194 summarizes modern 5:2 stator structures in other bacteria, replacing the historical 4:2 model without claiming a KT2440 structure.


## 2026-11-11 — reconcile chemotaxis and merged flagellar audits

Retain merged flagellar evidence and decisions, including gradient-guided stator mechanics and FliG switching; retain branch primary structural references, target-specific caveats, and broad-family limits. FliN direct CheY-contact uncertainty is preserved.
