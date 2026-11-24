# Curation Notes for Mouse Arfrp1 (UniProtKB:Q8BXL7, MGI:1923938)

## 1. Gene Identity & Sequence Conservation
- **Symbol / Accession**: `Arfrp1` (`UniProtKB:Q8BXL7`, `MGI:1923938`), 201 aa, 97.5% identical to human `ARFRP1` (`Q13795`), sharing identical N-terminal NatC/SYS1-binding amphipathic helix `1-MYTLLSGLYKYMFQ-14` (`Tyr2`), P-loop `24-GLDNAGKT-31` (`Lys30`, `Thr31`), Switch II `75-DLGGQ-79` (`Gln79`), and G4 `134-NKQD-137` in `PANTHER:PTHR45909:SF1` (`PTN000196303`).

## 2. Direct Experimental Evidence in Mouse (`Mus musculus`)
- **Early Embryonic Lethality & Epiblast E-Cadherin Mistrafficking (`PMID:11839814`, `PMID:17127620`, `PMID:18662990`)**:
  - Germline `Arfrp1-/-` embryos implant normally through E5.0 but undergo epiblast apoptosis and detachment during gastrulation between E6.0 and E7.0 [PMID:11839814, "Our results demonstrate that ARFRP1 is necessary for early embryonic development during gastrulation."].
  - Subsequent mechanistic analysis in `Arfrp1-/-` embryos and `Arfrp1(vil-/-)` enterocytes showed that `ARL1` dislocates from Golgi membranes [PMID:17127620] and E-cadherin is retained in intracellular compartments rather than reaching the lateral/cell-surface plasma membrane, explaining epiblast cell detachment during gastrulation [PMID:18662990]. Therefore, `GO:0007369` (`gastrulation`, `IMP` `PMID:11839814`, `acts_upstream_of_or_within`) is retained as `KEEP_AS_NON_CORE` (a pleiotropic developmental phenotype downstream of core TGN protein sorting).
- **Tissue-Specific Conditional Knockouts Confirm Core TGN Cargo-Sorting Roles**:
  - **Adipocytes (`Arfrp1(ad-/-)`, `PMID:20038528`, `PMID:20230794`)**: Abnormal trans-Golgi ultrastructure, mislocalization of `GLUT4` to the basal plasma membrane (`PMID:20230794`), cytosolic displacement of `SNAP23`, defective lipid-droplet enlargement, and elevated lipolysis (`PMID:20038528`).
  - **Intestinal Epithelium (`Arfrp1(vil-/-)`, `PMID:18662990`, `PMID:22505585`)**: Intracellular retention of E-cadherin, cytosolic dislocation of `ARL1`, impaired Golgi lipidation of chylomicrons, and defective `ApoA-I` secretion via the `ARFRP1`-`ARL1`-Golgin-245-`Rab2` cascade.
  - **Hepatocytes (`Arfrp1(liv-/-)`, `PMID:22927645`, `PMID:24186947`)**: Intracellular retention of `GLUT2`, reduced `IGF1` secretion and hepatic glycogen storage (`PMID:22927645`), and impaired Golgi VLDL lipidation and `ApoC3` secretion (`PMID:24186947`).
  - **Pancreatic Beta Cells (`PMID:33359402`)**: Impaired TGN-to-plasma-membrane delivery of `SNAP25` via `GOPC` and reduced glucose-stimulated insulin secretion.
  - **Planar Cell Polarity Cargo Sorting (`PMID:23326640`, `PMID:29666182`, `PMID:32972971`)**: Direct interaction of GTP-bound mouse Arfrp1 with clathrin adaptor `AP-1` mediates TGN export of `Vangl2`, and `Y2A` on Arfrp1 abolishes Sys1 co-immunoprecipitation and Golgi targeting independently of GTP binding (`PMID:32972971`).

## 3. Key Annotation Decisions
- **`GO:0003924`, `GO:0005525`, `GO:0005794`, `GO:0005802`, `GO:0006886`, `GO:0034067`, `GO:0042147`, `GO:0043001`**: `ACCEPT` as core molecular functions, Golgi/TGN compartments, and trafficking processes.
- **`GO:0005829` (`cytosol`, `IEA`)** and **`GO:0007369` (`gastrulation`, `IMP` `PMID:11839814`)**: `KEEP_AS_NON_CORE`.
- **`GO:0016020` (`membrane`, `IDA` `PMID:11839814` and `IEA` `GO_REF:0000117`)**: `MODIFY` to `GO:0032588` (`trans-Golgi network membrane`).
