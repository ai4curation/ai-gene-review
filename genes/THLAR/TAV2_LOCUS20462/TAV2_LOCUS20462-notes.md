# TAV2_LOCUS20462: IMDH1-like isopropylmalate dehydrogenase

## Identity and inference

UniProtKB A0AAU9SYX6, field pennycress (Thlaspi arvense), has native ORF name TAV2_LOCUS20462; the Arabidopsis-like alias is an inferred functional descriptor, not a newly asserted official symbol. TAV2_LOCUS20462 encodes a predicted IMDH1-like, NAD-dependent hydroxyacid dehydrogenase in field pennycress. Homology to Arabidopsis IMDH1 supports oxidative decarboxylation of methylthioalkylmalate intermediates in glucosinolate chain elongation, together with activity on 3-isopropylmalate in leucine metabolism. The inferred enzyme uses a divalent metal cofactor. Its native substrate spectrum and relative pathway contributions have not been measured.

The existing [phmmer analysis](../../../projects/THLAR_OILSEED/ortholog_mapping/RESULTS.md) was inspected alongside the newly fetched target UniProt record. This is independent sequence evidence, not a GOA annotation used as support. A reciprocal best hit is not by itself a phylogenetic proof of strict one-to-one orthology. No accession matched gocams/index.tsv.

## Primary source assessment

- [PMID:21697089](https://pubmed.ncbi.nlm.nih.gov/21697089/): Arabidopsis IPMDH1 specializes toward methylthioalkylmalate but retains 3-isopropylmalate activity; mutagenesis demonstrates a substrate-specificity determinant. No target residue numbering or kinetic value is transferred.
- [PMID:19674406](https://pubmed.ncbi.nlm.nih.gov/19674406/): Arabidopsis IMDH1 biochemistry, localization and mutant metabolite analyses support dual glucosinolate and leucine contributions; these support the homolog inference, not native pennycress flux.

## Annotation decisions

- GO:0000287 magnesium ion binding: ACCEPT. IPMDH-family membership and the curated RuleBase-supported target cofactor statement support magnesium binding as a comparative assignment. This does not establish native metal occupancy or preference relative to manganese.
- GO:0003862 3-isopropylmalate dehydrogenase activity: ACCEPT. The target has IPMDH1-like sequence placement and RuleBase-supported chemistry. Arabidopsis IPMDH1 retains 3-isopropylmalate turnover in addition to its specialized methylthioalkylmalate activity. This term describes only the leucine-pathway substrate, not the distinct methylthioalkylmalate reaction.
- GO:0009098 L-leucine biosynthetic process: KEEP_AS_NON_CORE. Unlike MAM, IPMDH1 retains an established leucine-pathway reaction and Arabidopsis IPMDH1 has a secondary leucine-metabolic role. The target RuleBase assignment and close IMDH1 match support retaining this process as peripheral to the predicted specialized chain-elongation role; native flux allocation remains untested.
- GO:0016616 oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor: MODIFY. The NAD-dependent hydroxyacid oxidation is sound, but this target is an IMDH1-like enzyme. Refine to the exact 3-isopropylmalate activity and the separately proposed specialized methylthioalkylmalate reaction; GO:0003862 must not be treated as covering every alkylmalate substrate.
- GO:0051287 NAD binding: ACCEPT. The target RuleBase-supported catalytic reaction uses NAD, in agreement with the close IMDH1 match and experimentally characterized Arabidopsis enzyme. This is binding as part of catalysis rather than an unsupported generic interaction.

QuickGO is_a/part_of ancestry and exact reaction definitions were checked live on 2026-10-26. GO:0034722 is a descendant of both GO:0016787 and GO:0140096, despite its small-peptide substrates. GO:0010326 is the unelongated methionine reaction; GO:0003862 is the 3-isopropylmalate reaction. Exact elongated-substrate activities are not silently equated to those terms. No NEW biological-process annotation was added; existing process refinements are identified as descendants or lateral corrections in their reasons.

## Research provenance

Applied review, annotation-reviewer and core-function synthesis guidance. Normal fetch-gene seeded original rows; these fields are preserved. Default Falcon deep research and publication caching were launched concurrently. Falcon failed authentication (403) and automatic Perplexity-lite fallback failed with insufficient_quota (401); log /tmp/thlar-TAV2_LOCUS20462-deep.log. No provider report was fabricated. Manual source assessment and existing reproducible sequence analysis were used. Fitness retrieval is not applicable to this plant target. Target-specific publication searches did not establish a native assay for this exact accession; this is a literature-access conclusion, not proof that none exists.
