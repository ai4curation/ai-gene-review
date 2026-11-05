# pde2 functional review

## 2026-11-04 — c-di-AMP degradation audit

Identity: A0A0H2XFX6, Staphylococcus aureus subsp. aureus USA300. The original seeded annotation payloads and both raw source files were preserved. All review actions were judged on the gene-specific biology; no new GO annotations were added.

Actual Falcon research was attempted with `just deep-research-falcon STAA3 pde2` and failed with HTTP 403 authentication. No provider report was manufactured. Manual research used the primary papers and curated source statements cited below.

- [PMID:27834680 New Insights into the Cyclic Di-adenosine Monophosphate (c-di-AMP) Degradation Pathway and the Requirement of the Cyclic Dinucleotide for Acid Stress Resistance in Staphylococcus aureus.] Cached full text examined; locus SAUSA300_1650 establishes identity independently of the uncharacterized UniProt name. Native mutant and purified-protein data support pApA clearance, while physiological direct c-di-AMP hydrolysis remains uncertain.

Pde2 pApA clearance is kept separate from weak direct c-di-AMP turnover. The canonical pApA hydrolase proposal states only chemistry; feedback relief is its biological justification. The DHH domain alone does not establish a distinct RNA-binding role.

Module membership: `MODULE:bacterial_c_di_amp_signaling`, `pde2_activity`.
