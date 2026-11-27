# TOP1MT notes

## 2026-11-27 manual family review

The automated deep-research provider was unavailable in this workspace, so this
review used the fetched GOA rows, UniProt, PAINT, and the cached primary
publications.

- TOP1MT is the mitochondrial paralog of nuclear TOP1. Zhang et al. cloned the
  human enzyme, showed that its N terminus contains a mitochondrial targeting
  sequence, and reported that "top1mt is a type IB topoisomerase that requires
  divalent metal (Ca(2+) or Mg(2+)) and alkaline pH for optimum activity"
  [PMID:11526219].
- PTHR10290 splits the two human paralogs cleanly: `PTN000033239` is the
  TOP1MT node, carries an IBD mitochondrial-nucleoid call, and has IRD losses
  for ancestral TOP1 nucleolus and chromosome-segregation assertions.
- The InterPro chromosome row was marked over-annotated because it follows the
  shared topoisomerase domain architecture rather than the mitochondrial
  targeting and mtDNA-nucleoid biology of TOP1MT.
- The PAINT DNA-replication row was modified to `GO:0006264` mitochondrial DNA
  replication. TOP1MT keeps the conserved ATP-independent strand
  breakage/rejoining chemistry, but the relevant duplex substrate is the
  circular mitochondrial genome, not nuclear chromosomes.
- The mitochondrial nucleoid rows were kept: Bogenhagen et al. found a set of
  native and cross-linked core human mtDNA-nucleoid proteins with known mtDNA
  transaction roles [PMID:18063578].
