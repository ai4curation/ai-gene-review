# hemF assessment notes

## Identity and core reaction

Q88RQ6 (PP_0073) is the reviewed KT2440 oxygen-dependent
coproporphyrinogen-III oxidase. UniProt assigns EC 1.3.3.3 and RHEA:18257,
where molecular oxygen supports oxidative decarboxylation of the A- and B-ring
propionates of coproporphyrinogen III to form protoporphyrinogen IX, two carbon
dioxide molecules, and two waters
[file:PSEPK/hemF/hemF-uniprot.txt "Catalyzes the aerobic"]
[file:PSEPK/hemF/hemF-uniprot.txt "Reaction=coproporphyrinogen III + O2 + 2 H(+)"].
UniProt also predicts a divalent-metal cofactor, a homodimer, and cytoplasmic
localization through HAMAP-rule transfer rather than direct KT2440 assays.

## OpenScientist assessment

The OpenScientist report correctly identifies the target, reaction, and
oxygen-dependent distinction from radical-SAM HemN, and it explicitly notes
the lack of direct KT2440 kinetics or genetics. It presents unsaved target
sequence analysis and exact residue mapping, transfers detailed mechanism and
dimer architecture from the human ortholog, and concludes that Q88RQ6 is
cofactor-free despite the target record's predicted divalent-metal sites. The
report also assumes HemF is the principal aerobic route and HemN a low-oxygen
backup without KT2440 flux data, and its pathway sketch omits HemJ-family
PP_0431. These claims were not used as target evidence.

## Curation decisions

GO:0004109 is accepted as the predicted core molecular function, with
GO:0006785 as the endpoint-specific heme-b process and cytoplasm as the core
location. The two imported homodimer rows are retained as non-core structural
properties. The broad porphyrin-biosynthesis row is modified to GO:0006785.
Whether the predicted divalent metal is required and how flux is divided
between HemF and HemN remain experimental questions.
