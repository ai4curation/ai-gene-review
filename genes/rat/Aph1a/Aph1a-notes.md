# Aph1a (rat) review notes

- Fetched A0ABK0KYA7 (matches requested accession; RGD:1311546, GeneID 365872). 33 GOA rows
  in the stub (34 GOA lines; two SynGO presynaptic-membrane IDA lines differ only in ECO).
- No deep research available; manual summary in Aph1a-deep-research-manual.md.
- Key experimental rat data: PMID:20126630 (rat brain fractionation; Aph-1aL in synaptic
  membrane, synaptic vesicle, endosome-enriched fractions) and PMID:20145246 (endogenous
  rat Aph-1 binds Jagged-1 in E13 embryo microsomes [PMID:20145246 "we were able to observe
  an interaction between endogenous Jagged-1 and endogenous Aph-1"]).
- Core function modelled as in human APH1A review: protein-macromolecule adaptor
  (assembly scaffold) plus contributes_to aspartic endopeptidase activity, intramembrane
  cleaving (presenilin is the catalytic subunit).
- GO:0006509 ectodomain proteolysis is propagated from a human HGNC-UCL IDA
  (PMID:15274632); gamma-secretase performs intramembrane cleavage after shedding, so
  MODIFY to GO:0031293 and record a source defect.
- SynGO IEP row for presynaptic membrane: location from fractionation/imaging, not an
  expression pattern; recorded WRONG_EVIDENCE_CODE (CHECK), as in the rat Gria2 precedent.
- GO:0007220 Notch receptor processing is is_a protein metabolic process only (not under
  GO:0007219 or GO:0016485 in the current GO build), checked with OAK.
- Substrate binding (APP/Jagged) has no informative MF term short of protein binding;
  not proposed as NEW.
