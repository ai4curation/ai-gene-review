# Curation Notes for `tauC` (`VPARA_03670`, `A0A0H2M7Y1`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Overview
- **UniProtKB Accession:** `A0A0H2M7Y1` (`A0A0H2M7Y1_VARPD`, unreviewed, 294 aa, 30,858 Da)
- **Gene Symbol / Locus Tag:** `tauC` / `VPARA_03670` (`EMBL:KLN58256.1` on genomic contig `JZWI01000003`, `RefSeq:WP_021006827.1`)
- **Organism:** *Variovorax paradoxus* strain TBEA6 (`NCBITaxon:34073`)
- **Genomic Context:** Encoded at the 3' end of the three-gene `tauA-tauB1-tauC` (`VPARA_03650-VPARA_03670`) taurine ABC importer operon on contig `JZWI01000003` (`KLN58254.1`, `KLN58255.1`, `KLN58256.1`).
- **Domain Architecture & Topology:**
  - Six Phobius-predicted transmembrane alpha-helices at residues `42..62`, `100..121`, `141..160`, `166..185`, `221..241`, and `261..283` (`FT TRANSMEM`).
  - ABC transporter transmembrane type-1 domain (`PROSITE:PS50928`, `Pfam:PF00528`, `InterPro:IPR000515`, residues `100..280`).
  - Specific subfamily: `PANTHER:PTHR30409:SF9` (`TAURINE TRANSPORT SYSTEM PERMEASE PROTEIN TAUC`), `HAMAP:MF_01668` (`ABC_tauC`), `InterPro:IPR035906` (`MetI-like_sf`).

## 2. Literature & Comparative Evidence
- **[PMID:8808933](https://pubmed.ncbi.nlm.nih.gov/8808933/) (van der Ploeg et al. 1996, *J Bacteriol* 178:5438-5446):** Identified `tauC` in the *E. coli* `tauABCD` operon as the integral membrane permease subunit of the ABC-type taurine importer.
- **[PMID:10781534](https://pubmed.ncbi.nlm.nih.gov/10781534/) (Eichhorn, van der Ploeg & Leisinger 2000, *J Bacteriol* 182:2687-2695):** Deletion and complementation analysis in *E. coli* established that `tauABC` mediates taurine import and its subunits cannot form functional hybrid transporters with `ssuABC`.

## 3. Review of Existing GOA Annotations (5 IEA rows)
1. **`GO:0005886` (`plasma membrane`, `located_in`, IEA `GO_REF:0000120` from `UniProtKB-SubCell:SL-0037`, `PANTHER:PTN001319101`, `UniRule:UR000083623`)** -> **`ACCEPT`**:
   - Core subcellular localization of the 6-TM integral inner-membrane permease (`PROSITE:PS50928`, `PROSITE-ProRule:PRU00441`).
2. **`GO:0015734` (`taurine transmembrane transport`, `involved_in`, IEA `GO_REF:0000120` from `PANTHER:PTN001319101`, `UniProtKB-KW:KW-0029`, `UniRule:UR000083623`)** -> **`ACCEPT`**:
   - Core biological process mediated by TauC (`HAMAP:MF_01668`, `PANTHER:PTHR30409:SF9`) within the `tauA-tauB1-tauC` operon.
3. **`GO:0016020` (`membrane`, `located_in`, IEA `GO_REF:0000120` from `InterPro:IPR000515`, `UniProtKB-KW:KW-0812`, `UniProtKB-SubCell:SL-0162`)** -> **`TOO_GENERAL`**:
   - True but uninformative parent cellular component already entailed by the accepted specific annotation `GO:0005886` (`plasma membrane`).
4. **`GO:0022857` (`transmembrane transporter activity`, `enables`, IEA `GO_REF:0000104` from `UniRule:UR000083623`)** -> **`MARK_AS_OVER_ANNOTATED`**:
   - Following the `PSEPK/tauC` comparator convention, TauC is the transmembrane channel subunit of a multi-subunit ABC importer (`GO:0055052`) and cannot catalyze taurine transport independently of the periplasmic binding protein TauA and the ATPase subunit TauB1. Its contribution to complex-level `GO:0015411` (`ABC-type taurine transporter activity`) is recorded via `contributes_to_molecular_function` in `core_functions`.
5. **`GO:0058024` (`sulfonate transmembrane transporter activity`, `enables`, IEA `GO_REF:0000118` from `PANTHER:PTN001319101`)** -> **`MARK_AS_OVER_ANNOTATED`**:
   - As with `GO:0022857`, an isolated TauC permease subunit does not have standalone transporter activity outside the intact TauABC complex; its contribution is captured via `contributes_to_molecular_function` (`GO:0015411`) on the `GO:0055052` complex.

## 4. Proposed New Annotations
- **`GO:0055052` (`ATP-binding cassette (ABC) transporter complex, substrate-binding subunit-containing`, `part_of`, IC from `file:VARPD/tauC/tauC-uniprot.txt` and `PMID:8808933`)** -> **`NEW`**:
   - TauC (`VPARA_03670`, `KLN58256.1`) forms the integral inner-membrane translocation channel of the TauABC importer complex (`GO:0055052`) with `tauA` (`VPARA_03650`, `KLN58254.1`) and `tauB1` (`VPARA_03660`, `KLN58255.1`).
