# Curation Notes for `cadA2` (`VPARA_44980`, `A0A0H2LVW9`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Overview
- **UniProtKB Accession:** `A0A0H2LVW9` (`A0A0H2LVW9_VARPD`, unreviewed, 759 aa, 78,618 Da)
- **Gene Symbol / Locus Tag:** `cadA2` / `VPARA_44980` (`EMBL:KLN54354.1` on genomic contig `JZWI01000024`, `RefSeq:WP_047786071.1`)
- **Organism:** *Variovorax paradoxus* strain TBEA6 (`NCBITaxon:34073`)
- **Genomic Context:** Encoded on genomic contig `JZWI01000024` within the same heavy-metal resistance island as `czcA3-czcB-czcC-czcI-czcR-cusS` (`VPARA_44890-VPARA_44940`, `KLN54345.1-KLN54350.1`), 4 ORFs downstream of `cusS` (`VPARA_44980`, `KLN54354.1`).
- **Domain Architecture & Key Sequence Motifs (Verified against `SQ` block):**
  - **N-terminal Heavy-Metal-Associated (HMA) cytoplasmic domain (`CDD:cd00371`, `InterPro:IPR006121`, `SUPFAM:SSF55008`, residues ~`1..120`):** Contains a cysteine-rich metal-binding motif `26-CCGSTAC-32` (`Cys26`, `Cys27`, `Cys32`) and `57-MDC-59` (`Cys59`).
  - **Transmembrane domain M (`InterPro:IPR023298`):** UniProt `RuleBase:RU362081` annotates six transmembrane helices at `140..160`, `166..186`, `198..214`, `368..390`, `705..726`, and `732..750`, while residues `402..421` (`402-KALVLLVIACPCALVISTPV-421`) form the canonical $\text{P}_{1\text{B}}$-type intramembrane metal-translocation helix carrying the invariant `Cys410-Pro411-Cys412` (`410-CPC-412`) motif.
  - **Cytoplasmic Actuator (A) domain (`Pfam:PF00122`, `InterPro:IPR059000`, `FT DOMAIN 251..352`):** Contains the conserved `296-TGES-299` phosphatase motif.
  - **Cytoplasmic HAD-like phosphorylation (P) and nucleotide-binding (N) domains (`Pfam:PF00702`, `InterPro:IPR023299`, `InterPro:IPR018303`, `PROSITE:PS00154`):** Contains the invariant catalytic phosphorylation aspartate `Asp454` within the `454-DKTGTIT-460` P-type ATPase motif (`PROSITE:PS00154`) and the conserved $\text{Mg}^{2+}$-coordinating hinge motif `650-GDGINDAPALA-660`.
  - **Family & Subfamily Classification:** `NCBIfam:TIGR01512` (`ATPase-IB2_Cd`, $\text{Cd}^{2+}$/$\text{Zn}^{2+}$-exporting $\text{P}_{1\text{B}-2}$-type ATPase), `NCBIfam:TIGR01525` (`ATPase-IB_hvy`), `InterPro:IPR027256` (`P-typ_ATPase_IB`), `PANTHER:PTHR48085:SF5` (`CADMIUM_ZINC-TRANSPORTING ATPASE HMA4-RELATED`), `EC 7.2.2.12` (`RHEA:20621`, P-type $\text{Zn}^{2+}$ transporter).

## 2. Literature & Comparative Evidence
- **[PMID:9405611](https://pubmed.ncbi.nlm.nih.gov/9405611/) (Rensing, Mitra & Rosen 1997, *Proc Natl Acad Sci U S A* 94:14326-14331):** Identified *E. coli* ZntA as the prototype bacterial $\text{Zn}^{2+}$/$\text{Cd}^{2+}$-translocating $\text{P}_{1\text{B}}$-type ATPase, showing that everted membrane vesicles catalyze vanadate-sensitive, ATP-dependent accumulation of $^{65}\text{Zn(II)}$ and $^{109}\text{Cd(II)}$ (`"Everted membrane vesicles from a wild-type strain accumulated 65Zn(II) and 109Cd(II) by using ATP as an energy source. Transport was sensitive to vanadate, an inhibitor of P-type ATPases."`).
- **[PMID:12867443](https://pubmed.ncbi.nlm.nih.gov/12867443/) (Legatzki et al. 2003, *J Bacteriol* 185:4354-4361):** Demonstrated the physiological interplay between the CzcCBA RND efflux complex and the two soft-metal-transporting $\text{P}_{1\text{B}}$-type ATPases CadA and ZntA in *Ralstonia metallidurans* (*Cupriavidus metallidurans* CH34), establishing that both CadA and ZntA export cytoplasmic $\text{Cd}^{2+}$ and $\text{Zn}^{2+}$ across the inner membrane (`"Cadmium and zinc are removed from cells of Ralstonia metallidurans by the CzcCBA efflux pump and by two soft-metal-transporting P-type ATPases, CadA and ZntA."`).

## 3. Review of Existing GOA Annotations (16 IEA rows)
1. **`GO:0000166` (`nucleotide binding`, `enables`, IEA `GO_REF:0000002` from `InterPro:IPR023299`)** -> **`TOO_GENERAL`**:
   - True but uninformative parent term already entailed by the accepted child term `GO:0005524` (`ATP binding`).
2. **`GO:0005524` (`ATP binding`, `enables`, IEA `GO_REF:0000120` from `InterPro:IPR001757`, `UniRule:UR000169778`)** -> **`ACCEPT`**:
   - Core cosubstrate-binding activity of the cytoplasmic N/P domains (`InterPro:IPR023299`, `InterPro:IPR001757`), required for formation of the `Asp454` acyl-phosphate intermediate (`454-DKTGTIT-460`).
3. **`GO:0005886` (`plasma membrane`, `located_in`, IEA `GO_REF:0000120` from `UniProtKB-SubCell:SL-0039`, `UniRule:UR000169778`)** -> **`ACCEPT`**:
   - Core subcellular localization of the multi-pass inner-membrane $\text{P}_{1\text{B}}$-type efflux ATPase (`RuleBase:RU362081`).
4. **`GO:0006812` (`monoatomic cation transport`, `involved_in`, IEA `GO_REF:0000002` from `InterPro:IPR027256`)** -> **`TOO_GENERAL`**:
   - True but uninformative parent process already entailed by the accepted specific child terms `GO:0071577` (`zinc ion transmembrane transport`) and `GO:0070574` (`cadmium ion transmembrane transport`).
5. **`GO:0015086` (`cadmium ion transmembrane transporter activity`, `enables`, IEA `GO_REF:0000118` from `PANTHER:PTN002458237`)** -> **`ACCEPT`**:
   - Core molecular function of CadA/ZntA-family $\text{P}_{1\text{B}-2}$-type ATPases (`NCBIfam:TIGR01512` `ATPase-IB2_Cd`, `PANTHER:PTHR48085:SF5`), which export both $\text{Cd}^{2+}$ and $\text{Zn}^{2+}$ across the cytoplasmic membrane (PMID:9405611, PMID:12867443).
6. **`GO:0016020` (`membrane`, `located_in`, IEA `GO_REF:0000120` from `InterPro:IPR001757`, `InterPro:IPR027256`, `UniProtKB-SubCell:SL-0162`, `PANTHER:PTN002458237`)** -> **`TOO_GENERAL`**:
   - True but uninformative parent cellular component already entailed by `GO:0005886` (`plasma membrane`).
7. **`GO:0016463` (`P-type zinc transporter activity`, `enables`, IEA `GO_REF:0000120` from `RHEA:20621`, `EC:7.2.2.12`)** -> **`ACCEPT`**:
   - Primary catalytic and transport activity (`EC 7.2.2.12`, `RHEA:20621`) coupling ATP hydrolysis at `Asp454` (`454-DKTGTIT-460`) to transmembrane $\text{Zn}^{2+}$ export via the intramembrane `410-CPC-412` site (PMID:9405611, PMID:12867443).
8. **`GO:0016887` (`ATP hydrolysis activity`, `enables`, IEA `GO_REF:0000002` from `InterPro:IPR001757`)** -> **`TOO_GENERAL`**:
   - True but uninformative parent molecular function already entailed by `GO:0016463` (`P-type zinc transporter activity`, which is an `is_a` descendant of `GO:0019829` $\rightarrow$ `GO:0042626` $\rightarrow$ `GO:0016887`).
9. **`GO:0019829` (`ATPase-coupled monoatomic cation transmembrane transporter activity`, `enables`, IEA `GO_REF:0000002` from `InterPro:IPR027256`)** -> **`TOO_GENERAL`**:
   - True but uninformative parent molecular function already entailed by the accepted specific child term `GO:0016463` (`P-type zinc transporter activity`).
10. **`GO:0022857` (`transmembrane transporter activity`, `enables`, IEA `GO_REF:0000118` from `PANTHER:PTN002458237`)** -> **`TOO_GENERAL`**:
    - True but uninformative parent molecular function already entailed by `GO:0016463` and `GO:0015086`.
11. **`GO:0030001` (`metal ion transport`, `involved_in`, IEA `GO_REF:0000120` from `ARBA:ARBA00028072`, `PANTHER:PTN002458237`)** -> **`TOO_GENERAL`**:
    - True but uninformative parent process already entailed by `GO:0071577` (`zinc ion transmembrane transport`) and `GO:0070574` (`cadmium ion transmembrane transport`).
12. **`GO:0046872` (`metal ion binding`, `enables`, IEA `GO_REF:0000002` from `InterPro:IPR006121`, `InterPro:IPR036163`)** -> **`ACCEPT`**:
    - Supported by the N-terminal heavy-metal-associated (HMA) regulatory domain (`CDD:cd00371`, `InterPro:IPR006121`, `SUPFAM:SSF55008`, containing `26-CCGSTAC-32`) and the intramembrane `410-CPC-412` metal-coordination site.
13. **`GO:0055085` (`transmembrane transport`, `involved_in`, IEA `GO_REF:0000118` from `PANTHER:PTN002458237`)** -> **`TOO_GENERAL`**:
    - True but uninformative parent process already entailed by `GO:0071577` and `GO:0070574`.
14. **`GO:0070574` (`cadmium ion transmembrane transport`, `involved_in`, IEA `GO_REF:0000108` from `GO:0015086`)** -> **`ACCEPT`**:
    - Core biological process mediated by CadA2 (`NCBIfam:TIGR01512`, `PANTHER:PTHR48085:SF5`; PMID:9405611, PMID:12867443).
15. **`GO:0071577` (`zinc ion transmembrane transport`, `involved_in`, IEA `GO_REF:0000108` from `GO:0016463`)** -> **`ACCEPT`**:
    - Core biological process mediated by CadA2 (`EC 7.2.2.12`, `RHEA:20621`; PMID:9405611, PMID:12867443).
16. **`GO:0098655` (`monoatomic cation transmembrane transport`, `involved_in`, IEA `GO_REF:0000108` from `GO:0019829`)** -> **`TOO_GENERAL`**:
    - True but uninformative parent process already entailed by `GO:0071577` and `GO:0070574`.
