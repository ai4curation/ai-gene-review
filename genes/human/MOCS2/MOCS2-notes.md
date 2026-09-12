# MOCS2 (human) — gene review notes

UniProt: O96007 (MOC2B_HUMAN, "Molybdopterin synthase catalytic subunit"). HGNC:7193. Gene ID 4338.

## Gene architecture: bicistronic

MOCS2 is a **bicistronic gene** producing two proteins from overlapping reading frames:
- **MOCS2A** (small subunit; UniProt O96033) — a ubiquitin-like sulfur-carrier protein whose C-terminal thiocarboxylate (Gly-Gly → Gly-aminoethanethioate) delivers sulfur.
- **MOCS2B** (large / catalytic subunit; UniProt O96007, this entry) — the MoaE-family catalytic subunit.

[file:human/MOCS2/MOCS2-uniprot.txt "This protein is produced by a bicistronic gene which also produces the small subunit (MOCS2A) from an overlapping reading frame. Expression of these 2 proteins are related since a mutation that removes the start codon of the small subunit (MOCS2A) also impairs expression of the large subunit (MOCS2B)."]

First reported as a bicistronic transcript with overlapping reading frames by Stallmeyer et al. [PMID:10053003] and Sloan et al. [PMID:9889283].

## Core molecular function: molybdopterin synthase (EC 2.8.1.12)

MOCS2B is the **catalytic subunit of the molybdopterin (MPT) synthase complex**, which catalyses the **second step of molybdenum cofactor (MoCo) biosynthesis**: conversion of cyclic pyranopterin monophosphate (cPMP / precursor Z / compound Z) to molybdopterin (MPT) by insertion of two sulfur atoms into the pterin to form the dithiolene group that chelates molybdenum.

[file:human/MOCS2/MOCS2-uniprot.txt "Catalytic subunit of the molybdopterin synthase complex, a complex that catalyzes the conversion of precursor Z into molybdopterin. Acts by mediating the incorporation of 2 sulfur atoms from thiocarboxylated MOCS2A into precursor Z to generate a dithiolene group"]

- GO MF: **GO:0030366 molybdopterin synthase activity** ("Catalysis of the conversion of precursor Z to molybdopterin, the final step in molybdopterin biosynthesis." — OLS/go.db).
- EC 2.8.1.12; RHEA:26333.
- The sulfur is delivered as a C-terminal thiocarboxylate on the small subunit MOCS2A [PMID:12732628 "The sulfur used for the formation of the dithiolene group of MPT exists in the form of a thiocarboxylate group at the C terminus of the smaller subunit of MPT synthase."].

Mechanistic / catalytic characterization: Leimkuhler et al. [PMID:12732628 "MOCS2A and MOCS2B were purified after heterologous expression in E. coli, and the separately purified subunits readily assemble into a functional MPT synthase tetramer."] — this paper also mapped disease mutations: MOCS2A-V7F weakens the MOCS2A–MOCS2B interaction; MOCS2B-E168K attenuates binding of precursor Z [PMID:12732628 "a MOCS2B-E168K mutation identified in a severely affected patient attenuates binding of precursor Z."].

Physiological role of the upstream sulfurtransferase (MOCS3) that charges MOCS2A: Matthies et al. [PMID:15073332 "the sulfurated form of MOCS3-RLD was able to provide the sulfur for the thiocarboxylation of MOCS2A, the small MPT synthase subunit in humans."]. Same paper establishes cytosolic localization [PMID:15073332 "MOCS3 in addition to the subunits of MPT synthase are localized in the cytosol."].

Edwards et al. [PMID:25709896] provide human-recombinant functional data: WT MOCS2B binds MOCS2A (Kd = 0.36 μM) and supports MPT synthesis; the disease mutant MOCS2B-S140F disrupts complex assembly and abolishes activity [PMID:25709896 "While WT MOCS2B showed an effective MPT synthesis (determined by the oxidation product FormA, Fig. 2E), MOCS2B-S140F was only able to produce low levels of MPT at high concentrations of MOCS2A."]. This paper is the basis for the recent IDA MF/BP/CC annotations (2025 dates in GOA).

## Complex / subunit composition

**Heterotetramer**: (MOCS2A)2(MOCS2B)2. [file:human/MOCS2/MOCS2-uniprot.txt "Heterotetramer; composed of 2 small (MOCS2A) and 2 large (MOCS2B) subunits"] — homologous to E. coli MoaD (small) / MoaE (large). GO CC: **GO:1990140 molybdopterin synthase complex** (ComplexPortal CPX-6341).

MOCS2B ↔ MOCS2A interaction confirmed by ITC and biochemistry [PMID:25709896], and reported in the mutation-mapping papers [PMID:12732628], [PMID:16021469 "The mutation was expressed in vitro and was found to abolish the binding affinities of the large subunit of molybdopterin synthase (MOCS2B) for both precursor Z and the small subunit of molybdopterin synthase (MOCS2A)."]. The GOA "protein binding" (GO:0005515) IPI entries against MOCS2A (O96033) capture this same subunit–subunit interaction; the specific, informative representation is the molybdopterin synthase complex CC + molybdopterin synthase activity MF, so the bare "protein binding" entries are best marked as over-annotations.

## Location

**Cytosol** (GO:0005829), with the whole MPT synthase machinery localized there [PMID:15073332 "MOCS3 in addition to the subunits of MPT synthase are localized in the cytosol."]. HPA IDA and PMID:26705305 IDA also support cytosol. A **nucleus** annotation (GO:0005634) comes from PMID:26705305 (IDA) and UniProt-SubCell IEA; the UniProt record lists Nucleus as a secondary location, tied to the moonlighting PKR/ATAC role.

## Moonlighting role (PKR/ATAC — non-core)

Suganuma et al. [PMID:26705305] report that human MPT synthase plus the ATAC acetyltransferase complex bind and inhibit the stress kinase PKR (EIF2AK2), suppressing eIF2α/JNK phosphorylation and thereby promoting translation initiation of iron-responsive mRNAs [PMID:26705305 "MPT synthase and ATAC directly interacted with PKR and suppressed latent autophosphorylation of PKR and its downstream phosphorylation of JNK and eukaryotic initiation factor 2α (eIF2α)."]. This underlies:
- GO:0009968 negative regulation of signal transduction (IDA) — a real but secondary/moonlighting activity, keep as non-core.
- GO:0005515 protein binding IPI vs EIF2AK2/PKR (Q9NS73) and MBIP.
- GO:0005634 nucleus (IDA).

These are genuine experimental findings but are not the canonical MoCo-biosynthesis core function; treat as KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED (for the bare "protein binding").

## Disease

**Molybdenum cofactor deficiency, type B / B1 (MOCODB1; MIM 252160)** — autosomal recessive; neonatal intractable seizures, opisthotonus, facial dysmorphism, hypouricemia, elevated urinary sulfite / S-sulfocysteine; severe neurologic damage, often lethal in early childhood. [file:human/MOCS2/MOCS2-uniprot.txt "Molybdenum cofactor deficiency, type B1 (MOCODB1)"]. Compound Z (oxidation product of cPMP) accumulates in urine in MOCS2 deficiency, and exogenous cPMP is NOT effective (unlike MOCS1 deficiency) [PMID:25709896 "with MOCS2 mutations supplementation with cPMP is ineffective."]. Many disease-variant reports (Reiss, Hahnewald, etc.); GO does not annotate the disease directly (captured via variants), so no BP term for disease is expected.

## GOA annotation summary and review stance

- **Core MF**: GO:0030366 molybdopterin synthase activity — multiple IDA (PMID:25709896, and contributes_to from PMID:12732628 / PMID:15073332) + IEA + Reactome TAS. ACCEPT the enables IDA as core; the `contributes_to` IDA entries are appropriate (activity requires both subunits) — ACCEPT/KEEP.
- **Core BP**: GO:0006777 Mo-molybdopterin cofactor biosynthetic process — IDA (PMID:25709896, 12732628, 15073332) + IEA. ACCEPT.
- **Core CC**: GO:1990140 molybdopterin synthase complex (IDA PMID:25709896, ComplexPortal, IPI) + GO:0005829 cytosol (IDA PMID:15073332, HPA, PMID:26705305). ACCEPT.
- GO:0032324 molybdopterin cofactor biosynthetic process — a broader/parent-ish process term (ARBA IEA + Reactome TAS); less precise than GO:0006777; KEEP_AS_NON_CORE (redundant, less specific but not wrong).
- GO:0005634 nucleus — secondary location tied to moonlighting role; KEEP_AS_NON_CORE.
- GO:0009968 negative regulation of signal transduction — PKR moonlighting (IDA PMID:26705305); KEEP_AS_NON_CORE.
- GO:0005515 protein binding (all IPI entries) — MARK_AS_OVER_ANNOTATED (uninformative; the specific interactions are already captured by the complex CC and the moonlighting story). Per policy never REMOVE a bare protein-binding IPI.
- IBA cytosol (GO_REF:0000033) — ACCEPT (consistent with experimental cytosol).
