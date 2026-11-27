# CARS2 manual review notes

Seeded CARS2 from the current GOA file and reviewed 15 annotation rows. The GOA
file is populated, not header-only.

Key evidence:

- UniProt curates CARS2 as a mitochondrial cysteine-specific aminoacyl-tRNA
  synthetase and lists the canonical Rhea cysteine + tRNA(Cys) + ATP reaction.
- PMID:29079736 identifies CARS2 as "a mitochondrial isoform of CARS" and
  demonstrates that human CARS2 catalyzes PLP-dependent production of CysSSH and
  CysSSSH from cysteine. The abstract reports that targeted disruption of
  mitochondrial CARS genes in mice and human cells implicates the enzymes in
  endogenous CysSSH production.
- Reactome:R-HSA-379726 records the mitochondrial tRNA aminoacylation pathway.
  It states that mitochondrial tRNA synthetases act in the mitochondrial matrix
  to charge mtDNA-encoded tRNAs with their cognate amino acids.
- PMID:34800366 defined MitoCoP, a human mitochondrial high-confidence proteome,
  using complementary subtractive proteomics, spatial proteomics, importomics,
  and curated database/literature evidence; the CARS2 GOA row is the derived HTP
  mitochondrion assertion.

Annotation decisions:

- Kept all cysteine-tRNA ligase, ATP binding, and mitochondrion rows.
- Marked `GO:0005737` cytoplasm too general. The family-root PAINT row is sound
  because mitochondria are part of the cytoplasm in GO, but the CARS2-specific
  node and direct annotations correctly use mitochondrion.
- Marked generic nucleotide binding and aminoacyl-tRNA ligase activity too
  general beside ATP binding and cysteine-tRNA ligase activity.
- Refined the generic and obsolete process rows to `GO:0070127` tRNA
  aminoacylation for mitochondrial protein translation.
- Recorded CARS2 cysteine persulfide synthesis as a core function through a
  proposed new molecular-function term, because the UniProt record already has
  Rhea reactions for persulfide production but GO has no matching term.

PANTHER:

- CARS2 is the animal mitochondrial subclade under `PANTHER:PTN002248443`, a
  30-leaf node carrying the mitochondrion IBD.
- The family-root cysteine-tRNA ligase and obsolete cysteinyl-tRNA
  aminoacylation IBDs reach both CARS1 and CARS2.
