# KT2440 OpgG: orthology, chemistry and physiological scope

The target is Q88D03/PP_5026, a 559-residue KT2440 protein with the OpgG-specific HAMAP MF_01069, InterPro IPR023704 and PANTHER PTHR30504:SF4 classification. This supports OpgG identity rather than assigning a function to every OpgD/OpgG-family member.

PMID37735577 cloned BL21(DE3) CAQ31569.1, removed a predicted signal sequence, added C-terminal His6 and expressed the recombinant protein in BL21(DE3). The 511-residue native precursor sequence is identical to frozen K-12 P33136; this bridges protein sequence, not native-strain physiology. The D361N glucan-bound structure is a mutant, whereas the weak hydrolysis assay used wild-type recombinant OpgG. Author numbering in deposited 8IP2 follows precursor positions; modeled chain A starts at residue 22, which does not independently prove the exact cloning boundary.

The reproducible global alignment in map_opgg.py maps E. coli OpgG D273/R332/D361 to KT2440 D268/R327/D356 and Loop A S415/L417 to S410/L412. Ligand-contact Y56 maps to F51. Conserved catalytic-pocket and OpgG-like loop features support homologous glycan chemistry but do not prove identical geometry or kinetics. There are 356 identical residues across 566 alignment columns including gaps (parameters and source hashes in residue-map.json). This independently computed alignment is not a reproduction of the provider's differently parameterized percent-identity calculation.

The biochemical paper reports OpgG activity of 0.11 U/mg, and 0.79% relative to OpgD at 8 mg/mL substrate. Poor Michaelis–Menten fitting prevented an equivalent OpgG kinetic characterization. The authors interpret OpgG as intrinsically hydrolytic but explicitly retain possible cofactor dependence and transglycosylation. No KT2440 assay or in-vivo cleavage/product assignment follows from these results. OpgD-like chain-length control, OpgG branching, and OpgG-OpgH physical cooperation are not interchangeable established mechanisms.

Short source quotations (cached PMID37735577):

- “EcOpgG was found to hydrolyze β-1,2-glucans; however, the catalytic velocity was very low”
- “The relative activity against EcOpgD was only 0.79% at 8.0 mg/mL β-1,2-glucan”
- “The possibility that EcOpgG is in fact a transglycosylase of the β-1,6-glucose side chain remains open.”
- “In the catalytic pocket of the complex, the electron density of a Sop16 molecule was observed”

Current official QuickGO checks (2026-11-06): GO0033913 describes random hydrolysis of 1→2 linkages in beta-D-glucans, not the OPG pathway or native flux. GO0030247 polysaccharide binding is an is_a child of carbohydrate binding GO0030246. A bound Sop16 molecule supports polysaccharide recognition in the homolog; target transfer remains inference. GO1900727 descends from glucan/carbohydrate biosynthesis and carbohydrate metabolism, but not from GO0051274 beta-glucan biosynthesis in the retrieved is_a/part_of closure; replacing the latter is a pathway-specific lateral interpretation, not a claimed ontology-descendant relationship. Source URLs: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033913 ; https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030246 ; https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030247 ; https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1900727/ancestors?relations=is_a,part_of . Raw API responses are preserved in the ignored audit cache.

The Pseudomonas primary PMID17906125 explicitly studies PA14 opgGH, not KT2440; its cached abstract describes beta-1,2-linked glucans with some beta-1,6 branches and succinyl substituents. It supports comparative pathway assignment, not exact KT2440 product structure or a purified OpgG reaction. PMID15313617 is abstract-only structural context and proposed branching, not demonstrated catalysis.
