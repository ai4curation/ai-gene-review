

## Full-gene re-review, 2026-09-20

All14 rows reviewed. Four broad catalytic/nucleotide annotations and membrane/cytosol restored to ACCEPT; cytoplasmic support now explicitly comes from PAINT rather than solubility. The four autophagy rows remain UNDECIDED while root independently checks PTN000681272 and target placement. Neither the LOK-related family name, domain count, huge ciliate kinome nor absence of a target assay is sufficient counterevidence. Falcon was read completely and its target-substrate/location limits incorporated; generic ciliate pathway discussion was removed from the biological description. Source rows are unchanged.


### Actual PAINT topology resolved during the same review

Root obtained the nested tree with POST to the PANTHER treeinfo endpoint. The exact lineage was independently read: PTN002805221 → PTN000681272 → PTN007795585 → PTN008401646 → PTN001218730 → PTN007795752 → PTN002805316 (A0BFB4/GSPATT00028266001). This supersedes the earlier inability to inspect the tree. All four autophagy rows are now ACCEPT as inherited functions. The evidence snapshot and explanation are in A0BFB4-placement-evidence.md/json and root’s projects/TREEGRAFTER/rereview-2026-09-20/a0bfb4-paint-classification-check.json. The remaining focused question reconciles live sequence classification with actual PAINT family assignment; it does not assume that the target lies outside the autophagy clade.


## Recovery PR specificity follow-up (2026-09-22)

Make the molecular work or process role explicit separately for each challenged term; retain evidence-based core versus peripheral judgments rather than treating ontology breadth as non-coreness.


## Final evidence and annotation-action reconciliation (2026-09-23)

Removed limitation/tool-access statements from positive support where applicable and retained the actual lineage or sequence evidence. Historical uncertainties remain in the rationale rather than being treated as proof of function.


## OpenScientist autophagy-architecture follow-up (2026-10-10)

Read the focused report on the PTHR24348 versus PTHR44167 placement issue. The report supports the same conclusion as the earlier topology snapshot that A0BFB4 is genuinely Atg1/ULK-related rather than misplaced into PTHR24348 by a donor-count artifact. Its new target-relevant argument is narrower: A0BFB4 retains the compact kinase domain but lacks the canonical C-terminal Atg1 interaction module, and ciliates lack the Atg13/Atg17/Atg101 initiation complex. Retained the kinase MF rows and broad PAINT localizations, marked the four autophagy BP/CC rows as over-annotated, and removed autophagosome assembly / phagophore assembly site from the core function pending Paramecium-specific localization or knockdown evidence.
