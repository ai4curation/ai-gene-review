# Curation Notes: var6 (A0A0N9LX43) in Variovorax paradoxus

## Overview
- **UniProt ID:** `A0A0N9LX43` (`A0A0N9LX43_VARPD`, 2,583 aa)
- **Gene symbol / GenBank protein:** `var6` (`ALG65341.1`, `EMBL:KT362218`)
- **Organism:** *Variovorax paradoxus* strain P4B (`NCBITaxon:34073`)
- **Function:** Bimodular nonribosomal peptide synthetase (NRPS, `GO:1904091`) in the variobactin/variochelin (`var`) hybrid PKS/NRPS lipopeptide siderophore biosynthetic gene cluster.

## Domain Architecture & Biosynthetic Role
- **Domain organization:** Three condensation/epimerization domains (`PF00668`: `LCL_NRPS-like` `cd19531`, `E_NRPS` `cd19534`, `DCL_NRPS` `cd19543`), two ATP-dependent amino acid adenylation domains (`PF00501` / `PF13193` / `IPR010071`), and two 4'-phosphopantetheinylated peptidyl-carrier protein (PCP) domains (`PF00550` / `PROSITE:PS50075` at residues 981-1055 and 2483-2557, modified at Ser1016 and Ser2517).
- **Evidence:** Johnston et al. 2015 ([PMID:26412281 "A second Variovorax isolate (V. paradoxus P4B (ref. 32)) was found to possess another distinct NRPS/PKS gene cluster, corresponding to a putative lipopeptide (Fig. 2b, Supplementary Fig. 17a and Supplementary Table 7)."]) sequenced the *V. paradoxus* P4B `var` cluster (`GenBank:KT362218`, where `var6` sits immediately downstream of `var5` `ALG65340.1` and upstream of `var7` `ALG65342.1`) and isolated variobactin A and B, noting `"several unforeseen amino-acid substitutions"` relative to the Ser/Thr-combinatorialized GNP prediction. Comparative characterization of the orthologous *Variovorax* `var` cluster in *V. boronicumulans* ([PMID:27023373], cached abstract-only) and *Variovorax* sp. H002 ([PMID:38590537 "The absolute configurations of the amino acid constituents, Pro, Ser and two modified ornithine residues, in 3–5 were assigned as ʟ, ᴅ, and ʟ, respectively (Figures S25, S33, and S41, Supporting Information File 1)."]) established D-Ser and L-Pro at the corresponding modules in variochelins. Cytoplasmic localization (`GO:0005737`, `NEW` `IC`) is documented in `var6-bioinformatics/RESULTS.md` (`FT SIGNAL = 0`, `FT TRANSMEM = 0`).
