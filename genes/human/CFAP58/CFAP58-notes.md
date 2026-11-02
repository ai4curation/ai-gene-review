# CFAP58 notes

## Deep research status

Automated deep research was attempted and failed, so no `CFAP58-deep-research-*.md`
file exists for this gene:

- `just deep-research human CFAP58 --provider falcon` failed with
  `Exception: Failed to authenticate` (Edison/Falcon JWT authentication error).
- `just deep-research human CFAP58 --provider perplexity` failed with
  `Provider 'perplexity' not available. Available: falcon, asta, openscientist`.

Notes below come from a manual PubMed search (`CFAP58[Title/Abstract]`, 15 hits; several
are unrelated lncRNA `CFAP58-DT` cancer-signature papers and were ignored) and the cached
publications. Every cited PMID was cached with `just fetch-pmid` / `just fetch-gene-pmids`.

## Identity

- UniProt Q5T655 (CFA58_HUMAN); 872 aa; almost entirely coiled coil (CFAP58_CC Pfam
  domain); PANTHER PTHR32083:SF31. Testis-enriched.
- Disease: spermatogenic failure 49 (SPGF49, MIM:619144), autosomal recessive MMAF.

## Human genetics and sperm phenotype

- [PMID:32791035 "we identified bi-allelic loss-of-function variants in CFAP58 by using
  whole-exome sequencing in five (5.6%) unrelated individuals from a cohort of 90
  MMAF-affected Chinese men"]; [PMID:32791035 "Transmission electron microscopy
  demonstrated striking flagellar defects with axonemal and mitochondrial sheath
  malformations."]; localization [PMID:32791035 "Immunofluorescence assays showed that
  CFAP58 localized at the entire flagella of control sperm and predominantly
  concentrated in the mid-piece."]; markers [PMID:32791035 "the abundances of axoneme
  ultrastructure markers SPAG6 and SPEF2 and a mitochondrial sheath protein, HSP60, were
  significantly reduced"]. Abstract only (PMC7477015 exists but full text was not
  retrievable through the cache).
- [PMID:33314088 "CFAP58 was absent in the CFAP58-mutated sperm."] (abstract only).
- [PMID:40675161 "Transmission electron microscopy (TEM) analysis revealed the absence of
  the central pair (CP) of microtubules in the axonemal structure of sperm flagella."]
  and [PMID:40675161 "the CFAP58 mutation disrupts CP assembly during spermiogenesis"]
  (abstract only; Pakistani families plus a knock-in mouse).
- [PMID:42799967 "CFAP58 may contribute to the structural connection between radial
  spokes (RS) and doublet microtubules (DMTs); its absence leads to RS damage and
  axonemal instability."] (abstract only, 2026; mechanistic statement is tentative).

## Mouse and cattle

- [PMID:32791035 "The male mice were infertile and presented with severe flagellar
  defects"] (Cfap58 KO).
- [PMID:38602507 "the loss of Cfap58 not only causes severe defects in the sperm tail, but
  also affects the manchette structure, resulting in abnormal sperm head shaping."] and
  [PMID:38602507 "CFAP58 interacts with IFT88 and CCDC42"]; proposed as an
  IMT/IFT cargo (abstract only).
- Somatic cells: [PMID:31904090 "In neural progenitor cells, endogenous Cfap58 signals
  overlapped with signals of the centrosome marker"]; knockdown impairs primary cilium
  growth in astrocytes. Notch: [PMID:31904090 "Inhibition of Notch signaling elevated not
  only the expression level of Cfap58 in vitro and in vivo, but also the length of the
  primary cilia and sperm midpiece."] i.e. Cfap58 is downstream of (repressed by) Notch;
  nothing shows the protein transduces a Notch signal.

## Open points

- The exact axonemal position of CFAP58 is not resolved structurally. It is not among
  the mouse sperm central-apparatus proteins assigned by in situ cryo-ET
  (PMID:40473901 does not mention CFAP58), so the loss of the central pair in mutants
  may be secondary. The 2026 RS-DMT interface proposal is from IF/TEM, not structure.
- Its midpiece enrichment and mitochondrial-sheath phenotype distinguish it from the
  purely axonemal MMAF proteins.

## Annotation decisions (summary)

- Notch signaling pathway (IEA, ISS) -> REMOVE: Cfap58 expression is a Notch target, the
  protein does no work in the pathway.
- protein binding x5 (high-throughput Y2H) -> REMOVE (uninformative).
- cilium assembly (IEA, ISS) and cilium / motile cilium (IEA) -> TOO_GENERAL, entailed by
  accepted sperm axoneme assembly / sperm flagellum.
- protein localization to motile cilium (IMP) -> MARK_AS_OVER_ANNOTATED (marker-depletion
  evidence shows necessity, not transport).
- extracellular region (HDA tears proteome) -> MARK_AS_OVER_ANNOTATED.

## Review round 2 (PR 5062 automated review)

- `sperm principal piece` (IDA, GO_REF:0000052) ACCEPT: the reason now states the
  inference explicitly. The HPA-type source is not quotable; whole-flagellum staining in
  control sperm [PMID:32791035 "Immunofluorescence assays showed that CFAP58 localized at
  the entire flagella of control sperm and predominantly concentrated in the mid-piece."]
  includes the principal piece.
- core_functions keeps both `sperm axoneme assembly` (GO:0007288) and `sperm flagellum
  assembly` (GO:0120316); the description now spells out why: the requirement is
  flagellum-wide (mitochondrial sheath malformation and HSP60 depletion in the midpiece,
  where CFAP58 is concentrated, as well as axonemal defects), while whether the sheath
  contribution is direct remains open, so `sperm mitochondrial sheath assembly` itself
  stays non-core.
