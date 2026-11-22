# PIK3CA (human, P42336) — curation notes

Journal of the GO annotation review. Provenance recorded inline as
`[PMID:xxxx "verbatim text"]`.

## Identity and core biology

PIK3CA encodes p110α, the ~110 kDa catalytic subunit of class IA
phosphoinositide 3-kinase (PI3Kα). It is an obligate heterodimer with a p85-family
regulatory subunit (PIK3R1/p85α and its splice forms p55α/p50α, PIK3R2/p85β,
PIK3R3/p55γ) [PMID:19200708 "Class 1A PI3Ks are a collection of heterodimeric lipid kinases that consist of a p110 catalytic subunit and a regulatory subunit."].

Core molecular function: phosphorylation of the 3'-OH of the inositol ring of
membrane PI(4,5)P2 using ATP to generate the second messenger PIP3
[PMID:19200708 "The activated p110 catalytic subunit of PI3K primarily uses phosphatidylinositol 4,5-biphosphate (PIP2) as a substrate to generate phosphatidylinositol 3,4,5-triphosphate (PIP3)."].
UniProt records EC 2.7.1.153 (PI(4,5)P2 3-kinase → GO:0046934) and EC 2.7.1.137
(PtdIns 3-kinase → GO:0016303), plus a secondary/autophosphorylation
protein-serine kinase activity EC 2.7.11.1
[PMID:28676499 "PI3Ks have dual kinase specificity: a lipid kinase activity that phosphorylates the 3'-hydroxyl of phosphoinositides and a protein-kinase activity that includes autophosphorylation."].
The lipid kinase is the physiologically dominant activity; the protein-kinase
activity (p85 autophosphorylation etc.) is real but of unresolved in-vivo
importance (deep research; UniProt FUNCTION).

Downstream: PIP3 recruits PH-domain effectors (AKT, PDK1) to the membrane,
driving the PI3K-AKT-mTOR axis controlling growth, survival, proliferation,
metabolism [PMID:19200708 "Subsequently PIP3 acts as a lipid second messenger promulgating signals via a high affinity interaction with pleckstrin homology (PH) domains in downstream effectors, such as serine/threonine kinases AKT and PDK1"].

## Isoform specialization (for KEEP_AS_NON_CORE decisions)

- p110α is the primary insulin/IGF/RTK-responsive class IA isoform
  [PMID:19200708 "the p110α isoform is the primary insulin-responsive PI3K associated with the IRS-1 complex, a key mediator of insulin, insulin-like growth factor-1 and leptin action"].
  Supports GO:0008286 insulin receptor signaling, GO:0048009 IGF receptor signaling,
  GO:0007173 EGFR signaling (all KEEP_AS_NON_CORE, downstream context of the core MF).
- p110α is the endothelial-cell-autonomous isoform in vascular development
  [PMID:19200708 "p110α, but not p110β/δ, exerts endothelial cell-autonomous functions by regulating endothelial cell migration during vascular development"].
  Supports GO:0001944 vasculature development, GO:0043542 endothelial cell migration,
  GO:0038084 VEGF signaling (KEEP_AS_NON_CORE).
- Kinase activity of p110α is required for development (homozygous kinase-dead is
  embryonic-lethal) [PMID:19200708 "the knock-in of homozygous kinase-dead p110α (PIK3CAD933A/D933A) causes early embryonic lethality"]. Necessity, not a separate
  process participation — informs that overgrowth/developmental terms stay non-core.
- Cardiac/cytoskeletal roles: p110α is "the key PIP3-producing enzyme in the
  heart"; its loss increases gelsolin-mediated actin severing
  [PMID:30568254 "loss of PI3Kα, the key PIP3-producing enzyme in the heart, increases gelsolin-mediated actin-severing activities"]. Supports the cardiac-muscle and
  actin-cytoskeleton IEA/ISS transfers from mouse Pik3ca (P42337) as KEEP_AS_NON_CORE.
- Anoikis/survival: in intestinal crypt cells the predominant complexes are
  p110α/p85β and p110α/p55γ, and p110α (not β/γ/δ) knockdown reduces Akt-1 and
  survival [PMID:22402981 "the inhibition and/or siRNA-mediated expression silencing of p110α, but not that of p110β, γ or δ, results in Akt-1 down-activation and"];
  [PMID:22402981 "the predominant PI3-K complexes expressed by HIEC cells are p110α/p85β and p110α/p55γ"]. Supports GO:0005943 class IA complex (IDA) and
  GO:2000811 negative regulation of anoikis.

## Paralog caveats

- PMID:21035500 (platelet activation, TAS) is titled/framed on PI3Kβ
  ("Regulation and roles of PI3Kβ, a major actor in platelet signaling"); platelet
  activation is predominantly a p110β function → MARK_AS_OVER_ANNOTATED for p110α.
- PMID:30496354 (GO:0038084 VEGF, GO:0043491, GO:0051897; IGI with VEGFA P15692) is
  framed on p110β/cardiac remodelling but the full text assays PI3Kα compensation in
  endothelium; keep as non-core rather than removing an experimental IGI I cannot
  fully adjudicate.
- GO:0005944 class IB complex (IBA at PTN000799659, WITH PIK3CG P48736): class IB is
  the p110γ complex. p110α is class IA, never class IB → REMOVE (IBA over-propagation
  arguable on biological grounds).

## Protein binding (GO:0005515)

47 generic `protein binding` IPI rows (p85 subunits PIK3R1/R2/R3, GRB2, IRS1,
ERBB3, HRAS-adjacent, high-throughput interactome maps, etc.). Per repo policy,
generic protein binding is uninformative → REMOVE (removal does not deny the
interaction). The functionally meaningful facts (p85 heterodimer = class IA
complex; IRS/RTK adaptor recruitment) are captured by GO:0005943 and the signaling
BP terms. No specific replacement MF is invented from interaction data alone.

## Core function synthesis

1. Class IA PI3K lipid kinase: GO:0046934 (PI(4,5)P2 3-kinase → PIP3), in
   GO:0005943 class IA complex, at plasma membrane, directly involved in
   GO:0043491 PI3K-AKT signal transduction.
