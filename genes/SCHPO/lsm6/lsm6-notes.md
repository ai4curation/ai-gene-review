# lsm6 evidence notes

Lsm6 is a conserved Sm-fold RNA-binding protein shared by the Lsm2-8 and Lsm1-7 complexes. Nuclear Lsm2-8 recognizes uridine-rich RNA ends and supports U6 snRNA function, spliceosome assembly and telomerase RNA protection. Cytoplasmic Lsm1-7 associates with Pat1 and promotes mRNA decapping and turnover. Fission yeast structures and RNA-binding assays establish the contribution of Lsm6 to these oligomeric RNA-binding assemblies.

## Identity and prediction provenance

PomBase primary symbol lsm6, locus SPAC2F3.17c, current UniProt Q9UUI1. The supplied pre-release post-processed-2026_02_28k.xml is the source of the reviewed claims; its placeholder sequence, taxonomy and dates are not biological metadata. The current UniProt sequence is not established as the model input. Current API availability and published-list inclusion are separate properties; all biological judgments here concern the preserved original claims.

## Primary evidence inspected

- [PMID:22615807 Crystal structures of Lsm3, Lsm4 and Lsm5/6/7 from Schizosaccharomyces pombe.] "RNA binding assays show that Lsm2/3 and Lsm5/6/7 bind to oligo(U) whereas no RNA binding is observed for Lsm3 and Lsm4. Analysis of the inter-subunit interactions in Lsm5/6/7 reveals the organization order among Lsm5, Lsm6 and Lsm7."
- [PMID:32518066 Molecular basis for the distinct cellular functions of the Lsm1-7 and Lsm2-8 complexes.] "The multi-ORF expression system was assembled into a single plasmid through ligation independent cloning as described for Lsm2–8, with the ORFs assembled in order Lsm6, Lsm3, Lsm2, Lsm1, Lsm4, Lsm7, and Lsm5."
- [PMID:16823372 ORFeome cloning and global analysis of protein localization in the fission yeast Schizosaccharomyces pombe.] "Next, we determined the localization of 4,431 proteins, corresponding to approximately 90% of the fission yeast proteome, by tagging each ORF with the yellow fluorescent protein."

## Evidence limits and adjudication

- GO:0005515 (KEEP_AS_NON_CORE): Retain the reported physical interaction as supporting complex-assembly evidence. Generic protein binding does not specify the nuclease or RNA-binding function and is not a useful core molecular-function summary.
- GO:0005682 (UNDECIDED): The original fission yeast spliceosome structure contains U2 and U5 particles, but the available abstract does not establish the specific Lsm6 contact or subcomplex assignment. Lsm6 is canonically an Lsm-ring component associated with U6, so the exact U2/U5 assignment requires inspection of the full structural model and supplementary protein identities. No misattribution is inferred from the abstract alone. The original PMID:26292707 remains the evidence source requiring resolution.
- GO:0005730 (KEEP_AS_NON_CORE): Curated phylogenetic evidence supports an ancillary nucleolar RNA-processing role, consistent with Lsm2-7 association with snoRNA in budding yeast. This is compatible with conserved RNA-binding ring biology but is less directly established for fission yeast Lsm6 than its Lsm1-7 and Lsm2-8 roles.

Primary reports are interpreted at the species, assay and subunit level. Abstract-only experimental annotations are not rejected because a title foregrounds another subunit. PAINT asserts inheritance from a curated ancestral node; donor count and target self-inclusion are not objections. ARBA overlap is recorded only as provenance, never as biological validation. CNN and LSP reflect established biological knowledge, without asserting training-data membership.

Telomerase assembly is supported at ring level by [PMID:29422501]: "Co-immunoprecipitation assays confirmed an interaction between Lsm3 and Lar7 (Fig. 5b), indicating that they co-exist as a complex. Their association was sensitive to the presence of RNase and was abolished in lar7-W103A and lar7-FV197EE mutants. In addition, an interaction between wild-type Lar7 and Trt1 was detected, which was also dependent on RNA (Fig. 5c). These data suggested that Lar7, LSm2–8 and Trt1 independently bind to TER1 to form the telomerase ribonucleoprotein complex.". This directly assays Lsm3 within the Lsm2–8 ring; inference to shared Lsm6 is grounded in target ring reconstitution, not a claim that Lsm6 was the tagged bait.

## Provider report appraisal

The Falcon report and its structural evidence summary were inspected. It correctly distinguishes recombinant Lsm5/6/7 hexamers from physiological heteroheptamers, but its absence-of-complete-target-ring-evidence claim is incomplete: PMID:32518066 directly reconstitutes S. pombe Lsm1-7 and Lsm2-8. The primary full text was inspected.

Additional structural-source check: the [publisher article PDF mirrored by Georgia Tech](https://williams.chemistry.gatech.edu/course_Information/2024_3521_Spring/papers/Yan_2015_spliceosome.pdf) was inspected. Its main text describes heptameric Sm rings at U2 and U5. The accessible main text of PMID:26292707 describes Sm rings associated with U2 and U5, while fission yeast Lsm6 is experimentally established in Lsm RNA-binding rings. The exact protein identities and contacts underlying the PomBase U2/U5 assignment require resolution against the supplementary models and chain mappings. The broader spliceosome context is compatible with Lsm6 function, but it does not by itself settle this precise RNA or particle assignment. The experimental assignments remain UNDECIDED.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Identity: Q9UUI1 is the canonical, Swiss-Prot reviewed, full-length (75 aa) lsm6 product
(SPAC2F3.17c); not an isoform, fragment or alternative gene model. Single Sm domain
(IPR047575, PF01423), Lsm6/SmF entry IPR016487. PANTHER PTHR11021:SF1 (U6 snRNA-associated
Sm-like protein LSM6), the same subfamily as S. cerevisiae LSM6 (Q06406), human LSM6
(P62312) and mouse Lsm6 (P62313) (interpro/panther/PTHR11021/PTHR11021-entries.csv). The SmF
branch (smf1, SPBC3E7.14) is a separate subfamily of the same family. The family review
(interpro/panther/PTHR11021/PTHR11021-review.yaml) agrees on SF1 placement and already warns that
Lsm6 should not inherit U2/U5 membership from SmF; no disagreement.

Main change: the three PomBase annotations from PMID:26292707 (U2 snRNA binding IDA, U2 snRNP
EXP, U5 snRNP IDA), previously UNDECIDED, are now REMOVE with a PROBABLE source defect.
Evidence: lsm6-bioinformatics/check_3jb9_composition.py (new; RESULTS-rereview.md). The PDB 3JB9 model of
that paper contains 27 S. pombe proteins including smf1 and all seven Sm proteins, but no Lsm
protein. Lsm6 is not cross-referenced to 3JB9. smf1 carries no annotation citing the paper. So this
is a deposited-model argument, not a title-based one. The likely cause is a SmF to Lsm6 mix-up; it
is flagged for PomBase to check (requested_change CHECK, corrected_value smf1).

Other changes:
- GO:0005515 protein binding (Lsm5, Lsm7 IPI) KEEP_AS_NON_CORE -> REMOVE (protein-binding policy;
  ring packing is captured by the complex terms). The old reason wrongly mentioned "nuclease".
- RNA binding (IBA, IEA) ACCEPT -> MODIFY to poly(U) RNA binding (already IDA).
- Sm-like protein family complex (ARBA) ACCEPT -> MODIFY to Lsm2-8 complex / Lsm1-7-Pat1 complex.
- NEW contributes_to GO:0030629 U6 snRNA 3'-end binding (PMID:32518066 S. pombe Lsm2-8 structures with
  U6 3' cyclic-phosphate RNA). Used as the core MF for the Lsm2-8 function.
- Added a separate core function for the fission-yeast telomerase holoenzyme role (PMID:35277511,
  PMID:29422501).
- Nucleolus, snoRNP and SSU-rRNA maturation IBAs (PTN000111600, budding-yeast LSM6 donor) are kept
  as non-core. The node is the Lsm6 branch containing the target; there is no fission yeast data.
- PAINT did not propagate decapping or mRNA decay terms to the Lsm6 node. I treat that omission
  as deliberate: no NEW decapping process term, raised as a suggested question instead.

Relative to review next: S. cerevisiae LSM6 (Q06406, YDR378C, SGD:S000002786), which is in the same
PANTHER subfamily SF1 and is the donor for the Lsm6-node IBAs. No review exists in the repo
(no genes/yeast/LSM6). Human LSM6 (P62312) is also unreviewed.

Modules: none in modules/ model the Lsm2-8 or Lsm1-7 rings. modules/dmel_spliceosome.yaml
mentions the U6-associated LSm ring only in passing (Drosophila).
