# mer (O27784, MTH_1752) notes

Methanothermobacter thermautotrophicus Delta H, coenzyme F420-dependent
N5,N10-methylenetetrahydromethanopterin reductase (Mer, EC 1.5.98.2). ARCHAEA
project round 7: step 5 of hydrogenotrophic methanogenesis (methylene-H4MPT to
methyl-H4MPT).

## Literature search

Deep-research providers were unavailable; no deep-research file was made. PubMed
E-utilities queries (2026-11-07): "methylenetetrahydromethanopterin reductase
structure Shima", "methylenetetrahydromethanopterin reductase F420", "Ma K Thauer
methylenetetrahydromethanopterin reductase". Cached and read (all abstract-only):
PMID:2298726 (Delta H purification, the GOA EXP reference), PMID:8522533 (Delta H
mer gene), PMID:2379499 (strain Marburg purification), PMID:1696553 (Blue
Sepharose affinity, F420-competitive), PMID:1953299 (M. kandleri Mer),
PMID:10891279 (Mer structures). PMID:9006047 and PMID:18487331 already cached.

## Activity (strain Delta H itself)

- Purified from strain Delta H; reduces methylene- to methyl-H4MPT with F420 as
  the specific cosubstrate; reversible, reduction favoured; single ~35 kDa
  subunit; no flavin, no Fe-S [PMID:2298726 "The enzyme catalyzes the reduction of
  5,10-methylene- to 5-methyltetrahydromethanopterin."; "The electron carrier
  coenzyme F420 is specifically used as the cosubstrate."; "The active enzyme does
  not contain a flavin prosthetic group or iron-sulfur clusters"].
- Gene cloned and sequenced from Delta H; monocistronic transcript, rising to a
  maximum at mid-exponential growth [PMID:8522533].
- Strain Marburg enzyme: specific for F420H2 (NADH, NADPH, reduced viologens
  inactive); colourless, no flavin or iron; ternary-complex mechanism; Km
  CH2=H4MPT 0.3 mM, F420H2 3 uM; kcat 3600 s-1; oxygen-stable [PMID:2379499].
- Binds Blue Sepharose competitively with F420, not with NAD, NADP, FAD, FMN
  [PMID:1696553 "Binding was competitive with coenzyme F420 rather than with NAD,
  NADP, FAD, FMN, AMP, ADP and ATP."].
- M. kandleri Mer: same F420 specificity, no prosthetic group, ternary complex,
  salt-activated [PMID:1953299].
- Rhea: RHEA:21144, 5-methyl-5,6,7,8-tetrahydromethanopterin + oxidized coenzyme
  F420-(gamma-L-Glu)(n) + H(+) = 5,10-methylenetetrahydromethanopterin + reduced
  coenzyme F420-(gamma-L-Glu)(n) (Rhea REST, ec:1.5.98.2). ChEBI: CHEBI:57818
  (methylene-H4MPT, 3-), CHEBI:139511 (reduced F420-(gamma-Glu)n), CHEBI:58116
  (5-methyl-H4MPT, 3-), CHEBI:133980 (oxidised F420-(gamma-Glu)n), CHEBI:15378.

## Structure: luciferase-like fold, no flavin

- Crystal structures of M. kandleri Mer and "M. thermoautotrophicum" Mer (tMer):
  TIM barrel with three insertions; F420 and methylene-H4MPT sites postulated in a
  cleft; most similar to FMN-dependent bacterial luciferase, but Mer lacks a
  prosthetic group [PMID:10891279 "It is composed of identical 35-40 kDa subunits
  and lacks a prosthetic group."; "It is surprising that Mer is structurally most
  similar to a bacterial FMN-dependent luciferase"].
- So the structural kinship with luciferase does not bring flavin or O2 chemistry:
  Mer transfers a hydride directly from F420H2 to methylene-H4MPT, ternary complex.

## InterPro2GO check (task lead)

- GOA row: GO:0016705 oxidoreductase activity, acting on paired donors, with
  incorporation or reduction of molecular oxygen, IEA GO_REF:0000002, from
  IPR011251 (Luciferase-like domain) and IPR036661 (Luciferase-like domain
  superfamily). Both entries carry GO:0016705 as their only GO mapping (InterPro
  API, 2026-11-07). GO:0016705 requires O2 to be reduced or incorporated (OLS
  definition). Mer uses no O2 and is oxygen-stable; it is a reductase with two
  organic substrates. REMOVE.
- No FMN binding or monooxygenase row reached this gene (no TreeGrafter row at
  all; PANTHER PTHR43244 is "FAMILY NOT NAMED", SF1 is
  5,10-METHYLENETETRAHYDROMETHANOPTERIN REDUCTASE).
- Scope (UniProt REST, 2026-11-07): of 450 UniProtKB entries with IPR019946 (Mer),
  446 carry GO:0016705. Of the 53 reviewed IPR011251 entries whose record
  mentions F420, 52 carry GO:0016705: 9 Mer, 23 F420-dependent glucose-6-phosphate
  dehydrogenases (Fgd), F420-dependent secondary alcohol dehydrogenase (Adf),
  mycobacterial F420-dependent ketoreductases and uncharacterised Mycobacterium
  proteins. None of these F420-dependent luciferase-like hydride transferases is
  O2-dependent. The mapping is right for the genuine flavin monooxygenases of the
  superfamily (bacterial luciferase LuxA, alkanesulfonate monooxygenase) and
  wrong for the whole F420-dependent clade. A scope problem: a curated rule or a
  narrower mapping could separate them (e.g. exclude members that match
  IPR019946, or the F420-dependent family entries).
- Candidate new archaea pattern: "a superfamily named after a flavin
  monooxygenase passes O2 chemistry to deazaflavin (F420) reductases" (relative of
  patterns 1 and 14: family-founder reaction inherited by divergent members).

## GO term label

- GO:0018537 label "coenzyme F420-dependent N5,N10-methenyltetrahydromethanopterin
  reductase activity" says methenyl, but its definition (OLS) is the Mer reaction:
  "5-methyltetrahydromethanopterin + coenzyme F420 + H+ =
  5,10-methylenetetrahydromethanopterin + reduced coenzyme F420". The label names
  the wrong substrate (methenyl-H4MPT is the Hmd/Mtd substrate), inviting
  confusion with GO:0030268 (Mtd) and GO:0047068 (Hmd). Recorded as a proposed
  NODE_RENAME to "coenzyme F420-dependent N5,N10-methylenetetrahydromethanopterin
  reductase activity". The term itself is correct for Mer, so the rows are
  accepted.

## Location

- UniProt: Cytoplasm (ECO:0000305). Soluble enzyme purified from extracts, F420
  and H4MPT are cytoplasmic coenzymes, no TM segment. IEA cytoplasm row accepted.
