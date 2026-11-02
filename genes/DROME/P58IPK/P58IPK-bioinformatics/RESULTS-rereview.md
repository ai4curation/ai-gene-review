# P58IPK (Q9VHA8) re-review analysis

Script: `rereview_analysis.py` (run with `uv run rereview_analysis.py`); raw output: `rereview_output.txt`.
Sequences fetched live from UniProt REST; tree from the PANTHER 19 treeinfo API for PTHR44140.

## Identity of the benchmark accession

Q9VHA8 (498 aa) is the FlyBase-linked UniProt entry for FBgn0037718 and is not a fragment or alternative gene model. The only other fly PTHR44140 entry, Q7K3H7 (498 aa), has an identical sequence (Q9VHA8 == Q7K3H7 sequence: True). No reviewed Swiss-Prot entry exists for the fly gene.

## Pairwise identity (global, BLOSUM62, % of shorter sequence)

| accession | protein | length | identity to Q9VHA8 | HPD present |
|---|---|---|---|---|
| Q13217 | human DNAJC3 | 504 | 44.6% | True |
| Q91YW3 | mouse Dnajc3 | 504 | 45.2% | True |
| P91189 | worm dnj-7 | 491 | 44.6% | True |
| P40358 | yeast JEM1 | 645 | 29.1% | True |

The J-domain HPD tripeptide of Q9VHA8 is at residues 424-426 (AAQKWHPDNFRDE), in the J domain annotated at 396-463. This H424 is the counterpart of the invariant P58 H422 that mediates BiP interaction in mouse P58/DNAJC3 (PMID:18923430).

## PANTHER tree placement

Leaf paths (root to parent) for model-organism members:

- P58IPK FlyBase:FBgn0037718 (PTHR44140:SF2): Eukaryota PTN001941043 > Unikonts > Opisthokonts PTN002454288 > Metazoa-Choanoflagellida > Eumetazoa > Bilateria PTN000637047 > Protostomia > Ecdysozoa > Arthropoda > Hexapoda-Crustacea > Endopterygota > Diptera.
- DNAJC3 HGNC:9439 (PTHR44140:SF3): ... > Bilateria PTN000637047 > Deuterostomia > Chordata > Craniata-Tunicata > DUPLICATION PTN001531906 > Euteleostomi PTN002891327 > ... > Homo-Pan.
- JEM1 SGD:S000003609 (PTHR44140:SF2): ... > Opisthokonts PTN002454288 > Fungi > ... > Saccharomycetaceae.
- dnj-7 (SF2) and dnj-28 (SF4) of C. elegans descend from a nematode duplication PTN000637080 under Ecdysozoa.

Interpretation: fly P58IPK and human DNAJC3 are orthologs, joined by the Bilateria speciation node PTN000637047. The PANTHER subfamily label difference (SF2 for fly, SF3 for DNAJC3) arises because the SF3 boundary is drawn at the vertebrate duplication PTN001531906 (DNAJC3 versus the teleost dnajc3b/prkri SF1 copy), not because fly and human belong to paralogous clades. SF2 as labelled is therefore a grade that contains the ancestral nodes (Eukaryota to Bilateria) and all non-vertebrate members including yeast JEM1, which is a more distant (Opisthokont-level) relative. The nearest experimentally characterised relative by tree placement is vertebrate DNAJC3 (human Q13217; mouse Q91YW3).

The PAINT IBD assertions are all placed at the Eukaryota root node PTN001941043 (ER, protein-folding chaperone binding, misfolded protein binding, protein folding in ER), so they apply to the fly gene by descent. Vertebrate-specific DNAJC3 activities documented in mammals (eIF2-alpha kinase inhibition) were not placed on any ancestral node in the PAINT file and are not transferred.

## Limits

No signal-peptide or transmembrane predictor was run here; the SignalP feature (1..36) is from the UniProt record. No full multiple alignment or tree was built; placement relies on the PANTHER 19 tree.
