# hmd (Q58194, MJ0784) notes

Methanocaldococcus jannaschii DSM 2661, H2-forming
N5,N10-methylenetetrahydromethanopterin dehydrogenase (Hmd), the
[Fe]-hydrogenase (5,10-methenyltetrahydromethanopterin hydrogenase, EC 1.12.98.2).
ARCHAEA project leads round ("Leads from round 7", pattern 1): Q58194 inherits P5C
reductase and proline biosynthesis IBA rows from PANTHER node PTN000182176. Kept
consistent with the M. thermautotrophicus review (genes/METTH/hmd/).

## Literature search

No deep-research file was made. PubMed E-utilities queries (2026-11-09):
"(Hmd OR Fe-hydrogenase OR [Fe]-hydrogenase) AND jannaschii", "[Fe]-hydrogenase OR
iron-sulfur cluster-free hydrogenase" (60 most recent), "Hiromoto T[au] AND
hydrogenase", "Shima S[au] AND hydrogenase AND review[pt]", "Hmd AND Rossmann",
"HmdII OR HmdIII paralog", "framework for H2 activation". RCSB PDB REST was used to
tie the six Q58194 PDB entries to their papers. The bgpt MCP was unavailable (quota).

Newly cached (all abstract-only): PMID:16887798 (Korbas 2006 JBC), PMID:19162018
(Hiromoto 2009 FEBS Lett, C176A), PMID:19623593 (Hiromoto 2009 Angew, substrate
complex; no abstract, not quoted), PMID:26094576 (HmdII, FEBS J 2015),
PMID:30600878 (bacterial HmdII), PMID:20235826 (Thauer 2010 Annu Rev Biochem),
PMID:37671838 (Shima 2023 review). Reused from the METTH review: PMID:1521540,
PMID:8383041, PMID:14686932, PMID:16540118, PMID:18653896, PMID:9477254,
PMID:18487331.

## Direct evidence on the M. jannaschii protein

The M. jannaschii protein (jHmd) is the workhorse of the structural studies, as
recombinant apoenzyme reconstituted with FeGP cofactor extracted from
M. marburgensis Hmd.

- Apoenzyme structure at 1.75 A (PDB 2B0J): homodimer, N-terminal Rossmann
  fold-like domain with a mononucleotide-binding site for the GMP moiety of the
  cofactor; Cys176 at the bottom of the intersubunit cleft, essential for activity
  [PMID:16540118 "We report here on the crystal structure of the Hmd apoenzyme from
  Methanocaldococcus jannaschii at 1.75 A"; "The Rossmann fold-like structure of
  the N-terminal domain contains a mononucleotide-binding site, which could harbour
  the GMP moiety of the cofactor"; "Cys176, which is located at the bottom of a
  deep intersubunit cleft and which has been shown to be essential for enzyme
  activity"].
- Reconstituted jHmd is active; XAS/Mossbauer of cysteine mutants identifies
  Cys176 as the sulfur ligand [PMID:16887798 "the active, reconstituted enzyme
  from Methanocaldococcus jannaschii (jHmd) revealed the presence of mononuclear
  iron with two CO, one sulfur and one or two N/O in coordination distance"; "In
  jHmd, the single sulfur ligand is most probably provided by Cys176"].
- Holoenzyme structure (PDB 3DAF, 3DAG; RCSB primary citation = Shima et al. 2008)
  [PMID:18653896 "showing a mononuclear iron coordinated by the sulfur of cysteine
  176, two carbon monoxide (CO) molecules, and the sp2-hybridized nitrogen of a
  2-pyridinol compound"]. The abstract does not name the organism; the PDB link
  and the Cys176 numbering (Q58194 residue 176 is Cys, my script) identify it.
- C176A mutant structure (PDB 3F46, 3F47) and the acyl-iron reinterpretation
  [PMID:19162018 "It suggests an iron center octahedrally coordinated by one
  DTT-sulfur and one DTT-oxygen, two CO, the 2-pyridinol's nitrogen and the
  2-pyridinol's 6-formylmethyl group in an acyl-iron ligation."].
- C176A holoenzyme with methylene-H4MPT (PDB 3H65; Hiromoto 2009 Angew,
  PMID:19623593; abstract absent in cache, so not quoted). This places the
  substrate next to the FeGP iron, the framework for hydride transfer.

Reaction (Rhea RHEA:20017; GO:0047068): 5,10-methenyl-H4MPT+ + H2 =
5,10-methylene-H4MPT + H+. The H2 is cleaved heterolytically at the FeGP iron and
the hydride goes directly to the methenyl carbon [PMID:37671838 "[Fe]-hydrogenase
catalyzes the heterolytic cleavage of H2 and reversible hydride transfer to
methenyl-tetrahydromethanopterin."]. No NAD(P)H or flavin is involved.

Kinetic characterisation of the native M. jannaschii enzyme from cells is not in
the cached abstracts; the biochemistry (Zirngibl 1992) is on the M. marburgensis
enzyme. Physiology: M. jannaschii is a hydrogenotrophic CO2-reducing methanogen;
the Hmd step is step 4 of CO2 reduction (UniPathway UPA00640), with Mtd as the
F420-dependent alternative (PMID:18487331, M. maripaludis genetics).

## Paralogs

M. jannaschii also has HmdII (and most hydrogenotrophic methanogens HmdIII). HmdII
binds FeGP and methylene-H4MPT but is inactive [PMID:26094576 "holo-HmdII did not
catalyze the Hmd reaction, not even in a single turnover process"]. So Q58194 is
the catalytic Hmd (HAMAP MF_01090, PIRSF500165 HMDI, NCBIfam TIGR01723); the
paralogs are not the subject of this review.

## PANTHER PTHR11645:SF0 and node PTN000182176

- UniProt: "PANTHER; PTHR11645:SF0; PYRROLINE-5-CARBOXYLATE REDUCTASE 3". The IBA
  rows for GO:0004735 and GO:0055129 come from root node PTN000182176, seeded only by
  real P5C reductases (E. coli and P. aeruginosa ProC, yeast PRO3, human
  PYCR1/2/3, mouse Pycr, M. tuberculosis ProC, Drosophila; paint.tsv).
- The family review (interpro/panther/PTHR11645/PTHR11645-review.yaml) already
  assesses this node NEEDS_PRUNING, names Q58194, and lists Q58194 as a
  member_exception for both FAMILY_WIDE term assessments.
- Phylogenetic reading: the seeds are all bacterial and eukaryotic ProC/PYCR; the P5C
  reductase seeds include no Hmd and no archaeal protein. Hmd is a methanogen lineage (plus the HmdII/HmdIII paralogs and a few
  bacterial HmdII) whose apoenzyme structure places in the Rossmann-like domain a site proposed to hold
  the GMP of the FeGP cofactor, and catalysis built at an intersubunit cleft around
  Cys176. Whatever the ancestral relationship to P5CR (the 6PGDH C-terminal-like
  and NAD(P)-binding Rossmann superfamilies are shared, SUPFAM), the Hmd branch is a
  neofunctionalized clade: different substrate (methenyl-H4MPT+), different reductant
  (H2, not NAD(P)H), and a unique organometallic cofactor. No paper reports P5C
  reductase activity, NAD(P)H binding, or P5C binding for any Hmd. The node
  assertion is sound for the ProC/PYCR clade, but Q58194 should be excluded by an
  IRD (or a NOT) at the Hmd branch. Pattern 1 (over-propagation to a
  neofunctionalized member).
- My pairwise check (hmd-bioinformatics/RESULTS.md): Smith-Waterman z-scores of
  Hmd against ProC, PRO3, PYCR1 and PYCR3 are 0.6 to 5.6 against shuffles (Hmd vs
  METTH Hmd: 175), and global identity sits at the shuffled baseline. The four
  P5CRs carry a [GA]x[GA]xx[GA] motif in residues 1-40; Hmd does not. So the
  P5CR relationship is remote, below pairwise detection, and no P5CR catalytic
  residue can be mapped onto Hmd by alignment. I did not find any literature
  mapping P5CR catalytic residues onto Hmd; I make no residue-level claim.
- Crosscheck with family_gene_crosscheck: see review log below.

## Decisions

- GO:0047068 IEA: ACCEPT (core; direct structural and reconstitution work on this
  protein).
- GO:0019386 IEA: ACCEPT.
- GO:0006730 IEA: KEEP_AS_NON_CORE (as for METTH hmd).
- GO:0004735 IBA: REMOVE, over-propagation (pattern 1), source defect to GO_CENTRAL.
- GO:0055129 IBA: REMOVE, same.
- NEW GO:0005737 cytoplasm (IC), as in METTH hmd.
- Proposed term reused: "iron-guanylylpyridinol cofactor binding".
