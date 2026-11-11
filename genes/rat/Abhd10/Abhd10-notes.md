# Curatorial Notes for Rat Abhd10 (UniProtKB:Q5I0K5)

## Summary of Gene Product & Architecture

- **Protein**: Palmitoyl-protein thioesterase ABHD10, mitochondrial (`UniProtKB:Q5I0K5`, sequence version 2; 297 aa precursor; `RGD:1308084`, chromosome 11).
- **Mitochondrial Matrix Targeting & Active Site**:
  - Carries a conserved 43-residue N-terminal mitochondrial transit peptide (`FT TRANSIT 1..43`) cleaved to the 254-aa soluble mature chain `44..297` (`PRO_0000280736`).
  - Shares >92% sequence identity with mouse `Q6PE15` (`PDB:6NY9`) and ~78% mature-domain identity with human `Q9NUJ1`, strictly conserving the alpha/beta-hydrolase charge-relay catalytic triad at **Ser143** (`GSSLG` nucleophilic elbow), **Asp240**, and **His270** (`PMID:22294686`, `PMID:31740833`).
- **Rat Experimental Proteomics (`PMID:20966424`)**:
  - Suryawanshi et al. (`PMID:20966424`, abstract-only in cache) compared rat testicular vs cauda epididymal sperm domain proteomes (head and flagellum) by 2D-DIGE/MS and detected rat ABHD10 in epididymal sperm, consistent with mammalian ABHD10 enrichment in sperm midpiece mitochondrial sheaths demonstrated genetically and ultrastructurally in mouse (`PMID:41285782`).

## Key Curation Decisions

- **`GO:0008474` (`palmitoyl-(protein) hydrolase activity`)**: `ACCEPT` across `IBA` (`PTN001043685`), `ISO` (`MGI:2442422` and `Q9NUJ1`), `ISS` (`Q9NUJ1`), and `IEA` (`EC:3.1.2.22` / `RHEA:19233` / `ARBA:ARBA00085285`).
- **`GO:0002084` (`obsolete protein depalmitoylation`, `ISS` from `Q9NUJ1`)**: `MODIFY` -> `GO:0008474` (`palmitoyl-(protein) hydrolase activity`).
- **`GO:0004553` (`hydrolase activity, hydrolyzing O-glycosyl compounds`, `IBA` and `ISO` from `Q9NUJ1`)**: `REMOVE` (`SOURCE_BAD` / `SOURCE_MISCITATION`: human `Q9NUJ1` cleaves carboxylic ester linkages of acyl-glucuronides and cannot cleave the phenolic O-glycoside MPAG in `PMID:22294686`).
- **`GO:0005829` (`cytosol`, `ISO` from `Q9NUJ1`)**: `REMOVE` (`SOURCE_BAD` / `COMPARTMENT_OR_COMPLEX_MISMATCH`: transferred from post-mortem frozen human liver homogenate supernatant in `PMID:22294686` and refuted in mammalian mitochondria-depleted cytoplasm fractionation in `PMID:41285782`).
- **`GO:0005739` (`mitochondrion`, `IBA`, `IEA`, `ISO`, `ISS`)**: `ACCEPT` per the Root Organelle Policy, paired with **`NEW` `GO:0005759` (`mitochondrial matrix`, `IC`, `PMID:31740833`)** supported by two independent lines of evidence: (1) rat `Q5I0K5` possesses a cleavable N-terminal mitochondrial presequence (`FT TRANSIT 1..43`) and soluble alpha/beta-hydrolase mature chain lacking transmembrane segments, and (2) its conserved S-depalmitoylase activity (`GO:0008474`) acts inside the mitochondrial matrix as established for 92%-identical mouse `Q6PE15` (`PMID:31740833`, `PMID:41285782`).
- **`GO:0102390` (`mycophenolic acid acyl-glucuronide esterase activity`) & `GO:0006805` (`xenobiotic metabolic process`)**: `KEEP_AS_NON_CORE` on mammalian ortholog transfer rows (`ISO`, `ISS`, `IEA` from human `Q9NUJ1`), noting this hepatic drug-conjugate esterase activity is secondary to conserved mitochondrial protein S-depalmitoylation and has not been directly assayed in rat.
