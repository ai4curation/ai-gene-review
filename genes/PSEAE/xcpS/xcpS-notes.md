# xcpS (PA3102, Q00513) review notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol)

Fetched with `just fetch-gene PSEAE xcpS` (first attempt timed out at UniProt, second succeeded);
accession Q00513 matches the worklist (rank 46, PA3102). No deep-research provider was used;
these are manual notes from the cached publications, PubMed searches and the UniProt record.
Publications PMID:17464073, PMID:18832308 (and, not used, PMID:12581354, PMID:1389315) were
cached with `ai-gene-review fetch-pmid`; all abstract-only.

### What XcpS is

- GspF-family inner-membrane platform protein of the Xcp T2SS. UniProt: "Belongs to the GSP F
  family"; NCBIfam TIGR02120 (GspF), InterPro IPR011850 (T2SS_GspF), PANTHER PTHR30012:SF0.
- Similar to type IV pilus PilC [PMID:1588814 "XcpR and XcpS, show similarity to the PilB and
  PilC proteins required for fimbriae assembly"].
- Inner-membrane core component; stabilised by XcpR (GspE) and XcpY (GspL) via its cytoplasmic
  loop; P. putida swap hybrids define species-specific functional domains [PMID:17464073 "One of
  the core components of the Xcp system is the inner-membrane protein XcpS (GspF)"; "XcpS was
  shown to be stabilized by co-expression of the XcpR (GspE) and XcpY (GspL) components of the
  machinery, demonstrating an interaction between these three proteins"; "The cytoplasmic loop of
  XcpS was found to be involved in the stabilization by XcpR and XcpY"]. UniProt curates the
  topology (cytoplasmic 1..168, periplasmic 190..219, cytoplasmic 240..376) from this paper.
- XcpRSYZ subcomplex co-purified under native conditions [PMID:16168578 "This subcomplex was also
  found to interact with XcpR and XcpS to form a XcpRSYZ complex which was isolated under native
  conditions"].
- Polar localisation; tagged XcpS is functional [PMID:18832308 "Fusion of the Lumio tag to the C
  termini of the XcpR and XcpS proteins did not affect the functionality of these proteins";
  "labelled XcpS was still found to locate at the poles, whereas XcpR was evenly distributed in the
  cell"].
- Ca2+ binding sites in the cytoplasmic domain are only By-similarity (P45780); not annotated.

I did not find a PAO1 paper whose abstract reports an xcpS single-deletion secretion phenotype;
the 2003 pseudopilus paper uses xcpRS double deletions (PMID:12700254). Primary support for the
process term is therefore the functional analysis in PMID:17464073 and PMID:18832308.

### PseudoCAP rows

- GO:0015627 IDA PMID:16168578: direct co-purification; correct.
- GO:0015628 IDA PMID:9818381: a review (FEMS Microbiol Rev 1998, PubMed type Review). Same
  defect as recorded on xcpX: WRONG_EVIDENCE_CODE, CHECK; term correct.

### PAINT node composition

`genes/PSEAE/xcpV/xcpV-bioinformatics/node_leaves.py` (shared analysis for the three Xcp genes)
lists current QuickGO leaves of PTN000768597 for GO:0015628: 911 proteins, 846 T2SS-named,
7 named PilC/HofC/MshG, 58 generic. The node also carries a plasma membrane IBD seeded by E. coli
HofC (P36646, PTHR30012:SF7) and GspF (P41441), so the node spans both the GspF and the
HofC/PilC subfamilies. The T2SS process term at this node therefore leaks to a few type IV
pilus/MSHA platform proteins. Small fraction; noted, no defect filed.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000768597 | GO:0015628 protein secretion by the type II secretion system | 1 (sole seed) | 25 (12 taxa) in worklist; 911 proteins in current QuickGO | GO:0015628, IDA, PMID:9818381 | SOUND (term); evidence code UNVERIFIED (cited paper is a review; abstract only) | XcpS is a core Xcp component (PMID:16168578, PMID:17464073). PMID:9818381 is a review, so IDA is invalid; re-key to a primary paper (PMID:17464073) or TAS. Node term suits a GspF clade; a few PilC/HofC/MshG leaves receive it (minor over-propagation). |
