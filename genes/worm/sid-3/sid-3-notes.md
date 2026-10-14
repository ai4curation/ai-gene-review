# sid-3 (Q10925) review notes

Deep research was skipped: falcon times out in this environment and perplexity-lite is unavailable.
This review relies on cached full-text papers (PMID:22912399, PMID:28874466, PMID:28874467).

- ACK-family non-receptor tyrosine kinase (kinase, SH3 and CRIB domains) [PMID:22912399 "This domain composition is present in the activated Cdc-42–associated kinase (Ack) family of cytoplasmic tyrosine kinases"].
- Required in recipient cells for dsRNA import. Cell-autonomous RNAi is intact [PMID:22912399 "Nevertheless, these results clearly demonstrate that sid-3 mutants are not defective in the execution of RNAi."].
- Kinase activity is required: the K139A mutant does not rescue [PMID:22912399 "Thus, the kinase activity of SID-3 is essential to enable efficient import of dsRNA into C. elegans cells."].
- Required for an early, pre-replication step of Orsay virus infection, and kinase activity is needed for this [PMID:28874467 "Our experiments suggest that the kinase activity of SID-3 is important for its ability to promote Orsay virus infection."].
- sid-3 mutants derepress STA-1-bound antiviral genes [PMID:28874466 "genes upregulated in sid-3 mutants, including those shared with sta-1, were enriched for STA-1 binding by ChIP-seq"].

Decisions:
- GO:0035194 (ncRNA-mediated PTGS, IMP): MODIFY to GO:0033227 dsRNA transport.
  SID-3 is needed for dsRNA import, not for the silencing machinery.
- Plasma membrane IBA: kept as non-core. ACK kinases associate with membranes and vesicles, but
  SID-3 has only been seen in the cytoplasm.
- NEW GO:0050687 negative regulation of defense response to virus (IMP, PMID:28874466). This matches
  the module annoton.
