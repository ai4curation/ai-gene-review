# algI manual research and annotation review

## 2026-10-25 evidence synthesis

Q51392 / PA3548 encodes AlgI. PMID:12003941 directly maps an integral inner-membrane protein with seven transmembrane domains and shows a specific acetylation defect after nonpolar deletion. The broad acyltransferase annotation is supported by MBOAT classification and genetics. It does not establish a purified target reaction. PMID:40171682 explicitly says “This full model has yet to be demonstrated experimentally”. The acyl-shuttle model is informed by DltB/DltX/DltD and other MBOAT systems; their direct intermediates are not direct AlgI experiments. No native donor, acylated AlgI residue or complete AlgI→AlgJ→AlgX chemical relay is asserted as proven. PAINT PTN000328645 is retained for broad acyltransferase activity; it is not a substrate-specific transfer.

Exact PANTHER mapping is PTHR13285:SF23, official label TEICHOIC ACID D-ALANYLTRANSFERASE, in PTHR13285 ACYLTRANSFERASE. The surprising official label is not an assertion that AlgI modifies teichoic acid. Pfam PF03062 MBOAT and InterPro IPR028362 AlgI provide complementary context.

## Source and workflow provenance

Normal supported fetch seeded the exact accession and original GOA-derived fields; all 5 original rows were assessed individually and preserved. All publications cited in original annotations were cached and inspected. The 12003941 and 23779107 force-refresh attempts still yielded abstract-only caches. 31900562 has legacy full_text_html metadata but only duplicated abstract/repository content, so it is treated as abstract access. Substantive full text was available for 25165982, 37797696, 40171682 and, where used, 15489449 and 36494359. PMID:40171682 is a review and its relay model is distinguished from native experimental chemistry.

The review and annotation-reviewer workflows were applied, followed by activity-centered core synthesis. The default Falcon attempt on algI ran concurrently with publication caching and failed authentication; the Perplexity-lite fallback failed quota/credit availability (/tmp/bacillus-algI-deep.log). The established outage was not retried for the other three genes, and no provider-authored report was fabricated. FEBA fetch was attempted for all four bacteria; no local data were available and bulk retrieval failed (/tmp/bacillus-algI-fitness.log). No fitness inference is made.

GO:0051979 alginic acid acetylation is not a descendant of GO:0042121 alginic acid biosynthesis. Where the biosynthesis row is modified, the reason explicitly makes a lateral synthesis-to-modification correction. AlgX retains a separate production/export contribution. Quoted UniProt sections are backfilled with the supported helper. Publication text and source flat files are not manually altered. Matching codex history and targeted validation are completed after edits.

Annotation totals: 5 including 0 NEW; {'ACCEPT': 4, 'MODIFY': 1}.

Validation outcome: `just validate PSEAE algI` passed with no curation warnings, and the matching codex history passed schema validation. Original seeded annotation fields were compared to the saved seed and remain unchanged.

## Independent final QA, 2026-10-25

Corrected the PMID:37797696 construct attribution: the negative surrogate acetylesterase assay and binary ITC use P. putida proteins, whereas the isolated AlgF oligosaccharide-binding assay uses P. aeruginosa AlgF. The Results explicitly state “AlgFPa did not display any affinity for the oligomers tested.” This supersedes any earlier grouping of both negative assays as Pp. Native Pa co-IP and the Pa NMR structure remain target-specific.

## Deep research availability, 2026-11-02

No provider deep-research report exists for this gene. During the alginate O-acetylation module audit, `just deep-research-falcon PSEAE algI` was retried and failed with "403 Failed to authenticate"; earlier Falcon and Perplexity attempts for the KT2440 homologs also failed (see genes/PSEPK/algI/algI-notes.md). No deep-research file was written by hand. The review instead rests on cached primary publications, the UniProt record and the existing annotation reviews.
