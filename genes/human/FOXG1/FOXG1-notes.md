# FOXG1 review notes

All 19 original annotation contexts were reconciled with the genuine fetched seed before transferring the reviewed judgments. The [source guide](FOXG1-source-guide.md) records original article access and assay limits; the [source evidence](FOXG1-source-evidence.yaml) preserves all original QuickGO objects, the genuine exported/stored mapping and the reviewed decisions. The authored candidate has passed ordinary validation, strict GOA matching and private rendering.

## Biological synthesis

FOXG1 is a nuclear forkhead transcription factor with a core role in regulating RNA polymerase II transcription. Human motif-selection, engineered reporter and endogenous promoter-association experiments provide complementary evidence. PLU-1/KDM5B and TLE1 interactions support transcription corepressor binding, with tagged/Y2H assays and endogenous co-complex recovery kept distinct. The three existing brain-development annotations remain non-core developmental context, supported beyond expression alone by human neurodevelopmental evidence.

The review actions are 8 ACCEPT, 3 KEEP_AS_NON_CORE, 5 TOO_GENERAL and 3 MODIFY. The two generic binding assertions are refined to transcription corepressor binding; the demonstrated Pol II repression context refines the broader negative-transcription assertion. One direction-neutral Pol II transcription-factor core is retained. No new annotation, quotation or alternative product is proposed.

## Source and construct boundaries

The current reviewed human record is [UniProt P55316](https://www.uniprot.org/uniprotkb/P55316/entry), a 489-amino-acid protein. Historical FOXG1A/B/C or HFK clone names do not establish three natural products. The HT-SELEX workbook uses a 135-amino-acid eDBD with two documented historical sequence conflicts, R281P and R291A, relative to current P55316 residues 163–297. No effect of those differences or exact wild-type fragment identity is inferred.

The EGFP–FOXG1 construct in PMID:21280142 is engineered and includes a reported codon 82 repair before R244C mutagenesis. Its sequence history is distinct from the HT-SELEX clone. Mutant SC35-associated foci do not establish a normal FOXG1 splicing function. Endogenous FOXG1/TLE1 co-immunoprecipitation and sequential ChIP in human BT048 cells support complex recovery and promoter co-occupancy, without a purified affinity or resolved binary-interface claim.

The three PTHR46617 IBAs are grounded in literal positive ancestral IBDs on the exact human sequence lineage. The target appearing among experimental descendants is valid grounding, not circular transfer. Source-specific limits in older TAS references remain explicit even where independent gene-level evidence supports a consistent term-granularity judgment.

## Questions and source follow-up

The biological questions concern how TLE and KDM5B recruitment select repressed targets in developing human neural cells, and how FOXG1 dosage and subnuclear distribution change regulation across neural cell states. Separate source follow-up concerns the precise historical TAS assay passages and mapping older constructs to the current sequence; these access questions are not new biological claims.

The genuine fetch produced 19 annotations and all 12 planned normal sources are present: three existing sources were preserved byte-for-byte and nine absent files were acquired. The original pending seed, GOA and UniProt snapshots are retained. No provider call was made because the existing credential failure remains unresolved; the selected manual primary readings supply the research record. The genuine history records this review session. Computed status is COMPLETE, with no annotation advisories from ordinary validation; strict GOA matching covers all 19 contexts. Private rendering and local-link inspection passed. Full repository integration remains pending.

History validation and final rendering/link checks passed. The default whitespace check reported only 18 original CRLF lines in the fetched PANTHER entries CSV; a command-only `cr-at-eol` check passed without changing source bytes or repository configuration. All 19 source contexts and all 12 normal source files remain intact.
