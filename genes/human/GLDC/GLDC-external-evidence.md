# GLDC external evidence and source limits

This evidence record distinguishes original observations from biological interpretation.
The normal cached publications remain unchanged; external originals were read separately.

## Catalysis and reaction boundaries

[PMID:24467211](https://pubmed.ncbi.nlm.nih.gov/24467211/) was checked against selected
published Methods/Results reproduced with the [article](https://www.researchgate.net/publication/259953853_Glycine_Decarboxylase_Is_an_Unusual_Amino_Acid_Decarboxylase_Involved_in_Tumorigenesis).
Human GLDC and H-protein were expressed in bacteria. Excess PLP supported H-free CO2
release; productive aminomethyl transfer used lipoylated H. The paper reports an active
monomer and no comparable stimulation by free lipoate in its preparation. Its methylamine
reverse-reaction experiment does not test inhibition. The normal cache contains only the
abstract; the external reading did not cover a complete PDF or every supplement.

[PMID:2268343](https://pubmed.ncbi.nlm.nih.gov/2268343/) remains abstract-only. A suggested
question asks UniProt for the TAS statement; a miscitation has not been demonstrated.

The current [OLS definition](https://www.ebi.ac.uk/ols4/ontologies/go/classes?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0009055)
and [QuickGO definition](https://www.ebi.ac.uk/QuickGO/term/GO:0009055), rechecked on
2026-11-06, both include enzyme-associated redox transformations. Neither resource
restricts this term to electron carriers. This defeats a carrier-only objection but does
not positively establish the separate GLDC activity. The cited TAS remains unresolved.

The current [IPR001597 entry](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR001597/)
is a domain entry with a direct GO:0016829 mapping and a description including P-proteins.
The GO definition excludes oxidative cleavage. The physiological GLDC reaction and an
artificial partial reaction should not be conflated: without H-protein, excess PLP is
consumed as a cosubstrate. The lyase row is therefore MARK_AS_OVER_ANNOTATED; the
domain-level applicability concern is PROBABLE and asks InterPro to CHECK its scope.

## Chicken donor and cofactor identity

The original P15505 record and its QuickGO annotations identify chicken experiments.
[PMID:7440562](https://pubmed.ncbi.nlm.nih.gov/7440562/) reports purified liver-mitochondrial
P protein, homodimer formation, PLP, methylamine inhibition and free-lipoate stimulation.
[PMID:7440563](https://pubmed.ncbi.nlm.nih.gov/7440563/) has no accessible abstract; JBC
full-text requests returned 403. [PMID:3426593](https://pubmed.ncbi.nlm.nih.gov/3426593/)
identifies the PLP-linked chicken peptide. Its peptide Lys-35 must not be mistaken for a
human residue number. In the actual family MSA, human K754 aligns with chicken K738 at
column 1271. Conservation supports homology, not a new target experiment.

The current GO:0036255 and GO:1903442 definitions describe cellular or organismal stimulus
responses. Purified-enzyme modulation and lipoylated-H dependence do not by themselves
establish human participation in those processes.

## Human assembly deposits

[6I33](https://www.rcsb.org/structure/6I33) and [6I35](https://www.rcsb.org/structure/6I35)
are recombinant human GLDC deposits. Their polymer sequence exactly matches P23378
residues 45–1020 with an additional M prefix and GHHHHHH suffix. Author/PISA dimer
assemblies cite gel filtration and SAXS, respectively. Those method labels are deposited
provenance: underlying solution curves and conditions were not obtained, and the shared
citation remains unpublished. This supports a dimer model while leaving its relationship
to the published monomer preparation unresolved. 6I34 is a Neanderthal construct and was
excluded from the modern-human proof. Neither crystal-chain counts nor PISA alone were
treated as evidence of the native solution assembly.

## Localization

The original [MitoCoP paper](https://pubmed.ncbi.nlm.nih.gov/34800366/) and Table S1 include
P23378/GLDC in pool 1. Its subtractive, spatial and importomics classifications are each
class/cluster 1. This is organelle evidence; carried-over annotation columns do not turn
the experiment into matrix-specific localization.

The current [HPA record](https://www.proteinatlas.org/ENSG00000178445-GLDC/subcellular)
supports mitochondrial staining in human cell lines. Its additional uncertain nuclear
signal is not used to manufacture a new annotation. The current [Reactome reaction](https://reactome.org/content/detail/R-HSA-5693967)
explicitly places the human GLDC catalytic entity in the mitochondrial matrix. That
compartment assessment is retained separately from the event's unresolved dimer model.

## Phylogenetic evidence

Original PANTHER19 PTHR11773 tree/MSA/attributes and the retained PAINT IBD/IRD records
were replayed: 287 nodes, 157 leaves, 2010 alignment columns; human AN46/PTN002482993
matches the complete 1020-aa target sequence. AN0/PTN000206531 bears the catalytic and
glycine-cleavage IBDs; AN28/PTN000206533 bears the mitochondrial IBD. All are ancestors
of the target, and all three incoming donor sets match their actual descendant positions.
The on-path cytosol IRD does not negate the mitochondrial assignment. Human self evidence
is legitimate descendant grounding, and donor count is not treated as a weakness.

Source URLs, original-byte digests and target-specific checks are retained in
[source evidence](GLDC-source-evidence.json). The three broad process terms are verified
ancestors of GO:0019464; PLP and pyridoxal binding are distinct ligand terms.

## Family material and review follow-up

The existing [family review](../../../interpro/panther/PTHR11773/PTHR11773-review.md)
and [generated family research](../../../interpro/panther/PTHR11773/PTHR11773-deep-research-falcon.md)
were read as secondary leads. The former's native-dimer wording is not an additional
human experiment. The latter discusses the split bacterial P-protein architecture;
structural homology does not independently resolve human solution stoichiometry.
The deposited human dimers and chicken experiments remain positive evidence, alongside
the published recombinant monomer. The remaining biological question concerns matched
native-human assembly and activity, rather than whether any dimer model exists.
No additional research provider was invoked. The source digest record and historical
context archive remain JSON operational records; they do not replace the curated YAML.
