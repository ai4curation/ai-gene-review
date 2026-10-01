# SOS2 (human, UniProt Q07890) - curation notes

## Identity

- UniProt Q07890 (SOS2_HUMAN), 1332 aa, Son of sevenless homolog 2; paralog of SOS1
  [file:human/SOS2/SOS2-uniprot.txt].
- Domains: N-terminal histone fold, DH (198-388), PH (442-546), N-terminal Ras-GEF/REM (595-739),
  Ras-GEF/CDC25 (778-1017), C-terminal disordered proline-rich region (1142-1332)
  [file:human/SOS2/SOS2-uniprot.txt].
- PANTHER PTHR23113 (GUANINE NUCLEOTIDE EXCHANGE FACTOR), subfamily PTHR23113:SF150 (SON OF SEVENLESS
  HOMOLOG 2) [file:human/SOS2/SOS2-uniprot.txt]; PAINT node PTN000560991 carries GEF activity and Ras
  protein signal transduction (also used in modules/erk_cascade.yaml).
- No GO-CAM model in `gocams/index.tsv` contains Q07890.

## Molecular function

- Ras GEF [file:human/SOS2/SOS2-uniprot.txt "Acts as guanine nucleotide exchange factor (GEF) for RAS
  proteins."]; the CDC25-homology domain promotes GDP release from RAS
  [file:human/SOS2/SOS2-deep-research-falcon.md "The CDC25-homology domain destabilizes nucleotide
  coordination and promotes GDP dissociation."].
- Cellular evidence: SOS2 in a TPR1-Galpha16 complex enhances Ras activation [PMID:20639119 "Expression of
  SOS2 enhanced Galpha16QL-induced Ras activation and its subsequent signaling."].
- Rac/Rho GEF activity of SOS2 (via DH domain) is not established, unlike SOS1
  [file:human/SOS2/SOS2-deep-research-falcon.md "SOS1 is a demonstrated RAC-GEF, whereas SOS2 has supporting
  interaction and homology evidence but had not, as of the authoritative 2021 synthesis, been formally
  established as an equivalent RAC-GEF."]. The two Reactome cytosol rows come from Rho/Rac GEF events;
  the location is fine but the implied activity is provisional.

## Recruitment / binding

- GRB2 binds the SOS2 proline-rich C-terminus through its SH3 domains, with higher affinity than SOS1
  [PMID:7629138 "We show that hSos2 interacts with Grb2 via its proline-rich COOH-terminal domain and that
  this interaction is dependent on the SH3 domains of Grb2."; "the apparent binding affinity of hSos2 for
  Grb2 is significantly higher relative to that of hSos1 both in vitro and in vivo"].
- Other IPI partners are all SH3-domain proteins (NCK1, CRK, PLCG1, ABL1, PACSIN3, SNX9), identified in
  SH3/proline-peptide screens [PMID:17474147; PMID:14679214 "The proline-rich Sos peptide retrieved only
  SH3 domain containing proteins as specific binding partners."]. All GO:0005515 rows -> MODIFY to
  GO:0017124 SH3 domain binding.

## Localization

- Cytosolic at rest, acts at the plasma membrane on prenylated RAS after GRB2-mediated recruitment
  [file:human/SOS2/SOS2-deep-research-falcon.md "SOS2 is a soluble intracellular protein that is primarily
  cytosolic in unstimulated cells."].

## Processes

- Ras protein signal transduction (core), downstream of RTKs; contributes preferentially to PI3K-AKT output
  in some contexts; partially redundant with SOS1 (Sos2-null mice viable).
- Insulin receptor signalling (IEA from mouse ortholog): plausible, non-core.

## Disease

- Noonan syndrome 9 (heterozygous gain-of-function variants) [PMID:25795793 "We identified two novel genes,
  SOS2 and LZTR1, associated with Noonan syndrome"].

## Annotation decisions

- GEF activity (IBA, IEA) ACCEPT; GO:0005085 is the current term (Ras-specific GEF term GO:0005088 no longer
  resolves in the GO build).
- GO:0046982 protein heterodimerization activity (InterPro2GO from histone-fold IPR009072) -> REMOVE: the
  SOS histone fold is an intramolecular tandem histone-like domain within a single chain, not evidence of a
  heterodimerization activity with another protein.
- PMID:19593445 (known batch miscitation) is not present in the SOS2 GOA set.
