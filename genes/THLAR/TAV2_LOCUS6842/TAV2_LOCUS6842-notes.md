# TAV2_LOCUS6842: MAM1/3-like methylthioalkylmalate synthase

## Identity and inference

UniProtKB A0AAU9RP64, field pennycress (Thlaspi arvense), has native ORF name TAV2_LOCUS6842; the Arabidopsis-like alias is an inferred functional descriptor, not a newly asserted official symbol. TAV2_LOCUS6842 encodes a predicted methylthioalkylmalate synthase in field pennycress. It is a MAM1/3-like homolog inferred to condense acetyl-CoA with methionine-derived 2-oxo acids during glucosinolate side-chain elongation, probably in plastids. Its native chain-length range is unresolved; similarity to Arabidopsis MAM1 does not establish restriction to one elongation cycle or exclude MAM3-like substrate promiscuity.

The existing [phmmer analysis](../../../projects/THLAR_OILSEED/ortholog_mapping/RESULTS.md) was inspected alongside the newly fetched target UniProt record. This is independent sequence evidence, not a GOA annotation used as support. A reciprocal best hit is not by itself a phylogenetic proof of strict one-to-one orthology. No accession matched gocams/index.tsv.

## Primary source assessment

- [PMID:14740211](https://pubmed.ncbi.nlm.nih.gov/14740211/): The accessible Arabidopsis MAM1 abstract reports the first two condensation cycles and lack of activity with primary-metabolic synthase substrates. The negative specificity is not transferred uniquely to a MAM1/3-like target.
- [PMID:17369439](https://pubmed.ncbi.nlm.nih.gov/17369439/): Arabidopsis MAM3 accepts all six condensation-cycle substrates and some non-methionine 2-oxo acids, including the isopropylmalate-synthase substrate. This bounds the uncertainty of a co-ortholog assignment.

## Annotation decisions

- GO:0003824 catalytic activity: MODIFY. The target is a strong MAM1/3-like sequence match with MAM subfamily membership. Both characterized Arabidopsis MAM proteins catalyze this condensation; GO:0010177 is a supported descendant of this general catalytic term. This inference does not determine the number of native chain-elongation cycles.
- GO:0003852 2-isopropylmalate synthase activity: UNDECIDED. The shared MAM1/MAM3 best hit does not uniquely resolve paralog-specific substrate promiscuity. Arabidopsis MAM1 lacks this activity whereas MAM3 converts 2-oxoisovalerate to isopropylmalate. Thus neither a positive nor negative target assignment is justified from the PANTHER family mapping alone.
- GO:0009098 L-leucine biosynthetic process: MARK_AS_OVER_ANNOTATED. MAMs were recruited from an isopropylmalate-synthase-like family into specialized glucosinolate metabolism. Even the MAM3 side reaction is not sufficient to establish its normal contribution to leucine production. The target mapping supports MAM function, not a demonstrated native leucine-pathway role.
- GO:0009507 chloroplast: ACCEPT. Both characterized Arabidopsis MAMs act in plastid-associated chain elongation, including direct localization of MAM3. The closely matching 506-residue target supports the comparative assignment; the ARBA location statement is not used as independent evidence and native targeting is untested.
- GO:0010177 methylthioalkylmalate synthase activity: ACCEPT. Independent reciprocal sequence analysis matches the same pennycress protein to MAM1 and MAM3, and target MAM subfamily membership agrees. Primary Arabidopsis assays establish the conserved reaction. Retain this inferred activity without transferring exact MAM1 chain-length restriction.
- GO:0019761 glucosinolate biosynthetic process: ACCEPT. The target is inferred to perform an enzymatic chain-elongation step, rather than merely respond to or regulate glucosinolate accumulation. MAM-specific sequence placement plus primary homolog enzymology support the existing process annotation independently of ARBA.
- GO:0046912 acyltransferase activity, acyl groups converted into alkyl on transfer: MODIFY. The target is a strong MAM1/3-like sequence match with MAM subfamily membership. Both characterized Arabidopsis MAM proteins catalyze this condensation; GO:0010177 is a supported descendant of this general catalytic term. This inference does not determine the number of native chain-elongation cycles.

QuickGO is_a/part_of ancestry and exact reaction definitions were checked live on 2026-10-26. GO:0034722 is a descendant of both GO:0016787 and GO:0140096, despite its small-peptide substrates. GO:0010326 is the unelongated methionine reaction; GO:0003862 is the 3-isopropylmalate reaction. Exact elongated-substrate activities are not silently equated to those terms. No NEW biological-process annotation was added; existing process refinements are identified as descendants or lateral corrections in their reasons.

## Research provenance

Applied review, annotation-reviewer and core-function synthesis guidance. Normal fetch-gene seeded original rows; these fields are preserved. Default Falcon deep research and publication caching were launched concurrently. Falcon failed authentication (403) and automatic Perplexity-lite fallback failed with insufficient_quota (401); log /tmp/thlar-TAV2_LOCUS6842-deep.log. No provider report was fabricated. Manual source assessment and existing reproducible sequence analysis were used. Fitness retrieval is not applicable to this plant target. Target-specific publication searches did not establish a native assay for this exact accession; this is a literature-access conclusion, not proof that none exists.

## 2026-10-26 independent evidence-selection QA

Matched supporting quotations to the actual claim: specific SOT17 reciprocal mapping rather than the neighboring SOT18 search row, positive MAM condensation evidence for the functional claim, and direct homolog localization text where localization is inferred. Only relevant corrections apply to this gene. Annotation actions and all seeded fields are unchanged.
