# lepB research notes

## Functional assignment

LepB is the KT2440 type I signal peptidase (EC 3.4.21.89). The local UniProt
record states that it cleaves hydrophobic N-terminal signal or leader sequences
from secreted and periplasmic proteins [file:PSEPK/lepB/lepB-uniprot.txt
"Cleavage of hydrophobic, N-terminal signal or leader sequences from secreted
and periplasmic proteins."].

The local UniProt record still maps the S26 peptidase to GO:0006465
[file:PSEPK/lepB/lepB-uniprot.txt "GO; GO:0006465; P:signal peptide processing;
IEA:InterPro."]. The authoritative [QuickGO term endpoint](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0006465),
retrieved 2026-08-08, returns `isObsolete: true`, names the term `obsolete signal
peptide processing`, and gives the definition "OBSOLETE. The proteolytic removal
of a signal peptide from a protein during or after transport to a specific
location in the cell." Its comment recommends the molecular-function term
GO:0009003 signal peptidase activity. The fetched GOA row carries GO:0051604
protein maturation, which is sound but broad; live GO:0016485 protein processing
is the more specific process for maturation by peptide-bond cleavage and is the
better replacement for LepB-mediated signal-peptide cleavage.

## Localization

UniProt calls LepB a multi-pass membrane protein. Plasma-membrane localization
is a taxon-aware refinement: in Gram-negative P. putida, the Sec channel and
type I signal peptidase occupy the cytoplasmic membrane. No independent
KT2440-specific topology experiment was found in this first pass.
