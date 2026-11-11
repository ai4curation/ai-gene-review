# Horse TGFBR3 (F7E1V2) sequence comparison with human and mouse TGFBR3

Scripts: `compare_to_human.py` (output `compare_to_human.out`) and `nterm_alignment.py`
(output `nterm_alignment.out`). Both fetch sequences live from UniProt REST and run a
global BLOSUM62 alignment (Biopython PairwiseAligner, gap open -10, extend -0.5).
Run with `uv run --script <script>`.

## Phylogenetic placement

UniProt places F7E1V2 in PANTHER PTHR14002:SF7 (TRANSFORMING GROWTH FACTOR BETA RECEPTOR
TYPE 3), the same subfamily as human Q03167, mouse O88393 and rat P26342
(`interpro/panther/PTHR14002/PTHR14002-entries.csv`). The IBA rows descend from PAINT node
PTN002678643 (Euteleostomi TGFBR3 clade) and PTN008553354.

## Results

- Horse F7E1V2 is 809 aa; human Q03167 is 851 aa. Identity over 806 aligned residues is 0.870
  (mouse O88393: 0.831 over 798 aligned residues).
- Human residues 2-12 and 51-81 have no horse counterpart, and horse residues 1-41 do not
  align with human residues 1-80. The horse N-terminus (MMKALAAPLGSPSPSAFGTFLWQNSLNFMEVGAYLEEKKVLS)
  has no hydrophobic h-region: the maximum Kyte-Doolittle mean over a 12-residue window is 0.71,
  far below a signal peptide. Human residues 1-20 are the predicted signal peptide (UniProt Q03167).
  So the Ensembl model ENSECAT00000021086.3 most likely has a wrong first exon or start codon.
  The F7E1V2 entry has no SignalP feature, only an ARBA "Signal" keyword.
- From human residue 82 onwards the horse model matches closely, apart from 1-residue and
  2-residue indels (human 359 and 762-763).
- Conserved functional positions: GAG attachment serines human S534/S545 map to horse S494/S505.
  The phospho-Thr840 that mediates beta-arrestin2 binding maps to horse T798. The ligand-interaction
  region human 737-751 maps to horse 697-711. The C-terminal PDZ-binding tail STPCSSSSTA is identical.
  The ZP domain (415-690) and transmembrane helix (743-767) are annotated on F7E1V2.

## Interpretation

F7E1V2 is the horse TGFBR3 ortholog. Every functional region characterised in the rodent and
human proteins is conserved, except the extreme N-terminus. In the horse model that region looks
like a gene-model artefact: there is no signal peptide, and roughly 30 residues of the
endoglin-related (orphan) domain N-terminus are missing. The real horse protein is almost
certainly a type I membrane proteoglycan with a canonical signal peptide. This result was not
checked against horse transcript data.
