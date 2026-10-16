# ANKS4B notes

## Biology
- ANKS4B (also called Harp) is the ankyrin-repeat scaffold of the intermicrovillar adhesion complex (IMAC).
  - It localizes to microvillar tips and is essential for intermicrovillar adhesion [PMID:26812018].
  - Knockdown in CACO-2BBE cells abolishes clustering; rescue restores it [PMID:26812018].
- Partners:
  - Binds USH1C NPDZ1 through its SAM domain and class I PBM [PMID:26812018; PMID:15461667].
  - Binds the MYO7B cargo tail at a site distinct from USH1C; USH1C activation is needed for the tripartite complex [PMID:26812018].
  - The ternary complex has been characterized structurally [PMID:26812017], and it phase-separates [PMID:31644917].
- A cryptic apical targeting sequence, with a coiled coil and a basic-hydrophobic repeat, sends ANKS4B to the brush border [PMID:32636301].
- Mouse beta cells: Anks4b is an HNF4A target that binds GRP78 and enhances ER stress-induced apoptosis [PMID:22589549]. Abstract-only; this is the basis of the ISS rows.
- Zika/autophagy restriction [PMID:32793175]: an indirect phenotype, not used.

## GOA calls
- **ACCEPT:** microvillus, brush border, plasma membrane (via the membrane-binding repeat), cell projection, myosin binding, brush border assembly, protein localization to microvillus, and protein-containing complex assembly (IMP; scaffold of IMAC assembly).
  - IBA rows carry propagation_review on PTN008607450, seeded by mouse Anks4b and human ANKS4B.
- **Protein binding rows:**
  - USH1C rows → PDZ domain binding (GO:0030165).
  - MYO7B → myosin tail binding (GO:0032029) and adaptor activity (GO:0030674).
  - LRRK2 screen hits (two papers, neither discusses ANKS4B) → REMOVE.
- **UNDECIDED:**
  - Stereocilia ankle link (IDA, PMID:31644917): abstract-only. The abstract is about microvillar tip-link densities, not stereocilia ankle links.
  - ER membrane (ISS/IEA from mouse): the full text could not be retrieved, and the abstract has no ER localization.
- **KEEP_AS_NON_CORE:** response to ER stress (ISS).
- **Not proposed:** intermicrovillar adhesion (GO:0090675). It is part_of brush border assembly, which is already carried, and its comparators (CDHR2, CDHR5) are the adhesion molecules themselves; USH1C and MYO7B do not carry it.
