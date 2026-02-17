# Hsp14 (Saci_1665, Q4J8A6) - Research Notes

## Overview

Hsp14 is a small heat shock protein (sHSP) of the alpha-crystallin/Hsp20 family from the thermoacidophilic crenarchaeon *Sulfolobus acidocaldarius*. It is 126 amino acids (14.3 kDa). *S. acidocaldarius* grows optimally at 75-80 degrees C and pH 2-3, and has a minimalist chaperone repertoire: Hsp14, Hsp20, and Hsp60 (a group II chaperonin/thermosome). Notably, Hsp70 is absent from this organism [PMID:34637594 "Hsp70 is absent in thermophilic and hyperthermophilic archaea"].

## Key Publications

### PMID:34637594 - Roy et al. (2022) FEBS J
"Archaeal Hsp14 drives substrate shuttling between small heat shock proteins and thermosome"

Key findings:
- Hsp14 dimer is the active form; forms oligomeric storage form at higher temperature [PMID:34637594 "the dimer is the active form of Hsp14, and it forms an oligomeric storage form at a higher temperature"]
- Rapid subunit exchange between dimeric states; rate increases with temperature [PMID:34637594 "the dynamics of the Hsp14 oligomer are maintained by rapid subunit exchange between the dimeric states"]
- Forms hetero-oligomers with Hsp20 at 50-70 degrees C via subunit exchange [PMID:34637594 "hetero-oligomer formation only at higher temperatures (50-70 degrees C)"]
- Direct physical interaction between Hsp14 and Hsp60 (thermosome), enthalpy-driven [PMID:34637594 "an enthalpy-driven direct physical interaction between Hsp14 and Hsp60"]
- Hsp14 transfers sHsp-captured substrate proteins to Hsp60 for refolding [PMID:34637594 "Hsp14 could transfer sHsp-captured substrate proteins to Hsp60, which then refolds them back to their active form"]
- Fills the substrate transfer role normally played by Hsp70 in other organisms [PMID:34637594 "In the absence of Hsp70, how aggregating protein substrates are transferred to Hsp60 for refolding remains elusive"]

### PMID:37516156 - Bhowmick et al. (2023) Res Microbiol
"Heat shock response in Sulfolobus acidocaldarius and first implications for cross-stress adaptation"

Key findings:
- hsp14 and hsp20 play crucial roles in the majority of stress conditions [PMID:37516156 "the gene thB encoding the B subunit of the thermosome, as well as hsp14 and hsp20, play crucial roles in the majority of stress conditions"]
- Upregulated under heat shock (92 degrees C), oxidative stress, and nutrient stress [PMID:37516156 "we assessed the expression of these selected genes under oxidative and nutrient stresses"]

### PMID:32562000 - Baes et al. (2020) Extremophiles
"Defining heat shock response for the thermoacidophilic model crenarchaeon Sulfolobus acidocaldarius"

Key findings:
- Dynamic increase in mRNA levels of all relevant heat shock proteins upon heat shock [PMID:32562000 "a dynamic increase in mRNA levels of all relevant heat shock proteins"]
- S. acidocaldarius does not seem better equipped to handle sudden supra-optimal temperature stress than mesophilic organisms [PMID:32562000]

## Molecular Functions

1. **Unfolded protein binding** (GO:0051082) - Hsp14 binds aggregating/unfolded substrate proteins [PMID:34637594]
2. **Unfolded protein carrier activity** (GO:0140309) - Hsp14 shuttles captured unfolded substrates from sHSPs to the thermosome (Hsp60) for ATP-dependent refolding [PMID:34637594]. This is the most distinctive function.
3. **Protein-folding chaperone binding** (GO:0051087) - Direct physical interaction with Hsp60 (thermosome) [PMID:34637594]

## Biological Processes

1. **Response to heat** (GO:0009408) - Upregulated under heat shock [PMID:32562000, PMID:37516156]
2. **Protein folding** (GO:0006457) - Participates in the sHSP-to-thermosome protein folding pathway [PMID:34637594]

## Cellular Component

1. **Cytoplasm** (GO:0005737) - sHSPs are cytoplasmic proteins

## Domain Architecture

- Alpha-crystallin domain (ACD) (Pfam: PF00011, HSP20)
- SHSP domain (aa 21-126, PROSITE PS01031)
- InterPro: IPR002068 (A-crystallin/Hsp20_dom), IPR008978 (HSP20-like_chaperone)
- NCBIfam: NF041799 (Hsp14)
