# fpvI (PA2387, Q9I193) review notes

Reviewer: claude-code, 2026-11-05. PseudoCAP tier-2 IBA-seed batch (ECF sigma factors).

## Literature

- fpvI deletion abolishes pyoverdine-dependent fpvA expression, and cloned fpvI stimulates
  it [PMID:12562796, full text]. A Fur box lies upstream of fpvI.
- FpvR inhibits FpvI; ferri-pyoverdine signalling through FpvA increases FpvI activity
  [PMID:12492864 "FpvR negatively regulates the activity of a second ECF sigma factor, FpvI,
  which is required for the synthesis of FpvA"]. Abstract only.
- Background: "Activated FpvI bound to the RNA polymerase initiates transcription of fpvA"
  [PMID:19730690].

## Decisions

- All sigma factor activity rows (IBA, IEA, IDA, 2 IMP): ACCEPT. The IDA from
  PMID:12492864 is deferred to the curator, because the abstract does not name the assay.
- GO:0006355: MODIFY to GO:2000142. GO:0003700: TOO_GENERAL. DNA binding: KEEP_AS_NON_CORE.
- Curation gap, not proposed as NEW: FpvI's process role in ferri-pyoverdine import
  (regulation of the fpvA receptor). No suitable regulation-of-siderophore-transport term
  was checked here.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002455017 | GO:0016987 sigma factor activity | 16 | 250 (29 taxa) | GO:0016987, IDA+IMP, PMID:12492864; IMP, PMID:12562796 (PseudoCAP) | SOUND | Loss- and gain-of-function control of fpvA transcription (full text of PMID:12562796 read) and FpvR-regulated FpvI activity. | 15 others (FecI, Mtb SigD/SigE/SigL, Sco SigR, 10 PAO1 ECF sigmas incl. PvdS and AlgU with in vitro transcription) | Yes |

### Node PTN002455017 (shared by the whole ECF sigma batch)

PTN002455017 is the ECF sigma factor clade of PANTHER PTHR43133 (250 leaf IBAs, 29
taxa). It carries two IBDs (`.cache/paint/IBD.gaf`):

- GO:0016987 sigma factor activity, 16 seeds: E. coli FecI (P23484), M. tuberculosis
  SigE (P9WGG7), SigL (P9WGH5) and SigD (P9WGG9), S. coelicolor SigR (Q7AKG9), and 11
  P. aeruginosa ECF sigmas: PA2093 (Q9I222), foxI (Q9I114), PA2050 (Q9I265), PA0149
  (Q9I6Y3), PA0472 (Q9I646), PA4896 (Q9HUR7), vreI (Q9I5P9), sigX (Q9I2W5), fpvI
  (Q9I193), algU (Q06198), pvdS (G3XCV1). Accessions were resolved against UniProt REST.
- GO:0006355 regulation of DNA-templated transcription, 8 seeds: M. tuberculosis SigC
  (P9WGH1), SigL (P9WGH5), SigH (P9WGH9) and SigM (O53590), V. cholerae RpoE (Q9KPA6),
  E. coli RpoE (P0AGB6), algU (Q06198), pvdS (G3XCV1).

Both node terms suit a clade made up entirely of ECF sigma-70 family proteins. The
GO:0016987 IBD has direct biochemical seeds: PvdS (PMID:10873648, in vitro transcription)
and AlgU (PMID:7644517, in vitro transcription). It also has well-characterised
non-Pseudomonas seeds. It stands without any single seed. The GO:0016987 node is also
seeded by PA2093, foxI, PA2050, PA0149 and PA0472, which the parallel agent is reviewing,
and any node-level GO_CENTRAL defect for it is recorded there. I found none to record.
None of those five genes seeds the GO:0006355 IBD, so its node assessment belongs to
this batch (pvdS, algU). It is sound, and no GO_CENTRAL defect is needed.

Cross-reference: the same node is assessed in the reviews of PA4896, vreI, pvdS, sigX, fpvI and algU (this batch) and of PA2093, foxI, PA2050, PA0149 and PA0472 (parallel agent).
