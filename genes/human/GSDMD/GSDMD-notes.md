# GSDMD (Gasdermin-D) research notes

UniProt: P57764 (GSDMD_HUMAN), 484 aa. HGNC:25697. Chr 8q24.3.
Family: gasdermin family (PANTHER PTHR16399 GASDERMIN). Domains: Gasdermin (PF04598),
Gasdermin_C (PF17708), Gasdermin_pore (IPR040460), Gasdermin_PUB (IPR041263).

## Summary of function

GSDMD is the terminal executioner of pyroptosis, a lytic, pro-inflammatory form of
programmed cell death. Full-length GSDMD is an autoinhibited two-domain protein: an
N-terminal pore-forming domain (GSDMD-NT, ~residues 1-275) held inactive by an
intramolecular interaction with the C-terminal repressor domain (GSDMD-CT).
Inflammatory caspases cleave the interdomain linker (at Asp275 by CASP1; also CASP4/CASP5
in the non-canonical, cytosolic-LPS pathway; CASP8 in the Yersinia/TAK1-inactivation
context), releasing GSDMD-NT. The freed N-terminal fragment binds acidic membrane
phospholipids of the inner leaflet, oligomerizes, and inserts to form large
(10-15 nm inner-diameter) transmembrane pores. These pores conduct mature IL-1β and IL-18
out of the cell and drive pyroptosis; terminal membrane rupture (cytolysis) is executed
downstream by NINJ1.

- Precursor is a pore-forming protein that plays a key role in host defense against
  pathogen infection and danger signals [UniProt FUNCTION; PMID:26375003, PMID:26375259,
  PMID:27281216].
- GSDMD-NT "moves to the plasma membrane where it strongly binds to inner leaflet lipids,
  including monophosphorylated phosphatidylinositols ... homooligomerizes within the
  membrane and forms pores of 10-15 nanometers of inner diameter, allowing the release of
  mature interleukin-1 (IL1B and IL18) and triggering pyroptosis" [UniProt FUNCTION;
  PMID:27281216, PMID:27418190, PMID:29898893, PMID:33883744].
- Autoinhibition: "intramolecular interactions between N- and C-terminal domains mediate
  autoinhibition in the absence of activation signal" [UniProt ACTIVITY REGULATION;
  PMID:26375003, PMID:28928145, PMID:29576317, PMID:32109412].
- Cleavage at Asp87 by CASP3/CASP7 inactivates pyroptotic ability [UniProt;
  PMID:28392147].

## Lipid binding (the membrane-targeting specificity)

GSDMD-NT binds inner-leaflet acidic phospholipids and cardiolipin; it does NOT bind
phosphatidylcholine/phosphatidylethanolamine (outer leaflet), which is why secreted
GSDMD-NT kills bacteria (which expose cardiolipin/PG) but spares neighboring mammalian
cells from the outside [PMID:27281216 "Pore-forming activity and structural autoinhibition
of the gasdermin family"].
- Binds: PI4P, PI(4,5)P2, PI(3,4,5)P3, phosphatidic acid, phosphatidylserine, cardiolipin.
- The specific lipid-binding GO terms (PI4P, PI(4,5)P2, PS, PA, cardiolipin binding) are
  all mechanistically supported by the same body of biochemistry.

## Structure of the pore (channel activity)

Cryo-EM shows GSDMD-NT forms a 27-33-mer ring-shaped transmembrane β-barrel pore ~215 Å
outer / ~in the 10-15 nm inner-diameter range. The pore is a large, non-selective conduit
("wide pore channel activity", GO:0022829).
- "Gasdermin D pore structure reveals preferential release of mature interleukin-1"
  [PMID:33883744, full text available] — cryo-EM structure; IDA support for wide pore
  channel activity (GO:0022829), pyroptotic cell death (GO:0141201), plasma membrane
  (GO:0005886), positive regulation of inflammatory response (GO:0050729).

## Cleavage/activation, PTMs

- Cleaved by CASP1 at Asp275 (canonical inflammasome) and by CASP4/CASP5 (non-canonical,
  cytosolic LPS). CASP8 cleaves upon TAK1 inactivation (Yersinia YopJ).
- Palmitoylation at Cys191 by ZDHHC5/ZDHHC9 directs membrane translocation/pore formation
  [PMID:38530158 "The palmitoylation of gasdermin D directs its membrane translocation and
  pore formation", full text available].
- Succination at Cys191 by fumarate (Krebs cycle metabolite) modulates activity.
- Ubiquitination by TRAF1/TRAF2; O-GlcNAcylation by OGT reduces cleavage.
- Microbial evasion: cleaved/inactivated by enteroviral 3C proteases; ubiquitinated by
  Shigella IpaH7.8 for degradation.

## Subcellular location (by fragment)

- Full-length GSDMD: cytosol.
- GSDMD-NT: cell membrane (plasma membrane, the pore); also mitochondrial membrane
  (releases mtDNA, by similarity).
- p13 fragment (CASP3/CASP7 product): nucleus — acts as a STAT1 transcription coactivator
  for CIITA/MHC-II in gut food tolerance (by similarity to mouse Q9D8T2). This explains
  the nucleus/nucleoplasm annotations.

## Additional biology

- p40 fragment (papain/allergen cleavage) forms pores that selectively release IL-33,
  promoting type 2 inflammation [PMID:35794369, full text available] — also IDA support
  for wide pore channel activity (GO:0022829).
- Secreted GSDMD-NT has direct bactericidal activity against Gram-negative and
  Gram-positive bacteria [PMID:27281216].
- Neutrophil granule annotations (ficolin-1-rich granule lumen, tertiary/specific granule
  lumen; all Reactome TAS) reflect neutrophil localization datasets; GSDMD is expressed in
  neutrophils and involved in NETosis, but these lumen CC terms are bulk-proteomic granule
  assignments, not core function.

## GOA annotation assessment orientation

Core molecular functions to capture:
- wide pore channel activity (GO:0022829) — the defining MF, IDA-supported.
- The lipid-binding activities (PI4P, PI(4,5)P2, PS, PA, cardiolipin) — real, but they are
  the membrane-targeting mechanism upstream of pore formation; keep as core/contributing.
Core processes:
- pyroptotic inflammatory response (GO:0070269) / pyroptotic cell death (GO:0141201).
- defense response to (Gram-neg / Gram-pos) bacterium; positive regulation of IL-1β
  production; positive regulation of inflammatory response.
Locations:
- plasma membrane (the active pore), cytosol (precursor). NLRP3/canonical inflammasome
  "part_of" — GSDMD is a substrate/effector recruited at the inflammasome; these are
  reasonable but represent recruitment rather than a stable stoichiometric subunit.

## protein binding (GO:0005515, IPI)

Multiple IPI "protein binding" rows from interactome screens (PMID:25416956 human
interactome; PMID:31515488; PMID:32296183; PMID:34296442). Uninformative per project
guidelines — mark as over-annotated/non-core (keep, but not core; recommend more specific
MF where a real partner is known).

## Key references (verified against UniProt curation / cached full text)

- PMID:26375003 — Shi et al., Nature 2015: CASP4/5/11 cleave GSDMD; pyroptosis effector.
- PMID:26375259 — Kayagaki et al., Nature 2015: GSDMD identified as inflammasome
  substrate required for pyroptosis (CRISPR screen).
- PMID:27281216 — Ding et al., Nature 2016: pore-forming activity, lipid specificity,
  structural autoinhibition, bactericidal activity. (cached, abstract-only)
- PMID:27418190 — Liu et al., Nature 2016: GSDMD-NT pores in membranes.
- PMID:33883744 — Nature 2021: GSDMD pore cryo-EM structure, IL-1 release. (full text)
- PMID:35794369 — allergen protease p40 fragment, IL-33 release. (full text)
- PMID:38530158 — palmitoylation directs membrane translocation. (full text)
