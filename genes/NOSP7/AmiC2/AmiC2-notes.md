# AmiC2 (Npun_F1846 / B2J2S4) — Nostoc punctiforme ATCC 29133 / PCC 73102 — Gene Review Notes

UniProt: **B2J2S4** (B2J2S4_NOSP7, unreviewed/TrEMBL), 616 aa, 67.2 kDa. Ordered locus
**Npun_F1846** (EMBL ACC80505.1). Taxon NCBITaxon:63737 (*Nostoc punctiforme* strain ATCC
29133 / PCC 73102). UniProt protein name "Cell wall hydrolase/autolysin", EC 3.5.1.28.
Evidence at protein level (PE 1). Encoded immediately downstream of its paralog
**AmiC1 = Npun_F1845 (B2J2S3)** — a tandem amidase pair mirroring the *Anabaena* PCC 7120
alr0092/alr0093 arrangement.

## Summary

**This is the directly characterised *N. punctiforme* AmiC2** — the subject of the
definitive biochemical, structural and cell-biological work on this enzyme, not merely an
ortholog inferred from another strain. AmiC2 is a secreted **cell-wall
N-acetylmuramoyl-L-alanine amidase** (EC 3.5.1.28) that hydrolyses the amide bond between
N-acetylmuramoyl residues and L-alanine in peptidoglycan (PG). Unlike the housekeeping AmiC
amidases of unicellular bacteria (which split the septum for daughter-cell separation), the
cyanobacterial AmiC2 **drills a regular array of nanopores into the septal cross-wall
(murein)**. These nanopores form the framework through which **septal junctions (SJs)**
thread to directly connect the cytoplasms of adjacent cells in the filament, enabling
intercellular exchange of metabolites and signalling molecules. This communication is a
prerequisite for multicellular behaviour, filament integrity and heterocyst
(N2-fixation cell) differentiation.

## Direct experimental evidence (this protein, Npun_F1846)

- **Crystal structure of the catalytic domain, PDB 5EMI**, X-ray 1.12 Å, residues 439-616
  in complex with Zn(2+) [file:NOSP7/AmiC2/AmiC2-uniprot.txt "X-RAY CRYSTALLOGRAPHY (1.12
  ANGSTROMS) OF 439-616 IN COMPLEX WITH ZN(2+)."; "PDB; 5EMI; X-ray; 1.12 A; A=439-616."].
  The AmiC2-cat structure "differs significantly from known structures of cell splitting
  and PGN recycling amidases" and has "A wide and shallow binding cavity" whose active site
  "harbors an essential zinc ion" [PMID:26833702]. The E. coli AmiC autoinhibitory α-helix
  is absent, and "AmiC2-cat exhibits strong hydrolytic activity in vitro" [PMID:26833702].
  A conserved-glutamate point mutation near the zinc abolishes activity, and zinc removal
  destabilises the domain [PMID:26833702 "A single point mutation of a conserved glutamate
  near the zinc ion results in total loss of activity, whereas zinc removal leads to
  instability of AmiC2-cat."]. => IDA amidase activity + IDA zinc ion binding.
- **Amidase activity in vivo and in vitro** [PMID:23444428 "The AmiC2 protein localizes to
  the young septum between cells and shows bona fide amidase activity in vivo and in
  vitro."].
- **Morphogene / multicellular-development phenotype (IMP).** Inactivation of the single
  *N. punctiforme amiC2* gene "completely changes the morphology and abrogates cell
  differentiation and intercellular communication" [PMID:21244533], establishing AmiC2 as
  "a novel morphogene required for cell-cell communication, cellular development and
  multicellularity" [PMID:21244533].
- **Nanopore drilling (IMP/IDA).** By EM of isolated PG sacculi, "AmiC2 drills holes into
  the cross-walls, forming an array of ~155 nanopores with a diameter of ~20 nm each"
  [PMID:23444428]; the enzyme "perforates the septal peptidoglycan creating an array of
  nanopores, which may be the framework for septal junction complexes" [PMID:28929086].
- **Localization (IDA).** "Immunofluorescence shows that native AmiC2 localizes to the
  maturing septum" [PMID:26833702]; "AmiC2-GFP localizes in the cell wall with a focus in
  the cross walls of dividing cells" [PMID:21244533].

## Protein family / domain architecture

- **AMIN domain** (InterPro IPR021731, Pfam PF11741; 2 copies in this protein) in the
  N-terminal region — a septal/PG-targeting module directing the enzyme to the division
  septum.
- **N-acetylmuramoyl-L-alanine amidase catalytic domain, Amidase_3 / MurNAc-LAA**
  (InterPro IPR002508, IPR050695, Pfam PF01520, SMART SM00646, CDD cd02696) in the
  C-terminal region (SMART domain 502..611) — a **Zn-dependent amidase**
  (SUPFAM SSF53187 Zn-dependent exopeptidases; Gene3D 3.40.630.40). PANTHER family
  **PTHR30404 / PTHR30404:SF0 "N-acetylmuramoyl-L-alanine amidase AmiC"**.
- Zn(2+)-binding residues from PDB 5EMI: positions **449, 464, 517**
  (ligand Zn(2+), ChEBI:29105) [file:NOSP7/AmiC2/AmiC2-uniprot.txt].
- The mature protein is exported (the sequence begins `MLSSPAMAA…`, a processed/secreted
  N-terminus), consistent with action in the periplasmic/cell-wall compartment where the
  septal PG resides.

## Ortholog relationship (RBH, context)

Reciprocal-best-hit analysis against *Nostoc/Anabaena* PCC 7120 (taxon 103690) confirms a
clean 1:1 ortholog assignment: **B2J2S4 (Npun_F1846) = AmiC2 ortholog of A0ACD7S2F2
(alr0093)** — forward best hit B2J2S4→A0ACD7S2F2 (~2e-272, ~71% identity) and reciprocal
best hit A0ACD7S2F2→B2J2S4, both ways ✓ [file:modules/septal_junction/RESULTS.md]. The
tandem paralog **B2J2S3 (Npun_F1845) = AmiC1 ortholog of alr0092**. Because B2J2S4 is itself
the experimentally assayed protein, evidence for its function is EXPERIMENTAL (IDA/IMP), not
ISS-by-orthology.

## Cellular localisation

AmiC2 localises to the newly formed division septum / cross-wall (the periplasmic cell-wall
compartment where septal PG lies): immunofluorescence to the maturing septum [PMID:26833702]
and AmiC2-GFP focused in the cross walls of dividing cells [PMID:21244533]. The GOA CC
annotation (GO:0030288 outer membrane-bounded periplasmic space, TreeGrafter) is a
defensible compartment call for a secreted amidase of a diderm (outer-membrane-bearing)
cyanobacterium acting on periplasmic septal PG; the experimentally supported and more
informative location is the **cell septum (GO:0030428)**.

## Relationship to AmiC1 (Npun_F1845)

AmiC1 is the adjacent tandem paralog. In *Anabaena* PCC 7120 the two amidases are partly
redundant for nanopore formation and cell–cell communication [PMID:28929086]. In
*N. punctiforme*, however, *amiC1* could not be inactivated and **AmiC2 alone is essential**
for multicellular development [PMID:21244533]. Care was taken here to attribute results to
the amidase actually assayed (Npun_F1846 / AmiC2), distinct from Npun_F1845 / AmiC1.

## Cited references (verified via cached publications/)

- PMID:26833702 — Büttner et al. 2016, FEBS J — structure/function/localization of
  *N. punctiforme* AmiC2; crystal structure PDB 5EMI, essential active-site zinc, strong in
  vitro hydrolytic activity. Abstract cached (full_text_available: false).
- PMID:21244533 — Lehner et al. 2011, Mol Microbiol — "The morphogene AmiC2 is pivotal for
  multicellular development in *Nostoc punctiforme*." Morphogene phenotype, AmiC2-GFP
  cross-wall localization. Abstract cached.
- PMID:23444428 — Lehner et al. 2013, FASEB J — "Prokaryotic multicellularity: a nanopore
  array for bacterial cell communication." Nanopore drilling (~155 pores, ~20 nm), amidase
  activity in vivo and in vitro. Abstract cached.
- PMID:28929086 — Bornikoel et al. 2017, Front Cell Infect Microbiol — *Anabaena* PCC 7120
  amiC1/amiC2 mutants, nanopores, FRAP, heterocysts; cited for mechanism context. Full text
  cached.
- PMID:23463784 (UniProt reference 2) is a *N. punctiforme* sugar-transporter/symbiosis
  paper unrelated to AmiC2 function — a genome/sequence reference only; not cited.
