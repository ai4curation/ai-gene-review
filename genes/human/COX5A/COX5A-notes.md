# COX5A review notes

UniProtKB:P20674 — Cytochrome c oxidase subunit 5A, mitochondrial (HGNC:2267). 150 aa
precursor; residues 1–41 mitochondrial transit peptide, mature chain 42–150.

## Core biology (grounded in UniProt P20674 + cached publications)

- **Nuclear-encoded structural (supernumerary / non-catalytic) subunit of mitochondrial
  respiratory Complex IV (cytochrome c oxidase, COX)** — the terminal enzyme of the
  electron transport chain. The catalytic core (heme A / heme A3, Cu_A, Cu_B redox centres)
  is carried by the three **mtDNA-encoded** subunits MT-CO1, MT-CO2, MT-CO3; COX5A is one
  of the 11 nuclear-encoded supernumerary subunits that surround and stabilise that core
  [P20674 SUBUNIT: "a catalytic core of 3 subunits MT-CO1, MT-CO2 and MT-CO3, encoded in
  the mitochondrial DNA, and 11 supernumerary subunits ... COX5A ..."].
- Complex IV accepts electrons from reduced cytochrome c and reduces O2 to water while
  pumping protons across the inner membrane [P20674 FUNCTION: "the last enzyme in the
  mitochondrial electron transport chain which drives oxidative phosphorylation";
  "reduction of oxygen to water"].
- **Location:** mitochondrial inner membrane, peripheral membrane protein on the matrix
  side [P20674 SUBCELLULAR LOCATION: "Mitochondrion inner membrane ... Peripheral membrane
  protein ... Matrix side"]. Structurally resolved in the intact 14-subunit human CIV
  [PMID:30030519] and in supercomplex/megacomplex assemblies [PMID:28844695].
- **Disease:** biallelic COX5A variants cause Mitochondrial complex IV deficiency nuclear
  type 20 (MC4DN20; MIM 619064) — pulmonary arterial hypertension, lactic acidemia,
  failure to thrive; patient tissues show decreased CIV levels/activity [PMID:28247525,
  reported in P20674 DISEASE].

## Functional-role / MF reasoning

COX5A is **non-catalytic**. The catalytic redox chemistry (cytochrome-c oxidase activity,
GO:0004129; electron transfer, GO:0009055) resides in the mtDNA-encoded core, not in COX5A.
The two curated MF annotations GO:0004129 and GO:0009055 (both old TAS from PMID:2853101,
a 1988 cDNA-cloning paper that establishes COX5A is a COX subunit but does NOT demonstrate
catalytic activity for this subunit) are best treated as **contributes_to / structural**
rather than enabling catalysis by COX5A itself. Core MF for COX5A = **structural molecule
activity (GO:0005198)**, with the catalytic activity attributed to the complex
(contributes_to GO:0004129).

## Annotation triage summary

- CC respiratory chain complex IV (GO:0045277): strongly supported (IBA, IEA, IPI/ComplexPortal,
  IMP, IDA, structure) → ACCEPT. Use current term GO:0045277 (GO:0005751 is obsolete).
- BP mitochondrial electron transport, cytochrome c to oxygen (GO:0006123): IBA/IEA/NAS → ACCEPT
  as core BP (complex-level process COX5A is part of).
- CC mitochondrial inner membrane (GO:0005743): IEA/EXP/IDA/TAS → ACCEPT (matches UniProt).
- CC mitochondrial membrane (GO:0031966): IDA ComplexPortal → ACCEPT but broader parent of 0005743
  (keep as non-core / accept; less specific).
- CC mitochondrion (GO:0005739): HTP proteome → ACCEPT (broad but correct).
- CC mitochondrial intermembrane space (GO:0005758): TAS Reactome reaction-context. COX5A itself is
  matrix-side inner-membrane; the IMS term reflects the reaction (electron transfer from cyt c in IMS)
  not COX5A's own topology → MARK_AS_OVER_ANNOTATED (mislocalises the subunit).
- BP oxidative phosphorylation (GO:0006119): IEA UniPathway → ACCEPT (broader, correct).
- BP proton transmembrane transport (GO:1902600): IEA inferred from GO:0004129 mapping. COX IV does
  pump protons; the complex-level process is legitimate → ACCEPT (non-core; complex activity).
- BP cellular respiration (GO:0045333): NAS ComplexPortal → ACCEPT (broad parent, correct).
- MF cytochrome-c oxidase activity (GO:0004129) TAS: catalytic activity of the COMPLEX, not this
  non-catalytic subunit → MODIFY to structural molecule activity / MARK_AS_OVER_ANNOTATED. Keep as
  contributes_to in core_functions.
- MF electron transfer activity (GO:0009055) TAS: same reasoning — redox centres are in MT-CO1/CO2 →
  MARK_AS_OVER_ANNOTATED.
- MF protein binding (GO:0005515) IPI x6: bare, uninformative. Two point to specific biology
  (RAB5IF/Q9BUV8, AFG1L-LACE1/Q8WV93); four are HT interactome hits (KRT31, KRT40, EXOSC8, SPDEF,
  MESD, PIK3R1, APP). Per policy: MARK_AS_OVER_ANNOTATED (do not REMOVE experimental IPIs).

## Core functions
- MF: structural molecule activity (GO:0005198); contributes_to cytochrome-c oxidase activity (GO:0004129)
- BP: mitochondrial electron transport, cytochrome c to oxygen (GO:0006123)
- CC: located_in mitochondrial inner membrane (GO:0005743); in_complex respiratory chain complex IV (GO:0045277)
