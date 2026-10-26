# TAV2_LOCUS24872: IIL1-like IPMI large subunit

## Identity and inference

UniProtKB A0AAU9T4X1, field pennycress (Thlaspi arvense), has native ORF name TAV2_LOCUS24872; the Arabidopsis-like alias is an inferred functional descriptor, not a newly asserted official symbol. TAV2_LOCUS24872 encodes an IIL1-like large subunit of a predicted heterodimeric isopropylmalate isomerase in field pennycress. The aconitase-like catalytic architecture and close Arabidopsis IIL1 match support contribution to malate-derivative isomerization in leucine biosynthesis and methionine-derived glucosinolate chain elongation. Catalysis depends on association with a small LeuD-like subunit; native subunit pairing and plastid targeting remain untested.

The existing [phmmer analysis](../../../projects/THLAR_OILSEED/ortholog_mapping/RESULTS.md) was inspected alongside the newly fetched target UniProt record. This is independent sequence evidence, not a GOA annotation used as support. A reciprocal best hit is not by itself a phylogenetic proof of strict one-to-one orthology. No accession matched gocams/index.tsv.

## Primary source assessment

- [PMID:19597944](https://pubmed.ncbi.nlm.nih.gov/19597944/): Arabidopsis IPMI comprises a shared large subunit and specialized small subunits; mutant profiling supports both leucine and methionine-chain-elongation reactions. Target activity remains inferred.
- [PMID:20663849](https://pubmed.ncbi.nlm.nih.gov/20663849/): The accessible abstract reports physical large/small-subunit association and chloroplast-stromal functional complexes in Arabidopsis. AtLeuD1/2 correspond to SSU2/3; AtLeuD3 is the leucine-specific SSU1.

## Annotation decisions

- GO:0003861 3-isopropylmalate dehydratase activity: ACCEPT. The 95.3% identity IIL1 match and catalytic IPMI-domain architecture support the conserved enzyme subunit. Arabidopsis IIL1 forms functional heterodimers with LeuD small subunits. This annotation is interpreted as contribution within the enzyme complex, not autonomous catalysis by an isolated large subunit; original machine fields are preserved.
- GO:0120528 2-(omega-methylthio)alkylmalate dehydratase activity: NEW. The exact methionine-chain-elongation hydro-lyase activity is distinct from the pre-existing 3-isopropylmalate reaction, not its ancestor or descendant. Specific sequence mapping, complementary large/small-subunit architecture and primary Arabidopsis heterodimer evidence support a comparative annotation. The contribution qualifier explicitly avoids claiming an autonomous subunit enzyme. Native pennycress complex activity is untested.

QuickGO is_a/part_of ancestry and exact reaction definitions were checked live on 2026-10-26. GO:0034722 is a descendant of both GO:0016787 and GO:0140096, despite its small-peptide substrates. GO:0010326 is the unelongated methionine reaction; GO:0003862 is the 3-isopropylmalate reaction. Exact elongated-substrate activities are not silently equated to those terms. No NEW biological-process annotation was added; existing process refinements are identified as descendants or lateral corrections in their reasons.

## Research provenance

Applied review, annotation-reviewer and core-function synthesis guidance. Normal fetch-gene seeded original rows; these fields are preserved. Default Falcon deep research and publication caching were launched concurrently. Falcon failed authentication (403) and automatic Perplexity-lite fallback failed with insufficient_quota (401); log /tmp/thlar-TAV2_LOCUS24872-deep.log. No provider report was fabricated. Manual source assessment and existing reproducible sequence analysis were used. Fitness retrieval is not applicable to this plant target. Target-specific publication searches did not establish a native assay for this exact accession; this is a literature-access conclusion, not proof that none exists.
