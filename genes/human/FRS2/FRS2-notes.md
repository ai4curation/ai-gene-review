# FRS2 (Q8WU20) curation notes

## Identity
- FRS2 / FRS2alpha / SNT-1; 508 aa; N-myristoyl Gly2, IRS-type PTB domain (13-115), long disordered
  C-terminal tail with FGFR-phosphorylated tyrosines (Y196, Y306, Y349, Y392, Y436, Y471 by similarity
  to mouse Q8C180) (UniProt FRS2-uniprot.txt). Paralog FRS3 (FRS2beta/SNT-2, O43559); PANTHER
  PTHR21258:SF40 (DOK-related docking proteins).

## Core biology (with provenance)
- Discovery as lipid-anchored docking protein: [PMID:9182757 "FRS2 functions as a lipid-anchored docking
  protein that targets signaling molecules to the plasma membrane in response to FGF stimulation to link
  receptor activation with the MAPK and other signaling pathways essential for cell growth and
  differentiation"]; myristoylation needed [PMID:9182757 "We find that FRS2 is myristylated and that this
  modification is essential for membrane localization, tyrosine phosphorylation, Grb2/Sos recruitment, and
  MAPK activation"].
- Direct PTB-domain binding to FGFR1 juxtamembrane (non-pY motif): [PMID:9660748 "we show that FRS2/SNT-1
  and a newly isolated SNT-2 protein directly bind to FGF receptor-1 (FGFR-1)"]; constitutive for FGFR1 but
  activation-dependent for TrkA [PMID:10629055 "While FGFR1 interacts with FRS2 constitutively, independent
  of ligand stimulation and tyrosine phosphorylation, NGF receptor (TrkA) binding to FRS2 is strongly
  dependent on receptor activation"]; NMR structural basis [PMID:11090629 "The SNT-1 phosphotyrosine binding
  (PTB) domain recognizes activated TRKs at a canonical NPXpY motif and, atypically, binds to
  nonphosphorylated FGFRs in a region lacking tyrosine or asparagine"].
- Effector recruitment: SHP2 via N-SH2 [PMID:9632781 "we demonstrate that FRS2 forms a complex with the
  N-terminal SH2 domain of the protein tyrosine phosphatase Shp2 in response to FGF stimulation"]; GRB2
  direct and indirect [PMID:9632781 "These experiments demonstrate that FRS2 recruits Grb2 molecules both
  directly and indirectly via complex formation with Shp2"]; PI3K via GRB2-GAB1 [PMID:11353842 "we
  demonstrate that tyrosine phosphorylation of FRS2alpha leads to Grb2-mediated complex formation with the
  docking protein Gab1 and its tyrosine phosphorylation, resulting in the recruitment and activation of
  PI3-kinase"].
- Other RTKs: TrkA/Trk family (PTB binds NPXpY, competes with SHC) [PMID:10092678 "we demonstrate that the
  phosphotyrosine binding domain of FRS-2 directly binds the Trk receptors at the same phosphotyrosine
  residue that binds the signaling adapter Shc"], with functional rescue of NGF differentiation
  [PMID:10092678]; ALK [PMID:17274988 "Shc and FRS2 adaptors were recruited and phosphorylated following
  antibody-based ALK activation"]; EGFR in A-431 cells [PMID:12974390]; RET per UniProt "Binds RET (By
  similarity)" (not independently verified here - no RET paper cached).
- Negative feedback: [PMID:12974390 "activated ERK1/2 phosphorylates FRS2 on serine/threonine residues
  thereby down-regulating its tyrosine phosphorylation"].

## Localization
- Cytoplasmic face of the plasma membrane via myristoylation [PMID:9182757]. Reactome places FRS2 in cytosol
  for several TrkA/TrkB reactions - compartment modelling artefact, marked over-annotated.
- Adherens junction IDA from E-cadherin BioID (PMID:25468996) - high-throughput proximity; non-core.

## Decisions summary
- GO:0005068 (RTK adaptor) accepted as core MF; it is the right term for FRS2 in the FGFR module and also
  covers Trk/ALK/RET/EGFR use since the term is not FGFR-specific.
- GO:0005515 protein binding rows MODIFIED to FGFR binding (FGFR1 partners), SH2 domain binding
  (Hadari 1998 SHP2 N-SH2), protein phosphatase binding (LuTHy PTPN11).
- TAS from PMID:9660748 for GPCR signaling (GO:0007186) and receptor PTP signaling (GO:0007185) removed:
  unsupported by paper; SHP2 is a non-receptor PTP. Phosphatase activator activity marked over-annotated.
- Considered NEW GO:0048011 neurotrophin TRK receptor signaling pathway (participation evidence from
  Meakin 1999 rescue). Comparator check (QuickGO 2026-09-30): SHC1 (P29353), FRS3 and mouse Frs2 carry no
  GO:0048011/GO:0038180 annotation, so not proposed; raised as a suggested question instead.
