# Pck1 (mouse, Q9Z2V4) curation notes

## Deep research status

- 2026-10-16: `just deep-research mouse Pck1 --provider falcon` was run twice and failed both
  times with `Exception: Failed to authenticate` / `Provider falcon exited with code 1` / `All
  providers failed`. No deep-research file was produced, and none has been written by hand.
  These notes are built from the cached publications (`publications/PMID_*.md`), the UniProt
  record and the GOA/GO-CAM files.

## Identity and family

- Pck1 encodes the cytosolic GTP-dependent phosphoenolpyruvate carboxykinase (PEPCK-C,
  EC 4.1.1.32), 622 aa, PANTHER PTHR11561:SF18, Pfam PEPCK_N + PEPCK_GTP. Mitochondrial
  paralog is Pck2. UniProt: "Belongs to the phosphoenolpyruvate carboxykinase [GTP] family."
- Reaction: oxaloacetate + GTP = phosphoenolpyruvate + GDP + CO2 (RHEA:10388); physiologically
  both directions annotated in UniProt from PMID:30193097.
- Mn2+ cofactor (by similarity to human P35558).

## Core function: PEPCK-C catalysis in gluconeogenesis, cataplerosis, glyceroneogenesis

- Whole-body / hepatic knockouts (Magnuson lab).
  [PMID:10938127 "Mice that lack this enzyme die within 3 days of birth, while mice with at
  least a 90% global reduction of PEPCK, or a liver-specific knockout of PEPCK, are viable."]
  [PMID:10938127 "hepatic PEPCK may function more as an integrator of hepatic energy metabolism
  than as a determinant of gluconeogenesis."]
- Liver flux with 2H/13C: cataplerosis and gluconeogenesis from TCA intermediates require PEPCK-C.
  [PMID:15347677 "gluconeogenesis from tricarboxylic acid (TCA) cycle intermediates was nearly
  absent"] [PMID:15347677 "Disruption of hepatic cataplerosis due to loss of PEPCK leads to the
  accumulation of TCA cycle intermediates and a nearly complete blockage of gluconeogenesis from
  amino acids and lactate"]
- Kidney compensates for hepatic loss. [PMID:34156032 "Glucose homeostasis was maintained by a
  compensatory rise in renal glucose production and gluconeogenesis."]
- Kidney-specific (Pax8) KO and knock-in: ammoniagenesis, acid-base, glucose/lactate.
  [PMID:37102687 "PCK1 deletion led to hyperchloremic metabolic acidosis characterized by reduced
  but not abolished ammoniagenesis."] [PMID:37102687 "PCK1 is essential for kidney tubular cell
  acid-base control, mitochondrial function, and glucose/lactate homeostasis."]
- Renal expression rises with acidosis and K+ restriction (expression readout).
  [PMID:19458124 "SNAT3, PDG, and PEPCK mRNA abundance were elevated during MA and after 14-day
  K(+) restriction but not during high protein intake."]
- Adipose glyceroneogenesis: PPARE promoter mutation abolishes adipose Pck1 expression.
  [PMID:11792850 "The mutation abolished expression of the gene in white adipose tissue and
  considerably reduced its expression in brown adipose tissue"] [PMID:11792850 "the role of
  PEPCK-C in the regulation of glyceroneogenesis, a pathway critical for maintaining the
  deposition of triglycerides in adipose tissue."]
- Adipose overexpression increases glyceroneogenesis and FFA re-esterification.
  [PMID:11872659 "Transgenic mice showed a chronic increase in PEPCK activity, which led to
  increased glyceroneogenesis, re-esterification of free fatty acids (FFAs), increased adipocyte
  size and fat mass, and higher body weight."]
- Skeletal muscle overexpression (PEPCK-Cmus mice). [PMID:17716967 "On a mouse treadmill,
  PEPCK-C(mus) mice ran up to 6 km at a speed of 20 m/min, whereas controls stopped at 0.2 km."]
  [PMID:17716967 "We conclude that overexpression of PEPCK-C repatterns energy metabolism and leads
  to greater longevity."] This is a gain-of-function phenotype in a tissue with little native
  PEPCK-C; it supports cataplerotic capacity but is not a normal physiological role of muscle Pck1.
- Hanson-lab review framing PEPCK-C as a cataplerotic enzyme: PMID:19636077 (abstract not
  cached; title only).
- Acetylation toggles direction (mouse and human enzymes studied). [PMID:30193097 "dynamic
  acetylation of PCK1 interconverts the enzyme between gluconeogenic and anaplerotic
  activities."] [PMID:30193097 "SIRT1 deacetylates PCK1 and fully restores the gluconeogenic
  ability of PCK1."]
- Memory CD8+ T cells. [PMID:29230018 "CD8+ Tm cells markedly upregulate cytosolic
  phosphoenolpyruvate carboxykinase (Pck1)"] [PMID:29230018 "Abrogation of Pck1-glycogen-PPP
  decreases GSH/GSSG ratios and increases levels of reactive oxygen species (ROS), leading to
  impairment of CD8+ Tm formation and maintenance."] Pck1 provides metabolic flux; it is not a
  differentiation regulator per se.
- Transcriptional control (Pck1 as target): ATF3 represses the promoter. [PMID:11916968
  "transient transfection assays indicated that ATF3 repressed the activity of the PEPCK
  promoter."] HIF-1alpha liver KO lowers PEPCK. [PMID:19643083 "This appeared to result from
  reduced expression of PGK-1 and PEPCK since 3-PG, PEP and malate were accumulated to greater
  extents in the regenerated liver."]

## The PCK1 "protein kinase" / INSIG / SREBP claim (key issue)

- Single primary study, human HCC cells: [PMID:32322062 "activated AKT in human hepatocellular
  carcinoma (HCC) cells phosphorylates cytosolic phosphoenolpyruvate carboxykinase 1 (PCK1), the
  rate-limiting enzyme in gluconeogenesis, at Ser90. Phosphorylated PCK1 translocates to the
  endoplasmic reticulum, where it uses GTP as a phosphate donor to phosphorylate INSIG1 at Ser207
  and INSIG2 at Ser151."] [PMID:32322062 "This phosphorylation reduces the binding of sterols to
  INSIG1 and INSIG2 and disrupts the interaction between INSIG proteins and SCAP, leading to the
  translocation of the SCAP-SREBP complex to the Golgi apparatus"]
- Only independent follow-up found by PubMed search ("PCK1 INSIG SREBP protein kinase" returns
  only these two): PRRSV infection in monkey MARC-145 cells. [PMID:39433189 "Activated PCK1 then
  phosphorylated insulin-induced genes (INSIGs), resulting in their degradation."] No mouse
  biochemical or genetic experiment on Pck1 kinase activity or Ser90 was found.
- UniProt mouse record carries the kinase activity only "By similarity" to human P35558
  (RHEA:64020, ECO:0000250).
- GO-CAM gomodel:6205c24300000880 (human SREBP model): PCK1 activity GO:0106264 (part_of
  GO:0046889, occurs_in ER) has RO:0002630 (directly negatively regulates) edges to INSIG2 and
  INSIG1 sterol-binding activities (GO:0008142), which are part_of GO:0036316 SREBP-SCAP complex
  retention in ER. Downstream: SCAP -> MBTPS1/MBTPS2 (GO:0051604 protein maturation) -> KPNB1
  (GO:0006607 NLS-bearing protein import into nucleus) -> SREBF1/2 (GO:0045542 positive regulation
  of cholesterol biosynthetic process). The GO-CAM-to-GAF conversion emitted
  acts_upstream_of_or_within rows for PCK1 to each of these downstream processes, which were then
  projected to mouse Pck1 by ISO (GO_REF:0000119, with UniProtKB:P35558). The current human PCK1
  GOA file in this repo has no GO:0036316 / GO:0051604 / GO:0006607 / GO:0045542 rows, so the
  mouse rows are stale relative to the source.
- Assessment: PCK1 is not part of the retention machinery; the model says it inhibits retention
  (opposite sign); evidence is one human cancer-cell study plus a monkey-cell virus study.
  -> MARK_AS_OVER_ANNOTATED for GO:0036316, GO:0051604, GO:0006607, GO:0045542; same for the
  GO:0106264 kinase rows, peptidyl-serine phosphorylation rows and (positive) regulation of lipid
  biosynthetic process rows, all of which trace to PMID:32322062. Do not propose SREBP terms as NEW.

## Localization

- Cytosol is the principal compartment (IBA, IDA PMID:19458124, ISO). ER association is the
  AKT-phosphorylated pool in the human study; there is also a mouse IDA (PMID:19458124; abstract
  does not describe the localization data). Kept as non-core.
- Mitochondrion IBA (PTN000169230) is inherited from the node that also covers Pck2; mouse Pck1 is
  the cytosolic isozyme and has no transit peptide -> REMOVE.

## GO term notes

- GO:0046327 "glycerol biosynthetic process from pyruvate" (synonym glyceroneogenesis) is obsolete
  and points to GO:0006114 glycerol biosynthetic process, so GO:0006114 is GO's intended term for
  glyceroneogenesis, even though the pathway product is glycerol 3-phosphate.
