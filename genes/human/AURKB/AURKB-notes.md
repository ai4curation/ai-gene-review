# AURKB notes

## 2026-10-05 review (PAINT, affinage)

- Catalytic subunit of the chromosomal passenger complex (CPC) [file:human/AURKB/AURKB-uniprot.txt "CC       passenger complex (CPC), a complex that acts as a key regulator of"]. Corrects kinetochore-microtubule attachments, for example via Ska complex exclusion [PMID:22371557 "In this paper, we show that Aurora B negatively regulates the localization of the Ska complex to KTs and that recruitment of the Ska complex to KTs depends on the KMN network."], and enforces the abscission checkpoint.
- GO:0004712 (Ser/Thr/Tyr kinase) is changed to GO:0004674. UniProt records only Ser and Thr reactions.
- Spindle-pole and centrosome IBA/IEA rows are Aurora-A-type locations inherited at the family node, so they are kept as non-core.
- The p53 rows (PMID:20959462) are kept as non-core. The UV-response and B-cell apoptosis rows from the same paper are UNDECIDED, because neither topic appears in the cached full text.
- Two rows are marked over-annotated: G2/M transition (from a cGAS phosphorylation paper) and telomere maintenance (an RNAi screen hit).
- All 62 GO:0005515 IPI rows are removed under policy. The CPC partners (INCENP, BIRC5, CDCA8) are covered by GO:0032133.

## 2026-10-05 revision (reviewer round 1)

- GOA has a NOT|enables GO:0004674 row (IDA, PMID:26829474). It is removed: the paper's wild-type data show acetylation-stimulated kinase activity [PMID:26829474 "As reflected by H3 phosphorylation, TIP60 mediated K215 acetylation robustly stimulated Aurora B activity (Fig. 3c and d; Supplementary Fig. 5k)."]. The builder previously ignored the `negated` flag. An audit of all opus-5-5 campaign genes on main found no other affected rows.
- The histone-kinase outputs (H1.4 S27, H3 S10/S28) are deliberately subsumed under GO:0004674 in core_functions. GO:0140197 is accepted at row level.
