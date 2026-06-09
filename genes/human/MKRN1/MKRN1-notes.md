# MKRN1 (Q9UHC7) research notes

Makorin RING finger protein 1 (RNF61). RING-type E3 ubiquitin ligase with C3HC4 RING and
multiple CCCH/C3H zinc-finger motifs (RNA-binding). Makorin family; paralog MKRN2/3.

## Core MF: RING E3 ubiquitin ligase
UniProt: "E3 ubiquitin ligase catalyzing the covalent attachment of ubiquitin moieties onto
substrate proteins." CATALYTIC ACTIVITY EC=2.3.2.27 [PMID:19536131].
- Substrates: p53/TP53 (suppresses p53 under normal conditions), CDKN1A/p21 (degrades under
  stress, promoting apoptosis), TERT (negative regulator of telomerase), FILIP1.
  [PMID:19536131 "Differential regulation of p53 and p21 by MKRN1 E3 ligase controls cell
  cycle arrest and apoptosis."]
- Direct E3 ligase activity: GO:0061630 (IDA, PMID:19536131); polyubiquitination GO:0000209.

## Core BP: ribosome-associated quality control of poly(A) translation
MKRN1 is an RNA-binding E3 that acts in RQC at poly(A) stalls (premature polyadenylation):
[PMID:31640799 "The RNA-binding ubiquitin ligase MKRN1 functions in ribosome-associated quality
control of poly(A) translation."]
- Binds PABPC1, associates with polysomes, positioned upstream of poly(A) tails in a PABPC1-
  dependent manner; promotes ribosome stalling at poly(A): [PMID:31640799 "MKRN1 depletion
  abrogates ribosome stalling at A-rich sequences and results in reduced ubiquitylation of
  RPS10 and PABPC1."]
- Ubiquitylates ribosomal protein RPS10 and PABPC1 [PMID:31640799 "MKRN1 ubiquitylates
  ribosomal protein RPS10 and translational regulators."]
- Acts upstream of ZNF598 (which then ubiquitylates RPS10/RPS20) and LTN1-mediated nascent
  chain degradation. This is the RQC role highlighted in the batch instructions.

## RNA binding
GO:0003723 RNA binding (HDA, PMID:22658674) — consistent with CCCH zinc fingers and poly(A)
recognition.

## Localization
Cytosol (Reactome TAS) — consistent with cytoplasmic E3 / ribosome-associated function.

## Annotation plan
- GO:0061630 ubiquitin protein ligase activity (IBA/IEA/TAS/IDA): ACCEPT (core MF).
- GO:0016567 protein ubiquitination / GO:0000209 polyubiquitination: ACCEPT.
- GO:0046872 metal ion binding (IEA): ACCEPT/KEEP_AS_NON_CORE (RING + zinc fingers coordinate Zn).
- GO:0003723 RNA binding (HDA): ACCEPT (genuine; underlies poly(A) recognition).
- protein binding IPI (19536131, 32296183): KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED (HT).
- cytosol TAS: ACCEPT.
- NEW: GO:1990116 ribosome-associated ubiquitin-dependent protein catabolic process and/or
  GO:0072344 rescue of stalled cytosolic ribosome (RQC of poly(A) translation), from PMID:31640799.
