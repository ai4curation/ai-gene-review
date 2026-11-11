# Dic4 (Q9VVS1) placement within PTHR45618:SF13 — re-review analysis (2026-10-20)

Script: `fetch_and_tree.py` (run with `uv run --with biopython python fetch_and_tree.py`).
Outputs: `sf13_members.fasta`, `sf13_members.aln.fasta` (MAFFT L-INS-i), `sf13_nj.nwk`, `results-rereview.txt`.

## Inputs

PANTHER 19.0 classification files place all six Drosophila Dic-like carriers (Dic1 Q9Y166, Dic2 Q9VDM3,
Dic3 A1Z787, Dic4 Q9VVS1, CG16736 Q9VHG7, CG6893 A0A6M3Q724) in PTHR45618:SF13 MITOCHONDRIAL DICARBOXYLATE
CARRIER, together with human SLC25A10 (Q9UBX3), mouse Slc25a10 (Q9QZD8) and yeast DIC1 (Q06143). Human
SLC25A11 (OGC, Q02978) was used as outgroup.

## Results

Pairwise identity to Dic4 over aligned non-gap columns: Dic3 0.418, Dic1 0.407, SLC25A10 0.388, Dic2 0.386,
mouse Slc25a10 0.377, CG6893 0.336, DIC1_YEAST 0.289, SLC25A11 0.284, CG16736 0.221.

Neighbour-joining tree (BLOSUM62 distances, 200 bootstrap replicates, rooted on SLC25A11):

```
(((((((((Slc25a10_MOUSE,SLC25A10_HUMAN)100,Dic1_DROME)43.5,Dic2_DROME)61.5,Dic3_DROME)47.5,Dic4_DROME)20.5,CG6893_DROME)17.5,CG16736_DROME)5,DIC1_YEAST),SLC25A11_HUMAN_outgroup);
```

- Dic4 has the longest terminal branch of the Dic1-Dic4 group (0.32 vs 0.18 for Dic1 and 0.25 for Dic3).
- The tree places Dic4 outside a (SLC25A10 + Dic1, Dic2, Dic3) group, but support for every internal node
  among the fly paralogs is low (<62%), so the branching order of Dic1-Dic4 is not resolved by this analysis.
- Mammalian SLC25A10 pairs most closely with Dic1 (consistent with Dic1 being the functional DIC ortholog,
  PMID:21130726), so SLC25A10 is a co-ortholog of the whole fly Dic expansion rather than a 1:1 ortholog of Dic4.

## PAINT context (from `interpro/panther/PTHR45618/PTHR45618-paint.tsv` and QuickGO IBA rows)

The eukaryote-level IBD node PTN000756618 carries dicarboxylate (malate, succinate, oxaloacetate),
phosphate, sulfate and thiosulfate transport. PAINT curators added fly-specific IRD (NOT) nodes:
PTN000640886 (blocks malate GO:0015140/GO:0071423) and PTN000640888 (blocks malate, succinate, oxaloacetate
and their transport). In current QuickGO IBA rows, Dic3 lacks only the malate terms, whereas Dic4 lacks all
dicarboxylate terms but keeps phosphate, sulfate and thiosulfate terms. This matches Dic4 lying under
PTN000640888 and Dic3 under PTN000640886 only. The curator therefore deliberately withdrew dicarboxylate
transport from the Dic4 lineage but left the phosphate/sulfur-anion terms in place.

## Interpretation

Dic4 is a fast-evolving, fly-lineage paralog inside the DIC subfamily. It has no 1:1 characterised ortholog.
By sequence identity its nearest experimentally characterised relatives are Dic3 and Dic1, and the tree does
not reliably separate them. Dic1 is the reviewed paralog with a typical DIC activity, and the human co-ortholog
SLC25A10 is the best-characterised member of the subfamily. Neither placement supports transferring a
substrate-specific activity to Dic4: its only direct test (PMID:21130726) found no transport.

Limitations: this is a distance tree on 10 sequences, with low support values. It is not the PANTHER/PAINT
tree, and contact-point residues were not analysed here.
