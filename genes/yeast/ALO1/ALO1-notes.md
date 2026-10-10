# ALO1 (YML086C, P54783) review notes

## Identity
- D-arabinono-1,4-lactone oxidase (ALO), EC 1.1.3.37; also oxidises L-gulono- and L-galactono-1,4-lactone; FAD-linked oxidoreductase (VAO/aldonolactone oxidoreductase group), covalent FAD [UniProt:P54783].
- Homology to animal GULO and plant GLDH [PMID:10094636 "The deduced amino acid sequence of the enzyme shared 32% and 21% identity with that of L-gulono-1,4-lactone oxidase from rat and L-galactono-1,4-lactone dehydrogenase from cauliflower"].

## Location
- Purified from mitochondrial fraction [PMID:10094636 "D-Arabinono-1,4-lactone oxidase catalysing the final step of D-erythroascorbic acid biosynthesis was purified from the mitochondrial fraction of Saccharomyces cerevisiae."].
- Mitochondrial outer membrane, found in MOM proteome (PMID:16407407, PMID:16689936) and described as MOM-located with Myo2 interaction [PMID:39775849 "One robust hit was Alo1, a poorly characterized D-arabinono-1,4-lactone oxidase located in the mitochondrial outer membrane."].
- YeastCyc/GO-CAM default "cytosol" is wrong for this membrane protein.

## Function
- Erythroascorbate synthesis: [PMID:10094636 "In the alo1 mutants, D-erythroascorbic acid and the activity of D-arabinono-1,4-lactone oxidase could not be detected."]
- Oxidative stress: [PMID:10094636 "The alo1 mutants showed increased sensitivity towards oxidative stress, but overexpression of ALO1 made the cells more resistant to oxidative stress."]; but erythroascorbate's antioxidant importance questioned [PMID:11281285 "suggests that erythroascorbate is of limited importance as an antioxidant in S. cerevisiae"].
- Newly: Myo2 cargo-binding domain interactor; alo1 mutants have mitochondrial morphology/inheritance defects [PMID:39775849 "We found that mutants lacking Alo1 exhibited defects in mitochondrial morphology and inheritance."]; proposed Myo2 recruitment role [PMID:39775849 "We propose that Alo1 supports the recruitment of Myo2 to mitochondria"].

## Curation conclusions
- Core MF GO:0003885; BP GO:0070485; location mitochondrial outer membrane (GO:0005741); the module currently uses the less specific GO:0031966 mitochondrial membrane.
- Mitochondrial inheritance / myosin V binding: new moonlighting role, non-core.
- Cytosol (RCA) -> modify to MOM.
