# TAV2_LOCUS24348: GGP1-like gamma-glutamyl peptidase

## Identity and inference

UniProtKB A0AAU9T3M3, field pennycress (Thlaspi arvense), has native ORF name TAV2_LOCUS24348; the Arabidopsis-like alias is an inferred functional descriptor, not a newly asserted official symbol. TAV2_LOCUS24348 encodes a predicted cytosolic GGP1-like gamma-glutamyl peptidase in field pennycress. The enzyme is inferred to hydrolyze gamma-glutamyl bonds in glutathione conjugates during glucosinolate biosynthesis, releasing glutamate and cysteinylglycine conjugates. The homologous Arabidopsis enzyme also hydrolyzes glutathione itself. Its glutamine-amidotransferase-like fold and conserved catalytic residues support cysteine-peptidase chemistry rather than establishing a physiological glutamine-amidotransferase role.

The existing [phmmer analysis](../../../projects/THLAR_OILSEED/ortholog_mapping/RESULTS.md) was inspected alongside the newly fetched target UniProt record. This is independent sequence evidence, not a GOA annotation used as support. A reciprocal best hit is not by itself a phylogenetic proof of strict one-to-one orthology. No accession matched gocams/index.tsv.

## Primary source assessment

- [PMID:21712415](https://pubmed.ncbi.nlm.nih.gov/21712415/): Purified Arabidopsis GGP enzymes process multiple glucosinolate-related glutathione conjugates, supported by mutant accumulation and localization. The target inference uses specific GGP1 mapping.
- [PMID:41176694](https://pubmed.ncbi.nlm.nih.gov/41176694/): Arabidopsis GGP1 structures and mutagenesis establish cysteine-peptidase chemistry for glutathione and its conjugates. A GATase-like fold does not alone establish a glutamine-metabolic function.

## Annotation decisions

- GO:0005829 cytosol: ACCEPT. The 88.8%-identity, full-coverage GGP1 reciprocal match and specific GGP1 subfamily assignment support transfer from directly localized Arabidopsis GGP1. The target ARBA localization text is not treated as independent evidence.
- GO:0006541 L-glutamine metabolic process: MARK_AS_OVER_ANNOTATED. The UniRule transfer reflects an amidotransferase-related family, but the target maps specifically to GGP1. Characterized GGP1 hydrolyzes gamma-glutamyl bonds in glutathione and its conjugates; this is distinct from glutamine hydrolysis or amidotransfer. Family architecture alone does not establish the annotated physiological glutamine role.
- GO:0016787 hydrolase activity: MODIFY. Specific GGP1 sequence placement, conserved cysteine-peptidase catalytic architecture and Arabidopsis GGP assays support GO:0034722. Live QuickGO confirms that this is a descendant of both broad parent terms, including catalytic activity acting on a protein; the tripeptide substrate does not justify rejecting that formal ontology ancestor.
- GO:0019760 glucosinolate metabolic process: MODIFY. The enzyme is inferred to perform gamma-glutamyl cleavage of glutathione conjugates during glucosinolate assembly. The biosynthetic descendant GO:0019761 is more precise than the existing metabolic parent. The annotation is supported by target mapping plus primary homolog biochemistry, not ARBA alone.
- GO:0140096 catalytic activity, acting on a protein: MODIFY. Specific GGP1 sequence placement, conserved cysteine-peptidase catalytic architecture and Arabidopsis GGP assays support GO:0034722. Live QuickGO confirms that this is a descendant of both broad parent terms, including catalytic activity acting on a protein; the tripeptide substrate does not justify rejecting that formal ontology ancestor.

QuickGO is_a/part_of ancestry and exact reaction definitions were checked live on 2026-10-26. GO:0034722 is a descendant of both GO:0016787 and GO:0140096, despite its small-peptide substrates. GO:0010326 is the unelongated methionine reaction; GO:0003862 is the 3-isopropylmalate reaction. Exact elongated-substrate activities are not silently equated to those terms. No NEW biological-process annotation was added; existing process refinements are identified as descendants or lateral corrections in their reasons.

## Research provenance

Applied review, annotation-reviewer and core-function synthesis guidance. Normal fetch-gene seeded original rows; these fields are preserved. Default Falcon deep research and publication caching were launched concurrently. Falcon failed authentication (403) and automatic Perplexity-lite fallback failed with insufficient_quota (401); log /tmp/thlar-TAV2_LOCUS24348-deep.log. No provider report was fabricated. Manual source assessment and existing reproducible sequence analysis were used. Fitness retrieval is not applicable to this plant target. Target-specific publication searches did not establish a native assay for this exact accession; this is a literature-access conclusion, not proof that none exists.
