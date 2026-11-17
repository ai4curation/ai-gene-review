# pyrG (E. coli K-12, P0A7E5) notes

Deep research was not generated for this gene; these notes summarise the cached
publications (mostly abstract-only) and the UniProt record.

## Function

- CTP synthase: ATP-dependent amination of UTP to CTP using glutamine or ammonia
  [PMID:11336655 "Cytidine 5'-triphosphate synthase catalyses the ATP-dependent formation of CTP
  from UTP with either ammonia or glutamine as the source of nitrogen"].
- Two-domain enzyme: N-terminal amidoligase (ATP/UTP site) and C-terminal type 1 glutamine
  amidotransferase; ammonia travels through a 25 A channel [PMID:15157079 "A gated channel that spans
  25 A between the glutamine hydrolysis and amidoligase active sites provides a path for ammonia
  diffusion"].
- Cys379 is the glutamine-hydrolysis nucleophile; C379A keeps NH3-dependent activity but loses
  glutamine-dependent activity [PMID:11336655 "The mutant enzyme (C379A), which is fully active with
  ammonia but has no glutamine-dependent activity"].
- GTP is an allosteric activator of glutamine-dependent activity (PMID:4550559, PMID:11336655);
  CTP is a feedback inhibitor (PMID:16216072).
- Mg2+ needed beyond nucleotide complexation: separate free-metal site (PMID:8385490).
- Quaternary structure: dimer-tetramer equilibrium driven by ATP/UTP (PMID:15157079, PMID:7779798).
- Filaments: E. coli CtpS forms filaments in vivo and in vitro (PMID:20639870); polymerisation is
  stimulated by CTP and inhibits activity, a negative-feedback mechanism (PMID:25030911).

## Annotation decisions

- GO:0019856 pyrimidine nucleobase biosynthetic process (IBA) is MODIFY to GO:0044210, consistent
  with the PTHR11550 family review (WRONG_NODE term at PTN000167473) and the URA7/URA8 reviews.
- Generic oligomerisation terms (identical protein binding, protein-containing complex, protein
  homotetramerization) kept as non-core.
- No PAINT IRD/IKR loss on the lineage (`just paint-losses ECOLI pyrG`).
