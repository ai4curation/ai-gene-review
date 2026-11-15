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

## 2026-10-28: core function locations (PR #5679 review)

The core function listed only ER membrane, which is where the complex assembles. The rat-brain fractionation (PMID:20126630) puts gamma-secretase activity mainly with the early endosome marker syntaxin 13 and partly with the plasma membrane marker N-cadherin, so the core locations are now early endosome and plasma membrane, and the early endosome IDA row is ACCEPT.

The plasma membrane ISO row now also moves from KEEP_AS_NON_CORE to ACCEPT, so its reason agrees with the core function, which names plasma membrane as a location.

## ND re-check (2026-11-15)

- PubMed searched 2026-11-15 through E-utilities: (Aph1a OR "Aph-1a" OR "APH-1A" OR "Aph-1alpha") AND (rat OR rats OR Rattus), All Fields: 13 hits. The rat material is co-immunoprecipitation of APH-1 with nicastrin and presenilin from rat brain (PMID:12297508, whose siRNA experiments used human cell lines), Aph-1 binding Jagged-1 in rat embryo microsomes (PMID:20145246), detection of APH1a in rat sympathetic neurons (PMID:37031474), and synaptic fractionation (PMID:20126630); PMID:16249316 and PMID:16718279 concern Aph-1b, and the rest use human or other cells.
- No paper on rat Aph1a identifies a biological process of the protein; the gamma-secretase process rows rest on human and mouse work and are carried here by ISO/IEA. The BP ND row therefore follows the evidence-code guideline and is ACCEPT with nd_case INFERABLE (projects/NO_DATA.md), replacing the earlier REMOVE.
