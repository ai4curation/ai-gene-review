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
