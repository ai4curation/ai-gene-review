# FbaB (fba2) — *Streptococcus pyogenes* — research notes

UniProt: **Q8G9G1** (Q8G9G1_STRPY, TrEMBL/unreviewed), gene **fba2** / **FbaB**
("Fn-binding protein of group A streptococci type B"); also annotated as
"Thioester-forming surface-anchored protein". 733 aa. NCBI taxon 1314
(*Streptococcus pyogenes*).

This gene is the entry point for PDB **9OJ3** (`pdb_00009oj3`), the 1.43 Å crystal
structure of the engineered **SpyTag003–SpyCatcher003** complex. SpyTag/SpyCatcher
are *not* separate genes — they are split/engineered fragments of the **CnaB2 domain**
of FbaB (the C-terminal "SpaA-like prealbumin fold" / Cna protein B-type domain,
roughly residues 462–541, which is exactly the region crystallized in 9OJ3 and the
earlier FbaB-CnaB2 structures 2X5P/4MLI/4MLS/5TTH/6XG6). So the natural biology to be
reviewed is the FbaB adhesin, and the SpyTag/SpyCatcher "module" is the engineered
derivative of one of its domains.

## Domain architecture (UniProtKB:Q8G9G1)

- **N-terminal thioester domain (TED)** — FT DOMAIN 92..212, Pfam PF08341 (TED),
  InterPro IPR013552, Gene3D "Thioester domain" (2.30.30.670). Internal
  Cys–Gln thioester bond; in related streptococcal adhesins this forms covalent
  "chemical-harpoon" bonds to host proteins (see PMID:26032562).
- **Fibronectin-binding repeats** — Pfam PF02986 (Fn_bind, x3), InterPro IPR004237;
  the C-terminal Fn-binding repeat region that mediates fibronectin binding
  [PMID:12359713].
- **CnaB2 / SpaA-like prealbumin-fold domain** — FT DOMAIN 465..544, Pfam PF17802
  (SpaA), InterPro IPR041033, SUPFAM SSF49478 "Cna protein B-type domain". Forms a
  spontaneous **intramolecular Lys–Asp isopeptide bond** (Glu-assisted) that gives
  the domain extreme mechanical/thermal/chemical stability. This is the domain split
  into SpyTag (C-terminal β-strand bearing the reactive Asp) and SpyCatcher (the rest,
  bearing the reactive Lys) [PMID:22366317].
- **LPXTG cell-wall anchor** — NCBIfam TIGR01167 (LPXTG_anchor) / TIGR03934 (TQXA);
  C-terminal sortase substrate motif anchoring FbaB to peptidoglycan
  [PMID:12359713, abstract: "an LPXTG motif and Fn-binding repeat domains in the
  C-terminal region"].

No GO annotations exist in UniProtKB/GOA for Q8G9G1 (TrEMBL, unreviewed) — the GOA
file fetched is empty. The review therefore proposes core functions de novo rather
than adjudicating existing annotations.

## Native function and virulence (FbaB)

- FbaB is a **surface-located fibronectin (Fn)-binding protein** and **major virulence
  factor** of group A *Streptococcus* (GAS), serotypes M3/M18, originally found in
  strains from toxic-shock-like syndrome (TSLS) patients
  [PMID:12359713 "Group A Streptococcus pyogenes has surface-located fibronectin
  (Fn)-binding proteins known to be a major virulence factor, which adheres to and
  invades host cells"].
- Designated FbaB; possesses an LPXTG motif and Fn-binding repeat domains; expressed
  on the cell surface of TSLS strains [PMID:12359713
  "designated as FbaB (Fn-binding protein of group A streptococci type B)"].
- **Strong fibronectin binding** by recombinant FbaB (ELISA + ligand blotting)
  [PMID:12359713 "recombinant FbaB exhibits a strong Fn-binding ability"].
- **Adhesion/invasion**: an FbaB-deficient mutant showed ~6-fold lower adhesion and
  invasion of HEp-2 cells, and reduced mouse mortality [PMID:12359713
  "An FbaB-deficient mutant strain showed 6-fold lower adhesion and invasion
  efficiencies to HEp-2 cells than the wild type"], i.e. FbaB mediates adhesion to,
  and invasion of, host cells and contributes to invasive disease.
- **Thioester domain / covalent host binding**: streptococcal surface proteins with
  TED domains (e.g. SfbI/Cpa) covalently capture host proteins (fibrinogen) via an
  internal thioester acting as a "chemical harpoon"
  [PMID:26032562 "the streptococcal surface protein SfbI mediates covalent interaction
  with the host protein fibrinogen using an unusual internal thioester bond as a
  'chemical harpoon'"]. FbaB carries the same TED domain; this is supportive
  background for FbaB's covalent host-binding capacity rather than direct FbaB data.

## CnaB2 isopeptide bond and the SpyTag/SpyCatcher engineering lineage

- Native rationale: the spontaneous isopeptide bond in the CnaB2 domain gives the
  adhesin mechanical resilience, plausibly needed to **bridge S. pyogenes to
  fibronectin during host-cell invasion under force**
  [PMID:22366317 "The resilience of SpyTag:SpyCatcher to pulling forces after
  isopeptide bond formation suggests that the CnaB2 domain may be exposed to high
  force in bridging S. pyogenes to fibronectin during cell invasion"].
- Engineering (Zakeri et al. 2012, PNAS): splitting the CnaB2 domain and engineering
  the fragments gave **SpyTag** (15-aa peptide) + **SpyCatcher** (protein), which
  reconstitute the **covalent isopeptide (amide) bond** spontaneously on mixing, in
  minutes, irreversibly (not broken by boiling/competition; resists >1 nN force)
  [PMID:22366317 "By splitting this domain and rational engineering of the fragments,
  we obtained a peptide (SpyTag) which formed an amide bond to its protein partner
  (SpyCatcher) in minutes"]. Reactive residues: SpyCatcher Lys, SpyTag Asp, catalytic
  Glu.
- Optimization: Li et al. 2014 (JMB; PDB 4MLI/4MLS) solved the SpyCatcher:SpyTag
  structure and trimmed/optimized SpyCatcher [PMID:24161952].
- 3rd generation: Keeble et al. 2019 (PNAS) engineered **SpyTag003/SpyCatcher003** for
  much faster reaction ("approaching infinite affinity") [PMID:31822621].
- PDB 9OJ3 (this entry): 1.43 Å crystal structure of SpyTag003–SpyCatcher003, reported
  as a case study by the ALS-ENABLE synchrotron resource
  [PMID:40531663 "A case study showcasing the main technologies of the resource
  applied to the characterization of the SpyCatcher-SpyTag protein system is
  presented"].

## Curation decisions

- One underlying gene only: **FbaB (Q8G9G1)**. The PDB "complex" is a homo-pairing of
  two engineered fragments of this single protein, so there is exactly one gene review.
- Core functions asserted from literature + domain evidence (no GOA to adjudicate):
  fibronectin binding (GO:0001968) driving adhesion to / invasion of host cells
  (GO:0044650), at the bacterial cell surface / cell wall (GO:0009986 / GO:0005618).
  The TED covalent-host-binding and CnaB2 isopeptide mechanical-stability roles are
  described but only the fibronectin/adhesion axis is asserted as an experimentally
  supported core function for *this* protein.
- The SpyTag/SpyCatcher engineering lineage is captured in the companion module
  `modules/spytag_spycatcher.yaml`, not as separate gene reviews.

## Key references

- PMID:12359713 — Terao et al. 2002, J Biol Chem. Original FbaB characterization
  (Fn binding; adhesion/invasion; LPXTG; virulence). Abstract-only in cache.
- PMID:22366317 — Zakeri et al. 2012, PNAS. SpyTag/SpyCatcher from the CnaB2 domain.
- PMID:24161952 — Li et al. 2014, J Mol Biol. SpyCatcher:SpyTag structure/optimization.
- PMID:31822621 — Keeble et al. 2019, PNAS. SpyTag003/SpyCatcher003.
- PMID:40531663 — Ralston et al. 2025, J Synchrotron Radiat. ALS-ENABLE; 9OJ3 case study.
- PMID:26032562 — Walden et al. 2015, eLife. Internal thioester (SfbI) covalent host
  binding — background for the FbaB TED domain.
