# SLC26A3 (DRA, "Down-Regulated in Adenoma") — curation notes

UniProt: P40879 (S26A3_HUMAN), 764 aa. HGNC:3018. Taxon: Homo sapiens (9606).

## Identity and core function

SLC26A3 is the apical (brush-border) plasma-membrane Cl-/HCO3- anion exchanger of
the intestinal epithelium, the principal luminal Cl- absorption / HCO3- secretion
transporter of the ileum and colon. It is a member of the SLC26/SulP (sulfate
permease) secondary-active transporter family with a SulP transmembrane domain plus a
cytoplasmic STAS domain.

- Family / fold: [file:human/SLC26A3/SLC26A3-uniprot.txt CC:SIMILARITY, "Belongs to the SLC26A/SulP transporter (TC 2.A.53) family."]. UniProt FT: SulP TM domain (TRANSMEM helices 77-490), STAS domain 525-720, C-terminal PDZ-binding motif 761-764 (ETKF).
- Core transport: electrogenic coupled 2 Cl- / 1 HCO3- exchange. [PMID:16606687 "slc26a3 mediates a coupled 2Cl-/1HCO3- exchanger."] and UniProt catalytic activity [file:human/SLC26A3/SLC26A3-uniprot.txt CC:FUNCTION, "stoichiometry of 2:1 in the intestinal epithelia"]. Rhea RHEA:72203: hydrogencarbonate(in) + 2 chloride(out) = hydrogencarbonate(out) + 2 chloride(in).
- Activity regulation: inhibited by low intracellular pH [PMID:19321737 "Cl(-)/HCO(3)(-) exchange was steeply inhibited with pH(i) decrease between 7.3 and 6.8"]; UniProt [file:human/SLC26A3/SLC26A3-uniprot.txt CC:ACTIVITY REGULATION "Inhibited by acidic pH."]. Functionally couples with NHE3 (electroneutral NaCl absorption) via indirect pHi linkage [PMID:19321737 "Electroneutral NaCl absorption in the intestine is mediated by functional coupling of the Na(+)/H(+) exchanger and Cl(-)/HCO(3)(-) exchanger."].

## Localization

- Apical/brush-border membrane of enterocytes [PMID:22159084 "the mature glycosylated form of SLC26A3 exists at the plasma membrane"; file:human/SLC26A3/SLC26A3-uniprot.txt CC:SUBCELLULAR LOCATION "Apical cell membrane"]. Colocalizes with NHE3 and E3KARP/NHERF2 in the apical compartment of human proximal colon [PMID:12369822 "Immunofluorescence colocalizes dra, NHE3, and E3KARP in the apical compartment of human proximal colon."].
- Multi-pass membrane protein (14 TM helices per UniProt topology). N-glycosylated at N153/N161/N165 in the large extracellular loop; glycosylation needed for efficient surface expression and protease protection [PMID:22159084].

## Protein interactions (PDZ-motif / STAS)

SLC26A3 has a C-terminal class I PDZ-binding motif (…ETKF, 761-764). Deleting 761-764
abolishes NHERF4 binding [file:human/SLC26A3/SLC26A3-uniprot.txt FT MUTAGEN 761..764].

- Binds the second PDZ domain of NHERF2 / E3KARP [PMID:12369822 "In vitro the ETKF motif of dra binds to the second PDZ domain of E3KARP, the affinity being comparable to that of the known ligand CFTR."].
- Binds the third PDZ domain of NHERF4; this internalizes SLC26A3 and reduces exchange activity [PMID:22627094 "A direct protein-protein interaction was identified between the PDZ-binding motif of SLC26A3 and the third PDZ domain of NHERF4."; "Interaction with NHERF4 decreased the level of SLC26A3 expression on the plasma membrane, which led to reduced SLC26A3 anion exchange activity."].
- Binds PDZK1/CAP70 [file:human/SLC26A3/SLC26A3-uniprot.txt CC:SUBUNIT "Interacts with PDZK1"]. By similarity interacts with CFTR, SLC26A6, NHERF1.
- Large-scale PDZ-fragmentomics affinity map (PMID:36115835) recovers binding to a panel of PDZ-domain scaffolds (NHERF2, NHERF4, PDZK1, DLG3/4, GRIP1/2, GRID2IP, MPDZ, PATJ, SCRIB, TJP1/ZO-1, WHRN, MAGI1/2, LNX1/2, FRMPD2, IL16, APBA2). These are all PDZ-domain interactions mediated by the SLC26A3 C-terminal motif — consistent with GO:0030165 PDZ domain binding, not generic protein binding.

All of the GO:0005515 "protein binding" rows (PMID:12369822, PMID:22627094,
PMID:36115835 x20) are bare, uninformative protein-binding IPIs; per project policy they
are REMOVEd and replaced by a single informative NEW GO:0030165 (PDZ domain binding) row.

## Other substrates (SLC26/SulP family functions)

The SLC26/SulP family transports sulfate, oxalate, and other anions. SLC26A3's
dominant physiological activity is Cl-/HCO3- exchange; oxalate transport is a
secondary activity with direct gene-specific evidence: Slc26a3-knockout mice lose
intestinal oxalate absorption and show a 66% fall in urinary oxalate
[PMID:23886857 "DRA mediates a predominance of the apical uptake of oxalate and Cl(-) absorbed in the small and large intestine of mice"].
Kept as non-core: GO:0019531 oxalate transmembrane transporter, GO:0019532 oxalate
transport.
Sulfate is NOT a SLC26A3 substrate: P40879 is not an IBD seed at the sulfate nodes
(PTN000212046 / PTN000929279), UniProt FUNCTION is silent on sulfate, and the early
DRA "sulfate transporter" characterization is contested. The sulfate rows
GO:0008271, GO:0015116, GO:1902358 (IBA+IEA) are REMOVEd, the IBA rows with a
propagation_review (FUNCTIONAL_DIVERGENCE); the dedicated family sulfate transporters
are SLC26A1/A2.

## Disease

Loss-of-function variants cause congenital chloride diarrhea (DIAR1 / CLD, MIM:214700):
voluminous watery chloride-rich stools [PMID:9554749 "An inherited defect in intestinal
anion exchange, congenital chloride diarrhea (CLD), was recently shown to be caused by
mutations in the down-regulated in adenoma (DRA) gene."]. Named DRA because colonic
expression is lost in adenomas/adenocarcinomas [file:human/SLC26A3/SLC26A3-uniprot.txt
CC:TISSUE SPECIFICITY "Expression is significantly decreased in adenomas"].

## Sperm / mouse-derived (By similarity, GO_REF:0000107 IEA / GO_REF:0000024 ISS from Q9WVC8)

Mouse slc26a3 (Q9WVC8) annotations propagated to human: sperm capacitation
(GO:0048240), sperm midpiece (GO:0097225), intracellular pH elevation (GO:0051454),
membrane hyperpolarization (GO:0060081), cellular response to cAMP (GO:0071320). UniProt
records a By-similarity role in sperm Cl-/HCO3- homeostasis and midpiece localization.
These are kept as non-core (peripheral to the intestinal transport core function, and
inferred from the mouse ortholog).

## Action summary

- Core MF: GO:0140900 chloride:bicarbonate antiporter activity (2Cl-/1HCO3-). ACCEPT (IDA x4, IBA, IEA).
- Substrate-named MF (Cl, HCO3): ACCEPT/core. Oxalate MF/BP: KEEP_AS_NON_CORE. Sulfate MF/BP: REMOVE (P40879 not an IBD seed at the sulfate nodes; propagation_review FUNCTIONAL_DIVERGENCE).
- GO:0005452 (solute:inorganic anion antiporter, Reactome TAS x2): MODIFY -> GO:0140900 (already carried; Reactome reaction is the Cl-/HCO3- exchange).
- Locations: plasma membrane (ACCEPT), apical PM (ACCEPT), brush border (ACCEPT); bare GO:0016020 membrane (IEA/ISS) -> TOO_GENERAL.
- Generic BP: GO:0006820 monoatomic anion transport, GO:0055085 transmembrane transport -> TOO_GENERAL (specific Cl/HCO3 transport asserted elsewhere).
- GO:0015701 bicarbonate transport, GO:1902476 chloride transmembrane transport -> ACCEPT (core).
- All GO:0005515 protein binding -> REMOVE; NEW GO:0030165 PDZ domain binding (IPI).
