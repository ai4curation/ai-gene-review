# Klf2 (rat, Q9ET58) - manual literature synthesis

No deep-research API was available; this synthesis was compiled by hand from cached
publications (publications/PMID_*.md), PubMed metadata and the UniProt record.

## Identity and domain architecture
- Krueppel-like factor 2 (LKLF), 351 aa, Swiss-Prot Q9ET58, RGD:1359220, GeneID 306330.
- Three C-terminal C2H2 zinc fingers (FT ZN_FING 268-292, 298-322, 328-350; Pfam PF00096 x3,
  PROSITE PS00028/PS50157) form the DNA-binding domain; N-terminal disordered transactivation
  region with a 9aaTAD motif (42-50); WWP1-interaction region 110-264 (UniProt, by similarity).
- UniProt function (by similarity to human KLF2 Q9Y5W3): "Transcription factor that binds to the
  CACCC box in the promoter of target genes such as HBB/beta globin or NOV and activates their
  transcription." [Klf2-uniprot.txt]

## Rat experimental literature
- Wick et al. 2005 [PMID:15540987] (full text): a yeast one-hybrid screen of a rat lung cDNA
  library with the proximal rat cPLA2 (Pla2g4a) promoter repeatedly isolated LKLF; GST-LKLF bound a
  GC-rich element at -37/-30 by EMSA; overexpression activated the promoter (RL-65 rat lung
  epithelial cells and Sp1-free Drosophila SL-2 cells); a DNA-binding-domain-only dominant-negative
  and stable siRNA against LKLF in RL-65 cells reduced basal cPLA2 expression and blocked
  H-Ras induction [PMID:15540987 "LKLF bound to a GC-rich region of the cPLA2 promoter located
  between -37 and -30 upstream from the transcription start site"]. LKLF was also an ERK substrate
  in vitro.
- Cullingford et al. 2008 [PMID:18406357] (full text): neonatal rat cardiac myocytes; endothelin-1
  increased Klf2 mRNA ~9-fold within 15-30 min as an immediate-early gene (cycloheximide
  insensitive, partly U0126 sensitive); H2O2 induced Klf2 (~3.6-fold, ERK-dependent); IL-1beta
  and TNFalpha downregulated Klf2 [PMID:18406357 "IL-1β or TNFα profoundly and rapidly (from ∼ 1 h)
  downregulated Klf2 mRNA expression"]. All are mRNA expression measurements.
- Clerk et al. 2009 [PMID:19192484] (abstract text not in cache; title only): "negative feedback
  regulation of interleukin 6 by Atf3 and Klf2" in endothelin-1-stimulated cardiac myocytes.
- Wang et al. 2006 [PMID:16466697] (abstract): pulsatile forward flow sustains KLF2 expression in
  endothelial cells while oscillatory flow suppresses it; flow-associated KLF2 patterns also in a
  rat aortic restenosis model; KLF2 siRNA sensitized ECs to oxLDL-induced apoptosis.

## Orthologue literature (mouse/human)
- Mouse Klf2-/- embryos die E12.5-14.5 of hemorrhage with defective tunica media / vessel
  stabilization; angiogenesis and vasculogenesis normal [PMID:9367982].
- Klf2 is required for primitive erythropoiesis and embryonic beta-like globin (Ey, beta-h1)
  expression [PMID:15947087].
- Klf2-null ES-cell chimeras show defective late lung development [PMID:10409672].
- KLF2 licenses T-cell egress: binds and transactivates the S1pr1 promoter [PMID:16855590].
- Endothelium: KLF2 is the transcription factor most specifically induced by prolonged laminar
  flow [PMID:12176889]; it induces eNOS (NOS3) and represses cytokine-induced VCAM1/E-selectin,
  partly by competing for CBP/p300 [PMID:15136591].
- KLF2 binds the VEGFA promoter and represses it (uric-acid / miR-92a angiogenesis study)
  [PMID:26299712]; this is the source of the human "cellular stress response to acid chemical",
  "negative regulation of sprouting angiogenesis" and "negative regulation of transcription by
  RNA polymerase II" annotations transferred to rat.
- Klf2 with Prdm14 promotes reversion of epiblast stem cells to naive pluripotency, with DNA
  demethylation and X reactivation [PMID:22482507] (source of mouse "epigenetic regulation of
  gene expression").

## Synthesis
Klf2 is a sequence-specific C2H2 zinc-finger transcription factor that binds CACCC/GC-rich
promoter elements and predominantly activates RNA polymerase II transcription of target genes
(cPLA2 in rat lung epithelium; eNOS, S1pr1, embryonic globins in orthologues), with
context-specific repression of others (VEGFA; inflammatory adhesion molecules, largely
indirectly). It is a flow-responsive endothelial factor and an immediate-early gene in cardiac
myocytes. Developmental phenotypes (vessel stabilization, erythropoiesis, lung development,
T-cell trafficking) are downstream consequences of its transcriptional activity.
