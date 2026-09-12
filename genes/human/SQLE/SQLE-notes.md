# SQLE (Q14534) review notes

Human squalene monooxygenase / squalene epoxidase. UniProt entry name ERG1_HUMAN. 574 aa.
EC 1.14.14.17. Gene on 8q24.1 [PMID:9286711 "human SQLE to 8q24.1"].

## Core biology (verified)

- FAD-dependent flavoprotein monooxygenase (epoxidase) that catalyzes the stereospecific
  oxidation of squalene to (S)-2,3-epoxysqualene (2,3-oxidosqualene), the first oxygenation
  step of sterol/cholesterol biosynthesis.
  - UniProt CATALYTIC ACTIVITY: squalene + reduced [NADPH--hemoprotein reductase] + O2 =
    (S)-2,3-epoxysqualene + oxidized [NADPH--hemoprotein reductase] + H2O + H(+);
    Rhea:RHEA:25282; EC=1.14.14.17.
  - [PMID:30626872 "SQLE is a flavin adenosine dinucleotide (FAD)–dependent epoxidase that
    catalyzes stereospecific conversion of non-sterol intermediate squalene to
    2,3(S)-oxidosqualene"] and "the first oxygenation step in cholesterol synthesis".
- Second rate-limiting enzyme of cholesterol biosynthesis, downstream of HMGCR.
  - [PMID:30626872 "SQLE is proposed to be the second rate-limiting enzyme of the cholesterol
    biosynthesis downstream of HMGCR"].
- Requires external NADPH-cytochrome P450 reductase as electron donor (Group E FAD
  monooxygenase). [PMID:30626872 "requires external NADPH-cytochrome P450 reductase (P450R)
  as an electron donor for squalene epoxidation"]. Also confirmed biochemically in
  [PMID:10666321] (Km squalene 7.7 uM; Km FAD 0.3 uM; NADPH-cytochrome P450 reductase is the
  requisite electron transfer partner).
- Cofactor: FAD (loosely bound). UniProt COFACTOR Name=FAD; ChEBI:57692. Structural FAD
  binding sites resolved in PDB 6C6N/6C6P/6C6R [PMID:30626872].

## Localization

- Endoplasmic reticulum / microsome membrane. Peripheral membrane protein — despite an
  N-terminal hydrophobic INTRAMEM region (21-41) and C-terminal hydrophobic helices, it has
  NO transmembrane helices (contrary to predictions).
  - UniProt SUBCELLULAR LOCATION: Microsome membrane; Endoplasmic reticulum membrane;
    Peripheral membrane protein.
  - Topology/membrane association shown in [PMID:26434806] (N100-GFP topology in ER membrane).
- GO annotations to `membrane` (GO:0016020) and `intracellular membrane-bounded organelle`
  (GO:0043231) from PMID:30626872 are correct but non-specific parents of ER membrane.

## Regulation (feedback, not core catalysis)

- N-terminal regulatory domain (first ~100 aa) senses cholesterol and mediates
  cholesterol-accelerated proteasomal degradation via the E3 ligase MARCHF6 (MARCH6).
  [PMID:26434806] cholesterol induces a conformational change in SM N100-GFP leading to
  ubiquitin-proteasome degradation. A 62-73 amphipathic degron is required
  (UniProt REGION 62-73; PMID:28972164, cited in UniProt but not in GOA).
- Transcriptionally a direct SREBP2 target; also transcriptionally upregulated by MYC
  [PMID:33791309 "Through transcriptional upregulation of SQLE ... MYC increases cholesterol
  production and promotes tumor cell growth"].

## Cancer / interactions (non-core)

- SQLE is a known oncogene / drug target in multiple cancers; SQLE knockdown decreases
  proliferation (MYC axis, CASIMO1 axis).
- Interacts with the microprotein CASIMO1 (SMIM22); this interaction modulates lipid droplet
  formation and SQLE protein accumulation [PMID:29765154]. This underlies the IMP annotations
  GO:0042127 (regulation of cell population proliferation) and GO:0140042 (lipid droplet
  formation) — these are downstream/contextual (cancer cell biology), not the core sterol
  enzyme function; treat as KEEP_AS_NON_CORE.
- Binary-interactome IPIs (GO:0005515 protein binding): HuRI [PMID:32296183] hits CREB3L1
  (Q96BA8), REEP4 (Q9H6H4), TMEM14B (Q9NUH8) — all in UniProt INTERACTION block; and
  K7EJ46 (SMIM22/CASIMO1 isoform) from [PMID:29765154]. Bare `protein binding` is
  uninformative per curation policy -> MARK_AS_OVER_ANNOTATED (not REMOVE, per policy on IPIs).

## Annotation-specific judgments

- GO:0004506 squalene monooxygenase activity: core MF. Multiple lines (EXP PMID:10666321,
  IDA PMID:30626872, IBA, IEA, NAS PMID:9286711). ACCEPT the experimental/IBA ones as core.
- GO:0006695 cholesterol biosynthetic process (IDA PMID:33791309; IC PMID:30626872) and
  GO:0016126 sterol biosynthetic process (IDA/IBA/IEA/NAS): both correct; sterol biosynthetic
  process is the broader classic BP, cholesterol biosynthetic process is the specific human
  pathway. Both ACCEPT (BP), core = cholesterol/sterol biosynthesis.
- GO:0071949 FAD binding (IDA PMID:30626872) and GO:0050660 flavin adenine dinucleotide
  binding (IEA): cofactor binding, real (structural FAD sites). Keep as non-core cofactor
  binding (the catalytic MF GO:0004506 is the core).
- GO:0005783 endoplasmic reticulum (IBA is_active_in) and GO:0005789 ER membrane
  (IDA PMID:26434806, IEA SubCell, TAS Reactome): correct CC; ER membrane is the specific
  location. ACCEPT.
- GO:0008203 cholesterol metabolic process (IEA ARBA): correct broad parent of cholesterol
  biosynthetic process; ACCEPT as non-core (biosynthesis is the specific role).
- GO:1904614 response to biphenyl (IEA GO_REF:0000107, Ensembl ortholog transfer from rat
  P52020): This is an ortholog-transferred "response to chemical" term based on rat data.
  It is a peripheral/response phenotype, not a core function; but it is an electronic ortholog
  transfer (not experimental). Given it is a narrow response term transferred by Ensembl from
  a single rat dataset with no human evidence and no obvious biological relevance to the core
  enzyme, MARK_AS_OVER_ANNOTATED (keep, flag as over-annotation), do not assert core.

## Core function synthesis

- MF: GO:0004506 squalene monooxygenase activity (FAD flavoprotein; squalene + O2 + NADPH ->
  (S)-2,3-epoxysqualene).
- BP: cholesterol biosynthetic process (GO:0006695) / sterol biosynthetic process (GO:0016126).
- CC: endoplasmic reticulum membrane (GO:0005789), peripheral membrane protein.
- Cofactor: FAD binding (GO:0071949).
