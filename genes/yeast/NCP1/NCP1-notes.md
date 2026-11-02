# NCP1 (YHR042W, P16603) review notes

## Identity
- NADPH--cytochrome P450 reductase (CPR), EC 1.6.2.4, diflavin (FAD + FMN) reductase; synonyms CPR1, PRD1 [UniProt:P16603].
- Single-pass membrane protein anchored by an N-terminal segment, catalytic domain on the cytoplasmic side; ER membrane is the main location; also detected in mitochondrial outer membrane proteomes and isolated plasma membranes [UniProt:P16603].

## Activity
- Purified recombinant native and N-terminally truncated CPR reduce cytochrome c and reconstitute CYP61 (Erg5) sterol Delta22-desaturation [PMID:11485306 "Protein functionality was demonstrated by cytochrome c reduction and reconstitution of CYP61-mediated sterol Delta(22)-desaturation."].
- CYP51-CPR fusion is catalytically active with NADPH [PMID:9087488 "FUS protein catalyzed the demethylation of substrate at the 14alpha position"].
- Catalyses NADPH-dependent ferrireductase activity of isolated plasma membranes, but not essential for cellular ferrireductase activity [PMID:9368374 "Cytochrome P-450 reductase (encoded by the NCP1 gene) was found to catalyse all the NADPH-dependent ferrireductase activities associated with isolated plasma membranes"].
- In vitro, Ncp1/NADPH can reduce Dph3 and support the first step of diphthamide synthesis, slower than Cbr1 (physiological relevance unclear) [PMID:27694803 "both Mcr1 and Ncp1 reduced Dph3 at a slower rate compared to that of Cbr1 under similar reaction conditions"].

## Ergosterol biosynthesis role
- ncp1 disruption is viable, ~25% ergosterol [PMID:9468503 "resulted in a viable strain accumulating approximately 25% of the ergosterol observed in a sterol wild-type parent"]; electron donor to squalene epoxidase (Erg1), CYP51 (Erg11) and CYP61 (Erg5) [PMID:9468503 "function with the monooxygenases squalene epoxidase, CYP51, and CYP61 in the ergosterol biosynthesis pathway"].
- Deletion makes cells 200-fold more ketoconazole sensitive; an alternative electron supply exists [PMID:2543395 "suggesting that an alternate pathway may provide for the functions of this reductase in S. cerevisiae."]; the alternative is cytochrome b5 (CYB5), a multicopy suppressor [PMID:8181746 "yeast cytochrome b5-encoding gene (CYB5), which encodes a 120-amino-acid (aa) protein, is required and sufficient for the suppressor effect"].

## Curation conclusions
- Core MF GO:0003958 NADPH-hemoprotein reductase activity; BP GO:0006696; CC GO:0005789 ER membrane.
- IBA "cytosol" from a diflavin-reductase node that includes NOS, MTRR, NDOR1/TAH18 does not fit the membrane-anchored CPR: removed.
- Mitochondrial outer membrane / plasma membrane detections kept as non-core.
- YeastCyc lists the reductase only as a generic reactant of the ERG1/ERG11/ERG5 reactions; the module adds NCP1 explicitly.
