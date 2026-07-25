# hemN assessment notes

## Identity and core reaction

Q88F35 (PP_4264) is a predicted oxygen-independent coproporphyrinogen-III
dehydrogenase of the HemN radical-SAM family. UniProt assigns the two-SAM
conversion of coproporphyrinogen III to protoporphyrinogen IX and one [4Fe-4S]
cluster
[file:PSEPK/hemN/hemN-uniprot.txt "Reaction=coproporphyrinogen III + 2 S-adenosyl-L-methionine ="]
[file:PSEPK/hemN/hemN-uniprot.txt "Binds 1 [4Fe-4S] cluster."]. These are
family- and rule-based assignments rather than direct KT2440 experiments.

## OpenScientist assessment

The OpenScientist report correctly identifies the target, radical-SAM
reaction, and [4Fe-4S] requirement and explicitly notes that Q88F35 has not
been experimentally characterized. It presents unarchived target residue
mapping, transfers E. coli structural and mechanistic details, and transfers
Anr/Dnr regulation and mutant phenotypes from other species. It also promotes
PP_3781 from an uncharacterized HemN-family protein to a redundant KT2440
oxidase even while acknowledging that it could be a HemW-type protein. The
pathway diagram substitutes HemG/HemY for the KT2440 HemJ-family PP_0431 step.
These extrapolations were not used as target evidence.

## Curation decisions

GO:0051989 is accepted as the most precise core molecular function and
GO:0006785 is used for the heme-B endpoint. Cytoplasmic localization and the
[4Fe-4S] cofactor remain grounded in UniProt family rules, with broad metal and
iron-sulfur binding kept non-core. KT2440-specific regulation, oxygen-regime
dominance, and any PP_3781 redundancy remain open questions.
