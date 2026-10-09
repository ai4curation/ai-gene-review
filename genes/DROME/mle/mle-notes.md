# mle (P24785) review notes

## Identity
- DExH-box RNA helicase, RNA helicase A / DHX9 family; two N-terminal dsRBDs. [PMID:9184214 "Maleless protein (MLE) is highly homologous to human RNA helicase A"]

## Activities
- RNA/DNA helicase, ATPase, ssRNA/ssDNA binding in vitro; ATP-site mutant (mle-GET) dead and fails to rescue. [PMID:9184214 "this mutation abolished both NTPase and helicase activities of MLE"]
- Structure: uridine-specific DExH helicase; couples ATP hydrolysis to translocation. [PMID:26545078 "MLEcore is an unusual DExH helicase that can unwind blunt-ended RNA duplexes and has specificity for uridine nucleotides."]
- roX binding: iCLIP of roX tandem stem-loops [PMID:23870142 "MLE RNA helicase and MSL2 ubiquitin ligase, bind evolutionarily conserved domains containing tandem stem-loops in roX1 and roX2 RNAs in vivo"]; dsRBD structures [PMID:30649456; PMID:30805612].
- UNR facilitates MLE-roX2 interaction. [PMID:25158899]

## Localization
- Nuclear in both sexes; X-bound only in males. [PMID:1653648 "MLE is associated with hundreds of discrete sites along the length of the X chromosome in males and not in females."]

## Processes
- Dosage compensation; roX remodeling for DCC assembly. [PMID:26545078 "The MLE helicase remodels the roX lncRNAs, enabling the lncRNA-mediated assembly of the Drosophila dosage compensation complex."]
- napts allele: neural phenotypes (lifespan, song, arborization) - indirect via sodium channel. [PMID:16272407 "However, the mle napts strain exhibits significantly reduced life span"]

## Curation decisions
- RNA helicase / helicase / DNA-RNA helicase rows MODIFY -> GO:0034458 (already IMP). ATP hydrolysis rows KEEP_AS_NON_CORE (revised after deep research: ATPase and unwinding outputs are partly separable genetically).
- Shared MSL convention: GO:0072487 and GO:0016456 ACCEPT; chromosome rows MODIFY -> X chromosome; nuclear chromosome (25501352 4th-chromosome binding) ACCEPT.
- Nucleus ACCEPT for MLE (female nuclear pool not X-bound).
- DHX9-derived nucleolus IBA REMOVE; dsDNA binding, chromatin organization, cytoplasmic translation ISS MARK_AS_OVER_ANNOTATED.
- GO:0001069 (human DHX9 Alu paper) UNDECIDED - cannot see fly data.

## Deep research (falcon, added after initial review)
- `mle-deep-research-falcon.md` agrees: MLE is an ATP-dependent roX-remodeling helicase and assembly factor, not a histone-modifying enzyme ["In this pathway, MLE is an RNA-remodeling enzyme and assembly factor"]. It reports separable ATPase and helicase outputs in separation-of-function alleles, so ATP hydrolysis rows were changed from MODIFY to KEEP_AS_NON_CORE. It also notes the napts allele disrupts para transcript processing without MLE being the editing enzyme, and a 2024 MLE-CLAMP interaction (PMID:38471568).
