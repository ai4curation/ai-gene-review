# Gene Review Notes: Enterobacteria phage phiX174 gene F (P03641)

## Overview
- **Gene symbol**: `F`
- **UniProt ID**: `P03641` (`CAPSD_BPPHS`)
- **Organism**: Enterobacteria phage phiX174 isolate Sanger (`NCBITaxon:1217068`)
- **Product**: Major capsid protein F (gpF, 427 aa, 48.4 kDa; initiator Met removed)
- **Phage lifecycle module**: `phage_capsid_assembly.yaml` (T=1 icosahedral viral capsid coat) and `phage_adsorption_entry.yaml` (LPS interaction and 5-fold vertex channel opening during genome ejection)

## Biological Function & Mechanism
1. **T=1 Icosahedral Capsid Shell & Morphogenesis**:
   - Sixty copies of major coat protein F form the ~30-nm T=1 icosahedral shell of the phiX174 virion (`PMID:1370343`, `PMID:8158636`, `file:BPPHS/F/F-uniprot.txt`).
   - Each gpF subunit folds into the canonical eight-stranded antiparallel beta-barrel ("jelly-roll" motif) with two large insertion loops that make up over 60% of the polypeptide chain (`PMID:1370343`, `PMID:8158636`).
   - During assembly in the host cytoplasm, five gpF monomers form a `9S` pentamer, which associates with internal scaffolding protein B, a `6S` spike pentamer of protein G, and pilot protein H to form the `12S` pre-assembly complex (`file:BPPHS/F/F-uniprot.txt`, `PMID:9305849`).
   - Twelve `12S` complexes are joined by 240 copies of external scaffolding protein D into the `108S` procapsid (`PMID:9305849`). Upon ssDNA and protein J packaging (`132S` provirion) and subsequent gpD release, the 60 gpF subunits undergo an 8.5-Angstrom radial collapse around the packaged genome (`PMID:11991963`).
2. **Host Cell Entry & Genome Ejection Channel**:
   - Upon host attachment, one of the twelve G spike pentamers dissociates from a unique 5-fold vertex, exposing the EF loops of the underlying F pentamer to bind bacterial lipopolysaccharide (LPS) (`file:BPPHS/F/F-uniprot.txt`).
   - The F pentamer at this unique 5-fold vertex forms an open channel through which pilot protein H and the viral ssDNA genome are ejected (`file:BPPHS/F/F-uniprot.txt`).

## GO Annotation Review Summary
- **Modified term (`MODIFY`)**:
  - `GO:0005198` (`structural molecule activity`, IEA) -> `MODIFY` to `GO:0039660` (`structural constituent of virion`), the specific child term for virion capsid structural proteins.
- **Accepted core terms (`ACCEPT`)**:
  - `GO:0039615` (`T=1 icosahedral viral capsid`, 3 IDA rows from `PMID:11991963`, `PMID:1370343`, `PMID:8158636`, and 1 IEA row): all four rows accepted consistently.
- **Broad ancestor (`TOO_GENERAL`)**:
  - `GO:0019028` (`viral capsid`, IEA): direct parent of `GO:0039615` (`T=1 icosahedral viral capsid`).
- **Non-core term (`KEEP_AS_NON_CORE`)**:
  - `GO:0046718` (`symbiont entry into host cell`, IEA): reflects the secondary role of the exposed EF loops and 5-fold vertex channel of gpF during LPS interaction and genome ejection (`file:BPPHS/F/F-uniprot.txt`).
