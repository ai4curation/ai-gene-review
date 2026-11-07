# Curation Notes for `cusS` (`VPARA_44940`, `A0A0H2MBG2`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Overview
- **UniProtKB Accession:** `A0A0H2MBG2` (`A0A0H2MBG2_VARPD`, unreviewed, 443 aa, 48,473 Da)
- **Gene Symbol / Locus Tag:** `cusS` / `VPARA_44940` (`EMBL:KLN54350.1` on genomic contig `JZWI01000024`, `RefSeq:WP_021004630.1`)
- **Organism:** *Variovorax paradoxus* strain TBEA6 (`NCBITaxon:34073`)
- **Genomic Context & Nomenclature Note:** Encoded at the 3' end of the `czcA3-czcB-czcC-czcI-czcR-cusS` (`VPARA_44890-VPARA_44940`) heavy-metal resistance gene cluster on contig `JZWI01000024` (`KLN54345.1-KLN54350.1`), immediately downstream of its cognate response regulator `czcR` (`VPARA_44930`, `KLN54349.1`). Although the preliminary WGS EMBL submission (`KLN54350.1`) assigned the gene symbol `cusS`, its NCBIfam classification is `TIGR01386` (`czcS`, heavy metal sensor histidine kinase), its InterPro entry is `IPR006290` (`CzcS`), its PANTHER subfamily is `PTHR45436:SF9` (`SENSOR PROTEIN CZCS`), and its syntenic partner is `czcR` (`VPARA_44930`, `TIGR01387`), identifying `VPARA_44940` as the CzcS heavy-metal sensor histidine kinase of the `czc` cluster.
- **Domain Architecture & Key Residues:**
  - Two transmembrane alpha-helices at residues `21..41` and `145..168` (`FT TRANSMEM`, `SAM:Phobius`) flanking the periplasmic heavy-metal-sensing domain (residues `42..144`).
  - Cytoplasmic HAMP signal-transducing linker domain (`PROSITE:PS50885`, `InterPro:IPR003660`, residues `169..222`).
  - C-terminal histidine kinase domain (`PROSITE:PS50109`, `InterPro:IPR005467`, residues `230..443`; `EC 2.7.13.3`) comprising the His Kinase A phospho-acceptor/dimerization domain (`Pfam:PF00512`, `InterPro:IPR003661`, residues `223..288`) with the conserved autocatalytic histidine phospho-acceptor `His233` (within `230-DVAHELRTPLA-240`, `FT MOD_RES 233 /note="Pros-phosphohistidine" /evidence="ECO:0000256|PROSITE-ProRule:PRU00107"`) and the C-terminal HATPase_c ATP-binding catalytic domain (`Pfam:PF02518`, `InterPro:IPR003594`).

## 2. Literature & Comparative Evidence
- **[PMID:10198000](https://pubmed.ncbi.nlm.nih.gov/10198000/) (Grosse et al. 1999, *J Bacteriol* 181:2385-2393):** Constructed $\Delta czcS$ and $\Delta czcR$ deletion mutants in *Alcaligenes eutrophus* (*Cupriavidus metallidurans* CH34) and demonstrated by growth in $5\text{ mM }\text{Zn}^{2+}$, reporter induction by $\text{Zn}^{2+}$/$300\ \mu\text{M}$, $\text{Co}^{2+}$, and $\text{Cd}^{2+}$, and `czcCBA` mRNA analysis that the CzcRS two-component system senses heavy-metal cations and activates `czc` transcription.

## 3. Review of Existing GOA Annotations (9 IEA rows)
1. **`GO:0000155` (`phosphorelay sensor kinase activity`, `enables`, IEA `GO_REF:0000120` from `PROSITE-ProRule:PRU00107`, `InterPro:IPR003661`, `PANTHER:PTN001614306`, `RHEA:16537`, `EC:2.7.13.3`)** -> **`ACCEPT`**:
   - Core catalytic and sensory molecular function of CusS/CzcS (`EC 2.7.13.3`, `PROSITE:PS50109`, phospho-acceptor `His233`).
2. **`GO:0000160` (`phosphorelay signal transduction system`, `involved_in`, IEA `GO_REF:0000120` from `PROSITE-ProRule:PRU00107`, `PROSITE-ProRule:PRU00102`, `InterPro:IPR003660`, `PANTHER:PTN001614306`)** -> **`ACCEPT`**:
   - Core biological process mediated by the CzcS/CusS sensor kinase paired with its cognate response regulator CzcR (`VPARA_44930`).
3. **`GO:0005524` (`ATP binding`, `enables`, IEA `GO_REF:0000120` from `PROSITE-ProRule:PRU00107`, `InterPro:IPR003594`)** -> **`ACCEPT`**:
   - Core nucleotide-binding activity of the C-terminal HATPase_c catalytic domain (`Pfam:PF02518`, `InterPro:IPR003594`, `PROSITE:PS50109`).
4. **`GO:0005886` (`plasma membrane`, `located_in`, IEA `GO_REF:0000120` from `UniProtKB-SubCell:SL-0037`, `PANTHER:PTN001614306`)** -> **`ACCEPT`**:
   - Core subcellular localization of the two-TM integral inner-membrane sensor kinase (`FT TRANSMEM 21..41` and `145..168`).
5. **`GO:0016020` (`membrane`, `located_in`, IEA `GO_REF:0000120` from `InterPro:IPR006290`, `UniProtKB-SubCell:SL-0162`, `PANTHER:PTN001614306`)** -> **`TOO_GENERAL`**:
   - True but uninformative parent cellular component already entailed by the accepted specific term `GO:0005886` (`plasma membrane`).
6. **`GO:0016310` (`phosphorylation`, `involved_in`, IEA `GO_REF:0000108` from `GO:0016772`)** -> **`TOO_GENERAL`**:
   - True but uninformative parent biological process already entailed by `GO:0000160` (`phosphorelay signal transduction system`) and `GO:0046777` (`protein autophosphorylation`).
7. **`GO:0016772` (`transferase activity, transferring phosphorus-containing groups`, `enables`, IEA `GO_REF:0000043` from `UniProtKB-KW:KW-0418`)** -> **`TOO_GENERAL`**:
   - True but uninformative parent molecular function already entailed by the accepted specific child term `GO:0000155` (`phosphorelay sensor kinase activity`).
8. **`GO:0046686` (`response to cadmium ion`, `involved_in`, IEA `GO_REF:0000002` from `InterPro:IPR006290`)** -> **`ACCEPT`**:
   - Supported by `InterPro:IPR006290` (`CzcS`, `NCBIfam:TIGR01386`), `PANTHER:PTHR45436:SF9` (`SENSOR PROTEIN CZCS`), and experimental characterization of CzcRS sensing of $\text{Zn}^{2+}$, $\text{Co}^{2+}$, and $\text{Cd}^{2+}$ (PMID:10198000).
9. **`GO:0046777` (`protein autophosphorylation`, `involved_in`, IEA `GO_REF:0000118` from `PANTHER:PTN001614306`)** -> **`ACCEPT`**:
   - Core biochemical step in which CusS/CzcS autophosphorylates at the conserved histidine residue `His233` (`FT MOD_RES 233 /note="Pros-phosphohistidine"`, `RHEA:16537`) upon periplasmic metal sensing.

## 4. Proposed New Annotations
- **`GO:0010043` (`response to zinc ion`, `involved_in`, ISS from `PMID:10198000` and `file:VARPD/cusS/cusS-uniprot.txt`)** -> **`NEW`**:
   - Zinc ($\text{Zn}^{2+}$) is the primary physiological inducer sensed by the CzcS (`TIGR01386`, `PTHR45436:SF9`) sensor kinase in the `czc` heavy-metal resistance system (PMID:10198000).
