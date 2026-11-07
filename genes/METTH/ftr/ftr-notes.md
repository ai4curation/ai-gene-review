# ftr (P21348, MTH_1259) notes

Methanothermobacter thermautotrophicus Delta H,
formylmethanofuran:tetrahydromethanopterin formyltransferase (Ftr, EC 2.3.1.101).
ARCHAEA project round 7: step 2 of CO2 reduction to methane (formyl-MFR ->
5-formyl-H4MPT), reviewed so the hydrogenotrophic methanogenesis pathway can be
built as a module.

## Literature search

Deep-research providers were unavailable. PubMed E-utilities queries:
"formylmethanofuran tetrahydromethanopterin formyltransferase" (23 hits) and
"Ermler U[au] AND formyltransferase". Cached and read (all abstract-only):
PMID:2403564, PMID:3097011, PMID:9195883, PMID:16466742, PMID:1483480,
PMID:7601152; PMID:8481089 was already cached (round 6, mtd).

## Enzyme from M. thermautotrophicus

- Gene cloned and sequenced from strain Delta H (this entry's reference 1);
  functional enzyme expressed in E. coli [PMID:2403564 "When this fragment was
  subcloned into the phagemid pTZ18R, a functional enzyme was synthesized under
  control of the lac promoter."]. Unrelated to other pterin-using proteins
  [PMID:2403564 "The sequence of FTR does not appear to be homologous to any
  other sequenced proteins, including proteins which use pterin substrates."].
- Purified from M. thermoautotrophicum cells (Wolfe lab; the abstract does not
  name the strain) as a tetramer; the product is 5-formyl-H4MPT
  [PMID:3097011 "The enzyme is a tetramer of similar or identical subunits (Mr =
  41,000)."; "The product of formyl transfer by the purified enzyme was shown by a
  number of criteria to be 5-formyl-H4MPT, as opposed to 10-formyl-H4MPT or
  5,10-methenyl-H4MPT."].
- Reconstitution with purified Mch gave methenyl-H4MPT, and Ftr was essential for
  CO2 -> CH4 in reconstituted extracts [PMID:3097011 "Additional reconstitution
  experiments established that the formyltransferase is an essential enzyme for
  the conversion of carbon dioxide to methane."]. This is participation, not only
  necessity: Ftr catalyses the C1 transfer step itself.

## Orthologue biochemistry and structure (Methanopyrus kandleri)

- Purified M. kandleri Ftr: ternary-complex mechanism, absolutely dependent on
  lyotropic salts (adaptation to high intracellular salt) [PMID:1483480 "The
  catalytic mechanism of formyltransferase was determined to be of the
  ternary-complex type."].
- Recombinant M. kandleri Ftr has native properties [PMID:7601152].
- Crystal structure (Ermler et al. 1997): homotetramer of two dimers, each subunit
  two alpha/beta lobes, active site near the dimer interface [PMID:9195883 "The
  crystal structure of Ftr, determined to a resolution of 1:73 AE reveals a
  homotetramer composed essentially of two dimers."].
- Coenzyme complex (Acharya et al. 2006): no prosthetic group; methanofuran bound
  at the dimer interface; conserved Glu245 stabilises the oxyanion intermediate
  after N5 of H4MPT attacks the formyl carbon [PMID:16466742 "The enzyme, which is
  devoid of a prosthetic group, catalyzes the reversible formyl transfer between
  the two substrates coenzyme methanofuran and coenzyme tetrahydromethanopterin
  (H4MPT) in a ternary complex catalytic mechanism."].
- Family is also present in sulfate-reducing archaea (A. fulgidus) and
  methylotrophic bacteria [PMID:16466742 "is an essential enzyme in the one-carbon
  metabolism of methanogenic and sulfate-reducing archaea and of methylotrophic
  bacteria."]; in M. extorquens the homologue is the FhcD subunit of the
  formyltransferase/hydrolase complex (not cached, not cited).

## Annotation assessment

- GO:0030270 (IEA UniRule/EC/Rhea): ACCEPT, core. Rhea RHEA:18061
  (N-formylmethanofuran + H4MPT + H+ = N5-formyl-H4MPT + methanofuran; CHEBI:57727,
  CHEBI:58103, CHEBI:58018, CHEBI:58151).
- GO:0016740 transferase activity (InterPro2GO, IPR002770 C-terminal and IPR022667
  N-terminal Ftr domain entries): correct but general; MODIFY to GO:0030270. Both
  domain entries are Ftr-specific (IPR022667: 920 proteins), so the family-wide
  mapping could be the specific term; logged as a suggested question, not a defect.
  GO:0030270 is_a GO:0016747 is_a GO:0016746 acyltransferase is_a GO:0016740 (OLS).
- GO:0019386 methanogenesis from CO2: ACCEPT (obligate hydrogenotroph; catalyses
  step 2).
- GO:0006730 one-carbon metabolic process: KEEP_AS_NON_CORE (as mtd).
- GO:0005737 cytoplasm: ACCEPT; soluble enzyme purified from cell extracts, no TM
  or signal peptide, coenzyme substrates are cytoplasmic.
- PANTHER: no PANTHER DR line in the UniProt record.
- No new archaeal error pattern: all five rows are true; the only issue is a
  general InterPro2GO MF term on Ftr-specific domain entries (pattern 6-like).
