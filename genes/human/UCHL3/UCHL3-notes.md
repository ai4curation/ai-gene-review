# UCHL3 (human, P15374) notes

## 2026-11-23 - Seed and family context

Seeded UCHL3 from UniProt:P15374 and the 2026-11-04 human GOA GPA/GAF/GPI release because the QuickGO annotation/search endpoint returned HTTP 500 for the live fetch. The generated GOA TSV contains 41 real GOA rows, not a header-only failed fetch. PTHR10589 contains four reviewed human proteins: UCHL1/P09936, UCHL3/P15374, UCHL5/Q9Y5K5 and BAP1/Q92560. BAP1, UCHL1 and UCHL5 already have local reviews; UCHL3 is the only missing human member.

## 2026-11-23 - Curated conclusions

UCHL3's core activity is cytosolic cysteine-type deubiquitination, with direct support for hydrolyzing ubiquitin C-terminal peptide, amide, ester and isopeptide bonds and for processing ubiquitin-ribosomal precursors. It also cleaves the C terminus of NEDD8, but that activity is secondary because Reactome treats SENP8 as redundant for the same NEDD8 maturation reaction. PMID:27941124 supports a separate DNA-damage role in which ATM-phosphorylated UCHL3 deubiquitinates RAD51 and promotes RAD51-BRCA2 binding during homologous recombination; the matching production GO-CAM is gomodel:69a0c46f00002570. The PTN000063381 GO:0030163 protein catabolic process IBD was treated as over-propagated from an Uchl3 perturbation phenotype, because small UCHL3 liberates ubiquitin from adducts and precursor proteins rather than acting as a proteasomal degradation factor like the UCHL5 branch.

PMID:21453705 reports physical interaction between Uch-L3 and SMAD1 and decreased polyubiquitinated SMAD1 during osteoblast differentiation; that BMP-signaling context is recorded as a follow-up question rather than a new GO process annotation from one overexpression and knockdown study. The CLPB, DMWD and SPRED1 protein-binding rows likewise remain interaction leads without a resolved UCHL3 substrate or regulatory function.
