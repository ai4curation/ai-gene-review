# Klf5 (rat, F1LSL7) - manual literature synthesis

No deep-research API was available for this session; this file was written by the reviewer
from cached publications (`publications/PMID_*.md`), PubMed metadata and the UniProt record.
Every statement carries its provenance.

## Identity and domain structure

- Rat Klf5 (RGD:621446, GeneID 84410) is represented by the unreviewed TrEMBL entry F1LSL7
  (443 aa, PE 4 "Predicted"). The protein carries three C-terminal C2H2 zinc fingers
  (FT DOMAIN 359..388, 389..418, 419..443, PROSITE PS50157) and is placed in PANTHER
  PTHR23235:SF82 "KRUEPPEL-LIKE FACTOR 5" [file:rat/Klf5/Klf5-uniprot.txt].
- KLF proteins "bind to consensus GC-rich or CACCC sequences through the three C-terminal
  zinc fingers" [PMID:18406357].
- Mouse orthologue: MGI:1338056; human orthologue: KLF5, UniProtKB Q13887 (the With/From
  sources of the ISO/IEA rows).

## Rat experimental data

### Vascular smooth muscle cells: p21 promoter (PMID:21383775, full text; 2024 expression of concern)
- "There are four tandem typical Klf5-binding sites (TCE) and two RARα-binding sites (RARE)
  in the promoter region of p21"; "mutation of TCE sites removed the inhibitory effect of
  Klf5, but not RARα"; ChIP and oligo pull-down show Klf5 binds the TCE region
  [PMID:21383775].
- "Klf5, RARα and HDAC2 form a repression complex to synergistically inhibit the expression
  of p21 under basal conditions"; RAR agonist Am80 triggers HDAC2-dependent Klf5
  deacetylation and dissociation from the promoter [PMID:21383775].
- The authors stress this repressive role is atypical: "many of the genes identified to date
  as direct targets of Klf5 are transactivated by Klf5" [PMID:21383775].
- Caveat: PubMed lists an "Expression of concern in Cell Res. 2024 Apr;34(4):331"
  [PMID:21383775]; conclusions should be weighted accordingly.

### Cardiac myocytes: endothelin-1 response (PMID:18406357, full text)
- In neonatal rat cardiac myocytes, "Klf5 mRNA was upregulated from 1 h, with maximal
  expression at 1.5 h (~13-fold relative to controls)"; the response requires new protein
  synthesis ("Klf5 is a second phase gene") and is inhibited by U0126 (ERK1/2)
  [PMID:18406357]. This is expression evidence only.

### Intestinal epithelial cells (PMID:14726538, abstract only)
- "expression of KLF5 (IKLF/BTEB2) is limited to proliferating crypt cells"; expression of KLF5
  in non-transformed rat ileal IEC-18 cells "enhances colony formation, cyclin D1
  transcription, and cell growth", whereas in colon cancer lines and Ras-transformed cells
  KLF5 reduced colony number [PMID:14726538]. Gain-of-function, context-dependent.

## Orthologue (mouse) data underlying ISO rows

- Klf5+/- mice: "showed diminished levels of arterial-wall thickening, angiogenesis, cardiac
  hypertrophy and interstitial fibrosis"; angiotensin II induces KLF5, "which in turn activated
  platelet-derived growth factor-A (PDGF-A) and transforming growth factor-beta (TGF-beta)
  expression"; KLF5 interacts with RAR [PMID:12101409, abstract].
- Adipogenesis: "KLF5, in turn, acts in concert with C/EBPbeta/delta to activate the
  PPARgamma2 promoter"; dominant-negative KLF5 inhibits and wild-type KLF5 induces
  adipocyte differentiation [PMID:16054042, abstract].
- Skeletal muscle: Klf5 "was induced in the nuclei of differentiating myoblasts and newly
  formed myofibers"; "Satellite cell-specific Klf5 deletion severely impaired muscle
  regeneration"; "Klf5 physically associates with both MyoD and Mef2" and "MyoD recruitment
  was greatly reduced in the absence of Klf5" [PMID:27743478, full text]. Little or no Klf5 is
  expressed in quiescent satellite cells, and Klf5 knockdown did not affect C2C12
  proliferation [PMID:27743478], which argues against a role in satellite-cell activation.

## Synthesis

Klf5 is a nuclear, sequence-specific (GC/CACCC, TCE) DNA-binding transcription factor that
mainly activates RNA polymerase II target genes (PDGF-A, TGF-beta, PPARgamma2, cyclin D1,
muscle genes), and can be recruited into co-repressor assemblies (RARalpha/HDAC2 at p21)
that repress specific targets. Its tissue roles (vascular remodeling, adipogenesis, muscle
regeneration, intestinal epithelium) are downstream consequences of this transcriptional
activity.
