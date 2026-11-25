# DNAH3 notes

## Identity and structure
- UniProt Q8TD57, 4116 aa; full heavy-chain architecture [file:human/DNAH3/DNAH3-uniprot.txt].
- IDAc heavy chain in human respiratory axonemes [PMID:37258679 "IDAa is DNAH12, IDAc is DNAH3, and IDAb and IDAe are both DNAH7"].

## Localization / expression
- Testis and trachea [PMID:9256245]; in testis, "Initially, DNAH3 was expressed in the cytoplasm of spermatogonia and spermatocytes, and then it clearly transferred into the flagellum of early and late spermatids." [PMID:39503742].

## Interactions
- "Combined comparative proteomics and co-immunoprecipitation analyses demonstrated that DNAH3 forms a complex with DNALI1." and the stem domain mediates it [PMID:41731497].

## Loss of function
- Patients + KO: "the absence of DNAH3 led to decreased expression of other IDA-associated proteins, including DNAH1, DNAH6 and DNALI1" [PMID:39503742].
- KO: absence of IDAs; DNAH6, DNAH10, DNALI1 reduced [PMID:41731497].
- Patients: CP loss, MS/FS dislocation, partial IDA absence; two KO lines with AT; airway and brain cilia grossly normal in KO [PMID:38312775 "the gross ciliary morphology of trachea and brain appear normal in Dnah3-KO mice"].
- OAT/MMAF patients [PMID:39588341].
- Conflicting: KO sperm with normal morphology, energy-metabolism defect [PMID:39774634 "spermatozoa from Dnah3-knockout mice displayed normal morphology"].

## Curation decisions
- Core MF: minus-end-directed MT motor activity; dynein light intermediate chain binding (direct DNALI1 co-IP) ACCEPTED.
- Dynein intermediate chain binding UNDECIDED (IBD seeded only by Dictyostelium cytoplasmic dynein).
- NAS (PMID:9256245) axonemal dynein complex -> inner dynein arm; cilium-dependent cell motility -> flagellated sperm motility.

## PANTHER / IBA check
- Human Q8TD57 and mouse Q8BW94 have identical IBA sets (8 terms) in QuickGO; no family split. DNAH3 seeds the PTN008951089 IBDs (IDA assembly, sperm flagellum assembly).

## Deep research
- Falcon deep research failed (Edison API authentication 503 errors on repeated attempts).
