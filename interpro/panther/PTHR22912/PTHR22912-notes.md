# PTHR22912 curation notes

## 2026-10-26 — AcoL SF219 scope correction

The original SUBFAMILY_ONLY lists omitted SF219 even though the committed family inventory already included its Bacillus subtilis AcoL member O34324. Current UniProt independently reports the same assignment, and panther.obo names SF219 DIHYDROLIPOYL DEHYDROGENASE. The sole SF219 representative in the committed reviewed-protein inventory is AcoL; this is not a claim that the inventory enumerates all extant descendants.

The full native locus study PMID:10368162 identifies AcoL's putative FAD-binding domain, Cys38/Cys43 redox-disulfide site, NAD(H)-binding region and interface domain. This supports a conventional E3 catalytic assignment and FAD binding, in agreement with the existing real PTN000530299 IBD. AcoL's membership and the primary architecture establish the omitted chemistry scope; no new PTN, clade loss, residue requirement or experimental seed was invented. PAINT assertions remain unchanged.

SF219 was added only to the existing GO:0004148 and GO:0050660 applicability lists and documented as a subfamily with its exact representative. The existing SthA distinction and all other accepted subfamilies remain intact. The primary does not report purified Bacillus AcoL catalysis; native acetoin-system association does not prove shared usage by OGDH, PDH or other complexes. The individual gene review preserves this distinction. Family metadata's unchecked LLM description was not used as evidence.

Propagation verification: a targeted live QuickGO query on 2026-10-26 independently confirmed that O34324 has GO_Central IBA rows for both GO:0004148 and GO:0050660 with PANTHER:PTN000530299 in with/from. This explicitly links this leaf to that inherited assertion; it was not inferred merely because AcoL belongs to PTHR22912. The cached PAINT IBD records identify the node and its experimental descendant seeds. Annotation data are used here only to trace the existing inference, not as functional supporting evidence; the primary sequence analysis supplies that evidence. No complete tree reconstruction or universal statement about unobserved SF219 descendants is claimed.
