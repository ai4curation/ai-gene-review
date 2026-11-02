# algF manual research and annotation review

## 2026-10-25 evidence synthesis

Q06062 / PA3546 encodes AlgF. PMID:7934909 distinguishes an algF acetylation defect from the downstream algA polar effect that initially eliminates polymer production. PMID:12003941 places soluble mature AlgF in the periplasm. PMID:31900562 reports a strain-dependent polymer-yield/stability effect, which does not establish direct glycosyltransferase chemistry.

PMID:37797696 is the principal functional advance: Pa AlgF has a two-beta-sandwich architecture and native AlgF–AlgX association; Pp AlgF directly binds Pp AlgJ and AlgX by ITC (Kd 86±12 and 178±5 micromolar). These direct ITC assays use P. putida constructs, not Q06062. The reported negative acetylesterase and polymer-binding assays also use the Pp construct; one sentence inconsistently says “P. aeruginosa AlgFPp”, but the methods, figure labels and construct definitions identify Pp. Do not turn this into a directly measured Pa negative assay. Adding Pp AlgF did not increase the measured surrogate-substrate hydrolysis.

The NEW GO:0030674 protein-macromolecule adaptor activity is an explicitly inferred synthesis of native complex association, target requirement and ortholog pairwise binding. It is not bare protein binding, a direct measurement of a ternary bridge, or an assertion of catalytic activation. QuickGO defines an adaptor as bringing macromolecules into contact for coordinated function. The authors propose exactly this mediator role, while the exact simultaneous bridge and native acetyl handoff remain unresolved. A generic or terminal acetyltransferase MF is not assigned to AlgF.

No PANTHER DR cross-reference is present; Pfam PF11182 AlgF is the exact family evidence.

## Source and workflow provenance

Normal supported fetch seeded the exact accession and original GOA-derived fields; all 4 original rows were assessed individually and preserved. All publications cited in original annotations were cached and inspected. The 12003941 and 23779107 force-refresh attempts still yielded abstract-only caches. 31900562 has legacy full_text_html metadata but only duplicated abstract/repository content, so it is treated as abstract access. Substantive full text was available for 25165982, 37797696, 40171682 and, where used, 15489449 and 36494359. PMID:40171682 is a review and its relay model is distinguished from native experimental chemistry.

The review and annotation-reviewer workflows were applied, followed by activity-centered core synthesis. The default Falcon attempt on algI ran concurrently with publication caching and failed authentication; the Perplexity-lite fallback failed quota/credit availability (/tmp/bacillus-algI-deep.log). The established outage was not retried for the other three genes, and no provider-authored report was fabricated. FEBA fetch was attempted for all four bacteria; no local data were available and bulk retrieval failed (/tmp/bacillus-algF-fitness.log). No fitness inference is made.

GO:0051979 alginic acid acetylation is not a descendant of GO:0042121 alginic acid biosynthesis. Where the biosynthesis row is modified, the reason explicitly makes a lateral synthesis-to-modification correction. AlgX retains a separate production/export contribution. Quoted UniProt sections are backfilled with the supported helper. Publication text and source flat files are not manually altered. Matching codex history and targeted validation are completed after edits.

Annotation totals: 5 including 1 NEW; {'MODIFY': 1, 'ACCEPT': 3, 'NEW': 1}.

Validation outcome: `just validate PSEAE algF` passed with no curation warnings, and the matching codex history passed schema validation. Original seeded annotation fields were compared to the saved seed and remain unchanged.

## Independent final QA, 2026-10-25

Corrected the PMID:37797696 construct attribution: the negative surrogate acetylesterase assay and binary ITC use P. putida proteins, whereas the isolated AlgF oligosaccharide-binding assay uses P. aeruginosa AlgF. The Results explicitly state “AlgFPa did not display any affinity for the oligomers tested.” This supersedes any earlier grouping of both negative assays as Pp. Native Pa co-IP and the Pa NMR structure remain target-specific.

Withdrew the newly proposed GO:0030674 adaptor annotation and its intrinsic-MF core assignment. QuickGO defines the activity as bringing two or more macromolecules into contact; separate binary interactions do not establish that bridging. The authors’ bridge model is retained as a hypothesis. The supported process and compartment core remains, without replacing the withdrawn MF with a similarly unproved contributes_to catalytic-complex claim. This supersedes the initial five-row total and adaptor rationale above: four original rows remain, with no NEW row.

Retained the existing biosynthesis annotation after reassessing the later PDO300 nonpolar deletion and machinery-stability experiments in PMID:31900562. Biosynthetic participation includes structural organization and does not require polymerase catalysis. The earlier FRD1 algA polar-effect result remains valid but does not refute the later strain-dependent production contribution. Final four rows are all ACCEPT; acetylation and biosynthesis are not ancestor/descendant duplicates.
