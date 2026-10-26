# TAV2_LOCUS13090: SSU2/3-like IPMI small subunit

## Identity and inference

UniProtKB A0AAU9S4C4, field pennycress (Thlaspi arvense), has native ORF name TAV2_LOCUS13090; the Arabidopsis-like alias is an inferred functional descriptor, not a newly asserted official symbol. TAV2_LOCUS13090 encodes a predicted LeuD-like small subunit of isopropylmalate isomerase in field pennycress. It is most closely associated with the Arabidopsis SSU2/SSU3 group involved in methionine chain elongation for glucosinolate biosynthesis, rather than a uniquely resolved SSU3 ortholog. It is inferred to contribute substrate-recognition and catalytic architecture to a heterodimer with an IIL1-like large subunit in plastids. Native complex assembly and localization have not been assayed.

The existing [phmmer analysis](../../../projects/THLAR_OILSEED/ortholog_mapping/RESULTS.md) was inspected alongside the newly fetched target UniProt record. This is independent sequence evidence, not a GOA annotation used as support. A reciprocal best hit is not by itself a phylogenetic proof of strict one-to-one orthology. No accession matched gocams/index.tsv.

## Primary source assessment

- [PMID:19597944](https://pubmed.ncbi.nlm.nih.gov/19597944/): Arabidopsis IPMI comprises a shared large subunit and specialized small subunits; mutant profiling supports both leucine and methionine-chain-elongation reactions. Target activity remains inferred.
- [PMID:20663849](https://pubmed.ncbi.nlm.nih.gov/20663849/): The accessible abstract reports physical large/small-subunit association and chloroplast-stromal functional complexes in Arabidopsis. AtLeuD1/2 correspond to SSU2/3; AtLeuD3 is the leucine-specific SSU1.

## Annotation decisions

- GO:0003861 3-isopropylmalate dehydratase activity: ACCEPT. The target maps to the SSU2/SSU3 group and has the LeuD substrate-recognition domain. Arabidopsis small subunits associate with IIL1 to form functional IPMI. The retained reaction is a complex-associated biochemical capacity, not evidence for a dedicated physiological leucine role or independent small-subunit catalysis.
- GO:0009570 chloroplast stroma: ACCEPT. The SSU2/SSU3-like sequence relationship and primary localization of the Arabidopsis heterodimeric IPMI proteins to chloroplast stroma support this existing annotation. The target ARBA statement is not used as independent support; native import and processing have not been tested.
- GO:0019761 glucosinolate biosynthetic process: ACCEPT. The reciprocal mapping reverses to SSU2 and therefore supports the SSU2/SSU3 group rather than strict SSU3 identity. Both Arabidopsis paralogs contribute to glucosinolate chain elongation with IIL1. This is a catalytic-complex participant, not merely a protein required by a phenotype.
- GO:0120528 2-(omega-methylthio)alkylmalate dehydratase activity: NEW. The exact methionine-chain-elongation hydro-lyase activity is distinct from the pre-existing 3-isopropylmalate reaction, not its ancestor or descendant. Specific sequence mapping, complementary large/small-subunit architecture and primary Arabidopsis heterodimer evidence support a comparative annotation. The contribution qualifier explicitly avoids claiming an autonomous subunit enzyme. Native pennycress complex activity is untested.

QuickGO is_a/part_of ancestry and exact reaction definitions were checked live on 2026-10-26. GO:0034722 is a descendant of both GO:0016787 and GO:0140096, despite its small-peptide substrates. GO:0010326 is the unelongated methionine reaction; GO:0003862 is the 3-isopropylmalate reaction. Exact elongated-substrate activities are not silently equated to those terms. No NEW biological-process annotation was added; existing process refinements are identified as descendants or lateral corrections in their reasons.

## Research provenance

Applied review, annotation-reviewer and core-function synthesis guidance. Normal fetch-gene seeded original rows; these fields are preserved. Default Falcon deep research and publication caching were launched concurrently. Falcon failed authentication (403) and automatic Perplexity-lite fallback failed with insufficient_quota (401); log /tmp/thlar-TAV2_LOCUS13090-deep.log. No provider report was fabricated. Manual source assessment and existing reproducible sequence analysis were used. Fitness retrieval is not applicable to this plant target. Target-specific publication searches did not establish a native assay for this exact accession; this is a literature-access conclusion, not proof that none exists.

## 2026-10-26 independent evidence-selection QA

Matched supporting quotations to the actual claim: specific SOT17 reciprocal mapping rather than the neighboring SOT18 search row, positive MAM condensation evidence for the functional claim, and direct homolog localization text where localization is inferred. Only relevant corrections apply to this gene. Annotation actions and all seeded fields are unchanged.
