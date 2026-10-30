# opa1 (Danio rerio) review notes


## Batch 05 curation notes
- Core interpretation: opa1 encodes a mitochondrial dynamin-like GTPase that mediates mitochondrial inner-membrane fusion, cristae morphology, and mitochondrial organization. The core function is GTPase-dependent membrane remodeling/fusion at the mitochondrial inner membrane and intermembrane space; cardiac and embryonic phenotypes are downstream developmental consequences.
- Key UniProt support: Dynamin-related GTPase that is essential for normal mitochondrial morphology.
- Existing GOA annotations were reviewed against this core role; broad, inferred, or downstream phenotype annotations were kept as non-core unless they overstate the direct function.

## 2026-09-20 full-gene re-review

All 26 source rows reviewed and source fields preserved. Restore broad mitochondrial membrane, GTPase and GTP metabolism annotations: specificity is not exclusivity. Full PMID:25022898 Fig. 6H directly tests zebrafish Opa1 and ventricular hypertrophy; the title foregrounding Tom70 is not a gene-misattribution argument. PMID:23516612 directly supports mitochondrial morphology and developmental phenotypes.

Mouse ISS donor P58281 resolves to PMID:36171294. The full paper distinguishes cytokine output from early differentiation: “Thus, OPA1 sustains cytokine production in TH17 cells in vitro, but not early differentiation events associated with transcription factor expression.” Retain IL-17 production as inferred noncore; modify lineage commitment to that better-supported process. Zebrafish-specific immune tests remain absent from this evidence set, which is not negative evidence.

Read the complete existing Falcon report and the shared [EAT-3 OpenScientist adjudication](../../worm/eat-3/eat-3-hypotheses/microtubule-and-peroxisome-capacities/openscientist.md). The latter is useful for domain/topology concerns but overstates exclusion. It supplies no executable analysis artifact or target-negative capacity assay. Its caveat that primary localization alone does not refute a conditional interaction is retained. No duplicate report requested.

Independent live PANTHER treeinfo response (v19) verifies PTN000170013 → PTN000902162 → PTN008520527 → PTN008520528 → PTN008973342 → PTN007514526 (OPA1) → … → PTN000170160 (Q5U3A7). Thus neither challenged node is restricted to its extant classical-dynamin/DRP1 donors. Current PAINT IBDs were read directly; no target-loss event was established. Peroxisome fission and microtubule binding remain UNDECIDED. Compact API provenance/ancestry is in projects/IBA_REVIEW/rereview-2026-09-20/organelle-paint-lineages.json.

Additional full-primary cross-check: PMID:20185555 Fig. 2A tests purified human OPA1-S1 liposome association with phosphatidic acid as well as cardiolipin; Fig. 4 demonstrates membrane tubulation. PMID:32228866 Fig. 1A explicitly identifies an OPA1 middle domain and C-terminal GED, so the shared report's claim that absent GED database labels prove absence of that structural machinery is unsound. Its structure demonstrates a dynamin-like power stroke and helical membrane remodeling. This supports the accepted lipid-binding/tubulation terms without proving microtubule binding or peroxisome fission. PMID:28628083 abstract independently reports human L-OPA1/cardiolipin reconstituted fusion; PMID:37612504 abstract describes the lipid-binding paddle and membrane-bending lattice. The last two were not full-text verified.


## Recovery review consistency follow-up (2026-09-22)

Restored readable identifiers in manual prose. Where applicable, reconciled AP3M2 reference notes with the retained contextual claim, removed unrelated PIK3C3 support from unresolved projections, separated PIK3C3 aspect-specific reasons, and documented the surviving/renamed ATG14 membrane term. Source assertion fields and verbatim quotations are unchanged.

## Recovery evidence relevance follow-up (2026-09-23)

Removed the physical-interaction quotation from the peroxisome-fission review because it concerns a different capacity. The verified ancestral placement remains documented in `projects/IBA_REVIEW/rereview-2026-09-20/organelle-paint-lineages.json`; the UNDECIDED call does not assert that Opa1 performs peroxisome fission. Mitochondrial topology and specialization are relevant evidence, and rejection need not await a negative experiment, but the shared report's clade-exclusion and GED-loss premises were independently contradicted. Inheritance or loss at the OPA1 branch remains the question requiring adjudication.

The same burden-of-proof clarification now applies to both disputed peroxisome-fission and microtubule-binding rows: rejection does not require a negative assay. The reasons preserve the independently verified ancestry and contradicted domain-loss premise, with inheritance/loss unresolved. Opa1 no longer uses the AI report as a supporting quotation for either capacity.

## Final tracking PR evidence follow-up (2026-09-23)

Remove the negative-assay absence clause from the disputed report reference review, aligning it with the annotation reasons. Preserve the independently verified ancestry and domain-architecture rebuttal; no action or supporting quotation changes in this gene.

## Re-review 2026-09-28

Audit only; the 2026-09-20/23 adjudications were kept. The refreshed GOA added five rows, all resolved here (31 rows total):

- GO:0003924 GTPase activity (IBA, PTN000170013): ACCEPT, consistent with the IEA/ISS rows. Family-wide activity, intact dynamin-type G domain (291-567) on the target record; human OPA1 GTP hydrolysis measured directly [PMID:20185555 "OPA1-S1 associates strongly with liposomes containing 25% phosphatidic acid (POPA) or 25% phosphoserine (POPS)"].
- GO:0005737 cytoplasm (IBA, is_active_in, PTN000170013): MODIFY to mitochondrial inner membrane / intermembrane space. True by GO definition (cytoplasm includes organelles) but a lowest-common-denominator placement at the deep dynamin node; the target record gives a transit peptide, single IM helix and IMS topology for residues 113-776 [file:DANRE/opa1/opa1-uniprot.txt "inner mitochondrial membrane, and the short soluble form"]. propagation_review: TERM_SCOPING_PROBLEM / GRANULARITY_MISMATCH.
- GO:0005874 microtubule (IBA, is_active_in, PTN000170013): UNDECIDED, paired with the microtubule binding row already UNDECIDED from the same node. Topological objection recorded (entire GTPase/stalk/paddle region is IMS-facing per UniProt; structure assembled on lipid membranes [PMID:32228866 "hydrophobic residues in its extended membrane-binding domain are critical for its tubulation activity."]); inheritance-or-loss at the OPA1 branch still unresolved, so both rows stay together.
- GO:0043009 chordate embryonic development (IMP, PMID:23516612, second ZFIN row = splice-blocking MO): KEEP_AS_NON_CORE, same as the translation-blocking row [PMID:23516612 "splice-blocking morpholino (SB) designed to span the junction between intron 12 and exon 13 was also injected at 4."].
- GO:0097749 membrane tubulation (ISS from human S-OPA1 chain PRO_0000253479): ACCEPT, matching the whole-protein ISS row; the target annotates the corresponding short chain PRO_0000417514.

Also added a reference_review (HIGH/VERIFIED) for PMID:23516612, which lacked one, and two suggested questions/experiments (zebrafish L/S processing; PAINT decision on the OPA1-branch inheritance of the deep-node microtubule/peroxisome terms; in vitro lipid-stimulated GTPase/tubulation with purified zebrafish S-Opa1; stable CRISPR mutant EM). Validation: zero errors, zero warnings.
