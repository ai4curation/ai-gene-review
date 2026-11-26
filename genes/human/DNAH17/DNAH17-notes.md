# DNAH17 notes

## Deep research
- `just deep-research-falcon human DNAH17` failed (Edison/FutureHouse API: "Failed to authenticate"). No deep-research file; literature gathered from PubMed E-utilities (`DNAH17[tiab]`, 73 hits, many unrelated lncRNA DNAH17-AS1 papers) and cached with `just fetch-pmid`.

## Identity and structure
- Beta-type ODA heavy chain, sperm paralog of DNAH9/DNAH11 [PMID:31178125 "γ-type: DNAH5 and DNAH8 and β-type: DNAH9, DNAH11, and DNAH17"]. 4462 aa; synonyms DNAHL1, DNEL2. ATP P-loop AAA1 1847-1854 (UniProt).

## Localization
- Sperm axoneme only, not respiratory cilia [PMID:31178125 "We show that DNAH17 and DNAH8, but not DNAH5, DNAH9, or DNAH11, colocalize with α-tubulin along the sperm axoneme"].
- ODA loss in midpiece, principal piece and end piece of mutant sperm [PMID:41549443 "revealed a lack of outer dynein arms (ODAs) in the middle, principal, and end pieces of the flagella"].

## Disease / models
- SPGF39 [PMID:31178125 "By analyzing five male individuals who consulted for isolated infertility and displayed a loss of ODAs in their sperm cells but not in their respiratory cells, we identified bi-allelic mutations in DNAH17."].
- Mouse KO MMAF [PMID:33070343 "Similar to those found in patients, Dnah17-/- mice also displayed MMAF phenotype along with completely disorganized axonemal structures."]; rat KO infertile [PMID:33764336]; pig splice deletion MMAF [PMID:33724408].
- ODA assembly/docking defect [PMID:40009974 "DNAH17 deficiency impaired the assembly and docking of outer dynein arms"]; co-depletion of DNAH8, DNAI1, ODAD2, ODAD4 [PMID:41549443].
- ICSI outcomes variable; AOA sometimes required [PMID:37574497]; fertilization failure case [PMID:34126833].
- Candidate laterality association, unconfirmed [PMID:35692830 "We report for the first time a possible association between DNAH17 gene variants and left-right asymmetry disorders"].

## Annotation review decisions
- Core: minus-end-directed microtubule motor activity; outer dynein arm (IDA accepted); sperm flagellum/axoneme.
- REMOVE dynein light intermediate chain binding (IBA + IEA), same reasoning as DNAH8.
- MODIFY generic dynein complex (IBA, IEA) -> outer dynein arm; NAS cilium-dependent cell motility -> flagellated sperm motility.
- ODA assembly IDA kept as non-core (structural subunit participation).
- NEW: flagellated sperm motility (GO:0030317).

## PANTHER / IBA
- UniProt PANTHER xref: PTHR45703:SF4 (DYNEIN AXONEMAL HEAVY CHAIN 17), same as mouse Dnah17 (Q69Z23). GOA IBAs come from PTHR10676 nodes (PTN000743491, PTN000073047). Human and mouse both have 7 IBAs in QuickGO (checked 2026-10-14); no human/mouse IBA gap. Unlike DNAH8, DNAH17 gets no IBA for outer dynein arm or sperm flagellum (it has IDA for both instead).

## 2026-10-17 — consolidate duplicate sperm-motility coverage

The earlier standalone NEW GO:0030317 proposal duplicated the same term already proposed as the replacement for the imported GO:0060285/NAS/PMID:9373155 annotation. The functional participation argument remains supported: DNAH17 is a force-generating component of the sperm outer dynein arm. This correction removes only the redundant authored proposal and consolidates its unique supporting citations into that existing MODIFY review. All 28 genuine source annotations, their original identities, every other review decision, the integrated core, products and reference list are preserved. No additional verbatim excerpts were introduced; the earlier proposal remains available in the append-only Git/history record.

The prior PR #5009 approval remains part of the provenance. This correction addresses duplicate coverage, not a withdrawal of the positive motility evidence or a new completion-credit decision.

## 2026-10-17 — sperm-motility evidence and comparator scope

The human study reported DNAH17 along sperm axonemes but not the examined respiratory cilia; affected men lost sperm outer dynein arms while respiratory arms were preserved. This supports flagellated sperm motility as the informative replacement for the broad cell-motility assertion. DNAH17 supplies the outer-arm heavy-chain motor component. These observations do not establish its absence from every untested motile-cilium context [PMID:31178125](https://pubmed.ncbi.nlm.nih.gov/31178125/). The independent Dnah17-null mouse result supports a requirement for organized sperm flagella; that phenotype is not a purified motor-kinetics measurement [PMID:33070343](https://pubmed.ncbi.nlm.nih.gov/33070343/). The original NAS source remains attached to the imported annotation [PMID:9373155](https://pubmed.ncbi.nlm.nih.gov/9373155/). This follow-up inspected the complete cached abstracts of these three papers, not their full Methods.

The earlier comparator rationale is now independently checked against a [QuickGO exact-term mouse query](https://www.ebi.ac.uk/QuickGO/services/annotation/search?goId=GO%3A0030317&goUsage=exact&taxonId=10090&limit=200&page=1), retrieved on 2026-10-17. The first 200 of 458 returned annotations contain all five previously named examples: Dnah1 (E9Q8T7) and Dnah11 (E9Q7N9) include IMP records, while the recovered Dnah7a (E9Q0T8), Dnah7b (A0A571BD48/L7N1Y0), and Dnah7c (A0A087WR13) records are electronic. This verifies positive comparator annotation presence, not equivalent experimental support for all five or an independent demonstration of the human function. The remaining query pages and the comparator primary papers were not inspected for this bounded check. The biological human evidence remains the basis for the replacement; no duplicate NEW assertion is needed.

The existing mouse loss-of-function excerpt was moved from the core's support entry to the imported cell-motility review, where it anchors the specific process replacement. The core retains reference-only support from the same paper. No new verbatim publication text was added, and the inherited notes and reference assessments remain unchanged.


## 2026-10-17: local mouse-phenotype anchor

The integrated motor/structural core now includes a concise local abstract anchor for the mouse axonemal phenotype in [PMID:33070343](https://pubmed.ncbi.nlm.nih.gov/33070343/). The process-row anchor remains in place. This does not add a purified motor assay or change the human-versus-mouse evidence distinction. All earlier annotation decisions, products and biological core statements are retained.


### DNAH17 movement specificity follow-up (2026-10-17)

The broad PAINT cilium-movement assertion is retained biologically and refined to flagellated sperm motility. Human sperm axonemal localization and selective sperm outer-arm defects, with preservation of the examined respiratory cilia, support the sperm context [PMID:31178125]. The mouse phenotype corroborates the requirement but does not measure purified motor kinetics [PMID:33070343]. Current [GO:0030317](https://www.ebi.ac.uk/QuickGO/term/GO:0030317) is an is_a child of both [GO:0060294](https://www.ebi.ac.uk/QuickGO/term/GO:0060294) and [GO:0060285](https://www.ebi.ac.uk/QuickGO/term/GO:0060285); GO:0060294 is part_of GO:0060285. The IBA row therefore uses MODIFY with GO:0030317, matching the supported replacement already present on the NAS row. No NEW row is added, and the previous pointer to one is corrected. These typed relationships were retrieved from official QuickGO on 2026-10-17; the previously recorded mouse comparator evidence is unchanged.


### Specificity metadata for the movement annotation

The structured propagation assessment on GO:0060294 records a term-granularity refinement to its verified child GO:0030317, consistent with the human sperm evidence (PMID:31178125) and the existing sperm-motility replacement. It does not allege a faulty PAINT ancestor or a loss of the inherited movement function. No newly inspected donor or ancestral-node evidence is asserted by this metadata-only addition.
