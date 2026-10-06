# PRS5 notes (ribose-phosphate pyrophosphokinase subunit, UniProt Q12265)

## Gene-specific
- 496 aa with two NHRs; deletion reduces activity [PMID:9829955 "Loss of Prs5p has a significant impact on PRS enzyme activity, causing it to be reduced by 84%."]
- Synthetic lethal with prs1 / prs3 [PMID:9829955 "simultaneous deletion of PRS1 and PRS5 or PRS3 and PRS5 rendered the strains inviable"]
- Cytoophidia in quiescence [PMID:39836171 "CTPS cytoophidia are more prevalent in quiescent cells, forming complexes with Prs5 and Asn1 cytoophidia"] -> KEEP_AS_NON_CORE
- Adh7 interaction [PMID:17892321 "An additional interaction was confirmed between the alcohol dehydrogenase (NADP+) Adh7 and Prs5, the latter being a member of the PRS complex."] -> protein binding REMOVE (no functional follow-up).
- SGD IGI uses 'enables' for PRS5 but 'contributes_to' for PRS1-4; inconsistent since no subunit is active alone.

## PRS family evidence (shared)
- Five PRS genes; individual subunits inactive, specific pairs active in E. coli [PMID:15280369 "Expression of the five S. cerevisiae PRS genes individually in an Escherichia coli PRPP-less strain (Deltaprs) showed that a single PRS gene product had no PRPP synthase activity."]
- Active pairs [PMID:15280369 "These combinations were PRS1 PRS2, PRS1 PRS3, and PRS1 PRS4, as well as PRS5 PRS2 and PRS5 PRS4."]; stable enzyme needs >=3 subunits [PMID:15280369 "yeast PRPP synthase requires at least three different subunits to be stable in vitro"]
- Genetic architecture: [PMID:10212224 "a lethal phenotype that corresponds to strains containing a double disruption in PRS2 and PRS4 in combination with a disruption in either PRS1 or PRS3"]; Y2H [PMID:10212224 "Specifically PRS1 and PRS3 polypeptides interact strongly with each other, and there are significant interactions between the PRS5 polypeptide and either the PRS2 or PRS4 polypeptides."]
- PRPP use [PMID:9829955 "PRPP is required for the production of purine, pyrimidine, and pyridine nucleotides and the amino acids histidine and tryptophan"]
- Conserved motifs [PMID:9829955 "contains the characteristic motifs of PRS enzymes, the divalent cation binding site (DCbs) and the PRPP binding site (PRPPbs)"]
- Localization: cytoplasm by GFP [PMID:14562095; UniProt "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:14562095}."]
- Pairwise Prs-Prs 'protein binding' IPIs (Gavin, Betel, Tarassov, Yu, Michaelis, Uetz, Ito) all reflect hetero-oligomer assembly [PMID:17892321 "Among the experimentally confirmed predictions were interactions between the five components of the PRS complex, which together compose the 5-phosphoribosyl-1(a)-pyrophosphate synthetase enzyme (EC number 2.7.6.1)."] -> REMOVE as uninformative; captured by GO:0002189.

## Curation decisions (shared)
- Core: contributes_to GO:0004749 (no subunit active alone; matches SGD IGI 'contributes_to' qualifiers), GO:0006015, cytosol, in_complex GO:0002189.
- Downstream BPs (purine nucleotide biosynthesis IBA, nucleotide biosynthesis IEA/RCA from superpathway PRPP-PWY-1, ribonucleoside monophosphate biosynthesis IEA) -> KEEP_AS_NON_CORE: PRPP is a precursor; GO:0006015 is not part_of these.
- Mg2+ binding IEA -> KEEP_AS_NON_CORE (DCbs motif).
