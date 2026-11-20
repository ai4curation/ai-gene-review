# Neisseria assay-strain identity bridge

The official H44/76 assembly GCA_000185025.2 identifies strain H44/76 (taxon909420)
and links its AEQZ01 WGS flat file. `H44-assembly.xml` and the source provenance
are retained. `verify.py` parses the archived ENA CDS translations and compares
complete proteins to the official UniProt JSON records. All three matches are
exact and unique among 2,423 translated CDSs. Run from the worktree with
`uv run python analysis/module_audits/bacterial_lps_transport/literature-consultation/identity/verify.py`.
The source archive is deliberately ignored, at the path in the script; recover
it from the HTTPS URL in H44-genome-provenance.json and verify its SHA256 before
rerunning. No sequence was synthesized, modified or inferred from an annotation.

| Reviewed reference candidate | Exact H44/76 CDS | Identity | Scope |
|---|---|---|---|
| NEIMH LptD F0MIT7 | NMH_1010 / EFV64164.1, AEQZ01000016.1 | 802/802 | Same named strain as the primary studies; locus synonym NMBH4476_0275. |
| NEIMB LptE Q9K0A7 | NMH_2330 / EFV62668.1, AEQZ01000045.1 | 159/159 | MC58 reference protein identical to the H44/76 CDS; source phenotype remains H44/76/HB-1. |
| NEIMB carrier Q7DDQ9 | NMH_1931 / EFV63335.1, AEQZ01000038.1 | 176/176 | MC58 NMB0355; literature calls the carrier LptH to distinguish the unrelated neisserial lipid A phosphoethanolamine transferase named LptA. UniProt calls this carrier lptA. |

The complete current UniProt query for taxon909420 returned only 16 records,
including F0MIT7 but no H44/76 LptE/H/C record. This query result is an identifier
coverage limitation, not biological absence. MC58 Q9K136/LptC did not have an
exact complete match to this H44 assembly; no exact LptC bridge is asserted.
Sequence identity supports protein-role transfer in a matched biological context.
It does not make strain phenotypes, native expression levels, or experimental
plasmid/tag sequences identical.

## Source phenotype boundaries

PMID21705335 Table1 identifies H44/76 L3 and HB-1, an H44/76 derivative with the
capsule locus including galE inactivated, yielding truncated LPS. The paper uses
LPS terminology; meningococcal material is commonly termed LOS because it lacks
the long repeating O-antigen. Its locus names NMB0354/0355/0356/0707/1570/1571 are
explicitly MC58 homology coordinates, not evidence that MC58 was experimentally
assayed. LptE deletion did not abolish surface-accessible LPS; LptD levels fell,
consistent with a biogenesis/chaperone contribution. LptH/C/F/G loss prevented
surface accessibility in the tested backgrounds. LptC conditional depletion also
reduced LPS levels, with restoration on complementation. Survival is distinct
from transport: meningococci can survive LPS loss. The LptE result does not prove
absence of every possible contribution in every strain or condition.

PMID15192148 directly studies H44/76 Imp/LptD. Residual LPS in the knockout was
inaccessible to extracellular neuraminidase and to the OM-localized PagL assay,
supporting the surface-delivery role. PMID21705335 Table1 additionally identifies
an H44/76-derived imp/lptD plasmid. These observations support F0MIT7 as a strain-linked
positive; the full-length reference sequence is independently matched above.
Carrier activity for Q7DDQ9 remains a mechanistic inference from a source-matched
native transport phenotype and specific Lpt bridge architecture; no isolated
purified neisserial carrier kinetics are claimed. The three candidate proteins
alone do not constitute a complete reviewed Neisseria extractor/bridge panel.
