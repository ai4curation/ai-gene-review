# TCN2 (Transcobalamin-2 / Transcobalamin II) review notes

UniProt: P20062 (TCO2_HUMAN). HGNC:11653. Gene TCN2 (synonym TC2). 427 aa precursor;
signal peptide 1-18, mature chain 19-427. Secreted. Chromosome 22.
Deep research: falcon out of credits (HTTP 402); no deep-research file. Grounded in
UniProt record, GOA, and cached PMIDs/Reactome.

## Core biology (verified)

TCN2 is the **primary plasma vitamin B12 (cobalamin, Cbl)-binding and transport
protein**. It is secreted (notably by vascular endothelial cells), circulates in
plasma, binds newly absorbed cobalamin exported from the enterocyte, and delivers it to
peripheral cells. The holo-TC (TC:Cbl) complex is captured from plasma by the ubiquitous
cell-surface receptor **CD320 (TCblR)**, a member of the LDL-receptor family, and taken
up by **receptor-mediated endocytosis**; TC:Cbl is delivered to lysosomes where TC is
degraded and Cbl released for downstream cofactor use (methylcobalamin for methionine
synthase; adenosylcobalamin for methylmalonyl-CoA mutase). This CD320 route is the
physiologically essential pathway supplying B12 to tissues. TCN2 is **not an enzyme**;
its molecular function is cobalamin binding, enabling cobalamin transport / acting as
the ligand for its uptake receptor.

- Function (UniProt CC): "Primary vitamin B12-binding and transport protein. Delivers
  cobalamin to cells." [ECO:0000269|PubMed:8443384]
- SUBUNIT: "Interacts with CD320 (via LDL-receptor class A domains)."
  [ECO:0000269|PubMed:27411955]
- SUBCELLULAR LOCATION: "Secreted" [ECO:0000269|PubMed:3782074, 8443384]
- SIMILARITY: "Belongs to the eukaryotic cobalamin transport proteins family."

## Evidence from cached publications

- **PMID:3782074** (Quadros et al. 1986, JBC) — Purification & molecular characterization
  of human TCII from plasma; determined N-terminal 19 aa; holo-TCII contained 1 mol
  cobalamin/mol protein; single 43 kDa polypeptide. UniProt RP: "PROTEIN SEQUENCE OF
  19-37, AND SUBCELLULAR LOCATION." Basis for secreted/extracellular localization and
  cobalamin binding (1:1). Abstract-only cache.
  Verbatim: "the final preparation of holo-TCII contained 1 mol of cobalamin/mol of
  protein."

- **PMID:8443384** (Quadros et al. 1993, Blood) — Recombinant human TCII secreted by
  insect (baculovirus) cells; binds Cbl and facilitates cellular uptake by binding to
  the TCII-Cbl receptor on the plasma membrane of K562 cells. UniProt FUNCTION source.
  Verbatim: "Transcobalamin II (TCII) is a cobalamin (Cbl, vitamin B12)-binding protein
  in mammalian plasma that facilitates the cellular uptake of the vitamin."
  Verbatim: "binds Cbl and facilitates the uptake of Cbl in eukaryotic cells by binding
  to the receptor for TCII-Cbl on the plasma membrane of K562 cells."

- **PMID:16537422** (Wuerges et al. 2006, PNAS) — Crystal structures of human & bovine
  holo-TC; two-domain architecture (N-terminal alpha6-alpha6 barrel + smaller C-terminal
  domain); one Cbl buried at the domain interface; base-on conformation; His of barrel
  becomes axial ligand. Direct structural evidence for cobalamin binding.
  Verbatim: "One Cbl molecule in base-on conformation is buried inside the domain
  interface."
  Verbatim: "the plasma transport, and cellular uptake uses cell surface receptors and
  three Cbl-transporting proteins, haptocorrin, intrinsic factor, and transcobalamin
  (TC)." [note: exact substring is "plasma transport, and cellular uptake"]

- **PMID:27411955** (Alam et al. 2016, Nat Commun) — Crystal structure of human holo-TC
  in complex with CD320 ectodomain. Establishes TC as the ligand captured by CD320 for
  receptor-mediated endocytosis; pH-dependent release in endosome. Full text available.
  Basis for the IPI protein-binding (interactor CD320/Q9NPF0) and cargo-receptor-ligand.
  Verbatim: "Cellular uptake of vitamin B12 (cobalamin) requires capture of
  transcobalamin (TC) from the plasma by CD320, a ubiquitous cell surface receptor of
  the LDLR family."
  Verbatim: "transcobalamin (TC)-bound Cbl is transported into cells by receptor-mediated
  endocytosis, which requires Ca2+-dependent complex formation of TC with its cognate
  cell surface receptor CD320"

- **PMID:1708393** (Platica et al. 1991, JBC) — cDNA/deduced aa sequence; leader peptide
  18 aa + secreted protein of 409 aa; homology to TCI and rat intrinsic factor. TAS
  basis (via PINC) for extracellular localization. Abstract-only.
  Verbatim: "The cellular uptake of cobalamin (Cbl, vitamin B12) is mediated by
  transcobalamin II (TCII), a plasma protein that binds Cbl and is secreted by human
  umbilical vein endothelial (HUVE) cells."

## GOA annotations (29 GOA rows → 27 stub entries; grouped)

MF:
- GO:0031419 cobalamin binding — IBA (GO_REF:0000033), IEA (GO_REF:0000120), IDA
  x3 (PMID:27411955, PMID:8443384, PMID:16537422). CORE. ACCEPT experimental/IBA.
- GO:0140355 cargo receptor ligand activity — EXP (PMID:3782074, assigned Reactome).
  Captures TC being the ligand recognized by CD320 for endocytic uptake. Supportable
  (Alam 2016 structural + Reactome CD320 model). ACCEPT (core—ligand for its uptake
  receptor). Note: EXP reference PMID:3782074 is the purification paper; the functional
  ligand-for-receptor role is directly shown by PMID:27411955/8443384.
- GO:0005515 protein binding — IPI (PMID:27411955), interactor UniProtKB:Q9NPF0 (CD320).
  Bare "protein binding" — uninformative per policy → MARK_AS_OVER_ANNOTATED (the
  informative capture of the CD320 interaction is GO:0140355 cargo receptor ligand
  activity). Do NOT REMOVE (experimental IPI).

BP:
- GO:0015889 cobalamin transport — IBA (GO_REF:0000033), IEA (GO_REF:0000002 InterPro),
  TAS (Reactome R-HSA-9758890), IDA (PMID:8443384), TAS (PMID:3782074). CORE. ACCEPT.

CC:
- GO:0005576 extracellular region — IBA (GO_REF:0000033), IEA (GO_REF:0000044
  SubCell), EXP (PMID:3782074), IDA (PMID:8443384), TAS PMID:1708393, TAS Reactome
  (R-HSA-3000074, 3000122, 3325546, 9759202, 9759209, 3299657). Secreted protein → CORE
  location. ACCEPT experimental; ACCEPT/route-context for TAS/IEA/IBA.
- GO:0005886 plasma membrane — TAS Reactome (R-HSA-3000112, 3000122). TCN2 is not itself
  a PM protein; it is transiently AT the PM as the ligand of CD320 during receptor
  binding/endocytosis. KEEP_AS_NON_CORE (transient transport-pathway localization, not a
  resident membrane protein).
- GO:0043202 lysosomal lumen — TAS Reactome (R-HSA-3000112, 3000263, 9759202). TC:Cbl is
  delivered to lysosomes and degraded there. KEEP_AS_NON_CORE (transient
  transport-pathway localization; the terminal degradation compartment).

## Core function summary

1. Cobalamin (vitamin B12) binding — GO:0031419 (MF). 1:1 holo-TC; structurally defined.
2. Cobalamin transport — GO:0015889 (BP). Delivers newly absorbed B12 to peripheral cells.
3. Cargo receptor ligand activity — GO:0140355 (MF). TC:Cbl is the ligand captured by
   CD320 (TCblR) for receptor-mediated endocytic uptake.
Location: extracellular region GO:0005576 (secreted plasma protein).

## Disease
Transcobalamin II deficiency (TCN2D, MIM:275350): autosomal recessive; early-infancy
failure to thrive, megaloblastic anemia, pancytopenia, agammaglobulinemia,
immunodeficiency/recurrent infections, methylmalonic aciduria; untreated → neurological
(psychomotor/mental developmental delay). (UniProt DISEASE, PMID:14632784, 19373259,
32841161, 33023511.)
</content>
