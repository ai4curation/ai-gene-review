# SLC27A5 (horse, Equus caballus) - F6X2Q2

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Benchmark accession F6X2Q2 (DONKEY40_HORSE_PARTNER of donkey A0A9L0JNL2). New folder created
with `just fetch-gene HORSE F6X2Q2 --alias SLC27A5`; stub id confirmed as F6X2Q2. No ProtNLM2
file or prediction-evidence folder was opened or used.

### Deep research
`just deep-research-falcon HORSE SLC27A5 --fallback perplexity-lite` failed: falcon
"Exception: Failed to authenticate"; perplexity-lite fallback HTTP 401 (insufficient quota).
No deep-research file exists; the review uses the cached human primary literature
(PMID:10479480, PMID:10749848, PMID:11980911; all abstract-only) and the curated human
UniProt record (file:human/SLC27A5/SLC27A5-uniprot.txt). No horse-specific functional
literature on SLC27A5 was found.

### Identity: F6X2Q2 is an alternative/aberrant gene model
- F6X2Q2: TrEMBL, PE 3, 671 aa, Ensembl ENSECAT00000018051.4 / ENSECAP00000014705.4.
- A second horse entry from the same Ensembl gene (ENSECAG00000046881.1), A0A5F5PXH2
  (700 aa, ENSECAT00000070308.2), is the full-length model. UniProt gene name on that record
  is ZBTB45 with SLC27A5 as synonym (a VGNC cross-mapping oddity; F6X2Q2 carries the
  reciprocal ZBTB45 synonym).
- Alignment [file:HORSE/SLC27A5/SLC27A5-bioinformatics/RESULTS.md]: F6X2Q2 1-599 is 100%
  identical to A0A5F5PXH2 1-599 and 80.8% identical to human Q9Y2P5 1-589; the last 72
  residues of F6X2Q2 are unrelated to the conserved SLC27A5 C-terminus (20-33% identity in
  short gapped blocks). F6X2Q2 therefore lacks the AMP-binding_C subdomain (PF13193;
  576-652 in A0A5F5PXH2). In ANL-superfamily adenylating enzymes this C-terminal subdomain
  closes over the active site during adenylation, so a product ending as modelled would be
  expected to be catalytically compromised. Because all other mammalian SLC27A5 models
  (human, donkey, horse A0A5F5PXH2) share the conserved C-terminus, the F6X2Q2 C-terminus is
  most likely a gene-model artifact. Not tested whether such a transcript is expressed.
- Both horse records are PANTHER PTHR43107:SF25 (LONG-CHAIN FATTY ACID TRANSPORT PROTEIN 5),
  the same subfamily as human Q9Y2P5. This is the evolutionary basis for transferring the
  human SLC27A5 functions; no subfamily disagreement.

### PAINT/IBA
All 7 GOA rows are IBA (GO_REF:0000033):
- PTN001945407 (family-wide FATP node): LCFA-CoA ligase, LCFA transmembrane transporter,
  LCFA metabolic process, LCFA import into cell, plasma membrane.
- PTN001186241 (Eumetazoa node, taxon:6072, with SLC27A2/SLC27A4-like members, O14975, Q6P1M0,
  Q9Y2P5): ER membrane.
- PTN008678717 (Tetrapoda node grouping SLC27A2 and SLC27A5; donors O14975, Q9Y2P5,
  MGI:1347100, RGD:708535): bile acid metabolic process.
- Cholate-CoA ligase (GO:0047747) and VLCFA-CoA ligase (GO:0031957) were NOT propagated by
  PAINT. Cholate-CoA ligase is specific to SLC27A5 (SLC27A2/VLCS does not use C24 bile acids,
  PMID:11980911), so not propagating it at the SLC27A2+SLC27A5 node is correct; treated as a
  deliberate decision and not added as NEW. It is listed in core_functions on the basis of
  SF25 subfamily orthology to human SLC27A5.

### Biology (human ortholog, same subfamily)
- Cholate:CoA ligase [PMID:10749848 "exhibited cholate:CoA ligase (choloyl-CoA synthetase) activity with both"].
- C24 bile acid recycling [PMID:11980911 "We hypothesize that the primary function of homolog 2 is in the reactivation and recycling of C24 bile acids"].
- LC/VLC acyl-CoA synthetase, ER [PMID:10479480 "For all substrates tested (C18:0, C20:0, C24:0, C26:0)"; "the protein was associated with the endoplasmic reticulum but not with"].
- Hepatic LCFA uptake, by similarity to mouse [file:human/SLC27A5/SLC27A5-uniprot.txt "Plays an important role in hepatic fatty acid uptake and bile acid"].

### Decisions
- ACCEPT: LCFA-CoA ligase activity, LCFA metabolic process, ER membrane, bile acid metabolic process.
- KEEP_AS_NON_CORE: LCFA transmembrane transporter activity, LCFA import into cell, plasma membrane
  (consistent with the human and donkey reviews).
- Annotations are judged as claims about the SLC27A5 gene product; the F6X2Q2 C-terminal
  defect is recorded in the identity notes and does not change the gene-level actions.

### Relative
Canonical full-length product of the same gene: A0A5F5PXH2 (horse, 700 aa); no review exists
(would go in genes/HORSE/SLC27A5__A0A5F5PXH2). Characterized ortholog: human SLC27A5 Q9Y2P5
(genes/human/SLC27A5, status INITIALIZED although all rows carry actions).
