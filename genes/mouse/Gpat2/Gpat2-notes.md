# Gpat2 (mouse, Q14DK4) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: mouse Gpat2 is the experimentally characterised reference for GPAT2
orthologs (PANTHER subfamily PTHR12563:SF15, "GLYCEROL-3-PHOSPHATE
ACYLTRANSFERASE 2, MITOCHONDRIAL"; human Q6NUI2 is in the same subfamily per
`interpro/panther/PTHR12563/PTHR12563-entries.csv`). This review is written from
the literature and UniProt only; no ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon mouse Gpat2 --fallback perplexity-lite` failed: falcon
returned "Edison API request failed: Failed to authenticate" (HTTP 403) and the
perplexity-lite fallback also failed. No deep-research file exists. Literature was
gathered instead by a PubMed esearch for "Gpat2 / glycerol-3-phosphate
acyltransferase 2" and the mouse primary papers were cached with `just fetch-pmid`.

### Evolutionary placement

- PANTHER PTHR12563:SF15 (UniProt DR line). GPAT2 is the paralog of GPAT1 (Gpam,
  PTHR12563 other subfamily), both mitochondrial outer membrane GPATs.
- PAINT node PTN000970957 (taxon:6072, Eumetazoa) carries IBD for GO:0004366 GPAT
  activity, GO:0005739 mitochondrion, GO:0006650 glycerophospholipid metabolic
  process and GO:0019432 triglyceride biosynthetic process; donors include mouse
  Gpam (MGI:109162) and Gpat2 (MGI:2684962) (`PTHR12563-paint.tsv`).
- PAINT did NOT propagate piRNA processing from PTN000970957. That is consistent with
  the biology: the piRNA role is GPAT2-specific (shown in mouse germline stem cells)
  and is not a property of the GPAT1/GPAT2 clade. Do not transfer it beyond the
  GPAT2 subfamily without further evidence.

### Experimental findings in mouse

- Enzyme activity (GPAT, EC 2.3.1.15): Wang et al. 2007 cloned Gpat2 from mouse
  testis; transfection into Cos-7 increased NEM-sensitive GPAT activity 30% and
  [14C]oleate incorporation into TAG 84% [PMID:17689486 "When Cos-7 cells were
  transiently transfected with GPAT2, NEM-sensitive GPAT activity increased 30%."].
  Harada et al. 2007 independently cloned it (xGPAT1) and saw GPAT activity in CHO-K1
  [PMID:17013544 "showed GPAT activity when epitope-tagged xGPAT1 was expressed in
  Chinese hamster ovary (CHO)-K1 cells"].
- Lewin et al. 2004 (PMID:14724270) detected an NEM-sensitive mitochondrial GPAT
  activity in GPAT1-null liver, named mtGPAT2, before the gene was cloned. The
  attribution of this activity to the Gpat2 gene product rests on later work; the
  MGI IDA rows from this paper are kept, deferring to the curators.
- Acyl-CoA preference: arachidonoyl-CoA [PMID:22905194 "GPAT2 overexpression
  significantly increased GPAT activity only when arachidonoyl-CoA was used as a
  substrate"]. AGPAT activity also rose in membranes of overexpressing cells, but the
  authors note "we cannot exclude the possibility that the protein has dual enzymatic
  activities" — i.e. the AGPAT activity is less firmly attributed to GPAT2 itself.
  All enzyme data are from crude membranes of overexpressing cells; no purified
  protein kinetics exist.
- Localization: mitochondrial (confocal, PMID:17689486); outer mitochondrial membrane
  with two TM segments and N/C termini cytosolic (PMID:22285183 topology study).
- piRNA: GPAT2 co-IPs with MILI/PIWIL2 in GS cells and testis; knockdown impairs
  primary piRNA production; HXXXXD catalytic-motif mutants (H205G, D210G) still rescue,
  so the piRNA role is independent of acyltransferase activity [PMID:23611983].
  Gpat2-deficient mice (PMID:30951587) show defective piRNA production, IAP/LINE-1
  derepression in fetal testes, and spermatocyte/spermatogonial apoptosis.
- Expression: testis, pachytene spermatocytes; promoter methylation and retinoic acid
  regulate it (PMID:26268560). In vivo testis shRNA causes pachytene arrest
  (PMID:28729426).

### Decisions

- GPAT activity: ACCEPT all rows; core MF.
- AGPAT (GO:0003841): KEEP_AS_NON_CORE (crude-membrane evidence; authors could not
  separate a direct activity from an induced one).
- mitochondrion → MODIFY to mitochondrial outer membrane (precise and supported).
- lipid metabolic / glycerophospholipid metabolic / generic acyltransferase → MODIFY to
  specific terms.
- protein binding (PIWIL2 IPI) → REMOVE per protein-binding policy; the interaction is
  real and is described in core_functions.
- piRNA processing → MODIFY to GO:0140990 primary piRNA processing (is_a GO:0034587,
  checked via OLS ancestors), which is what PMID:23611983 tested.
- No NEW process terms for transposon silencing, spermatogenesis or apoptosis: those
  are downstream phenotypes of losing piRNAs (or germ cells), not steps GPAT2 performs.
