# DYNC2I2 (Q96EX3) research notes

Cytoplasmic dynein 2 intermediate chain 2 (WDR34; FAP133 homolog), human.

## Deep research status
Falcon deep research succeeded (`DYNC2I2-deep-research-falcon.md`; the first attempt with the 600 s default timed out, and the rerun with --timeout 2400 succeeded). Its summary agrees with the publication-based review below. The review's supporting quotes come from the cached publications.

## Summary of function
- A dynein-2 intermediate chain. [PMID:25205765 "The above data indicate that both WDR34 and WDR60 are intermediate chains of the dynein-2 complex."] Localization: [PMID:25205765 "mGFP–WDR34 localizes to centrosomes and primary cilia in serum-starved cells as well as showing a diffuse cytoplasmic distribution."]
- Light-chain binding sites: [PMID:30649997 "In this study, we demonstrated that the WDR34 intermediate chain interacts with the two light chains, DYNLL1/DYNLL2 and DYNLRB1/DYNLRB2, via its distinct sites."; "These observations together indicate that interactions of WDR34 with both DYNLL1/DYNLL2 and DYNLRB1/DYNLRB2 are essential for dynein-2–mediated retrograde trafficking of ciliary proteins."]
- KO phenotype: [PMID:30320547 "we show that WDR34 KO cells can assemble a dynein-2 motor complex that binds IFT proteins yet fails to extend an axoneme, indicating complex function is stalled"]
- Structure: WDR34 propeller binds heavy chain B (PMID:31451806).
- Non-ciliary report: TAK1-associated suppressor of IL-1R/TLR NF-kB signalling. [PMID:19521662 "Our findings suggest that WDR34 is a TAK1-associated inhibitor of the IL-1R/TLR3/TLR4-induced NF-kappaB activation pathway."] GOA carries no annotation for this (only cytoplasm EXP from this paper). It is mentioned in the description and in a suggested question.
- Disease: SRTD11 (Jeune/SRPS).

## Key curation decisions
- Protein binding: WDR60 rows changed (MODIFY) to dynein intermediate chain binding. DYNLL2 and DYNLRB1 rows changed to dynein light chain binding. HT Y2H rows (COIL, TRIM54, MEOX2 partners) REMOVE.
- Filopodium (IEA from mouse): UNDECIDED, because the primary evidence could not be accessed.
- Retrograde IFT IMP cited to PMID:29742051: WDR34-specific data were not found in the cached text. Accepted on the strength of PMID:30649997.

## HPA cilium atlas vs module role
- Module stage 4: dynein-2 intermediate chain; retrograde IFT motor.
- HPA v25: Primary cilium (Approved), Basal body (Supported), Centrosome (Supported); main locations Basal body, Centrosome and Nucleoplasm. GOA HPA rows: centrosome (non-core), cytosol (non-core), ciliary basal body (ACCEPT).
- Assessment: consistent with the module role and with published basal-body accumulation. The HPA nucleoplasm signal has no published functional counterpart and is not annotated in GOA. core_functions: contributes_to minus-end-directed MT motor activity, retrograde IFT, dynein light chain binding, cilium assembly. No disagreement.
