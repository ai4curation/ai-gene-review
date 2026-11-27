# Gene Review Notes: Enterobacteria phage phiX174 gene B (P03633)

## Overview
- **Gene symbol**: `B`
- **UniProt ID**: `P03633` (`SCAFB_BPPHS`)
- **Organism**: Enterobacteria phage phiX174 isolate Sanger (`NCBITaxon:1217068`)
- **Product**: Internal scaffolding protein B (gpB, 120 aa, 13.8 kDa)
- **Phage lifecycle module**: `phage_capsid_assembly.yaml` (Dual-scaffolded T=1 procapsid morphogenesis)

## Biological Function & Mechanism
1. **Early 12S Pre-assembly Complex & 108S Procapsid Formation**:
   - In the host cytoplasm, five copies of internal scaffolding protein B bind to the underside of an F coat pentamer (`9S`) together with a G spike pentamer (`6S`) and one copy of pilot protein H to form the `12S` pre-assembly intermediate (`file:BPPHS/B/B-uniprot.txt`, `PMID:9305849`).
   - Preventing premature aggregation of coat and spike pentamers, gpB induces conformational changes in gpF that enable external scaffolding protein D (240 copies) to join twelve `12S` complexes into the `108S` empty procapsid (`PMID:9305849`, `PMID:12473449`).
   - Within the 108S procapsid, 60 copies of gpB occupy binding clefts on the inner surface of the F capsid shell (`PMID:9305849`).
2. **Displacement & Extrusion During Genome Packaging**:
   - During stage III ssDNA packaging, highly basic DNA-binding protein J (gpJ) enters with the viral genome and competes for the same interior binding clefts on gpF, displacing gpB (`PMID:9305849`, `file:BPPHS/B/B-uniprot.txt`).
   - Structural studies in microviruses (`PMID:12473449`) indicate that gpB undergoes slow autoproteolytic cleavage at conserved Arg-Phe motifs (residues 77-78, 93-94, 108-109), facilitating extrusion of the internal scaffold fragments through the 30-Angstrom pores at the 3-fold axes of the procapsid.

## GO Annotation Review Summary
- **Accepted core terms**:
  - `GO:0046806` (`viral scaffold`, IDA from `PMID:9305849`)
  - `GO:0046807` (`viral scaffold assembly and maintenance`, IDA from `PMID:12473449`)
  - `GO:0019069` (`viral capsid assembly`, IEA)
  - `GO:0030430` (`host cell cytoplasm`, IEA)
- **Non-core terms (`KEEP_AS_NON_CORE`)**:
  - `GO:0006508` (`proteolysis`) and `GO:0008233` (`peptidase activity`): reflect the reported self-cleavage at Arg-Phe motifs (`PMID:12473449`) that assists scaffold exit through the procapsid pores; secondary to its primary structural scaffolding role.
- **Broad ancestor (`TOO_GENERAL`)**:
  - `GO:0016787` (`hydrolase activity`): broader than `GO:0008233` (`peptidase activity`).
