# Curation Notes: *Variovorax paradoxus* TBEA6 `czcB` (`A0A0H2LX82`, `VPARA_44900`)

## 1. Gene & Protein Identity
- **Organism:** *Variovorax paradoxus* TBEA6 (`NCBITaxon:34073`)
- **UniProtKB Accession:** `A0A0H2LX82` (`A0A0H2LX82_VARPD`, unreviewed TrEMBL, 455 aa)
- **Gene Symbol / Locus Tag:** `czcB` / `VPARA_44900`
- **Genomic Context:** Middle gene of the syntenic tripartite HME-RND heavy-metal efflux operon `czcA3-czcB-czcC` (`VPARA_44890`–`VPARA_44910`) on contig `JZWI01000024`:
  - `VPARA_44890` (`czcA3`, `A0A0H2MBF7`, 1,067 aa): inner-membrane HME-RND proton/cation antiporter
  - `VPARA_44900` (`czcB`, `A0A0H2LX82`, 455 aa): periplasmic membrane-fusion protein (MFP) adaptor
  - `VPARA_44910` (`czcC`, `A0A0H2M0U4`, 445 aa): outer-membrane factor (OMF) efflux channel

## 2. Sequence & Structural Verification
- **Domain Architecture (`UniProtKB:A0A0H2LX82`):**
  - `FT TRANSMEM 18..36` (`18-WIAIAAVLVLGLGAGAMIL-36`): N-terminal inner-membrane anchor helix.
  - `FT REGION 41..121` / `FT COMPBIAS 45..121` (`Basic and acidic residues`): disordered periplasmic transition-metal-binding region containing **10 histidine residues** (`His54, His59, His60, His74, His76, His78, His84, His89, His90, His110`) and 24 acidic (`Asp`/`Glu`) residues (`51-AAAHGDGEHHEEGGKEAKEEGKDHDHGHGEAKGHADNEHHEKGKEKDKEEGKKKAATSEHKEDEEK-116`).
  - `FT DOMAIN 155..298` (`Pfam:PF25973` `BSH_CzcB`: CzcB-like barrel-sandwich hybrid domain)
  - `FT DOMAIN 194..253` (`Pfam:PF25893` `HH_CzcB`: CzcB-like alpha-helical hairpin domain)
  - `FT DOMAIN 301..376` (`Pfam:PF25954` `Beta-barrel_RND_2`: CusB-like beta-barrel domain)
  - `FT DOMAIN 383..443` (`Pfam:PF25975` `CzcB_C`: CzcB-like C-terminal circularly permuted SH3-like domain)
  - Full-length membership in `NCBIfam:TIGR01730` (`RND_mfp`) and `InterPro:IPR006143`.
- **Comparative Betaproteobacterial Evidence:**
  - In the fellow Burkholderiales bacterium *Cupriavidus* (*Ralstonia*) *metallidurans* CH34, CzcB forms a dimeric/hexameric periplasmic adaptor in the tripartite $\text{CzcCB}_2\text{A}$ cation-proton antiporter complex that exports $\text{Co}^{2+}$, $\text{Zn}^{2+}$, and $\text{Cd}^{2+}$ across the cell envelope [PMID:10559151 CzcD is a heavy metal ion transporter involved in regulation of heavy metal resistance in Ralstonia sp. strain CH34., "The Czc system of Ralstonia sp. strain CH34 mediates resistance to cobalt, zinc, and cadmium through ion efflux catalyzed by the CzcCB(2)A cation-proton antiporter."]; [PMID:12829273 Efflux-mediated heavy metal resistance in prokaryotes., "The mechanisms of action, physiological functions, and distribution of metal-exporting proteins are outlined, namely: CBA efflux pumps driven by proteins of the resistance-nodulation-cell division superfamily, P-type ATPases, cation diffusion facilitator and chromate proteins, NreB- and CnrT-like resistance factors."].

## 3. Curation Decisions
- **Accepted:**
  - `GO:0030288` (`outer membrane-bounded periplasmic space`)
  - `GO:0046914` (`transition metal ion binding`)
- **Modified:**
  - `GO:0016020` (`membrane`) $\rightarrow$ `GO:0005886` (`plasma membrane`)
  - `GO:0022857` (`transmembrane transporter activity`) $\rightarrow$ `GO:0015562` (`efflux transmembrane transporter activity`) and `GO:0008324` (`monoatomic cation transmembrane transporter activity`)
  - `GO:0055085` (`transmembrane transport`), `GO:0015679` (`plasma membrane copper ion transport`), and `GO:0060003` (`copper ion export`) $\rightarrow$ `GO:0098655` (`monoatomic cation transmembrane transport`)
- **Too General:**
  - `GO:0030313` (`cell envelope`) — subsumed by `GO:0030288` (`outer membrane-bounded periplasmic space`) and `GO:0005886` (`plasma membrane`).
