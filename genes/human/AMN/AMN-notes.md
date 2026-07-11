# AMN (amnionless) — review notes

UniProt: Q9BXJ7 (AMNLS_HUMAN), 453 aa, single-pass type I transmembrane glycoprotein.
Gene HGNC:14604, chromosome 14. HPA: group enriched in intestine, kidney, liver.

## Core biology

AMN is the membrane-anchoring / endocytic co-receptor subunit of the **cubam**
endocytic receptor, formed together with cubilin (CUBN). Cubilin is a ~460-kDa
peripheral protein with the ligand-binding CUB domains but **no transmembrane
segment and no endocytosis signals**; AMN supplies both.

- **Membrane anchorage**: AMN is a type I TM protein (TM 358–378 per UniProt FT);
  the crystal structure (PDB 6GJE) shows a three-faced β-helix domain in AMN docking
  a three-subunit cubilin β-helix, anchoring three ligand-binding cubilin chains to
  the membrane [PMID:30523278].
- **Trafficking / glycosylation**: AMN is required for correct N-glycosylation and
  cell-surface (apical) targeting of cubilin; without AMN, cubilin is retained in the
  ER/Golgi. IGS-causing AMN mutations (T41I, M69K, C234F) cause ER retention and loss
  of cubilin surface expression [PMID:14576052; PMID:29402915].
- **Endocytosis signals**: the AMN cytoplasmic tail carries two redundant FXNPXF
  internalization motifs (residues ~406–411 and ~441–446) that engage the
  clathrin-associated sorting adaptors ARH (LDLRAP1) and Dab2 to internalize cubam
  and its ligands via clathrin-coated pits [PMID:20088845].

## Function / localization
- Non-enzymatic. Molecular function is a **cargo receptor / membrane co-receptor**
  role (GO:0038024 cargo receptor activity), providing anchorage + endocytic signals.
- Localizes to **apical plasma membrane / microvillus (brush border) membrane** of
  ileal enterocytes and renal proximal tubule cells; cycles through endocytic
  vesicles / coated pits; endosome membrane. A soluble form is shed (secreted).
- BP: **cobalamin transport** (GO:0015889), **receptor-mediated endocytosis**
  (GO:0006898), renal protein absorption (kidney reabsorption of albumin, transferrin,
  apoA-I, vitamin D-binding protein via cubam).

## Disease
Imerslund-Gräsbeck syndrome 2 / megaloblastic anemia 1 (IGS2, MIM:618882): selective
intestinal B12 malabsorption + mild proteinuria; same disorder as CUBN mutations
(both cubam subunits) [PMID:14576052; PMID:29402915; PMID:26040326].

## Key references (all cached)
- PMID:14576052 (Blood 2004, abstract-only cache) — cubam = CUBN+AMN; AMN directs
  subcellular localization and endocytosis of cubilin+ligand; N-glycosylation; soluble form.
- PMID:20088845 (Traffic 2010, full text) — FXNPXF signals → ARH/Dab2 → clathrin endocytosis.
- PMID:29402915 (Sci Rep 2018, full text) — AMN glycosylation/trafficking required for
  cubilin surface targeting; IGS mutants ER-retained.
- PMID:30523278 (Nat Commun 2018, full text) — cubam crystal structure; 1 AMN : 3 CUBN.
- PMID:19056867 — urinary exosome proteomics (AMN detected; HDA extracellular exosome).

## Annotation review decisions (summary)
- ACCEPT core: cargo receptor activity (IBA+IDA); cobalamin transport (IDA); receptor-mediated
  endocytosis (IDA/IMP/IBA); apical plasma membrane / microvillus membrane / endocytic vesicle;
  plasma membrane (EXP/TAS/IEA); renal protein absorption (IBA); intracellular protein
  localization (IBA); Golgi to plasma membrane protein transport (IDA); cobalamin metabolic process.
- MARK_AS_OVER_ANNOTATED: signaling receptor complex (GO:0043235) and signaling receptor binding
  (GO:0005102) — cubam is a nutrient/cargo endocytic receptor, not a signaling receptor; these are
  IBA/IPI over-annotations toward a "signaling" framing. protein binding (GO:0005515, IPI) —
  uninformative bare term (the informative content is the CUBN interaction = cargo receptor/anchor).
- ACCEPT with KEEP_AS_NON_CORE: extracellular region / extracellular exosome / endosome membrane /
  membrane / protein-containing complex — peripheral/secreted-form/proteomic localizations.
