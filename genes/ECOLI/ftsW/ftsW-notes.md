# Manual notes on ftsW

FtsW is the SEDS-family membrane polymerase paired with FtsI/PBP3 for septal peptidoglycan synthesis; it should be curated for glycan polymerization, division-site localization, divisome function, and peptidoglycan biosynthesis, not for D,D-transpeptidase activity.

## UniProt and literature synthesis

- UniProtKB:P0ABG4 lists FtsW as a probable peptidoglycan glycosyltransferase with EC 2.4.99.28 by HAMAP rule, places it in the E. coli inner membrane as a multipass protein, and describes its function with FtsI/PBP3 in cell division.
- Mercer and Weiss showed that FtsW is recruited to the septal site downstream of FtsZ, FtsA, FtsQ, and FtsL, and is needed to recruit FtsI/PBP3 [PMID:11807049].
- Wang and co-workers had already localized FtsW and FtsI to the septum [PMID:9603865], and Pastoret and colleagues mapped the FtsW topology as a 10-transmembrane protein with both termini in the cytoplasm [PMID:12423747].
- The SEDS polymerase papers provide the functional split now used for curation: FtsW and RodA are the glycan polymerases for the divisome and Rod system, respectively, while FtsI/PBP3 and MrdA/PBP2 are their cognate class-B PBP transpeptidases [PMID:27525505, PMID:27643381, PMID:37620344].

## Annotation review decisions

- The many FtsW protein-binding rows report real contacts with FtsI/PBP3, FtsN, FtsQ, MtgA, or PBP1b, but GO:0005515 is too generic to keep as a molecular function.
- The lipid-linked peptidoglycan transporter activity reported for FtsW is retained only as non-core because the 2011 in vitro flippase activity predates the SEDS glycosyltransferase model and the physiological identity of the lipid II flippase is controversial [PMID:21386816].
- The regulation of cell shape rows overstate FtsW biology. FtsW loss causes filamentation through failed septation; RodA/MrdB is the SEDS paralog that maintains rod shape during lateral-wall elongation.

## 2026-11-06 primary-evidence reassessment

This section supersedes the earlier shape and flippase verdicts above. All 44 original machine annotation payloads, including their original term IDs and references, are preserved. No NEW annotation was added. The existing UniProt/GOA bytes remain unchanged. A genuine `just deep-research ECOLI ftsW --provider falcon` attempt failed with HTTP 403 (authentication/access); no provider report was produced. Manual research used the primary sources below. `just paint-losses ECOLI ftsW` reported no IRD/IKR loss on the target lineage; no inference about the number of donor genes was used.

- **Native polymerase evidence.** PMID:33495624 uses E. coli BW25113-derived strains, including the MTSES-sensitive FtsW I302C allele, selective inhibition of other polymerases, alkyne-NAM incorporation into newly synthesized septal glycans and single-molecule tracking. FtsW inactivation reduces septal labeling; simultaneous loss of other polymerase activities removes the residual signal. This is target-specific in-vivo evidence, distinct from a purified wild-type P0ABG4 assay. The FtsW constructs and other mutations must not be silently equated with unmodified reference protein. The study concludes: “our results in live E.coli cells strongly support the notion that FtsW is an essential septal PGTase in vivo.”
- **Purified ortholog evidence.** PMID:30692671 expressed S. thermophilus, S. aureus and P. aeruginosa proteins in E. coli. The expression host does not make those E. coli FtsW assays. Cognate bPBPs stimulate polymerization, and catalytic-site substitutions in FtsW abolish it. This establishes conserved chemistry alongside the native target work; PMID:27525505 is contextual SEDS-family evidence, not a substitute for these distinctions.
- **Transport assay versus physiological role.** Full primary PMID:21386816 tests membrane vesicles and reconstituted His-tagged FtsW from pDML2400 expressed in C43(DE3), using NBD-lipid II accessibility and FRET. It reports that “purified FtsW induced the transbilayer movement of Lipid II in model membranes”. PMID:24711460 tests lipid-II analogues, TM deletions and substitutions; lipid-II transport can be impaired while phospholipid movement remains. This is positive assay evidence and is not erased by discovering polymerase activity. Mutant complementation failure alone cannot tell which FtsW function failed.
- **Independent native-flipping evidence.** Full primary PMID:25013077 chemically inactivates MurJ and measures colicin-M access to lipid II. FtsW depletion in a rodA deletion background leaves robust flipping, but the authors explicitly allow residual FtsW as a limitation. The transport MF/BP rows are therefore KEEP_AS_NON_CORE for assayed capacity, with native contribution unresolved. They do not define a required physiological FtsW flippase role or a MurJ-independent route.
- **Morphogenesis.** Current QuickGO defines GO:0008360 as modulation of cell surface configuration; it does not restrict the process to RodA-mediated lateral elongation. FtsW synthesizes the material shaping the septum and daughter poles. PMID:33495624 connects selective inhibition to wall synthesis and abnormal septa/poles, and PMID:9006034 describes division/shape phenotypes. Both original shape rows are accepted for this direct synthetic role, without assigning RodA's specific lateral-growth function.
- **Specificity and access.** Generic membrane is refined to plasma membrane, and cell division to its verified FtsZ-dependent descendant already present in the review. No redundant NEW terms are needed. Adjudicated physical contacts retain the bare-binding-policy REMOVE decision without calling the interaction false. The exact AP-MS edge behind PMID:29176613 remains UNDECIDED because the target-specific supplementary result was not established; the article-level network is insufficient to certify that edge.

QuickGO definitions and ancestor snapshots, provider failure log, PAINT output, baseline and exact preservation report are retained under the ignored audit cache. Unresolved native transport contribution would need discriminating experiments; ontology or literature-access tasks are not framed as biological knowledge gaps.

Identity limit: the 2011/2014 transport experiments identify E. coli His-FtsW plasmid pDML2400 and the C43(DE3) expression host; this audit did not align the original plasmid sequence against the frozen P0ABG4 sequence. The 2021 in-vivo study identifies BW25113-derived strains and explicit FtsW substitutions. These construct and strain contexts are preserved rather than presenting every experiment as an assay of purified, unmodified K-12 reference protein.


## PR6123 round-1 follow-up (2026-11-06)

- three flippase claims marked over-annotated with assay retained.

Historical annotation payloads, inherited NEW rows and raw/provider bytes were preserved against the published head 1678b44ceb3b7781cc4abcafbe54090c89f742bc. Claim-specific membrane support uses the frozen transmembrane prediction with its actual evidence code; a computational topology feature is not called an experimental localization. Full construct/strain mappings remain in the earlier notes and source analysis instead of being repeated on unrelated rows.

The direct enzyme-activator evidence in PMID:30692671 applies to the assayed StPBP2x and SaPBP1 constructs, including catalytic-serine mutants. GO:0008047 is current and requires direct interaction without covalent modification. No corresponding role is inferred for Bacillus PBP3 from catalytic compensation, and an essential physical PBP2B requirement alone does not identify direct activation chemistry. A divisome complex annotation describes septal pair membership, not a purified complete native assembly; PBP3 conditional backup is left outside that assertion.

All five D,D proposals now share one reaction definition and the QuickGO-verified GO:0016755 parent. The definition retains organism-dependent acceptors and does not turn an inferred PBP3 linkage into a product-resolved assay. QuickGO searches and responses are preserved in the ignored round-1 audit cache.
