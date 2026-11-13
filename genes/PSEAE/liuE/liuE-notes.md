# liuE (PA2011) review notes

UniProt: Q9I2A0 (Swiss-Prot, 300 aa),
"3-hydroxy-3-isohexenylglutaryl-CoA/hydroxy-methylglutaryl-CoA lyase". Locus
PA2011, in the liuRABCDE cluster.

## What is established

- A liuE mutant cannot grow on leucine/isovalerate or on acyclic terpenes, and
  accumulates intermediates of the acyclic terpene pathway
  [PMID:19459965 "A mutant in the liuE gene (ORF PA2011) of P. aeruginosa was unable
  to utilize both leucine/isovalerate and acyclic terpenes as the carbon source."].
- Purified His-tagged LiuE has HMG-CoA lyase activity with measured kinetics
  [PMID:19459965 "LiuE showed HMG-CoA lyase optimal activity at a pH of 7.0 and 37
  degrees C, an apparent K(m) of 100 microM for HMG-CoA and a V(max) of 21 micromol
  min(-1) mg(-1)."], and the conclusion is stated directly
  [PMID:19459965 "These results demonstrate that the liuE gene of P. aeruginosa encodes
  for the HMG-CoA lyase, an essential enzyme for growth in both leucine and acyclic
  terpenes."].
- The same purified protein also has HIHG-CoA lyase activity
  (3-hydroxy-3-isohexenylglutaryl-CoA lyase, EC 4.1.3.26), the corresponding
  step of the acyclic terpene (citronellol) pathway
  [PMID:19597963 "The LiuE protein was purified as a His-tagged recombinant protein
  and in addition to show HMG-CoA lyase activity (Chávez-Avilés et al. 2009, FEMS
  Microbiol Lett 296:117-123), also displays HIHG-CoA lyase activity, indicating a
  bifunctional role in both the leucine/isovalerate and acyclic terpenes catabolic
  pathways."]. These are the two EXP rows in GOA, assigned by UniProt.
- The earlier cluster-level paper only inferred the activity
  [PMID:16517656 "The liuE gene encodes a probable hydroxy-acyl-CoA lyase (probably
  HMG-CoA lyase), an enzyme with bifunctional activity that is essential for both AMTC
  and leucine degradation."]; it also notes that the atu cluster lacks an HMG-CoA
  lyase homologue, which is why liuE serves both pathways.

LiuE therefore performs the terminal cleavage step of both pathways itself:
HMG-CoA to acetyl-CoA plus acetoacetate for leucine/isovalerate, and the
analogous HIHG-CoA cleavage for citronellol-family terpenes. Both process
annotations are participation, not necessity.

## The GO:0046951 (ketone body biosynthetic process) IBA

This row is not PseudoCAP-seeded: the GO:0046951 IBD at PTN000031222 is seeded
by mammalian and insect HMGCL/HMGCLL1 only (P35914, P35915, Q8TB92, RGD:620554,
FB:FBgn0031877). In vertebrate liver, HMG-CoA lyase catalyses the last step of
ketogenesis, and "ketone body biosynthetic process" names that physiological
programme. In P. aeruginosa the same chemistry is the terminal step of amino
acid and terpene catabolism; acetoacetate is produced as a catabolic
intermediate feeding central metabolism, not synthesised as a circulating fuel.
Propagating the term to the bacterial members of this node reads a
lineage-specific physiological process off shared chemistry, so the leaf row is
marked over-annotated with a `propagation_review`, and a `GO_CENTRAL` defect
asks PAINT to restrict that IBD to the animal clade. Confidence `PROBABLE`: the
chemistry and the seed list are checkable facts, but where exactly the node
should be cut is a judgement for the PAINT curator who placed it.

## Literature search

Europe PMC, 2026-11-05: `aeruginosa AND liuE`. Cached and used: PMID:19459965,
PMID:19597963, PMID:16517656. Also returned PMID:16820476 (genes and proteins
needed for acyclic terpene and leucine catabolism) and PMID:26162879 (AtuE
hydratase), consistent with the above but not needed for the calls.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000031222 | GO:0006552 L-leucine catabolic process | 3 | 183 (100 taxa) | GO:0006552, IMP, PMID:19459965 (PseudoCAP) | SOUND | The paper combines the growth phenotype with purified-enzyme kinetics in the same study, and HMG-CoA lyase catalyses the terminal step of leucine catabolism, so the gene product does part of the work of the process. | Mouse Hmgcl (MGI:96158) and Aspergillus Q5B2F7 | Yes, but with only two other seeds it is the thinnest of the node's IBDs; mouse Hmgcl carries the leucine-catabolism evidence independently. |
| PTN000031222 | GO:0004419 hydroxymethylglutaryl-CoA lyase activity | 7 | 183 (100 taxa) | GO:0004419, IMP, PMID:16517656 (PseudoCAP) | INDIRECT-PHENOTYPE | A molecular function coded IMP from a cluster-mutagenesis study that itself calls the assignment "probable" and sequence-based. The claim is right, and this gene's two UniProt EXP rows (PMID:19597963, PMID:19459965) are the proper evidence, so only the coding of this row is at issue. | Human/rat/mouse HMGCL (P35914, P35915, MGI:96158, RGD:620554), human HMGCLL1 (Q8TB92), Arabidopsis AT2G26800, and Q9I2A0's own EXP-backed annotation | Yes - the mammalian HMGCL enzymes are directly characterised. |

PseudoCAP defects from this gene: one `WRONG_EVIDENCE_CODE` (PROBABLE) on the
GO:0004419 IMP row. `GO_CENTRAL` defects: one (PROBABLE), on the GO:0046951 IBD
at PTN000031222, as described above.

## Leucine catabolism module review (merged from a concurrent curation branch)


- Reviewed as an experimentally characterized bacterial exemplar of the distal L-leucine catabolism module
  (`modules/leucine_catabolism.yaml`); the P. aeruginosa liuRABCDE cluster (PA2011-PA2016) carries the
  direct enzymology and genetics that the P. putida KT2440 orthologs lack.
- Deep research: no provider deep-research file was generated for this gene in this session. The review
  rests on the cached PubMed records cited in the review (PMID:16517656, PMID:16820476, PMID:16272386,
  PMID:18469096, PMID:18625020, PMID:19459965, PMID:19597963, PMID:22158123), all abstract-only except
  PMID:22158123, and on the UniProt record.
- Acyclic terpene terms: the Atu pathway joins the Liu pathway at methylcrotonyl-CoA
  [PMID:16272386 "enters that of leucine/isovalerate (Liu, leucine and isovalerate utilization) at the level of methylcrotonyl-CoA"],
  so enzymes downstream of that point perform steps of acyclic monoterpenoid catabolism; PseudoCAP
  isoprenoid/terpene rows are refined to GO:0016100 monoterpenoid catabolic process, matching the liuC review.
