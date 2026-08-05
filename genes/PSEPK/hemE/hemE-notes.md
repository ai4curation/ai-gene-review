# hemE assessment notes

## Identity and core reaction

Q88CV6 (PP_5074) is the reviewed KT2440 uroporphyrinogen decarboxylase.
UniProt predicts cofactor-independent removal of the four acetate carboxyl
groups of uroporphyrinogen III to form coproporphyrinogen III and assigns the
protein to the cytoplasm
[file:PSEPK/hemE/hemE-uniprot.txt "Catalyzes the decarboxylation of four acetate groups of"]
[file:PSEPK/hemE/hemE-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm"].
These target assignments are HAMAP-rule based rather than direct KT2440
experiments.

## OpenScientist assessment

The OpenScientist report correctly identifies the target and core reaction and
explicitly notes the absence of direct KT2440 characterization. It presents an
unsaved alignment to human UROD, exact residue mapping, and ortholog-derived
claims about kinetics, substrate breadth, mechanism, dimer behavior, and
essentiality. Its pathway diagram also names HemG/HemY instead of the
HemJ-family PP_0431 protein present in KT2440. These extrapolations were not
used as target evidence.

## Curation decisions

GO:0004853 is accepted as the core molecular function. The broad
porphyrin-biosynthesis row is modified to the endpoint-specific live term
GO:0006785, while the existing broad heme-biosynthesis row remains correct.
The more specific cytosol row is accepted and retained in the core function.
The biologically compatible cytoplasm parent is marked over-annotated because
retaining both location terms would be redundant. No target-specific
essentiality or kinetic claim is added.
