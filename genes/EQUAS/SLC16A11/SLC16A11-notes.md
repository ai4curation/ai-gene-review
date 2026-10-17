# SLC16A11 (donkey, A0A9L0JV53) notes

DONKEY40 cohort review (ProtNLM2 evaluation). Unreviewed TrEMBL entry, 439 aa; names and comments come from ARBA.

## Identity and sequence
- PANTHER PTHR11360:SF80 (MONOCARBOXYLATE TRANSPORTER 11); InterPro MFS (IPR011701) and proton-linked MCT (IPR050327) [file:EQUAS/SLC16A11/SLC16A11-uniprot.txt "DR   PANTHER; PTHR11360:SF80; MONOCARBOXYLATE TRANSPORTER 11; 1."].
- Gene-model defect: donkey residues 1-100 are not homologous to human Q8NCK7, while donkey 101-439 align to human 113-447 at high identity; human TM1-TM3 have no counterpart [file:EQUAS/SLC16A11/SLC16A11-bioinformatics/RESULTS.md "The human N-terminal region containing predicted transmembrane helices 1-3 (human 12-32, 54-74, 82-102) therefore has no homologous counterpart in the donkey model"].
- The donkey sequence does not begin with Met, consistent with an incomplete/misassembled 5' end. The donkey gene is still expected to encode a full-length MCT11; the defect is in this UniProt/Ensembl model.

## Function (human ortholog)
- Proton-linked monocarboxylate transporter that moves pyruvate across the plasma membrane; implicated in hepatic lipid metabolism and type 2 diabetes risk [file:EQUAS/SLC16A11/SLC16A11-bioinformatics/SLC16A11-human-Q8NCK7-uniprot.txt "Proton-linked monocarboxylate transporter. It catalyzes the"].
- Location: ER membrane (PMID:24390345) and cell membrane, where it pairs with BSG (PMID:28666119) [file:EQUAS/SLC16A11/SLC16A11-bioinformatics/SLC16A11-human-Q8NCK7-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"]. Neither paper is cached locally; evidence taken from the Swiss-Prot record.

## Annotation decisions
- ER membrane, plasma membrane: ACCEPT.
- monocarboxylic acid transmembrane transporter activity and monocarboxylic acid transport (TreeGrafter): ACCEPT.
- transmembrane transporter activity, transmembrane transport (InterPro2GO): TOO_GENERAL.
- NEW pyruvate transmembrane transporter activity (ISS from human IDA).

## ProtNLM2
- GO:0022857 transmembrane transporter activity: correct, in donkey GOA, but less specific than donkey GOA's monocarboxylic acid transmembrane transporter activity -> LSP.
- No non-GO ProtNLM2 rows for this accession.
