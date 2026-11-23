# ILV1 (YER086W, P00927) notes

- Biosynthetic threonine dehydratase EC 4.3.1.19, mitochondrial [UniProt:P00927 "RecName: Full=Threonine dehydratase, mitochondrial;"]; reaction [UniProt:P00927 "Reaction=L-threonine = 2-oxobutanoate + NH4(+)"].
- Allosteric regulation [UniProt:P00927 "ACTIVITY REGULATION: Isoleucine allosterically inhibits while valine"]; [PMID:7042346 "Whereas the anabolic enzyme is an allosteric enzyme sensitive to feedback inhibition by isoleucine"].
- Location: mitochondrion by GFP (PMID:14562095) and proteomics (PMID:14576278, 16823961, 24769239) [UniProt:P00927 "SUBCELLULAR LOCATION: Mitochondrion"].
- Classical genetics: is-1 mutant with altered threonine deaminase (PMID:5345980; title-only cache).
- Relationship with CHA1: [PMID:7042346 "Saccharomyces cerevisiae mutants lacking the anabolic L-threonine deaminase, the ilv1- mutants, have been found to exhibit a normal ability to grow, without auxotrophy towards isoleucine, on L-threonine of L-serine as only nitrogen nutrient"]; the two [PMID:7042346 "display a limited ability to compensate for one another's absence and appear to play clearly distinct roles under normal physiological conditions"].

## Curation observations
- RCA cytosol rows (2) contradict mitochondrial location -> REMOVE.
- IGI L-threonine catabolic process (with CHA1) kept as non-core (backup).
- Module: Ilv1 is the yeast biosynthetic IlvA-family entry enzyme; Cha1 is a catabolic paralog in the same PANTHER family (PTHR48078 SF2 vs SF11) and should not satisfy the biosynthetic step except as a minor backup.
