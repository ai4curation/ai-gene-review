# spg1 (sid3; SPAC1565.06c; UniProt P87027) — curation notes

Session: 2026-09-27. Fission yeast Tem1/Spg1-family GTPase at the head of the septation
initiation network (SIN). Inputs: `spg1-uniprot.txt`, `spg1-goa.tsv` (22 rows),
`spg1-deep-research-falcon.md` (Edison), cached publications. Comparators:
`genes/yeast/TEM1/TEM1-ai-review.yaml` (complete MEN GTPase review), `genes/SCHPO/clp1/`,
`genes/SCHPO/cdc7/`. PomBase GO-CAM `gocams/66187e4700002284/` (septation initiation
signaling) models spg1/GTP twice: as GTPase activity and as signaling adaptor activity, both
occurring in the mitotic SPB, the adaptor node directly positively regulating Cdc7 kinase
activity and the GTPase node directly negatively regulating the adaptor node.

## Full-text availability

Abstract-only caches (curators read the full text; I did not): PMID:9203579, 9742395,
9420333, 10799520, 16787941, 16823372. Full text cached: PMID:19736319 (Etd1 paper).

## Holistic picture

- Identity: 198-aa Ras-superfamily small GTPase; 57% identical to S. cerevisiae Tem1; a
  distinct Tem1/Spg1 family closest to Rab/Ypt but lacking Rab-defining residues and the
  C-terminal CAAX motif [file:SCHPO/spg1/spg1-deep-research-falcon.md "Spg1 lacks the
  canonical C-terminal CAAX prenylation motif."]. UniProt: GTP-binding motifs 17-24, 65-69,
  122-125; CDD cd04128 "Spg1"; IPR017231 Small_GTPase_Tem1/Spg1.
- Founding paper [PMID:9203579 "The spg1 gene (septum-promoting GTPase) was cloned as a
  multicopy suppressor of a dominant-negative mutant of the Cdc7p kinase."]. Essential;
  null/ts alleles: no septum, growth/S-phase/mitosis continue, elongated multinucleate cells.
  Overexpression induces septation in G2, S and pre-Start G1 cells, requiring Cdc7 but not
  Cdc2; extra Cdc7 bypasses Spg1; Spg1-Cdc7 co-IP and two-hybrid [PMID:9203579 "Spg1p and
  Cdc7p can be coimmunoprecipitated from cell extracts, and interact in the two-hybrid
  system."].
- Biochemistry [PMID:9742395]: purified Spg1 binds and hydrolyses GTP; Byr4 alone inhibits
  GTP dissociation and hydrolysis; Byr4 + Cdc16 = two-component GAP; Cdc16 alone inactive;
  specific (no effect on seven Ypt GTPases) ["Byr4 and Cdc16 form a two-component GAP for
  the Spg1 GTPase."]. Deep research: >2/min combined dissociation+hydrolysis with Byr4-Cdc16
  vs ~0.2/min alone.
- Localisation and nucleotide-state asymmetry [PMID:9420333 "We demonstrate that Spg1p
  localizes to the spindle pole body in interphase and to both spindle poles during
  mitosis."; "Spg1p activity is required for localization of Cdc7p in vivo but not for its
  kinase activity in vitro."; GDP-Spg1-preferring antiserum: GTP-Spg1 predominates in mitosis
  when Cdc7 is on the SPB; Cdc7 asymmetry "may be mediated by inactivation of Spg1p on one
  spindle pole"]. Byr4 sits on SPBs lacking Cdc7; Byr4 overexpression displaces Spg1 and Cdc7
  from SPBs [PMID:10799520 "In contrast, Byr4 overexpression prevented Spg1 and Cdc7
  localization to SPBs."].
- Anchoring: Sid4-Cdc11 scaffold; Cdc11 N-terminus binds Spg1 (Morrell 2004, PMID:15062098,
  in UniProt SUBUNIT, not cached). Cached Cdc11 papers: "Spg1p, Sid2p, and Mob1p are detected
  at the SPB throughout the cell cycle" [PMID:12546793].
- Etd1 [PMID:19736319, full text]: binds Spg1 directly in vitro ["MBP-Etd1 (but not MBP) was
  specifically pulled down by GST-Spg1"]; partially activated spg1 allele suppresses etd1Δ;
  Etd1 needed for full Spg1 activation in late anaphase when spindle elongation brings the SPB
  to cell tips; "Spg1 is active at just one of the two SPBs during cytokinesis."; Etd1 loss
  from the half-cell with active Spg1 triggers Spg1 inactivation after ring constriction.
  GEF status open ["Although a GAP for Spg1 is known, no GEF has been identified."; binding
  persists in excess GppNHp, unlike most GEFs; no co-IP of endogenous proteins].
- Meiosis [PMID:16787941 "The SIN proteins localise to the spindle pole body in meiosis."];
  SIN mutants complete meiotic divisions but fail to encapsulate nuclei / form spores.
  Network-level phenotype; secondary role.

## Decisions

- GTPase activity (IBA/IDA/IEA), GTP binding (IBA/IDA/IEA): ACCEPT. Spg1 in its own
  WITH/FROM is the expected marker of target-level grounding.
- protein binding x3 (byr4 via PomBase and IntAct from PMID:9742395; etd1 from
  PMID:19736319): REMOVE per the GO:0005515 policy. The functional content lives on the
  regulators (GTPase activator activity on Byr4/Cdc16 and Etd1) and on Spg1's own GTPase / G
  protein activity. Interactions are not disputed.
- signaling adaptor activity (IDA PMID:9420333): MODIFY -> GO:0003925 G protein activity.
  GO:0035591's definition says adaptors "do not have catalytic activity"; Spg1 is a GTPase.
  GO:0003925 (is_a GTPase activity, is_a molecular function regulator; narrow synonym "small
  monomeric GTPase activity") is the GO term for a nucleotide-switch that binds effectors in
  its GTP state, and is what the TEM1 review proposed for the Tem1-Cdc15 relationship. Raised
  as a suggested question for PomBase rather than asserted as an error.
- SPB terms: spindle pole body IBA/IEA ACCEPT; mitotic SPB EXP/IDA/IDA/HDA ACCEPT (the
  PMID:9203579 IDA is not verifiable from the abstract; deferred to the curator, corroborated
  by PMID:9420333/10799520). Meiotic SPB IDA: KEEP_AS_NON_CORE (correct, secondary context).
- septation initiation signaling IGI (with cdc7): ACCEPT, core. Positive regulation of
  mitotic division septum assembly IMP/IBA: ACCEPT, core (Spg1 is the switch; a regulation
  term is the right relationship, it does not build the septum). Broad IEAs (intracellular
  signal transduction; positive regulation of cell cycle process): ACCEPT as true ancestors of
  the specific terms (checked via QuickGO: GO:0031028 is under GO:0035556 and GO:0007264;
  GO:0140281 is under GO:0090068).
- No NEW terms. Old/new mitotic SPB terms (GO:0071957/GO:0071958) were considered for
  core_functions locations but dropped: Spg1 protein is on both poles; the asymmetry is in
  nucleotide state, and PomBase's GO-CAM places both Spg1 activities in "mitotic spindle pole
  body". Sporulation process terms were not proposed (network-level phenotype; PomBase
  annotated only the meiotic SPB localisation to spg1 from PMID:16787941).
- core_functions: (1) G protein activity — GTP-Spg1 recruits Cdc7 to the SPB, initiating the
  SIN (septation initiation signaling; positive regulation of mitotic division septum
  assembly). (2) GTPase activity — Byr4-Cdc16-stimulated hydrolysis that keeps Spg1 off in
  interphase, inactivates it on the old SPB, and terminates signalling after ring
  constriction.

## Validation

`just validate SCHPO spg1`: valid, no errors. Rendered with `just render SCHPO spg1`.
