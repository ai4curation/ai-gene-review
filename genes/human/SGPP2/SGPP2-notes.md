# SGPP2 (Sphingosine-1-phosphate phosphatase 2) — review notes

UniProt: Q8IWX5 (SGPP2_HUMAN), 399 aa. HGNC:19953. Gene on chromosome 2.
Paralog of SGPP1 (Q9BX95). Belongs to the type 2 lipid phosphate phosphatase
(LPP / PAP2) family.

## Identity and molecular function

SGPP2 is the second human sphingosine-1-phosphate phosphatase (a.k.a. S1P
phosphohydrolase, SPP2/hSPP2). It was identified by homology to SPP1/SGPP1 and
shown to dephosphorylate sphingoid-base 1-phosphates.

- Identity / activity: "we have identified a second human S1P phosphohydrolase,
  SPP2, based on sequence homology to human SPP1. SPP2 exhibited high
  phosphohydrolase activity against S1P and dihydrosphingosine 1-phosphate."
  [PMID:12411432 "SPP2 exhibited high phosphohydrolase activity against S1P and dihydrosphingosine 1-phosphate"]
- Substrate specificity (sphingoid-base specific, not a general lipid
  phosphatase): "The dihydrosphingosine-1-phosphate phosphohydrolase activity was
  efficiently inhibited by excess S1P but not by lysophosphatidic acid,
  phosphatidic acid, or glycerol 3-phosphate, indicating that SPP2 is highly
  specific to sphingoid base 1-phosphates."
  [PMID:12411432 "indicating that SPP2 is highly specific to sphingoid base 1-phosphates"]
- UniProt FUNCTION: "Has specific phosphohydrolase activity towards sphingoid base
  1-phosphates. Has high phosphohydrolase activity against
  dihydrosphingosine-1-phosphate and sphingosine-1-phosphate (S1P) in vitro."
  [file:human/SGPP2/SGPP2-uniprot.txt "Has specific phosphohydrolase activity towards sphingoid base"]
- Reactions (UniProt CATALYTIC ACTIVITY): sphinganine 1-phosphate + H2O ->
  sphinganine + phosphate (RHEA:27514); sphing-4-enine 1-phosphate + H2O ->
  sphing-4-enine + phosphate (S1P, RHEA:27518); (4R)-hydroxysphinganine
  1-phosphate + H2O -> (4R)-hydroxysphinganine + phosphate (phyto-S1P,
  RHEA:33067). EC 3.1.3.-.
  [file:human/SGPP2/SGPP2-uniprot.txt "EC=3.1.3.- {ECO:0000269|PubMed:12411432, ECO:0000269|PubMed:27059959}"]
- FADS3 study confirms S1P/dihydro-S1P and also 4,14-sphingadiene-1-phosphate
  dephosphorylation by SPP1/SPP2 in vitro (source of one EXP annotation).
  [PMID:31916624 "SPD is metabolized to ceramides and SPD 1-phosphate with almost the same efficiency as sphingosine"]

Core MF term: **GO:0042392 sphingosine-1-phosphate phosphatase activity**
(verified current label via OLS). Also enables **GO:0070780
dihydrosphingosine-1-phosphate phosphatase activity** (a genuine second
sphingoid-base-1-P activity, kept as non-core).

## Subcellular location

Multipass ER membrane protein. UniProt: "Endoplasmic reticulum membrane ... 
Multi-pass membrane protein." Nine predicted TM helices; three PAP2 phosphatase
sequence motifs (regions 136-144, 163-166, 206-217) with catalytic residues
His166 (proton donor) and His213 (nucleophile).
[file:human/SGPP2/SGPP2-uniprot.txt "Endoplasmic reticulum membrane"]
[PMID:12411432 "SPP2 is localized to the endoplasmic reticulum"]

Reactome models the reaction on the ER membrane facing the cytosol: "SGPP1 and 2
... enzymes associated with the endoplasmic reticulum membrane catalyze the
hydrolysis of cytosolic sphingosine 1-phosphate (S1P), dihydro-S1P, and
phyto-S1P."
[Reactome:R-HSA-428664 "catalyze the hydrolysis of cytosolic sphingosine"]

Location terms: GO:0005789 endoplasmic reticulum membrane (core), GO:0005783
endoplasmic reticulum (parent, IDA).

## Biological role — sphingolipid rheostat / salvage

By dephosphorylating S1P back to sphingosine, SGPP2 opposes sphingosine kinase
and controls the S1P<->sphingosine<->ceramide balance ("sphingolipid rheostat"),
feeding sphingosine into the ceramide salvage/recycling pathway.

- UniProt: "Sphingosine-1-phosphate phosphatase activity is needed for efficient
  recycling of sphingosine into the sphingolipid synthesis pathway ... May play a
  role in attenuating intracellular sphingosine 1-phosphate (S1P) signaling."
  [file:human/SGPP2/SGPP2-uniprot.txt "is needed for efficient recycling of sphingosine into the sphingolipid"]
- Mouse Sgpp2 knockout: "SPPase activity is needed for efficient recycling of
  sphingosine into the sphingolipid synthesis pathway ... reveal a juncture in the
  sphingolipid recycling pathway that could impact the development of diabetes."
  Sgpp2-/- mice have normal skin (unlike Sgpp1-/-), defective adaptive beta-cell
  proliferation, and basal beta-cell ER stress.
  [PMID:27059959 "reveal a juncture in the sphingolipid recycling pathway that could impact the development of diabetes"]
  [PMID:27059959 "they exhibited defective adaptive β-cell proliferation"]
  [PMID:27059959 "β-cells from Sgpp2 −/− mice exhibited markers indicating an elevated basal ER stress response"]

BP terms: GO:0006670 sphingosine metabolic process (IDA, core-adjacent),
GO:0030149 sphingolipid catabolic process (S1P -> sphingosine is the committed
catabolic/salvage step), GO:0046839 phospholipid dephosphorylation (broad IBA
parent). GO:0061469 regulation of type B pancreatic cell proliferation is
supported only by the mouse Sgpp2-/- phenotype and is an organism/context-specific
downstream process (non-core).

## Regulation / induction

SGPP2 is an NF-kB-dependent, inflammation-inducible gene (distinguishing it from
the more constitutive SGPP1). Cached in publications/ (abstract-only,
PMID_17113265.md); title verified via PubMed.

- "expression and activity of S1P phosphatase 2 (SPP2) was found to be highly
  upregulated by inflammatory stimuli in a variety of cells (e.g., neutrophils,
  endothelial cells) ... SPP2 is an NFkappaB-dependent gene ... suggesting a
  pro-inflammatory role of SPP2."
  [PMID:17113265 Mechtcheriakova et al. 2007, Cell Signal; verified via PubMed, https://doi.org/10.1016/j.cellsig.2006.09.004]
- UniProt INDUCTION: "Strongly induced by TNF, also induced by bacterial
  lipopolycaccharides (LPS) in neutrophils, endothelial cells, and other cell
  types. Not induced by growth-related factors."
  [file:human/SGPP2/SGPP2-uniprot.txt "Strongly induced by TNF"]

## Tissue expression

UniProt: "Expressed strongly in kidney and heart, followed by brain, colon, small
intestine and lung." Mouse Sgpp2 mRNA is high in pancreatic islets.
[file:human/SGPP2/SGPP2-uniprot.txt "Expressed strongly in kidney and heart"]
[PMID:27059959 "WT mice expressed Sgpp2 mRNA at high levels in pancreatic islets"]

## Annotation-review summary

- Core MF: GO:0042392 sphingosine-1-phosphate phosphatase activity — multiple
  independent IDA/IMP/EXP/IBA/TAS annotations; ACCEPT the experimental ones, keep
  the redundant electronic/Reactome ones as non-core.
- GO:0070780 dihydrosphingosine-1-phosphate phosphatase activity — real second
  activity (EXP + IEA/RHEA); KEEP_AS_NON_CORE (sphingoid-base-1-P specificity is
  one active site acting on several substrates).
- ER membrane / ER localization — well supported (IDA + IBA + IEA + Reactome
  TAS); ACCEPT the experimental, keep redundant ones.
- BP: sphingosine metabolic process (IDA) ACCEPT as core-adjacent; sphingolipid
  catabolic process (Reactome TAS + ARBA IEA) KEEP_AS_NON_CORE; phospholipid
  dephosphorylation (IBA, over-broad) KEEP_AS_NON_CORE.
- regulation of type B pancreatic cell proliferation (ISS + IEA/Ensembl from
  mouse Sgpp2-/-) — real but organism/context-specific downstream phenotype;
  KEEP_AS_NON_CORE (not the molecular core function).

No REMOVE actions: all experimental annotations are sound; the electronic ones are
biologically defensible (redundant with experimental, not wrong).
