# spuA (PA0297, Q9I6J4) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I6J4 --alias spuA`; accession matches the worklist.
Unreviewed entry. No deep-research provider was used. Literature: the cached seed paper
(abstract in cache; I read the PMC full text, PMC3147493, online), the cached full text of
Lu et al. 2002 (PMID:12081945, also the spuD/spuE source), and the 2021 SpuA structure paper
(PMID:34605433, cached with `ai-gene-review fetch-pmid`, abstract only). PubMed search was down
(NCBI 500); the structure paper was found through Europe PMC search.

### Literature

- PMID:12081945 (Lu et al. 2002, full text cached): the spuA mutant phenotype originates here
  [PMID:12081945 "Although spuA and spuB mutants showed an apparent defect in spermidine
  utilization, the biochemical functions of the gene products have yet to be elucidated."].
- PMID:21622750 (Yao et al. 2011, the PseudoCAP-cited paper). The abstract does not mention spuA.
  In the full text (read online, not in the cache) spuA is renamed pauD1, the only E. coli PuuD
  homologue in PAO1 (44% identity), and the spuA phenotype is restated as earlier work ("we
  reported previously that a lesion in pauD1 (spuA) causes a significant growth defect on Spd
  but not Put"). The 2011 paper constructed pauA mutants, not a new spuA mutant, so the IMP
  experiment is in PMID:12081945. Recorded as a PSEUDOCAP WRONG_REFERENCE defect, PROBABLE.
- PMID:34605433 (Chen et al. 2021): [PMID:34605433 "Activity and substrate-binding assays
  confirm that SpuA exhibits a preference for γ-Glu-GABA as a substrate."]; crystal structures
  with a glutamyl thioester intermediate place it in the class I glutamine amidotransferase
  family. A comparator class I GATase from M. smegmatis uses glutamine instead.
- Consistency with spuD/spuE (genes/PSEAE/spuD, spuE): those are the periplasmic binding
  proteins of the spuDEFGH transporter in the same locus; they sit in a different PANTHER family
  and do not share PTN000230196. Both reviews accept spermidine/putrescine uptake; this review's
  catabolic reading of spuA is consistent with them (uptake by SpuDEFGH, gamma-glutamylation
  catabolism by SpuI/SpuB/SpuA).

### Other seed of PTN000230196

E. coli PuuD P76038, queried live in QuickGO 2026-11-05: GO:0009447 putrescine catabolic process
(IMP, PMID:16499623) and GO:0033969 gamma-glutamyl-gamma-aminobutyrate hydrolase activity (IDA,
PMID:15590624). PuuD alone supports the polyamine catabolic process node term.

### Annotation decisions

- GO:0033969 (IBA, IEA): ACCEPT, core MF (activity assays, PMID:34605433).
- GO:0016787, GO:0016811 (IEA): TOO_GENERAL (GO:0033969 is_a GO:0016811).
- GO:0046203 spermidine catabolic process (IMP, seed): ACCEPT; citation defect only.
- GO:0006598 polyamine catabolic process (IBA): TOO_GENERAL (entailed by GO:0046203).
- GO:0006541 L-glutamine metabolic process (IEA, UniRule): MARK_AS_OVER_ANNOTATED; SpuA prefers
  gamma-Glu-GABA, and glutamine use is the comparator enzyme's property.
- Not added: GO:0009447 putrescine catabolic process. SpuA catalyses the last step of the
  putrescine gamma-glutamylation route, but the spuA mutant grows normally on putrescine, so I
  leave this as a question.
- Action counts: ACCEPT 3, TOO_GENERAL 3, MARK_AS_OVER_ANNOTATED 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000230196 | GO:0006598 polyamine catabolic process | 2 | 17 (13 taxa) | GO:0046203 spermidine catabolic process, IMP, PMID:21622750 (PseudoCAP) | SOUND | spuA mutant is defective in spermidine utilization, and SpuA hydrolyses gamma-Glu-GABA, a step of the gamma-glutamylation polyamine pathway, so it does part of the work. The cited paper restates the result; the experiment is in PMID:12081945 (WRONG_REFERENCE, PROBABLE). | E. coli PuuD P76038 (IMP putrescine catabolic process; IDA GO:0033969) | Yes; node term suits a PuuD-like clade |

PSEUDOCAP defects: 1 (WRONG_REFERENCE, PROBABLE). No GO_CENTRAL defect.

## Review session 2026-11-11 (gamma-glutamyl putrescine catabolism module)

A parallel review was written on the module branch (PR #6306) and reconciled
with the review above on merge (2026-11-13). Its sources were PMID:34605433,
PMID:21622750 (abstracts cached) and PMID:12081945 (full text cached); no
deep-research provider was run.

- "Activity and substrate-binding assays confirm that SpuA exhibits a
  preference for γ-Glu-GABA as a substrate" [PMID:34605433]; structures of the
  H221N mutant trap a glutamyl-thioester intermediate [PMID:34605433].
- SpuA was added as an experimentally characterized Pseudomonas representative
  of the PuuD step in the gamma-glutamyl putrescine catabolism module.

### Reconciliation (2026-11-13)

- GO:0006541: the module branch had REMOVE; the merged review keeps
  MARK_AS_OVER_ANNOTATED (glutamine use not tested on SpuA), now also matching
  the KT2440 PuuD-family paralogs after review of PR #6306.
- GO:0006598 (IBA): the module branch had MODIFY to putrescine plus spermidine
  catabolism; the merged review keeps TOO_GENERAL, entailed by GO:0046203,
  because the full text of PMID:21622750 reports that the spuA (pauD1) lesion
  impairs growth on spermidine but not putrescine. GO:0009447 is therefore not
  asserted and stays a suggested question.
- GO:0046203 (IMP): kept the WRONG_REFERENCE source defect (experiment in
  PMID:12081945).
- Added from the module branch: aliases, propagation_review on the IBA rows,
  the thioester-intermediate quote and a kinetics experiment.
