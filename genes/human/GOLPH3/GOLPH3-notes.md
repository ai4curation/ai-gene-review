# GOLPH3 review notes

UniProt: **Q9H4A6** → **GOLPH3** (Golgi phosphoprotein 3). Taxon: 9606. PI4P-binding Golgi adaptor/scaffold.

## Core function (standalone summary)

GOLPH3 is a **PI4P-binding peripheral membrane protein** on the cytoplasmic face of the Golgi
(concentrated at the TGN). It is a **COPI vesicle adaptor** that recognises the cytoplasmic tails
of Golgi-resident glycosyltransferases and packages them into retrograde intra-Golgi vesicles,
retaining enzymes in the stack. By binding PI4P and MYO18A simultaneously it links Golgi
membranes to actomyosin, generating the tensile force that shapes the Golgi ribbon and promotes
budding. A minor mitochondrial pool contributes to lipid metabolism.

## Key evidence (provenance)

- [PMID:34473204 title]: "GOLPH3 and GOLPH3L are broad-spectrum COPI adaptors for sorting into
  intra-Golgi transport vesicles" — basis for GO:0140312 cargo adaptor activity (core) and
  GO:0045053 protein retention in Golgi.
- [PMID:19837035]: GOLPH3 is a "PtdIns(4)P-binding protein that depends on PtdIns(4)P for its
  Golgi" localisation and bridges PI4P and actomyosin to promote budding — basis for GO:0070273
  PI4P binding (core), GO:0048194 Golgi vesicle budding, Golgi ribbon formation.
- [PMID:16263763]: mitochondrial localisation / lipid role (non-core).

## Annotation landscape (GOA, 60 rows)

- Core MF: GO:0140312 cargo adaptor activity; GO:0070273 PI4P binding. Core processes: Golgi
  organization, protein retention in Golgi, Golgi vesicle budding, ribbon formation, protein
  targeting to Golgi. Core locations: Golgi/TGN/cisterna membranes, cytosol.
- 7 bare protein-binding IPI -> REMOVE. GO:0010467 gene expression -> MARK_AS_OVER_ANNOTATED
  (implausibly broad; downstream readout). mTOR/migration/apoptosis/mito -> KEEP_AS_NON_CORE.
