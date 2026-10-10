# Acot1 review notes

## Evidence summary
- [PMID:7906114] The rat Acot1 entry cites experimental evidence for acyl-CoA thioesterase/palmitoyl-CoA thioesterase activity.
- [PMID:23226270] This PMID supports a regulatory role of Acot1 in fatty-acid oxidation under the conditions tested.
- [UniProtKB:O88267] UniProt summarizes Acot1 as hydrolyzing acyl-CoAs to free fatty acids and CoA, with stronger activity toward long-chain fatty acyl-CoAs.

## Curation decisions
- Core function: long-chain acyl-CoA thioesterase (acyl-CoA hydrolase activity, GO:0047617).
- Specific catalytic activities were accepted; broad parent terms were modified to the specific activity where possible.
- Localization, cofactor/binding, and phenotype-level annotations were retained only as non-core unless directly tied to the enzymatic role.

## Re-review 2026-10-10

GOA changes: two new ISO rows from human ACOT1 (UniProtKB:Q86TX2) for GO:0001676 long-chain fatty acid metabolic process and GO:0047617 fatty acyl-CoA hydrolase activity, donor-splits of existing mouse-Acot1 (MGI:1349396) ISO rows. No retired rows. 22 rows total.

- PENDING resolved: both human-donor ISO rows ACCEPT (core activity/process conserved between orthologs; human ACOT1 donor IDA is PMID:16940157 per QuickGO).
- GO:0052815 medium-chain fatty acyl-CoA hydrolase activity (IEA, RHEA): MODIFY -> KEEP_AS_NON_CORE. GO defines medium-chain as 6-12 carbons, and UniProt records dodecanoyl-CoA hydrolysis for the rat enzyme with experimental evidence from PMID:7906114 ("Reaction=dodecanoyl-CoA + H2O = dodecanoate + CoA + H(+);"); the purified enzyme was active on C12-C16 [PMID:7906114 "Both enzymes were active toward fatty acyl-CoAs with chain-lengths of C12-16"]. "No activity at C8 or shorter" does not exclude C10-C12, so the term is a real secondary activity, not an error.
- GO:0000038 very long-chain fatty acid metabolic process (IBA, ISO): kept MARK_AS_OVER_ANNOTATED, with a sharper rationale. GO defines VLCFA as more than 22 carbons (long-chain is 13-22); the longest curated substrate for rat Acot1 and for human ACOT1 in UniProt is eicosanoyl-CoA (C20). The human donor IDA (PMID:16940157) is abstract-only in cache, so whether it contains C22+ data is unverified.
- GO:0010667 negative regulation of cardiac muscle cell apoptotic process (IMP): kept KEEP_AS_NON_CORE, now supported by the rat H9c2 data [PMID:23226270 "Annexin V/PI staining assay showed that overexpression of ACOT1 protected H9c2 cells from apoptosis (Figure 2C), while ACOT1 knockdown increased apoptosis (Figure 2D)."].
- Replaced circular `DR GO;` supporting quotes (which cite the annotation itself) on the ACCEPT rows with paper quotes (PMID:7906114, PMID:9490035) or UniProt CC lines; replaced one stale quote (GO:0006631 row) with the PATHWAY line.
- Added propagation_review blocks to the ISO rows (mouse and human Acot1 donors, SUPPORTS_TRANSFER).
- Description rewritten without curation commentary; core function now also lists cytosol as location. Status set to COMPLETE.

Open question: does Hunt et al. 2006 (PMID:16940157) report ACOT1 activity on C22+ acyl-CoAs? If so, the VLCFA rows should be ACCEPT/KEEP_AS_NON_CORE.
