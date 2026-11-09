# dnaEA curation notes

## Annotation-reviewer pass (2026-09-01)

Consulted the annotation-reviewer workflow against all 8 current GOA rows, UniProt Q88MG5, EC 2.7.7.7, and the annotated DnaE/PHP domains. Accepted DNA-directed DNA polymerase activity, cytoplasmic localization, and DNA replication. Marked generic nucleic-acid binding, catalytic activity, DNA polymerase activity, and DNA biosynthesis as over-annotated. Kept 3'-5' exonuclease activity UNDECIDED: a PHP domain is present, but its catalytic proofreading activity in Q88MG5 is not established and canonical DnaQ proofreading is separately encoded. No GOA row remains pending.



## Annotation-reviewer follow-up — 2026-11-06

Reviewed every original annotation against target architecture and the available literature. Original non-review row fields, inherited NEW rows, raw UniProt and GOA remain frozen; baseline is in `.cache/module-audit-logs/chromosomal-replication-20261106/`. Default Falcon was genuinely attempted for this gene and failed HTTP403 authentication; no provider text was fabricated. These are manual research notes.

Target Q88MG5 is the KT2440 record. Curated HAMAP/RuleBase and domain statements provide conserved-function evidence; no automatic GO cross-reference is used as biological support. P. aeruginosa reconstitution is comparative evidence, not a direct assay of this KT2440 sequence. Existing IEA annotations are assessed on the function, not the evidence code. No IBA rows occur in this target, so a PAINT-loss audit is not applicable.

- GO:0003676 nucleic acid binding: MODIFY. The DnaE replicase directly binds its DNA substrate; refine general nucleic-acid binding to DNA binding. The domain architecture identifies a replicative polymerase, not an RNA-binding protein.
- GO:0003824 catalytic activity: MODIFY. DnaE polymerase architecture and Pseudomonas alpha-epsilon reconstitution support DNA-directed polymerization; refine the generic catalyst term to GO0003887.
- GO:0003887 DNA-directed DNA polymerase activity: ACCEPT. The DnaE1 catalytic architecture supports template-directed DNA extension, independently corroborated by purified P. aeruginosa alpha-epsilon replicase reconstitution. The target Rhea/ARBA mapping alone is not used as proof; evidence is comparative rather than a Q88MG5 assay.
- GO:0005737 cytoplasm: ACCEPT. The bacterial replicase acts on the chromosome in the cytoplasm; this is a mechanistic localization inference, not validation of the ARBA label by itself.
- GO:0006260 DNA replication: ACCEPT. The DnaE alpha subunit directly synthesizes replicated DNA. Conserved DnaE1 architecture and the Pseudomonas reconstitution support its central replication role.
- GO:0008408 3'-5' exonuclease activity: UNDECIDED. Q88MG5 contains a PHP domain, but a PHP fold does not establish a catalytically competent metal-binding site or measurable 3-prime to 5-prime exonuclease. DnaE PHP domains vary in activity among bacteria; the independent DnaQ subunit neither proves nor excludes intrinsic proofreading. No target-specific PHP assay or validated catalytic-residue analysis was obtained, so the claim remains unresolved and is not made a core function.
- GO:0034061 DNA polymerase activity: MODIFY. The supported specificity is DNA-directed DNA polymerization, the descendant already present.
- GO:0071897 DNA biosynthetic process: ACCEPT. DnaE directly creates DNA by nucleotide addition, making DNA biosynthesis true. Current QuickGO does not place DNA replication under GO0071897 via is_a/part_of; retain this distinct product-formation claim rather than claiming an unsupported hierarchy.

Primary sources used: PMID:15611049. Independent frozen support: file:PSEPK/dnaEA/dnaEA-uniprot.txt.

Intrinsic PHP proofreading remains UNDECIDED. No validated metal-ligand comparison or target-specific assay was obtained. DnaQ presence is neither a proof of PHP inactivity nor evidence of dual proofreading. Keep the polymerization core distinct.
