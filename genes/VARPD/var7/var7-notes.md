# Curation Notes: var7 (A0A0N9LYB5) in Variovorax paradoxus

## Overview
- **UniProt ID:** `A0A0N9LYB5` (`A0A0N9LYB5_VARPD`, 2,431 aa)
- **Gene symbol / GenBank protein:** `var7` (`ALG65342.1`, `EMBL:KT362218`)
- **Organism:** *Variovorax paradoxus* strain P4B (`NCBITaxon:34073`)
- **Function:** Terminal bimodular nonribosomal peptide synthetase (`GO:1904091`) and C-terminal thioesterase (`GO:0016790`) in the variobactin/variochelin (`var`) lipopeptide siderophore biosynthetic gene cluster.

## Domain Architecture & Biosynthetic Role
- **Domain organization:** Two condensation/epimerization domains (`PF00668`: `E-C_NRPS` `cd19544` and `LCL_NRPS-like` `cd19531`), two PvdJ-like amino acid adenylation domains (`PF00501` / `cd17649`), two 4'-phosphopantetheinylated PCP domains (`PF00550` / `PROSITE:PS50075` at residues 1006-1080 and 2076-2153, modified at Ser1041 and Ser2111), and a C-terminal type I thioesterase domain (`PF00975` / `IPR001031`).
- **Evidence:** Incorporates the two C-terminal modified N-hydroxyornithine hydroxamate chelator monomers (synthesized by cluster tailoring enzymes `Var11` `ALG65346.1` lysine/ornithine N-monooxygenase and `Var12` `ALG65347.1` N-acyltransferase; established as N-delta-acetyl-N-delta-hydroxy-L-ornithine in *Variovorax* sp. H002 variochelins in [PMID:38590537], and combinatorialized across N-formylated, N-acetylated, or unmodified N-hydroxyornithine with monomer substitutions in *V. paradoxus* P4B variobactin A and B in [PMID:26412281]) and catalyzes thioesterase-mediated offloading of variobactin A and B ([PMID:26412281], [PMID:27023373] abstract-only). Cytoplasmic localization (`GO:0005737`, `ACCEPT`) is documented in `var7-bioinformatics/RESULTS.md` (`FT SIGNAL = 0`, `FT TRANSMEM = 0`).
