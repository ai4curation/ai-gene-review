# DNAJC14 (DRIP78 / HDJ3) research notes

## Identity
- UniProt Q6Y2X3, HGNC:24581, 702 aa. DnaJ/HSP40 subfamily C member 14.
- AltNames: DnaJ protein homolog 3 (hDj-3); Dopamine receptor-interacting protein of 78 kDa (DRIP78).
- Multi-pass ER membrane protein: 3 predicted transmembrane helices (250-270, 300-320, 326-346),
  large disordered N-terminus, J domain at 443-507 (C-terminal half, cytoplasmic side), Jiv90/Jiv
  domain (Pfam PF14901) characteristic of the DNAJC14/Jiv family. [file:human/DNAJC14/DNAJC14-uniprot.txt]

## Core function: ER membrane J-protein / GPCR ER export chaperone
- UniProt FUNCTION: "Regulates the export of target proteins, such as DRD1, from the endoplasmic
  reticulum to the cell surface." (by similarity, ECO:0000250). SUBUNIT: "Interacts with the
  FxxxFxxxF motif of DRD1 via its C-terminal domain." [file:human/DNAJC14/DNAJC14-uniprot.txt]
- Founding study: Bermak et al. 2001 Nat Cell Biol (PMID:11331877) "Regulation of transport of the
  dopamine D1 receptor by a new membrane-associated ER protein" — identified DRIP78 as ER protein
  controlling DRD1 surface delivery via an FxxxFxxxF ER-export motif. (Title in UniProt ref list.)
- DRIP78 also implicated in trafficking of other GPCRs (e.g. AT1R/angiotensin receptor) and the
  Ggamma subunit; acts as a chaperone retaining/regulating ER export.

## Flavivirus connection (Jiv domain)
- The Jiv/Jiv90 domain is homologous to the pestivirus NS5A-associated J-domain protein and to the
  region of flaviviral NS3 cofactor; DNAJC14 has been implicated as a host factor that regulates
  flavivirus (e.g. yellow fever, dengue) RNA replication via its J domain. (background; not in GOA)

## Localization
- ER membrane, multi-pass (by similarity). GO:0005789 IEA SubCell. [file:human/DNAJC14/DNAJC14-uniprot.txt]
- GO:0016020 membrane HDA (bulk proteomics PMID:19946888) — generic, non-core.

## GOA annotations
- GO:0050780 dopamine receptor binding IBA (GO_REF:0000033) and IEA (GO_REF:0000107, from rat ortholog
  Q5XIX0) — supported by DRD1 interaction; core MF.
- GO:0001664 G protein-coupled receptor binding IEA (rat ortholog) — generalization of DRD1 binding;
  consistent with broader GPCR-trafficking role.
- GO:0005515 protein binding IPI WITH P82979 (SARNP, a nuclear SAP/RNA-binding protein) from two HT
  screens (PMID:28514442, PMID:33961781) — uninformative; SARNP is nuclear, unrelated to ER GPCR
  trafficking; likely HT artifact. Keep non-core.

## Curation decisions
- Core MF: GPCR-export chaperone. dopamine receptor binding (GO:0050780) is the most specific
  supported MF; GPCR binding (GO:0001664) is the parent. The J-domain HSP70 co-chaperone activity is
  inferred but the functional readout is GPCR ER export. Core: dopamine receptor binding + the BP of
  protein export from ER / protein transport. No experimental human-specific paper cached; rely on
  UniProt (by similarity) and IBA.
- protein binding with SARNP: MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE (uninformative HT, wrong
  compartment partner).
