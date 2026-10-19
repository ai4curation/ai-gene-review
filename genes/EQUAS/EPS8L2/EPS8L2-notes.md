# EPS8L2 (donkey, Equus asinus; UniProt A0A9L0KBR4) - review notes

## Sources used

- Donkey UniProt record (unreviewed, Ensembl-derived): `EPS8L2-uniprot.txt`.
- Donkey GOA (8 IEA rows; 7 TreeGrafter GO_REF:0000118 rows from PANTHER node PTN008992914, 1 UniProt SubCell mapping GO_REF:0000044): `EPS8L2-goa.tsv`.
- Human ortholog EPS8L2 (Q9H6S3) UniProt record, fetched 2026-10-14: `EPS8L2-bioinformatics/human-EPS8L2-Q9H6S3-uniprot.txt`.
- Donkey-human alignment: `EPS8L2-bioinformatics/RESULTS.md`.
- Human QuickGO annotations (queried 2026-10-14) were used as a comparator: human EPS8L2 carries IDA/IGI annotations from PMID:14565974 for actin binding, Rho protein signal transduction, regulation of Rho protein signal transduction, ruffle membrane and positive regulation of ruffle assembly, plus IBA rows for the same terms and plasma membrane. PMID:14565974 is not cached in `publications/`, so it is not quoted here.
- No GOA row for the donkey protein cites a publication, so no publication was fetched.

## Identity and family

- Donkey record: "Belongs to the EPS8 family." [file:EQUAS/EPS8L2/EPS8L2-uniprot.txt "Belongs to the EPS8 family."]
- Domains: PTB, SH3 (459..542) and the EPS8 C-terminal effector region (InterPro EPS8-like IPR039801; PANTHER PTHR12287:SF20 EPS8-like protein 2).
- The donkey protein (681 aa) aligns to human EPS8L2 (715 aa) end to end [file:EQUAS/EPS8L2/EPS8L2-bioinformatics/RESULTS.md "Paired residues: 679; identical: 572; identity over paired: 84.24%"]. Missing human segments are N-terminal (4..27, 38..47).

## Function (human ortholog)

- [file:EQUAS/EPS8L2/EPS8L2-bioinformatics/human-EPS8L2-Q9H6S3-uniprot.txt "Stimulates guanine exchange activity of SOS1. May play a role in membrane ruffling and remodeling of the actin cytoskeleton."]
- Complex/actin: [same file "Part of a complex that contains SOS1, ABI1 and EPS8L2. Associates with F-actin."]
- Hearing: [same file "In the cochlea, is required for stereocilia maintenance in adult hair cells"]; localization [same file "Localizes at the tips of the stereocilia of the inner and outer hair cells."] (by similarity to mouse). Human disease DFNB106 (deafness).

## Review decisions (summary)

- actin binding: ACCEPT (core MF; EPS8 family actin capping/bundling, human IDA).
- cytoplasm: ACCEPT. plasma membrane: KEEP_AS_NON_CORE (the informative location is ruffle membrane). ruffle membrane: ACCEPT.
- vesicle: KEEP_AS_NON_CORE (human support is only exosome proteomics, HDA).
- Rho protein signal transduction / regulation of Rho protein signal transduction / positive regulation of ruffle assembly: ACCEPT (SOS1-ABI1-EPS8L2 Rac-GEF complex; human IDA/IGI).
- NEW: stereocilium tip (GO:0032426) location, supported by the human UniProt location note (by similarity to mouse).
