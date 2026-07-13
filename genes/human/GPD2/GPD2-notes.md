# GPD2 (human) — review notes

UniProt: P43304 (GPDM_HUMAN), gene symbol GPD2 (HGNC:4456). 727 aa precursor;
mitochondrial transit peptide 1–42; mature chain 43–727. Isoform 2 (P43304-2)
lacks residues 1–126 (VSP_017134).

## Identity and core biochemistry

GPD2 is the **mitochondrial FAD-dependent glycerol-3-phosphate dehydrogenase**
(mGPDH; also mtGPD, m-GDH, GPD-M). It is an inner-membrane flavoenzyme that
oxidises sn-glycerol-3-phosphate to dihydroxyacetone phosphate (DHAP), passing
electrons via its bound FAD to the ubiquinone (quinone) pool of the respiratory
chain.

- EC 1.1.5.3; Rhea:RHEA:18977. UniProt CATALYTIC ACTIVITY:
  [file:human/GPD2/GPD2-uniprot.txt "Reaction=a quinone + sn-glycerol 3-phosphate = dihydroxyacetone"]
  ("phosphate + a quinol; ... EC=1.1.5.3"). The physiological direction is
  left-to-right (G3P -> DHAP). This maps directly to GO:0004368
  "glycerol-3-phosphate dehydrogenase (quinone) activity" (OLS def:
  "sn-glycerol 3-phosphate + a quinone = glycerone phosphate + a quinol").
- Cofactor FAD: [file:human/GPD2/GPD2-uniprot.txt "Name=FAD; Xref=ChEBI:CHEBI:57692"];
  FAD-binding region 71..99 (FT BINDING /ligand="FAD"). KW: FAD; Flavoprotein.
  This supports GO:0050660 (flavin adenine dinucleotide binding) as a core MF,
  even though it is not currently in GOA.
- Family: [file:human/GPD2/GPD2-uniprot.txt "Belongs to the FAD-dependent glycerol-3-phosphate"]
  ("dehydrogenase family.").

## Glycerol-phosphate shuttle role

Together with cytosolic NAD-linked GPD1, GPD2 constitutes the glycerol-phosphate
shuttle, delivering cytosolic reducing equivalents to the ubiquinone pool
(bypassing Complex I). Reactome R-HSA-188467 summary:
[Reactome:R-HSA-188467 "FAD-linked mitochondrial glycerol 3-phosphate dehydrogenase (GPD2, alias: mGPDH) and its NAD-linked  cytosolic isoform (GPD1, alias:cGPDH) constitute glycerol phosphate shuttle."]
and [Reactome:R-HSA-188467 "GPD2 catalyzes the unidirectional conversion of glycerol-3-phosphate (G-3-P) to dihydroxyacetone phosphate (DHAP) with concomitant reduction of the enzyme-bound FAD."].
GO:0006127 (glycerol-3-phosphate shuttle) OLS def confirms the shuttle transfers
reducing equivalents from cytosolic NADH into mitochondria via G3P, with
mitochondrial GPDH using FAD to convert G3P back to DHAP and feeding FADH2
electrons into the electron transport chain.

## Calcium binding / regulation

GPD2 carries two C-terminal EF-hand domains (623–658, 659–694) and binds Ca2+
(FT BINDING residues 672,674,676,678,683). Calcium binding is regulatory:
[file:human/GPD2/GPD2-uniprot.txt "Calcium-binding enhance the activity of the"]
("enzyme."). This underlies its role as a beta-cell glucose sensor. The GOA
calcium-ion-binding annotation (GO:0005509, IEA from InterPro EF-hand
IPR002048) is consistent with the EF-hand domains but is a regulatory/accessory
feature, not the core catalytic function → KEEP_AS_NON_CORE.

## Pancreatic beta-cell / diabetes physiology

UniProt FUNCTION: [file:human/GPD2/GPD2-uniprot.txt "Calcium-responsive mitochondrial glycerol-3-phosphate"]
("dehydrogenase which seems to be a key component of the pancreatic beta-")
("cell glucose-sensing device."). PMID:9070847 (Novials et al. 1997,
abstract-only, full_text_available: false) reports EC/CATALYTIC-ACTIVITY and
ACTIVITY-REGULATION evidence and a calcium-binding-domain mutation in diabetic
subjects. Abstract:
[PMID:9070847 "The Ca(2+)-sensitive and mitochondrial enzyme FAD-linked glycerophosphate"]
("dehydrogenase (m-GDH) represents an essential component of the pancreatic B-cell")
("glucose-sensing device."). This is the source of the IDA on GO:0004368
(enables) in GOA — accept as the experimental basis of the core catalytic MF.

## Localization evidence

- SUBCELLULAR LOCATION (UniProt): [file:human/GPD2/GPD2-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion."]
- Mechanistically it is an inner-membrane protein facing the intermembrane-space
  side. GO:0005743 (mitochondrial inner membrane) is the specific correct
  location; GO:0005739 (mitochondrion) annotations are correct but less specific.
- HTP mitochondrial-proteome evidence: PMID:34800366 (MitoCoP, full text
  available) is a high-confidence human mitochondrial proteome; GPD2/P43304 is a
  MitoCoP member (supplementary Table S1). Supports GO:0005739 (located_in) as
  corroborating localization evidence:
  [PMID:34800366 "high-confidence mitochondrial proteome MitoCoP"].
- HPA IDA (GO_REF:0000052) and Reactome TAS also support mitochondrial /
  inner-membrane localization.

## Annotation review decisions (summary)

Core (evolved) function:
- GO:0004368 glycerol-3-phosphate dehydrogenase (quinone) activity — MF core.
  ACCEPT the IDA (PMID:9070847) and the IBA; the two Reactome TAS and the
  ARBA/InterPro IEA are redundant duplicates of the same activity → ACCEPT
  (duplicates of an experimentally supported term).
- GO:0006127 glycerol-3-phosphate shuttle — BP core (IBA + Reactome TAS). ACCEPT.
- GO:0006072 glycerol-3-phosphate metabolic process — parent BP; correct but
  general → KEEP_AS_NON_CORE (glycerophosphate shuttle / catabolism is the
  specific process).
- GO:0005743 mitochondrial inner membrane — specific correct location (TAS
  Reactome). ACCEPT.

Non-core / supporting:
- GO:0005739 mitochondrion (IBA is_active_in; IEA located_in; HPA IDA; HTP) —
  correct but less specific than the inner membrane → KEEP_AS_NON_CORE.
- GO:0005509 calcium ion binding (IEA InterPro EF-hand) — real regulatory
  feature, not core catalysis → KEEP_AS_NON_CORE.
- GO:0019563 glycerol catabolic process (IEA UniPathway) — GPD2 acts on
  glycerol-3-phosphate, not glycerol directly; it is one step of the glycerol
  degradation pathway (glycerol -> G3P by glycerol kinase -> DHAP by GPD2).
  UniProt PATHWAY: [file:human/GPD2/GPD2-uniprot.txt "Polyol metabolism; glycerol degradation via glycerol kinase"]
  ("pathway; glycerone phosphate from sn-glycerol 3-phosphate (anaerobic")
  ("route): step 1/1."). Pathway-level term; over-general for the specific
  activity but pathway-appropriate → KEEP_AS_NON_CORE.

No REMOVE actions: the only IEAs present (quinone MF, inner membrane, mitochondrion,
Ca-binding, glycerol catabolism) are all biologically correct, so none are
"clearly wrong". Experimental IDA (PMID:9070847) accepted.

## Core function term ids (final)

- MF: GO:0004368 glycerol-3-phosphate dehydrogenase (quinone) activity
- MF: GO:0050660 flavin adenine dinucleotide binding (FAD cofactor; not in GOA
  but strongly supported by UniProt COFACTOR + FAD-binding region)
- BP: GO:0006127 glycerol-3-phosphate shuttle
- Location: GO:0005743 mitochondrial inner membrane
