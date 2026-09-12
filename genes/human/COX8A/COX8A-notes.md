# COX8A review notes

UniProtKB:P10176 — Cytochrome c oxidase subunit 8A, mitochondrial (human, HGNC:2294).
Gene on chromosome 11. 69 aa precursor (25-aa mitochondrial transit peptide + 44-aa mature
chain). Single-pass inner-membrane protein (TM 37–60). This is the ubiquitously-expressed
COX8 isoform (the only COX VIII in primates; see PMID:2543673).

## Core biology (verified)

- **Structural, non-catalytic subunit of Complex IV (cytochrome c oxidase / CIV).** UniProt:
  "Component of the cytochrome c oxidase, the last enzyme in the mitochondrial electron
  transport chain which drives oxidative phosphorylation." The complex has a catalytic core
  of 3 mtDNA-encoded subunits (MT-CO1/2/3) plus 11 nuclear-encoded supernumerary subunits,
  one of which is COX8A ("11 supernumerary subunits ... COX8A and COXFA4, which are encoded
  in the nuclear genome" — PubMed:30030519). COX8A is the *smallest* subunit
  (PMID:26685157 title: "Loss of the smallest subunit of cytochrome c oxidase, COX8A").
- **Location:** mitochondrial inner membrane (GO:0005743), single-pass. Structure by cryo-EM
  (PMID:30030519, 5Z62/8D4T; also PMID:28844695 megacomplex). CIV = respiratory chain complex
  IV, GO:0045277 (current term; GO:0005751 is obsolete).
- **Process:** part of the electron-transport chain step that transfers electrons from
  cytochrome c to O2 (GO:0006123), within oxidative phosphorylation / cellular respiration,
  contributing to proton translocation across the inner membrane.
- **Non-catalytic:** The catalytic redox centers (heme a/a3, Cu_A, Cu_B) reside in MT-CO1 and
  MT-CO2. COX8A does not itself catalyze cytochrome-c oxidase chemistry; its MF is structural.
  Best MF = GO:0005198 structural molecule activity (contributes_to GO:0004129).
- **Assembly:** COX8A is incorporated at the MT-CO1/MT-CO2 association step (Reactome
  R-HSA-9865579: "associating with the COX7B, COX7C, and COX8A subunits").
- **Disease:** Mitochondrial complex IV deficiency, nuclear type 15 (MC4DN15; MIM:619059),
  autosomal recessive; Leigh-like syndrome + epilepsy (PMID:26685157). Patient tissues show
  decreased CIV levels/activity.
- **PTM:** Precursor is a SIFI-degron substrate; ubiquitinated by UBR4/KCMF1 (SIFI complex)
  in cytoplasm before import under mitochondrial stress (PMID:38297121). Not a GO annotation
  in the GOA here.

## GOA annotation dispositions

Cellular component / complex (all consistent, ACCEPT the informative ones):
- GO:0005739 mitochondrion (IBA, HTP) — ACCEPT (broad but correct).
- GO:0045277 respiratory chain complex IV (IBA, IEA, IPI) — ACCEPT (core complex membership).
- GO:0005743 mitochondrial inner membrane (IEA, EXP, TAS x4) — ACCEPT (core anatomical location).
- GO:0031966 mitochondrial membrane (IDA) — ACCEPT (correct, less specific than 0005743).

Biological process:
- GO:0006123 mito electron transport cyt c to O2 (IEA, NAS) — ACCEPT (core BP).
- GO:0006119 oxidative phosphorylation (IEA) — ACCEPT (correct, broader).
- GO:0045333 cellular respiration (NAS) — ACCEPT (correct, broader).
- GO:1902600 proton transmembrane transport (IEA, inferred from GO:0004129) — MARK_AS_OVER_ANNOTATED.
  Proton pumping is done by the MT-CO1 catalytic core, not this structural subunit; the
  inference is chained off a mis-assigned MF (see below). Not core.
- GO:0006091 generation of precursor metabolites and energy (TAS) — ACCEPT as non-core broad parent.
- GO:0043403 skeletal muscle tissue regeneration (IEA, orthology from rat P80433) —
  MARK_AS_OVER_ANNOTATED. Electronic ortholog transfer; not a demonstrated COX8A-specific
  function in human; a housekeeping OXPHOS subunit annotated to a specialized tissue process.

Molecular function:
- GO:0004129 cytochrome-c oxidase activity (TAS, PMID:2543673) — MARK_AS_OVER_ANNOTATED.
  COX8A is a non-catalytic supernumerary subunit; the catalytic activity belongs to the
  mtDNA-encoded core (MT-CO1/2). PMID:2543673 is a gene-mapping/cDNA paper and does not
  demonstrate that COX8A itself enables the oxidase activity. Better MF = structural molecule
  activity (GO:0005198), contributes_to GO:0004129. Not REMOVE (TAS/experimental-lineage,
  and the whole-complex activity is real).
- GO:0005515 protein binding (IPI x2; PMID:25416956, PMID:32296183) — MARK_AS_OVER_ANNOTATED.
  Uninformative; both are high-throughput binary interactome (Y2H) screens (HuRI / CCSB).
  Interactors (NPM1, MAGEA4, EDDM3B, BATF) are not CIV partners and likely non-physiological
  for a buried inner-membrane subunit. Per policy: MARK_AS_OVER_ANNOTATED, not REMOVE.

## Core functions used

- MF: GO:0005198 structural molecule activity (contributes_to GO:0004129 cytochrome-c oxidase activity)
- BP: GO:0006123 mitochondrial electron transport, cytochrome c to oxygen
- CC/location: GO:0005743 mitochondrial inner membrane; in_complex GO:0045277 respiratory chain complex IV
