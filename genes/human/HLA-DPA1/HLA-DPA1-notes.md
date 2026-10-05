# HLA-DPA1 curation notes

UniProt: P20036 (HLA class II histocompatibility antigen, DP alpha 1 chain).
Gene: HLA-DPA1 (HGNC), MHC class II region, chromosome 6p21.

## Deep research status

`just deep-research-falcon human HLA-DPA1` was launched in the background at the
start of this session. The Edison/falcon API returned repeated `429 Too Many
Requests` on task creation and no `HLA-DPA1-deep-research-falcon.md` was produced
within the session window; no perplexity key is configured, so no fallback
provider was available. Literature evidence below was therefore assembled from
the cached `publications/PMID_*.md` records, the UniProt record, PubMed (MCP),
QuickGO and OLS. No file was written under a `-deep-research-<provider>.md` name.

## What the protein is

HLA-DPA1 encodes the alpha chain of the HLA-DP class II molecule. It is a
single-pass type I membrane glycoprotein with an N-terminal alpha-1 domain
(one half of the peptide-binding groove) and a C1-set immunoglobulin-like
alpha-2 domain. It is obligately heterodimeric with a DP beta chain
(HLA-DPB1); the alpha-1 and beta-1 domains together form the peptide-binding
cleft.

- [file:human/HLA-DPA1/HLA-DPA1-uniprot.txt, "Binds peptides derived from antigens that access the
  endocytic route of antigen presenting cells (APC) and presents them on
  the cell surface for recognition by the CD4 T-cells."]
- [file:human/HLA-DPA1/HLA-DPA1-uniprot.txt, "Heterodimer of an alpha and a beta subunit; also referred as
  MHC class II molecule."]
- [file:human/HLA-DPA1/HLA-DPA1-uniprot.txt, "In the endoplasmic reticulum (ER) it forms a
  heterononamer; 3 MHC class II molecules bind to a CD74 homotrimer"]
- InterPro/Pfam: MHC_II_alpha (PF00993), C1-set (PF07654); PANTHER PTHR19944
  (MHC CLASS II-RELATED), subfamily SF64.

## Structural evidence that the alpha chain builds the peptide groove

The first HLA-DP structure, DP2 = DPA1\*01:03 / DPB1\*02:01, establishes directly
that the DP alpha chain contributes half of the antigen-binding groove and
constrains peptide side-chain pockets:

- [PMID:20356827 "Crystal structure of HLA-DP2 and implications for chronic beryllium disease.",
  "The α1 and β1 domains of DP2 form the peptide-binding groove, and the peptide takes an
  extended polyproline-like helical course through the groove."]
- [PMID:20356827, "its depth is due to the amino acids αAla11 and βGly11, whose small side
  chains open up the bottom of the pocket"] — an alpha-chain residue directly shapes the p6
  pocket, i.e. the alpha chain determines peptide-binding specificity, not just scaffolding.
- [PMID:20356827, "βAsp55 (corresponding to position 57 in most other MHCII β-chains) ( 28 ) is
  a strongly conserved residue among both human and mouse MHCII molecules, forming a conserved
  salt bridge across to αArg76 that is important in the formation of the antigen-binding cleft"]
- The crystallised molecule is a DP alpha/DP beta heterodimer with a bound self-peptide
  derived from the HLA-DR alpha chain: [PMID:20356827, "we crystallized DP2 ( DPA1*0103 ,
  DPB1*0201 ) with a bound self-peptide derived from the HLA-DR α-chain (pDRA) ( 26 ) and
  solved its structure to a resolution of 3.25 Å."]

Functional readout in the same paper: DP2-expressing fibroblasts present beryllium to a
patient-derived CD4 T-cell line, driving IFN-gamma production and proliferation; the
transfection host already expressed the DP alpha chain:

- [PMID:20356827, "Transfection into mouse DAP.3 L cells expressing DPA1*0103 was performed
  using Lipofectamine 2000"]
- [PMID:20356827, "16% of the T cells responded with production of IFN-γ versus only 0.2% when
  using unpulsed fibroblasts"]
- [PMID:20356827, "Similar findings were seen when Be-induced proliferation was used as a
  measure of T-cell response ( Fig. 4 C )"]
- Surface expression of the assembled DP alpha/beta molecule was confirmed with a
  conformation-dependent antibody: [PMID:20356827, "Fibroblasts transfected with each of the
  mutant DP2 molecules expressed DP2 equally well on the cell surface, as detected by staining
  with a conformation-dependent anti-DP mAb, B7.21"]

The later TCR co-complex structure (PMID:24995984, Clayton et al. 2014) shows the assembled
DP2/peptide/Be2+ complex engaged by an alphabeta TCR, with the TCR footprint spanning the
peptide and both chain helices:

- [PMID:24995984 "Structural basis of chronic beryllium disease: linking allergic
  hypersensitivity and autoimmunity.", "resulting in extensive contact with the entire
  length of the M2 peptide and DP2 beta chain helix, at the expense of the DP2 alpha chain
  helix"]
- [PMID:24995984, "Despite this tilted conformation, the footprint of the AV22 TCR on DP2-M2
  involves 280 atom-to-atom contacts (Table 1) and covers 1288 Å2, well within the range
  typically seen for CD4 T cell TCR contact with MHC-peptide ligands."]
- [PMID:24995984, "In the absence of Be2+ the unmutated DP2-M2 complex failed to bind the TCR"]

Note on reading these two papers for GO purposes: both mutational experiments target the
DP **beta** chain (betaGlu26/68/69); the DP alpha chain is the invariant partner supplying
the other half of the groove. So the GOA IMP/IDA rows on HLA-DPA1 from PMID:20356827 record
the alpha chain's participation as a component of the functional DP2 heterodimer rather than
allele-specific alpha-chain effects.

## Alpha/beta chain pairing

The DP alpha chain's conformation and surface epitopes depend on which polymorphic DP beta
chain it pairs with — direct evidence that the two chains form an obligate heterodimer
displayed at the cell surface:

- [PMID:2461352 "Epitope recognition by a DP alpha chain-specific monoclonal antibody
  (DP11.1) is influenced by the interaction between the DP alpha chain and its polymorphic
  DP beta chain partner.", "The HLA-DP alpha chain-specific monoclonal antibody DP11.1 binds
  only to the surfaces of cells types as DPw2 or DPw4 by primed lymphocyte typing."]
- [PMID:2461352, "Therefore the binding of antibody DP11.1 to its alpha chain
  epitope is influenced by the associations between the DP alpha chain and its
  polymorphic DP beta chain partner."]

This paper is cell-surface antibody staining and sequence comparison; it is the source of
three NAS rows in GOA (plasma membrane, immune response, MHC class II receptor activity).
Its abstract supports surface localisation of the DP alpha chain but says nothing about
receptor activity.

## Transcriptional regulation / IFN-gamma

The IDA row for `GO:0071346 cellular response to type II interferon` traces to a paper about
a repressor of the DPA promoter, not about the DP alpha protein responding to IFN-gamma:

- [PMID:8568247 "A zinc finger protein that represses transcription of the human MHC class II
  gene, DPA.", "Overexpression of XBR in a B cell line resulted in a dramatic reduction of
  transcription from a reporter gene construct driven by the DPA promoter, but not from
  similar constructs with mutations in the X2 box."]
- [PMID:8568247, "Similarly, overexpression of XBR reduced induction of
  reporter gene activity driven from the DPA promoter in HeLa cells treated with
  IFN-gamma."]

So the DPA promoter is IFN-gamma-inducible — the gene is a *target* of IFN-gamma signalling.
GO annotation practice treats "cellular response to X" as the responding cell's process and
MHC class II genes are canonical IFN-gamma/CIITA-induced genes, so the row is defensible, but
the protein is the output of the response and not a transducer of it; it is not a core
molecular function of the DP alpha chain. Kept as non-core.

## Interactome rows (SREBF2)

Three IPI `GO:0005515 protein binding` rows cite high-throughput AP-MS/image-fusion studies,
all with partner UniProtKB:Q12772 (SREBF2):

- [PMID:28514442 "Architecture of the human interactome defines protein communities and
  disease networks.", "To address challenges of scale in high-throughput AP-MS, we have
  established a robust AP-MS pipeline capable of targeting up to 500 human open reading
  frames (ORF's) per month4"]
- [PMID:33961781 "Dual proteome-scale networks reveal cell-specific remodeling of the human
  interactome.", "immunoprecipitations in HCT116 cells."]
- [PMID:34819669 "A multi-scale map of cell structure fusing protein images and
  interactions.", "Here we integrate immunofluorescence images in \nthe Human Protein Atlas4
  with affinity purifications in BioPlex5 to create a \nunified hierarchical map of human
  cell architecture."]

UniProt also records this single interaction:
[file:human/HLA-DPA1/HLA-DPA1-uniprot.txt, "P20036; Q12772: SREBF2; NbExp=3; IntAct=EBI-2802853, EBI-465059;"]

No mechanism, directionality, or biological consequence has been reported for a
HLA-DPA1/SREBF2 association, and SREBF2 is an ER/nuclear sterol-regulated transcription
factor with no described role in class II antigen presentation. Per repository curation
policy, generic `protein binding` is removed as uninformative (which does not assert the
interaction is false) unless a more informative MF is supported; nothing here supports one.

## Subcellular itinerary

UniProt records the full trafficking itinerary of the assembled complex, which is what
the long list of Reactome TAS component rows (ER, ER-to-Golgi vesicle, Golgi/TGN membrane,
endocytic and clathrin-coated vesicle membrane, endosome, lysosome, plasma membrane) also
describes:

- [file:human/HLA-DPA1/HLA-DPA1-uniprot.txt, "Cell membrane; Single-pass type I membrane
  protein. Endoplasmic reticulum membrane; Single-pass type I membrane protein. Golgi
  apparatus, trans-Golgi network membrane; Single-pass type I membrane protein. Endosome
  membrane; Single-pass type I membrane protein. Lysosome membrane; Single-pass type I
  membrane protein."]
- [file:human/HLA-DPA1/HLA-DPA1-uniprot.txt, "The MHC class II complex transits through a number of
  intracellular compartments in the endocytic pathway until it reaches
  the cell membrane for antigen presentation."]

The destination of function is the cell surface (presentation to CD4 T cells) and the
MIIC/late endosome-lysosome (peptide loading). The intermediate biosynthetic compartments
are transit stops and were kept as non-core.

## Consistency with other class II reviews in this repo

No other HLA class II alpha/beta chain gene (HLA-DRA, HLA-DRB1, HLA-DPB1, HLA-DQA1) has a
review directory in `genes/human/` yet, so there was no sibling review to align with. The
nearest reviewed relatives are the T-cell-side partners: `genes/human/CD4` (which uses
`GO:0023026 MHC class II protein complex binding` as a core MF and MODIFYs generic
`protein binding` IPI rows to it) and the CD3 chains. The convention followed here:

- `GO:0032395 MHC class II receptor activity` has an explicit GO comment restricting it to
  the *receptor for* class II, i.e. CD4-side molecules, not class II subunits themselves
  (OLS: "Note that this term is intended for annotation of gene products that act as
  receptors for MHC class II protein complexes, not for components of the MHC class II
  protein complexes themselves."). The NAS row on HLA-DPA1 therefore inverts the term and
  is removed; the right MF for the DP alpha chain is `GO:0042605 peptide antigen binding`
  (which OLS notes "can be used to describe the binding of a peptide to an MHC molecule")
  plus `part_of GO:0042613 MHC class II protein complex`.
- `GO:0023026 MHC class II protein complex binding` (IBA) describes binding *to* a class II
  complex. For a DP alpha chain the partner complex is the one it is itself part of, so the
  term is inverted the same way as GO:0032395. The IBA node PTN000460629 mixes class II
  subunits with class II *binders*; QuickGO shows the identical IBA row with donors
  P06340 (HLA-DOA), P13765 (HLA-DOB), P28067 (HLA-DMA), P28068 (HLA-DMB) — i.e. DM/DO, which
  genuinely bind class II alpha-beta-CLIP complexes in trans. The DP alpha chain does not.
  Flagged as over-annotated rather than removed, since the node placement is a defensible
  family-level call and DP alpha does contact class II molecules within the heterononamer.
- `GO:0002503 peptide antigen assembly with MHC class II protein complex` IBA is accepted:
  this is the loading of peptide into the groove, half of which the alpha chain builds.

## Comparator check for proposed NEW terms

Considered and rejected: `GO:0042608 T cell receptor binding`. HLA-DRA (P01903) and HLA-DRB1
(P01911) both carry GO:0042608 by IDA in QuickGO, so the term is in use for class II chains,
and PMID:24995984 shows an AV22 TCR engaging DP2. But the same paper states the tilted TCR
footprint is made "at the expense of the DP2 alpha chain helix", i.e. the published
DP-specific structure is the one case where the alpha-chain contribution to the TCR interface
is minimised, and no DP-alpha-specific TCR-binding measurement exists. Asserting a new MF
on the weakest available structural footing is not warranted; raised as a
`suggested_questions` entry instead.

Also considered: `GO:0009897 external side of plasma membrane` (HLA-DRB1 carries it by IDA).
PMID:2461352 is cell-surface antibody staining of the DP alpha chain, which would support it,
but the existing `GO:0005886 plasma membrane` and `GO:0009986 cell surface` rows already
cover the location at the granularity the evidence supports; adding a third overlapping
component term is redundancy, not coverage.
