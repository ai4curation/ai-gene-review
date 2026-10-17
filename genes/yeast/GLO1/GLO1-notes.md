# GLO1 (YML004C) notes

UniProt P50107; glyoxalase I, EC 4.4.1.5 [UniProt:P50107].

## Evidence journal
- Structural gene identified: multicopy GLO1 raises activity ~95-fold and confers methylglyoxal resistance; knockout viable [PMID:8824231 "Glyoxalase I activity increased approximately 95-fold when the GLO1 gene was introduced into the yeast cell with a multicopy plasmid, and the resultant transformant showed the increased resistance against methylglyoxal"].
- Glutathione dependence: gsh1 mutants hypersensitive to methylglyoxal, not rescued by Glo1 overproduction [PMID:8824231 "The gsh1-deficient mutant, which could not produce glutathione at all, was hypersensitive to methylglyoxal"].
- Alternative thiol substrate gamma-glutamylcysteine (much lower kcat/Km) [PMID:8824231 "Purified glyoxalase I from yeast could use gamma-glutamylcysteine as a substrate"].
- Monomer with two functional active sites (E163, E318 Zn ligands); metals probably Fe(II) + Zn(II), Mn can replace Zn [PMID:11050082 "Steady-state kinetics and metal analyses of the recombinant enzymes corroborate that yeast glyoxalase I has two functional active sites"].
- HDA GFP: nucleus + cytoplasm [PMID:14562095]. No evidence for a nuclear function.
- Zinc binding RCA from bioinformatic zinc-proteome survey [PMID:30358795].

## Pathway context
YeastPathways PWY-901 step 1 (methylglyoxal + GSH -> (R)-S-lactoylglutathione) is correct. Downstream: GLO2 (cytosol) / GLO4 (mitochondrial matrix).

## Decisions
- All MF/BP lyase and methylglyoxal catabolism rows ACCEPT.
- GO:0006749 glutathione metabolic process (IMP) KEEP_AS_NON_CORE (GSH is co-substrate; specific process is methylglyoxal catabolism).
- nucleus HDA, zinc/metal binding KEEP_AS_NON_CORE.
