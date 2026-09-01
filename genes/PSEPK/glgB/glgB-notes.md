# glgB curation notes

- Q88FN1 is a reviewed 1,4-alpha-glucan branching enzyme (EC 2.4.1.18) that transfers an alpha-1,4-glucan segment to create an alpha-1,6 branch. [file:PSEPK/glgB/glgB-uniprot.txt, "Reaction=Transfers a segment of a (1->4)-alpha-D-glucan chain to a"]
- The reviewed pathway field assigns glycogen biosynthesis. This supports participation in polymer branching, not the TreSB precursor or GlgE elongation reactions. [file:PSEPK/glgB/glgB-uniprot.txt, "PATHWAY: Glycan biosynthesis; glycogen biosynthesis."]
- GH13 family membership does not make the net GlgB reaction hydrolytic. The GO:0004553 InterPro mapping was removed in favor of GO:0003844. [file:PSEPK/glgB/glgB-uniprot.txt, "Belongs to the glycosyl hydrolase 13 family. GlgB"] [file:PSEPK/glgB/glgB-uniprot.txt, "DR   GO; GO:0003844; F:1,4-alpha-glucan branching enzyme activity"]
- Local PANTHER data place Q88FN1 in PTHR43651:SF3, specifically named 1,4-alpha-glucan branching enzyme. [file:interpro/panther/PTHR43651/PTHR43651-entries.csv, "Q88FN1"]
- PAINT places GO:0003844 at PTHR43651 ancestral node PTN000040010 using experimentally annotated branching enzymes, including the same-subfamily Mycobacterium exemplar P9WN45. [file:interpro/panther/PTHR43651/PTHR43651-paint.tsv, "PTN000040010"]
- Mycobacterium experiments identify GlgB as the fourth member of the TreS-Mak-GlgE-GlgB pathway but do not directly assay Q88FN1. [PMID:20305657 "We describe a new pathway from trehalose to alpha-glucan in Mycobacterium tuberculosis comprising four enzymatic steps mediated by TreS, Pep2, GlgE (which has been identified as a maltosyltransferase that uses maltose 1-phosphate) and GlgB."]
- In KT2440, glucose-starvation transcriptomics directly reports upregulation of glgB with glycogen-biosynthesis genes, supporting its physiological carbon-storage context without independently determining the enzyme reaction. [PMID:32267616 "In addition, upregulation was found for genes belonging to glycogen biosynthesis (glgA, glgB) and its degradation (glgX, glgP, malQ)."]
- GO:0043169 cation binding remains UNDECIDED: the InterPro mapping specifies neither ion nor site, and the reviewed UniProt record contains no cofactor or cation-binding feature.

## OpenScientist reconciliation

Source: `file:PSEPK/glgB/glgB-deep-research-openscientist.md` (1,461.43 seconds).

- The report corroborates the GH13 GlgB identity, alpha-1,6 branch-forming role,
  and placement downstream of TreSB and GlgE.
- Its proposed catalytic-residue positions, operon inference, and GlgC-absence
  interpretation are computational hypotheses rather than direct Q88FN1
  evidence and were not promoted into the curated core function.
- The report found no direct biochemical or genetic characterization of
  Q88FN1; the review therefore retains the target-specific UniProt and KT2440
  transcriptomic evidence as its primary grounding.
