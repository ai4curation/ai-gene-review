# rhgf-2 (T08H4.1; UniProt Q22354) - manual literature summary

No deep-research provider was available for this session; this file was written by hand
from the cached publications in `publications/` and a PubMed search
(`rhgf-2 OR (RHGF-2 AND elegans) OR T08H4.1`, two hits: PMID:22363657 and PMID:26188247).

## Identity and domain architecture

- RHGF-2 (T08H4.1, WBGene00006476) is a Dbl-family RhoGEF with tandem DH (Dbl homology /
  RhoGEF) and PH domains. UniProt Q22354 is an unreviewed TrEMBL entry (862 aa) with a DH
  domain at residues 131-323 (PROSITE PS50010) and PANTHER family PTHR13217 (PLEKHG5/PLEKHG7)
  subfamily SF11 (PLEKHG5) [file:worm/rhgf-2/rhgf-2-uniprot.txt].
- It is the worm ortholog of the PLEKHG5/Tech/Syx family [PMID:22363657 "RHGF-2
  exhibits significant identity to the mammalian RhoGEFs PLEKHG5/Tech/Syx"].
- It ends in a class I PDZ-binding motif (SDV); the UniProt sequence ends "...LETSDV".
- Lin et al. found a longer N-terminal isoform (RHGF-2l) by cDNA analysis, the WormBase
  T08H4.2 model being the 5' end; a short isoform (RHGF-2s) is sufficient for rescue
  [PMID:22363657 "smaller DNA fragments encoding only RHGF-2s (short isoform) were sufficient to rescue the developmental arrest and Dpy phenotypes in most rhgf-2(gk216) animals"].

## Biochemistry (Lin et al. 2012, PMID:22363657, full text)

- GEF activity specific to RHO-1 in vitro (immunoprecipitated FLAG-RHGF-2s from HEK293T,
  GST-GTPases, [35S]GTPgammaS loading) [PMID:22363657 "FLAG::RHGF-2 strongly stimulated the exchange of GDP for GTPγS35 on GST::RHO-1, but not on GST::CDC-42 or GST::CED-10."].
- Preferential binding to RHO-1 over CED-10 (Rac) and CDC-42, by GST pull-down and
  co-IP [PMID:22363657 "FLAG::RHGF-2 bound preferentially to GST::RHO-1 in comparison to binding with GST::CED-10 or GST::CDC-42."].
- Activates an SRE-luciferase reporter about 6-fold in HEK293T cells, used as a readout of
  RhoA activation [PMID:22363657 "we examined the ability of transiently expressed rhgf-2 to activate RhoA by monitoring SRE activation"].
- Binds MPZ-1 (MUPP1 ortholog) PDZ domain 8 (weaker to 9, 10) through its C-terminal SDV
  motif [PMID:22363657 "Only RHGF-2 containing the PDZ-binding motif bound to the MPZ-1 PDZ domains in a GST pull down experiment"].

## Genetics and expression

- rhgf-2(gk216) deletion: embryos arrest elongation at about the 1.5-fold stage and hatch
  as short immobile L1s [PMID:22363657 "Time-lapse video analysis revealed that rhgf-2(gk216) mutants arrested elongation early in the elongation process at the 1.5 fold stage of embryogenesis"].
  Seam cells fail to elongate. Rescued by genomic transgenes.
- Lin et al. saw rhgf-2s::gfp only in a subset of neurons from the 1.5-fold stage on, including
  nerve-ring axons where it co-localises with MPZ-1.
- Chan et al. 2015 (PMID:26188247, abstract only in cache) placed rhgf-2 genetically
  upstream of LET-502/ROCK in the RHO-1 elongation pathway, parallel to FEM-2/PP2c, and
  found that it is expressed throughout the embryo and that lateral-epidermis-specific
  expression can support elongation [PMID:26188247 "Genetically, rhgf-2 acts as an activator of let-502/Rho-binding kinase, in parallel to fem-2/PP2c phosphatase."].
  The rhgf-2; rga-2 double mutant is viable. Maternal RHGF-2 affects the rate of cleavage
  furrow ingression. So the elongation function is epidermal, which resolves the puzzle in
  Lin et al. of an apparently neuron-only expression.

## Gain-of-function observations (weak for GO process)

- RHGF-2 overexpression in mouse N1E-115 neuroblastoma cells causes rounding and blocks
  neurite outgrowth [PMID:22363657 "FLAG::RHGF-2 expression in N1E-115 cells induced cell rounding and inhibited neurite outgrowth to a similar extent as activated Gα12"].
- Overexpression in worms gives loopy locomotion. No loss-of-function locomotion phenotype
  could be scored because mutants arrest. The authors flag this as preliminary
  [PMID:22363657 "Additional analysis of RHGF-2 function in the nervous system is required to further define its role in the regulation of C. elegans locomotion."].
