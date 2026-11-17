# vreI (PA0675, Q9I5P9) review notes

Reviewer: claude-code, 2026-11-05. PseudoCAP tier-2 IBA-seed batch (ECF sigma factors).

## Literature

- VreI is the ECF sigma of the PUMA3 CSS system with VreA (PA0674, periplasmic
  receptor-like) and VreR (PA0676, sigma factor regulator) [PMID:19730690, full text].
- Overexpression induces the regulon [PMID:19730690 "overexpression of vreI upregulates 30
  genes"], including the Hxc type II secretion system, a two-partner secretion system and
  exbBD homologues.
- VreR is both required for VreI activity and inhibitory [PMID:19730690 "In conclusion,
  VreR is an anti-sigma regulator for VreI that is both required for the function of VreI
  and inhibits its activity under non-inducing conditions."].
- VreI is in the cytosolic fraction unless VreR tethers it [PMID:19730690 "VreI is
  associated to the membrane through the VreR sigma factor regulator"].
- PUMA3 regulates virulence in zebrafish embryos [PMID:19730690]. The Chevalier et al.
  review calls it "the unorthodox σVreI involved in the expression of virulence"
  [PMID:29729420].
- Domain note: UniProt lists only Pfam Sigma70_r4_2 (PF08281). There is no Pfam Sigma70_r2
  hit, though the InterPro sigma region 2 superfamily (IPR013325) and TIGR02937 match, so
  region 2 is divergent.

## Decisions

- Sigma factor activity rows: ACCEPT. GO:0006355 rows: MODIFY to GO:2000142. GO:0003700:
  TOO_GENERAL. DNA binding: KEEP_AS_NON_CORE. Cytosol (NAS): ACCEPT, supported by the
  fractionation data.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002455017 | GO:0016987 sigma factor activity | 16 | 250 (29 taxa) | GO:0016987, IMP, PMID:19730690 (PseudoCAP) | SOUND | Full text read: overexpression-driven target induction (microarray, RT-PCR, lacZ) that requires VreR. Genetic, not biochemical, but the expected evidence for an ECF sigma. Caveat: divergent region 2. | 15 others (FecI, Mtb SigD/SigE/SigL, Sco SigR, 10 PAO1 ECF sigmas incl. PvdS and AlgU with in vitro transcription) | Yes |

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
