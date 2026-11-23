# STAR (Steroidogenic acute regulatory protein, StAR / StARD1) — review notes

UniProtKB: P49675 (STAR_HUMAN), 285 aa, HGNC:11359, gene 8p11.2 (pseudogene on chr 13).

## Deep research status
Falcon deep-research is OUT OF CREDITS (HTTP 402); no `-deep-research-falcon.md` was generated.
Review grounded in `STAR-uniprot.txt`, seeded GOA (`STAR-goa.tsv`), and the cached
`publications/PMID_*.md` (all cited PMIDs present) plus cached Reactome entries.

## Core biology
StAR is the **steroidogenic acute regulatory protein**, a START-domain (StAR-related lipid
transfer) protein. It is NOT an enzyme. Its molecular function is **cholesterol binding /
cholesterol transfer**; it mediates the **rate-limiting, acute (minutes-scale) step of
steroidogenesis**: delivery of cholesterol from the outer to the inner mitochondrial membrane,
where CYP11A1 (P450scc) cleaves cholesterol to pregnenolone.

- UniProt FUNCTION: "Plays a key role in steroid hormone synthesis by enhancing the metabolism
  of cholesterol into pregnenolone. Mediates the transfer of cholesterol from the outer
  mitochondrial membrane to the inner mitochondrial membrane where it is cleaved to
  pregnenolone." (ECO from PubMed:12530629, 7761400, 7892608, 8948562)
- CATALYTIC ACTIVITY annotated in UniProt is a transport reaction (Rhea:39747):
  cholesterol(in) = cholesterol(out) — i.e., a transfer, not a chemical transformation.
- PATHWAY: Steroid metabolism; cholesterol metabolism.

## Localization / mechanism
- [PMID:12530629 "StAR works only on the OMM ... exerts its biological activity in a cellular
  location it occupies only transiently, rather than in the location (the matrix) to which it
  is targeted"]. Constructs immobilizing StAR on the OMM were active; matrix/IMS ones were not.
  So although the mature protein ends up in the matrix, its site of ACTION is the OMM.
- [PMID:17433772 (Miller, review) "StAR moves large amounts of cholesterol from the outer to
  inner mitochondrial membrane, but acts exclusively on the outer membrane"]; only the
  C-terminal alpha-helix interacts with the OMM; molten-globule transition required for activity.
- Reactome R-HSA-196126: "STAR steroidogenic acute regulatory protein mediates its delivery to
  the mitochondrial inner membrane"; R-HSA-196108 (Pregnenolone biosynthesis): "Cholesterol
  transport appears to be rate-limiting for steroid hormone synthesis ... at the step of
  StAR-mediated traversal of the mitochondrial membrane."
- Mitochondrion localization also supported by high-throughput proteomics
  [PMID:34800366 MitoCoP high-confidence human mitochondrial proteome, HTP].

## Tissue / disease
- Expressed in gonads, adrenal cortex, kidney (UniProt TISSUE SPECIFICITY); HPA: adrenal-enriched.
- Loss of function → congenital lipoid adrenal hyperplasia (Adrenal hyperplasia 1, AH1;
  MIM:201710): impaired synthesis of ALL adrenal and gonadal steroids, lipid accumulation,
  male pseudohermaphroditism. [PMID:7892608 "In three unrelated individuals ... steroidogenic
  acute regulatory protein ... was mutated and nonfunctional, providing genetic evidence that
  this protein is indispensable normal adrenal and gonadal steroidogenesis"].

## Function / activity evidence
- [PMID:7761400 "Human StAR, coexpressed in COS-1 cells with cytochrome P450scc and adrenodoxin,
  increased pregnenolone synthesis > 4-fold"] — functional steroidogenic activity; also tissue
  expression (ovary, testis, kidney) and gene mapping.
- [PMID:7892608] — genetic (loss-of-function) evidence, glucocorticoid/steroid deficiency.

## Annotation-specific caveats
- **PMID:18403318 is a StarD4 (StARD1 paralog) paper.** GOA carries two IDA annotations to STAR
  from it: cholesterol binding (GO:0015485) and positive regulation of bile acid biosynthetic
  process (GO:0070859). The abstract explicitly names StarD1 only as a comparison for cholesterol
  binding ("...binding of [14C]cholesterol by StarD4 similar to that of the cholesterol binding
  START domain proteins StarD1 and StarD5"). The bile-acid regulation phenotype is a StarD4
  property (hepatocyte overexpression), not a demonstrated STAR/StARD1 function. Per policy I do
  not REMOVE experimental annotations whose full text I can't verify; the bile-acid one is
  MARK_AS_OVER_ANNOTATED (misattributed-looking; not a core STAR function). Cholesterol binding
  is well-supported for STAR from many other sources, so ACCEPT that one.
- **protein binding (GO:0005515) IPIs (x5 references, many IntAct pairs):** high-throughput
  interactome / IntAct pairs (MAGEA11, HTT, RABEP1, SMPD2, STX8, AGTRAP, CMTM4, DGAT2L6, etc.).
  Uninformative "protein binding"; none is an established functional partner in steroidogenesis
  (UniProt only notes a putative TSPO interaction by similarity). Per policy: do not REMOVE bare
  protein-binding IPIs — MARK_AS_OVER_ANNOTATED.
- **mitochondrial matrix (GO:0005759):** StAR is targeted to the matrix but is imported and
  degraded there; its functional site is the OMM (PMID:12530629). Matrix location is real
  (where the mature protein ends up) but non-core. IEA matrix from SubCell and TAS-Reactome
  (LONP1/AFG3L2 degradation modules) reflect that it is a matrix-imported protein subject to
  proteolysis — KEEP_AS_NON_CORE.
- **cholesterol transfer activity (GO:0120020)** — this is the specific MF (a lipid transfer
  activity), preferred over the broad Reactome TAS "molecular carrier activity" (GO:0140104,
  MODIFY→GO:0120020) and "lipid binding" (GO:0008289, MODIFY→GO:0015485).

## Core functions (for review)
- MF: cholesterol transfer activity (GO:0120020) + cholesterol binding (GO:0015485).
- BP: intracellular cholesterol transport (GO:0032367) / cholesterol transport (GO:0030301);
  regulation of steroid biosynthetic process (GO:0050810) as the acute regulator; contributes to
  steroid/pregnenolone/glucocorticoid biosynthesis.
- CC: mitochondrial outer membrane (GO:0005741) is the functional site; mitochondrion (GO:0005739).

## 2026-10-25 full annotation audit

This audit supersedes earlier policy and citation conclusions above. All 44 original rows were assessed; original term/evidence/reference/qualifier fields are unchanged.

- **Actual work:** STAR binds and transfers cholesterol. It supplies the substrate for CYP11A1 and thereby participates in adrenal and gonadal steroidogenesis; it does not oxidize cholesterol. [PMID:12372832, "Thus StAR can transfer cholesterol between synthetic membranes without other protein components found in mitochondria."] Primary vesicle work complements the human cellular reconstitution in PMID:7761400 and human deficiency evidence in PMID:7892608.
- **Wrong-paralog suspicion corrected:** supported cache refresh of PMID:18403318 recovered full text. StarD1 was actually tested alongside STARD4, with direct cholesterol-binding comparison and a bile-acid synthesis increase after overexpression in primary mouse hepatocytes [PMID:18403318, "rates similar to that observed after StarD1 overexpression (10-fold increase)."]. GO:0070859 is KEEP_AS_NON_CORE, not misattributed. The experiment does not show normal human liver expression or an adrenal bile-acid role.
- **Localization:** active STAR acts at the OMM; imported matrix STAR is retained as a non-core location and substrate of turnover. Broad mitochondrion rows refine to both supported compartments. The separate intermembrane-space claim remains UNDECIDED: moving cholesterol across a compartment does not locate the protein there, and OMM activity does not exclude transient import transit. No proteolysis participation is inferred from being a LONP1/AFG3L2 substrate.
- **Tissue limits:** human STAR expression was reported in adrenal/gonadal contexts but not placenta in PMID:7761400. STAR dependence is not a universal rule for all steroidogenic cells or all vertebrates. Historical suggestions of a compulsory TSPO partnership are not promoted to a core complex.
- **GO-CAM inspected:** `685de18700001735` general transport, `685de18700001799` gonads, and `68b0f0d000007688` adrenal. The adrenal model places GO:0120020 at GO:0005741 in UBERON:0002369, with cholesterol transport nested within glucocorticoid biosynthesis. These curator roles agree with direct transfer, not enzymatic steroid conversion.
- **Family:** PANTHER:PTHR46489 and :SF1 both have official label STEROIDOGENIC ACUTE REGULATORY PROTEIN, MITOCHONDRIAL. The cached PAINT file places the steroid-biosynthesis IBD at PTN000253339. Refinement to steroid hormone biosynthesis does not reject that node or treat human STAR appearing among descendant sources as circular.
- Five bare protein-binding rows are REMOVE under the current policy, without rejecting the interactions. Broad location/process terms are refined, not rejected as false. PMID:12530629 and PMID:17433772 are indexed as reviews; their original evidence fields are preserved and focused primary support added.

### Retrieval and validation provenance

Falcon deep research was attempted for human/STAR with perplexity-lite fallback. Falcon failed authentication (403) and Perplexity returned insufficient_quota (401). No provider research file was fabricated. Manual source-specific findings are recorded here and in reference reviews. Publication caching ran concurrently with research retrieval; initial NCBI 429 failures were retried only for missing records. Existing caches were not force-refreshed except the key abstract-only PMID18403318 and PMID21636783 records needed for source-specific adjudication.

### Reviewed row ledger

1. GO:0006694 (IBA; GO_REF:0000033): MODIFY — STAR-mediated cholesterol delivery participates in steroid hormone biosynthesis.
2. GO:0032367 (IBA; GO_REF:0000033): ACCEPT — STAR facilitates intracellular cholesterol delivery from the mitochondrial outer to inner membrane.
3. GO:0015485 (IBA; GO_REF:0000033): ACCEPT — The STAR START domain binds cholesterol.
4. GO:0050810 (IBA; GO_REF:0000033): ACCEPT — Phylogenetic annotation for regulation of steroid biosynthesis. This captures StAR's defining role as the ACUTE regulator of steroidogenesis: cholesterol delivery across the mitochondrial membranes is rate-limiting, and StAR abundance (a labile protein induced by tropic hormones) sets the pace of steroid output.
5. GO:0005739 (IEA; GO_REF:0000002): MODIFY — STAR reaches mitochondria, with distinct active and post-import locations.
6. GO:0005741 (IEA; GO_REF:0000044): ACCEPT — UniProt SubCell electronic annotation to the mitochondrial outer membrane, the functional site of action of StAR.
7. GO:0005759 (IEA; GO_REF:0000044): KEEP_AS_NON_CORE — STAR is imported into the mitochondrial matrix after its productive outer-membrane action.
8. GO:0006694 (IEA; GO_REF:0000002): MODIFY — STAR-mediated cholesterol delivery participates in steroid hormone biosynthesis.
9. GO:0008289 (IEA; GO_REF:0000002): MODIFY — The STAR START domain binds cholesterol.
10. GO:0015485 (IEA; GO_REF:0000002): ACCEPT — The STAR START domain binds cholesterol.
11. GO:0015918 (IEA; GO_REF:0000117): MODIFY — ARBA electronic annotation for sterol transport. Correct at a broad level; cholesterol is a sterol, and StAR transports it between mitochondrial membranes. The more specific term intracellular cholesterol transport (GO:0032367) is separately annotated with experimental support.
12. GO:0042446 (IEA; GO_REF:0000117): MODIFY — ARBA electronic annotation for hormone biosynthetic process. StAR is required for steroid HORMONE synthesis, so this is correct but the more specific steroid hormone biosynthetic process (GO:0120178) is preferable.
13. GO:0120020 (IEA; GO_REF:0000002): ACCEPT — STAR transfers cholesterol between membranes.
14. GO:0120178 (IEA; GO_REF:0000117): ACCEPT — ARBA electronic annotation for steroid hormone biosynthetic process. StAR initiates steroid hormone synthesis by delivering cholesterol for conversion to pregnenolone.
15. GO:0005515 (IPI; PMID:25416956): REMOVE — IntAct-curated binary protein-protein interaction (IPI) from a proteome-scale interactome study (interactor MAGEA11, P43364-2). The bare term protein binding is uninformative about StAR's actual function.
16. GO:0005515 (IPI; PMID:25910212): REMOVE — IntAct-curated binary interaction (IPI) from a systematic interactome perturbation study (interactor G5E962 / MAGEA11). Uninformative protein binding term.
17. GO:0005515 (IPI; PMID:26871637): REMOVE — IntAct-curated binary interaction (IPI) from an alternative-splicing interactome study (interactor P43364 / MAGEA11). Uninformative protein binding term.
18. GO:0005515 (IPI; PMID:32296183): REMOVE — IntAct-curated binary interactions (IPI) from the HuRI reference human interactome (interactors incl. O60906/SMPD2, P43364/MAGEA11, Q15276/RABEP1, Q6RW13-2/AGTRAP, Q6ZPD8/DGAT2L6, Q8IZR5-2/CMTM4, Q9UNK0/STX8). Bare protein binding, uninformative.
19. GO:0005515 (IPI; PMID:32814053): REMOVE — IntAct-curated binary interaction (IPI) from a neurodegenerative-disease interactome study (interactor P42858 / HTT, huntingtin). Uninformative protein binding term.
20. GO:0006700 (TAS; Reactome:R-HSA-196108): ACCEPT — Reactome traceable annotation placing StAR in C21-steroid (pregnane) hormone biosynthesis, via the Pregnenolone biosynthesis pathway. Correct: StAR delivers cholesterol so CYP11A1 can generate pregnenolone (a C21-steroid), the precursor of glucocorticoids, mineralocorticoids and progestins.
21. GO:0008203 (IEA; GO_REF:0000041): ACCEPT — STAR participates in the cholesterol utilization pathway by delivering its substrate.
22. GO:0005759 (EXP; PMID:12530629): KEEP_AS_NON_CORE — STAR is imported into the mitochondrial matrix after its productive outer-membrane action.
23. GO:0005741 (IDA; PMID:12530629): ACCEPT — Direct experimental localization of StAR to the mitochondrial outer membrane, its functional site of action.
24. GO:0006704 (IDA; PMID:12530629): ACCEPT — STAR provides mitochondrial cholesterol delivery for adrenal glucocorticoid biosynthesis.
25. GO:0032367 (IDA; PMID:12530629): ACCEPT — STAR facilitates intracellular cholesterol delivery from the mitochondrial outer to inner membrane.
26. GO:0032367 (EXP; PMID:7892608): ACCEPT — STAR facilitates intracellular cholesterol delivery from the mitochondrial outer to inner membrane.
27. GO:0120020 (EXP; PMID:12530629): ACCEPT — STAR transfers cholesterol between membranes.
28. GO:0120020 (IDA; PMID:12530629): ACCEPT — STAR transfers cholesterol between membranes.
29. GO:0120020 (EXP; PMID:7892608): ACCEPT — STAR transfers cholesterol between membranes.
30. GO:0005741 (EXP; PMID:12530629): ACCEPT — Experimental is_active_in annotation: StAR exerts its cholesterol-transfer activity at the mitochondrial outer membrane. This is the most precise statement of where StAR functions.
31. GO:0005741 (EXP; PMID:17433772): ACCEPT — Experimental is_active_in annotation confirming StAR acts exclusively on the mitochondrial outer membrane.
32. GO:0032367 (EXP; PMID:17433772): ACCEPT — STAR facilitates intracellular cholesterol delivery from the mitochondrial outer to inner membrane.
33. GO:0120020 (EXP; PMID:17433772): ACCEPT — STAR transfers cholesterol between membranes.
34. GO:0006704 (EXP; PMID:7892608): ACCEPT — STAR provides mitochondrial cholesterol delivery for adrenal glucocorticoid biosynthesis.
35. GO:0140104 (TAS; Reactome:R-HSA-196126): MODIFY — Reactome traceable annotation to the broad molecular carrier activity term. StAR is indeed a cholesterol carrier, but the specific term cholesterol transfer activity (GO:0120020) is far more informative and is well supported experimentally.
36. GO:0005739 (HTP; PMID:34800366): MODIFY — STAR reaches mitochondria, with distinct active and post-import locations.
37. GO:0005759 (TAS; Reactome:R-HSA-9838081): KEEP_AS_NON_CORE — STAR is imported into the mitochondrial matrix after its productive outer-membrane action.
38. GO:0005759 (TAS; Reactome:R-HSA-9838093): KEEP_AS_NON_CORE — STAR is imported into the mitochondrial matrix after its productive outer-membrane action.
39. GO:0005759 (TAS; Reactome:R-HSA-9839105): KEEP_AS_NON_CORE — STAR is imported into the mitochondrial matrix after its productive outer-membrane action.
40. GO:0005759 (TAS; Reactome:R-HSA-9839149): KEEP_AS_NON_CORE — STAR is imported into the mitochondrial matrix after its productive outer-membrane action.
41. GO:0015485 (IDA; PMID:18403318): ACCEPT — The STAR START domain binds cholesterol.
42. GO:0070859 (IDA; PMID:18403318): KEEP_AS_NON_CORE — STAR overexpression enhances bile-acid synthesis in a cultured-hepatocyte assay.
43. GO:0005758 (TAS; Reactome:R-HSA-196126): UNDECIDED — The Reactome assignment to intermembrane space is not resolved by the outer-membrane activity experiments.
44. GO:0006694 (TAS; PMID:7761400): MODIFY — STAR-mediated cholesterol delivery participates in steroid hormone biosynthesis.

Counts: 9 MODIFY, 22 ACCEPT, 7 KEEP_AS_NON_CORE, 5 REMOVE, 1 UNDECIDED. No NEW annotations were added. All original seeded annotation fields were preserved.

## Root-organelle correction, 2026-10-26

The supported root mitochondrion annotations are retained as ACCEPT, separately from unchanged subcompartment claims. This supersedes earlier journal wording that refined the root location or treated its breadth as non-core. Original annotation payloads, unrelated review decisions and core functions are preserved. Source-specific rationales distinguish curated location/inference, original experimental annotations and source access limits; no new assay or target-table inspection is claimed.
