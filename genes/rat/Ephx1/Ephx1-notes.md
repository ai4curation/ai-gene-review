# Ephx1 review notes

## Evidence summary
- [UniProtKB:P07687] UniProt describes Ephx1 as hydrolyzing arene and aliphatic epoxides to less reactive, more soluble dihydrodiols.
- [PMID:9854022] The UniProt and GOA entries cite this publication for epoxide hydrolase activity and cis-stilbene-oxide hydrolase evidence.

## Curation decisions
- Core function: microsomal epoxide hydrolase 1 (epoxide hydrolase activity, GO:0004301).
- Specific catalytic activities and direct metabolic processes were accepted.
- Broad parent, localization, binding, and stimulus-response annotations were modified, kept non-core, or marked over-annotated according to support.

## Re-review 2026-10-10

**GOA changes.** One new row seeded (PENDING): GO:0047372 monoacylglycerol lipase activity
(IEA, GO_REF:0000116; RHEA:26132). No rows retired.

**Action.** GO:0047372 resolved to ACCEPT. RHEA:26132 is the reaction 2-arachidonoylglycerol
+ H2O -> glycerol + arachidonate, which the current UniProt record documents
[UniProtKB:P07687 "Metabolizes the abundant endocannabinoid 2-arachidonoylglycerol (2-AG)
to free arachidonic acid (AA) and glycerol (By similarity)"] with a matching CATALYTIC
ACTIVITY line. Accepted as a genuine secondary MF, not added to core_functions (core
remains epoxide hydrolase activity). No existing action changed.

**Re-audit.** The three IBA rows (epoxide hydrolase activity, arachidonate metabolic
process, epoxide metabolic process; GO_REF:0000033) are correctly handled: the
propagation_review notes rat Ephx1 (RGD:2557) is itself among the IBD seeds and does not
treat the target's own appearance as circular. The two MARK_AS_OVER_ANNOTATED rows (liver
development, cellular response to glucocorticoid stimulus; both IEP) are expression-pattern
annotations that overshoot participation, and were left. No GO:0005515 protein-binding rows.

**UniProt refresh.** This flat file still retains DR GO; cross-reference lines, so all
"GO; ..." UniProt quotes remain valid (0 stale). Description was rewritten to remove the
curation commentary ("The review accepts...") and expanded with standalone biology
(2-AG hydrolysis, 20(S)-OHC binding, lipid-epoxide substrates). status COMPLETE.


**Review follow-up 2026-10-17 (PR #4616 review).** Addressed the reviewer's findings. All sixteen UniProt `DR GO;` cross-reference `supporting_text` lines (which restate the annotation under review) were replaced with the relevant UniProt CC evidence: FUNCTION (epoxide hydrolysis), CATALYTIC ACTIVITY (cis-stilbene oxide reaction), SUBCELLULAR LOCATION (ER membrane), the "Binds 20(S)-hydroxycholesterol" line for oxysterol binding, and the "metabolism of endogenous lipids such as epoxide-containing fatty acids" FUNCTION line for the arachidonate-metabolic-process rows. GO:0047372 monoacylglycerol lipase activity changed ACCEPT -> KEEP_AS_NON_CORE, matching its own reason (secondary to the defining epoxide hydrolase activity) and the notes that it was not added to core_functions. Validates clean; 0 stale UniProt quotes.
