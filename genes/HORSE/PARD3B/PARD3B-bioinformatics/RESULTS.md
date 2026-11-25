# Horse PARD3B (A0A9L0RMF2): evolutionary grounding analysis

Script: `analyze.py` (PEP 723; `uv run --script analyze.py > analyze_output.txt`).
Raw output: `analyze_output.txt`. Human PARD3B UniProt record saved as `Q8TEW8-uniprot.txt`.

## Family and subfamily placement

UniProt PANTHER cross-references (fetched by the script):

- horse A0A9L0RMF2: PTHR16484:SF4 (PARTITIONING DEFECTIVE 3 HOMOLOG B)
- human PARD3B Q8TEW8: PTHR16484:SF4
- mouse Pard3b Q9CSB4: PTHR16484:SF4
- human PARD3 Q8TEW0: PTHR16484:SF10 (PARTITIONING DEFECTIVE 3 HOMOLOG), a different subfamily

The horse protein is in the PARD3B subfamily with human and mouse PARD3B. PARD3, Drosophila
Bazooka and C. elegans PAR-3 sit in other subfamilies of PTHR16484 (SF10, SF17).

## Global alignment (BLOSUM62, gap open -10, extend -0.5)

| Partner | Subfamily | Length | Identity over aligned pairs |
|---|---|---|---|
| human PARD3B Q8TEW8 | SF4 | 1205 | 1065/1205 (88.4%) |
| mouse Pard3b Q9CSB4 | SF4 | 1203 | 999/1203 (83.0%) |
| human PARD3 Q8TEW0 | SF10 | 1356 | 539/1088 (49.5%) |

## Gene-model note

The horse protein (1238 aa) aligns end to end with human and mouse PARD3B except for one
insertion of 31 residues near horse position 132 (N-terminal to PDZ1), absent from both the
human and the mouse canonical sequences. All three PDZ domains (horse 232-320, 414-487,
529-604) are present. Horse has 10 unreviewed PARD3B entries in UniProt (1106-1238 aa), so
A0A9L0RMF2 is one of several Ensembl transcript models; it is the longest. Whether the
31-residue segment is a real alternative exon or a gene-model artefact is not resolved here.

## Motif conservation

- **aPKC-binding region.** Horse residues aligned to human PARD3 815-835 (the FXR / S827 / KR
  region that binds the aPKC kinase domain) are `V L E L G L E G F P D Q H I N - - - F R L`:
  the PARD3 F818/R820 (FXR) motif is replaced (L, L), S827 is H, and the K831-R832 (KR) motif
  falls in a 3-residue gap. The horse protein shares the PARD3B-specific loss of the aPKC-binding
  motif.
- **14-3-3 site.** Horse residues aligned to human PARD3B 740-752 are identical, including
  S746 (the phosphorylation-dependent 14-3-3 binding site of human PARD3B).
- **LKB1-binding linker.** The horse segment between PDZ2 and PDZ3 (horse 488-528), which in
  mouse Par3L is required for LKB1 binding, is 38/41 identical to human and 36/41 identical to
  mouse PARD3B.

## Experimental GO annotations of the same-subfamily orthologs (QuickGO, non-IEA, non-IBA)

- human Q8TEW8: GO:0005515 protein binding (IPI, many partners incl. INSC, PMID:16458856, and
  high-throughput PMID:36115835); GO:0030054 cell junction (IDA, GO_REF:0000052, HPA);
  GO:0032991 protein-containing complex (IDA, PMID:16458856).
- mouse Q9CSB4: GO:0005515 protein binding (IPI, with Q9WTK7 = Stk11/LKB1, PMID:24859006).

No experimental process annotations exist for any PARD3B ortholog. Every horse IBA row comes
from the family-level node PTN001046835 seeded by Bazooka, PAR-3, mouse Pard3, rat Pard3 and
human PARD3 (other subfamilies).
