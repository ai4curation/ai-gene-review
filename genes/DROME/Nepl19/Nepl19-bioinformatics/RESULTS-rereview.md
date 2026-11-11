# Nepl19 subfamily placement (re-review, 2026-10-20)

Script: `subfamily_tree_rereview.py` (run with `uv run python subfamily_tree_rereview.py`).
Outputs: `subfamily_rereview.fasta`, `subfamily_rereview_aln.fasta`, `subfamily_rereview_tree.nwk`,
`subfamily_rereview_results.json`. These files are new and do not replace the earlier catalytic-site
analysis in `RESULTS.md`.

## Inputs

UniProt lists the following D. melanogaster canonical gene products in PANTHER subfamily
PTHR11733:SF238 (FI07649P-RELATED): Nepl19 Q9VAS1, Nepl17 Q9VAS4, Nepl18 Q9VAS2, Nepl20 Q9VAS0,
Nepl21 Q9Y136, Nepl15 Q9VCU1, Nep6 Q9VYJ1 and Nep4 Q8T062. Fly Nep2 (A0A0B4K692, SF224) and human
MME/neprilysin P08473 were added as out-of-subfamily references. The subfamily is insect-specific; its
UniProt members are dipteran and other insect sequences, so there is no vertebrate ortholog of Nepl19.

## Method

MAFFT L-INS-i alignment; Biopython identity distances; neighbour-joining tree rooted on human MME.
This is a quick distance tree without bootstrap support, so it indicates the grouping only roughly.

## Results

Percent identity of Nepl19 over aligned columns: Nepl21 33.1, Nepl20 32.6, Nepl17 31.5, Nepl18 31.1,
Nepl15 27.5, Nep4 27.4, Nep6 22.6, Nep2 21.6, human MME 20.9.

NJ topology: Nepl19 groups with the other 98F1 tandem-cluster paralogs (Nepl17, Nepl18, Nepl20,
Nepl21). Nepl15 is the next branch outside that cluster, then Nep6. Nep4 falls outside this Nepl clade
and groups with Nep2 (SF224), even though PANTHER places it in SF238.

Motif aligned to human MME HEITH (584-588):

| Protein | Motif |
|---|---|
| Nepl19 Q9VAS1 | QQLAH |
| Nepl17 Q9VAS4 | HEMAH |
| Nepl18 Q9VAS2 | HEMLH |
| Nepl20 Q9VAS0 | HELIH |
| Nepl21 Q9Y136 | HELIH |
| Nepl15 Q9VCU1 | RQMLH |
| Nep6 Q9VYJ1 | HEMVH |
| Nep4 Q8T062 | HELTH |
| Nep2 A0A0B4K692 | HEITH |
| human MME P08473 | HEITH |

## Interpretation

Within the 98F1 cluster, only Nepl19 has lost the HExxH zinc ligand and catalytic glutamate. Its
closest relatives keep that motif, so the loss happened recently in the Nepl19 lineage. Nepl15, the
nearest paralog that has been studied experimentally, has also lost the first His and the catalytic
Glu (RQMLH). Under this tree that loss arose independently. The two proteins are therefore comparable
non-catalytic M13 paralogs, but Nepl19 cannot inherit anything specific to Nepl15 from this tree.
Nep4 is catalytically active and is the only SF238 member with known in vivo substrates. It sits
outside the Nepl clade in this tree, and its peptidase activity does not transfer to Nepl19, whose
catalytic motif is disrupted.
