# B4MAQ2 (Dvir\GJ15622, Drosophila virilis Exportin-5) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 files were consulted for this re-review.

### Identity
- B4MAQ2 is 1238 aa, unreviewed (TrEMBL). UniProt lists isoform A and isoform B
  (EMBL EDW66311.1, KRF82632.1) on the same accession. It is the full-length
  canonical product, not a fragment. It aligns end to end with D. melanogaster
  Ranbp21/Exp5 Q9VWE7 (1241 aa): 85.9% identity over 1235 columns
  (file:DROVI/B4MAQ2/B4MAQ2-bioinformatics/RESULTS-rereview.md).
  Identity to human XPO5 Q9HAV4 is 38.5%, and to human XPO1 O14980 is 25.8%.
- PANTHER PTHR11223:SF3 (EXPORTIN-5) is shared with Q9VWE7, human XPO5 and
  S. pombe SPAC328.01c. Domains present: IBN_N (PF03810), Xpo1 (PF08389),
  Exportin-5 C-terminal (PF19273).

### Evolutionary grounding (PAINT, interpro/panther/PTHR11223/PTHR11223-paint.tsv)
- PTN000131749 (family root, both XPO1 and XPO5 subfamilies): nucleus, cytoplasm
  and GO:0005049 nuclear export signal receptor activity. Seeds include
  Q9HAV4 (XPO5), MGI:1913789 (Xpo5) and SGD:S000002743 (MSN5).
- PTN000131750 (exportin-5 clade): RNA binding and RNA export from nucleus.
- PTN000131787 (exportin-1 clade): ribosomal subunit export (GO:0000055, GO:0000056).
- PAINT did not propagate the human XPO5 experimental terms pre-miRNA export
  (GO:0035281), pre-miRNA binding or protein export from nucleus (GO:0006611)
  to any exportin-5 node. These omissions are treated as deliberate.

### Literature
- PMID:39098529 (fly Exp5 PAR-CLIP, full text): binds tRNAs, pre-tRNAs, miRNA
  precursors and some mRNAs/lncRNAs. Drosophila lacks Exportin-t. The paper
  cites earlier work showing that Exp5 knockdown lowers tRNA abundance.
  [PMID:39098529 "In Drosophila, knockdown of Exp5 is shown to reduce the tRNA abundance, indicating its roles in tRNA export (14)."]
- PMID:11777942 (human XPO5): binds RanGTP, shuttles, and exports dsRBD proteins.
  [PMID:11777942 "Like other known transport receptors, this Kap binds specifically to RanGTP,"]

### Changes from the previous review
- GO:0005049 changed from REMOVE to ACCEPT, and it is now the core MF. The GO
  definition says "The cargo can be either a RNA or a protein", and PAINT's
  root IBD includes exportin-5 seeds. The earlier review wrongly treated the
  term as specific to protein NES recognition by CRM1.
- GO:0006611 protein export from nucleus changed from REMOVE to
  MARK_AS_OVER_ANNOTATED. The row is ARBA plus InterPro only and PAINT did not
  propagate it, but human XPO5 does have protein-export evidence, so the
  claim is not contradicted.
- GO:0006886 changed from MODIFY (to RNA export) to MARK_AS_OVER_ANNOTATED,
  because the replacement term was already annotated.
- Dropped a supporting quote of the record's own DR GO line, which only
  restates the annotation.
- Added PMID:39098529 and PMID:11777942, and a new pairwise-identity analysis.

### Relative to review next
- D. melanogaster Ranbp21 (Q9VWE7), the same PANTHER subfamily SF3 and a
  Drosophila-genus ortholog. It has no review in the repo, and its GOA has
  only IBA/IEA rows despite the published CLIP work.
- Human XPO5 (Q9HAV4) has no review in the repo either.

### Family and modules
- interpro/panther/PTHR11223/PTHR11223-review.yaml places B4MAQ2 in SF3,
  consistent with this review. No disagreement.
- No module in modules/ covers Exportin-5, miRNA export or tRNA export.
