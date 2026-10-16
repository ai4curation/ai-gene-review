# NCGR_LOCUS1270 reference and term-scope check

NCGR_LOCUS1270 strongly resembles chloroplast FBPases. The original negative
annotation rationale did not establish that TreeGrafter selected a cytosolic
paralog.

## Actual reference identity

The GOA WITH/FROM value PTN004269459 resolves in the current PTHR11556 tree to
the **Sorghum bicolor A0A1B6QP66 / SORBI_3001G425400 leaf**. It is not itself a
deep ancestral node. The Miscanthus query is not a reference-tree leaf; this
check does not reconstruct its original insertion edge.

The current UniProt record for the sorghum reference describes a chloroplast
FBPase in the Calvin cycle. Its sequence is 409 aa and closely matches the
411-aa Miscanthus protein, including the N-terminal region and regulatory
insertion. The original claim that the reference must be a cytosolic paralog
is therefore unsupported. A retained ancestral annotation and an incorrect
query insertion are different possibilities.

Global BLOSUM62 alignments, with gap-open -10 and gap-extension -0.5 and terminal
gaps included, give:

| Comparator | Identity / alignment columns | Identity | Annotated specialization |
|---|---:|---:|---|
| Sorghum A0A1B6QP66, the named TreeGrafter reference | 400/413 | 96.85% | Chloroplast |
| Arabidopsis P25851 / CFBP1 | 317/421 | 75.30% | Chloroplast |
| Arabidopsis Q9MA79 / CYFBP | 171/418 | 40.91% | Cytosolic |

These comparisons support the chloroplast assignment. They do not establish
exclusive localization or exclude every secondary pathway role. Reference
records, sequence alignments, the exact PTN lineage and the tree-response hash
are retained in this directory.

Run from the repository root:

```sh
uv run --script genes/9POAL/NCGR_LOCUS1270/NCGR_LOCUS1270-bioinformatics/check_fbp_reference.py
```

## Fructose process scope

GO:0006000 is not an is_a ancestor of the two phosphorylated-fructose process
terms. That absence establishes neither disjointness nor a requirement that
every participating enzyme use free fructose directly. The definition includes
pathways as well as individual reactions; GO:0006002's definition explicitly
describes F6P as an intermediate in fructose metabolism.

Current QuickGO annotations assign GO:0006000 to human FBP1 (P09467, TAS,
PMID:7558035), human FBP2 (O00757, TAS, PMID:9678974), and Dictyostelium fbp
(Q6RYT0, IDA, PMID:4308724). These are comparator annotations, not new evidence
that the Miscanthus protein performs a particular physiological pathway. They
nevertheless contradict the report's blanket rule that FBPase substrate
chemistry excludes this GO process. The Dictyostelium PMID title and accession
were verified; its full experimental text was not retrieved, so no additional
assay details are inferred from that citation.

The named TreeGrafter reference is a chloroplast-associated sorghum homolog, not an established cytosolic-paralog mismatch.

Definitions, comparator responses and accession identity are captured in
`projects/TREEGRAFTER/rereview-2026-09-20/ncgr-fructose-ontology-and-comparators.json`.
The current family IBD slice lacks GO:0006000; this differs from the April 2026
TreeGrafter source record and is not itself a biological refutation or proof of
why an annotation changed.

## Report incorporation and unresolved scope

The complete OpenScientist report was read, including its recommendations on
other localizations and pathways. It supplies useful chloroplast-FBPase context
and the ontology-branch distinction, but overinterprets both. Its proposed
project-wide removal of fructose metabolism from all FBPases is not justified.
No computational code/output sidecar was exported beyond its report renders;
the sequence and mapping results above were independently recomputed.

Fructose metabolism, sucrose metabolism/biosynthesis, gluconeogenesis and a
conditional cytosolic pool remain UNDECIDED for this target. The ordinary
chloroplast Calvin-cycle role remains supported. Supplying carbon to another
pathway does not automatically establish direct participation, while altered
compartment preference or regulation does not by itself demonstrate loss of
every ancestral role. Clarification should establish the relevant process
boundaries and target physiology rather than infer exclusive function from the
dominant compartment. No new process annotation is proposed.
