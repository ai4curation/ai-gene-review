# Light-Source Open Datasets (Literature-First Seeds)

## Method
Goal: start from papers that **explicitly link to open datasets**, then follow the repository landing pages to collect facility + beamline details. Focus here is on **open/public datasets** with stable identifiers (DOIs or repository IDs).

## Seed repositories (strong paper ↔ dataset linkage)
- **CXIDB (Coherent X-ray Imaging Data Bank)**: open datasets with explicit paper metadata, facility/beamline, and CC0 licensing on entries.
- **SBGrid Data Bank**: open diffraction datasets with DOIs and beamline metadata; CC0 is the default license for datasets.
- **IRRMC**: CC0 raw diffraction datasets; supports beamline-based search and per-dataset DOIs.

## Curated examples (paper → dataset → facility/beamline)

| Dataset | Paper (title / DOI) | Facility / Beamline | Access notes |
|---|---|---|---|
| CXIDB ID 1 (DOI: 10.11577/1096903) | *Single mimivirus particles intercepted and imaged with an X-ray laser* (Nature 2011, DOI: 10.1038/nature09748) | LCLS / AMO | CC0; single-particle CDI |
| CXIDB ID 37 (DOI: 10.11577/1245696) | *Open data set of live cyanobacterial cells imaged using an X-ray laser* (Sci Data 2016, DOI: 10.1038/sdata.2016.58) | LCLS / AMO | CC0; very large raw diffraction sets | 
| CXIDB ID 22 (DOI: 10.11577/1169542) | *De novo protein crystal structure determination from X-ray free-electron laser data* (Nature 2013, DOI: 10.1038/nature12773) | LCLS / CXI | CC0; SFX raw data and metadata | 
| CXIDB ID 189 (DOI: 10.11577/1839200) | *Chemical Crystallography by Serial Femtosecond X-ray Diffraction* (Nature 2022, DOI: 10.1038/s41586-021-04218-3) | LCLS / CXI; SACLA / BL3 | CC0; multi-facility dataset with raw data directories | 
| CXIDB ID 92 (DOI: 10.11577/1491355) | *Coherent Diffractive Imaging of Microtubules using an X-ray Laser* (Nat Commun 2019, DOI: 10.1038/s41467-019-10448-x) | LCLS / CXI | CC0; serial fiber diffraction | 
| SBGrid DB 1118 (DOI: 10.15785/SBGRID/1118) | Dataset citation only (HEWL) | APS / 14-ID (BioCARS) | CC0; raw diffraction images | 
| IRRMC nsls2_fmx_20161122_lys_266 (DOI: 10.18430/M33590) | Dataset entry (Lysozyme calibration data) | NSLS-II / 17-ID-2 (FMX) | CC0; raw diffraction images | 

## URLs / landing pages
- CXIDB ID 37: https://www.cxidb.org/id-37.html
- CXIDB ID 22: https://www.cxidb.org/id-22.html
- CXIDB ID 189: https://www.cxidb.org/id-189.html
- CXIDB ID 92: https://www.cxidb.org/id-92.html
- CXIDB ID 1: https://www.cxidb.org/id-1.html
- SBGrid Data Bank: https://data.sbgrid.org/
- SBGrid dataset 1118: https://data.sbgrid.org/dataset/1118/
- IRRMC portal: https://proteindiffraction.org/
- IRRMC NSLS-II dataset: https://proteindiffraction.org/project/nsls2_fmx_20161122_lys_266/

## Next expansion steps
- Mine CXIDB for additional LCLS/SACLA/EuXFEL datasets linked to specific papers.
- Expand SBGrid and IRRMC entries to include **paper DOIs** (when available on dataset pages).
- Add ESRF/ALBA/DIAMOND DOI-linked datasets once individual paper DOIs are identified.
