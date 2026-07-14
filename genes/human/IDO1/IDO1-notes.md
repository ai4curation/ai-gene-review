# IDO1 (human) — gene review notes

UniProt: **P14902** (I23O1_HUMAN); HGNC:6059; gene symbol **IDO1** (synonyms IDO, INDO).
403 aa; EC **1.13.11.52**. Evidence: protein level (PE 1).

## Identity and core function

IDO1 is **indoleamine 2,3-dioxygenase 1**, a heme-dependent dioxygenase catalysing the
**first and rate-limiting step of tryptophan catabolism along the kynurenine pathway**:
oxidation of L-tryptophan (and other indoleamines) with O2 to N-formyl-L-kynurenine.

- "Catalyzes the first and rate limiting step of the catabolism of the essential amino acid
  tryptophan along the kynurenine pathway" [file:human/IDO1/IDO1-uniprot.txt, FUNCTION,
  ECO:0000269|PubMed:17671174, PubMed:18026683].
- Two catalytic-activity reactions are recorded in UniProt: `L-tryptophan + O2 = N-formyl-L-kynurenine`
  (Rhea:24536; ECO:0000269|PubMed:17671174, PubMed:18026683) and `D-tryptophan + O2 =
  N-formyl-D-kynurenine` (Rhea:14189; PubMed:18026683). EC=1.13.11.52 for both.
- Km 21.23 uM for L-Trp vs 4.6 mM for D-Trp; "Catalytic efficiency for L-tryptophan is 150 times
  higher than for D-tryptophan" [file:human/IDO1/IDO1-uniprot.txt, BIOPHYSICOCHEMICAL PROPERTIES,
  PubMed:18026683]. So L-Trp is the physiological substrate.
- Pathway: "Amino-acid degradation; L-tryptophan degradation via kynurenine pathway; L-kynurenine
  from L-tryptophan: step 1/2" [file:human/IDO1/IDO1-uniprot.txt, PATHWAY].

Distinct from TDO2: IDO1 and TDO2 catalyse the same first step but IDO1 is the broadly
**IFN-gamma-inducible, immunoregulatory** enzyme with broad indoleamine substrate specificity.

## Cofactor / metal

- Heme b, one per subunit; "In the active form, the heme iron is in its ferrous state Fe(+2)"
  [file:human/IDO1/IDO1-uniprot.txt, COFACTOR, PubMed:16477023, PubMed:16574111, PubMed:25313323].
- Proximal heme-iron binding residue His346 [file:human/IDO1/IDO1-uniprot.txt, BINDING 346].
- Crystal structures with heme confirm a heme-containing dioxygenase fold (2D0T etc.;
  PubMed:16477023 "Crystal structure of human indoleamine 2,3-dioxygenase: catalytic mechanism of
  O2 incorporation by a heme-containing dioxygenase").
- So `heme binding` (GO:0020037) and `metal ion binding` (GO:0046872, the iron) are correct MFs.

## Subcellular location

Cytoplasm, cytosol [file:human/IDO1/IDO1-uniprot.txt, SUBCELLULAR LOCATION]. Reactome R-HSA-198563
also describes "Cytosolic indoleamine 2,3-dioxygenase". So cytosol/cytoplasm CC annotations are
correct.

## Immunoregulation (genuine biological roles; not the primary MF)

- "Involved in the peripheral immune tolerance, contributing to maintain homeostasis by preventing
  autoimmunity or immunopathology" [file:human/IDO1/IDO1-uniprot.txt, FUNCTION, PubMed:25691885].
- "Tryptophan shortage inhibits T lymphocytes division and accumulation of tryptophan catabolites
  induces T-cell apoptosis and differentiation of regulatory T-cells" [file:human/IDO1/IDO1-uniprot.txt,
  FUNCTION, PubMed:25691885].
- "Acts as a suppressor of anti-tumor immunity" [file:human/IDO1/IDO1-uniprot.txt, FUNCTION,
  PubMed:14502282, PubMed:23103127, PubMed:25157255, PubMed:25691885].
- "Protects the fetus from maternal immune rejection" [file:human/IDO1/IDO1-uniprot.txt, FUNCTION,
  PubMed:25691885].
- Induction: "By IFNG/IFN-gamma in most cells" [file:human/IDO1/IDO1-uniprot.txt, INDUCTION,
  PubMed:1907934, PubMed:2109605].

These immune roles are the reason IDO1 (vs TDO2) is important, but the primary molecular function
is the enzymatic activity; downstream T-cell/immune effects are consequences of tryptophan depletion
and kynurenine production. Treated as KEEP_AS_NON_CORE.

## Per-reference notes on cited annotation sources

- **PMID:18026683** (Yuasa 2007, "Evolution of vertebrate IDOs"). Abstract-only. Enzymatically
  characterised mammalian IDOs (incl. human) with recombinant protein; established IDO/proto-IDO
  activity and Km differences. Source of EC=1.13.11.52 and the L-/D-Trp kinetics in UniProt.
  Supports GO:0033754 (indoleamine 2,3-dioxygenase activity) EXP. NB: the L-tryptophan
  2,3-dioxygenase activity (GO:0004833) EXP annotation reflects the same shared reaction chemistry;
  the IDO-specific term GO:0033754 is preferable.
- **PMID:2109605** (Dai & Gupta 1990). Abstract-only. cDNA cloning of human IFN-gamma-inducible
  IDO; showed transfection "led to constitutive expression of C42 specific RNA as well as IDO
  activity." Establishes tryptophan-degrading (kynurenine pathway) function and IFN-gamma
  inducibility. Does NOT establish electron transfer activity — the GO:0009055 electron transfer
  activity TAS from this paper is an over-annotation (IDO1 is a heme dioxygenase, not an electron
  carrier; the abstract only mentions IDO activity and Trp degradation).
- **PMID:25310899** (Demmers 2015). Abstract-only. Human renal tubular epithelial cells; IDO
  functionally implicated via the inhibitor 1-methyl-L-tryptophan (1-L-MT) in suppressing
  alloreactive T-cell proliferation and enhancing T-cell apoptosis. "inhibition of proliferation
  and enhancement of apoptosis of T cell subsets is differentially regulated by indoleamine
  2,3-dioxygenase and ICAM-1". Note: 1-L-MT only "partially restored or failed to restore"
  proliferation — consistent with the GOA NOT annotation for GO:0046006 (regulation of activated
  T cell proliferation), i.e. IDO not the driver of the proliferation effect in this system,
  whereas T-cell apoptosis (GO:0070234) was affected by 1-L-MT. IMP annotations here rest on
  full text the curator read; keep.
- **PMID:9712583** (Munn 1998, Science). Abstract-only. Classic maternal-fetal tolerance study:
  pharmacologic IDO inhibition caused T cell-induced rejection of allogeneic concepti in mice;
  "by catabolizing tryptophan, the mammalian conceptus suppresses T cell activity and defends
  itself against rejection." Supports female pregnancy / maternal-fetal tolerance role (mouse
  model; TAS to human via ortholog). KEEP_AS_NON_CORE.
- **Reactome:R-HSA-198563** "IDO1 dioxygenates L-Trp to NFK" — cytosolic localisation, TAS; correct.

## Curation summary

Core MF: **GO:0033754 indoleamine 2,3-dioxygenase activity** (EC 1.13.11.52) + **GO:0020037 heme
binding** + iron (**GO:0046872 metal ion binding**). Core BP: **GO:0006569 L-tryptophan catabolic
process** (kynurenine pathway, step 1). Location: cytosol/cytoplasm.

- GO:0004833 (L-tryptophan 2,3-dioxygenase activity) annotations → MODIFY to GO:0033754 (the
  IDO-specific term; GO:0004833 is properly the TDO term).
- GO:0009055 electron transfer activity (TAS) → MARK_AS_OVER_ANNOTATED (heme dioxygenase, not an
  electron carrier; source paper is a cloning paper).
- GO:0034354 'de novo' NAD+ biosynthetic process from L-tryptophan (IBA) → KEEP_AS_NON_CORE /
  over-annotation: IDO1 only performs the first committed step, not the full de novo NAD+ pathway.
- Immune annotations (GO:0070234 pos reg T cell apoptosis IMP; NOT GO:0046006; GO:0007565 female
  pregnancy TAS) → KEEP_AS_NON_CORE (genuine downstream immunoregulatory consequences).
