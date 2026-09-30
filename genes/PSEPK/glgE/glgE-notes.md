# glgE curation notes

- Q88FM9 is a predicted GlgE maltosyltransferase (EC 2.4.99.16; RHEA:42692) that transfers maltosyl units from alpha-maltose 1-phosphate to alpha-1,4-glucan. [file:PSEPK/glgE/glgE-uniprot.txt, "Reaction=alpha-maltose 1-phosphate + [(1->4)-alpha-D-glucosyl](n) ="]
- The record explicitly places GlgE in a branched alpha-glucan route with TreS, Mak, and GlgB. This supports GlgE polymer elongation, not assignment of the precursor-generating or branching reactions to GlgE. [file:PSEPK/glgE/glgE-uniprot.txt, "involved in a branched alpha-glucan biosynthetic pathway"]
- GH13 family membership describes the catalytic fold but does not make the net GlgE reaction hydrolytic. The GO:0004553 InterPro mapping was removed; GO:0016758 and GO:0030979 were retained. [file:PSEPK/glgE/glgE-uniprot.txt, "Belongs to the glycosyl hydrolase 13 family. GlgE"] [file:PSEPK/glgE/glgE-uniprot.txt, "DR   GO; GO:0016758; F:hexosyltransferase activity"]
- Q88FM9 and the characterized Mycobacterium GlgE P9WQ17 are both verified members of PTHR47786:SF2; PAINT places GO:0016758 at bacterial node PTN002233589 using P9WQ17 as the experimental seed. [file:interpro/panther/panther-members.tsv, "Q88FM9\tPTHR47786:SF2"] [file:interpro/panther/PTHR47786/PTHR47786-paint.tsv, "PTN002233589"]
- Streptomyces GlgE structural enzymology establishes the maltose 1-phosphate-dependent maltosyltransferase reaction and retaining mechanism at family level, not as a direct assay of Q88FM9. [PMID:24689960 "It catalyzes the α-retaining transfer of maltosyl units from α-maltose 1-phosphate to maltooligosaccharides and is predicted to use a double-displacement mechanism."]
- No target-specific biochemical publication was present in the local publication cache.

## OpenScientist reconciliation

Source: `file:PSEPK/glgE/glgE-deep-research-openscientist.md` (5,283.11 seconds).

- The report independently supports maltose 1-phosphate as donor,
  alpha-1,4-glucan as acceptor, and placement between TreSB and GlgB.
- Its catalytic-residue, gene-cluster, and GlgC-absence analyses are
  computational corroboration. They do not establish target-specific enzyme
  kinetics or prove that this route carries all alpha-glucan flux in KT2440.
- The curated review therefore retains the exact reaction and pathway role
  while recording the absence of direct Q88FM9 biochemical characterization.
