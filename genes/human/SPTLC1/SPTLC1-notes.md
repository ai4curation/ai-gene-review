# SPTLC1 (O15269) review notes

## Summary of function (verified biology)

SPTLC1 (serine palmitoyltransferase long chain base subunit 1; a.k.a. LCB1) is a
membrane subunit of the **serine palmitoyltransferase (SPT)** holoenzyme, which
catalyses the **first, committed and rate-limiting step of de novo sphingolipid
biosynthesis**: the PLP-dependent condensation of **L-serine + palmitoyl-CoA ->
3-ketodihydrosphinganine (3-oxosphinganine) + CO2 + CoA** (EC 2.3.1.50) at the
**ER membrane** [file:human/SPTLC1/SPTLC1-uniprot.txt; PMID:9363775 "It catalyzes the
pyridoxal-5'-phosphate-dependent condensation of L-serine and palmitoyl-CoA to
3-oxosphinganine."].

The catalytic core is a **heterodimer of SPTLC1 + SPTLC2 (or SPTLC3)** that assembles
as a dimer of heterodimers; small subunits **SPTSSA/SPTSSB** confer full activity and
substrate specificity, and **ORMDL proteins (ORMDL3)** negatively regulate the complex
in the presence of ceramide [PMID:19416851; PMID:33558761; PMID:33558762].
SPTLC1 belongs to the class-II PLP-dependent aminotransferase family; the PLP-binding
catalytic lysine resides on SPTLC2, so SPTLC1 by itself is not catalytic — GOA reflects
this with `contributes_to`/`part_of` qualifiers on several MF/complex annotations.

## Disease
- **HSAN1A (MIM:162400)**: autosomal dominant hereditary sensory and autonomic
  neuropathy; SPTLC1 missense variants (e.g. C133W) shift substrate use toward
  alanine/glycine, producing toxic **1-deoxysphingolipids** [file:...SPTLC1-uniprot.txt].
- **ALS27, juvenile (MIM:620285)**: variants disrupt ORMDL-mediated homeostatic
  inhibition, up-regulating SPT and elevating canonical sphingolipids
  [file:...SPTLC1-uniprot.txt; PMID:33558761].

## Annotation-review decisions (key points)

- **Core MF**: GO:0004758 serine C-palmitoyltransferase activity (confirmed current label
  via OLS). GOA carries `enables` (IDA PMID:19416851, TAS PMID:9363775) and
  `contributes_to` (several IDA) plus an IEA. All ACCEPT; the `contributes_to` framing is
  biologically apt because catalysis requires the SPTLC1-SPTLC2 heterodimer.
- **Core BP**: GO:0030148 sphingolipid biosynthetic process (TAS PMID:19416851; IDA
  acts_upstream). Also GO:0046512 sphingosine biosynthetic process and GO:0046513 ceramide
  biosynthetic process (IBA + IDA) — accepted; these are the LCB/ceramide arms of the same
  de novo pathway.
- **Core CC**: GO:0005789 ER membrane (EXP PMID:21618344, IEA, NAS, TAS Reactome);
  GO:0017059 serine palmitoyltransferase complex (multiple IPI/IDA); GO:0098554 cytoplasmic
  side of ER membrane (IDA). All ACCEPT — consistent with single-pass ER membrane protein
  whose catalytic domain (res 37-473) is cytoplasmic.
- **GO:0006686 sphingomyelin biosynthetic process** IDA via **PMID:30242129**: the cached
  FULL TEXT of that paper is about **SMS1 (SGMS1) + GCS (UGCG)** and does **not mention
  SPTLC1/SPT at all** (grep: 0 hits for SPTLC/palmitoyltransferase). SM biosynthesis is
  several steps downstream of the SPT-catalysed step. Marked MARK_AS_OVER_ANNOTATED (not
  REMOVE, per policy for experimental annotations) — the reference does not assay SPTLC1 and
  SM synthesis is not a direct SPTLC1 function. The IEA GO:0006686 (ARBA) is likewise an
  over-broad downstream mapping -> MARK_AS_OVER_ANNOTATED.
- **GO:0006688 glycosphingolipid biosynthetic process** IDA (PMID:19416851): abstract notes
  LCB profiling / diversity of long-chain bases but the direct enzymatic product is a
  3-ketosphingoid, not glycosphingolipid; downstream pathway term -> KEEP_AS_NON_CORE.
- **GO:0005515 protein binding** IPIs (SPTLC2, SPTLC3, SPTSSA, ORMDL3, SPTSSB): uninformative
  bare term; the informative content (SPT complex, ORMDL regulation) is captured by
  GO:0017059. MARK_AS_OVER_ANNOTATED per curation policy.
- **GO:1904649 regulation of fat cell apoptotic process** (IEA GO_REF:0000107 + ISS
  GO_REF:0000024, both transferred from mouse O35704): peripheral, orthology-transferred;
  KEEP_AS_NON_CORE.
- **GO:1904504 positive regulation of lipophagy** IDA (PMID:25332431): mouse-liver study
  (Atg7 KO; SPT overexpression induces autophagy). Indirect/physiological, upstream-of-or-
  within qualifier; KEEP_AS_NON_CORE.
- **GO:0030170 pyridoxal phosphate binding** IEA (InterPro): SPT is PLP-dependent, but the
  PLP-binding catalytic lysine is on SPTLC2, not SPTLC1 (class-II aminotransferase fold
  retained in SPTLC1 without the catalytic Lys). Kept but MARK_AS_OVER_ANNOTATED — likely
  over-propagated from the family-level InterPro signature to the non-catalytic subunit.

## Provenance notes
- file: UniProt quotes taken verbatim from SPTLC1-uniprot.txt (FUNCTION, CATALYTIC ACTIVITY,
  SUBCELLULAR LOCATION, SUBUNIT, SIMILARITY blocks).
- Reactome title left exactly as fetched ("SPTLC complexes transfer acyl-CoA onto serine").
- Core MF id/label used: GO:0004758 serine C-palmitoyltransferase activity.
