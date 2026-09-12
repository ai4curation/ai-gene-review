# ATP5PO (OSCP) review notes

UniProtKB:P48047 · HGNC:850 · gene ATP5PO (syn. ATP5O, ATPO) · 213 aa precursor
(transit peptide 1-23; mature chain 24-213). Family: ATPase delta chain family.

## Function (verified biology)

ATP5PO encodes the **oligomycin sensitivity conferral protein (OSCP)**, the subunit at
the top of the **peripheral (stator) stalk** of the mitochondrial F1Fo ATP synthase
(Complex V). It caps the F1 catalytic head and, together with the b/F6/d subunits, forms
the stationary peripheral stalk that holds the F1 alpha3beta3 catalytic hexamer static
against the rotating central stalk — essential for coupling proton flux through Fo to ATP
synthesis in F1. It is a **structural (non-catalytic) subunit**; it confers oligomycin
sensitivity on the complex.

- UniProt FUNCTION [P48047]: "Subunit OSCP, of the mitochondrial membrane ATP synthase
  complex (F(1)F(0) ATP synthase or Complex V) that produces ATP from ADP in the presence
  of a proton gradient across the membrane... Part of the complex F(0) domain and the
  peripheric stalk, which acts as a stator to hold the catalytic alpha(3)beta(3) subcomplex
  and subunit a/ATP6 static relative to the rotary elements."
- UniProt SUBUNIT: peripheral stalk = subunits F6, b, d, and OSCP. [PMID:37244256]
- Cryo-EM structure of the human ATP synthase resolves OSCP (chain O, residues 24-213):
  [PMID:37244256 "Structure of the human ATP synthase."]

## Key experimental anchors

- **PMID:12110673** (IDA): human F1Fo ATP synthase immunocaptured from heart/fibroblasts;
  OSCP identified as a bona fide subunit; complex V displayed oligomycin-sensitive ATP
  hydrolysis. Supports part_of ATP synthase complex + contributes_to rotational MF.
- **PMID:15850986** (IMP / IDA): OSCP is the binding target of the F1Fo-ATPase inhibitor
  Bz-423; RNAi knockdown of OSCP changes cellular sensitivity, functionally implicating
  OSCP in ATP synthase activity → supports involved_in proton motive force-driven mito ATP
  synthesis (GO:0042776) and mitochondrion localization.
- **PMID:7490082** (cloning, NAS): "This ATP5O subunit is a key structural component of the
  stalk of the mitochondrial respiratory chain F1F0-ATP synthase." Supports the structural
  role and part_of complex.
- **PMID:30266287** (IPI with PPID/Cyclophilin D, Q08752): OSCP interacts with Cyclophilin
  D and with amyloid-beta; CypD/OSCP is functionally linked to the permeability transition
  pore and F1Fo ATP synthase dysfunction in AD. This is the one functionally-informative
  interaction among the IPI set.
- **PMID:34954817** (not cached): biallelic ATP5PO variants → Mitochondrial complex V
  deficiency, nuclear type 7 (MC5DN7); confirms essential role in complex V. Recorded from
  the UniProt DISEASE line.

## Localization

- Mitochondrial inner membrane (GO:0005743) — anatomical location of the complex; supported
  by Reactome TAS, ComplexPortal NAS (PMID:26297831), and UniProt SubCell.
- Mitochondrion (GO:0005739) — multiple IDA/HDA/IBA.
- Plasma membrane (PMID:17851741, IDA) and cell surface (Ensembl IEA): "ecto-ATP synthase"
  — a minor, non-core surface pool reported on HepG2 hepatocytes; keep as non-core.
- Nucleus (GO:0005634, HDA PMID:21630459): sperm-nucleus proteomics; contaminant / non-core.

## Annotation decisions summary

- Core: structural molecule activity (GO:0005198, authored MF); part_of proton-transporting
  ATP synthase complex (GO:0045259); involved_in proton motive force-driven mitochondrial
  ATP synthesis (GO:0042776); located_in mitochondrial inner membrane (GO:0005743).
- `contributes_to GO:0046933` (rotational ATP synthase MF): ACCEPT — correct "contributes_to"
  usage for a non-catalytic subunit of the catalytic complex.
- `enables GO:0046933` (InterPro IEA): MODIFY → the enables/contributes_to distinction
  matters; OSCP does not itself enable the rotary catalytic MF. Downgrade to structural role.
- `GO:0016887 ATP hydrolysis activity` (contributes_to, Ensembl IEA): MARK_AS_OVER_ANNOTATED —
  in vivo OSCP/complex only synthesizes; hydrolysis is an artificial in-vitro reverse activity.
- `estradiol binding` (GO:1903924), `cellular response to cAMP` (GO:0071320), `cellular
  response to cytokine stimulus` (GO:0071345): Ensembl orthology-transferred from rat; not
  core OSCP functions → MARK_AS_OVER_ANNOTATED.
- Bare `protein binding` IPIs (GO:0005515): MARK_AS_OVER_ANNOTATED per policy (uninformative),
  not REMOVE.
- `nucleus`, `cell surface`, `plasma membrane`: KEEP_AS_NON_CORE (minor/contaminant pools).
