# mch (O26867, MTH_773) notes

Methanothermobacter thermautotrophicus Delta H,
N5,N10-methenyltetrahydromethanopterin cyclohydrolase (Mch, EC 3.5.4.27).
ARCHAEA project round 7: step 3 of CO2 reduction to methane (N5-formyl-H4MPT ->
methenyl-H4MPT+), reviewed so the hydrogenotrophic methanogenesis pathway can be
built as a module.

## Literature search

Deep-research providers were unavailable. PubMed E-utilities query
"methenyltetrahydromethanopterin cyclohydrolase" (24 hits), plus the Ftr search
(see ftr-notes.md). Cached and read (all abstract-only): PMID:3782039,
PMID:8617278, PMID:10545331, PMID:9676239, PMID:23013430, PMID:15752192,
PMID:8481088, PMID:3097011. The Delta H entry is PE 3 (inferred from homology);
there is no paper on the Delta H gene product itself, but the organism has a single
mch gene and the enzyme was purified from M. thermoautotrophicum cells.

## Enzyme from M. thermautotrophicus

- Purified from M. thermoautotrophicum (Wolfe lab; abstract names no strain):
  41 kDa subunit, apparent dimer, Mg2+-stimulated, equilibrium favours
  methenyl-H4MPT, folates are not substrates [PMID:3782039 "The
  5,10-methenyltetrahydromethanopterin cyclohydrolase of Methanobacterium
  thermoautotrophicum was purified 128-fold to homogeneity."; "Folate derivatives
  did not serve as substrates for this enzyme."].
- mch gene cloned from strain Marburg (now Methanothermobacter marburgensis);
  963 bp (320 aa, the same length as O26867); recombinant enzyme active in E. coli
  [PMID:8617278 "The mch gene was overexpressed in Escherichia coli yielding an
  active enzyme of 37 kDa with a specific activity of 30 U/mg cell extract
  protein."].
- Purified Mch with purified Ftr reconstituted methenyl-H4MPT formation from
  formyl-MFR and H4MPT [PMID:3097011 "Reconstitution of a portion of the
  methanogenic C1 cycle was effected by combining purified formyltransferase,
  methenyl-H4MPT cyclohydrolase, formylmethanofuran, and H4MPT to give
  methenyl-H4MPT."].

## Orthologues and structure

- M. kandleri Mch overproduced in E. coli [PMID:9676239] and crystallised
  (Grabarse et al. 1999): homotrimer, new alpha/beta fold, active-site pocket
  between two domains [PMID:10545331 "In the third step of this reaction sequence,
  N(5)-formyl-H(4)MPT is converted to methenyl-H(4)MPT(+) by the enzyme
  methenyltetrahydromethanopterin cyclohydrolase."]. Fold unlike the
  tetrahydrofolate cyclohydrolase/dehydrogenase (FolD), so not a FolD homologue.
- A. fulgidus Mch (Upadhyay et al. 2012): substrate complexes; Arg183 and Glu186
  catalytic; Glu186 sets N5- rather than N10-formyl product [PMID:23013430].
- A. fulgidus and M. kandleri Mch are cytoplasmic [PMID:8481088 "The two
  cytoplasmic enzymes were found to have very similar molecular and catalytic
  properties."].
- In Methanosarcina barkeri, an mch deletion blocks methanogenesis from H2/CO2
  [PMID:15752192 "Cell suspension experiments showed that methanogenesis from
  methanol or from H(2)/CO(2) is blocked in the mutant"]. Orthologue genetics.

## Annotation assessment

- GO:0018759 (IEA UniRule/EC/Rhea): ACCEPT, core. Rhea RHEA:19053
  (5,10-methenyl-H4MPT + H2O = N5-formyl-H4MPT + H+; CHEBI:58337, CHEBI:15377,
  CHEBI:58018). Physiological direction in CO2 reduction is formyl-H4MPT ->
  methenyl-H4MPT+ (dehydrative cyclisation), reverse of the Rhea left-to-right.
- GO:0019386: ACCEPT. GO:0006730: KEEP_AS_NON_CORE. GO:0005737: ACCEPT.
- PANTHER: no PANTHER DR line in the UniProt record.
- No new archaeal error pattern; all four rows true. Minor: Delta H Mch subunit
  composition reported as dimer (M. thermautotrophicus) vs trimer (M. kandleri,
  A. fulgidus structures); UniProt gives no SUBUNIT line.
