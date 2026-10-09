# SNRPGP15 notes (A8MWD9, RUXGL_HUMAN)

## 2026-10-04 Tier 3 audit (pseudogene / PE5 product)

### Locus and product existence
- HGNC:49371, "small nuclear ribonucleoprotein polypeptide G pseudogene 15",
  locus_type `pseudogene` (HGNC REST). Ensembl ENSG00000224543 biotype
  `processed_pseudogene`, single exon, chr19:14489388-14489609 (GRCh38).
- UniProt: PE 5 (uncertain); "CAUTION: Could be the product of a pseudogene."
  FUNCTION and SUBCELLULAR LOCATION lines are ECO:0000250 (by similarity), no
  experimental data. EMBL cross-references are NOT_ANNOTATED_CDS (genomic AC012318, EST
  CK005235).
- PubMed search for "SNRPGP15" returns no papers. The two UniProt references
  (PMID:15057824 chr19 sequence; PMID:15489334 MGC) are sequence-only.
- Bioinformatics (file:human/SNRPGP15/SNRPGP15-bioinformatics/RESULTS.md):
  - 72/76 identical to SNRPG (P62308); substitutions M13T, L17F, N55K, V61E.
  - GRCh38 and the UniProt-cited clone AC012318 both have TGA at codon 75 (SNRPG Arg75).
    The genome encodes a 74-aa ORF; the UniProt 76-aa sequence (ending ERV) is not the
    genomic translation. A restoring allele (rs1249850259 T>C) has gnomAD exome AF 2.06e-06.
  - 16 MS peptides mapped to A8MWD9 (PeptideAtlas/ProteomicsDB) are all exact SNRPG
    substrings; the discriminating tryptic peptides (GFDPFMNLVIDECVEMATSGQQK, NIGMVEIR)
    are not observed. No proteomic evidence for the SNRPGP15 product.
  - One 5' EST (CK005235) carries the four SNRPGP15-specific residues plus three more
    differences; origin (this locus with read errors vs another copy) unresolved.

### Fold / function residues vs SNRPG
- Sm-site recognition by SmG: [PMID:25555158 "U127 binding pocket comprises SmG L3
  residues Phe34 and Asn39, and loop 5 (L5) residue Arg63"]. All three retained in
  SNRPGP15. All 4PJO RNA-contacting SmG residues (K3, P36-N39, R63-N65) retained.
- Changed ring-interface residues: M13T (contacts SmE Met14) and V61E (β4/Sm2, contacts
  SmE Pro17/Leu20). V61E puts a charge into the SmG-SmE hydrophobic interface; effect untested.
- Ring order: [PMID:25555158 "SmF-SmE-SmG-SmD3-SmB-SmD1-SmD2"].

### GOA
- 13 IBA rows from PANTHER PTHR10553 nodes PTN000058285 (snRNPs, SMN-Sm complex,
  tri-snRNP, precatalytic spliceosome, splicing, P granule), PTN000058284 (U12-type,
  catalytic step 2 spliceosome, U2-type prespliceosome), PTN000058283 (contributes_to RNA
  binding; deep Sm/LSm node). UniProt places A8MWD9 in PTHR10553:SF26 "SMALL NUCLEAR
  RIBONUCLEOPROTEIN G-RELATED".
- 5 IEA rows: InterPro2GO (IPR034098 Sm_G -> splicing, spliceosomal complex; IPR047575 Sm
  -> RNA binding), ARBA (snRNP complex), UniProt SubCell (nucleus, itself by similarity).
- Propagation route: PAINT IBD on SmG/Sm nodes -> IBA to every tree leaf, including this
  processed-pseudogene retrocopy, because UniProt keeps A8MWD9 in the reference proteome
  and PANTHER classifies it in the SmG subfamily. Node placement is phylogenetically
  correct (the sequence is a recent SNRPG retrocopy); the failure is that no product is
  shown to exist. InterPro2GO/ARBA rows follow the same logic from domain signatures.

### Decision
- REMOVE all 18 rows: product of a processed pseudogene with an in-frame stop at codon 75
  in the reference genome and no discriminating peptide; no experimental data on the
  locus. Reversible if unique peptides (e.g. NIGMVEIR) are ever observed.
- No core functions; no NEW terms.
- Upstream suggestions: PANTHER/PAINT could exclude PE5 pseudogene-caution entries from
  IBA propagation (or UniProt could demote/obsolete A8MWD9 to match the genomic ORF);
  UniProt "Proteomics identification" keyword is set from shared, non-discriminating
  peptides.
