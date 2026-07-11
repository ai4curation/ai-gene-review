# PIGW review notes

UniProtKB:Q7Z7B1, HGNC:23213, human PIGW (Glucosaminyl-phosphatidylinositol-acyltransferase PIGW; PIG-W;
GlcN-PI-acyltransferase). 504 aa, multi-pass ER membrane protein (11 TM helices per UniProt features).
PANTHER PTHR20661; Pfam PF06423 (GWT1); InterPro IPR009447 (PIGW/GWT1); PIRSF017321 (GWT1).

Deep research: falcon provider is OUT OF CREDITS (HTTP 402) — no `-deep-research-falcon.md` was generated.
This review is grounded in the UniProt record, the seeded GOA, and cached publications (PMID:24367057;
Reactome R-HSA-162710, R-HSA-162683).

## Core biology

PIGW is the **GPI inositol acyltransferase** that catalyses the fourth step of GPI-anchor biosynthesis in
the ER: transfer of an acyl group (usually palmitate) from acyl-CoA to the **2-OH of the inositol ring** of
glucosaminyl-phosphatidylinositol (GlcN-PI), producing GlcN-(acyl)PI.

UniProt FUNCTION [file:human/PIGW/PIGW-uniprot.txt "Acyltransferase that catalyzes the acyl transfer from an
acyl-CoA at the 2-OH position of the inositol ring of a 6-(alpha-D-glucosaminyl)-1-(1,2-diacyl-sn-glycero-3-
phospho)-1D-myo-inositol (glucosaminyl phosphatidylinositol, GlcN-PI) ... and participates in the fourth step
of GPI-anchor biosynthesis"].

Catalytic activity (RHEA:60496 / RHEA:83759): GlcN-PI + fatty acyl-CoA -> GlcN-(acyl)PI + CoA. The inositol
acyl group is important for GPI transamidase recognition and is later removed by PGAP1.

Reactome R-HSA-162683: "In the fourth step of GPI synthesis, an acyl group (typically palmitate) is
transferred from acyl CoA to glucosaminyl-PI. Mutagenesis and cloning studies suggest that a single protein,
PIG-W, catalyzes this reaction (Murakami et al. 2003)."

## GOA MF term

The GOA molecular-function term carried across IBA (GO_REF:0000033), IEA/RHEA (GO_REF:0000116), and ISS
(GO_REF:0000024) is **GO:0032216 glucosaminyl-phosphatidylinositol O-acyltransferase activity** (label
confirmed current in local go.db 2026-07). This is the exact current term to use for core_functions MF.

## Localisation

ER membrane, multi-pass. UniProt [file:human/PIGW/PIGW-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic
reticulum membrane"; "Multi-pass membrane protein"]. GO:0005789 (ER membrane) is the current CC.

## Disease

Deficiency causes GPIBD11 (MIM:616025) — inherited GPI deficiency (hyperphosphatasia with mental retardation /
epileptic encephalopathy spectrum). PMID:24367057 (Chiyonobu et al. 2014): first PIGW-deficient patient, West
syndrome (hypsarrhythmia) + hyperphosphatasia + developmental delay; compound heterozygous NM_178517
c.211A>C (T71P) and c.499A>G (M167V). Variants reduce GPI-anchored protein surface expression on granulocytes.
UniProt DISEASE [file:human/PIGW/PIGW-uniprot.txt "developmental delay, intellectual disability, tonic
seizures associated with hypsarrhythmia, dysmorphic facial features, and elevated serum alkaline phosphatase"].

PMID:24367057 abstract is the basis of the two experimental-ish GOA annotations:
- GO:0072659 (protein localization to plasma membrane) IMP — the reduced surface GPI-AP expression phenotype
  (transport of GPI-APs to the cell surface requires PIGW).
- GO:0006505 (GPI anchor metabolic process) IC — curator inference (with GO:0072659) from the same paper.

## Annotation review decisions

- GO:0032216 O-acyltransferase activity (IBA, IEA-RHEA, ISS): ACCEPT — this is the specific, correct MF.
- GO:0006506 GPI anchor biosynthetic process (IBA, IEA, ISS, TAS-Reactome): ACCEPT — core BP.
- GO:0005783 endoplasmic reticulum (IBA): ACCEPT (CC; located within ER; ER membrane is more specific).
- GO:0005789 ER membrane (IEA-SubCell, ISS x2, TAS-Reactome): ACCEPT — precise location, multi-pass.
- GO:0006505 GPI anchor metabolic process (IEA-ARBA, IC): parent of biosynthetic process; keep the IC
  (curator, PMID:24367057) as ACCEPT but non-core (biosynthetic child is the informative core term);
  the IEA-ARBA duplicate MARK_AS_OVER_ANNOTATED (less informative parent, redundant with biosynthetic).
- GO:0016020 membrane (IEA-InterPro): MARK_AS_OVER_ANNOTATED — too general; ER membrane is the specific CC.
- GO:0016746 acyltransferase activity (IEA-InterPro): MARK_AS_OVER_ANNOTATED — general parent of GO:0032216.
- GO:0016747 acyltransferase activity, transferring groups other than amino-acyl groups (TAS-Reactome):
  MARK_AS_OVER_ANNOTATED — general parent of GO:0032216.
- GO:0072659 protein localization to plasma membrane (IMP, PMID:24367057): KEEP_AS_NON_CORE — downstream
  consequence of GPI-anchor synthesis, not the direct MF; experimental (defer to curator, do not REMOVE).
