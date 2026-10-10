# rde-8 (Q23342) review notes

Deep research: falcon timed out (exit 137) and perplexity-lite is unavailable. No
deep-research file was generated. The primary paper PMID:25635455 is cached with full text.

## Key facts with provenance
- RDE-8 is a NYN-domain endoribonuclease [PMID:25635455 "These data indicate that RDE-8 encodes an endoribonuclease required for RNAi."].
- Its D76N mutation is catalytic-dead. It is needed for RRF-1 RdRP activity in vitro
  [PMID:25635455 "We further show that RDE-8 is required for efficient RRF-1 RdRP activity in vitro."].
- It binds target mRNA only weakly or indirectly [PMID:25635455 "RDE-8 contains no recognizable RNA-binding domain, and we only detected target binding when the conserved catalytic residues of RDE-8 were mutated"].
- It is located in the cytoplasm and in Mutator foci [PMID:25635455].
- Recruitment to Mutator foci requires MUT-15 and NYN-1/2 [PMID:30036386].

## Decisions
- RNA endonuclease (IBA, IDA) and siRNA processing: ACCEPT (core).
- mRNA binding (IBA, IDA): non-core.
- Nucleus IBA: over-annotated (no nuclear pool reported).
- 3'-UTR-mediated mRNA destabilization IBA: MODIFY to GO:0090625 siRNA-mediated gene
  silencing by mRNA destabilization.
