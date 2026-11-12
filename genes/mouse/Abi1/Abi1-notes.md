# Research & Curation Notes: mouse Abi1 (UniProtKB:Q8CBW3)

## 1. Identity & Domain Architecture (`PTHR10460:SF2`)
- **Gene / Protein**: Mouse `Abi1` (Abl interactor 1; `MGI:104913`, synonyms `Ssh3bp1`, `e3B1`, `Ablphilin-1`), canonical sequence `Q8CBW3-1` (481 aa, `sequence_version: 3`), PANTHER subfamily `PANTHER:PTHR10460:SF2` (`ABL INTERACTOR 1`), 1:1 ortholog of human `ABI1` (`Q8IZP0`).
- **Conserved modules & residues on 481-aa `Q8CBW3-1`**:
  - N-terminal WAVE-binding (`WAB`, residues 18–79) and t-SNARE coiled-coil homology / HHR region (residues 45–107), including conserved `Tyr53` (`MOD_RES 53`) and `Ser88`.
  - Central proline-rich / PxxDY & Abl-regulatory region containing `Tyr213` (`MOD_RES 213`, `PMID:19131326`) and `Ser216` (`MOD_RES 216`).
  - C-terminal SH3 domain (residues 419–478; conserved tyrosine `Tyr428`, `MOD_RES 428`).

## 2. Direct Experimental Biology in *Mus musculus*
- **Essential subunit for WAVE regulatory complex integrity & embryogenesis (`PMID:21482783`, `PMID:15143189`, `PMID:12672821`, `PMID:26428302`)**:
  - Conditional/constitutive `Abi1` knockout mice die around E11.5 with severe cardiovascular and brain/neural tube defects (`PMID:21482783`; ENU forward-genetics allele `MGI:3578145` also exhibits early morphogenetic/somitogenesis defects, `PMID:15755804`).
  - `Abi1`-null MEFs show marked depletion of WAVE1, WAVE2, Nap1 (`Nckap1`), and Sra-1/PIR121 (`Cyfip1`/`Cyfip2`), impaired dorsal ruffling, and altered migration (`PMID:21482783`), and `Abi1+/-; Abi2-/-` MEFs require the N-terminal WAB domain of Abi1 to maintain WAVE1 protein levels and lamellipodial tip recruitment (`PMID:15143189`).
- **Signaling adaptor for c-Abl, EPS8–SOS1, and barbed-end capping (`PMID:10499589`, `PMID:11003655`, `PMID:12672821`, `PMID:15558031`, `PMID:19564905`)**:
  - Identified as an Abl-interactor that suppresses v-Abl transformation (`PMID:7590237`, `PMID:11003655`) and directly promotes c-Abl-mediated phosphorylation of mammalian Enabled (`Enah`/`Mena`) at Tyr296 (`PMID:12672821`).
  - Forms the EPS8–ABI1–SOS1 Rac-GEF complex (`PMID:10499589`) and relieves EPS8 autoinhibition to regulate actin barbed-end capping and BDNF-responsive axonal filopodia remodeling (`PMID:15558031`, `PMID:19564905`).
- **Specialized cellular & tissue contexts**:
  - **Megakaryocyte maturation & lamellipodial spreading (`PMID:17664349`)**: `Abi1` siRNA knockdown in mouse ES-derived megakaryocytes phenocopies `Wasf2-/-`, impairing peripheral lamellipodia formation on fibrinogen and terminal megakaryocyte/proplatelet maturation (`KEEP_AS_NON_CORE` on `GO:0035855` `megakaryocyte development`, `ACCEPT` on `GO:0072673` `lamellipodium morphogenesis`).
  - **Neuronal dendrite & spine dynamics (`PMID:10995551`, `PMID:17304222`, `PMID:25297099`, `PMID:19208628`)**: Localizes to growth cones, dendritic spines, and postsynaptic densities (`PMID:10995551`, `PMID:17304222`; note `PMID:21795692` carries a broad `GO:0043005` `IDA` row in GOA while mentioning anti-Abi1 only in its antibody list, refined via `MODIFY` to `GO:0030426`/`GO:0043197`), and interacts with IRSp53 (`Baiap2`, `PMID:19208628`) and CaMKIIα (`Camk2a`, `PMID:25297099`) to regulate dendritic protrusion stability and morphogenesis (`KEEP_AS_NON_CORE` as neuronal specialization of core actin/adaptor function).
  - **Hematopoietic stem cell homeostasis (`PMID:30213875`)**: Bone-marrow `Abi1` loss derepresses SFK, STAT3, and NF-κB signaling, causing myeloproliferative neoplasm / myelofibrosis-like disease in mice.

## 3. GOA Annotation Audit Notes
- All bare `GO:0005515` (`protein binding`) IPI rows are resolved per policy:
  - `Sos2` (`Q02384`, `PMID:11003655`) → `MODIFY` to `GO:0005070` / `GO:0035591` (`signaling adaptor activity`) or `GO:0017124` (`SH3 domain binding`; Fan & Goff 2000 show Abi1 SH3 binds Sos1/Sos2 proline-rich region, `GO:0035591` / `GO:0017124` — specifically `ABI1`'s SH3 binds Sos proline-rich motif, so `ABI1` is the SH3 domain protein and Sos is the proline-rich partner; `GO:0035591` `signaling adaptor activity` is exact!).
  - `Eps8` (`Q08509`, `PMID:9010225`, `PMID:15558031`, `PMID:19564905`) and `Baiap2`/IRSp53 (`Q8BKX1`, `PMID:19208628`) → `MODIFY` to `GO:0017124` (`SH3 domain binding`) / `GO:0035591` (`signaling adaptor activity`) (ABI1 polyproline/PxxDY binds the SH3 domain of EPS8 and IRSp53!).
  - `Camk2a` (`P11798`, `PMID:25297099`) → `MODIFY` to `GO:0019901` (`protein kinase binding`).
  - `Wasf2` (`Q8BH43`, `PMID:18044991`, `PMID:20697350`) and `Diaph3`/mDia2 (`Q9Z207`, `PMID:18044991`) → `REMOVE` on bare `GO:0005515` (WRC subunit association with WAVE2 is captured by `GO:0031209` `SCAR complex`, and co-precipitation in proteomic/motility complexes carries no standalone MF beyond adaptor/WRC subunit).
- **`GO:0061098` (`positive regulation of protein tyrosine kinase activity`, `ISO`, `PMID:17101133`)**: `ACCEPT` (`NO_FAILURE_CORE`) as the core Biological Process counterpart of `GO:0030296` (`protein tyrosine kinase activator activity`, `IDA`, `PMID:12672821`, `ACCEPT`), harmonized with human `ABI1` and `PTHR10460`.
- **`GO:0005856` (`cytoskeleton`, `IEA`, `GO_REF:0000044`)**: `ACCEPT` as-is because Abi1 is a cytosolic signaling adaptor and WRC subunit dynamically recruited across cytoskeletal remodeling sites rather than an intrinsic structural filament subunit, with leading-edge/lamellipodial compartments captured by `GO:0030027` and `GO:0031252`.
