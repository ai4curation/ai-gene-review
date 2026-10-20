# Gene Review Notes: Salmonella phage P22 `12` (`P03006`, Replicative DNA helicase gp12)

## Overview
- **Gene symbol**: `12`
- **UniProt ID**: `P03006` (`VG12_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Protein length**: 458 amino acids (50.5 kDa), EC 5.6.2.3
- **Operon / genomic context**: Located in the early right ($P_R$) replication operon immediately downstream of gene `18` (`c1`-`18`-`12`), occupying the syntenic position of lambda gene `P` ([PMID:6241581](https://pubmed.ncbi.nlm.nih.gov/6241581/), [PMID:11053393](https://pubmed.ncbi.nlm.nih.gov/11053393/)).

## Function and Structural Architecture
- **DnaB-family replicative 5'-3' DNA helicase**:
  - Unlike coliphage lambda gpP (which is an adaptor/loader that hijacks the host *E. coli* DnaB helicase), Salmonella phage P22 gp12 is itself a full-length superfamily 4 (DnaB-like) hexameric replicative DNA helicase closely related to bacterial DnaB ([PMID:6241581](https://pubmed.ncbi.nlm.nih.gov/6241581/, "Gene 12 is nonhomologous to its lambda counterpart (gene P), but closely related to dnaB of Escherichia coli.")).
  - Consequently, gp12 renders P22 viral DNA replication independent of host `dnaB` function (`file:genes/BPP22/12/12-uniprot.txt`, `"CC   -!- FUNCTION: Renders P22 DNA replication independent of a functional dnaB gene of the host. {ECO:0000305}."`).
  - Domain architecture in `12-uniprot.txt`:
    - `InterPro:IPR007693` / `Pfam:PF00772` (`DnaB` / `DNA_helicase_DnaB-like_N`), `InterPro:IPR036185` (`DNA_heli_DnaB-like_N_sf`), `InterPro:IPR016136` (`DNA_helicase_N/primase_C`)
    - `InterPro:IPR007694` / `Pfam:PF03796` / `CDD:cd00984` (`DnaB_C` / `DNA_helicase_DnaB-like_C`), `InterPro:IPR027417` (`P-loop_NTPase`), `PROSITE:PS51199` (`SF4_HELICASE`)
    - `PANTHER:PTHR30153` (`REPLICATIVE DNA HELICASE DNAB`) / `PANTHER:PTHR30153:SF2` (`REPLICATIVE DNA HELICASE`).
  - Catalytic activity: Couples ATP hydrolysis (`GO:0016887`) with unwinding of duplex DNA at the replication fork by translocating in the 5'-3' direction (`GO:0043139` `5'-3' DNA helicase activity`).

## Review of Existing GO Annotations
- **Accepted core annotations**:
  - `GO:0043139` (`5'-3' DNA helicase activity`, `IEA` `GO_REF:0000003` and `ISS` `GO_REF:0000024`): `ACCEPT`. Core enzymatic activity of the DnaB-family hexameric replicative helicase.
  - `GO:0016887` (`ATP hydrolysis activity`, `IEA` `GO_REF:0000116` and `ISS` `GO_REF:0000024`): `ACCEPT`. ATP hydrolysis drives 5'-3' translocation and duplex unwinding.
  - `GO:0005524` (`ATP binding`, `IEA` `GO_REF:0000120`): `ACCEPT`. Required for P-loop NTPase catalytic cycle (`InterPro:IPR027417`, `PROSITE:PS51199`).
  - `GO:0003677` (`DNA binding`, `IEA` `GO_REF:0000043`): `ACCEPT`. Directly binds DNA at the replication fork during unwinding.
- **Modified annotation**:
  - `GO:0006260` (`DNA replication`, `IEA` `GO_REF:0000120`): `MODIFY` -> `GO:0039693` (`viral DNA genome replication`). gp12 specifically catalyzes unwinding of the bacteriophage P22 genome during lytic viral DNA replication, matching the process annotation of its partner initiator gp18 (`P03687`).
- **Too-general annotations (`TOO_GENERAL`)**:
  - `GO:0000166` (`nucleotide binding`, `IEA` `GO_REF:0000043`): Entailed by accepted `GO:0005524` (`ATP binding`).
  - `GO:0003678` (`DNA helicase activity`, `IEA` `GO_REF:0000002`): Entailed by accepted `GO:0043139` (`5'-3' DNA helicase activity`).
  - `GO:0004386` (`helicase activity`, `IEA` `GO_REF:0000043`): Entailed by accepted `GO:0043139` (`5'-3' DNA helicase activity`).
  - `GO:0016787` (`hydrolase activity`, `IEA` `GO_REF:0000043`): Entailed by accepted `GO:0016887` (`ATP hydrolysis activity`).
  - `GO:0003824` (`catalytic activity`, `IEA` `GO_REF:0000117`): Entailed by accepted `GO:0043139` (`5'-3' DNA helicase activity`) and `GO:0016887` (`ATP hydrolysis activity`).
- **Removed annotation (`REMOVE`)**:
  - `GO:0016853` (`isomerase activity`, `IEA` `GO_REF:0000043`): Artifact of automated UniProt keyword (`KW-0413` Isomerase) mapping derived from the IUBMB reclassification of helicases under EC class 5.6.2.3. In the Gene Ontology, DNA helicases (`GO:0043139`) are classified under catalytic activity / ATP-dependent activity acting on DNA, not under `GO:0016853` (`isomerase activity`).
- **Proposed `NEW` annotation**:
  - `GO:0030430` (`host cell cytoplasm`, `located_in`): gp12 acts in the cytoplasm of the infected *Salmonella* host cell where phage P22 DNA replication occurs.
