# mtd (Q50501, MTH_1464) notes

Methanothermobacter thermautotrophicus Delta H, coenzyme F420-dependent
N5,N10-methylenetetrahydromethanopterin dehydrogenase (Mtd, EC 1.5.98.1).
ARCHAEA project round 6; tests lead in annotation-patterns.md pattern 19
(InterPro2GO IPR002844 / IPR036080 -> GO:0008901 ferredoxin hydrogenase activity).

## Literature search

Deep-research providers were unavailable. PubMed E-utilities queries:
"F420-dependent methylenetetrahydromethanopterin dehydrogenase",
"methylenetetrahydromethanopterin dehydrogenase kandleri structure",
"methylenetetrahydromethanopterin dehydrogenase F420 purification",
"methylenetetrahydromethanopterin dehydrogenase Archaeoglobus",
"Hartmann GC Thauer 1996", "Afting Thauer Hmd nickel",
"mtd gene methanobacterium thermoautotrophicum". Cached and read (most are
abstract-only): PMID:1991149, PMID:4084309, PMID:7852356, PMID:8215796,
PMID:14499608, PMID:19761261, PMID:1521540, PMID:8599536, PMID:8481089,
PMID:1911853, PMID:11081790, PMID:9006047, PMID:7730278; PMID:18487331 (full
text) was already cached.

## Biochemistry (strain Delta H itself)

- Purified from strain Delta H; strictly F420-dependent, reversible, hexamer of
  36 kDa subunits, ternary-complex mechanism [PMID:1991149 "The methanogenic
  electron carrier coenzyme F420 was strictly required as the co-substrate.";
  "The dehydrogenase (Mr 216,000) was purified as an apparent hexamer of six
  identical 36 kDa subunits."].
- Independent purification: "The purified enzyme is absolutely dependent on
  coenzyme F420 ... for activity. Several alternative electron acceptors are
  ineffectual in the reaction." [PMID:4084309].
- Gene cloned from the closely related strain Marburg and expressed in E. coli;
  recombinant enzyme "strictly dependent on coenzyme F420"; no homology to the
  H2-forming enzyme (MTH = Hmd) [PMID:7852356 "no identifiable homology to MTH"].

## No metal, no H2, no ferredoxin

- M. kandleri F420-Mtd: colourless, no chromophoric prosthetic group, ternary
  complex mechanism [PMID:8215796 "in agreement with the finding that the enzyme
  lacked a chromophoric prosthetic group"].
- Crystal structure (M. kandleri): homohexamer (trimer of dimers), alpha/beta
  domain plus helix-bundle domain; "No structural similarities are detectable to
  other enzymes with F(420) and/or substituted tetrahydropterins as substrates."
  [PMID:14499608]. Substrate complexes show direct hydride transfer between
  methenyl-H4MPT+ C14a and F420H2 C5 in a face-to-face arrangement
  [PMID:19761261 "thereby ensuring a direct hydride transfer between their C14a
  and C5 atoms"]. So catalysis is a direct hydride transfer between two organic
  substrates with no metal or redox cofactor.
- Mtd activity does not require nickel [PMID:18487331 "the specific activities of
  Hmd and Mtd, neither of which requires nickel for activity, increased six- and
  fourfold"].
- Hmd (H2-forming methylene-H4MPT dehydrogenase, EC 1.12.98.2, GO:0047068) is the
  enzyme that uses H2 for the same C1 interconversion; it is a different protein
  [PMID:1521540; PMID:8599536 "contains neither nickel nor iron-sulfur
  clusters" (as then understood; Hmd was later shown to carry an iron-guanylylpyridinol
  cofactor, not cited here)]. Mtd and Hmd share no sequence homology [PMID:7852356].

## InterPro2GO verdict (IPR002844 / IPR036080 -> GO:0008901)

- GO:0008901 is defined as "2 reduced ferredoxin + 2 H+ = 2 oxidized ferredoxin +
  H2" (OLS). Mtd involves neither ferredoxin nor H2.
- IPR002844 and IPR036080 have identical membership: 169 proteins (InterPro API,
  queried 2026-11-07). UniProtKB query xref:interpro-IPR002844 returned 163
  entries, all named F420-dependent methylenetetrahydromethanopterin
  dehydrogenase (EC 1.5.98.1), 162 Methanobacteriota and 1 Halobacteriota, all
  Archaea; reviewed members include M. kandleri P94951, M. marburgensis P55300,
  A. fulgidus O29544, M. jannaschii Q58441, M. maripaludis, Methanosarcina,
  Methanosphaera. The InterPro entry description itself says the enzyme "requires
  coenzyme F420" and cites the Mtd EC number (old 1.5.99.9). No member is a
  hydrogenase. The mapping is wrong for every member: a clean InterPro2GO removal.
- Probable origin: confusion with Hmd (an H2-using methylene-H4MPT dehydrogenase,
  once called a "hydrogenase"), but this is not documented; cause left unstated.
- The same entries also map to GO:0015948 methanogenesis. That is true for the
  methanogen members but not for Archaeoglobus fulgidus (O29544), a sulfate
  reducer that uses Mtd in the oxidative direction [PMID:8481089 "The
  sulfate-reducing Archaeoglobus fulgidus contains a number of enzymes previously
  thought to be unique for methanogenic Archaea."]. Methanosarcina barkeri uses
  Mtd for methanol oxidation to CO2 [PMID:1911853 "Methylene reductase and
  methylene dehydrogenase are proposed to function in the methanol oxidation step
  to CO2."]. Flagged as a CHECK source defect (scope over-reach).

## Physiology in M. thermautotrophicus

- Obligate hydrogenotroph (H2 + CO2). Mtd catalyses step 4 of CO2 reduction to
  methane [PMID:14499608 "The fourth reaction step of CO(2)-reduction to methane
  in methanogenic archaea is catalyzed by coenzyme F(420)-dependent
  methylenetetrahydromethanopterin dehydrogenase (Mtd)."].
- Redundant with Hmd for methenyl-H4MPT reduction; mtd transcribed under H2
  limitation, mth (hmd) under H2 excess [PMID:9006047 "Under such H2-limited growth
  conditions ... the mtd and mcr genes ... were transcribed"].
- Under nickel limitation (M. marburgensis) Frh falls and Hmd/Mtd rise, so the
  Hmd-Mtd cycle can reduce F420 with H2; shown genetically in M. maripaludis
  [PMID:18487331]. In that cycle Mtd runs in the methylene-H4MPT oxidising
  direction, still within CO2-reducing methanogenesis.
- Location: no experimental localisation. Purified as a soluble hexamer, acts on
  soluble cytoplasmic C1 carriers and F420; no TM segment or signal peptide in
  UniProt features. Added cytoplasm (IC).

## Decisions

- GO:0030268 (defined with F420 as acceptor): ACCEPT, core.
- GO:0008901: REMOVE + INTERPRO source defect (DELETE_VALUE, CONFIRMED).
- GO:0015948: MODIFY -> GO:0019386 (organism is obligate CO2 reducer).
- GO:0019386: ACCEPT.
- GO:0006730: KEEP_AS_NON_CORE (true; no H4MPT-specific C1 process child exists).
- NEW GO:0005737 cytoplasm (IC).
