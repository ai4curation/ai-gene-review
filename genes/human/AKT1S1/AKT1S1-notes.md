# AKT1S1 (Q96B36) review notes

## 2026-10-04: PAINT/affinage review

PRAS40 is a well-characterized substrate-competitive inhibitor of mTORC1.
- **Mechanism:** [PMID:17510057 "We, therefore, propose that PRAS40 regulates mTORC1 kinase activity by functioning as a direct inhibitor of substrate binding."]
- **Structure:** [PMID:29236692 "reveals PRAS40 inhibits both substrate-recruitment sites"]
- **Release by insulin:** [PMID:17386266 "Insulin stimulates Akt/PKB-mediated phosphorylation of PRAS40, which prevents its inhibition of mTORC1 in cells and in vitro."]
- **Affinage:** an accurate summary.
- **Stale record:** PMID:17386266 was in the old record format and was re-fetched.

Decisions:
- **14-3-3 interaction rows (YWHAB, YWHAH, YWHAZ, and yeast BMH1 used as an affinity matrix): MODIFY to GO:0071889 14-3-3 protein binding.** The comparator check is positive: in human, the 14-3-3 clients RPTOR, IRS2, HDAC7 and CFTR carry GO:0071889, so client binding is conventionally annotated. BAD and FOXO3 happen not to carry it.
- **RPTOR interaction rows:**
  - Low-throughput papers (17386266, 19446321, 29236692): MODIFY to GO:0030291. There is no TORC1-binding MF term, and raptor binding is the inhibitory mechanism.
  - OpenCell (35271311) and the astrin paper (23953116, abstract-only and silent on PRAS40 activity): REMOVE. The source shows association, not inhibition. The astrin row changed in round 1 of PR #3965.
- **Neurotrophin TRK signaling (InterPro IEA): MARK_AS_OVER_ANNOTATED.** PRAS40 is a generic downstream Akt substrate.
- **Kept as non-core:** apoptosis regulation (IEA/ISS) and cell size (IDA).
- **Nucleoplasm (Reactome, HSF1 reaction): MARK_AS_OVER_ANNOTATED** (changed in round 1). PRAS40 appears there only as a modeled subunit of mTORC1, and UniProt records cytosol only.
