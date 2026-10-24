# DNAH1 curation notes

Deep research: `just deep-research-falcon human DNAH1` failed (Edison API "Failed to
authenticate", three attempts across the three IDA genes); no deep-research file exists.
The review is based on the cached publications and UniProt record listed below.

## Identity and structure
- Q9P2D7, 4265 aa; stem 1-1542 plus AAA1-AAA6 motor with stalk (UniProt FT REGION).
  UniProt function: [file:human/DNAH1/DNAH1-uniprot.txt "Produces force towards the minus ends of"].
- Classified as an axonemal inner-arm heavy chain at cloning [PMID:9373155 "Two of these clones,
  gHDHC7 and gMDHC7, are homologous genes encoding axonemal inner arm dyneins."].
- Assigned to IDA d in respiratory cilia [PMID:39056782 "affects the encoded heavy chains DNAH1 and
  DNAH7 of IDAd and IDAb/e, respectively"].

## Localization
- Sperm flagellum, full length [PMID:24360805 "In control individuals, DNAH1 antisera decorated the
  full length of the sperm flagellum"].
- Respiratory cilia, full length [PMID:39056782 "IF staining against DNAH1 demonstrated the
  localization along the full-length ciliary axoneme."].

## Partners and dependencies
- DNALI1 [PMID:36792588 "As anticipated, the murine DNALI1 is localized within the entire sperm
  flagellum and interacts with the HDC subunit DNAH1 in the testis"]; DNAH1 is lost from
  DNALI1-deficient flagella [PMID:36792588 "Accordingly, we demonstrated that DNAH1 and DNAH7 were
  absent from the flagella lacking DNALI1 in both species."].
- TTC29/ZMYND12 [PMID:37934199 "Thus, our data indicate that ZMYND12 interacts with DNAH1 and
  DNALI1, two established components of the axonemal IDA."].
- DNAH3 and DNAH12 are needed for DNAH1 in sperm [PMID:39503742; PMID:40146200]. DNAH2 loss in mice
  also removes DNAH1 from flagella [PMID:33968937 "Another IDA component, DNAH1, is also absent in
  the flagella of Dnah2Δ/Δ sperm"].

## Phenotypes
- Human MMAF / SPGF18 [PMID:24360805 "Five unrelated subjects out of 18 (28%) carried a homozygous
  variant in DNAH1"; PMID:27798045; PMID:34867808]. Patients mostly lack respiratory symptoms
  [PMID:24360805 "Although DNAH1 is also expressed in other ciliated cells, infertility was the only
  symptom of primary ciliary dyskinesia observed in affected subjects"].
- PCD (CILD37): one family, homozygous p.Lys1154Gln [PMID:25927852]. Treated as limited evidence.
- Mouse Mdhc7/Dnah1 KO: infertile, ~50% lower tracheal CBF, no gross axonemal defects
  [PMID:11371505 "The reduction in both ciliary and flagellar motility is not correlated with any
  gross defects in the axonemal structure."]. ENU ferf1 missense: abnormal motility and zona
  penetration failure [PMID:30734403].

## Curation decisions
- Core MF: minus-end-directed microtubule motor activity (IBA, intact motor domain). The NAS motor
  and axonemal dynein complex rows are modified to the more specific terms.
- Light intermediate chain binding is accepted for DNAH1 (DNALI1 partner). Intermediate chain
  binding is kept as non-core (seeded only by a Dictyostelium cytoplasmic dynein; no IC partner
  shown for DNAH1).
- Sperm axoneme assembly is kept as non-core: human loss disorganizes the axoneme, but mouse
  knockouts do not show that.

## PANTHER / IBA check
- Human DNAH1 and mouse Dnah1 (E9Q8T7) carry the same six IBA terms in QuickGO (GO:0008569,
  GO:0030286, GO:0030317, GO:0036126, GO:0045505, GO:0051959), so there is no ortholog
  family-split problem of the kind seen for DNAH12.
- PANTHER geneinfo places the protein in family PTHR10676 (the source of the IBAs), whereas the
  UniProt/InterPro cross-reference places it in PTHR22878 (each in a subfamily correctly named
  for this gene). This is the same two-route disagreement noted for DNAH12, but here it does not
  cost the gene any IBAs.
