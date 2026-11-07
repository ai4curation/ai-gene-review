# hmd (O27211, MTH_1142) notes

Methanothermobacter thermautotrophicus Delta H, H2-forming
N5,N10-methylenetetrahydromethanopterin dehydrogenase (Hmd), the
[Fe]-hydrogenase (5,10-methenyltetrahydromethanopterin hydrogenase, EC 1.12.98.2).
ARCHAEA project round 7: step 4 of hydrogenotrophic methanogenesis, H2-dependent
alternative to Mtd (genes/METTH/mtd/).

## Literature search

Deep-research providers were unavailable; no deep-research file was made. PubMed
E-utilities queries (2026-11-07): "Fe-hydrogenase crystal structure active site
geometry Shima", "Hmd hydrogenase methanogenic", "Zirngibl Thauer", "Afting
Thauer", "light-sensitive iron-containing cofactor hydrogenase", "Pilak
Fe-hydrogenase apoenzyme", "Hiromoto Fe-hydrogenase", "iron-sulfur cluster-free
hydrogenase Hmd crystal", "Lyon EJ Shima 2004". Cached and read (all
abstract-only): PMID:1521540, PMID:1765081, PMID:8383041, PMID:14686932,
PMID:16540118, PMID:18653896, PMID:9477254, PMID:11081790, PMID:9006047;
PMID:18487331 (full text) was already cached. PMID:19623593 (Hiromoto 2009,
substrate complex) and PMID:15127449 (cofactor light-inactivation product) were
cached but have no abstract, so they are not cited. No paper reports a
biochemical assay of the Delta H Hmd protein itself: the Thauer-lab enzyme work
used strain Marburg (now M. marburgensis), M. jannaschii and M. kandleri.

## Identity of the gene product

- UniProt O27211 is PE 3 (inferred from homology); FUNCTION is by similarity
  (ECO:0000250). The characterised enzyme is M. marburgensis Hmd P32440 (GOA has
  EXP PMID:1521540 and IDA PMID:1765081 rows on it).
- My global pairwise alignment (Biopython PairwiseAligner, BLOSUM62, gap -10/-0.5;
  run in scratch, not saved as an analysis) gives 97.7% identity (336/344)
  between O27211 and P32440, and 66.9% to M. jannaschii Hmd Q58194. The cysteine
  that ligates the iron (Cys176 in the M. jannaschii structure, PMID:18653896,
  PMID:16540118) aligns to Cys172 of O27211, which is conserved. So the Marburg
  biochemistry transfers with high confidence.

## Activity

- Reversible dehydrogenation of methylene-H4MPT to methenyl-H4MPT+ and H2; a
  single 43 kDa polypeptide; no Fe-S clusters, nickel or flavins (as then
  understood) [PMID:1521540 "It catalyzes the reversible dehydrogenation of
  methylenetetrahydromethanopterin (CH2 = H4MPT) to methenyltetrahydromethanopterin
  (CH identical to H4MPT+) and H2"; "did not contain iron-sulfur clusters, nickel,
  or flavins"].
- Isotope studies: CH2=H4MPT + H+ <-> CH≡H4MPT+ + H2, dG0' +5 kJ/mol
  [PMID:8383041 "It catalyzes the reversible conversion of
  N5,N10-methylenetetrahydromethanopterin"].
- Hmd and Mtd are genetically distinct proteins [PMID:1765081 "No corresponding
  sequences were found indicating that the two dehydrogenases are genetically
  distinct enzymes."].
- Rhea: RHEA:20017, 5,10-methenyl-5,6,7,8-tetrahydromethanopterin + H2 =
  5,10-methylenetetrahydromethanopterin + H(+) (Rhea REST, ec:1.12.98.2). ChEBI:
  CHEBI:58337 (methenyl-H4MPT, 2-), CHEBI:18276 (dihydrogen), CHEBI:57818
  (methylene-H4MPT, 3-), CHEBI:15378 (H+). GO:0047068 has the same reaction
  (OLS definition).

## The FeGP cofactor

- 2004: Hmd contains about one functional Fe per subunit, tightly bound to a
  light-sensitive low-molecular-mass cofactor; CO inhibits and protects
  [PMID:14686932 "When purified in the dark, Hmd consistently contained per
  monomer about one Fe, which was tightly bound to the cofactor."; "reference to
  Hmd as 'metal-free' hydrogenase is no longer appropriate"].
- Apoenzyme structures (M. jannaschii, M. kandleri): homodimer; the iron is
  coordinated by two CO, one S and a pyridone linked by a phosphodiester to
  guanosine; Rossmann-like N-terminal domain binds the GMP moiety
  [PMID:16540118 "The iron is coordinated by two CO molecules, one sulphur and a
  pyridone derivative, which is linked via a phosphodiester bond to a guanosine
  base."].
- Holoenzyme structure: mononuclear Fe with Cys176 S, two CO and the
  sp2 N of the 2-pyridinol [PMID:18653896 "showing a mononuclear iron coordinated
  by the sulfur of cysteine 176, two carbon monoxide (CO) molecules, and the
  sp2-hybridized nitrogen of a 2-pyridinol compound"].
- GOA check (pattern 17): O27211 has NO metal-ion or iron-binding row and no
  cofactor-binding row at all, so the pattern 17 error (cofactor metal annotated
  as free metal ion binding) does not occur here. Instead there is no GO term to
  hold the right claim: GO has GO:0160300 iron-guanylylpyridinol cofactor
  biosynthetic process but no FeGP-cofactor binding MF (OLS search,
  "guanylylpyridinol", "FeGP cofactor"; GO:0048037 cofactor binding is obsolete).
  I do not add iron ion binding: that would recreate pattern 17. Proposed a new
  term instead.

## Physiology in Methanothermobacter

- Strain Delta H: the "mth" gene (= hmd, H2-dependent methenyl-H4MPT reductase)
  is transcribed under H2 excess, mtd under H2 limitation [PMID:9006047 "Under
  conditions of excess H2, ... transcription of the mth and mrt genes that encode
  the H2-dependent N5,N10-methenyltetrahydromethanopterin (methenyl-H4MPT)
  reductase (MTH)"].
- Nickel limitation (strain Marburg): F420-reducing [NiFe]-hydrogenase activity
  near zero; Hmd six-fold up, Mtd four-fold up; Hmd + Mtd then reduce F420 with H2
  [PMID:9477254 "the reduction of F420 with H2 is catalyzed by the metal-free
  methylenetetrahydromethanopterin dehydrogenase system"]. The rise is at least
  partly transcriptional and hmd expression is not H2-controlled in M.
  marburgensis [PMID:11081790 "the increase is due, at least in part, to
  increased expression of the hmd gene"]. Note the H2-control discrepancy with
  the Delta H transcription study (PMID:9006047); different strains and culture
  regimes.
- Genetics (M. maripaludis): Hmd-Mtd cycle can replace F420-reducing hydrogenase;
  hmd essential when fru and frc are deleted [PMID:18487331].

## PANTHER

- UniProt DR: PANTHER PTHR11645 (PYRROLINE-5-CARBOXYLATE REDUCTASE) and
  PTHR11645:SF0 (PYRROLINE-5-CARBOXYLATE REDUCTASE 3). UniProt query
  (2026-11-07): 43 of the 50 UniProtKB entries with IPR010062 (HMD) carry
  PTHR11645;PTHR11645:SF0. Hmd shares only the Rossmann-like N-terminal domain
  with P5C reductases.
- The PTHR11645 family review (interpro/panther/PTHR11645/PTHR11645-review.yaml)
  already flags root node PTN000182176 as NEEDS_PRUNING because it propagates
  GO:0004735 P5C reductase activity and GO:0055129 L-proline biosynthesis to Hmd.
  QuickGO (2026-11-07): M. jannaschii Hmd Q58194 carries both IBA rows; O27211
  and P32440 carry none. So the METTH gene escapes the error, but it is latent for
  any Hmd that PAINT reaches.

## Location

- No location row in GOA. Soluble single-polypeptide enzyme purified from cell
  extract; substrates are soluble C1 carriers; UniProt has no TM or signal
  peptide feature. Added cytoplasm (IC), matching mtd.
