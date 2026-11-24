# PR6169 item 4: PTHR45900 scope adjudication

## Recommended resolution

1. **GO:0000150 DNA strand exchange activity:** restore the canonical positive `FAMILY_WIDE` default with an explicit `member_exceptions` entry for UniProtKB:Q1D5A2/MXAN_3991. Ground this exception in the actual ImuA-only negative control in PMID:34190612 Figure 4E, alongside its accessory/inhibitory role. Describe the negative at the tested assay conditions and avoid claiming impossibility under every substrate or condition. Keep the existing PTN000534381 assessment `SOUND`; do not set `pruned_node_id` or `lost_in_clade_node_id` because Q1D5A2 has no established leaf in this cached tree.
2. **GO:0000725 recombinational repair:** retain `UNRESOLVED` for applicability across *all current external family assignments*, while explicitly retaining `SOUND` for the existing PAINT descendant set and positive evidence for canonical RecA. The negative strand-exchange control does not itself establish a negative native recombinational-repair phenotype. ImuA's observed anti-RecA/TLS role argues against simply granting the process from classification, but is insufficient for a categorical process member exception. Do not label this a downgrade of the canonical RecA evidence.
3. Keep the Q1D5A2 SF1 classification as a source assertion. A misleading automated RecName does not demonstrate an incorrect homology/HMM assignment. Do not report a classifier defect or invent a missing ImuA loss node.
4. Keep `MOSTLY_COHERENT`, measured ImuA DNA binding/ATP hydrolysis and the bounded sensor-activity assessment. No implication that ImuA is inactive for every RecA-related activity follows.

## Direct primary evidence, with limits

The publisher's complete Figure 4 was downloaded and visually inspected; the unmodified source image is archived beside this note. In panel E, lane 2 contains ImuA without RecA1 and does not show the joint-molecule product observed with the RecA1-only lane 3. Subsequent lanes test ImuA inhibition of RecA1. This distinguishes an assay-scoped negative for intrinsic strand exchange from inhibition alone. The text describes RecA1 joining homologous substrates and inhibition by ImuA; the lane assignments add the direct ImuA-only control.

Panel B's earlier DNA-binding negative must not be generalized: PMID:38591662 later measured positive DNA binding with a different assay/substrate. Its full cached text also reports positive ATPase activity and predominantly monomeric ImuA, with filament formation described as unlikely. These findings support functional divergence without proving universal inactivity. No direct negative native recombinational-repair assay was identified.

Source: [Sheng et al., Figure 4 and Results](https://journals.asm.org/doi/10.1128/aem.00919-21). Image: [original publisher image](https://journals.asm.org/cms/10.1128/AEM.00919-21/asset/c557929b-a606-44b3-bc29-62d5959ae6bf/assets/images/large/aem.00919-21-f004.jpg). The 2021 publication cache remains unchanged and abstract-only. The image is an archived primary artifact, not an altered figure or a quantitative reanalysis.

## Why the two scope statements need not contradict

`node_assessments` judges the existing PAINT IBD and the descendants of that node in the versioned tree. Q1D5A2 is absent from the cached PTHR45900 tree, so that assertion is not being applied to this protein by the inspected tree. `term_assessments.scope: FAMILY_WIDE` means safe for all members, including externally assigned members not represented in that tree. These are different quantifiers. `SOUND` for the inspected node therefore does not force a universal grant to Q1D5A2, and a universal-scope uncertainty does not negate the characterized RecA descendants.

Suggested GO:0000725 scope reason:

> Canonical RecA participation in recombinational repair is established, and the existing PTN000534381 IBD remains SOUND for the assessed cached-tree descendants. Applicability to every current external PTHR45900 assignment is unresolved: Q1D5A2/ImuA is absent from that tree and has an independently established accessory/anti-RecA role. Figure 4E supplies a negative intrinsic strand-exchange control under the tested conditions, but does not test every possible contribution to native recombinational repair. Retain the canonical positive inference; neither grant this process to ImuA from classification alone nor assert a demonstrated absence of all repair participation.

## Actual schema constraints

- `TermScopeEnum.FAMILY_WIDE` means safe for all members. The `member_exceptions` mechanism can carve out a named member; its meaning is **the term does not hold**, not merely that the member is unstudied.
- Exceptions are supported under `FAMILY_WIDE` or `SUBFAMILY_ONLY`. The cross-check rejects them under `UNRESOLVED`. Thus a negative exception cannot be used as an uncertainty bucket for GO:0000725.
- `pruned_node_id` and `lost_in_clade_node_id` are optional. If a pruned node is supplied, a corresponding negative node assessment is required. No such node is known for Q1D5A2, so omit both.
- The family schema has no `source_defects` slot. Its `Reference` class contains only `id` and `title`, with no `reference_review`. In the gene schema, source defects are supported in annotation `Review`, `ReferenceReview`, `FunctionalIsoform` and `GoCamActivityReview`. A separately justified naming correction could be recorded in a gene reference review, but is neither necessary nor sufficient to solve this family-scope question.

No family, gene, module, historical record, PAINT source or released round1 artifact was edited by this consultation. Root owns implementation and validation of the final family judgment.
