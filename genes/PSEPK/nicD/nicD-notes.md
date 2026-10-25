# KT2440 nicD evidence notes

## Identity and reaction

Reviewed Q88FY3, PP_3943, is the NicD N-formylmaleamate deformylase. Actual UniProt DR:PANTHER PTHR43798:SF33 is HYDROLASE, PUTATIVE (AFU_ORTHOLOGUE AFUA_2G14860)-RELATED; the parent family is MONOACYLGLYCEROL LIPASE. These official names were checked against the PANTHER ontology, but neither supplies exact substrate specificity. Pfam PF00561 and InterPro IPR000073/IPR029058 support the alpha/beta-hydrolase fold. Selection as a pathway enzyme requires the demonstrated deformylase chemistry.

PMID:18678916 shows recombinant NicD crude extracts convert N-formylmaleamate to maleamate and formate, verified by HPLC and proton NMR. This is not a purified-NicD kinetic measurement. The cached abstract explicitly says “Further conversion of N-formylmaleamic acid to formic and maleamic acid is catalyzed by the NicD protein”. The full paper reports individual S101A, D125A and H245A substitutions abolishing activity, while E221A retains approximately 70%. Current UniProt lists E221 as a predicted catalytic residue and phrases several mutation entries as combined substitutions; the primary Results support D125 and describe the substitutions individually. This discrepancy is documented rather than silently copied.

The primary Methods sentence calling the products formate and maleate conflicts with its Results/HPLC-NMR interpretation and pathway diagram: the immediate product is maleamate; NicF subsequently removes the remaining amide nitrogen. The Results and chemically distinct steps govern the review.

## Annotation decisions

The native nicotinate process is accepted: NicD performs a chemical step and the nicD mutant cannot grow on nicotinate, with cluster complementation. The broad linear-amide hydrolase row is MODIFY to the already proposed N-formylmaleamate deformylase activity; the core uses that proposed term. QuickGO searches for formylmaleamate recovered no exact term. The prior membrane REMOVE is changed to UNDECIDED: whole-cell extract activity and an absent membrane annotation do not rule out peripheral association. A cytosolic replacement is not asserted without localization evidence.

## Source access and research provenance

Review and annotation-reviewer workflow applied on 2026-10-25. Existing KT2440 Falcon reports were read as literature guides, not regenerated or treated as primary experiments. PMID:18678916 remains abstract-only locally after a supported force refresh; the full Results and Methods were independently read at https://pmc.ncbi.nlm.nih.gov/articles/PMC2516282/. The review quotes the cached abstract or curated experimental UniProt statements where appropriate and does not pretend that a body-specific quotation is present in the cache. PMID:22530095 was fetched with full text. No publication cache was manually edited.

For the new S16 comparator, default Falcon deep research with Perplexity-lite fallback ran concurrently with publication caching; Falcon authentication failed and Perplexity returned HTTP401 insufficient_quota (log `/tmp/bacillus-nicotinate-s16-deep.log`). No provider-branded research file was fabricated. FEBA retrieval was attempted for all four targets: no local database or remote source was reachable, and no fitness artifact was written. PSEP6 also lacks a configured organism mapping. This is missing data, not a negative fitness phenotype. The GO-CAM index had no matches to Q88FY3, Q88FY4, Q88FY5 or F8G0M3.

## Shared downstream chemistry and taxonomic boundary

The lower order is N-formylmaleamate --NicD/Nfo--> maleamate plus formate --NicF/Ami--> maleate plus ammonium --MaiA/NicE/Iso--> fumarate. PMID:22530095 directly characterized the S16 versions after recombinant expression and purification. Its full text reports: “Attempts to degrade nicotinic acid by resting cells of strain S16 did not result in any degradation after 24 h of incubation”. S16 lacks the KT2440 nicAB entry genes in that study. Thus a shared lower enzyme cannot establish complete nicotinate degradation or justify transferring nicotinate-catabolism annotation to the nicotine-pathway comparator. The nicotine enzymes named NicA/NicA2 are not the KT2440 nicotinate hydroxylase small subunit merely because they share a name. No new nicotine-process annotation was added to the KT2440 genes.

## PR 5544 follow-up (2026-10-25)

Retained membrane UNDECIDED after reassessing the recorded primary-methods and results evidence. Whole-extract enzymology is not a subcellular-fractionation experiment, and no transmembrane helix is required for peripheral membrane association. The alpha/beta-hydrolase domain quotation was removed from this row because it is not localization evidence. The accepted NicB membrane claim has positive target topology/location support; it does not create a symmetric requirement to reject NicD. Current evidence supports neither a positive localization nor its negation.

Live QuickGO checks on 2026-10-25 found no exact terms using EC 1.17.2.1, EC 3.5.1.106, EC 3.5.1.107 or the corresponding substrate-specific activity names. Nicotinate dehydrogenase GO:0050138 remains the NADP-specific reaction. All 14 direct children of GO:0016725 were inspected: acceptor classes include NAD/NADP, oxygen, disulfide, quinone and iron-sulfur protein, but no generic cytochrome-acceptor child. GO:0047111 is formate-specific and cannot substitute. Thus GO:0016725 remains the supported parent for cytochrome-linked NicAB; search non-retrieval is reported as a current search result, not proof that no future ontology term can exist.

GO:0033966 N-substituted formamide deformylase activity was also checked live: its actual definition specifies N-benzylformamide hydrolysis to benzylamine/formate (RHEA:12096), so the superficially general name is not an exact substitute for N-formylmaleamate deformylase.
