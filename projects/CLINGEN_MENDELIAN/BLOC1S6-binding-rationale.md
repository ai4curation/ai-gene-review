---
title: "BLOC1S6 binding annotation rationale"
species: [human]
autolink_gene_symbols: false
---

# BLOC1S6 binding annotation rationale

[ClinGen Mendelian project](../CLINGEN_MENDELIAN.md) · [BLOC1S6 research notes](../../genes/human/BLOC1S6/BLOC1S6-notes.md)

The BLOC1S6 review retains 58 existing `GO:0005515 protein binding` annotations as `KEEP_AS_NON_CORE` and refines 11 others to supported syntaxin or SNARE binding terms. This records a scoped exception for this gene review, not a new repository-wide retention rule. The [third review of PR #3770](https://github.com/ai4curation/ai-gene-review/pull/3770#issuecomment-5938278897) correctly identified that the earlier notes did not explain the departure from written guidance clearly enough.

The [annotation-reviewer guidance](https://github.com/ai4curation/ai-gene-review/blob/main/.claude/skills/annotation-reviewer/SKILL.md) recommends `MODIFY` when a more informative molecular function is supported, otherwise generally `REMOVE` for uninformative generic binding. That policy removes an annotation for its limited functional information; it does not assert that the interaction is false. The supplied [ActionEnum definitions](../../src/ai_gene_review/schema/gene_review.yaml) describe `KEEP_AS_NON_CORE` as retaining an existing annotation outside the core synthesis, and `REMOVE` as judging it unlikely to be correct. These are different reasons for exclusion. For BLOC1S6, this task uses the latter distinction: an adequately supported physical association can remain outside the core when neither an evidence-backed refinement nor a biological reason to reject it has been established. Breadth alone is not treated as over-annotation.

The scientific purpose is to preserve the existing partner- and source-specific observations without promoting a list of interactions into pallidin's function. Pallidin's core remains its contribution to BLOC-1 adaptor activity and endosomal cargo sorting, with the accepted syntaxin-binding activity. Retaining a broad interaction does not give pallidin its partner's catalytic activity, identify a physiological pathway for every screen hit, or establish an isolated binding interface.

## Evidence distinctions behind the decisions

| Evidence in the BLOC1S6 review | Decision and limit |
| --- | --- |
| Source-listed syntaxin and SNAP-family partners, including the native BLOC-1 pull-down experiments in [PMID:19546860](https://pubmed.ncbi.nlm.nih.gov/19546860/) | Eleven `MODIFY` decisions use syntaxin binding, syntaxin-1 binding or SNARE binding. Native-complex recovery with anti-pallidin detection does not map every direct pallidin contact. |
| Human BLOC-1 assembly and selected reconstitution experiments in [PMID:22203680](https://pubmed.ncbi.nlm.nih.gov/22203680/) | Pallidin–BLOS1 and pallidin–Cappuccino pair reconstitution supports more than a complex-membership label alone. The dysbindin association in that study is interpreted at the octamer level; the isolated-pair result is not extended to every co-subunit. |
| Curated IPI records from binary interaction screens | Retention preserves the reported association and partner identifier. The review read the studies' abstracts and corroborating UniProt interaction records; it did not independently inspect every supplementary pair. No new mechanistic interpretation is inferred from those uninspected measurements. |
| Affinity-purification mass spectrometry, including [PMID:33961781](https://pubmed.ncbi.nlm.nih.gov/33961781/) | Non-core retention records physical co-association. Co-purification does not by itself demonstrate direct binary contact. |

Fourteen of the retained rows name BLOC-1 co-subunits BLOC1S1, BLOC1S4, DTNBP1 or BLOC1S5. The seven accepted `GO:0031083 BLOC-1 complex` annotations capture membership; the interaction rows retain particular partners, references and assay contexts. Their coexistence is not evidence that the interaction is false or circular. It also does not make every interaction an independently established interface. The [gene review](../../genes/human/BLOC1S6/BLOC1S6-ai-review.yaml) records those evidence limits for each row.

## Where this exception stops

`KEEP_AS_NON_CORE` is not a substitute for `UNDECIDED`. When inaccessible or insufficiently adjudicated evidence leaves the relevant assertion unresolved, `UNDECIDED` remains the required action. An accessible abstract can support a limited assembly-level claim without resolving a specific contact or mechanism; the unresolved stronger claim must not be silently added. The retained curated screen records are not a claim that their complete primary datasets were independently verified. A specific contradiction or unresolved identity would require a fresh decision on that row, not automatic retention under this exception.

This rationale does not change the existing metabolic-process, ER-lumen, gene-expression or other annotation decisions. It does not make `GO:0042802 identical protein binding` interchangeable with homodimerization: self-association alone does not establish stoichiometry. Nor does it reverse the [ABCC6 review](../../genes/human/ABCC6/ABCC6-ai-review.yaml), which documents generic-binding removals under the general informational-exclusion policy alongside evidence-backed refinements. Different gene records must state the evidence and the exclusion criterion actually used; this BLOC1S6 exception should not be generalized by copying its action labels.
