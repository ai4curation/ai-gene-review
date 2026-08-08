# SLC19A3 (Thiamine transporter 2 / ThTr-2 / THTR2) — review notes

UniProt: Q9BZV2 (S19A3_HUMAN). Gene: SLC19A3. HGNC:16266. 496 aa, 12-TM,
reduced-folate-carrier (RFC / TC 2.A.48) family. MANE-select NM_025243.4 /
NP_079519.1.

## Core biology (grounded in UniProt file)

- **Function**: "Mediates high affinity thiamine uptake, probably via a proton
  anti-port mechanism" [file:human/SLC19A3/SLC19A3-uniprot.txt CC FUNCTION,
  ECO:0000269|PubMed:11731220,33008889,35512554,35724964]. "Has no folate
  transport activity" [file: CC FUNCTION, PubMed:11731220]. Also "Mediates
  H(+)-dependent pyridoxine transport" [file: CC FUNCTION,
  PubMed:33008889,35512554,35724964,36456177].
- **Catalytic activity (thiamine)**: "thiamine(out) + H(+)(in) = thiamine(in) +
  H(+)(out)" Rhea:RHEA:71271, ChEBI:CHEBI:18385 (thiamine)
  [file: CC CATALYTIC ACTIVITY].
- **Catalytic activity (pyridoxine)**: "pyridoxine(out) + n H(+)(out) =
  pyridoxine(in) + n H(+)(in)" Rhea:RHEA:76203, ChEBI:CHEBI:16709 (pyridoxine)
  [file: CC CATALYTIC ACTIVITY].
- **Kinetics**: KM 2.33 µM thiamine (pH 5.5), 2.36 µM thiamine (pH 7.4); KM 18.5 µM
  pyridoxine (pH 5.5), 20 µM pyridoxine [file: CC BIOPHYSICOCHEMICAL PROPERTIES].
  pH optimum 7.5 for thiamine transport [file: PubMed:11731220].
- **Location**: "SUBCELLULAR LOCATION: Membrane; Multi-pass membrane protein"
  [file: CC SUBCELLULAR LOCATION]. Reactome places it at the plasma membrane
  (R-HSA-199626, "associated with the plasma membrane"). 12 TRANSMEM helices in FT.
- **Tissue**: "Widely expressed but most abundant in placenta, kidney and liver"
  [file: CC TISSUE SPECIFICITY, PubMed:11136550,15871139].
- **Disease**: BTBGD (biotin-thiamine-responsive basal ganglia disease, MIM:607483),
  autosomal recessive; episodic encephalopathy; treatable with high-dose thiamine
  (+/- biotin) [file: CC DISEASE, PubMed:15871139]. BTBGD variants G23V, T422A
  [file: FT VARIANT, PubMed:15871139].
- **Family**: "Belongs to the reduced folate carrier (RFC) transporter (TC 2.A.48)
  family" [file: CC SIMILARITY]. InterPro IPR028337 = ThTr-2; PANTHER
  PTHR10686:SF37 THIAMINE TRANSPORTER 2. Paralogs SLC19A1 (RFC, folate) and
  SLC19A2 (THTR1, thiamine).
- **Structure**: multiple cryo-EM structures (PDB 8S4U, 9G5K, etc.).

## Key primary references

- **PMID:11731220** (Rajgopal 2001) — abstract only. Cloned SLC19A3, showed
  [3H]thiamine uptake (not methotrexate/folate) in HeLa transfectants; "high degree
  of specificity for vitamin B1"; pH optimum ~7.5; established ThTr2. Basis of the
  original thiamine-transport IDA.
- **PMID:33008889** (Yamashiro 2020, JBC) — abstract only. SLC19A2 and SLC19A3
  transport pyridoxine (B6) in addition to thiamine; pH-dependent (acidic-favoring),
  protonophore-sensitive; Km 18.5 µM pyridoxine for SLC19A3; siRNA knockdown of
  endogenous SLC19A3 in Caco-2 reduces pyridoxine uptake. IDA for thiamine transport
  and pyridoxine transport.
- **PMID:35512554** (Yamashiro 2022, DMPK) — abstract only. Human SLC19A3 transports
  both thiamine and pyridoxine; rat/mouse Slc19a3 transport thiamine but NOT
  pyridoxine (species difference). IDA thiamine + pyridoxine transport.
- **PMID:35724964** (Miyake 2022, JBC) — FULL TEXT. Identified 7 residues (Gln86,
  Gly87, Ile91, Thr93, Trp94, Ser168, Asn173) critical for human pyridoxine transport
  (not needed for thiamine); mutagenesis (IMP). Confirms thiamine transport by all
  orthologs. Basis of FT SITE annotations 86/87/91/93/94/168/173.
- **PMID:36456177** (Akino 2023, Life Sci Alliance) — FULL TEXT. Primary about DIRC2
  (SLC49A4) lysosomal pyridoxine exporter; SLC19A3 used as a plasma-membrane
  pyridoxine-transport positive control (FLAG-tagged, drives cellular pyridoxine
  accumulation). IDA pyridoxine transport.
- **PMID:11136550** (Eudy 2000) — abstract only. Identification/characterization of
  human+mouse SLC19A3; 496 aa, 12 TM, member of reduced-folate family; widely
  expressed, most abundant in placenta/kidney/liver. NAS "membrane" (a
  bioinformatic/structural inference in the original paper).
- **PMID:32296183** (Luck 2020, HuRI) — full text. Systematic high-throughput
  yeast-two-hybrid reference interactome (HuRI). Source of 11 bare GO:0005515
  "protein binding" IPI annotations (ARLN, CYB561, CYP4F2, GET1, LAT, PLPPR2, THBD,
  TMEM14A, TMEM14B, TMEM242, ZFPL1). Systematic Y2H hits with no dedicated SLC19A3
  functional follow-up; over-annotated bare protein binding.

## Reactome

- **R-HSA-199626** "SLC19A2/3 transport extracellular THMN to cytosol" — plasma
  membrane thiamine uptake; explicitly states SLC19A3/THTR2 "associated with the
  plasma membrane" mediates transport of extracellular thiamin into the cytosol, and
  that SLC19A3 "has no affinity for biotin" (studies of cultured cells). Supports
  thiamine transmembrane transporter activity (TAS) and plasma membrane (TAS).
- **R-HSA-196819** "Vitamin B1 (thiamin) metabolism" — pathway-level TAS placing
  SLC19A3 in thiamine metabolism (thiamine-containing compound metabolic process).

## Curation reasoning summary

- **Core MF**: thiamine transmembrane transporter activity (GO:0015234) — strongly
  supported by IDA/TAS/ISS/IBA and the UniProt catalytic reaction. This is the
  defining function.
- Pyridoxine transport (GO:0031923, BP) — well supported experimentally (IDA x3 + IMP)
  and by UniProt catalytic activity; genuine secondary/moonlighting activity of the
  human ortholog specifically. Keep as non-core (thiamine is the physiologically named
  and disease-relevant substrate). No pyridoxine *MF transporter* term is annotated;
  the transport is captured only at BP level in GOA.
- **Core BP**: thiamine transport (GO:0015888) / thiamine transmembrane transport
  (GO:0071934).
- **Core CC**: plasma membrane (GO:0005886).
- Bare protein binding GO:0005515 (IPI, HuRI Y2H): MARK_AS_OVER_ANNOTATED (systematic
  screen, uninformative, not core function). Do NOT remove (IPI experimental).
- Biotin transport: literature/Reactome note that SLC19A3 has NO affinity for biotin
  in cultured cells despite biotin-responsiveness of BTBGD — so do not annotate biotin
  transport. Biotin responsiveness of the disease is likely indirect.
- No `thiamine diphosphate biosynthetic process` (GO:0009229) annotation in GOA
  (present only in UniProt DR, IEA:Ensembl); SLC19A3 is a transporter, not a ThDP
  biosynthetic enzyme — that IEA would be an over-annotation, but it is not in the
  GOA set being reviewed.
