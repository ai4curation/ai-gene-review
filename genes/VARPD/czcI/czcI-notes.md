# Curation Notes for `czcI` (`VPARA_44920`, `A0A0H2LVR9`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Overview
- **UniProtKB Accession:** `A0A0H2LVR9` (`A0A0H2LVR9_VARPD`, unreviewed, 123 aa, 13,551 Da)
- **Gene Symbol / Locus Tag:** `czcI` / `VPARA_44920` (`EMBL:KLN54348.1` on genomic contig `JZWI01000024`, `RefSeq:WP_021004628.1`)
- **Organism:** *Variovorax paradoxus* strain TBEA6 (`NCBITaxon:34073`)
- **Genomic Context:** Encoded on genomic contig `JZWI01000024` within the heavy-metal resistance gene cluster (`czcA3` `VPARA_44890` `KLN54345.1`, `czcB` `VPARA_44900` `KLN54346.1`, `czcC` `VPARA_44910` `KLN54347.1`, `czcI` `VPARA_44920` `KLN54348.1`, `czcR` `VPARA_44930` `KLN54349.1`, `cusS` `VPARA_44940` `KLN54350.1`, and `cadA2` `VPARA_44980` `KLN54354.1`), where consecutive EMBL CDS accessions (`KLN54345.1–KLN54350.1`) and locus tags stepping by 10 place `czcI` immediately downstream of `czcC` (`VPARA_44910`) and immediately upstream of the two-component regulatory genes `czcR` (`VPARA_44930`) and `cusS` (`VPARA_44940`).
- **Domain Architecture & Targeting:**
  - N-terminal Sec signal peptide at residues `1..20` (`1-MRRWLLIFLLLLLPLQSSWA-20`, `FT SIGNAL 1..20`, `SAM:SignalP`).
  - Mature periplasmic domain at residues `21..123` (`Pfam:PF11162` `DUF2946`, `NCBIfam:NF045614` `efflu_CzcI_Cupr`, `InterPro:IPR055013` `CzcI`) containing 9 histidine residues (`His28`, `His36`, `His39`, `His40`, `His42`, `His75`, `His81`, `His105`, `His109`), including a histidine-rich cluster (`36-HWGHHEHE-43`) and a conserved `71-CAVCH-75` motif.

## 2. Literature & Comparative Evidence
- **[PMID:10198000](https://pubmed.ncbi.nlm.nih.gov/10198000/) (Grosse et al. 1999, *J Bacteriol* 181:2385-2393):** Analyzed the transcriptional organization of the `czcNICBADRS` heavy-metal homeostasis determinant in *Alcaligenes eutrophus* (*Cupriavidus metallidurans* CH34), identifying a 400-nt `czcI` transcript and continuous `czcN-czcI-czcC` transcription induced by $\text{Zn}^{2+}$ ($300\ \mu\text{M}$), $\text{Co}^{2+}$, and $\text{Cd}^{2+}$.
- **[PMID:12829273](https://pubmed.ncbi.nlm.nih.gov/12829273/) (Nies 2003, *FEMS Microbiol Rev* 27:313-339):** Reviewed bacterial heavy-metal efflux systems, including the `czc` CBA efflux determinant and its associated periplasmic/regulatory proteins.

## 3. Review of Existing GOA Annotations (1 IEA row)
1. **`GO:0046686` (`response to cadmium ion`, `involved_in`, IEA `GO_REF:0000002` from `InterPro:IPR055013`)** -> **`ACCEPT`**:
   - `InterPro:IPR055013` (`CzcI`, integrating `Pfam:PF11162` and `NCBIfam:NF045614` `efflu_CzcI_Cupr`) maps to `GO:0046686` (`response to cadmium ion`). In *V. paradoxus* TBEA6, `czcI` (`VPARA_44920`, `KLN54348.1`) is encoded directly between `czcA3-czcB-czcC` (`VPARA_44890-VPARA_44910`, `KLN54345.1-KLN54347.1`, `UniProtKB:A0A0H2MBF7`, `UniProtKB:A0A0H2LX82`, `UniProtKB:A0A0H2M0U4`) and `czcR-cusS` (`VPARA_44930-VPARA_44940`, `KLN54349.1-KLN54350.1`, `UniProtKB:A0A0H2LVW5`, `UniProtKB:A0A0H2MBG2`), which is a cobalt-zinc-cadmium ($\text{Co}^{2+}$/$\text{Zn}^{2+}$/$\text{Cd}^{2+}$) resistance cluster (PMID:10198000).

## 4. Proposed New Annotations
- **`GO:0010043` (`response to zinc ion`, `involved_in`, ISS from `PMID:10198000`)** -> **`NEW`**:
   - Co-transcribed and syntenically conserved in the `czcA3-czcB-czcC-czcI-czcR-cusS` (`VPARA_44890-VPARA_44940`) Zn2+/Cd2+/Co2+ resistance island (PMID:10198000).
- **`GO:0030288` (`outer membrane-bounded periplasmic space`, `located_in`, IC from `file:VARPD/czcI/czcI-uniprot.txt` and `PMID:10198000`)** -> **`NEW`**:
   - Mature CzcI (`VPARA_44920`, `NCBIfam:NF045614`, `InterPro:IPR055013`) is a soluble periplasmic heavy-metal resistance modulator lacking transmembrane helices in this diderm Gram-negative betaproteobacterium.
