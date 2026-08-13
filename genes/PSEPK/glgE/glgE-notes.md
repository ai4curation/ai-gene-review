# glgE curation notes

- Q88FM9 is a predicted GlgE maltosyltransferase (EC 2.4.99.16; RHEA:42692) that transfers maltosyl units from alpha-maltose 1-phosphate to alpha-1,4-glucan. [file:PSEPK/glgE/glgE-uniprot.txt, "Reaction=alpha-maltose 1-phosphate + [(1->4)-alpha-D-glucosyl](n) ="]
- The record explicitly places GlgE in a branched alpha-glucan route with TreS, Mak, and GlgB. This supports GlgE polymer elongation, not assignment of the precursor-generating or branching reactions to GlgE. [file:PSEPK/glgE/glgE-uniprot.txt, "involved in a branched alpha-glucan biosynthetic pathway"]
- GH13 family membership describes the catalytic fold but does not make the net GlgE reaction hydrolytic. The GO:0004553 InterPro mapping was removed; GO:0016758 and GO:0030979 were retained. [file:PSEPK/glgE/glgE-uniprot.txt, "Belongs to the glycosyl hydrolase 13 family. GlgE"] [file:PSEPK/glgE/glgE-uniprot.txt, "DR   GO; GO:0016758; F:hexosyltransferase activity"]
- PTHR47786 has the correct family name, but Q88FM9 is absent from the local member snapshot and the metadata description is unchecked LLM text. It was not used as target-level evidence. [file:interpro/panther/PTHR47786/PTHR47786-metadata.yaml, "Alpha-1,4-glucan:maltose-1-phosphate maltosyltransferase"]
- No target-specific biochemical publication was present in the local publication cache.

## OpenScientist reconciliation

Source: `file:PSEPK/glgE/glgE-deep-research-openscientist.md`.

- The report independently supports maltose 1-phosphate as donor,
  alpha-1,4-glucan as acceptor, and placement between TreSB and GlgB.
- Its catalytic-residue, gene-cluster, and GlgC-absence analyses are
  computational corroboration. They do not establish target-specific enzyme
  kinetics or prove that this route carries all alpha-glucan flux in KT2440.
- The curated review therefore retains the exact reaction and pathway role
  while recording the absence of direct Q88FM9 biochemical characterization.
