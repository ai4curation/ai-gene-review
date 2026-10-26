# NCU06296 (Q7SAD4) bioinformatics: phylogenetic placement and FMO motif check

Date: 2026-10-21. Independent of any ProtNLM2 output.

## 1. PANTHER placement (PANTHER 19)

Source: PANTHER geneinfo and treeinfo services
(`https://www.pantherdb.org/services/oai/pantherdb/geneinfo?geneInputList=Q7SAD4&organism=367110`,
`https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR23023`), queried 2026-10-21.

Q7SAD4 is placed in PTHR23023:SF292 FLAVIN-BINDING MONOOXYGENASE-LIKE PROTEIN (AFU_ORTHOLOGUE AFUA_6G01900).
Path from the leaf to the root of the PTHR23023 tree (reproduced by `panther_placement.py`, output `panther_placement_output.txt`):

| node | event | taxon | subfamily | leaves |
|---|---|---|---|---|
| PTN000545913 | duplication | (Neurospora in-paralogs) | SF292 | 2 (NCU06296, NCU08749) |
| PTN001125012 | speciation | Sordariomyceta | SF292 | 4 |
| PTN001125011 | speciation | Sordariomycetes-Leotiomycetes | SF292 | 5 |
| PTN002744969 | duplication | Sordariomycetes-Leotiomycetes | SF292 | 8 |
| PTN002346104 | speciation | Pezizomycotina | SF292 | 11 (incl. Aspergillus fumigatus AFUA_6G01900, A. nidulans ANIA_02629/ANIA_08660) |
| PTN008587727 | duplication | Pezizomycotina | SF226 | 13 |
| PTN008378500 | speciation | Dikarya | SF226 | 15 |
| PTN007724818 | speciation | Fungi | SF226 | 16 |
| PTN000545687 | speciation | Opisthokonts | SF226 | 215 (sister to the whole animal FMO clade) |
| PTN008378499 | speciation | Eukaryota | SF226 | 497 (adds plant FMOs) |
| PTN004593253 | duplication | Eukaryota | SF266 | 842 |
| PTN000545685 | speciation | LUCA | SF266 | 848 |
| PTN009058586 | root | - | - | 850 |

Findings:

- The fungal clade containing Q7SAD4 is joined to the animal FMO clade by a speciation node
  (Opisthokonts). Human FMO1, FMO2, FMO3, FMO4 and FMO5 arise from later animal duplications
  and are therefore all co-orthologs of the fungal clade at equal phylogenetic distance; each
  sits in its own subfamily (SF154, SF84, SF44, SF74, SF78), not in SF292.
- No member of SF292 or of the fungal clade has experimental GO annotation; every leaf in the
  Fungi node is an uncharacterised genome-project entry.
- The IBA "monooxygenase activity" on Q7SAD4 lists PANTHER:PTN009058586, the family root.
  The PANTHER GO-slim MF annotation on every node of the path carries only generic terms
  (oxidoreductase, monooxygenase, NAD(P)H-dependent single-oxygen-incorporating oxidoreductase
  GO:0016709); no substrate-specific activity (e.g. GO:0004499) is placed on any ancestor.
- Yeast FMO1 (P38866, the yFMO of PMID:10077572) is classified by PANTHER 19 in a different
  family, PTHR43539:SF78; S. pombe fmo1 (Q9HFE4) is in PTHR23023:SF266 on a branch outside the
  Eukaryota SF226 clade. Neither is a close relative of Q7SAD4.

## 2. Motif and hydrophobicity scan

Scripts: `motif_scan.py` (output `motif_scan_output.txt`) and `align_fmo3.py`
(output `align_fmo3_output.txt`), run with `uv run --script`.

- FAD-binding Rossmann motif GxGxxG is conserved at residues 10-15 (GSGLFG), aligned to
  FMO3 GAGVSG (9-14).
- The FMO-identifying motif FxGxxxHxxxY of FMO3 (FKGKCFHSRDY, 166-176) is not present as a
  contiguous motif; the global alignment maps it to Q7SAD4 159-175 with an insertion, and the
  aligned residues read FKGQ...LFHSKEL (F, K, G and the H-S pair retained).
- The second (NADPH-binding) GxGxxG motif of FMO3 (GLGNSG, 191-196) is not conserved; the
  aligned Q7SAD4 segment (191-209, VLGSKG in the alignment, around VVTVLGGTKSAWD) lacks the
  GxGxxG pattern.
- The FMO3 FATGY motif (327-331) has no aligned counterpart in Q7SAD4.
- Global identity to FMO3 over 441 aligned pairs is 29.3%.
- No 19-residue Kyte-Doolittle window reaches 1.6 in Q7SAD4 (mammalian FMO3 has a C-terminal
  membrane anchor that does reach this threshold); the Q7SAD4 C-terminus is charged.

Interpretation (inconclusive on cofactor specificity): the FAD-binding motif and the core of
the FMO motif are retained, consistent with a flavin-dependent monooxygenase. The canonical
NADPH-binding dinucleotide motif and FATGY are diverged, so NADPH (versus NADH) preference
cannot be read from the sequence. There is no predicted C-terminal membrane anchor of the
mammalian type, so ER-membrane localization of mammalian FMOs should not be transferred.
