# ATRIP notes

## 2026-10-05 review (PAINT, affinage)

- Obligate ATR partner [PMID:11721054 "Thus, ATRIP and ATR are mutually dependent partners in cell cycle checkpoint signaling pathways."]; RPA-ssDNA recruitment [PMID:12791985 "The binding of ATRIP to RPA-coated ssDNA enables the ATR-ATRIP complex to associate with DNA and stimulates phosphorylation of the Rad17 protein that is bound to DNA."]; TopBP1 activation [PMID:18519640].
- The six ATR IPIs were changed to GO:0019901 protein kinase binding (core MF). The other 19 IPIs were removed under policy.
- Added NEW site of DNA damage (IDA, PMID:11721054); comparator ATR carries it by IDA.
- K63-polyubiquitin binding (IDA, PMID:24332808, abstract-only) is kept as non-core, deferring to the curator.
- DNA repair (IBA) and regulation of DSB repair (NAS) are non-core. The 20 Reactome nucleoplasm rows are accepted.
- Possible MF gap: direct RPA-ssDNA binding (yeast Ddc2/Lcd1 has damaged DNA binding IDA); raised as a suggested question.

## 2026-10-05 revision (reviewer round 1)

- Added NEW GO:0030674 protein-macromolecule adaptor activity (IDA, PMID:12791985) as the core MF. ATRIP bridges ATR to RPA-ssDNA and recruits TopBP1 (PMID:18519640). Affinage's grounding proposed GO:0060090. Single-stranded DNA binding is kept out, because ATRIP-alone ssDNA binding is contested (the affinage record cites PMID:14729973 and PMID:14724280, which are not cached).
- Comparator recorded (QuickGO, 2026-10-05): ATR (Q13535) carries GO:0090734 site of DNA damage by IDA.
- The ATR IPI rows now also quote UniProt's RPA-binding SUBUNIT clause. GO:0090734 cites UniProt's foci note. The GO:2000779 wording is aligned with the checkpoint thesis, and the affinage reference_review scopes VERIFIED to the 3 checked citations.
