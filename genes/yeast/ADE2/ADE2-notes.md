# ADE2 (YOR128C, P21264) notes

- AIR carboxylase, step 6. Domain architecture: N-terminal PurK ATP-grasp (IPR005875) + C-terminal class I PurE (IPR033747) [UniProt:P21264].
- Fungal Ade2 (Cryptococcus ortholog) is a two-step enzyme: PurK domain uses AIR + ATP + HCO3- to make N5-CAIR, PurE domain converts N5-CAIR to CAIR [PMID:9500840 "the ADE2-PurK activity uses AIR, ATP, and HCO3- as substrates"].
- Therefore GO:0004638 / EC 4.1.1.21 (class II direct carboxylation, animal PAICS) is the wrong reaction description; MODIFY to GO:0034028 + GO:0034023. YeastCyc assigns EC 4.1.1.21 (mis-modelled reaction).
- ade2 red pigment from AIR [PMID:8939809 "leads to the accumulation of a cell-limited red pigment"].
- Nucleobase metabolic process terms (IMP/IBA/ARBA) -> MODIFY to de novo IMP biosynthesis.
- Note: direct S. cerevisiae biochemistry of the two sub-reactions not found in the cache; inference from the Cryptococcus enzyme and domain composition.
