# galK (P0A6T3, GAL1_ECOLI) notes

## Deep research status

- 2026-11-12: no deep-research provider key was available in this session, so no
  `galK-deep-research-*.md` file exists. This review is based on the UniProt record,
  the cached publications behind the GOA rows, and additional abstracts fetched with
  `just fetch-pmid` (PMID:12816414, PMID:14612558, PMID:200486, PMID:3158881).
- Most of the GOA source papers (PMID:13390972, PMID:13977183, PMID:16590575,
  PMID:4889465) are cached title-only; experimental rows on them are accepted by
  deferring to the curator where the claim is independently corroborated.

## Identity

- E. coli K-12 galK (b0757, JW0740; synonym galA), third gene of the galETKM operon.
  Galactokinase, EC 2.7.1.6, 382 aa; initiator Met removed [file:ECOLI/galK/galK-uniprot.txt
  "Removed"] (PMID:200486, N-terminal sequencing).
- GHMP kinase family, GalK subfamily [file:ECOLI/galK/galK-uniprot.txt "Belongs to the
  GHMP kinase family. GalK subfamily."]; InterPro IPR000705, IPR022963; NCBIfam TIGR00131;
  PANTHER PTHR10457:SF7; HAMAP MF_00246.
- Sequence homology with yeast GAL1 including an ATP-binding motif [PMID:3158881 "find
  several regions of strong homology among which is a potential ATP-binding site homology"].

## Molecular function

- Reaction [file:ECOLI/galK/galK-uniprot.txt "Reaction=alpha-D-galactose + ATP =
  alpha-D-galactose 1-phosphate + ADP"]; curated from PMID:12816414, PMID:14612558, PMID:200486.
- Substrate range: D-galactose (KM 2.1 mM), 2-deoxy-D-galactose, D-galactosamine; not
  D-galacturonic acid, D-talose, L-altrose, L-glucose (UniProt kinetics from
  PMID:12816414 and PMID:14612558).
- Y371H broadens substrate range [PMID:14612558 "displayed a surprisingly substantial
  degree of kinase activity toward sugars as diverse as d-galacturonic acid, d-talose,
  l-altrose, and l-glucose, all of which failed as wild-type GalK substrates"].
- Mg2+ and ATP binding residues are HAMAP rule predictions (ECO:0000255), not direct
  E. coli structure data; no E. coli GalK crystal structure is cited in UniProt.

## Biological process

- Leloir pathway, first step [PMID:13914787 "The functions pertaining to the three
  genetically defined cistrons were found to relate, respectively, to the expression of
  galactokinase, galactose 1-phosphate uridyl transferase, and uridine diphosphate
  galactose 4-epimerase."].

## Location

- Cytosol: E. coli cytosolic proteome [PMID:18304323 "we identified 1103 proteins from the
  cytosolic fraction of the Escherichia coli strain MC4100"]; GalK is not named in the
  cached main text (data tables), so the IDA is accepted by deferring to the curator.

## Curation decisions

- 19 review rows (the 20 GOA lines include two IDA galactokinase lines on the same PMID, merged into one row): ACCEPT 9, MODIFY 6, KEEP_AS_NON_CORE 4.
- kinase activity / phosphotransferase (alcohol acceptor) IEA -> MODIFY to GO:0004335.
- galactose metabolic process (IBA, IEA) -> MODIFY to GO:0033499 (descendant), with
  propagation_review on the IBA.
- cytoplasm (IDA, IEA) -> MODIFY to cytosol GO:0005829.
- Mg2+ binding (IDA, IEA) and ATP binding (IEA): KEEP_AS_NON_CORE (cofactor/co-substrate
  binding integral to the kinase activity).
- carbohydrate phosphorylation IEA: KEEP_AS_NON_CORE; OLS shows GO:0046835 has no
  children, so it cannot be refined.
- No NEW rows proposed.
