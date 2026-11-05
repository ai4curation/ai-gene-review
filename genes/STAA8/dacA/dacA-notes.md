# dacA curation notes

## 2026-11-04 — c-di-AMP module audit

Identity: UniProtKB:Q2FW92; Staphylococcus aureus subsp. aureus NCTC 8325. All 6 machine annotation payloads and raw UniProt/GOA files are preserved. No NEW annotation rows were added.

An actual `just deep-research-falcon STAA8 dacA` call failed with HTTP 403 authentication failure. No provider report was authored manually; this journal records manual source research.

QuickGO definitions checked on 2026-11-04 distinguish GO:0004016 (ATP to monomeric cAMP) from GO:0106408 (two ATP to c-di-AMP). The former is MODIFY, including experimental rows where present, because full-text product measurements support the latter. Electronic GO:0006171 cAMP biosynthesis mappings are removed where present. These are chemical identity corrections, not arguments from evidence-code rank. Source defects remain NOT_REPORTED.

The protein supplies the cyclase role in [bacterial c-di-AMP signaling](../../../modules/bacterial_c_di_amp_signaling.yaml). Membrane attachment applies to CdaA/DacA; DisA is soluble and chromosome-associated. No transport or host-response process is inferred merely from c-di-AMP-dependent phenotypes.

- [PMID:30668586 Inhibition of the Staphylococcus aureus c-di-AMP cyclase DacA by direct interaction with the phosphoglucosamine mutase GlmM.](https://pubmed.ncbi.nlm.nih.gov/30668586/): Assessed against the fetched primary publication. Full text available.

PMID:30668586 used LAC* genomic DNA, so its findings are applied to NCTC 8325 by sequence/family inference, not claimed as a direct strain-specific assay. The raw Q2FW92 sequence version 1 retains the paper’s D176/G177/T207 active-site and N166/T172/P173 interface residues (checked directly against the fetched sequence). The HAMAP CAUTION does not specify which feature fails propagation; no loss of catalysis is inferred from it. The source remains unchanged.

### PAINT trace and validation

The downloaded PAINT IBD.gaf contains PTN002149835, GO:0004016, IBD, dated 20171208, seeded by Q8Y5E4/O31854/Q45589. The inspected Q8Y5E4 and Q45589 publications establish dinucleotide chemistry, so the correction addresses the ancestral activity label rather than donor number. The first `just paint-losses` attempt could not resolve lineage losses because the PANTHER tree service timed out. A retry after service recovery succeeded: the PTHR34185 tree resolves Q2FW92 to PTN002149860, and `just paint-losses STAA8 dacA` reports no IRD or IKR loss on this gene’s lineage. This successful check supersedes the earlier UNKNOWN status; the chemical-product correction remains grounded in the primary assays.

Focused validation and HTML rendering pass. Generated HTML and local execution logs are excluded from the curation PR. The STAA8 DacA membrane location has an intentional annotation-coverage advisory: its positive sequence topology and homologous biochemical evidence support the core location, without manufacturing an extra annotation row to silence the warning.
