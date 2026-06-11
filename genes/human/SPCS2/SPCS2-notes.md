# SPCS2 (Signal peptidase complex subunit 2) — review notes

UniProt: Q15005 (SPCS2_HUMAN), 226 aa; aka SPC25, "Microsomal signal peptidase 25 kDa subunit". HGNC:28962, chr 11. Multi-pass ER membrane protein (two TM helices ~87-107 and 112-132), N and C termini cytosolic.

## Core identity / function
- One of three non-catalytic accessory subunits (SPCS1, SPCS2, SPCS3) of the ER signal peptidase complex (SPC). Catalytic subunits = SEC11A (SPC-A) / SEC11C (SPC-C).
  - UniProt FUNCTION: "Component of the signal peptidase complex (SPC) which catalyzes the cleavage of N-terminal signal sequences from nascent proteins as they are translocated into the lumen of the endoplasmic reticulum (PubMed:34388369). Enhances the enzymatic activity of SPC and facilitates the interactions between different components of the translocation site (By similarity)." [UniProt Q15005]
  - UniProt SUBUNIT: "Component of the signal peptidase complex paralog A (SPC-A) composed of a catalytic subunit SEC11A and three accessory subunits SPCS1, SPCS2 and SPCS3 ... Within the complex, interacts with SEC11A or SEC11C and SPCS1 ... The complex induces a local thinning of the ER membrane which is used to measure the length of the signal peptide (SP) h-region."
- Note: unlike SPCS1, SPCS2 is described (by similarity to yeast Spc25/Q04969) as ENHANCING SPC enzymatic activity and facilitating translocation-site component interactions. Still non-catalytic.
- Cryo-EM structure: [PMID:34388369] identifies SPCS2 in both SPC paralogs (PDB 7P2P/7P2Q).
- Historical: SPC25 (=SPCS2) topology determined together with SPC12 in [PMID:8632014] (the 25-kDa subunit). [SPCS2 GOA itself does not cite 8632014, but UniProt links it.]

## Secondary / non-core
- PMID:34232536 (coronavirus interactome): IntAct interaction with SARS-CoV-2 Spike (P0DTC2). High-throughput; bare protein binding; non-core.

## Annotation assessment
- GO:0005787 signal peptidase complex (IBA, IEA, IPI/ComplexPortal) — CORE, ACCEPT.
- GO:0005789 ER membrane (IEA, IDA, ISS, TAS) — CORE localization, ACCEPT.
- GO:0016020 membrane (IEA) — generic; KEEP_AS_NON_CORE.
- GO:0045047 protein targeting to ER (IBA) — mis-specified; SPC acts after translocation. MODIFY -> GO:0006465 signal peptide processing (UniProt DR uses GO:0006465 IDA:ComplexPortal).
- GO:0016485 protein processing (IDA, ComplexPortal) — ACCEPT (correct; GO:0006465 is more specific). Core process.
- GO:0005515 protein binding (IPI PMID:34232536 SARS-CoV-2 S; IPI PMID:34388369 intra-complex SPCS1/SEC11A/SPCS3) — KEEP_AS_NON_CORE (bare protein binding).

## Core function summary
Non-catalytic accessory subunit of the ER signal peptidase complex; ER multi-pass membrane protein that enhances SPC enzymatic activity and facilitates interactions at the translocation site, contributing to signal peptide processing of preproteins.
