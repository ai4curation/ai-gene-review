# Q9KWG3 — Streptomyces sp. strain CL190 phosphomevalonate kinase (orfC)

## Identity and folder name

- Stub `id: Q9KWG3` (PMK_STRC1), 374 aa, NCBITaxon:93372. UniProt gives no gene name or ordered
  locus name.
- EMBL AB037666 (protein BAB07792.1): the CDS has only `/product="phosphomevalonate kinase"`
  and no `/gene` qualifier; only `hmgr` and `hmgs` carry gene names in that record
  (checked with the ENA flat file, 2026-11-18).
- The original paper names the flanking open reading frames orfA to orfE
  [PMID:10894721 "Sequence analysis of the flanking regions of the hmgr gene revealed five new open
  reading frames, orfA to -E"]. Its full text (read on the PMC web page, not cached) assigns the
  PMK to orfC by comparison with yeast PMKs. "orfC" is a positional ORF label, not a gene symbol,
  so the folder stays at the accession, `genes/STRC1/Q9KWG3`.
- Classification: PANTHER PTHR31814:SF2 (PHOSPHOMEVALONATE KINASE, GHMP/ERG8 type), NCBIfam
  TIGR01220 (Pmev_kin_Gr_pos, the Gram-positive-type PMK family), InterPro IPR005917 and
  IPR035102.

## Literature search (2026-11-18)

- NCBI `Streptomyces CL190 AND mevalonate` -> 9 hits; on this cluster: PMID:10894721 (cluster
  cloning and E. coli reconstitution), PMID:11158573 (orfD is a type 2 IPP isomerase),
  PMID:10648511 (CL190 also has the MEP pathway), PMID:15118326 (HMGS/HMGR for mevalonate
  production; not PMK).
- NCBI `Streptomyces AND "phosphomevalonate kinase"` -> 2 hits: PMID:15981409 (Dairi 2005 review
  of actinomycete MV clusters), PMID:11515548 (cluster from another strain, KO-3988).
- UniProt cites PMID:23378249 (Nishimura et al. 2013, S. solfataricus) for this protein's
  FUNCTION and CATALYTIC ACTIVITY with ECO:0000269. The cached abstract mentions only the
  Sulfolobus enzymes, and the full text (J Biochem) could not be retrieved; a web search found
  no description of the Streptomyces enzyme assay. The most likely reading is that the
  Streptomyces PMK was assayed alongside the Sulfolobus enzyme in the full text (for example as
  a reference enzyme), but this could not be checked here.

## What the evidence shows

- Genetic reconstitution: E. coli carrying hmgr plus orfA-E used the mevalonate pathway and grew
  on fosmidomycin, which blocks its native MEP pathway [PMID:10894721 "This transformant could
  grow in the presence of fosmidomycin, a potent and specific inhibitor of the nonmevalonate
  pathway, indicating that the mevalonate pathway, intrinsically absent in E. coli, is operating
  in the E. coli transformant."]. A working classical pathway needs a PMK, and orfC is the only
  PMK candidate in the cluster, so this is genetic evidence that orfC supplies the PMK step.
- Biochemical activity of the recombinant protein: UniProt curated statement citing
  PMID:23378249 (not verified from the cached abstract).
- Context: Streptomyces strains with both MEP and MV pathways use the MV cluster for isoprenoid
  secondary metabolites [PMID:15981409 "some Streptomyces strains possess the mevalonate (MV)
  pathway via which isoprenoid antibiotics are produced"]; CL190 uses both pathways
  [PMID:10648511].

## Annotation decisions

- PMK activity (IEA, EC/Rhea): ACCEPT, core. Supported by the reconstitution, the TIGR01220/
  PTHR31814 classification, and the curated UniProt function.
- ATP binding (IEA, GHMP N-domain): ACCEPT.
- IPP biosynthesis, mevalonate pathway (IEA, UniPathway): ACCEPT, core; UniProt's PATHWAY line
  cites PMID:10894721 (ECO:0000269).
- No IBA rows: the strain is not in the PANTHER reference proteome set, so PAINT does not reach
  it. No NEW rows.
