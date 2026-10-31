# MLKL (human, Q8NB16) curation notes

## Provenance / process

- Deep research via falcon was not attempted: it is known to fail for this batch (HTTP 402). No
  `-deep-research-*.md` file exists; these notes are built directly from cached publications
  (fetched with `just fetch-gene-pmids` and `just fetch-pmid`), UniProt, and QuickGO.
- No human RIPK1 or RIPK3 reviews exist yet in `genes/human/`, so there is nothing to align with.
- Context: PANTHER family review `interpro/panther/PTHR44329/PTHR44329-review.yaml` lists MLKL as a
  member exception to family-wide GO:0004672 protein kinase activity and to the SF298-scoped
  GO:0004713 protein tyrosine kinase activity, and judged the PAINT NOT node PTN008689042 SOUND.

## Domain architecture

- N-terminal four-helix bundle (4HB, executioner domain, ~res 1-125), two-helix "brace", C-terminal
  pseudokinase domain (PsKD). UniProt: "Pseudokinase that plays a key role in TNF-induced"
  necroptosis; "The protein kinase domain is catalytically inactive" (mouse-derived, By similarity).

## Pseudokinase status (firm)

- Mouse MLKL: [PMID:24012422 "Although the pseudokinase domain binds ATP, it is catalytically inactive"].
- Human MLKL binds ATP without divalent cations (Class 2 pseudokinase) and the earlier reported kinase
  activity is attributed to contamination: [PMID:24107129 "it is probable that the catalytic activity previously attributed to MLKL is likely to arise from the catalytic activity of a contaminating protein"];
  [PMID:24107129 "We measured ATP binding to human MLKL by both thermal-shift assay and ITC"].
- Human structure: PMID:24219132 (abstract only) - crystal structure of human PsKD, nucleotide-binding
  mutagenesis; source of the IDA ATP binding annotation.
- [PMID:24703947 "binds to RIP3 through its kinase-like domain but lacks kinase activity of its own"].
- [PMID:29930286 "Despite lacking catalytic activity, MLKL has retained the ability to bind ATP"].
- GOA has NO positive kinase-activity rows for human MLKL; both kinase rows are NOT (ISS GO:0004672 and
  IBA GO:0004674 from PTN008689042). Both accepted.

## Activation and execution

- RIPK3 phosphorylates MLKL T357/S358: [PMID:22265413 "MLKL was phosphorylated by RIP3 at the threonine 357 and serine 358 residues"].
- Oligomerization: Cai 2014 reported trimers [PMID:24316671 "MLKL forms a homotrimer through its amino-terminal coiled-coil domain"],
  but the trimer was partly disulfide-stabilized during lysis [PMID:24316671 "the disulphide bonds of the trimerized MLKL proteins were formed by oxidation during cell lysis"];
  later work shows human MLKL tetramers [PMID:29930286 "Wild-type hMLKL assembled into tetramers in vitro, robustly permeabilized liposomes"].
  Stoichiometry remains debated -> generalize homotrimerization to protein homooligomerization.
- PIP binding / membrane permeabilization: [PMID:24813885 "a patch of positively charged amino acids on the surface of the 4HBD binds to phosphatidylinositol phosphates (PIPs)"];
  [PMID:24813885 "induces leakage of PIP-containing liposomes as potently as BAX"];
  [PMID:24703947 "The phosphorylated MLKL forms an oligomer that binds to phosphatidylinositol lipids and cardiolipin"];
  [PMID:26853145 "PI(4,5)P2 is the preferred PIP-binding partner"].
- Inositol phosphate code: IPMK/ITPK1 needed for MLKL oligomerization and membrane localization
  [PMID:29883610 "In IP kinase mutant cells, MLKL failed to oligomerize"].
- 4HB clusters: membrane localization necessary but not sufficient [PMID:25288762 "membrane localization is necessary, but insufficient, to induce cell death"].
- Downstream Ca2+ influx via TRPM7 (Cai 2014) - not taken as an MLKL activity.

## Localization

- Cytosol (basal), plasma membrane (activated) [PMID:24316671]. Nucleus: mouse, influenza/ZBP1 nuclear
  necroptosis (ISS transfer only for human) - non-core.

## Decisions summary

- REMOVE: GO:0007166 cell surface receptor signaling pathway (IEA InterPro2GO from the Cbl-N
  superfamily IPR036537; structural 4HB fold resemblance, not Cbl adaptor function).
- MODIFY: protein binding (x3, RIPK3 partner) -> protein kinase binding; homotrimerization ->
  protein homooligomerization.
- NEW: GO:0005546 PI(4,5)P2 binding; GO:0140912 membrane destabilizing activity (MLKL itself
  permeabilizes membranes; comparator NINJ1 carries the term; GSDMD carries wide pore channel activity).
- Necroptotic signaling pathway kept non-core (MLKL is the effector at the end of the RIPK3 pathway;
  execution phase of necroptosis is the core process).
