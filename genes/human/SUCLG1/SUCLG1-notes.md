# SUCLG1 (P53597) notes

## 2026-11-11 first review

Written as part of the evolutionary review of the succinyl-CoA synthetase families (PTHR11117 alpha, PTHR11815 beta); see genes/yeast/LSC2/LSC2-bioinformatics/RESULTS.md.

- SUCLG1 is the single alpha subunit shared by the two human enzymes [PMID:30470562 "Succinate-CoA ligase (SUCL) is a heterodimer consisting of an alpha subunit encoded by SUCLG1, and a beta subunit encoded by either SUCLA2 or SUCLG2 catalyzing an ATP- or GTP-forming reaction, respectively, in the mitochondrial matrix."].
- The alpha subunit does not set nucleotide specificity [PMID:9765290 "Because the two succinyl-CoA synthetases incorporate the same alpha-subunit, the determinants of nucleotide specificity must reside within the beta-subunit"]. CoA binds the alpha subunit [PMID:32627745 "The CoA portion binds in the CoA-binding site located in the amino-terminal domain of the α-subunit"].
- Loss of SUCLG1 removes both beta subunits and all activity, with rescue [PMID:27484306 "The patient's cells lack the SUCLG1 protein, with significantly reduced levels of SUCLA2 and SUCLG2 protein."].
- Evolutionary reading of the GDP-forming rows: accepted here. Human SUCLG1 is the case the PAINT root placement was built from; the same node over-propagates to fungal alpha subunits (LSC1 removes it, S. pombe marks it over-annotated). The difference is the beta repertoire of the genome, not anything in the alpha subunit.
- GO:0004774 succinate-CoA ligase activity (IMP) accepted at the parent level: the fibroblast assay does not separate the two enzymes and loss of the alpha subunit removes both.
- Side activities (malate-CoA ligase, acid-thiol ligase, malate metabolic process) kept as non-core and toxic metabolite repair marked over-annotated, matching SUCLA2 [PMID:40108300 "Here we discover that CLYBL additionally functions as a metabolite repair enzyme for malyl-CoA, a side product of promiscuous citric acid cycle enzymes."]. PMID:40108300 is abstract-only in the cache.
- RNA binding (HDA, mRNA interactome capture) marked over-annotated.
- Protein binding IPI rows with SUCLG2 removed under the protein-binding policy; the interaction is real and is the GDP-forming complex.

### Affinage

Fetched with projects/AFFINAGE_EVALUATION/affinage_deep_research.py (trust gates clear). Recorded as a reference with correctness DISPUTED: the narrative claims that could be checked are right, but its GO grounding "catalytic activity, acting on a protein" is wrong for SUCLG1. Leads it supplied, none imported as annotations: restriction of POLRMT succinylation [PMID:38649537 "Mechanistically, SUCLG1 restricts succinyl-CoA levels to suppress the succinylation of mitochondrial RNA polymerase (POLRMT)."], Lys90 butyrylation and SIRT4 (PMID:41991142, not cached, unverified). Both are indirect or regulatory and are recorded as suggested questions.

### Not done

No falcon or perplexity deep research (keys not available in this session). Literature beyond GOA was limited to the Affinage citations and the family literature.
