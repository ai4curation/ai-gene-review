# COQ4 (YDR204W, UniProt O13525) – review notes

## Function
- Cloned by complementation of a Q-deficient mutant; peripheral protein on the matrix face of the inner membrane [PMID:11469793 "Coq4p was shown to peripherally associate with the matrix face of the mitochondrial inner membrane"]. At that time the function was unknown [PMID:11469793 "The function of Coq4p is unknown"].
- coq4 mutants make no Q and accumulate 3-hexaprenyl-4-hydroxybenzoate (HHB) [PMID:9266513 "Q mutant strains harboring mutations in the coq3, coq4, coq5, coq6, coq7, or coq8 genes were unable to produce Q"].
- Structural organizer of the CoQ synthome [PMID:24406904 "indicating that Coq4 is a central organizer of the Coq complex"].
- Catalytic role: COQ4 performs C1 decarboxylation + hydroxylation as a single oxidative decarboxylation [PMID:38295803 "these two reactions occur in a single oxidative decarboxylation step catalyzed by COQ4"]. Evidence is complementation of E. coli ubiD/ubiX-ubiH defects and activity in C. glutamicum; the abstract does not specify which COQ4 ortholog(s) were used.
- UniProt: EC 4.1.1.130 by similarity (HAMAP MF_03111); Zn2+ cofactor by similarity [UniProt:O13525 "Name=Zn(2+)"].

## GO notes
- GO:0120539 (4-hydroxy-3-methoxy-5-polyprenylbenzoate decarboxylase) is the right MF; GO definition cites PMID:38295803. The companion GO:0120538 (2-methoxy-6-polyprenylphenol 4-hydroxylase, ferredoxin-dependent) is defined as a separate reaction; PomBase GO-CAM 662af8fa00000408 assigns GO:0120538 to coq6 whereas Pelosi et al. attribute both C1 reactions to COQ4.
- CC: extrinsic component of mitochondrial inner membrane (matrix side) is the most precise location; complex membership = GO:0110142 ubiquinone biosynthesis complex (definition explicitly includes COQ4).
- ND root MF from SGD is superseded by GO:0120539 IBA/IEA.

## YeastPathways
- YeastPathways PWY3O-19 / PWY3O-862 have no gene for the decarboxylation (RXN3O-73) and assign C1 hydroxylation (RXN3O-12) to COQ6; COQ4 is absent from YeastCyc entirely (no COQ4 reactions in the summary file).
