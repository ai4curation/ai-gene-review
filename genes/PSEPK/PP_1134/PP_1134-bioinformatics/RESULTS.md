# PP_1134 (Q88NS1) bioinformatics

Scripts in this folder; numbers come from BERIL runs in `projects/hackathon/runs/`:

- `homology.py` -> run `20261030T213754Z-pp1134-homology` (copied to `../PP_1134-dashboard-prediction-evidence/homology_results.json`)
- `fb_fitness.py` -> run `20261030T213420Z-pp1134-fitness` (copied to `../PP_1134-dashboard-prediction-evidence/fitness_results.json`)

## Dashboard query vs Q88NS1

The dashboard query (NZ_BCAU01000123.1_43, 543 aa) aligns to Q88NS1 (535 aa) over query 9-543 / subject 1-535: 533 identical of 535 aligned pairs (99.6%). The 8 extra query residues are an N-terminal extension MAGILDPA from an upstream start codon call; the two substitutions are query D234/subject E226 and query L506/subject I498. The KT2440 start (MLRITELK...) matches the start of the 3NLC homolog (MIRINEIK...), so the shorter KT2440 model is probably the real start.

## Homologs (NCBI BLAST of Q88NS1, E <= 1e-5)

- Swiss-Prot: one hit only, Q05627 (Cbei_0202, "Uncharacterized protein", Clostridium beijerinckii), 48.0% identity over 529 aligned residues. No characterized protein of any FAD-oxidoreductase family (UbiI/UbiH/2-polyprenylphenol hydroxylases, FixC, ETF-QO, geranylgeranyl reductases) is detected at this threshold.
- PDB: one hit only, 3NLC chain A (VP0956, Vibrio parahaemolyticus; NESG target VpR147, 2.15 A), 67.5% identity over 533 aligned residues. 3NLC contains bound FAD (non-polymer entity 2, comp_id FAD). No publication describes an activity for VP0956.

## Family

InterPro IPR028348 (PIRSF038984) "FAD dependent protein": "This entry represents uncharacterised FAD dependent proteins. Their function is not clear." IPR049516 / PF21688 is a C-terminal domain inserted in the FAD/NAD(P)-binding domain, "whose exact function is not yet clear". PANTHER PTHR42842 (SF3), COG2509 ("FAD-dependent dehydrogenase", general function prediction only), KEGG K07137 ("uncharacterized protein"). Pfam PF28550 (DUF8436) covers residues 1-60. The only reviewed UniProtKB entry carrying IPR028348, IPR049516, PF28550 or PIRSF038984 is the uncharacterized Q05627.

## Fitness (KT2440, orgId Putida, BERDL kescience.fitnessbrowser)

PP_1134 was measured in 300 experiments. No experiment passes |fit| >= 1 with |t| >= 4; no |t| >= 4 at all. Range -0.59 (propanediamine as N source, t -3.2) to +0.47 (DL-2-aminobutyrate as N source, t 3.6). No specific-phenotype entry. Top cofitness partner is PP_0567 (arginine decarboxylase) at 0.44; no partner exceeds 0.44, so cofitness is uninformative. Neighbours PP_1130-PP_1136 likewise have no strong phenotypes; only the branched-chain amino acid ABC transporter genes PP_1137-PP_1139 do.

## Neighbourhood (KT2440)

PP_1132 NhaA (-), PP_1133 IS transposase (+), PP_1134 (-), PP_1135 conserved exported protein of unknown function (-, ~100 bp downstream), PP_1136 conserved protein of unknown function (+), PP_1137-PP_1139 Liv-type ABC transporter (-). In P. simiae and P. fluorescens the NhaA / SlyB / putative-lipoprotein neighbours are conserved, but none points to a substrate.
