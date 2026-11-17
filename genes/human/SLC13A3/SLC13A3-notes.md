# SLC13A3 (NaDC3 / NaC3) curation notes

UniProt: Q8WWT9 (S13A3_HUMAN), 602 aa, chromosome 20. HGNC:14430.
Gene synonyms: NADC3, SDCT2. TC 2.A.47.1.15 (DASS / divalent anion:Na+ symporter family), SLC13A/DASS, NADC subfamily.

## Gene identity and family

SLC13A3 encodes the Na(+)/dicarboxylate cotransporter 3 (NaDC3, also NaC3, SDCT2), a
plasma-membrane secondary-active transporter of the SLC13 (DASS) family. It is a close
paralog of SLC13A2 (NaDC1, low-affinity dicarboxylate, apical/renal), SLC13A5 (NaCT,
citrate-preferring, liver/brain), and the sulfate transporters SLC13A1/SLC13A4; the family
is related to the *Drosophila* longevity gene *Indy* (I'm Not Dead Yet). NaDC3 is the
*high-affinity* member for di- and tricarboxylates.

[file:human/SLC13A3/SLC13A3-uniprot.txt CC:SIMILARITY "Belongs to the SLC13A/DASS transporter (TC 2.A.47) family"]

## Molecular function: high-affinity Na+-coupled di/tricarboxylate symport

Electrogenic Na+-coupled symporter: imports 4–6-carbon di- and tricarboxylates with a
probable stoichiometry of 3 Na+ : 1 divalent dicarboxylate.

[file:human/SLC13A3/SLC13A3-uniprot.txt CC:FUNCTION "High-affinity sodium-dicarboxylate cotransporter that accepts a range of substrates with 4-6 carbon atoms, such as the citric acid cycle intermediates succinate and alpha-ketoglutarate (2-oxoglutarate), as well as other compounds including N-acetyl-L-aspartate"]
[file:human/SLC13A3/SLC13A3-uniprot.txt CC:FUNCTION "Transports the dicarboxylate into the cell with a probable stoichiometry of 3 Na(+) for 1 divalent dicarboxylate, rendering the process electrogenic"]
[Reactome:R-HSA-433101 "Kinetic studies in human retinal pigment epithelial (HRPE) cells suggest three sodium ions co-transported with every divalent succinate"]

Substrates (UniProt catalytic-activity + kinetics): succinate (KM 25–112 uM), 2-oxoglutarate/
alpha-ketoglutarate (KM 45–149 uM), N-acetyl-L-aspartate (KM 220 uM), glutarate (KM 40 uM),
fumarate, malate, dimethylsuccinates, itaconate, and the low-affinity substrate glutathione
(KM 1.65 mM). Citrate is transported in its divalent form only.

[file:human/SLC13A3/SLC13A3-uniprot.txt CC:FUNCTION "Can transport citrate in a Na(+)-dependent manner, recognizing the divalent form of citrate rather than the trivalent form which is normally found in blood"]

Cryo-EM structures (PDB 8UVC–8UVI) show a homodimer using an elevator-type mechanism; SNT
motifs and a TXP motif form the substrate site.

[file:human/SLC13A3/SLC13A3-uniprot.txt CC:SUBUNIT "Homodimer; the dimer shifts between outward and inward conformations to generate an elevator-type movement for substrate transport"]

Glutathione is a genuine but *low-affinity* substrate (secondary activity, not core):
[PMID:24247155 "At -60 mV, GSH currents showed saturation kinetics with a KM of 1.65 mM"]
[PMID:24247155 "The kinetic data show that NaDC3 is a low-affinity GSH transporter"]

D-/L-2-hydroxyglutarate are NaDC3 substrates (relevant to organic acidurias), distinguishing
NaDC3 from the citrate-preferring neuronal NaCT/SLC13A5:
[PMID:21264516 "D- and L-2OHGA, but not 3OHGA, showed affinities to NaDC3, indicating that D- and L-2OHGA impair the uptake of dicarboxylates into astrocytes thereby possibly interfering with their feeding of tricarboxylic acid cycle intermediates to neurons"]

## Localization: basolateral plasma membrane

Multi-pass plasma-membrane protein; in kidney it is on the *basolateral* membrane of
proximal tubule cells (step 1 of renal organic-anion secretion, upstream of OAT1-3).

[file:human/SLC13A3/SLC13A3-uniprot.txt CC:SUBCELLULAR_LOCATION "Cell membrane"]
[PMID:27053689 "NaDC3-related immunostaining was detected in the BLM of proximal tubules"]
[Reactome:R-HSA-433101 "NaDC3 is expressed in the basolateral membrane of renal proximal tubular epithelial cells, sinusoidal membrane of hepatocytes, and brain synaptosomes"]
[PMID:24247155 "hNaDC3 present at the basolateral membrane of proximal tubule cells mediates sodium-dependent GSH uptake"]

Detected in urinary exosomes (shed membrane vesicles) by proteomics [PMID:19056867].

## Tissue expression and physiology

Highest in kidney; also placenta, brain (astrocytes, choroid plexus), liver, pancreas.
[file:human/SLC13A3/SLC13A3-uniprot.txt CC:TISSUE_SPECIFICITY "Expression is highest in kidney"]
[PMID:30635937 "SLC13A3 is mainly expressed in kidney, in astrocytes, and in the choroid plexus"]

Supplies TCA-cycle intermediates (succinate, αKG) to cells; in brain, clears/handles NAA and
dicarboxylates. In hepatocytes, imports itaconate to drive TFEB-dependent lysosomal biogenesis
in antibacterial innate immunity [PMID:39116875, from UniProt].

## Disease

Biallelic SLC13A3 variants cause ARLIAK (acute reversible leukoencephalopathy with increased
urinary alpha-ketoglutarate; MIM:618384). Variants A254D and G548S abolish/severely reduce
transport.
[PMID:30635937 "the missense mutations caused a marked reduction in the capacity to transport αKG, succinate, and NAA"]

## Curation decisions summary

- Core MF: GO:0015362 high-affinity sodium:dicarboxylate symporter activity (and the
  substrate-named GO:0017153, GO:0005310, GO:0015139, GO:0015141 all ACCEPT as reinforcing).
- Citrate (GO:0015137 / GO:0015746) and glutathione (GO:0034634 / GO:0034775) activities are
  genuine but secondary → KEEP_AS_NON_CORE.
- 9x GO:0005515 protein binding (PMID:32296183 HuRI binary interactome) → REMOVE per
  protein-binding policy (uninformative; HuRI Y2H interactors ARL13B, CISD2, CREB3L1, CYB5R3,
  ERGIC3, FAM209A, GPX8, LEUTX, RMDN3).
- Bare/generic terms entailed by specific ones asserted here → TOO_GENERAL: GO:0016020 membrane,
  GO:0022857 transmembrane transporter activity, GO:0055085 transmembrane transport (x2),
  GO:0015370 solute:sodium symporter activity.
- Plasma membrane (GO:0005886) and basolateral plasma membrane (GO:0016323) ACCEPT.
- Sodium ion transmembrane transport (GO:0035725): coupled Na+ movement, true but peripheral →
  KEEP_AS_NON_CORE.
- extracellular exosome (GO:0070062) KEEP_AS_NON_CORE (urinary-exosome proteomics).
- transport across blood-brain barrier (GO:0150104, NAS, general BBB review): peripheral and
  weakly supported → KEEP_AS_NON_CORE.
- No GO term exists for N-acetyl-L-aspartate transmembrane transporter activity (confirmed
  absent via OLS) → proposed_new_terms entry.
