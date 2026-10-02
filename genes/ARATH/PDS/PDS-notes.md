# PDS (Q07356, AT4G14210, PDS3) — Arabidopsis thaliana — review notes

## Identity

- UniProt Q07356, `PDS_ARATH`, 566-aa precursor, EC 1.3.5.5. RecName
  "15-cis-phytoene desaturase, chloroplastic/chromoplastic"; AltName "Phytoene
  dehydrogenase" / "Phytoene desaturase"
  [file:ARATH/PDS/PDS-uniprot.txt "RecName: Full=15-cis-phytoene desaturase, chloroplastic/chromoplastic"].
- Single-copy Arabidopsis locus At4g14210, TAIR name PDS3
  [file:ARATH/PDS/PDS-uniprot.txt "TAIR; AT4G14210; PDS3."]. Deep-research
  (retrieval support only, not citable) agrees: "PDS, also called PDS3, is the
  single-copy Arabidopsis thaliana locus At4g14210". Distinct from ZDS
  (At3g04870, zeta-carotene desaturase, the downstream enzyme).
- Family: "Belongs to the carotenoid/retinoid oxidoreductase family."
  [file:ARATH/PDS/PDS-uniprot.txt]. Domains: Amino_oxidase (IPR002937, PF01593),
  FAD/NAD(P)-binding fold (IPR036188), Phytoene_desaturase (IPR014102),
  Zeta_carotene_desat/Oxidored (IPR050464); PANTHER PTHR42923:SF45.

## Molecular function

- Catalyses the first two desaturations of the plant poly-cis carotenoid route.
  UniProt FUNCTION: "Converts phytoene into zeta-carotene via the intermediary
  of phytofluene by the symmetrical introduction of two double bonds at the
  C-11 and C-11' positions of phytoene with a concomitant isomerization of two
  neighboring double bonds at the C9 and C9' positions from trans to cis."
  [file:ARATH/PDS/PDS-uniprot.txt].
- Rhea reaction (EC 1.3.5.5): 2 plastoquinone + 15-cis-phytoene =
  9,9',15-tri-cis-zeta-carotene + 2 plastoquinol [RHEA:30287;
  file:ARATH/PDS/PDS-uniprot.txt "Reaction=2 a plastoquinone + 15-cis-phytoene ="].
  This matches the module concept (`modules/carotene_backbone_biosynthesis.yaml`,
  pds_step): GO:0016166, RHEA:30287, PTHR42923:SF45, PAINT node PTN000078359.
- Cofactor FAD (by similarity to A2XDA1); plastoquinone is the electron acceptor.
  UniProt COFACTOR: FAD [file:ARATH/PDS/PDS-uniprot.txt]. It is therefore a
  genuine oxidoreductase (unlike the paralogous CRTISO, which is a non-redox
  isomerase — hence oxidoreductase IEA is correct for PDS but was removed for
  CRTISO).
- Experimental basis: Bartley, Scolnik & Beyer (1999) expressed Arabidopsis PDS
  and ZDS in E. coli and showed the poly-cis desaturation pathway yields
  pro-lycopene [PMID:9914519 "the two carotene desaturases phytoene desaturase
  and carotene zeta-carotene desaturase from Arabidopsis thaliana"; "pro-lycopene
  (7,9,7',9'-tetra-cis)-lycopene is the main end product of the plant
  desaturation pathway"]. This is the IDA source (TAIR/TIGR); cached record is
  abstract-only (`full_text_available: false`) but the curators read the full
  text. Product of PDS itself is (tri-cis) zeta-carotene; downstream Z-ISO, ZDS
  and CRTISO complete conversion to all-trans-lycopene.
- Structure/oligomer: rice PDS crystallography shows a homotetramer (dimer of
  dimers) with a carotene-binding cavity and quinone site; norflurazon/fluridone
  are competitive inhibitors at the quinone region (deep-research, retrieval
  support only; primary work is on the rice ortholog). UniProt SUBUNIT:
  "Homotetramer." [file:ARATH/PDS/PDS-uniprot.txt]. These are homolog-based for
  Arabidopsis, so not asserted as core Arabidopsis annotations.

## Biological process

- carotenoid biosynthetic process (GO:0016117): the module-level process; PDS
  performs a committed desaturation step. Annotated IBA, IDA (PMID:9914519) and
  IEA (InterPro IPR014102 Phytoene_desaturase). All accepted.
- carotene biosynthetic process (GO:0016120): PDS's immediate product,
  zeta-carotene, is a carotene. Annotated IDA (PMID:9914519) and IEA (ARBA).
  Accepted. (Per brief: in the current ontology GO:0016120 is NOT a descendant of
  GO:0016117; do not "fix" this.)

## Localization

- Nuclear-encoded, plastid-targeted; transit peptide 1..86, mature chain 87..566
  [file:ARATH/PDS/PDS-uniprot.txt]. UniProt SUBCELLULAR LOCATION: "Plastid,
  chloroplast"; "Plastid, chromoplast"; "Membrane ... Peripheral membrane
  protein" [file:ARATH/PDS/PDS-uniprot.txt].
- Chloroplast (GO:0009507): HDA proteomics (PMID:18431481), IEA SubCell, ISM
  (AtSubP), TAS (PMID:9700076). All accepted — correct organelle.
- Chromoplast (GO:0009509): IEA SubCell, ISS. Accepted; UniProt records
  chromoplast and the DEVELOPMENTAL STAGE note "Ripening fruit."
- Chloroplast thylakoid (GO:0009534, HDA PMID:20061580) and chloroplast envelope
  (GO:0009941, HDA PMID:12938931 and PMID:20061580): AT_CHLORO / envelope
  proteomics. Consistent with the enzyme being a peripheral membrane protein of
  plastid membranes (deep research: ~84% envelope, ~16% thylakoid — retrieval
  support only). Accepted as membrane sites of action.
- Membrane (GO:0016020): IEA SubCell (SL-0162) and ISS (A2XDA1). Generic but
  correct (peripheral membrane protein). Accepted as a correct broad location.
- Cytosol (GO:0005829, HDA PMID:28887381): high-throughput protein-correlation
  profiling that explicitly found many proteins "clearly partitioned between
  cytosolic and membrane-associated pools" [PMID:28887381]. For a
  transit-peptide-bearing plastid enzyme, the cytosolic signal reflects the
  pre-import precursor / dual-pool detection, not the functional site. Kept as a
  non-core location (experimental HDA, not removed).

## Action summary

- No REMOVE: the two GO_REF:0000002 InterPro2GO rows (GO:0016117 from
  Phytoene_desaturase IPR014102; GO:0016491 oxidoreductase from Amino_oxidase
  IPR002937) are both biologically correct for PDS — this is not a wrong-paralog
  mapping like squalene/GGPP synthase on a phytoene synthase, so the brief's
  REMOVE instruction does not apply here.
- No generic `protein binding` (GO:0005515) annotation exists for PDS.
- oxidoreductase activity (GO:0016491) accepted as a correct but generic parent
  of the specific phytoene dehydrogenase activity (GO:0016166) already annotated.
- No NEW terms proposed: PDS's catalytic step and processes are already covered
  by GO:0016166, GO:0016117 and GO:0016120. Participation/comparator tests give
  no well-grounded gap (there is no GO term specific to the
  phytoene->zeta-carotene sub-step, and the module itself uses GO:0016166 at the
  parent level for both PDS and CrtI routes).

## Core function

One core function: 15-cis-phytoene:plastoquinone oxidoreductase (phytoene
desaturase) activity (GO:0016166), directly involved in carotenoid biosynthetic
process (GO:0016117) and carotene biosynthetic process (GO:0016120), at plastid
(chloroplast/chromoplast) membranes (envelope and thylakoid).

## Final action decisions (completed review)

- Tally: 19 ACCEPT, 1 KEEP_AS_NON_CORE (cytosol HDA), 1 MODIFY, 1 NEW; 0 PENDING.
- **GO:0016491 oxidoreductase activity (IEA, IPR002937): MODIFY -> GO:0016166**
  phytoene dehydrogenase activity. Revised from the earlier "ACCEPT" note:
  oxidoreductase activity is uninformatively broad when the specific EC 1.3.5.5
  activity is known and already annotated (IDA/IBA/IEA). This mirrors the sibling
  ZDS review, which MODIFY'd the identical IPR002937->GO:0016491 row to the
  specific desaturase activity GO:0016719. Not a REMOVE: PDS genuinely is an
  oxidoreductase, so the parent is correct, just too general.
- **NEW: GO:1901177 lycopene biosynthetic process (IDA, PMID:9914519).** Revised
  from the earlier "no NEW" note. Participation test: PDS performs two of the four
  desaturations of the phytoene->lycopene route, so it does part of the work of
  lycopene biosynthesis (not merely required for it). Comparator test: the sibling
  desaturase ZDS, in the same role in the same pathway and characterised in the
  same paper (PMID:9914519), carries GO:1901177 (IDA); PDS lacked it. UniProt
  PATHWAY explicitly places PDS in "lycopene biosynthesis"
  [file:ARATH/PDS/PDS-uniprot.txt "PATHWAY: Carotenoid biosynthesis; lycopene biosynthesis."].
  Both tests satisfied; proposed conservatively.
- cytosol (GO:0005829, HDA PMID:28887381) kept as KEEP_AS_NON_CORE, not REMOVE:
  it is an experimental HDA hit; the study reports many proteins "clearly
  partitioned between cytosolic and membrane-associated pools"
  [PMID:28887381], so the signal reflects the pre-import precursor / dual pool,
  not a functional cytosolic activity.

## Provenance note

`PDS-deep-research-falcon.md` was used as retrieval support only. All identifiers
(GO, Rhea, PANTHER, CHEBI, PMIDs) and all verbatim `supporting_text` quotes were
taken from the cached publications, the UniProt record, QuickGO and the module
file — never from the deep-research narrative.
