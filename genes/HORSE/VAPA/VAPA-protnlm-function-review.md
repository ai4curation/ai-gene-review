# VAPA: ProtNLM function-text review

**PLI (score 0): nematode sperm-MSP function is transferred to a membrane-anchored VAPA protein.**

## Original prediction

[ProtNLM A0A3Q2H1L9](https://www.uniprot.org/uniprotkb/A0A3Q2H1L9/entry#prot-nlm), frozen API snapshot 2026-09-08.

> Central component in molecular interactions underlying sperm crawling. Forms an extensive filament system that extends from sperm villipoda, along the leading edge of the pseudopod

## Claims and evidence

Both sperm crawling and the villipodial/pseudopod filament system describe the nematode major-sperm-protein motility system. [PMID:14565983](https://pubmed.ncbi.nlm.nih.gov/14565983/) experimentally dissects Ascaris MSP-based amoeboid locomotion. This is a specific homologous-domain functional transfer, not a generic statement about a mammalian sperm protein.

Horse VAPA instead retains a cytoplasmic MSP domain at residues 14–131, a coiled-coil region and a C-terminal transmembrane helix at 273–293. Its MSP domain is virtually identical to human VAPA, including the experimentally defined FFAT-binding region. The 45-residue horse insertion is in the intervening linker, corresponding to human alternative splicing; it does not convert the protein into a soluble nematode sperm filament subunit. [Reproducible alignment](VAPA-bioinformatics/RESULTS.md).

The primary VAPA structural/biochemical study states: “VAP‐A, VAP‐B, and MOSPD2 are anchored in the ER membrane by a carboxyl‐terminal transmembrane domain with their MSP domain projecting into the cytosol.” It directly tests FFAT recognition and lipid-transfer contact formation ([PMID:33124732](https://pubmed.ncbi.nlm.nih.gov/33124732/)). The horse architecture and conservation justify transferring this adaptor mechanism. An MSP-domain name alone does not justify transferring the nematode motility mechanism.

**Error type: PARALOG_OVERANNOTATION**, used here for functional over-transfer between homologous MSP-domain protein groups. The exact model training donor is unknown. Both atomic motility claims are contradicted by the target architecture and mammalian biological context. No training-set novelty conclusion is made.
