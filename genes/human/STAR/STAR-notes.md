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
