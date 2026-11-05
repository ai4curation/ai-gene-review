# algU (PA0762, Q06198) review notes

Reviewer: claude-code, 2026-11-05. PseudoCAP tier-2 IBA-seed batch (ECF sigma factors).

## Literature

- Purified AlgT with E. coli core RNAP transcribes the algT promoter in vitro, and the
  activity depends on its -35 region [PMID:7644517 "The purified protein, in the presence of
  E. coli RNA polymerase core enzyme, was able to initiate transcription of an algT
  promoter"].
- AlgT is required for initiation at the algR and algD promoters [PMID:7928961] and
  directly for algZ [PMID:14645293, full text]. Ten more AlgU promoters were mapped
  [PMID:11807066, full text].
- Activation: MucA sequesters sigma-22. Cell wall stress releases it by AlgW- then
  YaeL-dependent regulated intramembrane proteolysis [PMID:19226327 "these data indicate
  that cell wall stress signals release sigma(22) by regulated intramembrane proteolysis
  (RIP)"].
- Downstream outputs: rpoH P3 and the heat response [PMID:9159526]; paraquat/heat
  resistance [PMID:7961422]; mexCD-oprJ induction [PMID:18838593]; biofilm via ppyR/psl
  (indirect) [PMID:20348252]; flagellar repression via fleQ [PMID:16291668].

## Decisions

- Sigma factor activity (IBA, IEA, IDA seed): ACCEPT. Cytosolic RNAP complex (IDA): ACCEPT.
- GO:0006355: MODIFY to GO:2000142. GO:0045893 (IEP x2): MODIFY to GO:2000144.
  GO:0003700: TOO_GENERAL.
- CollecTF: GO:0000976 MODIFY to GO:0001046; GO:0001216 MODIFY to GO:0016987; GO:0032993
  KEEP_AS_NON_CORE.
- GO:0006950 (ARBA): MODIFY to GO:0036460. GO:0036460: ACCEPT. GO:0032885 (x2): ACCEPT,
  because there is no alginate-specific term.
- Downstream phenotypes (antibiotic, heat, biofilm x2, motility, oxidative stress):
  KEEP_AS_NON_CORE.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002455017 | GO:0016987 sigma factor activity | 16 | 250 (29 taxa) | GO:0016987, IDA, PMID:7644517 (PseudoCAP) | SOUND | The abstract states in vitro transcription by reconstituted AlgT holoenzyme, dependent on the -35 region: direct (CONFIRMED from abstract text). | 15 others (FecI, Mtb SigD/SigE/SigL, Sco SigR, 10 PAO1 ECF sigmas incl. PvdS and AlgU with in vitro transcription) | Yes |
| PTN002455017 | GO:0006355 regulation of DNA-templated transcription | 8 | 250 (29 taxa) | AlgU is a WITH/FROM seed; no PseudoCAP GO:0006355 row on algU in current GOA (its experimental BP rows are on descendants) | SOUND (seed via descendant terms) | AlgU's IMP/IEP regulation-of-transcription descendants support it. | 7 others (E. coli and V. cholerae RpoE, Mtb SigC/SigH/SigL/SigM, plus AlgU or PvdS) | Yes; no GO_CENTRAL defect. |

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
