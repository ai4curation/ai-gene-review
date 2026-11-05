# LOC732824 (ZmCCaMK, A0A804P0P6) review notes

## 2026-10-28 session

- fetch-gene resolved A0A804P0P6 (GeneID 732824, Zm00001eb200350); GOA keyed to that accession
  (8 IEA rows, all MF). No switch needed.
- A second TrEMBL entry, Q208N4 (from GenBank DQ403196, the ZmCCaMK cDNA used in the papers),
  is still active with an identical sequence (CRC64 83CA9566392266E9) and the same 8 IEA rows in
  QuickGO. Two TrEMBL entries for one gene; the literature-linked one is Q208N4. Recorded as a
  problem for the orchestrator, not as a source defect on this row set.
- No experimental GO annotations exist for either accession, although the maize literature
  contains direct kinase assays [PMID:22865912; PMID:27208250 "ZmCCaMK was found to phosphorylate His-ZmNAC84 in vitro ( Fig. 1C )."; PMID:41482925]
  and a YFP-fusion localization [PMID:22865912 "YFP–ZmCCaMK was localized in the nucleus, the cytoplasm, and the plasma membrane in maize mesophyll protoplasts"].
  This is a curation gap (literature not in GOA), not a knowledge gap.

## Decisions

- Core MF: GO:0004683 calcium/calmodulin-dependent protein kinase activity (ACCEPT IEA row).
  protein kinase activity and protein serine/threonine kinase activity rows MODIFY to it
  (GO:0004683 is_a GO:0004674 is_a GO:0004672, checked with runoak ancestors).
- kinase activity, transferase activity, nucleotide binding: TOO_GENERAL (entailed by
  GO:0004683 / ATP binding kept elsewhere).
- calcium ion binding: ACCEPT (three EF-hands, PROSITE EF_HAND_1 x3; Ca2+ dependence of the
  kinase is part of its mechanism).
- ATP binding: KEEP_AS_NON_CORE.
- NEW: nucleus (IDA, PMID:22865912). Cytoplasm and plasma membrane also seen with the 35S
  YFP fusion; not added (overexpression, diffuse cytoplasmic signal, and orthologs are nuclear).
  Mentioned in suggested experiments instead.
- NEW: calmodulin binding (IDA, PMID:33864702, abstract states Ser-67 phosphorylation
  regulates Ca2+/CaM binding of ZmCCaMK). Abstract only; kept conservative.
- No NEW process terms. ABA- and BR-induced antioxidant defence evidence is RNAi /
  overexpression plus a downstream substrate (ZmNAC84). The kinase does perform a step
  (phosphorylating NAC84) in an ABA-triggered cascade, so GO:0009738 abscisic acid-activated
  signaling pathway is plausible, but it is neither added as a NEW row nor put in
  core_functions (single-lab, protoplast-based; raised as a suggested question).
- Root symbiosis (AM) is the canonical ortholog function but untested in maize; not asserted.
