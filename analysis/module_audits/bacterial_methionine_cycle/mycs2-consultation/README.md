# Mycolicibacterium smegmatis mc²155 consultation

MetE and MetH reviews are COMPLETE. All 16 seeded annotation payloads remain in their original order; there are no new, removed or retired rows. Four immutable raw files are preserved.

Native source PMID33468593 establishes the cobalamin/riboswitch context and conditional use of the two routes. It names MSMEG_4185 (MetH) and reference genome CP000480.1. Mapping the named native MetE to MSMEG_6638 additionally uses the official strain/locus record; an exact experimental full-construct sequence is not claimed. ADP1 papers18319726/18840283 and M. tuberculosis phenotypes are not target evidence.

MetE/A0R6Q9 is the canonical 771-residue two-domain folate-dependent enzyme, distinct from compact MesD/MesB. Conserved zinc binding is supported, but inconsistent one-versus-two zinc predictions do not establish target stoichiometry. MetH/A0QZX6 has the complete canonical modular architecture. Donor/cofactor chemistry combines native functional context with explicitly labeled homolog evidence and curated domain/rule assignments. Homocysteine consumption, tetrahydrofolate metabolism and terminal methionine regeneration are direct mechanistic participation inferences, not measurements of whole native SAM-cycle flux. GO0071267 salvage is not restricted to MTA chemistry. Cytosol is an inferred location, not a target fractionation result.

Fresh QuickGO definitions and ancestry are archived. Both genuine Falcon requests failed with HTTP403 authentication errors; no provider report was fabricated. Target accessions are absent from cached PAINT trees, so tool completion does not resolve target loss status. No source-only ARBA family assertion is used as support; the MetH classification quote is the actual InterPro MetH domain assignment.

Run `uv run python analysis/module_audits/bacterial_methionine_cycle/mycs2-consultation/check_preservation.py`. Focused validation, rendering and generated-history checks pass; logs, source/action accounting and immutable release manifest accompany this note. The builder records the curation transformation but should not be rerun against a frozen release.
