# Curation Notes: Bacteriophage T4 `ac` (Acridine sensitivity protein / gp52.2, P18924)

## Overview
- **Gene symbol:** `ac` (synonym: `52.2`)
- **UniProt ID:** `P18924` (`Y522_BPT4`)
- **Length:** 51 amino acids
- **Function:** Small hydrophobic host-membrane protein (gp52.2) whose wild-type expression renders T4 development sensitive to acridine dyes (such as acriflavin) by increasing host membrane permeability; loss-of-function mutations in `ac` confer acridine resistance.

## Biological Role and Mechanism
- Gene `ac` (historically mapped to ORF `52.2`, encoding a 51-aa hydrophobic polypeptide with two predicted transmembrane segments) was identified as the classical T4 acridine-resistance locus (Silver 1965, 1967; Mosig et al. 1998, PubMed 9560385; Miller et al. 2003, PubMed 12626685).
- Wild-type T4 infection increases uptake of acriflavin and related acridine compounds across the *Escherichia coli* cell envelope, inhibiting phage DNA replication and maturation; null or missense mutations in `ac` abolish this phage-induced acridine uptake and allow T4 development in the presence of acriflavin (PubMed 9560385).
- Apart from conferring acridine sensitivity via host membrane insertion/modification, the physiological role of `ac` during normal uninhibited T4 infection remains uncharacterized.

## Review of Existing GO Annotations
- `GO:0033644` (host cell membrane, IEA, GO_REF:0000044): **ACCEPT**. Consistent with its strongly hydrophobic two-transmembrane-helix architecture, UniProt subcellular location annotation, and physiological role in modifying host membrane permeability to acridines.
- `GO:0046677` (response to antibiotic, IEA, GO_REF:0000043): **REMOVE**. This annotation is an automated UniProt keyword-mapping artifact (`Antibiotic resistance` -> `GO:0046677`). First, acridines/acriflavin are intercalating dye mutagens/antiseptics rather than classical antibiotics. Second, and more importantly, the wild-type `ac` gene product does not mediate a protective response to an antibiotic; rather, wild-type `ac` makes the infected cell *sensitive* to acridines, and only *loss-of-function* mutations in `ac` confer acridine resistance (PubMed 9560385).
