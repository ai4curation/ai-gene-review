# ANKRD39 notes

- Uncharacterized; 183 aa, with four ANK repeats at residues 30-158. PE1; HPA low tissue specificity. PAN-GO 0.
- GOA: three ND root placeholders, all ACCEPT, each with an aspect-specific reason.
- PTHR24171 has 9 annotated PAINT nodes (for example the tankyrase node PTN000652929), but ANKRD39 is in SF9 and none propagates to it. The family files are committed.
- PubMed recall: two Alzheimer's gene-list or docking studies only. Affinage reports nothing.
- knowledge_gaps: WHOLLY_DARK.

## Round 2 (reviewer, PR #4129)

- The gap no longer says "partners are unknown". UniProt cross-references 65 IntAct and 71 BioGRID interactors, all high-throughput, none reciprocally validated, with no SUBUNIT line and no GO row. The experiment is now to validate those deposited interactors rather than discover partners from scratch.
- The PAINT file is now cited (the tankyrase node as an example of annotated nodes in other subfamilies), along with Pharos Tdark and UniProt's absence of any GO term.
- The two Alzheimer's gene-list papers (PMID:38995776, PMID:31816601) are now listed with relevance NONE, so the negative literature recall can be audited.
