# MCR1 review notes

## 2026-10-10

- Seeded `genes/yeast/MCR1` with `just fetch-gene yeast MCR1`, then fetched all GOA PMIDs
  with `just fetch-gene-pmids yeast MCR1`.
- Tried `just deep-research-falcon yeast MCR1 --fallback perplexity-lite`; both providers
  failed because `agentapi` and provider API keys were unavailable. No
  `MCR1-deep-research-{provider}.md` file was created.
- Manual PubMed/web searches for `Saccharomyces cerevisiae MCR1`, `YKL150W`,
  `NADH-cytochrome b5 reductase`, and the 2016 Dph3 reductase paper found one direct
  2008 Mcr1 import paper missing from GOA, PMID:18279676, and did not find a newer
  post-2016 primary paper that changes Mcr1's core mitochondrial reductase assignment.

## Literature synthesis

- PMID:8001120 is the primary MCR1 paper and is abstract-only in the cache. It reports
  that `MCR1` encodes two mitochondrial NADH-cytochrome b5 reductase isoforms, one
  outer-membrane anchored and one released into the intermembrane space:
  [PMID:8001120, "The S. cerevisiae gene MCR1 encodes two mitochondrial isoforms of
  NADH-cytochrome b5 reductase."].
- PMID:18279676, also abstract-only, revisited the biogenesis of the outer-membrane
  form. The IMS form uses the TOM complex, while the outer-membrane form inserts by a
  TOM-independent route: [PMID:18279676, "while the IMS form crosses the outer membrane
  via the translocase of the outer mitochondrial membrane (TOM) complex, the other form
  is integrated into the outer membrane by a process that does not require any of the
  known import components at the outer membrane"].
- PMID:10622712 is abstract-only and supports retention of the
  ergosterol-biosynthesis annotation, but the abstract frames the CYP51
  reconstitution as a microsomal cytochrome b5/NADH-cytochrome b5 reductase
  system rather than distinguishing mitochondrial Mcr1 from the ER-localized
  paralog Cbr1: [PMID:10622712, "fungal CYP51 mediated sterol
  14alpha-demethylation can be wholly and efficiently supported by the
  cytochrome b5/NADH cytochrome b5 reductase electron transport system"].
- PMID:11420140 is abstract-only and supports the oxidative-stress row through
  D-erythroascorbyl free-radical reduction. The `mcr1` disruptant lost almost all
  NADH-D-erythroascorbyl free-radical reductase activity and became hypersensitive to
  hydrogen peroxide and menadione, while multicopy `MCR1` increased the reductase
  activity and D-erythroascorbate level: [PMID:11420140, "the mitochondrial
  NADH-cytochrome b(5) reductase functions as NADH-D-erythroascorbyl free radical
  reductase and plays an important role in the response to oxidative damage in S.
  cerevisiae"].
- PMID:27694803 is full-text and mainly establishes Cbr1, not Mcr1, as the physiological
  NADH-dependent Dph3 reductase. Mcr1 can reduce Dph3 in vitro more slowly, but `mcr1`
  deletion alone did not produce the killer-toxin phenotype and only enhanced the
  `cbr1` phenotype in the double mutant: the Dph3/tRNA evidence is therefore a
  non-core backup activity rather than a central Mcr1 function.
- PMID:16606443 is a full-text, protein-array WW-domain interaction paper. The cached
  body does not contain `MCR1`, `YKL150W`, or `P36060`, so it is enough to explain the
  high-throughput Rsp5 IPI row but not enough to infer a specific Mcr1 ubiquitination
  or Rsp5-linked molecular function.

## PAINT and GOA decisions

- `MCR1/P36060` is in `PTHR19370:SF171`, the fungal/plant/animal
  NADH-cytochrome b5 reductase 2 subfamily. PAINT places `GO:0005739 mitochondrion`
  and `GO:0004128 cytochrome-b5 reductase activity, acting on NAD(P)H` at
  `PANTHER:PTN000452207`, with `SGD:S000001633` as a descendant seed. This self-seeding
  is expected for an IBA whose node placement is grounded partly in the target's own
  experimental annotation.
- PAINT places `GO:0006696 ergosterol biosynthetic process` at child node
  `PANTHER:PTN000452208`, again with `SGD:S000001633` as the seed. This is a
  valid self-seeded inherited PAINT assertion, but it is kept as non-core
  because the available CYP51 reconstitution evidence tracks the microsomal
  cytochrome-b5/NADH-cytochrome-b5-reductase system rather than establishing
  that mitochondrial Mcr1 feeds ER-localized CYP51 in vivo.
- The molecular function rows need two layers of specificity: `GO:0016491
  oxidoreductase activity` is true but too broad, while `GO:0090524 cytochrome-b5
  reductase activity, acting on NADH` captures the EC/RHEA direction better than
  `GO:0003954 NADH dehydrogenase activity`.
