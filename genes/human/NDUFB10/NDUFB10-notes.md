# NDUFB10 (PDSW) — gene review notes

## Identity and family

- UniProt **O96000** (NDUBA_HUMAN); HGNC:7696; gene **NDUFB10** (aliases PDSW, "Complex I-PDSW", "NADH-ubiquinone oxidoreductase PDSW subunit"). 172 aa, ~20.8 kDa. [file:human/NDUFB10/NDUFB10-uniprot.txt "RecName: Full=NADH dehydrogenase [ubiquinone] 1 beta subcomplex subunit 10"; "AltName: Full=Complex I-PDSW"]
- Belongs to the "complex I NDUFB10 subunit family". [file:human/NDUFB10/NDUFB10-uniprot.txt "SIMILARITY: Belongs to the complex I NDUFB10 subunit family."]
- One of the 45 subunits of human mitochondrial respiratory chain Complex I (NADH:ubiquinone oxidoreductase). [file:human/NDUFB10/NDUFB10-uniprot.txt "SUBUNIT: Complex I is composed of 45 different subunits"]

## Core biology: accessory (supernumerary) subunit, non-catalytic

- NDUFB10 is an **accessory subunit**, NOT one of the 14 conserved catalytic core subunits. Bacterial and human complex I share 14 core subunits that are essential for enzymatic function; the remaining 31 human accessory subunits (including NDUFB10) have roles in assembly/stability. [PMID:27626371 "Bacterial and human complex I share 14 core subunits that are essential for enzymatic function; however, the role and necessity of the remaining 31 human accessory subunits is unclear."]
- It resides in the **membrane arm**, specifically the distal P_D domain (the "hydrophobic protein / HP fraction"). [PMID:28040730 "which encodes an accessory subunit located within the PD part of complex I"] [PMID:9878551 "all located within the hydrophobic protein (HP) fraction of complex I"]
- Structurally NDUFB10 lies **parallel to the membrane on the IMS face spanning ND4 and ND5** (i.e., not transmembrane; the bovine homolog is PDSW). [PMID:28040730 "the bovine homolog PDSW of human NDUFB10 appears to be located parallel to the membrane on the IMS face spanning ND4 and ND5"] [PMID:28040730 "In contrast to most PD accessory subunits, it does not contain a transmembrane domain"]
- UniProt FUNCTION: "Accessory subunit that is involved in the functional assembly of the mitochondrial respiratory chain complex I." The NADH dehydrogenase activity is a property of the *complex*, not of NDUFB10 itself. [file:human/NDUFB10/NDUFB10-uniprot.txt "FUNCTION: Accessory subunit that is involved in the functional assembly"; "Complex I has an NADH"]

## Assembly role and disease

- Loss of NDUFB10 (and most accessory subunits) reduces the amount of fully assembled complex I. [PMID:28040730 "Knockdown of most accessory subunits, including NDUFB10, in HEK293T cells resulted in decrease in fully assembled complex I"]
- Human biallelic NDUFB10 mutations cause **isolated complex I deficiency (MC1DN35, MIM:619003)**: an infant with fatal infantile lactic acidosis and cardiomyopathy; compound heterozygous mutations (a premature stop → absent protein, and C107S). [PMID:28040730 "An infant presented with fatal infantile lactic acidosis and cardiomyopathy, and was found to have profoundly decreased activity of respiratory chain complex I"] [file:human/NDUFB10/NDUFB10-uniprot.txt "DISEASE: Mitochondrial complex I deficiency, nuclear type 35 (MC1DN35)"]
- Disruption disrupts the assembly of the membrane arm; assembly stalls at a late (~830 kDa) stage. [PMID:28040730 "resulting in the perturbed assembly of the holoenzyme at the 830 kDa stage"] [PMID:28040730 "NDUFB10 is important for the assembly of complex I at the late stage where the PD domain is being assembled"]

## Twin-CX9C / MIA40 (CHCHD4) import

- NDUFB10 is imported into the mitochondrial IMS by the disulfide-relay oxidoreductase **CHCHD4/MIA40**; it transiently interacts with CHCHD4 and acquires intramolecular disulfide bonds. [PMID:28040730 "NDUFB10 was identified together with three other complex I subunits as a substrate of the intermembrane space oxidoreductase CHCHD4 (also known as Mia40)"] [PMID:28040730 "during its mitochondrial import and maturation NDUFB10 transiently interacts with CHCHD4 and acquires disulfide bonds"]
- The disulfide bonds are required for folding, import, and function in complex I assembly. [file:human/NDUFB10/NDUFB10-uniprot.txt "PTM: The formation of intramolecular disulfide bonds is assisted by"]
- The C107S disease variant impairs CHCHD4-mediated oxidation → protein stays in cytosol / is degraded → loss of function. [PMID:28040730 "NDUFB10 C107S localized largely to the cytosol, while the wild type protein was completely localized to mitochondria"]
- The GOA-recorded interactor for the PMID:28040730 IPI (UniProtKB:Q8N4Q1) is CHCHD4/MIA40 — a biologically meaningful, function-relevant interaction (the import/oxidoreductase partner). Distinct from the many high-throughput "protein binding" hits.

## Localization

- Mitochondrion inner membrane; peripheral membrane protein; matrix side (UniProt). Present in curated ComplexPortal CPX-577 (Mitochondrial respiratory chain complex I). [file:human/NDUFB10/NDUFB10-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion inner membrane"]
- Identified as a genuine complex I subunit by immunopurification + MS of the human enzyme. [PMID:12611891 "we can resolve and identify the human homologues of 42 polypeptides"]
- Confirmed subunit in cryo-EM megacomplex (PMID:28844695) and multiple PDB structures (5XTC, 9CWT, 9I4I, etc.). [file:human/NDUFB10/NDUFB10-uniprot.txt "PDB; 9CWT; EM"]

## Interaction (protein binding IPI) annotations — assessment

The GOA "protein binding" (GO:0005515) IPI annotations mostly come from large-scale interactome / neurodegeneration-screen datasets in which NDUFB10 appears as one of many prey/bait, and do NOT establish a specific NDUFB10 molecular function:
- PMID:17500595 — Huntingtin interacting proteins are genetic modifiers of neurodegeneration (HTT screen). Not NDUFB10-specific function.
- PMID:25416956 — proteome-scale human interactome (Rolland et al., HI-II-14). High-throughput Y2H.
- PMID:32296183 — reference human binary interactome (HuRI). High-throughput Y2H.
- PMID:32814053 — neurodegenerative-disease interactome map (aggregation-focused). High-throughput.
- PMID:14557246 (AIP/Tom20 study) — here NDUFB10 is used as a control mitochondrial preprotein that binds the import receptors Tom20 and Tom22 in vitro. [PMID:14557246 "other mitochondrial preproteins, ATP/ADP carrier protein and NDUFB10, which lack a cleavable presequence, also bound to AIP as well as to Tom20."] This is a real import-machinery interaction but still contributes an uninformative bare "protein binding" term.
- PMID:28040730 IPI (with Q8N4Q1 = CHCHD4/MIA40) is the one functionally meaningful interaction (import/oxidoreductase partner); still a bare "protein binding" term.

Per curation policy, none of these experimental IPI annotations is REMOVED; all bare GO:0005515 terms are marked over-annotated (uninformative), with the biology captured instead in `core_functions` and BP terms.

## Curation conclusions

- Honest molecular function = **structural molecule activity (GO:0005198)** — NDUFB10 contributes to the structural integrity of complex I; it is non-catalytic.
- It **contributes_to** the complex-level **NADH dehydrogenase (ubiquinone) activity (GO:0008137)** but does NOT directly enable it. The GOA `enables GO:0008137` (NAS, PMID:9878551) is an over-annotation of a complex-level activity to a single accessory subunit.
- Core BP: **mitochondrial respiratory chain complex I assembly (GO:0032981)** and participation in **mitochondrial electron transport, NADH to ubiquinone (GO:0006120)**.
- Core CC: **respiratory chain complex I (GO:0045271)** (part_of), located in mitochondrial inner membrane (GO:0005743).
- The IEA `involved_in proton transmembrane transport (GO:1902600)` (inferred logically from the complex-level GO:0008137) and NAS `proton motive force-driven mitochondrial ATP synthesis (GO:0042776)` over-attribute complex-level / downstream OXPHOS activities to this accessory subunit; kept as non-core / over-annotated rather than as direct functions.
