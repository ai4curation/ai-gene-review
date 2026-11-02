# Prx4 (Jafrac2, DPx-4156, CG1274; Q9V3Q4) notes

## Identity check
- UniProt Q9V3Q4 gene synonyms include DPx-4156, Jafrac2 and dPrx4 (CG1274, FBgn0040308): Prx4 is the protein called Jafrac2 by Tenev et al. 2002, so PMID:12356728 does concern this gene.
- Typical 2-Cys peroxiredoxin (AhpC/Prx1 subfamily) with a 1-17 signal peptide (UniProt FT SIGNAL 1..17); mature chain begins at Ala18 ("AKPE..."), matching an N-terminal IAP-binding motif.

## Literature journal
- 2-Cys Prx with thioredoxin-dependent peroxidase activity [PMID:11677042 "The three 2-Cys Prx were also shown to be active in the thioredoxin system and were, consequently, classified as thioredoxin peroxidases"]; one family member secreted [PMID:11677042 "one was found to be secreted"].
- IAP antagonist claim [PMID:12356728 "We have identified the thioredoxin peroxidase Jafrac2 as an IAP-interacting protein in Drosophila cells that harbours a conserved N-terminal IAP-binding motif"; "In healthy cells, Jafrac2 resides in the endoplasmic reticulum but is rapidly released into the cytosol following induction of apoptosis"; "Jafrac2 displaces Dronc from DIAP1 by competing with Dronc for the binding of DIAP1"].
- In vivo physiology [PMID:23271054 "Reduced expression of dPrx4 (up to 90%) resulted in greater sensitivity to oxidative stress, an elevated H₂O₂ flux, and increases in lipid peroxidation, but no effect on longevity"]; overexpression causes redistribution and apoptosis [PMID:23271054 "aberrant redistribution of the dPrx4 protein from the endoplasmic reticulum (ER) to cytosol and hemolymph"]; JAK/STAT [PMID:23271054 "dPrx4, on secretion into the hemolymph, elicits a JAK/STAT-mediated response"]; stress-induced secretion [PMID:23271054 "found a prominent increase in the dPrx levels in the hemolymph of flies subjected to septic injury, cold, or paraquat treatment"].
- Hyperoxidation of 2-Cys Prxs [PMID:33920774].

## Assessment of the IAP-antagonist role (requested check)
- Evidence: a single primary study (Tenev et al. 2002) with co-IP/binding to DIAP1 BIR2, competition with Dronc, motif-mutant (N-terminal Ala) loss of DIAP1 binding and of eye-ablation activity, and genetic suppression by reduced dronc dosage (per abstract and falcon deep research summary of the full text). The 2013 study refers to "the known proapoptotic effects of the cytosolic form of dPrx4" and observed apoptosis on strong overexpression, but did not independently test DIAP1 binding.
- Limits: all death-promoting evidence is gain-of-function (overexpression/ectopic expression) or in cultured cells; no loss-of-function study shows Prx4 is required for developmental or stress-induced apoptosis; the full text is not in the local cache. The claim is therefore plausible and curator-annotated, but is a single-lab, overexpression-based finding.
- Conclusion: the IAP-antagonist activity is kept as a non-core, conditional (stress-released cytosolic pool) role; Prx4's core function is ER-luminal thioredoxin-dependent peroxide reduction. Its membership in an RHG/apoptosome caspase-activation module should be treated as peripheral and flagged as resting on one study.

## Curation thoughts
- Obsolete thioredoxin peroxidase activity IBA -> thioredoxin-dependent peroxiredoxin activity.
- Determination of adult lifespan (IEA): knockdown had no longevity effect -> over-annotated.
