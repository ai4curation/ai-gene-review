# LRAT (Lecithin retinol acyltransferase) — review notes

UniProt: O95237 (LRAT_HUMAN). HGNC:6685. Gene on chromosome 4. 230 aa, 25.7 kDa.
EC 2.3.1.135. Belongs to the H-rev107 (HRASLS/NlpC-P60 thioesterase-like) family.

## Function / catalytic activity

LRAT is the enzyme catalyzing the first committed storage/entry step of retinoid
(vitamin A) metabolism and of the visual (retinoid) cycle. It transfers an acyl
group from the sn-1 position of **phosphatidylcholine (lecithin)** onto
**all-trans-retinol**, producing **all-trans-retinyl esters** (the storage form of
vitamin A and the substrate for the RPE65 isomerohydrolase).

- [file:human/LRAT/LRAT-uniprot.txt "Transfers the acyl group from the sn-1 position of phosphatidylcholine to all-trans retinol, producing all-trans retinyl esters (PubMed:9920938). Retinyl esters are storage forms of vitamin A"]
- [PMID:9920938 "The enzyme responsible for conversion of all-trans-retinol into retinyl esters, the lecithin retinol acyltransferase (LRAT) has been characterized at the molecular level."]
- [PMID:9920938 HPLC of product from LRAT-transfected HEK-293 cells: "[3H]all-trans-retinol into authentic [3H]all-trans-retinyl palmitate"] — confirms all-trans-retinol → retinyl palmitate.
- [PMID:10819989 "The membrane-bound enzyme catalyzes the transfer of an acyl group from the sn-1 position of lecithin to vitamin A to generate retinyl esters."]

EC 2.3.1.135 = phosphatidylcholine--retinol O-acyltransferase. GO:0047173
(phosphatidylcholine-retinol O-acyltransferase activity) is the precise MF term and
its GO definition matches the UniProt/RHEA:17469 reaction exactly. NOTE: the acyl
donor is lecithin (a phospholipid), NOT acyl-CoA; therefore GO:0050252 "retinol
O-fatty-acyltransferase activity" (acyl-CoA + retinol; the ARAT reaction) is a
*different* activity and is NOT annotated to LRAT. Reactome annotates the broader
GO:0016416 "O-palmitoyltransferase activity" (palmitoyl transfer, EC generic);
palmitoyl is one of the acyl groups LRAT transfers, but GO:0016416 is a less
informative sibling of GO:0047173 under GO:0008374 (O-acyltransferase activity).

## Catalytic mechanism (thiol acyltransferase)

LRAT is a **thiol acyltransferase**; Cys161 is the essential catalytic nucleophile
(forms an acyl-thioester intermediate). Cys168 also matters (C168A dead, C168S
active); Cys182/Cys208 are dispensable.
- [PMID:10819989 "The activities of the C161A and C168A mutants are virtually nil."]
- [PMID:10819989 "LRAT is a thiol acyltransferase"]
- [PMID:10819989 "C161 may be the essential nucleophilic residue critical for catalysis."]
- UniProt ACT_SITE annotations: Cys161 "Acyl-thioester intermediate"; His60/Cys72 catalytic (PROSITE PRU01283).

## Localization

Endoplasmic reticulum membrane; single-pass membrane protein. Also rough ER,
endosome/multivesicular body, and perinuclear cytoplasm (by similarity to rodent
orthologs, in hepatic stellate cells and endothelial cells). Topology: cytoplasmic
1-194, TM 195-215, lumenal 216-230.
- [file:human/LRAT/LRAT-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"]
- [file:human/LRAT/LRAT-uniprot.txt "Single-pass membrane protein"]
- [file:human/LRAT/LRAT-uniprot.txt "Endosome, multivesicular body"]

The MVB/perinuclear/rough-ER localizations are ISS/IEA transferred from rat
Q9JI61, based on observations in hepatic stellate cells (retinoid-storing cells)
[PMID:18544127]. ER membrane is the functionally central site for the enzyme.

## Biological role / pathway

- PATHWAY: retinol (vitamin A) metabolism [file:human/LRAT/LRAT-uniprot.txt "PATHWAY: Cofactor metabolism; retinol metabolism."]
- Provides retinyl-ester substrate for RPE65 isomerohydrolase in the RPE → 11-cis-retinal
  chromophore regeneration; critical for vision (visual/retinoid cycle).
- Retinoid storage in liver (hepatic stellate cells) and intestine.
- Reactome: canonical retinoid cycle in rods (R-HSA-2453902); retinoid metabolism and
  transport (R-HSA-975634); defective visual phototransduction due to LRAT loss of
  function (R-HSA-9918442).

## Tissue expression

High in testis and liver, then RPE, small intestine, prostate, pancreas, colon; low
in brain. In liver localizes to hepatic stellate cells and endothelial cells.
- [file:human/LRAT/LRAT-uniprot.txt "Found at high levels in testis and liver, followed by"]
- [file:human/LRAT/LRAT-uniprot.txt "retinal pigment epithelium, small intestine, prostate, pancreas and"]

## Disease

Biallelic LRAT loss-of-function variants cause **Leber congenital amaurosis 14
(LCA14, MIM:613341)** / early-onset severe retinal dystrophy / retinitis pigmentosa.
- [file:human/LRAT/LRAT-uniprot.txt "Leber congenital amaurosis 14 (LCA14)"]
- Variants: S175R (LCA14, loss of function; PMID:11381255), P173L (PMID:17011878).
- LCA14 / RP references: PMID:11381255, PMID:17011878, PMID:18055821.

## Interactions

HuRI binary interactome (PMID:32296183) reports LRAT interacting with BLCAP
(P62952), HSD17B13 (Q7Z5P4), TMX2 (Q9Y320) (also NME2P1 in UniProt IntAct block).
These are large-scale Y2H/binary-map "protein binding" (GO:0005515) IPI hits with no
functional characterization; TMX2 is an ER thioredoxin-related membrane protein and
HSD17B13 an ER lipid-droplet enzyme, so co-ER-membrane residence is plausible, but
none establish a specific molecular function. Treated as non-informative
over-annotations (never removed, per policy).

## Annotation review summary

Core MF: **GO:0047173 phosphatidylcholine-retinol O-acyltransferase activity**
(experimental IDA PMID:10819989; IBA; ARBA IEA; Reactome TAS) — ACCEPT.
Core BP: **GO:0042572 retinol metabolic process** and the broader **GO:0001523
retinoid metabolic process** / **GO:0006776 vitamin A metabolic process**; visual
role captured biologically (RPE65 substrate provision).
Core CC: **GO:0005789 endoplasmic reticulum membrane**.

Over-annotations kept but down-weighted: GO:0016416 O-palmitoyltransferase (generic
Reactome), GO:0016746 acyltransferase (generic PINC TAS), GO:0005515 protein binding
(HuRI IPI x3), retinol/retinoic-acid binding (Ensembl IEA — LRAT handles retinol as
substrate/product but is not primarily a soluble retinoid-binding transport protein),
multivesicular body / perinuclear region / rough ER (ISS/IEA from rodent stellate-cell
data — non-core relative to ER membrane).
