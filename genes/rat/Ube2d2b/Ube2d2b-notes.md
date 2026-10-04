# Ube2d2b (rat, P70711) notes

## Re-review 2026-10-04

**GOA changes.** One new row: GO:0005737 cytoplasm (IBA, GO_REF:0000033, is_active_in; PAINT node PTN008604282). No retired rows; the other 17 rows are unchanged.

**PENDING resolved.** GO:0005737 cytoplasm -> ACCEPT. The documented UBE2D substrates are largely cytoplasmic [UniProtKB:P70711 "Involved in the signal-induced conjugation and subsequent degradation of NFKBIA"; "Mediates ubiquitination of PEX5 and SQSTM1 and autoubiquitination of STUB1 and TRAF6."], and rat Ube2d2b sits inside the UBE2D clade with no divergence.

**Actions changed.**
- GO:0085020 K6-, GO:0044314 K27-, GO:0035519 K29- and GO:0070534 K63-linked ubiquitination (all ISO from human UBE2D4, Q9Y2X8): ACCEPT -> KEEP_AS_NON_CORE. QuickGO shows that every linkage-specific IDA on UBE2D4 (K6, K11, K27, K29, K48, K63) comes from one E3-free in vitro survey [PMID:20061386 "Because this study was performed in the absence of an E3 enzyme, our data indicate that the E2 enzymes are capable of directing the ubiquitination process to distinct subsets of ubiquitin lysines, depending on the specific E2 utilized."]. That shows linkage capacity, not a physiological pathway, so these minor-linkage terms are not core. The K11 rows were already MARK_AS_OVER_ANNOTATED, and that grading was kept because the PTHR24068 family review grades the K11 node as WRONG_NODE. K48 stays ACCEPT (the degradative linkage, consistent with GO:0006511).
- Each of these ISO rows now has a `propagation_review` naming the donor.

**Corrections.**
- The ISO reviews named the donor as "human UBE2D2". The WITH/FROM accession Q9Y2X8 is UBE2D4; this is corrected in the K6/K27/K29/K48/K63 rows.
- The core-function UniProt quote ("Catalyzes the covalent attachment of ubiquitin to other proteins; pathway protein ubiquitination.") was not verbatim; replaced with the FUNCTION and PATHWAY lines.
- The IEP cadmium and arsenite rows (MARK_AS_OVER_ANNOTATED, unchanged) now quote the abstracts, which show only reduced Ube2d expression [PMID:21467746 "Cd markedly decreased the expression of Ube2d1, Ube2d2, Ube2d3 and Ube2d4 prior to the appearance of cytotoxicity in the NRK-52E cells."; PMID:24212999 "suppressed Ube2d1, Ube2d2 and Ube2d4 expression, but not Ube2d3"].
- `status` set to COMPLETE.

**Open questions.** The rat Ube2d2a/Ube2d2b naming does not map one-to-one onto the "Ube2d2" measured in the toxicology papers; which rat locus they measured should be confirmed.
