# dacA curation notes

## 2026-11-04 — c-di-AMP module audit

Identity: UniProtKB:Q2FW92; Staphylococcus aureus subsp. aureus NCTC 8325. All 6 machine annotation payloads and raw UniProt/GOA files are preserved. No NEW annotation rows were added in the initial audit; the follow-up below adds one supported cellular-component recommendation.

An actual `just deep-research-falcon STAA8 dacA` call failed with HTTP 403 authentication failure. No provider report was authored manually; this journal records manual source research.

QuickGO definitions checked on 2026-11-04 distinguish GO:0004016 (ATP to monomeric cAMP) from GO:0106408 (two ATP to c-di-AMP). The former is MODIFY, including experimental rows where present, because full-text product measurements support the latter. Electronic GO:0006171 cAMP biosynthesis mappings were initially removed where present; the review follow-up below supersedes that decision with MODIFY to a proposed specific process. These are chemical identity corrections, not arguments from evidence-code rank. Source defects remain NOT_REPORTED.

The protein supplies the cyclase role in [bacterial c-di-AMP signaling](../../../modules/bacterial_c_di_amp_signaling.yaml). Membrane attachment applies to CdaA/DacA; DisA is soluble and chromosome-associated. No transport or host-response process is inferred merely from c-di-AMP-dependent phenotypes.

- [PMID:30668586 Inhibition of the Staphylococcus aureus c-di-AMP cyclase DacA by direct interaction with the phosphoglucosamine mutase GlmM.](https://pubmed.ncbi.nlm.nih.gov/30668586/): Assessed against the fetched primary publication. Full text available.

PMID:30668586 used LAC* genomic DNA, so its findings are applied to NCTC 8325 by sequence/family inference, not claimed as a direct strain-specific assay. The raw Q2FW92 sequence version 1 retains the paper’s D176/G177/T207 active-site and N166/T172/P173 interface residues (checked directly against the fetched sequence). The HAMAP CAUTION does not specify which feature fails propagation; no loss of catalysis is inferred from it. The source remains unchanged.

### PAINT trace and validation

The downloaded PAINT IBD.gaf contains PTN002149835, GO:0004016, IBD, dated 20171208, seeded by Q8Y5E4/O31854/Q45589. The inspected Q8Y5E4 and Q45589 publications establish dinucleotide chemistry, so the correction addresses the ancestral activity label rather than donor number. The first `just paint-losses` attempt could not resolve lineage losses because the PANTHER tree service timed out. A retry after service recovery succeeded: the PTHR34185 tree resolves Q2FW92 to PTN002149860, and `just paint-losses STAA8 dacA` reports no IRD or IKR loss on this gene’s lineage. This successful check supersedes the earlier UNKNOWN status; the chemical-product correction remains grounded in the primary assays.

Focused validation and HTML rendering pass. Generated HTML and local execution logs are excluded from the curation PR. The initial STAA8 DacA core-only membrane assignment is superseded by the positive NEW recommendation recorded below.

## 2026-11-04 — PR #5997 review follow-up

Rechecked QuickGO for c-di-AMP and cyclic-dinucleotide biosynthesis. No specific BP was found. [GO:0009190](https://www.ebi.ac.uk/QuickGO/term/GO:0009190) defines a phosphate diester between positions on one sugar; it is not used as an unqualified replacement for dinucleotide synthesis. The shared proposal **cyclic di-AMP biosynthetic process**, under verified [GO:0009165 nucleotide biosynthetic process](https://www.ebi.ac.uk/QuickGO/term/GO:0009165), defines formation of 3′,3′-cyclic diadenosine monophosphate. The original GO:0006171 row now uses MODIFY with the matching NTR. CdaA/DacA performs the synthesis itself; this is not a process inferred from being necessary for a phenotype. Source corrections remain NOT_REPORTED.

Added one GO:0005886 plasma membrane NEW row with IC evidence: target HAMAP transmembrane features plus [PMID:30668586 Inhibition of the Staphylococcus aureus c-di-AMP cyclase DacA, "DacA has three N-terminal transmembrane helices"](https://pubmed.ncbi.nlm.nih.gov/30668586/). The primary experiment used LAC; application to NCTC 8325 remains an explicit inference. This positive recommendation supersedes the earlier core-only treatment. The gene now has seven rows, preserving all six original machine payloads.

Follow-up focused validation passes. Original machine annotation payloads and both raw-source SHA-256 hashes still match the preserved seed baseline.
