# CG8142 curation notes

- CG8142 is an AAA+ activator-1 small subunit of replication factor C; ortholog of human RFC4 (named Rfc37 in PMID:27198229).
- Little gene-specific experimental work exists; evidence is from the RFC/RLC literature and fly complex purification.
- RFC function (general): [PMID:8999859 "It is a molecular matchmaker required for loading of proliferating cell nuclear antigen (PCNA) onto double-stranded DNA"]; [PMID:8999859 "Replication factor C (RF-C) is a heteropentameric protein essential for DNA replication and repair"].
- Elg1 complex membership in S2 cells: [PMID:27198229 "identified peptides from all components of the Elg1 PCNA-unloader complex: Elg1, Rfc4, Rfc38, CG8142, and Rfc3"]. Elg1 complex unloads PCNA: [PMID:27198229 "knocking down elg1 using dsRNAs did not affect total PCNA levels but resulted in increases in the levels of both chromatin-bound PCNA and monoubiquitinated PCNA"].
- PMID:24204884 (Elongin/Corto) cited by FlyBase NAS/IPI rows does not mention RFC (full text searched); flagged MISCITED; claims judged on RFC biology.
- Protein binding IPI rows are with other RFC small subunits (GOA WITH/FROM); removed as uninformative.
- Same decision table as RfC4/RfC3/RfC38/CG8142 (module consistency): contributes_to GO:0003689 and GO:0061860 (core), complexes GO:0005663 and GO:0031391.
- Round-2 rule applied: generic parents (DNA replication, ATP-dependent activity acting on DNA, protein-containing complex) changed from KEEP_AS_NON_CORE to MODIFY toward the specific term the gene already carries; subunit-level binding/ATPase terms stay KEEP_AS_NON_CORE.
- Naming: UniProt's automated (ARBA) RecName for Q9VX15 is "Replication factor C subunit 2" with synonyms DmRFC2/RFC2, and the GOA symbol is Rfc37; by sequence and by PMID:27198229 ("we refer to CG8142 here as Rfc37") the protein is the 37 kDa subunit orthologous to human RFC4. The ARBA name should not be read as a correction. The folder follows the symbol used in the module/task (CG8142).
- Review-bot round: added NEW contributes_to GO:0061860 DNA clamp unloader activity (IDA, PMID:27198229) so the core-function claim has an annotation row; identical across the four small subunits.
