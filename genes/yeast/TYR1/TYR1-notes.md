# TYR1 (YBR166C, P20049) notes

Pathway context: YeastPathways PWY3O-4120 (tyrosine biosynthesis), prephenate dehydrogenase. Batch context listed "prephenate dehydrogenase (NADP), EC 1.3.1.13" (from UniProt name) - NOT supported by biochemistry.

- Cofactor: [PMID:30771296 "We found that both enzymes favor the prephenate substrate and NAD+ cofactor in vitro."]; relaxed tyrosine feedback [PMID:30771296 "ScTyrA exhibited relaxed sensitivity to tyrosine inhibition"].
- NAD-binding motif: [PMID:2697638 "The canonical NAD-binding domain is located within the first 45 amino acids of the protein."]
- Regulated by phenylalanine, not GCN4 (PMID:2697638 abstract).
- UniProt names it "Prephenate dehydrogenase [NADP(+)]" EC 1.3.1.13 [UniProt:P20049] - appears legacy; GO NADP+ rows (IEA EC mapping and YeastPathways RCA) MODIFY -> GO:0008977 NAD+. NADP binding (InterPro2GO IPR006115) MARK_AS_OVER_ANNOTATED.
- Abstract-only: we cannot see the full kinetic table (NADP+ may give residual activity); "favor" implies preference, not exclusivity.
