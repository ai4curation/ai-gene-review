# PR6179 scientific adjudication — round 1

Published baseline: e2113833f0146fb160dbde5c8135b3c553c64cdf. Twenty Kdp reviews contain 274 ordered annotation payloads. The original source qualifiers, historical proposals and retired flags are preserved. The wider frozen source set is intentionally conservative; no existing source was fetched again.

## 1. Complex activity versus subunit relation

The official GO annotation guide (https://www.geneontology.org/docs/go-annotations/, consulted 2026-11-07) distinguishes execution by a gene product from contribution to an activity that cannot be ascribed to that subunit. Its exact short statement is: “Only the complex subunits required for the Molecular Function are annotated to the Molecular Function term with ‘contributes to’.” The manual annotation guide (https://pmc.ncbi.nlm.nih.gov/articles/PMC3706743/) likewise distinguishes catalytic subunits from noncatalytic contribution; lack of isolated activity alone is not a universal test for every multisubunit enzyme.

GO0008556 defines the ATP-coupled potassium movement reaction. KdpB supplies ATP hydrolysis; KdpA/B provide the coupled ion route. KdpC and KdpF contribute structural support, not the independently attributed coupled reaction. The source rows are preserved as received, but their `enables` attribution is marked over-annotated, with structured probable WRONG_QUALIFIER correction requests. This is not REMOVE, a NOT claim, or a denial of structural participation. Source-specific IBA/IEA propagation records distinguish role attribution from family identity. The existing source qualifiers are not silently rewritten.

PMID10608856 (cached abstract) reports purified KdpF restoration of detergent-solubilized KdpABC activity and near-normal membrane-associated activity without KdpF. Thus the required contribution is assay-context dependent; it is not universal in-vivo essentiality. PMID9789555 (cached abstract) reports proteoliposome transport and supports the stabilizing role. Lack of KdpC inhibitor labelling does not show that it has no contribution. PMID34272288 (cached full text) resolves the structural partnership stabilized by C/F; native contribution transfer to KT2440 remains inferred. NA1000 KdpABC genetics (PMID39133005 full text) corroborates locus participation, without an isolated KdpC transport assay. The contribution cores remain unchanged.

The GOA files were inspected only to recover the source-assigned database and WITH/FROM identifiers for correction routing; they are not evidence that a function is true. `source-row-provenance.json` records that routing. Confidence is PROBABLE because the source curator should confirm relation correction against the complete source record. The term and the experimental assembled-complex activity remain supported.

## 2. Family scope and named negatives

The PTHR45569 archive contains two GO0000155 member exceptions (P73870 and Q725T9), not a pair of GO0000160 exceptions. Both exact historical objects remain archived and are copied without alteration into `member-guards.yaml`. Independent architecture evidence supports absence of the canonical C-terminal histidine transmitter in these two proteins and Q1J2K3. This does not negate atypical serine kinase activity, nor automatically exclude participation of a split signaling component in a phosphorelay process.

The reviewer is correct that the checker accepts exceptions under either FAMILY_WIDE or SUBFAMILY_ONLY, and that MODIFY does not force a family/gene disagreement. The family notes are corrected. However, its only subfamily SF1 contains full-length and short architectures; granting SF1 wholesale with only three exceptions would presume an exhaustively partitioned boundary not established by the evidence. The current schema/checker has no field for an otherwise unresolved family with bounded member negatives. We retain UNRESOLVED plus the exact structured historical assertions and explicit named-member guards. This limitation is disclosed, not presented as an ordinary family checker success. No tree placement or loss node is invented.

PTHR48111's positive KdpE SF50 evidence likewise remains archived and used by the module's exact representatives/evidence gates. Lack of an audit of all other response-regulator subfamilies is not evidence that all lack potassium-homeostasis roles. The round-one note makes that boundary explicit rather than restoring an unsupported negative about other subfamilies.

## 3. Dgeo localization

The imidazole/NaCl cytosol statement belongs to recombinant purification in an E. coli host, not native D. geothermalis fractionation. The short KdpD_N/Usp architecture is compatible with a soluble kinase but does not establish its native partitioning or exclude membrane recruitment. GO0005737 is now UNDECIDED, without a cytosol replacement. The two membrane rows remain UNDECIDED. None supplies a core localization. Existing publication/cache text is unchanged.

## 4. KdpE activity and regulatory alternatives

Official QuickGO snapshots in `ontology.json` distinguish GO0000987 sequence-specific cis-regulatory binding from GO0001216 transcription activation. The former remains a valid separate gene annotation. The CAUVN direct ChIP/promoter-output evidence and the explicitly inferred KT2440 activator role support using GO0001216 for the integrated output core, matching ECOLI; both module output annotons are aligned. No annotation row or evidence code is changed to manufacture a new activator annotation.

The canonical and NA1000 profiles are evidence-qualified alternatives, not mutually exclusive biological mechanisms. `ONE_OR_MORE` replaces `EXACTLY_ONE` for those profiles. The F-containing/F-independent pump alternatives retain their contextual distinctions. Their explicit repeated role descriptors are not deduplicated by a schema change during this scientific response.

## 5. Bounded editorial and follow-up improvements

The repeated STAA8 KdpD sentence is removed once, preserving its LAC* versus NCTC8325 caveat. CAUVN KdpD gains a direct matched-protein phosphatase experiment with KdpE-alone autodephosphorylation controls. Historical audit receipts and duplicate provenance snapshots remain unchanged; the round-one capacity wrapper reuses the published checker instead of adding another copied implementation. No retrospective commit-splitting or broad formatting cleanup is attempted.
