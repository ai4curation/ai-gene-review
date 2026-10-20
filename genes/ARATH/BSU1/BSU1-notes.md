# BSU1 (At1g03445, UniProtKB:Q9LR78) curation notes

Session 2026-10-05/06 (brassinosteroid_signaling module curation).

- Identity checked: BSU1_ARATH, Q9LR78.
- Falcon deep research attempted; HTTP 402, no report.
- Kelch-repeat PPP Ser/Thr phosphatase, nuclear [PMID:14977918 "BSU1 encodes a nuclear-localized serine-threonine protein phosphatase with an N-terminal Kelch-repeat domain"].
- Key mechanism: dephosphorylates BIN2 pTyr200 [PMID:19734888 "BSU1 inactivates the GSK3-like kinase BIN2 (BR-insensitive 2) by dephosphorylating a conserved phospho-tyrosine residue (pTyr 200)"].
- Activated by CDG1 Ser764 phosphorylation [PMID:21855796 "CDG1 in turn phosphorylates S764 to activate BSU1, which inactivates BIN2 by dephosphorylating Y200 of BIN2."].
- NEW: GO:0004725 protein tyrosine phosphatase activity (IDA, PMID:19734888). Core function uses this term.
- IBA GO:0009966 too general -> MODIFY to GO:1900459.

## 2026-10-06 review follow-up (PR #4394)
- Direct BES1 dephosphorylation (Mora-Garcia 2004 interpretation) is not supported in vitro: [PMID:19734888 "However, BSU1 does not interact with or effectively dephosphorylate BZR2/BES1 in vitro and the biochemical function of BSU1 remains unknown"]; [PMID:19734888 "These results indicate that BSU1 inhibits BIN2 kinase activity but does not dephosphorylate pre-phosphorylated BZR1 in vitro."]. Recorded as a DISPUTED finding_review on PMID:14977918; removed from description and core function 2.
- GO:0004722 kept: [PMID:19734888 "show manganese-dependent phosphatase activities (Supplementary Information, Fig. S2b, c)"].
- GO:0008138 (protein tyrosine/serine/threonine phosphatase activity) considered as a single replacement for the GO:0004722 + GO:0004725 pair; kept the pair because both activities are each directly evidenced and BSU1 is a PPP-fold (not DSP-fold) enzyme.
