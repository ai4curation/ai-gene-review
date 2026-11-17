# Curation Notes for `ssuE` (`VPARA_09290`, `A0A0H2M6H0`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Overview
- **UniProtKB Accession:** `A0A0H2M6H0` (`A0A0H2M6H0_VARPD`, unreviewed, 194 aa, 20,975 Da)
- **Gene Symbol / Locus Tag:** `ssuE` / `VPARA_09290` (`EMBL:KLN57918.1` on genomic contig `JZWI01000005`, `RefSeq:WP_021006433.1`)
- **Organism:** *Variovorax paradoxus* strain TBEA6 (`NCBITaxon:34073`)
- **Genomic Context:** Encoded at the 3' end of the aliphatic sulfonate uptake and desulfonation gene cluster on contig `JZWI01000005` (`ssuB2` `VPARA_09230` `KLN57912.1`, `ssuC5` `VPARA_09240` `KLN57913.1`, `ssuD` `VPARA_09250` `KLN57914.1`, `ssuA2` `VPARA_09270` `KLN57916.1`, `ssuE` `VPARA_09290` `KLN57918.1`).
- **Domain Architecture & Classification:**
  - NADPH-dependent FMN reductase domain (`Pfam:PF03358`, `InterPro:IPR005025`, residues `1..142`) within the flavodoxin-like superfamily (`InterPro:IPR029039`).
  - Specific family membership: `NCBIfam:TIGR03567` (`FMN_red_SsuE`, FMN reductase, SsuE family), `InterPro:IPR019913` (`FMN_red_SsuE`), `PANTHER:PTHR43408:SF1` (`FMN REDUCTASE (NADPH)`), `EC 1.5.1.38`.

## 2. Literature & Comparative Evidence
- **[PMID:10480865](https://pubmed.ncbi.nlm.nih.gov/10480865/) (Eichhorn, van der Ploeg & Leisinger 1999, *J Biol Chem* 274:26639-26646):** Purified the two-component alkanesulfonate monooxygenase system from *E. coli* and demonstrated that SsuE is the NAD(P)H-dependent FMN reductase that supplies reduced flavin (`FMNH2`) to the alkanesulfonate monooxygenase SsuD (`"SsuE is the FMN reducing enzyme providing SsuD with FMNH(2)."` and `"SsuD catalysis was absolutely dependent on FMNH(2) and oxygen"`).
- **[PMID:10781557](https://pubmed.ncbi.nlm.nih.gov/10781557/) (Kahnert et al. 2000, *J Bacteriol* 182:2869-2878):** Showed in *P. putida* S-313 extracts that SsuE catalyzes NADPH-dependent FMN reduction (`"SsuE revealed NADPH-dependent FMN reductase activity and lower levels of FAD reductase activity (32% of the value with FMN). No activity was observed with NADH."`).
- **[PMID:26634408](https://pubmed.ncbi.nlm.nih.gov/26634408/) (Dayal,ernen & Ellis 2015, *Biochemistry* 54:7531-7538):** Demonstrated that optimal reduced-flavin transfer from SsuE to SsuD involves defined protein-protein interactions, while diffusional transfer can also occur under specified conditions.

## 3. Review of Existing GOA Annotations (4 IEA rows)
1. **`GO:0008752` (`FMN reductase [NAD(P)H] activity`, `enables`, IEA `GO_REF:0000002` from `InterPro:IPR020048`)** -> **`ACCEPT`**:
   - Core catalytic activity of SsuE (`NCBIfam:TIGR03567`, `InterPro:IPR020048`, `PANTHER:PTHR43408:SF1`). Because *P. putida* S-313 SsuE uses NADPH specifically in extract assays (PMID:10781557) whereas *E. coli* SsuE turns over both NADH and NADPH (PMID:10480865), and nicotinamide donor preference in *V. paradoxus* TBEA6 SsuE (`VPARA_09290`) has not been biochemically assayed, `GO:0008752` (`FMN reductase [NAD(P)H] activity`) is accepted at the warranted level of specificity.
2. **`GO:0016491` (`oxidoreductase activity`, `enables`, IEA `GO_REF:0000002` from `InterPro:IPR005025`)** -> **`TOO_GENERAL`**:
   - True but uninformative parent molecular function already entailed by the accepted child term `GO:0008752` (`FMN reductase [NAD(P)H] activity`).
3. **`GO:0046306` (`alkanesulfonate catabolic process`, `involved_in`, IEA `GO_REF:0000002` from `InterPro:IPR020048`)** -> **`ACCEPT`**:
   - Core pathway process in which SsuE (`VPARA_09290`, `KLN57918.1`) is co-encoded in the `ssuB2-ssuC5-ssuD-...-ssuA2-...-ssuE` cluster on contig `JZWI01000005` alongside `ssuB2` (`VPARA_09230`, `UniProtKB:A0A0H2MBB8`), `ssuC5` (`VPARA_09240`, `UniProtKB:A0A0H2M6G6`), `ssuD` (`VPARA_09250`, `UniProtKB:A0A0H2MCI3`), and `ssuA2` (`VPARA_09270`, `UniProtKB:A0A0H2M784`) and provides reduced $\text{FMNH}_2$ to SsuD (`VPARA_09250`).
4. **`GO:0052873` (`FMN reductase (NADPH) activity`, `enables`, IEA `GO_REF:0000003` from `EC:1.5.1.38`)** -> **`MARK_AS_OVER_ANNOTATED`**:
   - Over-specific nicotinamide cofactor assignment from `EC:1.5.1.38` mapping; NADPH vs NADH preference has not been experimentally assayed in *V. paradoxus* TBEA6 SsuE, and `GO:0008752` (`FMN reductase [NAD(P)H] activity`) is accepted as the core molecular function instead.

## 4. Proposed New Annotations
- **`GO:0005829` (`cytosol`, `located_in`, IC from `file:VARPD/ssuE/ssuE-uniprot.txt` and `PMID:10480865`)** -> **`NEW`**:
   - SsuE (`VPARA_09290`) is a 194-residue soluble cytoplasmic flavin reductase (`Pfam:PF03358`, residues `1..142`) lacking signal peptides or transmembrane helices that transfers reduced FMN to the cytosolic monooxygenase SsuD (`VPARA_09250`, `UniProtKB:A0A0H2MCI3`) in the cytosol (`GO:0005829`).
