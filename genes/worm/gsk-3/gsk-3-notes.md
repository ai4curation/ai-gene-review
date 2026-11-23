# gsk-3 (C. elegans, Q9U2Q9) review notes

## Provenance / process

- Deep research: not run. The falcon provider is known to fail for this batch (HTTP 402
  payment-required), so no `-deep-research-*.md` file exists. These notes are compiled directly
  from cached publications (`publications/PMID_*.md`) plus the UniProt record.
- `just fetch-gene-pmids worm gsk-3` cached all 11 GOA PMIDs. Extra PMIDs cached with
  `just fetch-pmid`: 16251270 (SKN-1), 11463373 (mesendoderm), 15572126 (ABar spindle),
  35635101 (gskl-1/gskl-2 sperm paralogs; context only), 17959600 (lithium; not used).
- Full text available only for PMID:12023307, PMID:20126385, PMID:19123269, PMID:26780296.
  All other papers are abstract-only, so experimental annotations from them are deferred to the
  curator rather than overruled.
- Older literature calls the gene `sgg-1` (e.g. Korswagen 2002, Maduro 2001).

## Identity / family

- 362 aa CMGC kinase, GSK-3 subfamily; kinase domain 36-320, catalytic Asp161 (UniProt FT).
  PANTHER PTHR24057:SF0 (default root subfamily). The family review
  (`interpro/panther/PTHR24057/PTHR24057-review.yaml`) aligns the catalytic K65/D161 and the
  priming-phosphate pocket Arg76 (GSK3B R96 equivalent) as conserved in worm GSK-3.
- Divergent nematode-specific paralogs gskl-1/gskl-2 (SF18) are sperm GSK-3s required for sperm
  motility and the post-fertilisation meiosis II signal [PMID:35635101 "Both genes encode
  functionally redundant sperm glycogen synthase kinase, type 3 (GSK3) protein kinases"]. The
  "oocyte meiosis" role sometimes attributed to GSK-3 in worm belongs to these paralogs, not to
  gsk-3 itself; gsk-3's documented germline/oocyte role is OMA-1 turnover at the
  oocyte-to-embryo transition.

## Kinase activity and substrates

- OMA-1: MBK-2 priming at T239 then GSK-3 at T339 in vitro [PMID:16289132 "Phosphorylation at
  T239 facilitates subsequent phosphorylation of OMA-1 by another kinase, GSK-3, at T339 in
  vitro"]; both sites needed for timely degradation [PMID:16289132 "Phosphorylation at both T239
  and T339 are essential for correctly-timed OMA-1 degradation in vivo"]. This is the classic
  primed (S/T-x-x-x-pS/pT-like) GSK-3 mode.
- gsk-3 mutants stabilise OMA-1 [PMID:16343905 "Mutations in four conserved protein kinase
  genes-mbk-2/Dyrk, kin-19/CK1alpha, gsk-3, and cdk-1/CDC2-cause stabilization of OMA-1
  protein"]; degradation is CUL-2/ZYG-11 dependent.
- SKN-1: [PMID:16251270 "in the absence of stress, phosphorylation by glycogen synthase kinase-3
  (GSK-3) prevents SKN-1 from accumulating in nuclei and functioning constitutively in the
  intestine"]; [PMID:16251270 "GSK-3 inhibits SKN-1 activity in the intestine"]. No GO term for
  this currently on gsk-3.
- PMID:23431196 (IDA kinase; WRM-1 cortical release) is abstract-only and the abstract does not
  mention GSK-3; deferred to WormBase curator.

## Wnt signalling — the unusual worm wiring

1. Positive role in the Wnt/beta-catenin asymmetry pathway (MOM-2/MOM-5 -> WRM-1/LIT-1 -> POP-1;
   SYS-1/POP-1 asymmetry). gsk-3 RNAi blocks endoderm induction like mom-2/Wnt
   [PMID:10444600 "Reducing the function of Wnt pathway genes, including a newly identified
   GSK-3beta homolog called gsk-3, disrupts endoderm induction"]. Korswagen notes this positive
   role [PMID:12023307 "both APR-1 and the GSK3β-like protein SGG-1 have been shown to function
   as positive, rather than negative regulators of a Wnt pathway in the early embryo"].
   Maduro 2001: [PMID:11463373 "SGG-1/GSK-3beta kinase acts both as a Wnt-dependent activator of
   endoderm in EMS and an apparently Wnt-independent repressor of the meds in the C lineage"].
   Comparator check (QuickGO, taxon 6239): GO:0001714 endodermal cell fate specification is
   carried by mom-2, mom-5, wrm-1, apr-1, lit-1, mom-4, dsh-2, mig-5, src-1 — the other
   signalling components in the same role — but not gsk-3. This is a genuine gap, so NEW
   proposed.
2. Spindle orientation branch (non-transcriptional). [PMID:10444600 "gsk-3 represents a branch
   point in the control of endoderm induction and spindle orientation"]; ABar
   [PMID:20126385 "ABar spindle positioning required MOM-2/Wnt and GSK-3 function, but not
   WRM-1/β-catenin or POP-1/TCF"]. Supports GO:0060069 and GO:0000132.
3. Wnt -> CED-10/Rac cytoskeletal branch for engulfment and DTC migration
   [PMID:20126385 "Animals lacking MOM-5/Fz, GSK-3, or APR-1 showed both persistent cell corpses
   and misshapen gonads"]. Non-core.
4. Negative regulation of BAR-1/beta-catenin canonical Wnt (EGL-20/Q lineage, vulva).
   PRY-1/Axin binds SGG-1 (Y2H) [PMID:12023307 "PRY-1 also binds the GSK3β homolog SGG-1"];
   SGG-1 overexpression phenocopies PRY-1 overexpression [PMID:12023307 "overexpression of SGG-1
   (like overexpression of PRY-1) induced anterior migration of the QL daughter cells"];
   conclusion [PMID:12023307 "a highly divergent destruction complex consisting of PRY-1, SGG-1,
   and APR-1 regulates BAR-1/beta-catenin signaling in C. elegans"]. Caveat in paper: RNAi is
   embryonic lethal, so loss-of-function in Q lineage not tested; overexpression may titrate.
   Second Axin AXL-1 also binds GSK-3 (IPI 17601533). Vulval IMP (PMID:16930586) abstract-only.

### Verdict for PTHR24057 family scoping

- GO:0090090 (negative regulation of canonical Wnt): supported for worm gsk-3 by IMP (vulva,
  deferred), overexpression (Q lineage) and Axin binding. IBA is acceptable for the worm leaf,
  consistent with the family review scoping SF0 metazoans in. But it is not the whole story:
  in the embryo gsk-3 acts positively in the Wnt/beta-catenin asymmetry pathway.
- GO:0030877 (beta-catenin destruction complex): plausible but NOT experimentally established
  in worm — only binary Y2H with PRY-1/AXL-1 plus inference; no complex isolated, and no IBA
  reaches worm (PAINT places it at the euteleost GSK3B node). Not added. Family review's listing
  of SF0 as applicable is reasonable but rests on fly/vertebrate data, not worm.
- PTN001173193 TOO_DEEP assessment (Metazoa+Choanoflagellida) is unaffected: worm is within
  Eumetazoa, so moving the node to PTN001173194 would keep the worm IBA.
- Tau-protein kinase (EC mapping + ISS): over-annotation, as scoped in the family review. Worm
  has a tau/MAP2-like protein PTL-1, but no evidence GSK-3 phosphorylates it.
