# Srlp (Q9VG69, CG5844) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: Srlp is the closest experimentally characterised relative (same PANTHER subfamily,
PTHR43802:SF1) of the fly paralog CG5611. ProtNLM2 output was not opened or used.

### Data fetch and deep research
- `just fetch-gene DROME Srlp`: 2 GOA rows (IDA mitochondrial matrix, IMP cellular response to hypoxia).
- `just deep-research-falcon DROME Srlp --fallback perplexity-lite` FAILED: falcon "Failed to
  authenticate"; perplexity fallback HTTP 401 insufficient quota. No deep-research file exists.
  Literature was gathered directly instead (Europe PMC search for CG5844/Srlp).
- Cached PMID:30931935 (full text), the only paper studying Srlp directly.

### Literature
- Mitochondrial matrix: matrix-targeted APEX labelling in fly muscle [PMID:26362788 "we demonstrate
  that this approach can be used effectively in vivo to analyze the Drosophila mitochondrial matrix
  proteome"]. Srlp-specific hit is in the supplement (not cached).
- Hypoxia: S2 RNAi screen [PMID:18653470 "We carried out a genome-wide RNA interference (RNAi) screen
  in Drosophila S2 cells for functions required to down-regulate translation during hypoxia"].
  Abstract-only; CG5844 not named in the abstract.
- Yu et al. 2019 [PMID:30931935 "The homozygous Srlp mutation was lethal"]; testis GSC defects by
  nos-Gal4/tj-Gal4 RNAi; HA-Srlp pull-down/LC-MS and co-IP with RpL6 [PMID:30931935 "Results of the
  co-immunoprecipitation assay confirmed that the Srlp protein could combine with the RpL6 protein"].
  Name "Spliceosome-Ribosome Linker Protein" comes from this. Mechanism weak: overexpressed tagged
  protein, post-lysis association, mRNA-level readouts, no localisation; inconsistent with matrix
  residence. FlyBase made no GO annotations from it; I add none (phenotype/necessity, not
  participation; bare protein binding is uninformative).

### Bioinformatics (Srlp-bioinformatics/RESULTS.md)
- PTHR43802:SF1 with CG5611 (54.9%), ech-3 (45.3%), Arabidopsis Q6NL24, CamK (6-oxocamphor hydrolase),
  BamA. Rat ECHS1 is PTHR11941 (outgroup only).
- First crotonase catalytic Glu retained (E158; = ECHS1 E144, CamK E124); second hydratase Glu
  (ECHS1 E164) is Met185. CG5611 has the same pattern (Asn). No specific reaction assignable.
- N-terminus Arg/Lys-rich, no acidic residues: presequence-like.

### Decisions
- GO:0005759 mitochondrial matrix IDA: ACCEPT (core location).
- GO:0071456 cellular response to hypoxia IMP: KEEP_AS_NON_CORE (screen phenotype; full text unseen;
  likely indirect).
- No NEW annotations. No MF assignable.

### Transfer guidance for CG5611
- Experimentally established in Drosophila for Srlp: mitochondrial matrix (IDA); requirement for
  hypoxic translational suppression in S2 cells (IMP, screen); organismal lethality and testis GSC
  phenotypes (not GO-annotated).
- Not established: any molecular function. Transfer of matrix localisation to CG5611 should be
  conditional on CG5611 having its own presequence-like N-terminus.
