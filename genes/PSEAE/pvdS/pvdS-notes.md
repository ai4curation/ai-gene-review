# pvdS (PA2426, G3XCV1) review notes

Reviewer: claude-code, 2026-11-05. PseudoCAP tier-2 IBA-seed batch (ECF sigma factors).

## Literature

- pvdS is required for pyoverdine promoter expression and activates them in E. coli
  [PMID:7751284 "The pvdS gene is required for expression from promoters of at least two
  pyoverdine synthesis genes and can cause expression from these promoters in Escherichia
  coli, where they are otherwise inactive"]. A null mutant makes no pyoverdine
  [PMID:7651323]. pvdA transcription needs PvdS [PMID:8636031].
- Biochemistry: purified PvdS directs core RNAP to pvd promoters and transcribes them in
  vitro [PMID:10873648 "The purified protein caused core RNA polymerase from Escherichia coli
  to bind specifically to the promoters of pyoverdine synthesis genes and enabled
  transcription from these promoters in vitro"]. It forms 1:1 complexes with core RNAP
  [PMID:10692351 "it spontaneously forms 1:1 complexes with the core fraction of RNA
  polymerase"].
- The IS box is the PvdS -35 recognition element [PMID:11222621 "IS box elements
  participate in sequence-specific recognition by PvdS to enable initiation of transcription
  from pvd promoters"].
- PvdS also drives toxA, regA and ptxR [PMID:18048935]. Membrane retention of part of the
  PvdS pool is relieved by pyoverdine signalling [PMID:18047579]. pvdS is a Fur target
  [PMID:8633080].

## Decisions

- Sigma factor activity rows (IBA, IEA, 2 IDA): ACCEPT.
- GO:0006355 (IBA, IEA, IMP seed): MODIFY to GO:2000142.
- GO:1900378 (6 rows): MODIFY to GO:1900706 positive regulation of siderophore
  biosynthetic process. The VqsR paper (PMID:15073293) does not mention pvdS in its
  abstract: PSEUDOCAP WRONG_REFERENCE defect, SUSPECTED, CHECK.
- CollecTF rows: GO:0000976 MODIFY to GO:0001046; GO:0001216 MODIFY to GO:0016987;
  GO:0032993 KEEP_AS_NON_CORE; GO:0045893 MODIFY to GO:2000144.
- GO:0071281 cellular response to iron ion (EXP): KEEP_AS_NON_CORE. This is Fur acting on
  the pvdS promoter.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002455017 | GO:0016987 sigma factor activity | 16 | 250 (29 taxa) | GO:0016987, IDA, PMID:10692351 and PMID:10873648 (PseudoCAP) | SOUND | The abstracts state core-RNAP binding, holoenzyme promoter binding and in vitro transcription: direct evidence (CONFIRMED from abstract text). | 15 others (FecI, Mtb SigD/SigE/SigL, Sco SigR, 10 PAO1 ECF sigmas incl. PvdS and AlgU with in vitro transcription) | Yes |
| PTN002455017 | GO:0006355 regulation of DNA-templated transcription | 8 | 250 (29 taxa) | GO:0006355, IMP, PMID:7751284 (PseudoCAP) | SOUND | The abstract states loss- and gain-of-function control of pvd promoter expression. The term is general but correct; the gene-level row is refined to GO:2000142 without affecting the IBD. | 7 others (E. coli and V. cholerae RpoE, Mtb SigC/SigH/SigL/SigM, plus AlgU or PvdS) | Yes; this batch owns the node (no parallel-agent gene seeds it). No GO_CENTRAL defect. |

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
