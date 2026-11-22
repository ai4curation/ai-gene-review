# CG5644 (Q9VSS3, FBgn0035948) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was consulted.

### Setup
- `just fetch-gene DROME CG5644` first resolved to Q7JVM8, a TrEMBL cDNA entry (GH22833p)
  that has no GOA rows. I re-ran it with `--uniprot-id Q9VSS3`, the FlyBase-linked
  proteome entry. GOA has one row for Q9VSS3: GO:0106389 ecdysteroid 22-kinase activity,
  TAS, PMID:32540344 (FlyBase).
- Deep research (`just deep-research-falcon ... --fallback perplexity-lite`) FAILED.
  Falcon gave "Exception: Failed to authenticate" and perplexity gave HTTP 401
  insufficient_quota. No deep-research file was written. The review is based on the
  primary literature read directly.

### Literature
- PMID:32540344 (Scanlan et al. 2020; abstract only): proposes that EcKLs are
  detoxification kinases. The abstract does not mention CG5644. The 2024 paper says
  CG5644 was not one of the 2020 detoxification candidates: "the 7 others—CG10514,
  CG31102, CG31087, CHKov2, CG9259, CG14314, and CG5644—were not (Scanlan et al. 2020)"
  [PMID:39208453]. FlyBase's TAS for the 22-kinase activity presumably rests on a
  statement in the full text that I cannot read.
- PMID:35794471 (Peng et al. 2022, Nature; full text): A. gambiae EcK2 (AGAP002181).
  "we validated its ecdysteroid kinase activity by incubating it with 20E, which resulted in
  phosphorylated 20E22P". With 3D20E as substrate no 22-phosphate product was detected.
- PMID:38291829 (Scanlan & Robin 2024, phylogenomics; full text): "AgEcK2, which encodes a
  20E 22-kinase in the mosquito A. gambiae (Peng et al. 2022), belongs to subfamily D and
  therefore the Diptera OLC Dip14." The clade is conserved as single-copy orthologs, and
  "CG5644 is the direct ortholog of AgEcK2, making it an excellent ecdysteroid 22-kinase
  candidate".
- PMID:39208453 (Scanlan & Robin 2024, G3; full text): this is the only experimental
  study of CG5644 in flies. It used UAS-ORF misexpression only.
  - "Only misexpression of CG6830 and CG5644 caused significant developmental arrest before
    the adult stage" (tub-GAL4).
  - phm-GAL4 (prothoracic gland) misexpression lowered adult survival (proportion 0.365).
  - Authors: "These data are consistent with the hypothesis that CG5644 encodes an ecdysteroid
    22-kinase". The abstract calls this "preliminary evidence".
  - Expression: "predominantly expressed in the adult nervous system" (FlyAtlas2). There is
    also a report of enrichment in ovarian border cells.
  - No loss-of-function allele was made, no substrate was assayed and no ecdysteroid
    phosphate was measured for CG5644.

### Evolutionary grounding (CG5644-bioinformatics/RESULTS.md)
- CG5644 and AgEcK2 (F5HIV2) are both in PANTHER PTHR11012:SF47 and eggNOG ENOG502SGND.
  They share 38.8% identity, are 459 vs 460 aa long, and both keep the HGDxWVNN
  catalytic loop. This matches the published subfamily D / Dip14 1:1 orthology.
- No PAINT node or IBA annotation covers CG5644. QuickGO has no GO annotations for F5HIV2.
- CG6830 is in SF6, a different subfamily, so 22-kinase specificity is NOT transferred to it.

### Decisions
- GO:0106389 TAS: ACCEPT. The activity is supported by subfamily-level orthology to a
  biochemically characterised 20E 22-kinase, by the conserved catalytic loop, and by
  misexpression phenotypes in the fly that fit the hypothesis. It is still an inference;
  no Drosophila biochemistry exists.
- No NEW process terms. Misexpression-induced developmental arrest is a gain-of-function
  phenotype and does not show that CG5644 normally participates in development or
  ecdysteroid inactivation in vivo.
