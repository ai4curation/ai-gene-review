# motA (PP_4905, Q88DC2) notes

## 2026-11-03 re-review
- Deep research: `just deep-research PSEPK motA --provider perplexity` failed (provider 'perplexity' not available); `just mod-description-deep-research` skipped (no MOD provider configured for PSEPK). Existing falcon report used; every falcon quote was checked as a verbatim substring.
- UniProt quotes now cite the local flat file (file:PSEPK/motA/motA-uniprot.txt). ARBA-only, imported (ECO:0000313), DE-name and DR GO lines are not used as support.
- Removed DE-name ("Flagellar motor rotation protein", imported ECO:0000313), DR GO and ARBA subcellular-location quotes.
- Added KT2440 genetics: PMID:36409076 [PMID:36409076 "In homogeneous fluids, the MotAB stator is crucial to promote swimming motility, so the movement of ΔmotAB mutant cells in aqueous fluids is strongly impaired."] [PMID:36409076 "the MotAB (PP4905 and PP4904)"]. NEW GO:0071973 changed from IC to IMP on this paper.
- GO:0071978 swarming: MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0071973. Chemotaxis kept MARK_AS_OVER_ANNOTATED with a rewritten reason (stator supplies torque; switching is done by the C ring/che proteins). NEW GO:1902600 changed from IEA (citing the UniProt file) to IC on PMID:18310339. GO:0015078 contributes_to (module MF, complex level) and GO:0120101 kept. Removed the GOA-file reference. Status COMPLETE.


## 2026-11-06 comparative flagellar audit

Reviewed every existing annotation and the biological summary/core functions. Original annotation payloads, including historical NEW proposals, are preserved. Family/domain evidence supports conserved structural assignments; comparative Salmonella or other bacterial assays are not presented as KT2440 experiments. Exact subunit counts and interaction geometries are not transferred as target measurements.

PMID:36409076 uses KT2440 FliC S267C as its stated wild type, reporting that the substitution does not affect motility. MotAB pair deletion tests conditional cellular function; it is not isolated-subunit proton flux. MotAB is important in fluid, whereas MotCD affects semisolid spreading. PMID:39766194 summarizes modern 5:2 stator structures in other bacteria, replacing the historical 4:2 model without claiming a KT2440 structure.

## 2026-11-06 — PR6138 evidence follow-up

Strengthened the chemotaxis inference with direct KT2440 gradient context (PMID32766440) and source-qualified stator phenotypes (PMID36409076). Mechanical execution is distinct from sensing or prior assembly. The MotCD clustering result is retained explicitly; agar spreading is not treated as a gradient-response assay.
