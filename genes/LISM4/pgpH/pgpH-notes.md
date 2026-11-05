# pgpH functional review

## 2026-11-04 — c-di-AMP degradation audit

Identity: A0A0H3GGY3, Listeria monocytogenes 10403S. The original seeded annotation payloads and both raw source files were preserved. All review actions were judged on the gene-specific biology; no new GO annotations were added.

Actual Falcon research was attempted with `just deep-research-falcon LISM4 pgpH` and failed with HTTP 403 authentication. No provider report was manufactured. Manual research used the primary papers and curated source statements cited below.

- [PMID:25583510 An HD-domain phosphodiesterase mediates cooperative hydrolysis of c-di-AMP to affect bacterial growth and virulence.] PubMed identity verified and cached full text examined, including HD-domain structural/biochemical evidence and 10403S genetic experiments.

The core is c-di-AMP hydrolysis, not its indirect envelope or stress phenotypes. A generic DHHA1-domain mapping does not establish a distinct nucleic-acid-binding role. Heme inhibition is characterized for Bacillus/Geobacillus proteins; ATPase activity is not generalized to S. aureus. pApA feedback was established for S. aureus GdpP and is not transferred to PgpH.

Module membership: `MODULE:bacterial_c_di_amp_signaling`, `pgph_pde_activity`.
