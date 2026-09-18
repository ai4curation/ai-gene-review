# rbsD curation notes

Q88K33 is assigned the RHEA:25432 interconversion of beta-D-ribopyranose and
beta-D-ribofuranose and the specific PANTHER D-ribose-pyranase subfamily
[file:PSEPK/rbsD/rbsD-uniprot.txt, "DR   PANTHER; PTHR37831:SF1; D-RIBOSE
PYRANASE; 1."]. The experimentally characterized *E. coli* ortholog catalyzes
the same conversion [PMID:15060078, "We show that RbsD catalyzes the pyran to
furan conversion of ribose"].

The electronic `intramolecular lyase activity` row is removed: current
GO:0062193 descends through `intramolecular transferase activity`, not
GO:0016872. Broad isomerase and transferase parents remain non-core, and
substrate binding is marked over-annotated because it does not represent a
separate evolved function from catalysis. Cytosol is used once in the
synthesized core rather than duplicating cytoplasm and cytosol.

OpenScientist states, "No direct biochemistry on the *P. putida* protein
itself." [file:PSEPK/rbsD/rbsD-deep-research-openscientist.md]. It also
supports treating RbsD as an accelerator of the reversible
pyranose/furanose bottleneck rather than the only possible source of the
furanose form; spontaneous interconversion remains possible.
