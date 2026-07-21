# hemC assessment notes

## Identity and core reaction

Q88RE5 (PP_0186) is a reviewed HemC/HMBS-family porphobilinogen deaminase
assigned EC 2.5.1.61. UniProt supports tetrapolymerization of four
porphobilinogen molecules to hydroxymethylbilane, a covalently bound
dipyrromethane cofactor, monomeric state, and the protoporphyrin precursor
pathway
[file:PSEPK/hemC/hemC-uniprot.txt "Tetrapolymerization of the monopyrrole PBG into the"]
[file:PSEPK/hemC/hemC-uniprot.txt "Binds 1 dipyrromethane group covalently"].

## OpenScientist assessment

The OpenScientist report correctly identifies Q88RE5/PP_0186 and recovers the
conserved HMBS reaction and cofactor mechanism. Direct KT2440 enzymology was not
found. The report nevertheless supplies an unsaved 66.6% pairwise alignment,
exact target-residue mapping, and target essentiality inferred from Francisella
and Salmonella. It also treats hemC-hemD adjacency as evidence for channeling and
uses a membrane-associated HemH generalization that does not match the curated
KT2440 HemH record. These claims were not used as target evidence.

## Curation decisions

GO:0004418 is accepted as the core molecular function. The broad tetrapyrrole
row is refined to GO:0006780 because HemC builds the immediate substrate that
HemD cyclizes to uroporphyrinogen III. Cytoplasm is retained from the machine
annotation and soluble enzyme architecture. No essentiality, channeling, or
target active-site-residue annotation was added.
