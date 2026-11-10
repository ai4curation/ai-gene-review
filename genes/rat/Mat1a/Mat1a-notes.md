# Mat1a (rat, P13444) review notes

## Identity
- UniProt P13444 (METK1_RAT), S-adenosylmethionine synthase isoform type-1, 397 aa; RGD:3050; GeneID 25331. Fetched accession matches the requested one.
- Belongs to the AdoMet synthase family (Pfam PF00438/PF02772/PF02773; InterPro IPR002133).

## Function (literature, cached publications)
- Catalyses SAM synthesis from L-methionine and ATP [file:rat/Mat1a/Mat1a-uniprot.txt "Catalyzes the formation of S-adenosylmethionine from methionine and ATP"].
- Liver isoenzyme exists as MAT I tetramer and MAT III dimer [PMID:10873471 "The liver enzyme exists in two oligomeric forms, a tetramer (MAT I) and a dimer (MAT III)"]; tetramers and dimers are in equilibrium [PMID:9202427 "these two isoforms might be in equilibrium"].
- Crystal structure (2.7 A) of MAT I with methionine analogue: methionine site at active-site cavity, Phe251 stacking, carboxylate coordinating Mg2+ linked to Asp180 [PMID:10873471 "its carboxylate group coordinates a Mg(2+), which, in turn, is linked to Asp180"].
- Substrate/product complexes define methionine-ATP recognition; Lys182 and Asp135* key [PMID:12888348 "we propose a key role for Lys182 in the correct positioning of the substrates"].
- Redox regulation: GSSG inhibits and dissociates oligomers [PMID:1517209 "inhibition of enzyme activity was correlated with dissociation of both AdoMet synthetases to a monomer"]; S-nitrosylation inactivates in vivo [PMID:9755242 "the activity of liver MAT appears to be regulated in vivo by S-nitrosylation"].
- Nucleocytoplasmic distribution; nuclear matrix association in extrahepatic tissues; nuclear fractions synthesize SAM [PMID:19497982 "Nuclear localization was the preferred distribution observed in extrahepatic tissues, where the protein colocalizes with nuclear matrix markers"].
- Alcoholic liver injury model: MAT1A mRNA doubled but protein unchanged; liver-specific MAT activity falls with LPS [PMID:10898761 "Although liver-specific MAT activity did not change, it was 32% lower after one and 68% lower after eight weekly enteral doses of lipopolysaccharide"].
- Betaine supplementation upregulates MAT-1 protein in ethanol-fed rat liver cytosol (proteomics) [PMID:19239903 "Significant upregulation of betaine homocysteine methyltransferase-1, methionine adenosyl transferase-1, and glycine N-methyltransferase were the most visually prominent protein changes"]. This is expression evidence only; it supports cytosolic presence in liver but does not justify any new process term.

## Decisions
- All MAT activity / SAM biosynthesis rows ACCEPT (core).
- Cytosol ACCEPT; nuclear matrix KEEP_AS_NON_CORE.
- ATP / Mg2+ / amino acid / ADP binding: KEEP_AS_NON_CORE (substrate/cofactor/ligand binding subsumed by catalytic activity). No "L-methionine binding" GO term exists (OLS search), so amino acid binding is as precise as available.
- identical protein binding and MAT complex ACCEPT (active site lies at subunit interface; obligate homo-oligomer).
- protein-containing complex assembly -> MODIFY to protein homooligomerization (GO:0051260), which covers both MAT I tetramer and MAT III dimer.
- L-methionine catabolic process KEEP_AS_NON_CORE (SAM synthesis is first step of hepatic methionine clearance).
- No NEW terms proposed.
