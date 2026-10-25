# algJ manual research and annotation review

## 2026-10-25 evidence synthesis

Q51393 / PA3547 encodes AlgJ. PMID:12003941 supports an uncleaved N-terminal anchor in the inner membrane, exposing the catalytic region to the periplasm. Both plasma-membrane and periplasmic annotations are therefore appropriate.

Species distinction in PMID:25165982 is essential: the crystal structure is Pseudomonas putida AlgJ75–370, while P. aeruginosa AlgJ79–379 was independently purified and assayed. Pa and Pp constructs hydrolyze 3-carboxyumbelliferyl acetate; Pa catalytic substitutions concern D193/H195/S297 rather than Pp D190/H192/S288. The directly measured MF added is acetylesterase activity (GO:0008126). Its core description explicitly identifies the surrogate-substrate assay: this does not establish native alginate deacetylation or reconstitution of the proposed AlgJ-to-AlgX transfer. Weak/undetectable polymer binding distinguishes AlgJ from terminal acetyltransferase AlgX.

No PANTHER DR cross-reference is present in the exact UniProt record; do not invent one. Pfam PF16822 ALGX supports the SGNH-like domain context; it does not make AlgJ and AlgX physiologically interchangeable.

## Source and workflow provenance

Normal supported fetch seeded the exact accession and original GOA-derived fields; all 6 original rows were assessed individually and preserved. All publications cited in original annotations were cached and inspected. The 12003941 and 23779107 force-refresh attempts still yielded abstract-only caches. 31900562 has legacy full_text_html metadata but only duplicated abstract/repository content, so it is treated as abstract access. Substantive full text was available for 25165982, 37797696, 40171682 and, where used, 15489449 and 36494359. PMID:40171682 is a review and its relay model is distinguished from native experimental chemistry.

The review and annotation-reviewer workflows were applied, followed by activity-centered core synthesis. The default Falcon attempt on algI ran concurrently with publication caching and failed authentication; the Perplexity-lite fallback failed quota/credit availability (/tmp/bacillus-algI-deep.log). The established outage was not retried for the other three genes, and no provider-authored report was fabricated. FEBA fetch was attempted for all four bacteria; no local data were available and bulk retrieval failed (/tmp/bacillus-algJ-fitness.log). No fitness inference is made.

GO:0051979 alginic acid acetylation is not a descendant of GO:0042121 alginic acid biosynthesis. Where the biosynthesis row is modified, the reason explicitly makes a lateral synthesis-to-modification correction. AlgX retains a separate production/export contribution. Quoted UniProt sections are backfilled with the supported helper. Publication text and source flat files are not manually altered. Matching codex history and targeted validation are completed after edits.

Annotation totals: 7 including 1 NEW; {'ACCEPT': 4, 'MODIFY': 2, 'NEW': 1}.

Validation outcome: `just validate PSEAE algJ` passed with no curation warnings, and the matching codex history passed schema validation. Original seeded annotation fields were compared to the saved seed and remain unchanged.

## Independent final QA, 2026-10-25

Corrected the PMID:37797696 construct attribution: the negative surrogate acetylesterase assay and binary ITC use P. putida proteins, whereas the isolated AlgF oligosaccharide-binding assay uses P. aeruginosa AlgF. The Results explicitly state “AlgFPa did not display any affinity for the oligomers tested.” This supersedes any earlier grouping of both negative assays as Pp. Native Pa co-IP and the Pa NMR structure remain target-specific.
