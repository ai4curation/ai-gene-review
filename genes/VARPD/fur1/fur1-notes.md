# Curation Notes for `fur1` (`VPARA_18200`, `A0A0H2M8T9`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Overview
- **UniProtKB Accession:** `A0A0H2M8T9` (`A0A0H2M8T9_VARPD`, unreviewed, 139 aa, 15,839 Da)
- **Gene Symbol / Locus Tag:** `fur1` (synonym `fur`) / `VPARA_18200` (`EMBL:KLN57112.1` on genomic contig `JZWI01000008`, `RefSeq:WP_021005176.1`)
- **Organism:** *Variovorax paradoxus* strain TBEA6 (`NCBITaxon:34073`)
- **Domain Architecture & Metal-Coordination Sites (Verified against `SQ` block):**
  - Homodimeric metalloregulator (`RuleBase:RU364037`) of the Fur family (`Pfam:PF01475`, `InterPro:IPR002481`, `NCBIfam:NF006999`, `PANTHER:PTHR33202:SF2` `FERRIC UPTAKE REGULATION PROTEIN`), comprising an N-terminal winged-helix DNA-binding domain (`Gene3D:1.10.10.10`, `InterPro:IPR036388`) and a C-terminal histidine/cysteine-rich dimerization and metal-binding domain (`InterPro:IPR043135`, `85-THHDHLICTSCGKVEEFYDAEIERRQQMISKDKGWILQDHAMSLYGLCGDCVGKR-139`).
  - **Regulatory $\text{Fe}^{2+}$/$\text{Mn}^{2+}$-sensing site (`PIRSR:PIRSR602481-2`, 1 $\text{Fe}^{2+}$ or $\text{Mn}^{2+}$ ion per subunit):** Coordinated by `His86`, `Asp88` (within `85-THHDH-89`), `Glu107` (within `104-FYDAEIE-110`), and `His124` (within `122-QDHAM-126`) (`FT BINDING 86`, `88`, `107`, `124`).
  - **Structural $\text{Zn}^{2+}$ site (`PIRSR:PIRSR602481-1`, 1 $\text{Zn}^{2+}$ ion per subunit):** Coordinated by the four conserved cysteines `Cys92`, `Cys95` (`92-CTSC-95`), `Cys132`, and `Cys135` (`132-CGDC-135`) (`FT BINDING 92`, `95`, `132`, `135`).

## 2. Literature & Comparative Evidence
- **[PMID:8522528](https://pubmed.ncbi.nlm.nih.gov/8522528/) (Ochsner, Vasil & Vasil 1995, *J Bacteriol* 177:7194-7201):** Purified *Pseudomonas aeruginosa* Fur and demonstrated by gel mobility shift and DNase I footprinting that holo-Fur-$\text{Fe(II)}$ specifically binds conserved 19-bp "Fur box" operator sequences (`GATAATGATAATCATTATC`) overlapping iron-regulated siderophore promoters (`pvdS`, `pchR`, `fepA-fes`) to repress transcription under iron-replete conditions.
- **[PMID:12581348](https://pubmed.ncbi.nlm.nih.gov/12581348/) (Pohl et al. 2003, *Mol Microbiol* 47:903-915):** Solved the 1.8-Å crystal structure and X-ray absorption spectroscopy of Fur, characterizing the distinct structural $\text{Zn}^{2+}$ site and regulatory $\text{Fe}^{2+}$-sensing site that couple intracellular iron occupancy to operator DNA binding.
- **[PMID:20562273](https://pubmed.ncbi.nlm.nih.gov/20562273/) (Chen, Bleam & Hickey 2010, *Appl Environ Microbiol* 76:5620-5630):** Demonstrated in *Pseudomonas putida* KT2440 that a $\Delta fur$ deletion mutant shows altered expression of iron-homeostasis genes and increased $\text{H}_2\text{O}_2$ sensitivity.

## 3. Review of Existing GOA Annotations (13 IEA rows)
Following the curated comparator reviews `genes/PSEAE/fur/fur-ai-review.yaml` and `genes/PSEPK/fur/fur-ai-review.yaml`:
1. **`GO:0000976` (`transcription cis-regulatory region binding`, `enables`, IEA `GO_REF:0000120` from `ARBA:ARBA00028970`, `PANTHER:PTN002848968`)** -> **`ACCEPT`**:
   - Core molecular function; holo-Fur binds conserved Fur-box operator sequences in cis-regulatory promoter regions of iron-regulated genes (PMID:8522528).
2. **`GO:0001216` (`DNA-binding transcription activator activity`, `enables`, IEA `GO_REF:0000117` from `ARBA:ARBA00027660`)** -> **`MODIFY` to `GO:0001217` (`DNA-binding transcription repressor activity`)**:
   - ARBA (`GO_REF:0000117`) assigned `GO:0001216` (activator), whereas Fur (`RuleBase:RU364037`, `KW Repressor`) acts primarily as an $\text{Fe(II)}$-dependent transcriptional repressor when bound to Fur-box operators overlapping target promoters (PMID:8522528; positive effects on some iron-storage genes are typically indirect via repression of small RNAs such as RyhB/PrrF). Refined laterally to `GO:0001217` (`DNA-binding transcription repressor activity`), matching `PSEAE/fur`.
3. **`GO:0003677` (`DNA binding`, `enables`, IEA `GO_REF:0000104` from `UniRule:UR000481764`)** -> **`TOO_GENERAL`**:
   - True but uninformative parent term already entailed by the accepted specific child term `GO:0000976` (`transcription cis-regulatory region binding`).
4. **`GO:0003700` (`DNA-binding transcription factor activity`, `enables`, IEA `GO_REF:0000120` from `InterPro:IPR002481`, `PANTHER:PTN002848968`, `UniRule:UR000481764`)** -> **`MODIFY` to `GO:0001217` (`DNA-binding transcription repressor activity`)**:
   - Unsigned parent transcription factor term; refined to the signed child term `GO:0001217` (`DNA-binding transcription repressor activity`), matching `PSEAE/fur`.
5. **`GO:0005737` (`cytoplasm`, `located_in`, IEA `GO_REF:0000044` from `UniProtKB-SubCell:SL-0086`)** -> **`TOO_GENERAL`**:
   - True but uninformative parent cellular component already entailed by the accepted specific child term `GO:0005829` (`cytosol`).
6. **`GO:0005829` (`cytosol`, `located_in`, IEA `GO_REF:0000118` from `PANTHER:PTN002848968`)** -> **`ACCEPT`**:
   - Core subcellular localization of the soluble 139-aa cytoplasmic repressor (`RuleBase:RU364037`).
7. **`GO:0006355` (`regulation of DNA-templated transcription`, `involved_in`, IEA `GO_REF:0000002` from `InterPro:IPR002481`)** -> **`TOO_GENERAL`**:
   - True but uninformative unsigned parent process already entailed by the accepted specific child term `GO:0045892` (`negative regulation of DNA-templated transcription`).
8. **`GO:0008270` (`zinc ion binding`, `enables`, IEA `GO_REF:0000118` from `PANTHER:PTN002848968`)** -> **`KEEP_AS_NON_CORE`**:
   - Unlike *P. putida* Fur (which lacks the 4-Cys motif), *V. paradoxus* TBEA6 Fur1 retains the canonical four-cysteine structural $\text{Zn}^{2+}$-binding motif at `Cys92`, `Cys95` (`92-CTSC-95`), `Cys132`, and `Cys135` (`132-CGDC-135`), annotated by `PIRSR:PIRSR602481-1` (`FT BINDING 92`, `95`, `132`, `135`). As in `PSEAE/fur`, structural $\text{Zn}^{2+}$ binding is genuine but non-core relative to regulatory $\text{Fe}^{2+}$ sensing, so `GO:0008270` is retained as `KEEP_AS_NON_CORE` while `GO:0008198` (`ferrous iron binding`) is added as `NEW`.
9. **`GO:0032993` (`protein-DNA complex`, `part_of`, IEA `GO_REF:0000117` from `ARBA:ARBA00028896`)** -> **`KEEP_AS_NON_CORE`**:
   - Matching `PSEAE/fur`, holo-Fur forms a transient operator-bound protein-DNA complex when repressing target promoters (PMID:8522528), which is true but adds little beyond `GO:0000976` and is kept as `KEEP_AS_NON_CORE`.
10. **`GO:0045892` (`negative regulation of DNA-templated transcription`, `involved_in`, IEA `GO_REF:0000118` from `PANTHER:PTN002848968`)** -> **`ACCEPT`**:
    - Core biological process of Fur (`RuleBase:RU364037`, `KW Repressor`; PMID:8522528).
11. **`GO:0045893` (`positive regulation of DNA-templated transcription`, `involved_in`, IEA `GO_REF:0000108` from `GO:0001216`)** -> **`MODIFY` to `GO:0045892` (`negative regulation of DNA-templated transcription`)**:
    - Automatically inferred via `GO_REF:0000108` from the ARBA `GO:0001216` row; refined laterally to `GO:0045892` (`negative regulation of DNA-templated transcription`) to match the modification of `GO:0001216` $\rightarrow$ `GO:0001217`.
12. **`GO:1900376` (`regulation of secondary metabolite biosynthetic process`, `involved_in`, IEA `GO_REF:0000118` from `PANTHER:PTN002848968`)** -> **`TOO_GENERAL`**:
    - True but uninformative parent process already entailed by the accepted specific child term `GO:1900705` (`negative regulation of siderophore biosynthetic process`, since `GO:1900705 is_a GO:1900376`).
13. **`GO:1900705` (`negative regulation of siderophore biosynthetic process`, `involved_in`, IEA `GO_REF:0000118` from `PANTHER:PTN002848968`)** -> **`ACCEPT`**:
    - Core biological process in siderophore-producing bacteria such as *Variovorax paradoxus* (which synthesizes vacidobactin and variobactin siderophores, PMID:26412281, and carries the `exbD5-exbB4-tonB-bfrD1` ferric-siderophore uptake locus).

## 4. Proposed New Annotations
- **`GO:0008198` (`ferrous iron binding`, `enables`, IC from `file:VARPD/fur1/fur1-uniprot.txt` and `PMID:12581348`)** -> **`NEW`**:
   - Captures the physiological iron-sensing cofactor activity of Fur1 at its conserved regulatory site (`His86`, `Asp88`, `Glu107`, `His124`; `PIRSR:PIRSR602481-2`, `CC -!- COFACTOR: Name=Fe(2+); Xref=ChEBI:CHEBI:29033; Evidence={ECO:0000256|PIRSR:PIRSR602481-2}`).
