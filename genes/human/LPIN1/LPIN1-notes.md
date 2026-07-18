# LPIN1 (lipin-1) review notes

UniProt: Q14693 (LPIN1_HUMAN), 890 aa, HGNC:13345. Source file: `LPIN1-uniprot.txt`.

## Core biology (from UniProt + primary literature)

LPIN1/lipin-1 is a **Mg2+-dependent phosphatidate phosphatase (PAP1)** (EC 3.1.3.4) that
catalyzes the penultimate step of glycerolipid synthesis: dephosphorylation of
**phosphatidic acid (PA) -> diacylglycerol (DAG) + Pi**.

- UniProt FUNCTION: "Acts as a magnesium-dependent phosphatidate phosphatase enzyme which
  catalyzes the conversion of phosphatidic acid to diacylglycerol during triglyceride,
  phosphatidylcholine and phosphatidylethanolamine biosynthesis and therefore controls the
  metabolism of fatty acids at different levels"
  [file:human/LPIN1/LPIN1-uniprot.txt].
- Catalytic activity RHEA:27429, EC=3.1.3.4; cofactor Mg(2+) (and to lesser extent Mn(2+))
  [file:human/LPIN1/LPIN1-uniprot.txt].
- Bifunctional: "Acts also as nuclear transcriptional coactivator for PPARGC1A/PPARA
  regulatory pathway to modulate lipid metabolism gene expression (By similarity)"
  [file:human/LPIN1/LPIN1-uniprot.txt]. Interacts (via LXXIL motif) with PPARA; interacts
  with PPARGC1A and MEF2C (all By similarity from mouse Q91ZP3).
- HAD-like fold with the DXDXT catalytic motif; lipins are NOT integral membrane proteins
  and translocate from cytosol to membranes [PMID:23426360 "lipins are not integral membrane
  proteins, and they need to translocate from the cytosol to intracellular membranes to
  participate in glycerolipid synthesis"].

## Enzymatic characterization (experimental, human protein)

- PMID:20231281 (Han & Carman 2010, EXP): purified human lipin 1 alpha/beta/gamma isoforms
  have PA phosphatase activity dependent on Mg2+/Mn2+; Km 0.35/0.24/0.11 mM for the three
  isoforms; inhibited by sphingoid bases, propranolol, Ca2+, Zn2+ [PMID:20231281 "PA
  phosphatase activities of the alpha, beta, and gamma isoforms were dependent on Mg(2+) or
  Mn(2+) ions"].
- PMID:23426360 (Eaton et al. 2013, IDA): lipin-1 PAP activity assayed with PA/PE mixtures;
  mTOR-dependent phosphorylation regulates membrane binding [PMID:23426360 "The lipin gene
  family encodes a class of Mg(2+)-dependent phosphatidic acid phosphatases involved in the
  de novo synthesis of phospholipids and triglycerides"].
- PMID:29765047 (Li et al. 2018, IDA; full text available): KAT5/Tip60-mediated acetylation
  at Lys-425/Lys-595 drives cytosol->ER translocation and DAG generation for TAG synthesis
  [PMID:29765047 "fatty acids stimulate Tip60-dependent acetylation and endoplasmic
  reticulum translocation of phosphatidic acid phosphatase lipin 1 to generate diacylglycerol
  for TAG synthesis"]. Basis for the experimental ER / cytosol localization annotations.
- PMID:39577771 (Stukey et al. 2025, EXP; full text): sertraline is a novel PAP inhibitor of
  human lipin 1 (alpha/beta/gamma) [PMID:39577771 "Sertraline also inhibited the PAP activity
  of human lipin 1"].
- PMID:31695197 (MacVicar et al. 2019, IDA): mTORC1-LIPIN1-YME1L axis; LIPIN1 decreases
  mitochondrial PE and promotes proteolysis [PMID:31695197 "a lipid signalling cascade via
  the phosphatidic acid phosphatase LIPIN1, which decreases phosphatidylethanolamine levels
  in mitochondrial membranes"]. Basis for phosphatidylethanolamine metabolic process
  annotation.
- PMID:18694939 (Grimsey et al. 2008, EXP; full text): lipin 1 is the major PAP1 enzyme in
  HeLa cells; siRNA depletion cuts cellular PAP1 ~86% [PMID:18694939 "lipin 1-depleted
  extracts show an 86% reduction in the total cellular PAP1 activity, indicating that lipin 1
  is the major PAP1 enzyme in these cells"]. Also cytosolic localization: lipin 1-HA shows
  predominantly cytosolic staining [PMID:18694939 "lipin 1-HA shows a predominantly cytosolic
  staining"]. PAP1 activity of lipin 1 is inhibited by mitotic phosphorylation
  [PMID:18694939 "the PAP1 activity of both lipins is inhibited by phosphorylation during
  mitosis"].

## Adipose / developmental role

- PMID:11138012 (Peterfy et al. 2001, ISS basis): Lpin1 is the fld gene; encodes "a novel
  nuclear protein which we have named lipin"; required for normal adipose tissue development
  [PMID:11138012 "lipin is required for normal adipose tissue development"]. This is the
  mouse-gene discovery paper; human nucleus annotation is ISS from mouse Q91ZP3.
- PMID:23028044 (Nadra et al. 2012, ISS basis for cold-induced thermogenesis): cell-autonomous
  lipin 1 required for WAT and BAT; Lpin1 loss alters PPARalpha/PGC-1alpha/UCP1 and cold
  sensitivity [PMID:23028044 "Loss of lipin 1 also affected BAT development and function, as
  revealed by histological changes, defects in the expression of ... (PPARalpha), PGC-1alpha,
  and UCP1, and functionally by altered cold sensitivity"]. Mouse study; human annotation ISS
  from mouse.

## Localization (UniProt SUBCELLULAR LOCATION)

Cytoplasm/cytosol; Endoplasmic reticulum membrane; Nucleus membrane (By similarity). Note:
"Translocates from the cytosol to the endoplasmic reticulum following acetylation by KAT5"
[file:human/LPIN1/LPIN1-uniprot.txt]. Lipin-1 has NO transmembrane domain (peripheral
membrane / soluble). The Reactome nuclear-envelope/nucleoplasm annotations reflect its
regulated dephosphorylation there (CTDNEP1:CNEP1R1, CDK1) and the nuclear-lamina context.

## Disease

Biallelic LPIN1 mutations cause **autosomal-recessive recurrent acute myoglobinuria (ARARM,
MIM:268200)** = recurrent childhood rhabdomyolysis [file:human/LPIN1/LPIN1-uniprot.txt DISEASE;
PMID:18817903 (not cited in GOA)].

## Interactome annotation

The single IPI "protein binding" (GO:0005515) comes from PMID:32814053, a large Y2H
neurodegenerative-disease interactome map (LPIN1 was one of ~500 ND-related baits; interactors
include HTT, ATXN10, WFS1 etc). Uninformative bare protein binding; MARK_AS_OVER_ANNOTATED.

## Curation decisions summary

- Core MF: phosphatidate phosphatase activity (GO:0008195) — multiple human-protein IDA/EXP.
- Core BP: triglyceride biosynthetic process (GO:0019432); diacylglycerol biosynthetic process
  (GO:0006651, proposed); phosphatidic acid metabolic process (GO:0046473) captured via the
  reaction. Phosphatidylethanolamine metabolic process (GO:0046337) is a real downstream
  metabolic role (DAG feeds PE synthesis) — ACCEPT/non-core.
- Nuclear transcriptional-coactivator role (GO:0003713 / GO:0045944): real but By-similarity/IBA
  in human; keep as non-core.
- IEA rat-ortholog terms (animal organ regeneration GO:0031100; negative regulation of
  myelination GO:0031642) are peripheral single-ortholog Ensembl transfers → over-annotated.
- Mitochondrial outer membrane (GO:0005741, IBA) and mitochondrial fission role: by similarity /
  supported by PMID:31695197 mitochondrial PE role; keep as non-core.
</content>
</invoke>
