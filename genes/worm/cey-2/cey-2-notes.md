# cey-2 review notes

## 2026-10-28: initial review

- Fetched with `just fetch-gene worm cey-2`; UniProt P91306 (TrEMBL, unreviewed),
  WormBase F46F11.2 / WBGene00000473. Five GOA rows.
- No deep-research provider available; manual literature survey in
  `cey-2-deep-research-manual.md`.
- Papers read in full: PMID:16247027 (Audhya 2005, CAR-1 TAP identifies CEY-2),
  PMID:25378320 (Arnold 2014, CEY family characterization), PMID:39423228 (Hayden
  2024, memory screen). PMID:16221731 (Boag 2005) is abstract-only.

### Decisions

- `GO:0003676 nucleic acid binding` (IBA + IEA): ACCEPT. CSD with RNP1/RNP2 motifs;
  no direct binding assay for CEY-2, and the RIP in PMID:25378320 found no specific
  enrichment, so I do not refine to `mRNA binding` on the existing rows. Both rows
  get the same action (consistency rule).
- `GO:0005634 nucleus` (IBA, is_active_in): REMOVE. Target-specific experimental
  evidence (PMID:25378320) that CEY proteins, including CEY-2, are only cytoplasmic
  and do not accumulate in the nucleus even after xpo-1 RNAi. The PAINT nucleus node
  rests on vertebrate YBX1/YBX2-type proteins with known nuclear roles; the
  nematode germline CEY-2 has diverged in localization. Flag for expert check.
- `GO:0010468 regulation of gene expression` (IBA): MODIFY to `GO:0010608
  post-transcriptional regulation of gene expression`. Two lines: exclusive
  cytoplasmic localization, and membership of a maternal mRNP with reduced maternal
  mRNA levels in cey-2,-3 mutants. Not refined further (e.g. mRNA stabilization) since
  only abundance, not decay rate, was measured.
- `GO:1990904 ribonucleoprotein complex` (IDA, PMID:16247027): ACCEPT. Direct TAP-MS.
- NEW `GO:0005737 cytoplasm` (IDA, PMID:25378320): GFP and immunostaining.
- No NEW process terms: the germline proliferation, apoptosis, oocyte maturation
  and memory data are RNAi/mutant phenotypes (necessity, not participation), and
  most are for cey-2,-3 combined.
