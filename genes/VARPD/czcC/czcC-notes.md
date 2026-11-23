# Curation Notes: *Variovorax paradoxus* TBEA6 `czcC` (`A0A0H2M0U4`, `VPARA_44910`)

## 1. Gene & Protein Identity
- **Organism:** *Variovorax paradoxus* TBEA6 (`NCBITaxon:34073`)
- **UniProtKB Accession:** `A0A0H2M0U4` (`A0A0H2M0U4_VARPD`, unreviewed TrEMBL, 445 aa)
- **Gene Symbol / Locus Tag:** `czcC` / `VPARA_44910`
- **Genomic Context:** Terminal gene of the syntenic tripartite HME-RND heavy-metal efflux operon `czcA3-czcB-czcC` (`VPARA_44890`–`VPARA_44910`) on contig `JZWI01000024`.

## 2. Sequence & Structural Verification
- **Domain Architecture (`UniProtKB:A0A0H2M0U4`):**
  - `FT SIGNAL 1..20` (`1-MRTLFVPLALLALAAPPAFS-20`, `ECO:0000256|SAM:SignalP`): N-terminal Sec signal peptide cleaved after `Ser20`.
  - `FT CHAIN 21..445` (`PRO_5002596506`, mature 425-aa outer-membrane channel subunit starting at `Gln21`).
  - `DR Pfam; PF02321; OEP; 2.` (two Outer Membrane Efflux Protein structural repeats, `Gene3D:1.20.1600.10`, `SUPFAM:SSF56954`, `InterPro:IPR003423` `OMP_efflux`, `InterPro:IPR010131` `MdtP/NodT-like`).
  - `DR PANTHER; PTHR30203; OUTER MEMBRANE CATION EFFLUX PROTEIN; 1.`
  - `FT COILED 326..371`: periplasmic alpha-helical barrel coiled-coil segment that docks with the periplasmic adaptor CzcB (`VPARA_44900`).
- **Role in the Tripartite $\text{CzcCB}_2\text{A}$ Complex:**
  - In *Cupriavidus* (*Ralstonia*) *metallidurans* CH34 and related Burkholderiales, CzcC forms the outer-membrane TolC-like channel of the tripartite $\text{CzcCB}_2\text{A}$ cation-proton antiporter complex, enabling direct extrusion of $\text{Co}^{2+}$, $\text{Zn}^{2+}$, and $\text{Cd}^{2+}$ across the outer membrane into the extracellular medium [PMID:10559151 CzcD is a heavy metal ion transporter involved in regulation of heavy metal resistance in Ralstonia sp. strain CH34., "The Czc system of Ralstonia sp. strain CH34 mediates resistance to cobalt, zinc, and cadmium through ion efflux catalyzed by the CzcCB(2)A cation-proton antiporter."]; [PMID:12829273 Efflux-mediated heavy metal resistance in prokaryotes., "The mechanisms of action, physiological functions, and distribution of metal-exporting proteins are outlined, namely: CBA efflux pumps driven by proteins of the resistance-nodulation-cell division superfamily, P-type ATPases, cation diffusion facilitator and chromate proteins, NreB- and CnrT-like resistance factors."].

## 3. Curation Decisions
- **Accepted:** `GO:0015562` (`efflux transmembrane transporter activity`).
- **Modified:**
  - `GO:0016020` (`membrane`) $\rightarrow$ `GO:0009279` (`cell outer membrane`)
  - `GO:0022857` (`transmembrane transporter activity`) $\rightarrow$ `GO:0015562` (`efflux transmembrane transporter activity`) and `GO:0008324` (`monoatomic cation transmembrane transporter activity`)
  - `GO:0055085` (`transmembrane transport`) $\rightarrow$ `GO:0098655` (`monoatomic cation transmembrane transport`)
