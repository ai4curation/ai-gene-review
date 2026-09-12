# SLC52A2 (RFVT2 / riboflavin transporter 2) — review notes

UniProt: Q9HAB3 (S52A2_HUMAN). Gene: SLC52A2 (HGNC:30224). Synonyms: GPR172A, PAR1, RFT3, hRFT3.
445 aa, 11 predicted transmembrane helices, cryo-EM structure PDB 8XSM.

## Identity and the confusing "hRFT" vs "RFVT/SLC52" nomenclature

This is the single most important thing to get right for this gene. Two independent
naming schemes exist for the three human riboflavin transporters and they are
cross-wired:

- **RFVT / SLC52 standard nomenclature** (current): SLC52A1 = RFVT1 (RFT1), SLC52A2 = RFVT2 (RFT3),
  SLC52A3 = RFVT3 (RFT2).
- **Kyoto/Inui-lab "hRFT" nomenclature** (older): hRFT1 = SLC52A1, hRFT2 = SLC52A3, **hRFT3 = SLC52A2**.

The UniProt entry for Q9HAB3 confirms the identity: RecName "Solute carrier family 52,
riboflavin transporter, member 2"; AltName "Riboflavin transporter 3; Short=hRFT3"
[file:human/SLC52A2/SLC52A2-uniprot.txt "AltName: Full=Riboflavin transporter 3;"].
PMID:24253200 states it explicitly: "RFVT2 (formerly RFT3)" and "RFVT3 (formerly RFT2)"
[PMID:24253200 "coding for human riboflavin transporters RFVT3 (formerly RFT2) and RFVT2 (formerly RFT3), respectively"].

Consequence for annotation review: in PMID:21854757 (Subramanian 2011), the entity called
**hRFT-3 is this gene (SLC52A2/RFVT2)**, whereas the "hRFT-2 apical" result in that paper is
about SLC52A3. So the GO:0016323 (basolateral plasma membrane) IDA attributed to Q9HAB3
from PMID:21854757 corresponds to that paper's hRFT-3, which was described as
"localized predominantly within intracellular vesicles, although expression was evident at the
BLM of some cells" [PMID:21854757 "this transporter was found to be localized predominantly within intracellular vesicles, although expression was evident at the BLM of some cells"].
The curator (who read the full text and knew hRFT-3 = SLC52A2) correctly captured the partial
BLM signal. Note this is NOT the dominant/canonical localization; the mainstream picture is
plasma-membrane / cell-surface expression.

## Core biology (from UniProt, authoritative)

- FUNCTION: "Plasma membrane transporter mediating the uptake by cells of the water soluble
  vitamin B2/riboflavin" [file:human/SLC52A2/SLC52A2-uniprot.txt "Plasma membrane transporter mediating the uptake by cells of"].
  Humans cannot synthesize riboflavin and must obtain it via intestinal absorption
  [file:human/SLC52A2/SLC52A2-uniprot.txt "Humans are unable"].
- CATALYTIC ACTIVITY: riboflavin(in) = riboflavin(out); Rhea RHEA:35015 / ChEBI:57986
  [file:human/SLC52A2/SLC52A2-uniprot.txt "Reaction=riboflavin(in) = riboflavin(out); Xref=Rhea:RHEA:35015,"].
- ACTIVITY REGULATION: transport is Na+-independent, moderately pH-sensitive, strongly
  inhibited by lumiflavin, weakly by FAD/FMN
  [file:human/SLC52A2/SLC52A2-uniprot.txt "Riboflavin transport is Na(+)-independent but"].
- KINETICS: KM = 0.33 uM for riboflavin
  [file:human/SLC52A2/SLC52A2-uniprot.txt "KM=0.33 uM for riboflavin"].
  This matches the "hRFT3" KM = 0.33 umol/L in PMID:20463145, confirming that paper is about Q9HAB3
  [PMID:20463145 "hRFT1, hRFT2, and hRFT3 for riboflavin were 1.38,\n0.98, and 0.33 micromol/L"].
- SUBCELLULAR LOCATION: Cell membrane; multi-pass membrane protein
  [file:human/SLC52A2/SLC52A2-uniprot.txt "SUBCELLULAR LOCATION: Cell membrane"].
- TISSUE SPECIFICITY: "Highly expressed in brain, fetal brain and salivary gland"
  [file:human/SLC52A2/SLC52A2-uniprot.txt "Highly expressed in brain, fetal brain and salivary"].
- SIMILARITY: "Belongs to the riboflavin transporter family"
  [file:human/SLC52A2/SLC52A2-uniprot.txt "Belongs to the riboflavin transporter family."].

## Disease — Brown-Vialetto-Van Laere syndrome type 2 (BVVLS2; MIM 614707)

Biallelic SLC52A2 loss-of-function → riboflavin transporter deficiency: childhood-onset
axonal sensorimotor neuronopathy with sensorineural deafness, optic atrophy, bulbar palsy,
respiratory insufficiency; treatable with high-dose oral riboflavin.
[file:human/SLC52A2/SLC52A2-uniprot.txt "autosomal recessive progressive neurologic disorder characterized by"];
PMID:24253200 abstract: "SLC52A2 mutations cause reduced riboflavin uptake and reduced riboflavin
transporter protein expression" and high-dose oral riboflavin gives "significant and sustained
clinical and biochemical improvements"
[PMID:24253200 "reduced riboflavin uptake and reduced riboflavin"].

## Functional / variant evidence supporting MF and CC

- PMID:20463145 (Yao 2010, "hRFT3"=SLC52A2): cloned, [3H]riboflavin uptake in HEK293, KM 0.33 uM,
  Na+/Cl- independent, inhibited by riboflavin analogs; strongly expressed in brain and salivary
  gland. Abstract only (full_text_available: false).
- PMID:24253200 (Foley 2014): in-vitro 3H-riboflavin transport assays for 7 BVVLS2 mutants;
  WT SLC52A2 transports riboflavin; "The dysfunctional p.W31S mutant was expressed in the plasma
  membrane" [PMID:24253200 "The dysfunctional p.W31S mutant was expressed in the plasma\nmembrane."];
  disease mutants show "a moderate but significant decrease in 3H-riboflavin transport activity
  compared with wild-type SLC52A2" [PMID:24253200 "3H-riboflavin transport activity compared with wild-type SLC52A2"].
- PMID:27702554 (Udhayabanu 2016): patient with SLC52A2 p.P141T + SLC52A3 p.N21S; 3H-RF uptake and
  live-cell confocal imaging; WT GFP-hRFVT-2 shows membranous/cell-surface expression, P141T
  "showed membranous expression similar to wild-type GFP-hRFVT-2"
  [PMID:27702554 "showed membranous expression similar to wild-type GFP-hRFVT-2"] with a slight
  reduction in riboflavin uptake.

## Protein interactions (bare "protein binding", high-throughput)

Two IntAct IPI annotations to GO:0005515:
- PMID:25416956 (Rolland 2014, human interactome map) — interactor CDC23 (Q9UJX2).
- PMID:32296183 (Luck 2020, HuRI binary interactome) — interactor FAM209A (Q5JX71).
Both interactors match UniProt's INTERACTION section
[file:human/SLC52A2/SLC52A2-uniprot.txt "Q9HAB3; Q9UJX2: CDC23;"],
[file:human/SLC52A2/SLC52A2-uniprot.txt "Q9HAB3; Q5JX71: FAM209A;"].
These are systematic Y2H/high-throughput hits with no functional interpretation; bare
"protein binding" is uninformative → MARK_AS_OVER_ANNOTATED (not removed; experimental IPI).

## Legacy / disputed function: 4-hydroxybutyrate (GHB) receptor

PMID:17197387 (Andriamampandry 2007) cloned "GHBh1"/GPR172A from human frontal cortex as a
putative gamma-hydroxybutyrate (GHB) receptor with GTP-gamma-S-sensitive signalling. This is the
basis of the GO:0062124 (4-hydroxybutyrate receptor activity) IDA and one of the plasma-membrane
IDAs. UniProt retains this only tentatively: "May also act as a receptor for 4-hydroxybutyrate
(Probable)" with ECO:0000305 [file:human/SLC52A2/SLC52A2-uniprot.txt "May also act as a receptor for 4-"].
The protein is now firmly established as a riboflavin transporter (SLC/TCDB 2.A.125 e-RFT family;
no GPCR fold). The GHB-receptor characterization is best treated as an over-annotation /
superseded secondary claim; per curation policy an experimental IDA is marked
MARK_AS_OVER_ANNOTATED rather than removed. The plasma-membrane IDA from the same paper is
retained (the localization observation is consistent with the transporter).

## riboflavin metabolic process (Reactome TAS)

GO:0006771 (riboflavin metabolic process) TAS from Reactome R-HSA-196843 "Vitamin B2 (riboflavin)
metabolism". SLC52A2 is a transporter, not a metabolic enzyme; it participates in the pathway only
by importing the vitamin. The specific and correct BP is GO:0032218 riboflavin transport (already
annotated). GO:0006771 is an over-annotation of a transporter as a metabolic-process participant →
MARK_AS_OVER_ANNOTATED.

## Summary of core functions

- MF: GO:0032217 riboflavin transmembrane transporter activity (Na+-independent riboflavin uptake).
- BP: GO:0032218 riboflavin transport (cellular riboflavin/vitamin B2 uptake; brain/systemic RF homeostasis).
- CC: GO:0005886 plasma membrane (multi-pass; cell-surface/apical-basolateral depending on cell type).
</content>
</invoke>
