# BACSU proA: comparative module audit

2026-11-07 UTC. The reference sequence is strain 168; the 2011 pathway genetics used JH642 derivatives. Their pathway architecture is comparative support, not a purified-enzyme or localization assay on this exact strain-168 sequence.

ProA supplies the common reductive step for both the anabolic ProB route and the osmotically induced ProJ route.

Curated HAMAP statements are the target-specific computational support. Primary publications are distinguished from exact-strain assays. All source annotation payloads and order are preserved, with no NEW rows. Broad true terms refine to supported descendants; nucleotide binding is part of catalysis. RNA binding, where present, remains UNDECIDED pending target evidence.

The Falcon research attempt failed; no provider report is represented as successful. Manual literature research is recorded here and in the review references.

- PMID:25367752: Comparative review; cached abstract read and publisher full text accessible. Supports pathway conservation and alternative routes; older channeling interpretations must be checked against PMID:39514317.
- PMID:21784929: Full primary text read. JH642-derivative genetics separates ProB/ProJ branches and shared ProA; reference target is strain168. Feedback resistance of ProJ is argued physiologically rather than measured here.
- PMID:8083159: Cached abstract read; UniProt identifies strain168 and records sequence conflicts in the original sequence. Gene organization supports pathway context. Multicopy protease phenotypes do not establish a direct protease regulatory activity of ProB.

## Independent annotation-reviewer consultation (2026-11-07 UTC)

Catalytic and pathway decisions are retained. Nucleotide binding is integral to the curated reaction: ATP donates phosphate in ProB/ProJ, while NADPH supplies reducing equivalents to ProA. These are mechanistic/HAMAP inferences, not measurements of target affinity or stoichiometry. The reductase remains at the existing cytoplasm term; no new cytosol annotation is manufactured.

PMID:25367752 publisher full text was independently accessible at https://onlinelibrary.wiley.com/doi/10.1111/brv.12146; the local cache remains abstract-only, and no publication file was rewritten. Its stale full_text_unavailable flag was removed. The findings now state biology with source quotations rather than repeat the access notes.

Selected evidence anchors:
- [PMID:21784929] In JH642-derived B. subtilis, ProA is shared by anabolic and osmoadaptive proline synthesis: its disruption eliminates osmoadaptive synthesis and causes proline auxotrophy. Source: "Disruption of the proA gene also abolished osmoadaptive proline biosynthesis but caused, in contrast to the disruption of proHJ, proline auxotrophy."
- [PMID:8083159] The B. subtilis proB and proA genes are adjacent and encode successive reactions in the glutamate route. The multicopy protease phenotype does not itself establish direct regulation of proteases by either enzyme. Source: "The proB gene encoding gamma-glutamyl kinase was followed by the proA gene encoding glutamyl-gamma-semialdehyde dehydrogenase at an interval of 39 nucleotides, suggesting that the genes constitute an operon."

No NEW rows, subtype-specific physiological annotations, target RNA activity, stable ProA-ProB complex or demonstrated substrate channeling were added. The five original Falcon attempts failed and remain documented in the original logs.

PAINT check: `just paint-losses BACSU proA` reported no IRD or IKR loss on this target lineage. The retained IBA therefore does not contradict a cached PAINT loss.


## PR6160 evidence follow-up (2026-11-07 UTC)

Tightened row-specific rationale. For ProB/ProJ, cytosol remains a comparative inference from HAMAP, soluble architecture and E. coli native-locus monomeric-GFP localization, not from GOA. For ProA, the review retains the explicitly curated cytoplasm granularity without treating absence of a finer row as evidence. No actions or original payloads changed.
