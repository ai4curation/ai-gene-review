# fabB (PA1609) review notes

UniProt: Q9I3B2 (unreviewed, 405 aa), "3-oxoacyl-[acyl-carrier-protein]
synthase 1" (beta-ketoacyl-ACP synthase I, KAS I; EC 2.3.1.41). Locus PA1609,
cotranscribed with fabA.

## What is established

- fabA and fabB were cloned from P. aeruginosa and encode
  beta-hydroxyacyl-ACP dehydratase and beta-ketoacyl-ACP synthase I
  [PMID:9286984 "The Pseudomonas aeruginosa fabA and fabB genes, encoding
  beta-hydroxyacyl-acyl carrier protein dehydratase and beta-ketoacyl-acyl carrier
  protein synthase I, respectively, were cloned, sequenced, and expressed in
  Escherichia coli."]. They form an operon
  [PMID:9286984 "Northern analysis demonstrated that fabA and fabB are cotranscribed
  and most probably form a fabAB operon."].
- Chromosomal fabB mutants are auxotrophic for unsaturated fatty acids
  [PMID:9286984 "Chromosomal fabA and fabB mutants were isolated; the mutants were
  auxotrophic for unsaturated fatty acids."]. The same point is restated in the
  structural paper
  [PMID:35136566 "Cells lacking FabB are auxotroph for unsaturated fatty acids, making
  FabB an essential gene for the bacteria."].
- The reaction FabB performs in unsaturated fatty acid synthesis is elongation
  of the cis-unsaturated intermediate produced by FabA, so the auxotrophy is a
  direct consequence of the enzyme's own catalysis rather than a downstream
  effect
  [PMID:35136566 "FabB is able to catalyse the elongation of cis-3-decenoyl-ACP up to
  three times, and synthesise cis-5-dodecenoyl-ACP, cis-7-tetradodecenoyl-ACP and
  cis-9-hexadodecenoyl-ACP."]. FabB is not responsible for the final vaccenic
  acid step, which is FabF's
  [PMID:35136566 "In contrast, FabF but and not FabB was shown to be responsible for the
  condensation of cis-9-hexadodecenoyl-ACP to cis-11-octadodecenoyl-ACP, the last step
  for the synthesis of vaccenic acid."].
- The P. aeruginosa enzyme has been crystallised as the active-site C161A
  variant, confirming the condensing-enzyme architecture and the catalytic
  cysteine
  [PMID:35136566 "This structure can now serve as a template for the structure-based
  design of FabB inhibitors."].

So FabB has both a general role (chain elongation in fatty acid biosynthesis,
the KAS I condensation step) and a specific one it cannot be replaced in
(elongation of the unsaturated intermediate). Both GO:0006633 and GO:0006636 are
therefore kept on this gene: the general term is not merely entailed by the
specific one, because FabB also elongates saturated acyl-ACPs.

## Literature search

Europe PMC, 2026-11-05: `aeruginosa AND FabB AND "fatty acid"`. Cached and used:
PMID:9286984, PMID:35136566. Also returned: PMID:41652533 / PMID:38335573 on
fabF1/fabF2 and on FabB in P. putida, which corroborate the division of labour
between FabB and FabF but were not needed for the annotation calls.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000918584 | GO:0006633 fatty acid biosynthetic process | 8 | 436 (128 taxa) | GO:0006636 unsaturated fatty acid biosynthetic process, IMP, PMID:9286984 (PseudoCAP) | SOUND | The seed is a mutant phenotype, but for this gene the phenotype and the activity coincide: FabB is the condensing enzyme that elongates the cis-unsaturated intermediate, so an unsaturated-fatty-acid auxotrophy is the expected consequence of losing its own catalytic step, not an indirect downstream effect. The seeded node term is the parent GO:0006633, which is the right level for a node of KAS enzymes spanning bacteria, plants and the human mitochondrial OXSM; the seed's more specific GO:0006636 is a descendant, so it supports the node term without pushing a lineage-specific claim up the tree. | E. coli FabB (P0A953) and FabF (P0AAI5), M. tuberculosis KasA/KasB (P9WQD7, P9WQD9), human OXSM (Q9NWU1), Arabidopsis AT1G74960 (KASI), PAO1 Q9HU15 | Yes. E. coli FabB and FabF alone carry direct experimental support for fatty acid biosynthesis. No `GO_CENTRAL` defect. |

The `GO:0004315` IBD at the same node (7 seeds, this gene not among them) is
likewise sound: KAS I/II activity is the family-defining activity and PAO1 FabB
has been crystallised with the catalytic cysteine identified.

PseudoCAP defects from this gene: none. The seed cites the right paper for the
right locus, and the evidence it rests on is appropriate for the term.
