# algX manual research and annotation review

## 2026-10-25 evidence synthesis

Q51372 / PA3551 encodes AlgX. PMID:25165982 directly demonstrates Pa AlgX binding to polymannuronate and terminal O-acetyl transfer onto the polymer using surrogate donor 4-nitrophenyl acetate, with ESI-MS products and enzyme-free controls. NEW MF GO:0016413 O-acetyltransferase activity is therefore supported without specifying the native donor. Direct polymer recognition supports NEW GO:0030247 polysaccharide binding and the separable polymer-handling core. Pa length-dependent binding is not generalized to the Pp ortholog, which behaves differently in PMID:36494359.

The production/export role is separable from catalytic modification. PMID:15489449 measures periplasm localization and nonpolar deletion with degraded oligomannuronate secretion, supporting protection/export of polymer. It contains no direct biofilm assay. PMID:36494359 Figure 5 directly measures alginate production and crystal-violet adherence in PAO1-derived algX deletion, WT complementation and N-terminal-interface mutant strains. WT complementation restores adherence; the interface mutant is defective. Its structural/biophysical complex work is P. putida and must be distinguished from these native P. aeruginosa assays. The existing biofilm row is retained non-core using this independent primary evidence, without changing its original citation fields. Broad alginic-acid biosynthesis rows are retained because the noncatalytic production/export contribution is not exhausted by acetylation.

NEW process GO:0051979 checks: (1) AlgX itself performs the chemical acetyl-transfer step on polymer; the case does not rest on knockout necessity. (2) Live QuickGO exact-term queries on 2026-10-25 found Q51392/AlgI with one GO0051979 annotation, Q51393/AlgJ with two, and Q06062/AlgF with two; these are catalytic-machinery/scaffold-role comparators, not precursor substrates. Comparator annotations establish convention only and are not cited as functional support. (3) QuickGO ancestors of GO0051979 include carbohydrate/polysaccharide metabolism, not GO0042121 alginic acid biosynthesis; neither term is an ancestor/descendant of the other. (4) gocams/index.tsv contains no matches to Q51392/Q51393/Q06062/Q51372 or algI/algJ/algF/algX, so no existing model assigns a contrary role. (5) The new process is not redundant with another proposed process. The direct biochemical assay and independent catalytic-site genetics justify this addition.

No PANTHER DR cross-reference is present. Pfam PF16822 ALGX and PF16824 CBM_26 identify the catalytic and carbohydrate-binding domains.

## Source and workflow provenance

Normal supported fetch seeded the exact accession and original GOA-derived fields; all 6 original rows were assessed individually and preserved. All publications cited in original annotations were cached and inspected. The 12003941 and 23779107 force-refresh attempts still yielded abstract-only caches. 31900562 has legacy full_text_html metadata but only duplicated abstract/repository content, so it is treated as abstract access. Substantive full text was available for 25165982, 37797696, 40171682 and, where used, 15489449 and 36494359. PMID:40171682 is a review and its relay model is distinguished from native experimental chemistry.

The review and annotation-reviewer workflows were applied, followed by activity-centered core synthesis. The default Falcon attempt on algI ran concurrently with publication caching and failed authentication; the Perplexity-lite fallback failed quota/credit availability (/tmp/bacillus-algI-deep.log). The established outage was not retried for the other three genes, and no provider-authored report was fabricated. FEBA fetch was attempted for all four bacteria; no local data were available and bulk retrieval failed (/tmp/bacillus-algX-fitness.log). No fitness inference is made.

GO:0051979 alginic acid acetylation is not a descendant of GO:0042121 alginic acid biosynthesis. Where the biosynthesis row is modified, the reason explicitly makes a lateral synthesis-to-modification correction. AlgX retains a separate production/export contribution. Quoted UniProt sections are backfilled with the supported helper. Publication text and source flat files are not manually altered. Matching codex history and targeted validation are completed after edits.

Annotation totals: 9 including 3 NEW; {'ACCEPT': 5, 'KEEP_AS_NON_CORE': 1, 'NEW': 3}.

Validation outcome: `just validate PSEAE algX` passed with no curation warnings, and the matching codex history passed schema validation. Original seeded annotation fields were compared to the saved seed and remain unchanged.

## Independent final QA, 2026-10-25

Corrected the PMID:37797696 construct attribution: the negative surrogate acetylesterase assay and binary ITC use P. putida proteins, whereas the isolated AlgF oligosaccharide-binding assay uses P. aeruginosa AlgF. The Results explicitly state “AlgFPa did not display any affinity for the oligomers tested.” This supersedes any earlier grouping of both negative assays as Pp. Native Pa co-IP and the Pa NMR structure remain target-specific.

## Deep research availability, 2026-11-02

No provider deep-research report exists for this gene. During the alginate O-acetylation module audit, `just deep-research-falcon PSEAE algI` was retried and failed with "403 Failed to authenticate"; earlier Falcon and Perplexity attempts for the KT2440 homologs also failed (see genes/PSEPK/algI/algI-notes.md). No deep-research file was written by hand. The review instead rests on cached primary publications, the UniProt record and the existing annotation reviews.
