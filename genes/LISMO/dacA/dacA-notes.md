# dacA curation notes

## 2026-11-04 — c-di-AMP module audit

Identity: UniProtKB:Q8Y5E4; Listeria monocytogenes EGD-e. All 8 machine annotation payloads and raw UniProt/GOA files are preserved. No NEW annotation rows were added.

An actual `just deep-research-falcon LISMO dacA` call failed with HTTP 403 authentication failure. No provider report was authored manually; this journal records manual source research.

QuickGO definitions checked on 2026-11-04 distinguish GO:0004016 (ATP to monomeric cAMP) from GO:0106408 (two ATP to c-di-AMP). The former is MODIFY, including experimental rows where present, because full-text product measurements support the latter. Electronic GO:0006171 cAMP biosynthesis mappings are removed where present. These are chemical identity corrections, not arguments from evidence-code rank. Source defects remain NOT_REPORTED.

The protein supplies the cyclase role in [bacterial c-di-AMP signaling](../../../modules/bacterial_c_di_amp_signaling.yaml). Membrane attachment applies to CdaA/DacA; DisA is soluble and chromosome-associated. No transport or host-response process is inferred merely from c-di-AMP-dependent phenotypes.

- [PMID:25605729 Structural and biochemical analysis of the essential diadenylate cyclase CdaA from Listeria monocytogenes.](https://pubmed.ncbi.nlm.nih.gov/25605729/): Assessed against the fetched primary publication. Full text available.

### PAINT trace and validation

The downloaded PAINT IBD.gaf contains PTN002149835, GO:0004016, IBD, dated 20171208, seeded by Q8Y5E4/O31854/Q45589. The inspected Q8Y5E4 and Q45589 publications establish dinucleotide chemistry, so the correction addresses the ancestral activity label rather than donor number. The first `just paint-losses` attempt could not resolve lineage losses because the PANTHER tree service timed out. A retry after service recovery succeeded: the PTHR34185 tree resolves Q8Y5E4 to PTN002437163, and `just paint-losses LISMO dacA` reports no IRD or IKR loss on this gene’s lineage. This successful check supersedes the earlier UNKNOWN status; the chemical-product correction remains grounded in the primary assays.

Focused validation and HTML rendering pass. Generated HTML and local execution logs are excluded from the curation PR.
