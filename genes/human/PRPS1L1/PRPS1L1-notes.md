# PRPS1L1 notes

## Functional summary

PRPS1L1, historically PRPS3, is a testis-enriched catalytic PRPS paralog. Taira
et al. cloned the human testis-specific PRPS3 transcript, showed that the same
autosomal gene encodes a testis-specific mRNA, and found a predicted protein
highly homologous to human PRPS1 and PRPS2 [PMID:2168892, "the human
testis-specific mRNA was encoded by an autosomal gene, termed PRPS3"].

Unlike PRPS2, PRPS1L1 does not have a direct human enzymology paper in the
cached GOA evidence. The catalytic review therefore rests on three mutually
consistent sources: the PRPS-family PTHR10210 IBA at `PTN000025022`, the manual
ISS transfer from human PRPS1, and the reviewed UniProt EC/RHEA/pathway record
that assigns the ATP + ribose 5-phosphate to PRPP + AMP reaction by similarity.

## Annotation decisions

- Accept `GO:0004749 ribose phosphate diphosphokinase activity`,
  `GO:0006015 5-phosphoribose 1-diphosphate biosynthetic process`,
  `GO:0002189 ribose phosphate diphosphokinase complex`, and cytoplasm. These
  are conserved PRPS-family claims and are within the PTHR10210 catalytic
  subfamily scope.
- Keep Mg2+ binding, ATP binding and protein homodimerization as non-core
  supporting molecular features.
- Keep purine nucleotide biosynthesis and ribonucleoside monophosphate
  biosynthesis as non-core downstream context because PRPS1L1 makes PRPP rather
  than a pathway-specific purine intermediate.
- Mark `GO:0006163 purine nucleotide metabolic process`,
  `GO:0009165 nucleotide biosynthetic process`, and
  `GO:0090407 organophosphate biosynthetic process` as too general.
- Mark `GO:0008584 male gonad development` as over-annotated. PRPS1L1 is
  testis-specific, but the cDNA paper establishes expression and a likely
  nucleotide-synthesis enzyme, not execution of a developmental step.

## PTHR10210 implications

The current family review already includes `PANTHER:PTHR10210:SF112` in the
catalytic scopes for ribose phosphate diphosphokinase activity, PRPP
biosynthesis and the PRPP synthetase complex. PRPS1L1 has no PAINT loss on its
lineage, so this gene review simply confirms that SF112 behaves like a catalytic
PRPS subfamily, while the male-gonad Ensembl IEA is a species/tissue-context
overreach outside the family-wide PRPP-synthesis function.
