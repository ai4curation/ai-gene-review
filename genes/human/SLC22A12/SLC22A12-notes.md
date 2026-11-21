# SLC22A12 (URAT1) — curation notes

UniProt: Q96S37 (S22AC_HUMAN). Gene: SLC22A12 / URAT1 / OATL4 / RST. HGNC:17989.
553 aa, 12-TM MFS transporter (SLC22 / organic cation transporter family, TC 2.A.1.19.11).

## Core identity

SLC22A12 encodes **URAT1**, the renal apical **urate/anion exchanger (antiporter)** that
mediates reabsorption of urate from the tubular lumen across the brush-border (apical)
membrane of the renal proximal tubule. It is the major molecular determinant of serum
urate and the pharmacological target of uricosuric drugs.

- **Molecular identification / mechanism** [PMID:12024214 "Here we identify the long-hypothesized urate transporter in the human kidney (URAT1, encoded by SLC22A12), a urate anion exchanger regulating blood urate levels and targeted by uricosuric and antiuricosuric agents"].
- UniProt FUNCTION (curated, ECO:0000269): [UniProtKB:Q96S37 CC:FUNCTION "Electroneutral antiporter that translocates urate across the apical membrane of proximal tubular cells in exchange for monovalent organic or inorganic anions"] and [UniProtKB:Q96S37 CC:FUNCTION "Mediates urate uptake by an exchange with organic anions such as (S)-lactate and nicotinate, and inorganic anion Cl(-)"].
- The transporter itself is **Na+-independent**; the inward urate flux is driven by the outward gradient of monocarboxylate counter-anions (lactate, nicotinate, pyrazinoate), which is maintained by separate Na+-monocarboxylate cotransporters (SMCT1/2). This is the tertiary-active "urate trap" model, mirroring the OAT3 organic-anion:dicarboxylate exchanger mechanism (its sister transporter SLC22A8).
- **Km(urate) = 371 uM** [UniProtKB:Q96S37 CC:BIOPHYSICOCHEMICAL PROPERTIES].
- UniProt curates four exchange catalytic activities (Rhea) to the Enomoto paper: urate(out)/(S)-lactate(in) (RHEA:72003), nicotinate(in)/urate(out) (RHEA:72023), urate(out)/n chloride(in) (RHEA:72319), and orotate(out)/nicotinate(in) (RHEA:72039; orotate from PMID:21350910).

## Location

- **Apical plasma / brush-border membrane** of proximal tubule epithelial cells
  (multi-pass membrane protein) [UniProtKB:Q96S37 CC:SUBCELLULAR LOCATION "Apical cell membrane"].
  EXP/IDA support: PMID:12024214, PMID:22194875, PMID:35144162, PMID:35462902.
- Brush border membrane ISS from mouse ortholog (Q8CFZ5); NAS from PMID:12024214.
- Kidney-enriched expression; proximal tubule epithelial cells of renal cortex
  [UniProtKB:Q96S37 CC:TISSUE SPECIFICITY "Detected in epithelial cells of proximal tubules in renal cortex"].
- Also reported on human aortic vascular smooth muscle cell membrane (non-renal context)
  [PMID:16775029 "Expression of URAT1 was localized to the cell membrane"]; proposed relevance to urate entry in vascular disease.
- Detected in urinary exosomes by LC-MS/MS (shed renal membrane protein, not a functional site) [PMID:19056867].

## Regulation / interactions

- **PDZK1** (NHERF3) scaffolds URAT1 at the apical brush border via its C-terminal PDZ
  motif and up-regulates transport activity [PMID:15304510 "The multivalent PDZ domain-containing protein PDZK1 regulates transport activity of renal urate-anion exchanger URAT1 via its C terminus"]; also PMID:14531806. This is the informative MF behind the bare protein-binding rows.
- A high-throughput fragmentomics PDZ-interactome screen (PMID:36115835) mapped URAT1's
  C-terminal PDZ-binding motif against many PDZ-domain proteins (PDZK1, DLG1/3/4, MAGI1/2,
  MPDZ, SCRIB, TJP1/ZO-1, PATJ, GRIP1/2, NHERF4, LNX1/2, APBA1/2, IL16, FRMPD2, GRID2IP).
  These 20 IPI rows are bare `GO:0005515 protein binding` and are PDZ-motif interactions
  already captured informatively by `GO:0030165 PDZ domain binding`; per the protein-binding
  policy the uninformative bare term is removed.
- Insulin stimulates renal urate reabsorption (URAT1 up-regulation); captured as an IEA
  `cellular response to insulin stimulus` transferred from the rat ortholog — a peripheral
  regulatory response.
- N-glycosylated [UniProtKB:Q96S37 CC:PTM "N-glycosylated"]; glycosylation characterized in PMID:35462902.

## Disease

- Loss-of-function variants cause **renal hypouricemia type 1 (RHUC1, MIM:220150)**:
  impaired tubular urate reabsorption, hypouricemia, high fractional urate excretion,
  predisposing to exercise-induced acute kidney injury and nephrolithiasis
  [UniProtKB:Q96S37 CC:DISEASE]. Many characterized RHUC1 missense variants reduce urate
  transport and/or membrane localization (e.g. R90H, T217M, E298D, G164S, Q382L, L418R,
  R434C/H), established in HEK293 uptake assays (PMID:12024214, PMID:14694169, PMID:15327384,
  PMID:15634722, PMID:22194875, PMID:26418379).
- Common variants influence serum uric acid in GWAS [PMID:19503597] (meta-analysis of
  uric acid loci).
- Drug target: uricosurics benzbromarone, probenecid, lesinurad, dotinurad, verinurad,
  sulfinpyrazone inhibit URAT1 (DrugBank/Guide-to-Pharmacology cross-refs in the UniProt record).

## Other substrates

- **Orotate** is transported by URAT1 coupled to nicotinate efflux (Cl-dependent),
  suggesting a role in renal orotate reabsorption [UniProt CC:FUNCTION, PMID:21350910;
  Km(orotate) = 5.2 uM]. A minor/secondary substrate relative to urate.

## Curation decisions (summary)

- Core MF: `GO:0015143 urate transmembrane transporter activity` (IDA, PMID:12024214;
  non-obsolete, verified QuickGO) — ACCEPT. Mechanism `GO:0015297 antiporter activity`
  is live and accurate but NOT currently in GOA → added as a conservative `NEW` row.
- The obsolete organic-anion grouping MF terms (GO:0008514, GO:0015347, GO:0015301) are
  deliberately avoided; no re-proposed grouping NTR.
- Core location: `GO:0016324 apical plasma membrane` / `GO:0031526 brush border membrane`.
- Bare `GO:0022857`, `GO:0055085`, `GO:0016020` are TOO_GENERAL (per 2026-11-14 maintainer
  ruling; no replacement) once the specific urate terms are asserted.
- Necessity vs participation: URAT1 *performs* urate transport (core); `urate metabolic
  process` (GO:0046415) is a transporter mis-fit (URAT1 does not metabolize urate) →
  MARK_AS_OVER_ANNOTATED; `cellular homeostasis`, `renal urate salt excretion`,
  `response to xenobiotic stimulus`, `cellular response to insulin stimulus` are genuine
  downstream/physiological roles → KEEP_AS_NON_CORE.
