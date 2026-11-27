# Curation Notes: *Variovorax paradoxus* TBEA6 `czcD` (`A0A0H2M558`, `VPARA_15480`)

## 1. Gene & Protein Identity
- **Organism:** *Variovorax paradoxus* TBEA6 (`NCBITaxon:34073`)
- **UniProtKB Accession:** `A0A0H2M558` (`A0A0H2M558_VARPD`, unreviewed TrEMBL, 320 aa)
- **Gene Symbol / Locus Tag:** `czcD` / `VPARA_15480`
- **Family Classification:** Cation Diffusion Facilitator (CDF) family (`NCBIfam:TIGR01297`, `NCBIfam:NF033827` `CDF_efflux_DmeF`, `Pfam:PF01545` `Cation_efflux`, `InterPro:IPR002524`).

## 2. Sequence & Structural Verification (`UniProtKB:A0A0H2M558`)
1. **Six-Transmembrane-Helix CDF Topology:**
   - `FT TRANSMEM 28..47` (TM1)
   - `FT TRANSMEM 59..80` (TM2, carrying conserved intramembrane metal-binding Site A residues **`His59`** and **`His62`** in `59-HMSSHALA-66`)
   - `FT TRANSMEM 92..113` (TM3)
   - `FT TRANSMEM 125..148` (TM4)
   - `FT TRANSMEM 185..210` (TM5, carrying conserved intramembrane metal-binding Site A residues **`His188`** and **`Asp192`** in `188-HVVAD-192`)
   - `FT TRANSMEM 216..234` (TM6)
2. **Extraordinary 28-Residue Histidine-Rich Cytoplasmic Loop (IL2, Residues 152–179):**
   - Between TM4 and TM5 (`FT REGION 155..177`, `FT COMPBIAS 158..177 /note="Basic and acidic residues"`), `VPARA_15480` carries the sequence `152-HHHGHGHDHGHGHAHPHHEGHGHAHGHD-179`, which contains **15 histidine residues** (`His152, His153, His154, His156, His158, His160, His162, His164, His166, His168, His169, His172, His174, His176, His178`) and 3 acidic residues (`Asp159, Glu170, Asp179`), in addition to an N-terminal cytosolic histidine cluster (`2-HTHDLSAWQHDHH-14` containing `His2, His4, His11, His13, His14`).
3. **Comparative Biochemical & Genetic Evidence:**
   - In *Cupriavidus* (*Ralstonia*) *metallidurans* CH34, CzcD exports cytoplasmic $\text{Zn}^{2+}$, $\text{Co}^{2+}$, and $\text{Cd}^{2+}$ across the inner membrane, conferring basal divalent-cation resistance and attenuating expression of the periplasmic/outer-membrane `czcCBA` efflux pump [PMID:10559151 CzcD is a heavy metal ion transporter involved in regulation of heavy metal resistance in Ralstonia sp. strain CH34., "All three proteins mediated a small but significant resistance to cobalt, zinc, and cadmium in Ralstonia, and this resistance was based on a reduced accumulation of the cations. Thus, CzcD appeared to repress the Czc system by an export of the inducing cations."].
   - In *Pseudomonas putida*, CzcD is co-induced alongside CzcCBA1 and CzcCBA2 during zinc excess [PMID:27797207 Responses of Pseudomonas putida to Zinc Excess Determined at the Proteome Level: Pathways Dependent and Independent of ColRS., "We identified dozens of proteins that responded to zinc in a ColR-independent manner, among others, known metal efflux systems CzcCBA1, CzcCBA2, CadA2 and CzcD."].

## 3. Curation Decisions
- **Accepted:**
  - `GO:0005385` (`zinc ion transmembrane transporter activity`)
  - `GO:0071577` (`zinc ion transmembrane transport`)
  - `GO:0006882` (`intracellular zinc ion homeostasis`)
- **Modified:**
  - `GO:0016020` (`membrane`) $\rightarrow$ `GO:0005886` (`plasma membrane`)
- **Too General:**
  - `GO:0008324`, `GO:0046873` (subsumed by `GO:0005385`)
  - `GO:0006812`, `GO:0006829`, `GO:0030001`, `GO:0055085`, `GO:0098655` (subsumed by `GO:0071577`)
