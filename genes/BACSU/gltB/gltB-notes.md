# Bacillus subtilis 168 GltB review

## Biological synthesis

GltB O34399 (BSU18440) is the small NADPH-input chain, not the glutamine-hydrolyzing large chain called GltB in many Gram-negative bacteria. Full native-species PMID:34931064 resolves two[4Fe–4S] clusters in GltB and electron flow from GltB-bound NADPH toward the GltA synthase center. The FAD/NAD(P)-binding domain and helical ferredoxin architecture of the exact168 protein independently support that mechanism. GltA contains FMN and[3Fe–4S]; the subunit cofactors must not be interchanged.

The native2022 structural study uses NCIB3610, not168. Its GltAB heterodimer and GudB-associated counter-enzyme assembly are distinct. GudB inhibition is mediated through GltA contacts; neither the binding location nor the active-GudB physiology should be reassigned indiscriminately to GltB or strain168. The generic four-heterodimer UniProt similarity statement is not propagated. No isolated-small-subunit full GOGAT turnover is asserted.

## Annotation and family decisions

All5 original rows remain. NADPH-GOGAT is ACCEPT as a component contribution. Generic oxidoreductase refines to both direct NAD(P)H oxidation and coupled GOGAT, while GO:0016639 refines to GOGAT. Generic iron-sulfur binding refines to4Fe–4S binding using the native structure and exact-target ferredoxin architecture. The glutamate-biosynthetic process is a direct electron-transfer contribution, not inference solely from a knockout. No NEW ancestral assimilation-cycle annotation is added.

PTHR43100:SF1 is officially GLUTAMATE SYNTHASE [NADPH] SMALL CHAIN, and differs from the PSEPK small-chain family placement. NCBIfam TIGR01317 GOGAT_sm_gam, two FAD/NAD(P)-binding domains and the helical ferredoxin classification are independent support. Physiological PMID:18326565 separates assimilatory GOGAT from native catabolic glutamate dehydrogenases; high-ammonium reverse chemistry does not imply effective native assimilation.

## Source access and preservation

Audit date: 2026-10-27. Exact-target identities are the immutable strain168 UniProt records; no GOA or UniProt file was changed. Every seeded annotation row is retained with its term, evidence, original reference, qualifier and supporting entities unchanged. No NEW annotation is introduced, so no comparator-based gap assertion is made. Term definitions and ancestry were checked through QuickGO; snapshots and focused logs are under `.cache/module-audit-logs/ammonia-bacsu-review/`. Canonical PMID fetches and the normal reference fetcher produced the cited caches; none was hand-written. Provider, publication and fitness acquisition attempts were already recorded under `.cache/module-audit-logs/ammonia-acquisition/`; failed providers are not evidence.

The native primary regulatory full texts PMID:18195355, PMID:24158439, PMID:25691471 and PMID:35778410 were read. The native GltAB primary full text PMID:34931064 was read, including its strain, biochemical, structural and cofactor details. PMID:11719184, PMID:12139611, PMID:17001076, PMID:18331450, PMID:21435182, PMID:23535029 and PMID:8093698 were available as abstracts. Publisher recovery for12139611,17001076,18331450,21435182,23535029 returned403. The PMC196239 URL recovery provides the accessible scanned-article page/abstract, not a new asserted full transcription. No inaccessible experimental annotation is rejected because its abstract foregrounds a partner.

PMID:22625175 is an abstract-only regulatory review, useful for synthesis but not a substitute for primary evidence. Primary PMID:18326565 (PMC2395005) and PMID:9829940 (PMC107716) are cached as abstracts. Normal PMC XML-page recovery returned browser challenges; EuropePMC fullTextXML recovery returned500 for both. The accessible PMC107716 web text was checked for methods and strain context, but no hand-built cache was manufactured. The abstract18326565 explicitly distinguishes native anabolic failure of RocG/GudB1 from heterologous E. coli GDH rescue; this supports a physiological conclusion under the studied conditions, not chemical irreversibility. In vitro reductive amination at high ammonium in the older study does not demonstrate effective native assimilation.

## Focused validation interpretation

The explicit core glutaminase subactivity (GltA) and NADPH-GOGAT complex membership (both chains) can trigger advisory requests for additional annotation rows. They are supported core context, but the review does not manufacture NEW assertions just to silence warnings. All machine rows remain intact. The GltA generic-GOGAT IBA has structured metadata after inspection of the actual PTN000234342 PAINT IBD row; native NADPH evidence supplies its target refinement.
