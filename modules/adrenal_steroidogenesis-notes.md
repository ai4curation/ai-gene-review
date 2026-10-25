# Adrenal steroidogenesis audit

## 2026-10-25: literature and scope assessment

The starting module is a human seven-protein template. Its chemistry is useful, but gene names and endpoint choices must not define a universal vertebrate pathway. The audit will distinguish the shared cholesterol-to-pregnenolone entry from species- and tissue-dependent corticosterone, cortisol, aldosterone and androgen branches, including interrenal tissue in fish. An enzyme active in gonads is not thereby demonstrated in the adrenal/interrenal pathway. Human disease examples are context, not evidence of evolutionary scope.

Five comparative/mechanistic references have been fetched and curated in the module. PMID21051590, PMID26038201, PMID27524977 and PMID35263051 have cached full text; PMID25445914 is abstract-only. They support the basic precursor relationships, mitochondrial versus microsomal redox systems, tissue zonation and divergent CYP11 architectures. Primary evidence is being checked by the individual gene reviewers before the structural module revision.

Key issues requiring explicit treatment:

- Normal adult mouse and rat adrenals predominantly make corticosterone without CYP17A1-dependent cortisol synthesis. This is not a claim of absence in every rodent tissue or life stage: fetal mouse Cyp17 activity has primary evidence (PMID7588219).
- Zebrafish Cyp17a2 supplies hydroxylase activity without Cyp17a1-like lyase activity. GO:0004508 describes hydroxylation, not both reactions. Separate annotons are needed; do not use NAD(P)-dependent C20 alcohol dehydrogenase as a proxy for oxidative C17-C20 cleavage.
- Human CYP11B1/B2 paralog names do not map one-to-one to all vertebrate terminal activities. Cattle and pigs have a combined enzyme, and independently evolved duplications produced other architectures. PTHR24279:SF1 contains human/mouse CYP11B2 and zebrafish Cyp11c1, so this subfamily alone cannot establish aldosterone synthesis.
- The terminal aldosterone route needs distinct 11beta hydroxylation, C18 hydroxylation and terminal C18 oxidation. A GO corticosterone 18-monooxygenase label must not stand for the whole sequence. Human CYP11B1 lacks the terminal oxidation, which does not by itself settle every broad biological-process participation claim.
- Cholesterol transfer and its acute regulation are distinct from the CYP11A1 reaction. Zebrafish cyp11a1.1 versus cyp11a1.2 expression and functional evidence must be separated; early morpholino phenotypes cannot overrule later knockout results.
- P450s require electron-transfer partners. The current boundary can describe them as required reaction context without pretending the seven proteins form a self-sufficient reconstituted system. A 2025 direct experiment (PMID40340376) is being checked against older claims that cytochrome b5 stimulates CYP17A1 only allosterically.

Source criticism matters even for good reviews. Figure 2B of PMID27524977 labels a terminal cortisol enzyme as microsomal CYP11B2, inconsistent with its correct main text about mitochondrial CYP11B1. Its CYP11B3 chemical wording is also imprecise. PMID35263051 contains a sentence conflating absence of terminal C18 oxidation with inability to form an earlier C18-hydroxylated product. Neither passage is used to define reaction chemistry. The TSPO machinery discussion is not evidence that TSPO is obligatory. Primary enzyme studies and the correct reaction definitions govern the module.

Human STAR, CYP11A1, HSD3B2, CYP17A1, CYP21A2, CYP11B1 and CYP11B2 are under systematic review. Nonhuman candidates include mouse Cyp11b2 and zebrafish Cyp11c1, Cyp17a1/Cyp17a2 and Cyp11a1 paralogs. Comparative proteins lacking the appropriate adrenal/interrenal context may remain notes-only comparators. Final representative counts and taxon constraints will follow the evidence, not a quota.


### Reaction restructuring and source disagreements

The working revision has 14 substrate-specific reaction nodes and 17 activity annotons, including separate HSD3B dehydrogenation/isomerization, CYP17 hydroxylase/lyase and terminal CYP11 oxidation. Eleven native adrenal/interrenal representatives are selected; the two additional fish paralogs remain reviewed comparators. Twenty-two references now provide comparative and primary support.

PANTHER release classifications and current UniProt disagree for HSD3B2 (PTHR10366:SF784 versus PTHR43245:SF51) and CYP21A2 (PTHR24281:SF83 versus PTHR24289:SF17). Both memberships are recognized by validation. The selected UniProt mapping is explicit and qualified; the older placement is not declared erroneous and no evolutionary placement is inferred. Functional restrictions and primary chemistry remain mandatory. Free-text lyase and terminal 18-oxidase activities have no asserted GO IDs, so automatic conformance checks cannot compare those activities; they are reviewed against the gene NTR cores manually.

### Completed curation checkpoint

The final curation pass has 26 module references and 434 reviewed original annotation rows across 13 genes: 11 native pathway representatives (396 rows) and two fish comparators (38 rows). Actions are 250 ACCEPT, 111 MODIFY, 52 KEEP_AS_NON_CORE, seven bare-binding REMOVE and 14 UNDECIDED; no NEW rows were added. Three annotation reviewers independently checked their steps and the reconstructed topology. Human STAR and CYP11A1 entry activities are linked to production GO-CAM models; gene-level evidence supplies localization independently where the model omits it.

All 13 targeted gene validations pass. Human CYP11B2 retains one documented positive-versus-negated cortisol annotation advisory. Module schema and scoped checks pass with 18 advisories, comprising repeated instances of the two family-source disagreements and automatic conformance limitations for specific lyase/18-oxidase activities without GO IDs. These are evidence limitations, not invitations to insert a broader or incorrect activity. The fish Cyp11c1 inner-membrane context is explicitly family-level; its individual review does not claim a target-specific localization experiment. Full repository validation is running before PR readiness.
