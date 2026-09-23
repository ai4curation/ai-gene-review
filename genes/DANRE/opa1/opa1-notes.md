# opa1 (Danio rerio) review notes


## Batch 05 curation notes
- Core interpretation: opa1 encodes a mitochondrial dynamin-like GTPase that mediates mitochondrial inner-membrane fusion, cristae morphology, and mitochondrial organization. The core function is GTPase-dependent membrane remodeling/fusion at the mitochondrial inner membrane and intermembrane space; cardiac and embryonic phenotypes are downstream developmental consequences.
- Key UniProt support: Dynamin-related GTPase that is essential for normal mitochondrial morphology.
- Existing GOA annotations were reviewed against this core role; broad, inferred, or downstream phenotype annotations were kept as non-core unless they overstate the direct function.

## 2026-09-20 full-gene re-review

All 26 source rows reviewed and source fields preserved. Restore broad mitochondrial membrane, GTPase and GTP metabolism annotations: specificity is not exclusivity. Full PMID25022898 Fig. 6H directly tests zebrafish Opa1 and ventricular hypertrophy; the title foregrounding Tom70 is not a gene-misattribution argument. PMID23516612 directly supports mitochondrial morphology and developmental phenotypes.

Mouse ISS donor P58281 resolves to PMID36171294. The full paper distinguishes cytokine output from early differentiation: “Thus, OPA1 sustains cytokine production in TH17 cells in vitro, but not early differentiation events associated with transcription factor expression.” Retain IL-17 production as inferred noncore; modify lineage commitment to that better-supported process. Zebrafish-specific immune tests remain absent from this evidence set, which is not negative evidence.

Read the complete existing Falcon report and the shared [EAT-3 OpenScientist adjudication](../../worm/eat-3/eat-3-hypotheses/microtubule-and-peroxisome-capacities/openscientist.md). The latter is useful for domain/topology concerns but overstates exclusion. It supplies no executable analysis artifact or target-negative capacity assay. Its caveat that primary localization alone does not refute a conditional interaction is retained. No duplicate report requested.

Independent live PANTHER treeinfo response (v19) verifies PTN000170013 → PTN000902162 → PTN008520527 → PTN008520528 → PTN008973342 → PTN007514526 (OPA1) → … → PTN000170160 (Q5U3A7). Thus neither challenged node is restricted to its extant classical-dynamin/DRP1 donors. Current PAINT IBDs were read directly; no target-loss event was established. Peroxisome fission and microtubule binding remain UNDECIDED. Compact API provenance/ancestry is in projects/IBA_REVIEW/rereview-2026-09-20/organelle-paint-lineages.json.

Additional full-primary cross-check: PMID20185555 Fig. 2A tests purified human OPA1-S1 liposome association with phosphatidic acid as well as cardiolipin; Fig. 4 demonstrates membrane tubulation. PMID32228866 Fig. 1A explicitly identifies an OPA1 middle domain and C-terminal GED, so the shared report's claim that absent GED database labels prove absence of that structural machinery is unsound. Its structure demonstrates a dynamin-like power stroke and helical membrane remodeling. This supports the accepted lipid-binding/tubulation terms without proving microtubule binding or peroxisome fission. PMID28628083 abstract independently reports human L-OPA1/cardiolipin reconstituted fusion; PMID37612504 abstract describes the lipid-binding paddle and membrane-bending lattice. The last two were not full-text verified.
