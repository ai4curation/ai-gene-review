# nadA curation notes

## 2026-07-20

- Target identity: PP_1231 / UniProtKB Q88NH8, type 1 NadA quinolinate synthase
  [UniProtKB:Q88NH8, "Belongs to the quinolinate synthase family. Type 1 subfamily."].
- Reaction: iminoaspartate and glycerone phosphate are condensed to quinolinate
  [UniProtKB:Q88NH8, "Catalyzes the condensation of iminoaspartate with dihydroxyacetone phosphate to form quinolinate."]
  [RHEA:25888, quinolinate synthase reaction].
- Cofactor: one [4Fe-4S] cluster is assigned per subunit
  [UniProtKB:Q88NH8, "Binds 1 [4Fe-4S] cluster per subunit."].
- Family grounding: the target has a PTHR30573 quinolinate-synthase family
  cross-reference, and experimentally grounded E. coli NadA P11458 is retained
  as a representative exemplar; no ancestral PTN is asserted
  [UniProtKB:Q88NH8, "PANTHER; PTHR30573; QUINOLINATE SYNTHETASE A; 1."].
- Curation: catalytic and quinolinate/de novo process terms are core; [4Fe-4S]
  binding is real but non-core; broad transferase and pyridine-nucleotide terms
  were modified to specific terms.
- OpenScientist independently recovered the canonical NadA reaction, catalytic
  [4Fe-4S] role, and L-aspartate de novo pathway placement. Its ortholog-based
  mechanism and provider-computed sequence comparison are useful family
  context, but not direct PP_1231 experimental evidence; no new target-level GO
  assertion was added [file:PSEPK/nadA/nadA-deep-research-openscientist.md,
  "No study reported here characterizes the P. putida KT2440 NadA enzyme directly; conclusions are inferred from highly conserved orthologs and from domain/family assignment."].
