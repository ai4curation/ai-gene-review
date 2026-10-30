# vab-1 review notes

## Session 1 (initial review)

- Fetched with `just fetch-gene worm vab-1`; UniProt O61460 (VAB1_CAEEL) confirmed. GOA has
  29 rows; the seeder collapsed two identical GO:0010172 IMP PMID:9506518 rows (UniProt and
  WB) into one, giving 28 existing_annotations.
- No deep-research provider available; literature summarised in vab-1-deep-research-manual.md.
- Abstract-only cache: PMID:9506518, 10409513, 10619431, 16267094, 19853560. Full text:
  12533508, 18555774, 26903502, 22363657.
- PMID:22363657 was flagged by the workflow as a key VAB-1 paper, but it is the RHGF-2
  RhoGEF paper; it mentions VAB-1 only as an unpublished Y2H hit with MPZ-1
  [PMID:22363657 "another positive in our yeast two-hybrid screening with MPZ-1 was VAB-1 (unpublished data)"].
  Recorded with LOW relevance.

### Decisions

- Kinase MF: protein kinase activity (IEA) and protein tyrosine kinase activity (IDA, IEA)
  are true but general; MODIFY to transmembrane receptor protein tyrosine kinase activity
  (GO:0004714), which the gene already carries (IBA/IEA).
- Ephrin receptor activity (GO:0005003) ACCEPT: EFN-1 is a ligand [PMID:10619431].
  GO:0004714 kept as well (ACCEPT) because VAB-1 also acts as the MSP receptor, which is not
  ephrin signalling.
- GO:0007169 kept (ACCEPT) for the same reason: MSP-VAB-1 signalling has no specific GO term.
- Oocyte maturation (IMP) -> MODIFY to negative regulation of oocyte maturation (GO:1900194):
  vab-1 nulls mature faster in the absence of sperm [PMID:12533508].
- Axonogenesis and regulation of axon guidance -> MODIFY to axon guidance (GO:0007411); VAB-1
  is a guidance receptor (loss: overextension; gain: early termination) [PMID:16386725].
- Embryo development (IMP) -> MODIFY to morphogenesis of embryonic epithelium (GO:0016331).
- Bare protein binding: VPR-1 row MODIFY to protein domain specific binding (the VPR-1 MSP
  domain binds the VAB-1 ectodomain); DAF-18 row MODIFY to phosphatase binding (GO:0019902).
- Signaling receptor complex (IBA) KEEP_AS_NON_CORE: Eph receptors form ligand-induced
  clusters in vertebrates; no worm data.
- No NEW terms proposed (strict bar). Candidates considered and rejected: ventral enclosure
  / epidermal cell migration (phenotype-based; already covered by GO:0016331),
  regulation of insulin receptor signalling via DAF-18 (indirect, longevity/dauer phenotypes),
  gonadal sheath contraction (phenotype only).
