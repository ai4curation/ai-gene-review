# ALG5 (human) review notes

UniProtKB: Q9Y673. HGNC:20266. Gene on chromosome 13. 324 aa, single-pass type II
ER membrane protein (signal-anchor TM 8-28; short lumenal N-terminus 1-7; large
cytoplasmic domain 29-324). Glycosyltransferase family 2 (CAZy GT2); CDD DPG_synthase.

## Verified core biology

ALG5 is the **dolichyl-phosphate beta-glucosyltransferase (Dol-P-Glc synthase)**,
EC 2.4.1.117 (RHEA:15401). It transfers glucose from **UDP-alpha-D-glucose onto
dolichyl phosphate** to make **dolichyl beta-D-glucosyl phosphate (Dol-P-Glc)**, on
the cytosolic face of the ER membrane. Dol-P-Glc is the lipid-linked glucose donor
used by ALG6, ALG8 and ALG10 to add the three terminal glucoses to the dolichol-linked
oligosaccharide (LLO) during N-glycosylation, producing Glc(3)Man(9)GlcNAc(2)-PP-Dol.

Sources:
- UniProt FUNCTION [file:human/ALG5/ALG5-uniprot.txt "Dolichyl-phosphate beta-glucosyltransferase
  produces dolichyl beta-D-glucosyl phosphate/Dol-P-Glc, the glucose donor substrate used
  sequentially by ALG6, ALG8 and ALG10 to add glucose residues on top of the Man(9)GlcNAc(2)-PP-Dol structure"]
- CATALYTIC ACTIVITY: RHEA:15401, EC=2.4.1.117 [file:human/ALG5/ALG5-uniprot.txt]
- Reactome R-HSA-446214 "Synthesis of dolichyl-phosphate-glucose": ALG5 "catalyzes the reaction
  of cytosolic UDP-glucose with dolichyl phosphate exposed on the cytosolic face of the ER membrane
  to form Dolichyl-P-glucose".

## Localization

ER membrane, single-pass (signal-anchor for type II membrane protein), catalytic
domain cytosolic. UniProt SUBCELLULAR LOCATION "Endoplasmic reticulum membrane
{ECO:0000269|PubMed:10359825}; Single-pass membrane protein {ECO:0000255}." The enzyme
is "most probably active on the cytoplasmic side of the endoplasmic reticulum".

## Key reference PMID:10359825 (Imbach et al. 1999, PNAS)

Abstract-only in cache (full_text_available: false). The paper is titled/framed around
ALG6 causing CDGS type-Ic, and states "Although ALG5 was not altered in the patients".
BUT the full text also **cloned and functionally characterized human ALG5**: it reports
"we have cloned and analyzed the human orthologs to the ALG5 dolichyl phosphate
glucosyltransferase and ALG6 ..." and "Expression of the human ALG5 and ALG6 cDNA could
partially complement the respective S. cerevisiae alg5 and alg6 deficiency." This is the
basis for the human ALG5 experimental annotations (IDA/IMP/IGI for MF, BP, and ER-membrane
localization; UniProt also cites this paper for EC 2.4.1.117 catalytic activity and the
ER-membrane subcellular location). Per curation policy I defer to the curator on these
experimental annotations (full text not in cache).

## Protein binding IPIs (GO:0005515)

Four IntAct IPI annotations (PMID:32353859, 32838362, 33060197, 36217030) all record the
interaction with SARS-CoV-2 protein ORF3a (P0DTC3, "3a") from proteome-wide virus-host
interactome screens. UniProt INTERACTION line: "Q9Y673; P0DTC3: 3a; Xeno; NbExp=4".
These are non-informative `protein binding` terms from high-throughput viral interactome
screens; they do not describe ALG5's endogenous molecular function. Per policy: bare
protein binding IPIs -> MARK_AS_OVER_ANNOTATED (not REMOVE). PMID:32838362 has full text and
mentions ORF3a; the others are abstract-only in cache.

## Disease

- ALG5-CDG (CDG type; congenital disorder of glycosylation) — rare, biallelic loss of
  ALG5 function.
- Polycystic kidney disease 7 (PKD7, MIM:620056), autosomal dominant: a specific ALG5
  splice/truncating variant and missense variants (R208H, R212H, 258-324del). UniProt
  DISEASE + PubMed:35896117 (Lemoine et al. 2022, AJHG; not in cache). Variants show
  "loss of function in protein N-linked glycosylation; unable to rescue defective PKD1
  glycosylation and maturation in ALG5-deficient cells". Mechanistically links ALG5 to
  PKD1 (polycystin-1) glycosylation/maturation.

## Annotation dispositions (summary)

Core: GO:0004581 MF (ACCEPT), GO:0006488 / GO:0006487 BP (ACCEPT), GO:0005789 ER membrane CC (ACCEPT).
- GO:0098554 / GO:0098556 (cytoplasmic side of ER / rough ER membrane): ACCEPT — consistent
  with topology (cytosolic catalytic domain) and UniProt "active on the cytoplasmic side".
- GO:0016020 membrane (HDA, NK membrane proteome PMID:19946888): too general vs ER membrane -> MODIFY? 
  It is a large-scale MS localization to bulk membrane; keep as non-core / over-annotated
  relative to the specific ER-membrane term. MARK_AS_OVER_ANNOTATED (redundant with specific CC).
- GO:0005515 protein binding x4: MARK_AS_OVER_ANNOTATED (viral interactome, non-informative).
