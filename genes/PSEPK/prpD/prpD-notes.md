# prpD curation notes

## Identity and pathway role

Q88KF2/PP_2338 is a PrpD-family 2-methylcitrate dehydratase in the
2-methylcitrate pathway. UniProt records the reaction
`(2S,3S)-2-methylcitrate = 2-methyl-cis-aconitate + H2O` and places the protein
in propanoate degradation
[UniProtKB:Q88KF2, "Reaction=(2S,3S)-2-methylcitrate = 2-methyl-cis-aconitate + H2O;"].

The direct biochemical evidence is from the Salmonella ortholog. Purified PrpD
has 2-methylcitrate dehydratase activity but does not perform the subsequent
hydration step
[PMID:11294638, "This work shows that the prpD gene of the prpBCDE operon of this bacterium encodes a protein with 2-methylcitrate dehydratase enzyme activity."].

## Cofactor annotation

The automated GO:0051537 2 iron, 2 sulfur cluster binding annotation is
inconsistent with the characterized PrpD family. The purified Salmonella enzyme
was explicitly Fe-S-free and did not require metal or reductant
[PMID:11294638, "Homogeneous PrpD enzyme did not contain an iron-sulfur center, displayed no requirements for metal cations or reducing agents for activity"].
This is an electronic annotation and can be removed on biochemical and
family-mechanistic grounds.

## Pathway boundary

PrpD performs the direct conversion to 2-methyl-cis-aconitate. A separate
aconitase hydrates that intermediate to 2-methylisocitrate
[PMID:11294638, "Homogeneous AcnA protein of S. enterica had strong aconitase activity and catalyzed the hydration of the 2-methyl-cis-aconitate to yield 2-methylisocitrate."].
KT2440 also encodes the AcnD/PrpF-like alternative machinery in the same locus,
so PrpD should be curated as a valid catalytic enzyme without assuming it is
the only in vivo implementation.
