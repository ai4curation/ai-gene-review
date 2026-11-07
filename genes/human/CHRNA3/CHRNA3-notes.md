# CHRNA3 evidence journal

## 2026-10-26 complete nicotinic receptor audit

Human alpha3 contributes principal ligand-binding faces to heteromeric ganglionic receptors with beta4 or beta2, sometimes including accessory alpha5 or beta3. Reconstituted alpha3beta4 and alpha3beta4beta3 stoichiometries are context-specific.

All original rows and signs retained; no NEW assertions. Normal Falcon/fallback attempts failed authentication/quota (shared foundation job logs); normal publication acquisition completed. Molecular conclusions use primary human reconstitution/structure, not provider text. Rodent physiological transfers are explicitly qualified. Root organelle pools remain intact. Generic binding is removed as uninformative without declaring the measured association false. No substrate proteolysis or enzyme activity is inferred from receptor degradation.

Donor tracing used normal QuickGO read-only queries, ignoring relationship qualifiers, to identify original experimental sources. The trace is provenance, not evidence for its own GO assertions. PMID:19385992 identifies rat alpha2-positive interneurons and downstream inhibitory-current modulation, not a human protein-localization image. PMID:10318955 identifies alpha3-dependent ganglionic rather than muscle machinery; PMID:16162937 distinguishes postsynaptic receptor activity from presynaptic release regulation. Mouse alpha5/alpha6/beta3 striatal primaries PMID:19693710 / PMID:12944511 / PMID:14657161 provide subtype-specific native context. PMID:20881005 reports human receptor biophysics, not behavioral assays; PMID:20923852 supports engineered beta3-containing alpha6 concatamers from its authentic abstract despite unsuccessful fulltext recovery. The beta4 neutrophil-granule assignments remain open because the cached Reactome summaries do not expose protein-specific experimental evidence.

No native stoichiometry is inferred solely from a fixed recombinant concatamer. No neuromuscular PAINT claim is declared evolutionarily lost from donor-count or absence-of-assay arguments; the exact target role at a neuron-to-muscle synapse remains unresolved. Each review reason records the specific available source and inference boundary.


## PR #5582 follow-up, 2026-10-26

Removed generic reference-review templates while preserving source-specific assessments and mined mechanistic findings from the cited receptor reconstitution/structural and native mouse studies. Human engineered receptor composition, reporter-mutation stoichiometry and mouse physiological effects are explicitly distinguished. Citation prose was normalized without altering original annotation payloads or existing supporting quotations.

## 2026-11-05 ORGANELLES ER batch 2 (endoplasmic reticulum rows)

Rows: GO:0005783 IEA (GO_REF:0000044, SL-0095) and ISS (GO_REF:0000024, rat P04757), both `located_in`; no ER sub-compartment rows.

- UniProt: "Endoplasmic reticulum {ECO:0000250|UniProtKB:P04757}" (file:human/CHRNA3/CHRNA3-uniprot.txt, CC SUBCELLULAR LOCATION), so the IEA keyword is itself by similarity to rat.
- QuickGO: rat P04757 GO:0005783 rests on an EXP from PMID:19474315 (Rezvani et al. 2009, UBXD4; abstract only, no PMC full text through the PubMed tool). Abstract: [PMID:19474315 "Our data suggest that UBXD4 modulates the distribution of alpha3* nAChRs between specialized intracellular compartments and the plasma membrane."]
- PMID:26265139 (full text): ERAD of alpha3 in differentiated PC12 cells, [PMID:26265139 "it is conceivable that CHIP/UBXN2A interactions occur while α3 is being extracted from the ER into the cytosol by p97"].
- Outcome: both rows ACCEPT -> KEEP_AS_NON_CORE. A real biosynthetic/quality-control ER pool of the gene (ABCA4/BACE2 rule), but the channel acts at the plasma/synaptic membrane, so not core. MARK_AS_OVER_ANNOTATED was the close alternative (no alpha3-plus-ER-marker image quoted). No NEW ER membrane row: transit pool of a multi-pass subunit. PMID:19474315 added to references.
