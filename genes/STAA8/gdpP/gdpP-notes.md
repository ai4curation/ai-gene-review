# gdpP functional review

## 2026-11-04 — c-di-AMP degradation audit

Identity: Q2G2T6, Staphylococcus aureus subsp. aureus NCTC 8325. The original seeded annotation payloads and both raw source files were preserved. All review actions were judged on the gene-specific biology; no new GO annotations were added.

Actual Falcon research was attempted with `just deep-research-falcon STAA8 gdpP` and failed with HTTP 403 authentication. No provider report was manufactured. Manual research used the primary papers and curated source statements cited below.

- [PMID:21909268 c-di-AMP is a new second messenger in Staphylococcus aureus with a role in controlling cell size and envelope stress.] Cached full text examined; SAOUHSC_00015 is identified as gdpP and experiments include the NCTC8325-derived RN4220 lineage. The source distinguishes the weak ATPase activity from the major phosphodiesterase function.

- [PMID:27834680 New Insights into the Cyclic Di-adenosine Monophosphate (c-di-AMP) Degradation Pathway and the Requirement of the Cyclic Dinucleotide for Acid Stress Resistance in Staphylococcus aureus.] Cached full text examined. The USA300 experiments support a species-level regulatory mechanism; its magnitude is not asserted as directly measured in the NCTC8325 reference strain.

The core is c-di-AMP hydrolysis, not its indirect envelope or stress phenotypes. A generic DHHA1-domain mapping does not establish a distinct nucleic-acid-binding role. Heme inhibition is characterized for Bacillus/Geobacillus proteins; ATPase activity is not generalized to S. aureus. pApA feedback was established for S. aureus GdpP and is not transferred to PgpH.

Module membership: `MODULE:bacterial_c_di_amp_signaling`, `gdpp_pde_activity`.

## 2026-11-05 — PR #5997 evidence follow-up

The hydrolysis evidence supports the catalytic assignment: [PMID:21909268 "Incubation of c-di-AMP with the recombinant rGdpP84–655 protein resulted in the complete conversion of c-di-AMP to 5′-pApA."]

Removed the hydrolysis quotation from the nucleic-acid-binding over-annotation judgment. The judgment assesses unsupported extension from DHHA1-domain membership; it is not a negative RNA-binding assay. The catalytic evidence remains on the catalytic assertion and core function.
