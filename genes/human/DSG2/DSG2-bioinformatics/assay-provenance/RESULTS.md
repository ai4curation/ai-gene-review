# Assay provenance results

The deposited reference identities for the human DSG2–DSC2 pair reproduce both IntAct ROGIDs: Q14126 is 1118 residues and Q02487 is 901 residues. Record [EBI-6901957](https://www.ebi.ac.uk/intact/interaction/EBI-6901957), also IM-20978-13, reports anti-tag co-immunoprecipitation (MI:0007), physical association (MI:0915), no expansion, and a COS-1 host. Its GFP tag and DSC2 binding-region feature are retained. These checks authenticate the database reference sequences, not a sequenced experimental insert or purified direct contact. [PMID:21220045](https://pubmed.ncbi.nlm.nih.gov/21220045/)

The 2022 network's Supplementary Table 3, row 151 lists a DSG2–DSC2 affinity of 29000 nM and points to the 2016 primary source. It is a literature-imported measurement, not an independent 2022 replication. [PMID:35922511](https://pubmed.ncbi.nlm.nih.gov/35922511/), [primary measurement](https://pubmed.ncbi.nlm.nih.gov/27298358/)

The human parotid-exosome workbook's sheet `Paratid Exosomes`, row 76 lists IPI00028931.2/DSG2 with two sequences, two spectra and sequence coverage 0.044. The extracted fields preserve those measurements and exclude the adjacent biological-function/location descriptions. This supports target-specific detection but does not establish peptide positions, intact-product topology, a purified vesicle-biogenesis function, or orthogonal DSG2 validation. [PMID:19199708](https://pubmed.ncbi.nlm.nih.gov/19199708/), [original workbook](https://ndownloader.figshare.com/files/4571341)

The same generic extraction finds the independent DSP record in row 176 (16 sequences, 16 spectra, coverage 0.083). A nonexistent-target query returns no record. These controls concern table selection, not experimental antibody or proteomic specificity.

- [x] Inputs and query parameters are explicit; measurements are calculated from records rather than embedded as expected outputs.
- [x] Input hashes and both sequence-derived ROGIDs were checked.
- [x] An independent gene query and a no-hit query were run successfully.
- [x] Calculated outputs are saved as `results.json`, `control-DSP.json` and `control-negative.json`.
- [x] The extraction completed with the pinned packages. An initial offline attempt lacked a cached dependency; the subsequent package acquisition and rerun succeeded.
A fresh download of every public endpoint was not repeated for this reproduction. Genuine previously acquired files were used; `fetch_inputs.py` implements hash-checked reacquisition and fails if an endpoint changes or denies access.

These limitations do not invalidate the saved-input extraction; they delimit future reproducibility and biological interpretation. The scripts do not perform new affinity measurements or peptide identification.
