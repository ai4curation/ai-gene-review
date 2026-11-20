# rmt2 curation notes

`ASPFU/rmt2` was fetched on 2026-11-20 from UniProt accession `Q4X1R1`, whose
primary gene name is `rmt2` and whose ORF name is `AFUA_2G09080`.

Manual searches on 2026-11-20 did not find a direct A. fumigatus rmt2
biochemical, deletion, localization, or translational-fidelity paper. I searched
for `AFUA_2G09080`, `Q4X1R1`, `"Aspergillus fumigatus" "rmt2"`,
`"Aspergillus" "Protein arginine N-methyltransferase 2"`, and broader fungal
Rmt2 phrases. The usable evidence is therefore the reviewed UniProt record, the
GOA homology inferences, the completed budding-yeast, fission-yeast, and
Neurospora Rmt2 family reviews, and the local `PTHR32379` PAINT slice.

The official PANTHER family name for `PTHR32379` is GUANIDINOACETATE
N-METHYLTRANSFERASE, but the PAINT table keeps the fungal Rmt2 branch separate
from vertebrate GAMT. The fungal `PANTHER:PTN001285370` node carries
`GO:0019702` protein arginine N5-methyltransferase activity from the
experimentally characterized S. cerevisiae seed. The vertebrate
`PANTHER:PTN001285367` node carries guanidinoacetate N-methyltransferase
activity and creatine biosynthesis, so those assertions should not propagate to
fungal rmt2 genes.

UniProt infers A. fumigatus rmt2 function and nucleus/cytoplasm localization
from budding-yeast Q03305. The PAINT nucleus and cytoplasm IBAs are broader
than the core activity, but they are the same PTHR32379 root placements already
accepted for `SCHPO/rmt2` and `NEUCR/ant-1`, and no A. fumigatus evidence
contradicts them.

The EnsemblFungi GO_REF:0000107 row for `GO:0019702` matches the fungal PAINT
activity and should be accepted. Its `GO:0045903 positive regulation of
translational fidelity` transfer is different: S. cerevisiae RMT2 has a direct
ribosome-function phenotype, but there is no direct A. fumigatus evidence yet,
and the PTHR32379 PAINT curator did not put a translation-process assertion on
the fungal Rmt2 node.
