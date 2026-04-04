# ubiE (Pseudomonas aeruginosa PAO1) - Research Notes

## Gene Identity

- UniProt: Q9HUC0
- Ordered locus: PA5063
- EC: 2.1.1.163 (demethylmenaquinone methyltransferase), 2.1.1.201 (2-methoxy-6-polyprenyl-1,4-benzoquinol methylase)
- Family: Class I SAM-dependent methyltransferase superfamily, UbiE/COQ5 family

## Core Biochemistry

UbiE is a bifunctional SAM-dependent C-methyltransferase that catalyzes the penultimate C-methylation step in both ubiquinone (coenzyme Q) and menaquinone (vitamin K2) biosynthesis. The E. coli ortholog was originally identified by Lee et al. (1997), who demonstrated that ubiE mutants fail to catalyze the C-methylation reaction in both pathways [PMID:9045837 "Strains of Escherichia coli with mutations in the ubiE gene are not able to catalyze the carbon methylation reaction in the biosynthesis of ubiquinone (coenzyme Q) and menaquinone (vitamin K2), essential isoprenoid quinone components of the respiratory electron transport chain"]. The same study showed that disruption of ubiE causes accumulation of 2-octaprenyl-6-methoxy-1,4-benzoquinone and demethylmenaquinone as predominant intermediates [PMID:9045837 "E. coli strains containing either the disruption or the point mutation in ubiE accumulated 2-octaprenyl-6-methoxy-1,4-benzoquinone and demethylmenaquinone as predominant intermediates"].

The yeast ortholog COQ5 was independently characterized by Barkovich et al. (1997), who confirmed C-methyltransferase activity and mitochondrial localization [PMID:9083049 "The DNA segment responsible for the complementation contained an open reading frame (GenBankTM accession number Z49210Z49210) with 44% sequence identity over 262 amino acids to UbiE, which is required for a C-methyltransferase step in the Q and menaquinone biosynthetic pathways in Escherichia coli"].

## Dual Pathway Function

The enzyme has two distinct catalytic activities:

1. **Menaquinone pathway** (EC 2.1.1.163): Converts demethylmenaquinol (DMKH2) to menaquinol (MKH2) by methylating the C-3 position. This is the final step in menaquinone headgroup maturation.
2. **Ubiquinone pathway** (EC 2.1.1.201): Converts 2-polyprenyl-6-methoxy-1,4-benzoquinol (DDMQH2) to 2-polyprenyl-3-methyl-6-methoxy-1,4-benzoquinol (DMQH2).

In the mycobacterial ortholog (MenG/Rv0558), Pujari et al. (2022) demonstrated that the actual substrate is the reduced form (demethylmenaquinol), as addition of reductants stimulated activity [PMID:36417754 "Interestingly, addition of dithiothreitol, dithionite, NADH, or other substrates of primary dehydrogenases to reaction mixtures containing membrane preparations stimulated the activity. Thus, these observations strongly suggest that demethylmenaquinol is the actual substrate of MenG"].

## P. aeruginosa Quinone Biology

P. aeruginosa uses ubiquinone-9 (coenzyme Q9) as the primary electron carrier in its aerobic respiratory chain. Matsushita et al. (1980) established that ubiquinone is indispensable for respiratory chain function in P. aeruginosa [PMID:6774977 "Complete removal of ubiquinone performed by extracting the lyophilized membrane particles with n-pentane containing acetone resulted in complete loss of all oxidase activities for glucose, gluconate, malate, succinate, and NADH"]. The respiratory chain of aerobically grown P. aeruginosa contains coenzyme Q9 along with b-type and c-type cytochromes [PMID:6766443 "The electron transport chain of the gram-negative bacterium Pseudomonas aeruginosa, grown aerobically, contained a number of primary dehydrogenases and respiratory components (soluble flavin, bound flavin, coenzyme Q9, heme b, heme c, and cytochrome o)"].

Critically, Vo et al. (2020) demonstrated that UQ9 is required for anaerobic denitrification in P. aeruginosa, not just aerobic respiration [PMID:32409583 "we established that UQ is the major quinone of [P. aeruginosa] and is required for growth under anaerobic respiration (denitrification)"]. This means that both ubiquinone and menaquinone biosynthesis are physiologically relevant in this organism, and the ubiE C-methylation step is essential for both pathways.

## Role in Electron Transport

E. coli studies showed that menaquinone (but not demethylmenaquinone) is required for certain anaerobic electron transfer pathways. Tyson et al. (1997) demonstrated that ubiE mutants, which produce demethylmenaquinone but not menaquinone, retain some but not all respiratory activity [PMID:9325429 "A mutant defective in the methyltransferase activity involved in both ubiquinone synthesis and conversion of demethylmenaquinone to menaquinone expressed the same Nrf activity as the parental strain"]. This work also established that menaquinone is essential for cytochrome-c-dependent TMAO reductase and Nrf activities.

## Operon Context

In E. coli, ubiE is the first gene of an operon containing ubiE-yigP-ubiB [PMID:10960098 "the ubiE gene encodes a C-methyltransferase required for the synthesis of both CoQ and menaquinone, and it is the 5' gene in an operon containing ubiE, yigP, and ubiB"]. In P. aeruginosa PAO1, ubiE (PA5063) is similarly located in a genomic context with genes involved in quinone metabolism, identified through the complete genome sequence [PMID:10984043].

## SAM-Binding and Structure

The protein belongs to the class I SAM-binding methyltransferase superfamily (IPR029063) with a Rossmann-like fold. It contains the UbiE/COQ5 family signature (IPR004033) and conserved sites (IPR023576) that coordinate SAM binding. The protein has 256 amino acids with SAM-binding residues at positions 79, 100, and 128-129 (UniProt annotation by HAMAP rule MF_01813).

## Summary

P. aeruginosa ubiE (PA5063) encodes a bifunctional SAM-dependent C-methyltransferase that is required for the C-methylation step in both ubiquinone and menaquinone biosynthesis. Both products are essential for the branched respiratory chain of P. aeruginosa, which uses ubiquinone for both aerobic and anaerobic (denitrification) respiration. The protein is annotated entirely by homology transfer (no direct experimental evidence in P. aeruginosa), but the function is strongly supported by experimental characterization of orthologs in E. coli, yeast, and mycobacteria.
