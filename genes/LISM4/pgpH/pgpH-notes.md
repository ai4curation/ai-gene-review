# pgpH functional review

## 2026-11-04 — c-di-AMP degradation audit

Identity: A0A0H3GGY3, Listeria monocytogenes 10403S. The original seeded annotation payloads and both raw source files were preserved. All review actions were judged on the gene-specific biology; no new GO annotations were added.

Actual Falcon research was attempted with `just deep-research-falcon LISM4 pgpH` and failed with HTTP 403 authentication. No provider report was manufactured. Manual research used the primary papers and curated source statements cited below.

- [PMID:25583510 An HD-domain phosphodiesterase mediates cooperative hydrolysis of c-di-AMP to affect bacterial growth and virulence.] PubMed identity verified and cached full text examined, including HD-domain structural/biochemical evidence and 10403S genetic experiments.

The core is c-di-AMP hydrolysis, not its indirect envelope or stress phenotypes. PgpH uses an HD domain rather than the GdpP DHH/DHHA1 architecture. Its ppGpp inhibition is supported by PMID:25583510; pApA feedback established for S. aureus GdpP is not transferred to PgpH.

Module membership: `MODULE:bacterial_c_di_amp_signaling`, `pgph_pde_activity`.

## 2026-11-05 — PR #5997 evidence follow-up

The hydrolysis evidence supports the catalytic assignment: [PMID:25583510 "The PgpH HD domain bound c-di-AMP with a high affinity and hydrolyzed it into 5′-pApA."]

Removed unrelated DHHA1 prose from these notes and retained the distinction between PgpH-specific evidence and GdpP regulation.
