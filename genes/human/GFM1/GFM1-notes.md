# GFM1 notes

## Deep research

`GFM1-deep-research-claude-code.md` (claude_code provider) completed in about 37 s with only
2 web searches and 6 citations (MedlinePlus, GeneCards, PMC copies of Tsuboi 2009 and Smits 2011,
a bioRxiv preprint). The report itself says most of its content is from background knowledge.
It was used only as a list of leads; every claim below was checked against cached publications.

## Function

- EF-G1mt is the mitochondrial translocase. In human mitochondria the two functions of bacterial
  EF-G are split: [PMID:19716793 "EF-G1mt specifically catalyzes translocation, whereas EF-G2mt
  mediates ribosome recycling with human mitochondrial RRF but lacks translocation activity"].
- Structures of the human 55S mitoribosome with EF-G1mt in three states, including a
  post-translocational one [PMID:32737313 "the mito-specific C-terminal extension in EF-G1mt is
  directly involved in translocation of the acceptor arm of the A-site tRNAmt"]. GTPase centre:
  [PMID:32737313 "the binding of EF-G1mt to the 55S mitoribosome stabilizes the factor in an active
  conformation necessary to catalyze the hydrolysis reaction"].
- Localisation: mitochondrial matrix, N-terminal transit peptide 1-36 (UniProt, HAMAP rule).

## Disease

- COXPD1 (MIM:609060): first described in siblings with progressive hepatoencephalopathy
  [PMID:15537906 "Sequencing of EFG1 revealed a mutation affecting a conserved residue of the
  guanosine triphosphate (GTP)-binding domain"].
- Leigh syndrome patient, complementation in yeast and mammalian cells [PMID:17160893].
- R250W in subdomain G'; fibroblast but not muscle OXPHOS defect; rescued by wild-type GFM1
  [PMID:21119709 "The OXPHOS system defects and the impairment in mitochondrial translation in
  fibroblasts were rescued by overexpressing wild-type GFM1"].
- Gfm1 R671C mouse model [PMID:34919756].

## Annotation decisions

- Protein binding (TRIM63 Y2H, influenza NS-segment AP-MS): removed as uninformative.
- Generic RNA binding (mRNA interactome capture): over-annotation.
- Generic translation and translational elongation IEAs: modified to GO:0070125 mitochondrial
  translational elongation.
- No annotation to ribosome disassembly / recycling: that is GFM2's role per PMID:19716793.
