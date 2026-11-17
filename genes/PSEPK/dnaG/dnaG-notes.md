# dnaG curation notes

## Annotation-reviewer pass (2026-09-01)

Consulted the annotation-reviewer workflow against all 7 current GOA rows and reviewed UniProt P0A118. Accepted DNA-directed RNA polymerase activity, cytoplasmic localization, DNA replication, primer synthesis, and zinc binding; retained generic DNA binding as non-core. Marked the parent nucleotidyltransferase term as over-annotated because GO:0003899 captures the catalytic role more precisely. QuickGO confirms that GO:0003896 is obsolete, so it was not authored. No GOA row remains pending.


## Annotation-reviewer follow-up — 2026-11-06

Reviewed every original annotation against target architecture and the available literature. Original non-review row fields, inherited NEW rows, raw UniProt and GOA remain frozen; baseline is in `.cache/module-audit-logs/chromosomal-replication-20261106/`. Default Falcon was genuinely attempted for this gene and failed HTTP403 authentication; no provider text was fabricated. These are manual research notes.

Target P0A118 is the KT2440 record. Curated HAMAP/RuleBase and domain statements provide conserved-function evidence; no automatic GO cross-reference is used as biological support. P. aeruginosa reconstitution is comparative evidence, not a direct assay of this KT2440 sequence. Existing IEA annotations are assessed on the function, not the evidence code. No IBA rows occur in this target, so a PAINT-loss audit is not applicable.

- GO:0003677 DNA binding: ACCEPT. DnaG binds its DNA template during primer synthesis. This is core substrate recognition, not a peripheral property; the available target-level evidence does not require a further standalone binding annotation.
- GO:0003899 DNA-directed RNA polymerase activity: ACCEPT. DnaG catalyzes RNA polymerization on a DNA template, as specified by target HAMAP MF_00974. Current QuickGO confirms DNA primase activity GO0003896 is obsolete, so the valid catalytic genus is retained and primer-synthesis context is represented in BP/core.
- GO:0005737 cytoplasm: ACCEPT. DnaG synthesizes primers at cytoplasmic bacterial replication forks; this is a conserved-function localization inference.
- GO:0006260 DNA replication: MODIFY. The direct role is RNA-primer synthesis, a replication sub-process already represented by GO0006269.
- GO:0006269 DNA replication, synthesis of primer: ACCEPT. DnaG itself polymerizes the RNA primers needed by DNA polymerase; it directly executes this process rather than only supplying a substrate or regulator.
- GO:0008270 zinc ion binding: ACCEPT. The target HAMAP annotation identifies one zinc ion in the N-terminal zinc-binding domain, which supports template recognition; this is a mechanistic cofactor property.
- GO:0016779 nucleotidyltransferase activity: MODIFY. The specific nucleotidyltransferase chemistry is DNA-directed RNA polymerization, already represented by GO0003899.

Primary sources used: . Independent frozen support: file:PSEPK/dnaG/dnaG-uniprot.txt.

Primary helicase–primase coupling support added: [PMID:17947583], explicitly a homologous structural system rather than KT2440 biochemistry.
