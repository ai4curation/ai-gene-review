# thiI (Q88CY4, PP_5045) - Pseudomonas putida KT2440 - review notes

## 2026-11-12 completion pass (thiamine diphosphate biosynthesis batch)

Deep-research providers were not available in this session; the existing
`thiI-deep-research-falcon.md` was used and its key KT2440 claim was checked against
the cached primary paper. No new provider file was created.

### Evidence

- KT2440 genetics: [PMID:37891428 "As expected, the content of 4-thiouridine in bulk tRNA was drastically reduced in the ΔthiI knockout strain (negative control)."] (full text cached; delta-thiI n = 1, used as a negative control).
- Mechanism (E. coli ortholog): [PMID:15037613 "IscS catalyzes sulfur transfer from l-cysteine to ThiI, which utilizes Mg-ATP to activate uridine 8 in tRNA and transfers sulfur to give s4U"]; [PMID:10595545 "ThiI catalyzes the adenylation of a substrate at the expense of ATP"].
- Thiazole role (orthologs): [PMID:9632726 "ThiS isolated from a thiI- strain does not contain this modification"]; [PMID:21724998 "the C-terminal rhodanese domain of ThiI was sufficient for thiazole synthesis in vivo"].
- KT2440 ThiI is 484 aa with THUMP (63-167), PP-loop AANH, and C-terminal rhodanese (405-483) domains, active-site Cys457, and the thiazole-specific signatures IPR026340 / TIGR04271 (UniProt Q88CY4). So it is the E. coli-type bifunctional ThiI, not the rhodanese-less Firmicute type (B. subtilis).
- The module notes PP_5105 as the KT2440 ThiS sulfur carrier (modules/thiamine_diphosphate_biosynthesis.yaml).

### Decisions (aligned with genes/ECOLI/thiI where the evidence is the same)

- GO:0000049 tRNA binding: KEEP_AS_NON_CORE (as E. coli, B. subtilis).
- GO:0002937 tRNA 4-thiouridine biosynthesis: ACCEPT (KT2440 delta-thiI phenotype).
- GO:0003723 RNA binding: MODIFY -> GO:0000049 (as E. coli, B. subtilis; previously MARK_AS_OVER_ANNOTATED, which contradicted the "correct but general is MODIFY" rule).
- GO:0004810 CCA tRNA nucleotidyltransferase: REMOVE (InterPro2GO IPR020536 mis-mapping; upstream report already filed from the E. coli review).
- GO:0005524 ATP binding: KEEP_AS_NON_CORE.
- GO:0005737 cytoplasm: MODIFY -> GO:0005829 cytosol (as E. coli).
- GO:0005829 cytosol: ACCEPT (site of the core activity; as E. coli).
- GO:0009229 thiamine diphosphate biosynthesis: KEEP_AS_NON_CORE (pathway endpoint; as E. coli; B. subtilis REMOVE because it lacks the rhodanese domain).
- GO:0016783 sulfurtransferase activity: MODIFY -> GO:0140741 + NTR ThiS sulfur-carrier protein sulfurtransferase activity (as E. coli).
- GO:0034227 tRNA thio-modification: MODIFY -> GO:0002937 (as E. coli, B. subtilis).
- GO:0052837 thiazole biosynthesis: ACCEPT (rhodanese-containing ThiI; as E. coli).
- GO:0140741 tRNA-uracil-4 sulfurtransferase activity: ACCEPT (core).

PTHR43209 family review is in an open PR (#5985); not duplicated here.
