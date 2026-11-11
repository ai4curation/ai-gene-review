# G1TUN6 (rabbit UBE2L6) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This review did not use the ProtNLM2 predictions or the prediction-evidence files.

### Identity
- G1TUN6 is a 153 aa TrEMBL entry (PE 3), gene UBE2L6, with CTD 9246 (the human UBE2L6 gene). It has a UBC core (2..149) and ACT_SITE Cys86.
- It is full length. The global alignment to human O14933 (153 aa) has no gaps, 79.7% identity, and Cys86 aligns to Cys86. Identity to the UBE2L3 paralog (P68036) is 52.3% ([file:RABIT/G1TUN6/G1TUN6-bioinformatics/RESULTS.md]). It is not a fragment, isoform or alternative gene model.

### Evolutionary grounding
- UniProt gives only the PANTHER family PTHR24067 with no subfamily. The PANTHER 19 web service places human UBE2L6 in PTHR24068:SF43 "UBIQUITIN_ISG15-CONJUGATING ENZYME E2 L6", which looks like a family renumbering between releases. UBE2L3 sits in separate subfamilies (SF67/SF116).
- PAINT node PTN000631065 (Mammalia), seeded by human UBE2L6 and mouse Ube2l6, carries ISG15 transferase activity and ISG15-protein conjugation. The broad E2 node PTN002514495 carries ubiquitin conjugating enzyme activity. Rabbit has no IBA rows, apparently because it is not a PANTHER genome.
- PAINT did not propagate innate immune response to the mammalian UBE2L6 node, although human O14933 has a UniProt IDA for it. I treat that omission as deliberate.

### Literature
- [PMID:15131269 "We therefore conclude that UbcH8 serves as a major E2 enzyme for ISG15 conjugation in vivo ."]. The same paper shows a ubiquitin E2 role: ["Rsp5p catalyzed efficient polyubiquitination of WBP2 in the presence of E1 Ub and UbcH8"]. UbcH7 (UBE2L3) forms only about 5% as much ISG15 thioester as UbcH8, so ISG15 functions should not be transferred to the paralog.
- The human innate immune response IDA comes from PMID:28724761. That paper's UBE2L6 result is negative: ["We also observed that loss of ISGylating enzymes (UBE1L and UBE2L6) did not affect the HEV type I IFN sensitivity."]. This is a donor-side problem, recorded in suggested_questions.

### Changes from the previous review
- ATP binding and ligase activity: REMOVE kept. UniProt quotes based only on ARBA were replaced with primary literature.
- ubiquitin conjugating enzyme activity: KEEP_AS_NON_CORE changed to ACCEPT. Ubiquitin E2 activity is demonstrated for the ortholog, so it is now a second core function.
- ubiquitin-like protein transferase activity: ACCEPT changed to MODIFY, with GO:0042296 and GO:0061631 as replacements (correct but general).
- ISG15-protein conjugation and ISG15 transferase activity: ACCEPT, now supported by the primary paper and the PAINT node rather than the deep-research text.
- innate immune response: KEEP_AS_NON_CORE changed to MARK_AS_OVER_ANNOTATED, because the donor evidence is negative and PAINT did not propagate the term.
- The description was rewritten. The deep-research file is kept in references but is no longer used as support.

### Relative
- Human UBE2L6 (O14933) is the closest characterised ortholog. It is inside PAINT node PTN000631065 with this gene and is the IDA donor. The repo has no human review of UBE2L6 (genes/human/UBE2L6 does not exist).
- Family review interpro/panther/PTHR24067: it is a single coarse "subfamily" grouping and assigns no SF to G1TUN6, so there is no disagreement with it. The PTHR24067 to PTHR24068 renumbering in PANTHER 19 is worth noting.
- Module: modules/ubiquitin_transfer_relay.yaml (E1-E2-E3 relay, which mentions ISG15 reuse). There is no ISGylation-specific module.
