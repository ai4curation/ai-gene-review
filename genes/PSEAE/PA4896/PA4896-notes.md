# PA4896 (Q9HUR7) review notes

Reviewer: claude-code, 2026-11-05. PseudoCAP tier-2 IBA-seed batch (ECF sigma factors).

## Literature

- PA4896 is one of five uncharacterised P. aeruginosa ECF sigma factors whose regulons
  Llamas et al. defined by overexpression [PMID:18086184 "the ECF sigmas PA0149, PA1912,
  PA2050, PA2093 and PA4896 have been overexpressed and their target gene candidates have
  been identified using DNA microarray, proteomic analysis, and/or lacZ reporter construct"].
- Each sigma drives one TonB-dependent transducer, and the regulated transport systems
  are only putative [PMID:18086184 "although all these sigma factors seem to control
  putative (metal) transport systems"]. A ligand is identified only for FemI (PA1912). No
  ligand is reported for PA4896.
- Abstract only: no PMC copy (PubMed ID conversion returned no PMCID). A Europe PMC search
  for "PA4896 AND aeruginosa" (2026-11-05, 15 hits) found only transcriptome and
  iron-related papers that mention the locus in passing. None characterises its signal.
- Domain architecture (UniProt): Pfam Sigma70_r2 (PF04542) and Sigma70_r4_2 (PF08281),
  NCBIfam TIGR02937 sigma70-ECF, PANTHER PTHR43133:SF63 (FecI-related).

## Decisions

- Sigma factor activity rows (IBA, IEA, IMP): ACCEPT, core.
- GO:0006355 (IBA, IEA): MODIFY to GO:2000142, which the gene carries. GO:0003700:
  TOO_GENERAL, because GO:0016987 is_a GO:0003700. DNA binding: KEEP_AS_NON_CORE.
- GO:0034756 regulation of iron ion transport (IMP): UNDECIDED. The abstract names no
  iron substrate for PA4896. PSEUDOCAP source defect, SUSPECTED, CHECK.
- Cytosol (NAS): ACCEPT.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002455017 | GO:0016987 sigma factor activity | 16 | 250 (29 taxa) | GO:0016987, IMP, PMID:18086184 (PseudoCAP) | SOUND | The abstract states that overexpression drove a specific regulon (TonB-dependent transducer); genetic evidence for an ECF sigma with intact region 2 and 4.2 modules. Confidence limited to the abstract, but the call does not rest on what it omits. | 15 others (FecI, Mtb SigD/SigE/SigL, Sco SigR, 10 PAO1 ECF sigmas incl. PvdS and AlgU with in vitro transcription) | Yes |

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
