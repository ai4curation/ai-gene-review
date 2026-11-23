# CycA (P14785) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: P14785 is the reviewed canonical CycA product (isoform A, 491 aa), FBgn0000404,
CG5940. It has its own folder (`CycA__P14785`) because `genes/DROME/CycA/` holds the
M9NFR3 (isoform C) record. No ProtNLM2 output or prediction-evidence files were opened
or used.

### Inputs
- `just fetch-gene DROME P14785 --alias CycA__P14785`: 38 GOA rows seeded. PMID:27170181
  was rate-limited on the first fetch and re-cached afterwards with full text.
- Deep research (`just deep-research-falcon ... --fallback perplexity-lite`) FAILED:
  falcon gave "Exception: Failed to authenticate" and perplexity gave HTTP 401
  insufficient_quota. No deep-research file exists. The review is based on the cached
  publications listed below.
- Literature read: PMID:2564316, 2139805, 8428595, 9210381, 15203007, 16854973, 11350926,
  11369230, 11027291, 10607563, 17431409, 1531147, 18291653, 22024320, 27170181,
  24019759, 26096977, 28484036, 28829944, 16139215, 38944040. Several are abstract-only.

### Evolutionary grounding
- PANTHER 19.0: PTHR10177:SF593 "G2_MITOTIC-SPECIFIC CYCLIN-A" (panther.obo). This is
  the same subfamily as the other A-type cyclins.
- PAINT (`interpro/panther/PTHR10177/PTHR10177-paint.tsv`): PTN000019791 carries IBDs for
  GO:0016538, GO:0005634, GO:0005737, GO:0000082 and GO:0000307. FBgn0000404 is a seed
  for the first four. CycA receives IBA rows for all of these except GO:0000307: the
  holoenzyme IBD is at the same node, but no fly IBA row is present in the current GOA
  file.
- PTN000020367 (taxon Bilateria), seeded by human CCNA2 and mouse Ccna2, gives cyclin
  A2-CDK2 complex. The fly experiment PMID:11027291 shows CycA-Cdc2c (Cdk2) complexes with
  H1 kinase activity, so this row is kept as non-core. The main partner is Cdk1.
- PTN007424001 gives MTOC. Its seeds are only B-type cyclins and cyclin F. PMID:1531147
  contrasts CycA (on chromatin) with CycB (at centrosomes and poles), so this row is
  marked over-annotated.

### What is experimentally established in Drosophila (for transfer)
- Cdk regulatory subunit: binds Cdc2 and Cdc2c and is needed for their H1 kinase activity
  in complex with it (PMID:11027291, PMID:10607563). The hydrophobic patch
  (M235/L239/W242) binds Frs (PMID:17431409).
- Mitotic entry (G2/M), acting synergistically with CycB (PMID:8428595, PMID:2139805,
  PMID:11350926). The C-terminal cyclin box region is enough for this.
- Essential mitotic function: CycA-Cdk activity inhibits Fzr/Cdh1 in G2, which prevents
  premature APC/C-Fzr degradation of CycB, CycB3 and Stg (PMID:15203007,
  PMID:16854973).
- CycA destruction is required for sister chromatid disjunction (PMID:11369230). This is
  regulation, not participation.
- CycA has S-phase-promoting activity, restrained in G1 (PMID:9210381). This is non-core;
  cyclin E is the physiological G1/S cyclin.
- Localization: cytoplasmic in interphase, nuclear from prophase. In germ cells it is on
  the spectrosome/fusome (PMID:22024320, PMID:27170181).

### Decisions worth flagging
- All six GO:0005515 rows were removed under the protein-binding policy. The partners
  are Frs/Z600 (an inhibitor), Cdk1 (already captured by GO:0016538) and Fzy (CycA is
  the APC/C substrate).
- Regulation of exit from mitosis (PMID:16854973) was MODIFIED to GO:1905785. The
  abstract describes failure to enter terminal mitoses because of premature APC/C-Fzr
  activity. The full text is not cached.
- Positive regulation of stem cell differentiation (PMID:28484036) was marked
  over-annotated. CycA is the substrate stabilized by Bam-Otu, and UniProt's curated
  phenotype says CycA RNAi has no GSC differentiation effect.
- Synapse (PMID:26096977) and asymmetric neuroblast division (PMID:16139215) are
  UNDECIDED, because the abstracts do not show the CycA data.
- The core function cites in_complex GO:0000307. It was not added as NEW because it is
  an ancestor of GO:0097124, which the gene already carries. This leaves one validation
  warning.
