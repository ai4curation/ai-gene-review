# Curation Notes for `tauA` (`VPARA_03650`, `A0A0H2M727`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Overview
- **UniProtKB Accession:** `A0A0H2M727` (`A0A0H2M727_VARPD`, unreviewed, 340 aa, 36,125 Da)
- **Gene Symbol / Locus Tag:** `tauA` / `VPARA_03650` (`EMBL:KLN58254.1` on genomic contig `JZWI01000003`, `RefSeq:WP_021006825.1`)
- **Organism:** *Variovorax paradoxus* strain TBEA6 (`NCBITaxon:34073`)
- **Genomic Context:** Encoded at the 5' end of the three-gene `tauA-tauB1-tauC` (`VPARA_03650-VPARA_03670`) taurine ABC importer operon on contig `JZWI01000003` (`KLN58254.1`, `KLN58255.1`, `KLN58256.1`). Note that in *V. paradoxus* TBEA6, the taurine dioxygenase `tauD1` (`VPARA_23370`, `A0A0H2MHV8`, `KLN56499.1` on contig `JZWI01000011`, curated in Tranche 2) is encoded at a separate genomic locus rather than immediately downstream of `tauC`.
- **Domain Architecture & Targeting:**
  - N-terminal Sec signal peptide at residues `1..30` (`FT SIGNAL 1..30`, `SAM:SignalP`), directing export to the periplasm.
  - Mature periplasmic substrate-binding domain (residues `31..340`): `NCBIfam:TIGR01729` (`tauA`, taurine-binding periplasmic protein), `InterPro:IPR010068` (`Taurine-bd_TauA`), `PANTHER:PTHR30024:SF47` (`TAURINE-BINDING PERIPLASMIC PROTEIN`), and periplasmic binding protein-like II superfamily (`InterPro:IPR028082`).

## 2. Literature & Comparative Evidence
- **[PMID:8808933](https://pubmed.ncbi.nlm.nih.gov/8808933/) (van der Ploeg et al. 1996, *J Bacteriol* 178:5438-5446):** Identified the sulfate-starvation-regulated `tauABCD` operon in *E. coli*, showing that disruption of these genes abolishes utilization of taurine as a sulfur source and that TauA carries a periplasmic signal peptide while TauB and TauC are the ATP-binding and membrane permease subunits of the taurine ABC uptake system.
- **[PMID:17203388](https://pubmed.ncbi.nlm.nih.gov/17203388/) (Javaux, Joris & De Witte 2007, *Protein J* 26:231-238):** Purified *E. coli* TauA and demonstrated high-affinity, high-specificity binding of taurine ($K_d = 11.3\text{ nM}$) at a single ligand-binding site (`"Measurement of K (d) value (mean 11.3 nM) by binding/dialysis studies revealed high affinity and specificity with taurine and also indicated that TauA possessed a unique binding site for its ligand."`).
- **[PMID:10781534](https://pubmed.ncbi.nlm.nih.gov/10781534/) (Eichhorn, van der Ploeg & Leisinger 2000, *J Bacteriol* 182:2687-2695):** In-frame deletion and complementation analysis of `tauABC` and `ssuABC` in *E. coli* demonstrated that the two ABC importers are complementary and their individual subunits are not functionally exchangeable.

## 3. Review of Existing GOA Annotations (2 IEA rows)
1. **`GO:0015734` (`taurine transmembrane transport`, `involved_in`, IEA `GO_REF:0000120` from `InterPro:IPR010068`, `PANTHER:PTN000559173`)** -> **`ACCEPT`**:
   - Core biological process mediated by TauA (`NCBIfam:TIGR01729`, `InterPro:IPR010068`, `PANTHER:PTHR30024:SF47`) as the periplasmic taurine-binding subunit of the TauAB1C importer.
2. **`GO:0030288` (`outer membrane-bounded periplasmic space`, `located_in`, IEA `GO_REF:0000120` from `InterPro:IPR010068`, `PANTHER:PTN000559173`)** -> **`ACCEPT`**:
   - Core subcellular localization supported by the N-terminal signal peptide (`FT SIGNAL 1..30`) and periplasmic binding protein family classification (`NCBIfam:TIGR01729`).

## 4. Proposed New Annotations
- **`GO:0030977` (`taurine binding`, `enables`, ISS from `PMID:17203388`)** -> **`NEW`**:
   - Purified bacterial TauA (`NCBIfam:TIGR01729`, `InterPro:IPR010068`, `PANTHER:PTHR30024:SF47`) binds taurine with high affinity ($K_d = 11.3\text{ nM}$) and specificity at a single periplasmic ligand-binding site (PMID:17203388), so `GO:0030977` (`taurine binding`) is added for TauA's intrinsic periplasmic ligand-capture activity, while its contribution to complex-level `GO:0015411` (`ABC-type taurine transporter transporter activity`) is recorded via `contributes_to_molecular_function` in `core_functions`.
- **`GO:0055052` (`ATP-binding cassette (ABC) transporter complex, substrate-binding subunit-containing`, `part_of`, IC from `file:VARPD/tauA/tauA-uniprot.txt` and `PMID:8808933`)** -> **`NEW`**:
   - TauA (`VPARA_03650`, `KLN58254.1`) is encoded immediately upstream of `tauB1` (`VPARA_03660`, `UniProtKB:A0A0H2MNF8`, `KLN58255.1`) and `tauC` (`VPARA_03670`, `UniProtKB:A0A0H2M7Y1`, `KLN58256.1`) on contig `JZWI01000003`, forming the periplasmic substrate-binding subunit of the TauABC importer complex (`GO:0055052`).
