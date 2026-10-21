# EPCAM (P16422) — curation notes

Deep-research providers are unavailable in this environment; research below is from the
cached publications, the UniProt record and PubMed.

## Protein and localization

EpCAM is a single-pass type I membrane glycoprotein of epithelia, with an extracellular
EpEX domain, a transmembrane helix and a short cytoplasmic EpICD. UniProt gives the
lateral cell membrane as the curated location, with tight junction as a second site.
[file:human/EPCAM/EPCAM-uniprot.txt "SUBCELLULAR LOCATION: Lateral cell membrane"]
[file:human/EPCAM/EPCAM-uniprot.txt "Note=Colocalizes with CLDN7 at the lateral cell membrane and tight junction."]
In kidney, immunohistochemistry detects it in both basolateral and apical membranes of
tubular epithelium and in the ureteric bud throughout nephrogenesis
[PMID:18025791 "EpCAM expression was found in the ureteric bud throughout nephrogenesis"].
It is a classic cell-surface marker of undifferentiated hESC
[PMID:19785009 "we have identified the antigen target of one such monoclonal antibody as the epithelial cell adhesion molecule (EpCAM)"].

Localization conclusion: plasma membrane, concentrated at the lateral membrane and tight
junctions, with the EpEX ectodomain extracellular and antibody-accessible. The shed EpEX
accounts for the extracellular-region row.

## Functions

- Calcium-independent homophilic epithelial adhesion that *weakens* cadherin-mediated
  adhesion.
  [PMID:9382878 "Ep-CAM-positive transfectants behave like cells with a decreased strength of cell-cell adhesion as compared to the parental cells"]
- Regulated intramembrane proteolysis: TACE and presenilin-2 release EpEX and EpICD;
  EpICD enters the nucleus with FHL2, beta-catenin and Lef-1 and drives transcription,
  including MYC and FABP5.
  [PMID:19136966 "regulated intramembrane proteolysis activates EpCAM as a mitogenic signal transducer in vitro and in vivo"]
- Proliferation and stem-cell maintenance; EpCAM knockdown in hESC reduces proliferation
  [PMID:19785009 "cell proliferation was decreased by >40%"].
- Interacts with phosphorylated claudin-7 at the lateral membrane and tight junction
  [file:human/EPCAM/EPCAM-uniprot.txt "Interacts with phosphorylated CLDN7."]

## Protein-binding rows

CLDN7 (PMID:16054130) is modified to cell adhesion molecule binding, since GO has no
claudin-binding term. CDH1 from the neurodegeneration interactome screen is modified to
cadherin binding; CALR, DLST, CDK5R1 and NEK7 from the same high-throughput screen are
removed as uninformative.

The IBA row `GO:0098641 cadherin binding involved in cell-cell adhesion` overstates the
mechanism: EpCAM's own adhesive activity is homophilic and calcium-independent, and its
documented effect on cadherin adhesion is to reduce it. Modified to
`GO:0098632 cell-cell adhesion mediator activity`.
