# ACVRL1 notes

Manual synthesis for the BMP9 GO-CAM review of `600ced8500002343`, using the
cached primary publications, the UniProt entry, and the BMP9 GO-CAM as context.

## Core receptor function

ACVRL1 encodes ALK1, a single-pass type I receptor serine/threonine kinase. Its
best established ligand context is endothelial BMP9/BMP10 signaling. BMP9
induces SMAD1/5/8 phosphorylation and a BMP-responsive ID1 reporter in
microvascular endothelial cells; the response is abolished by ALK1 silencing or
by soluble ALK1 extracellular domain, and BMP10 is likewise a potent ALK1 ligand
[PMID:17068149, "BMP9 and BMP10 are two specific ALK1 ligands"]. A structural
and kinetic study directly resolved mature BMP9 bound by the extracellular
domains of ALK1 and ACVR2B/ActRIIB [PMID:22718755, "crystal structure of a fully
assembled ternary complex of BMP9 with the extracellular domains of ALK1 and
ActRIIB"]. In human pulmonary artery endothelial cells, BMP9 signals through ALK1
with either BMPR-II or ActR-II type II receptors to activate SMAD1/5 and SMAD2
and to induce ID transcripts [PMID:19366699, "the type I receptor, ALK1, is
essential for these responses"].

The 1993 Attisano paper cloned the human TSR-I receptor, now ACVRL1/ALK1, in the
era before BMP9 was identified as its high-affinity physiological ligand
[PMID:8242742]. That work supports ALK1 as a type I transmembrane
serine/threonine kinase receptor in a TGF-beta-superfamily heteromeric complex,
but it is weaker and historically noisier evidence for the BMP9 state than the
later ligand and structure papers.

Human HHT2 variant assays are also consistent with a core cell-surface BMP9
receptor role: wild-type ALK1 localizes predominantly at the plasma membrane and
many pathogenic ACVRL1 missense variants either fail to respond to BMP9 or are
retained in the endoplasmic reticulum [PMID:26176610, "Wild type ALK1 is
predominantly present at the plasma membrane"].

## Contextual outputs

The vascular and lymphatic annotations are mostly consequences of ALK1/BMP9 or
ALK1/TGF-beta signaling in particular endothelial systems. BMP9 can suppress
microvascular endothelial migration and growth [PMID:17068149], suppress HPAEC
proliferation through ALK1 and BMPR-II [PMID:19366699], or promote endothelial
proliferation and angiogenesis in the allantois and tumor xenograft settings
[PMID:20406889]. Because the direction depends strongly on endothelial state and
assay context, proliferation, differentiation, and angiogenesis rows are retained
as contextual rather than treated as the molecular core of ACVRL1.

Postnatal lymphatic phenotypes are supported by ALK1 pathway blockade in mice
and by ligand responsiveness of lymphatic endothelial cells [PMID:19903896,
"Blockade of ALK1 signaling results in defective lymphatic development"].
Likewise, chondrocyte MMP-13 induction in osteoarthritis models and colon
epithelial differentiation in BMP9-treated human colonic monolayers are
supported, but they are not the receptor's defining cell-surface activity.

The Crohn's disease colonic epithelial study supports BMP9-ALK1 effects on
colonocyte differentiation and Notch target expression. It also reports increased
tight-junction transcripts and TEER after BMP9, but those endpoints do not by
themselves distinguish tight-junction assembly from maintenance or barrier
function; the matching GDF2 review left `GO:1903348 positive regulation of
bicellular tight junction assembly` unresolved, and this ACVRL1 review follows
that judgment.

## Interaction rows

The BMP10 and BMP9 `GO:0005515 protein binding` rows can be refined to
`GO:0036122 BMP binding`. Other `GO:0005515` rows name AP-MS partners, accessory
proteins, or generic interactors and are removed under the project policy for
bare protein binding. CK2beta/CSNK2B is a real ALK1 interactor that enhances
ALK1-mediated signaling [PMID:19592636, "CK2beta enhanced the ability of
activated or ligand-stimulated ALK-1 to inhibit endothelial cell migration"],
but CSNK2B is the regulatory subunit of protein kinase CK2 rather than a protein
kinase, so its rows do not support `GO:0019901 protein kinase binding`.

## BMP9 GO-CAM consistency

The BMP9 GO-CAM activity `gomodel:600ced8500002343/600ced8500002350` correctly
uses ACVRL1/ALK1 as the type I receptor for BMP9 signaling at the plasma
membrane. Its molecular function is currently `GO:0016361 activin receptor
activity, type I`. That term is legacy-compatible with some ALK1 biology, but it
does not name the BMP9-bound receptor state depicted in this model. The activity
should use `GO:0098821 BMP receptor activity`, supported by the BMP9/BMP10
functional receptor work and by the BMP9-ALK1-ActRIIB ternary structure.
