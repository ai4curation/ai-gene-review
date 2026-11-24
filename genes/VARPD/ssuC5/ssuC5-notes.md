# Curation Notes for `ssuC5` (`VPARA_09240`, `A0A0H2M6G6`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Overview
- **UniProtKB Accession:** `A0A0H2M6G6` (`A0A0H2M6G6_VARPD`, unreviewed, 284 aa, 29,638 Da)
- **Gene Symbol / Locus Tag:** `ssuC5` / `VPARA_09240` (`EMBL:KLN57913.1` on genomic contig `JZWI01000005`, `RefSeq:WP_021006428.1`)
- **Organism:** *Variovorax paradoxus* strain TBEA6 (`NCBITaxon:34073`)
- **Genomic Context:** Encoded on contig `JZWI01000005` immediately downstream of `ssuB2` (`VPARA_09230`, `KLN57912.1`) and immediately upstream of `ssuD` (`VPARA_09250`, `KLN57914.1`), with `ssuA2` (`VPARA_09270`, `KLN57916.1`) and `ssuE` (`VPARA_09290`, `KLN57918.1`) in the same cluster.
- **Domain Architecture & Topology:**
  - Five Phobius-predicted transmembrane alpha-helices at residues `34..56`, `91..114`, `126..144`, `150..169`, and `245..264` (`FT TRANSMEM`).
  - ABC transporter transmembrane type-1 domain (`PROSITE:PS50928`, `Pfam:PF00528`, `InterPro:IPR000515`, residues `80..264`).
  - Family classification: `NCBIfam:NF008470` (`SsuC`, aliphatic sulfonates ABC transporter permease SsuC), `PANTHER:PTHR30151:SF38` (`ALIPHATIC SULFONATES TRANSPORT PERMEASE PROTEIN SSUC-RELATED`).

## 2. Literature & Comparative Evidence
- **[PMID:10781534](https://pubmed.ncbi.nlm.nih.gov/10781534/) (Eichhorn, van der Ploeg & Leisinger 2000, *J Bacteriol* 182:2687-2695):** Established that `ssuABC` encodes the aliphatic sulfonate ABC importer in *E. coli*, whose components are not functionally exchangeable with `tauABC`.
- **[PMID:10781557](https://pubmed.ncbi.nlm.nih.gov/10781557/) (Kahnert et al. 2000, *J Bacteriol* 182:2869-2878):** Characterized the `ssuEADCBF` operon in *P. putida* S-313, identifying `ssuC` as the integral membrane permease component of the ABC-type sulfonate importer.

## 3. Review of Existing GOA Annotations (5 IEA rows)
1. **`GO:0005886` (`plasma membrane`, `located_in`, IEA `GO_REF:0000120` from `UniProtKB-SubCell:SL-0037`, `PANTHER:PTN001319101`, `UniRule:UR000083623`)** -> **`ACCEPT`**:
   - Core subcellular localization of the 5-TM integral inner-membrane permease (`PROSITE:PS50928`, `PROSITE-ProRule:PRU00441`).
2. **`GO:0016020` (`membrane`, `located_in`, IEA `GO_REF:0000120` from `PROSITE-ProRule:PRU00441`, `InterPro:IPR000515`, `UniProtKB-SubCell:SL-0162`)** -> **`TOO_GENERAL`**:
   - True but uninformative parent cellular component already entailed by the accepted specific annotation `GO:0005886` (`plasma membrane`).
3. **`GO:0022857` (`transmembrane transporter activity`, `enables`, IEA `GO_REF:0000104` from `UniRule:UR000083623`)** -> **`MARK_AS_OVER_ANNOTATED`**:
   - Following the `PSEPK/ssuC` comparator convention, SsuC5 is the transmembrane channel subunit of a multi-subunit binding-protein-dependent ABC importer (`GO:0055052`) and cannot catalyze ATP-driven alkanesulfonate import independently of the periplasmic binding subunit SsuA2 and the ATPase subunit SsuB2. Its contribution to complex-level `GO:0042959` (`ABC-type alkanesulfonate transporter transporter activity`) is recorded via `contributes_to_molecular_function` in `core_functions`.
4. **`GO:0055085` (`transmembrane transport`, `involved_in`, IEA `GO_REF:0000120` from `PROSITE-ProRule:PRU00441`, `PANTHER:PTN001319101`)** -> **`MODIFY` to `GO:0042918` (`alkanesulfonate transmembrane transport`)**:
   - `GO:0055085` is true but general; membership in `NCBIfam:NF008470` (`SsuC`) and `PANTHER:PTHR30151:SF38` (`ALIPHATIC SULFONATES TRANSPORT PERMEASE PROTEIN SSUC-RELATED`) and syntenic placement between `ssuB2` (`VPARA_09230`, `KLN57912.1`) and `ssuD` (`VPARA_09250`, `KLN57914.1`) on contig `JZWI01000005` support refinement to `GO:0042918` (`alkanesulfonate transmembrane transport`).
5. **`GO:0058024` (`sulfonate transmembrane transporter activity`, `enables`, IEA `GO_REF:0000118` from `PANTHER:PTN001319101`)** -> **`MARK_AS_OVER_ANNOTATED`**:
   - As with `GO:0022857`, an isolated SsuC5 permease subunit does not have standalone transporter activity outside the intact SsuABC complex; its contribution is captured via `contributes_to_molecular_function` (`GO:0042959`) on the `GO:0055052` complex.

## 4. Proposed New Annotations
- **`GO:0055052` (`ATP-binding cassette (ABC) transporter complex, substrate-binding subunit-containing`, `part_of`, IC from `file:VARPD/ssuC5/ssuC5-uniprot.txt`)** -> **`NEW`**:
   - SsuC5 (`VPARA_09240`, `KLN57913.1`) forms the transmembrane translocation pathway of the substrate-binding-subunit-containing SsuABC importer complex (`GO:0055052`) with `ssuB2` (`VPARA_09230`, `KLN57912.1`) and `ssuA2` (`VPARA_09270`, `KLN57916.1`).
