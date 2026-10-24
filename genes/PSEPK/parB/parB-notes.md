# parB (PP_0001, P0A151), Pseudomonas putida KT2440

## 2026-10-23: initial review

**Identity.** ParB/Spo0J-family centromere-binding protein, the first annotated gene of KT2440,
next to parA and oriC. NCBI WP_003253185.1 "MULTISPECIES: ParB/RepB/Spo0J family partition
protein [Pseudomonas]", named from SPARCLE architecture 11445026. UniProt Swiss-Prot entry with a
curated "by similarity" function [file:PSEPK/parB/parB-uniprot.txt "Binds to the DNA origin of
replication (By similarity)."].

**Domains and motifs.** ParB_N (ParB/Srx fold, CTP-binding; PF02195), HTH_ParB (PF17762), ParB_C
dimerisation (PF23552); TIGR00180. CTP-binding box GERRWRA at 91-97, identical in P. aeruginosa
ParB (79% identity overall) [file:PSEPK/parA/parA-bioinformatics/RESULTS.md].

**P. putida evidence.** parA and parB mutants give 5-10% anucleate cells in M9 at the transition
to stationary phase [PMID:11832517]. ParAB stabilises a parS-carrying mini-F in E. coli, and three
parS-like sequences lie in the oriC-parAB region [PMID:11849535 "Three sequences similar to
cis-acting stabilization sites of Bacillus subtilis are present in the P. putida oriC-parAB
region."].

**CTPase.** ParB proteins are CTP-dependent clamps [PMID:31649139 "We show that ParB is an enzyme
that hydrolyzes cytidine triphosphate (CTP) to cytidine diphosphate (CDP)."; PMID:31835030;
PMID:32077854 "show that CTP is required for spreading"]. P. aeruginosa ParB has been assayed
directly [PMID:38843873 "We found that the same holds true for the P. aeruginosa ParB."]. CTP
dependence is ancestral in the family [PMID:41448349]. Proposed NEW CTPase activity (ISO), and NEW
sequence-specific DNA binding (ISO) to record the evidence behind the DNA binding MODIFY.

**Sporulation.** The GOA (TreeGrafter) term positive regulation of sporulation is inherited from
B. subtilis Spo0J. P. putida does not sporulate [PMID:11849535 "not known to pass through
developmental phases"]. REMOVE.

**Related P. putida paper.** A ParB-like CTPase clamp, BisD, drives gene activation in P. putida
transfer competence (PMID:40842242). BisD is a separate protein of the ICE-associated
ParB-like family, not PP_0001.

**NCBI/CDD comparison.** The architecture gives only DNA binding. TIGR00180 also matches and
carries chromosome segregation, cytokinesis and DNA binding, but under winner-take-all only the
naming source passes on GO, so chromosome segregation is lost. The CDD region note still calls the
N-terminal domain a "ParB-like nuclease domain".
