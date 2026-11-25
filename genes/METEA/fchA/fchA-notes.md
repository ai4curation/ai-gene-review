# fchA (MexAM1_META1p1729, UniProtKB:Q49135) curation notes

## Deep research status

`just deep-research-falcon METEA fchA` was attempted on 2026-11-13 and failed
(Edison API 403, "Failed to authenticate"). These notes are a manual literature
survey. PubMed searches (2026-11-13): `fchA Methylobacterium` -> 35051495;
`Crowther formate main branch point methylotrophic` -> 18502865; UniProt references
PMID:7961516, PMID:10215859. All cached as abstracts only. Full text of
PMID:10215859 (Wiley) returned HTTP 403.

## Identity

- fchA was first described as `orf4` in the serine-cycle gene cluster
  [PMID:7961516 "The first of the full open reading frames (orf4) remains
  unidentified"]. Pomper et al. 1999 purified methenyl-H4F cyclohydrolase and
  identified its gene via N-terminal sequencing (UniProt: "PROTEIN SEQUENCE OF
  1-21" from PMID:10215859).

## Biochemistry

- M. extorquens AM1 has separate methenyl-H4MPT (Mch) and methenyl-H4F (FchA)
  cyclohydrolases, each specific for its substrate [PMID:10215859 "Both enzymes,
  which were specific for their substrates, were purified and characterized"].
- FchA: homodimer of 22 kDa subunits, specific activity 100 U/mg, Vmax 330 U/mg,
  Km 80 uM [PMID:10215859 "The methenyl H4F cyclohydrolase with a specific activity
  of 100 U x mg-1"]. Not homologous to classical FolD-type cyclohydrolase domains
  [PMID:10215859 "Its sequence was not similar to that of methenyl H4MPT
  cyclohydrolases or to that of other methenyl H4F cyclohydrolases"].
- Kim et al. 2022: kinetics show much higher cyclization (10-formyl-H4F ->
  methenyl-H4F) than hydrolysis; crystal structures apo (7VG4) and THF-bound (7VG5);
  substrate-binding residues verified by mutagenesis [PMID:35051495 "the enzyme has
  much higher cyclization than hydrolyzation activity"].
- In vivo direction: during methylotrophic growth the H4F pathway runs formate ->
  10-formyl-H4F -> methenyl-H4F -> methylene-H4F (assimilatory), so the physiological
  direction is cyclization (reverse of the EC 3.5.4.9 hydrolysis as written). GO
  MF terms are direction-neutral, so GO:0004477 covers it.

## Physiology

- orf4 (fchA) insertion mutants cannot grow on C1 compounds; also fail on C2 unless
  glyoxylate supplied [PMID:7961516 "Mutants in orf4 were also unable to grow on C2
  compounds, but growth was restored by glyoxylate"].
- Pomper et al. propose an anabolic role for FchA [PMID:10215859 "the methenyl-H4F
  cyclohydrolase an anabolic function in the C1-unit metabolism"].
- Crowther et al. 2008: mutants lacking the formate -> methylene-H4F enzymes show
  only minor C1 assimilation into biomass; formate is the main branch point
  [PMID:18502865 "only minor assimilation into biomass occurred in mutants lacking
  the methylene H4F synthesis pathway through formate"]. FchA is one of those enzymes
  (with FtfL and MtdA); the abstract does not name the genes.

## Localization

- UniProt states "Membrane; Single-pass membrane protein {ECO:0000305}" with a
  predicted TRANSMEM 25..46 (ECO:0000255). This is a sequence-prediction-based
  curator inference.
- Against membrane residence: (1) the same residues form helix 23..43 of the
  soluble up-and-down helical-bundle fold in the X-ray structures (FT HELIX
  23..43, ECO:0007829|PDB:7VG5); (2) the RCSB experimental record for 7VG5 lists
  crystallization by hanging-drop vapor diffusion with PEG 3350, MgCl2, Bis-Tris and
  no detergent, using PDB 1O5H (a soluble Thermotoga cyclohydrolase-like protein) as
  the search model (WebFetch of rcsb.org/experimental/7VG5, 2026-11-13); (3) the
  family (Pfam FTCD_C, IPR007044) is the soluble C-terminal domain of
  formiminotransferase-cyclodeaminase; (4) the enzyme was purified from cell
  extract as an active homodimer (PMID:10215859). The predicted TM is most likely a
  hydrophobic core helix of the bundle. One caveat: the full text of PMID:10215859
  was not accessible, so I cannot confirm whether the activity fractionated with
  the soluble fraction.

## Family

- No DR PANTHER line in UniProt.
- InterPro: IPR007044 (Cyclodeamin/CycHdrlase), IPR036178
  (Formintransfe-cycloase-like_sf), IPR054893 (MthfCyhylase). NCBIfam NF045657
  (MthfCyhylaseFchA). Pfam PF04961 (FTCD_C).

## Curation decisions

- GO:0003824 catalytic activity (InterPro2GO): MODIFY -> GO:0004477.
- GO:0004477 (EC mapping): ACCEPT, core.
- GO:0016020 membrane (SubCell): MARK_AS_OVER_ANNOTATED (prediction contradicted by
  structure; full text not seen, so not REMOVE).
- NEW GO:0035999 tetrahydrofolate interconversion (IC): FchA itself catalyses the
  interconversion of 10-formyl-H4F and 5,10-methenyl-H4F, so it does part of the
  process (participation test passes); bifunctional FolD-type enzymes that catalyse
  the same step are conventionally annotated to this term. GOA has no process row
  for fchA at all.
- Did not add GO:0019649 formaldehyde assimilation: the H4F branch assimilates C1
  units via formate (PMID:18502865), and a pathway-level term for serine-cycle
  methylotrophy is not available; recorded as a suggested question instead.
