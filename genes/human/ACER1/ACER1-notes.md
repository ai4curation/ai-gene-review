# ACER1 (Alkaline ceramidase 1) — review notes

UniProt: Q8TDN7 (ACER1_HUMAN). Gene: ACER1 (HGNC:18356), synonym ASAH3. Chromosome 19.
264 aa, 6-TM (multi-pass) endoplasmic-reticulum membrane protein.

## Core biology (from UniProt Q8TDN7 = file:human/ACER1/ACER1-uniprot.txt)

- **Molecular function**: alkaline ceramidase; hydrolyses ceramide to sphingosine + free
  fatty acid at alkaline pH.
  - `DE   RecName: Full=Alkaline ceramidase 1`; `EC=3.5.1.23`
  - FUNCTION: "Endoplasmic reticulum ceramidase that catalyzes the hydrolysis of ceramides
    into sphingosine and free fatty acids at alkaline pH (PubMed:17713573, PubMed:20207939,
    PubMed:20628055)."
  - Catalytic activity (RHEA:20856, EC 3.5.1.23): "an N-acylsphing-4-enine + H2O =
    sphing-4-enine + a fatty acid". Maps exactly onto GO:0017040 "N-acylsphingosine
    amidohydrolase activity" (verified via OLS: definition "an N-acylsphing-4-enine + H2O =
    a fatty acid + sphing-4-enine"). There is **no** distinct "alkaline ceramidase activity"
    GO term — GO:0017040 is the single ceramidase MF term.
- **Substrate preference**: "has a higher activity towards very long-chain unsaturated fatty
  acids like the C24:1-ceramide"; "strong substrate specificity towards the natural
  stereoisomer of ceramides with D-erythro-sphingosine as a backbone". Reactome R-HSA-428231:
  "ACER1 hydrolyses C20:0-C24:0 ceramides". May also hydrolyse dihydroceramides to
  dihydrosphingosine.
- **Location**: "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane
  {ECO:0000269|PubMed:17713573}; Multi-pass membrane protein". 6 TRANSMEM segments annotated.
  GO:0005789 (ER membrane, EXP/PMID:17713573) is the precise CC; GO:0005783 (ER, IDA) is the
  parent.
- **Cofactor / metal**: catalytic Zn(2+) (BINDING 77, 206, 210, by similarity to Q9NUN7);
  Ca(2+) binding (residues 13,14,16,18,27) and Ca(2+)-dependent activity
  (PubMed:17713573). Supports GO:0046872 metal ion binding (IEA-KW) and
  GO:0071277 cellular response to calcium ion (IDA).
- **Pathway**: "Lipid metabolism; sphingolipid metabolism." (UPA00222).
- **Tissue specificity**: "Mainly expressed in epidermis." HPA: "Tissue enriched (skin)".
  PMID:16477081: "alkaline CDase-1 occurs almost exclusively in epidermis".

## Physiological role (skin / keratinocytes)

- PMID:17713573 (J Invest Dermatol; abstract only): extracellular Ca2+ "markedly upregulates
  the human alkaline ceramidase 1 (haCER1) in HEKs; and its upregulation mediates the
  Ca2+(o)-induced growth arrest and differentiation of HEKs." "haCER1 catalyzed the
  hydrolysis of very long-chain ceramides to generate sphingosine (SPH). This in vitro
  activity required Ca2+." Ectopic haCER1 lowered C24:1/C24:0-ceramide and raised SPH + S1P;
  knockdown did the opposite and blocked Ca2+-induced keratin 1 / involucrin expression and
  growth arrest. Down-regulated by EGF (UniProt INDUCTION).
  → supports GO:0071277 (cellular response to Ca2+), GO:0010446 (response to alkaline pH,
  optimum pH 8.0), GO:0030154 / GO:0030216 (keratinocyte differentiation), sphingosine
  biosynthesis, ceramide catabolism.
- PMID:16477081 (J Lipid Res; abstract only): expression/activity of CDase isoforms in
  keratinocytes/epidermis is differentiation-associated; alkaline CDase-1 is epidermis-
  restricted. IEP-level (expression correlated with epidermis development / keratinocyte
  differentiation). Non-core: expression correlation, not a demonstrated developmental
  mechanism.
- PMID:20207939 (FASEB J; abstract only): alkaline ceramidase activity in erythrocytes
  generates SPH (the S1P precursor). This paper is about the ACER family activity in
  erythrocytes; ACER1 itself is skin-restricted, so the erythrocyte data is largely ACER2/3.
  The IMP annotations transferred to ACER1 (GO:0017040, GO:0046512, GO:0046514) are
  supported by the family activity and the enzyme's demonstrated ceramidase function —
  keep, but the erythrocyte biology is not ACER1's core context.
- PMID:20628055 (J Biol Chem; abstract only): primarily about ACER2 and dihydroceramide →
  dihydrosphingosine in tumour cells. Cited by UniProt for ACER1 catalytic activity on
  N-acylsphinganine / oleoyl substrates (RHEA:33551, RHEA:41299). IDA annotations for
  GO:0017040 and GO:0046512 on ACER1 traced to this reference are supported by the in-vitro
  substrate assays reported for the ACER enzymes; retained.

## Protein interaction

- PMID:32296183 (Luck et al., HuRI, "A reference map of the human binary protein
  interactome"): large-scale Y2H. UniProt INTERACTION records ACER1 (Q8TDN7)–MPP1 (Q00013),
  NbExp=3. This is a bare `protein binding` (GO:0005515) IPI from a proteome-scale screen; no
  established biological function for ACER1. Per policy: MARK_AS_OVER_ANNOTATED (do not
  REMOVE an IPI), do not promote to core. The abstract does not name ACER1/MPP1 (they are in
  supplementary data), so no verbatim supporting_text is quoted.

## Annotation-review summary

- **Core MF**: GO:0017040 N-acylsphingosine amidohydrolase activity (= ceramidase / alkaline
  ceramidase; EC 3.5.1.23).
- **Core CC**: GO:0005789 endoplasmic reticulum membrane (integral, multi-pass).
- **Core BP**: GO:0046514 ceramide catabolic process; GO:0046512 sphingosine biosynthetic
  process (the two direct outputs of the ceramidase reaction).
- **Non-core / supporting BP**: sphingolipid metabolic/catabolic/biosynthetic process
  (parents); cellular response to calcium ion; response to alkaline pH; keratinocyte
  differentiation / cell differentiation / epidermis development (physiological context in
  skin).
- **Over-annotations**: GO:0005515 protein binding (bare IPI, MPP1, screen-only);
  GO:0048733 sebaceous gland development (IEA from mouse ortholog, weak/indirect);
  GO:0016020 membrane (uninformative parent of ER membrane).
- **Verified GO term ids via OLS**: GO:0017040, GO:0046512, GO:0046514, GO:0005789,
  GO:0071277, GO:0010446, GO:0030148, GO:0048733 — all current, non-obsolete.
