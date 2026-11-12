# Curation Notes: VPARA_00520 (A0A0H2MPR3) in Variovorax paradoxus

## Overview
- **UniProt ID:** `A0A0H2MPR3` (`A0A0H2MPR3_VARPD`, 268 aa)
- **Gene symbol / locus tag:** `VPARA_00520` (`KLN58690.1`, `WP_021007649.1`)
- **Organism:** *Variovorax paradoxus* strain TBEA6 (`NCBITaxon:34073`)
- **Function:** Cytosolic polyphosphate kinase 2 (`PPK2`)-family phosphotransferase (`Pfam:PF03976`, `InterPro:IPR022300` `PPK2-rel_1`, `NCBIfam:TIGR03709`, `PANTHER:PTHR34383:SF3`).

## Domain Architecture & Subfamily Classification Conflict
- **Single-domain P-loop NTPase fold:** Contains the `PF03976` (`PPK2`) domain at residues 31–253 within a P-loop containing nucleoside triphosphate hydrolase fold (`Gene3D:3.40.50.300`, `InterPro:IPR027417`, `SUPFAM:SSF52540`) and carries a conserved Walker A P-loop motif (`GMDSSGK`, residues 65–71 in the `UniProtKB:A0A0H2MPR3` `SQ` sequence). PPK2 family enzymes catalyze phosphoryl transfer from inorganic polyphosphate to nucleotides and are grouped into three classes by nucleotide specificity ([PMID:31206993 "Polyphosphate kinase 2 (PPK2) transfer phosphate from inorganic polyphosphate to nucleotides. According to their activity, PPK2 enzymes are classified into three groups."], [PMID:31907778]).
- **Conflicting automated subfamily assignments (`ARBA` Class I vs. `PANTHER` Class II):**
  - UniProt `CC -!- SIMILARITY` (`ECO:0000256|ARBA:ARBA00009924`) labels `A0A0H2MPR3` as `Class I subfamily` (NDP-phosphorylating).
  - By contrast, `PANTHER:PTHR34383:SF3` labels it `POLYPHOSPHATE:AMP PHOSPHOTRANSFERASE` (Class II, AMP-phosphorylating), and `NCBIfam:TIGR03709` (`PPK2_rel_1`) / `InterPro:IPR022300` (`PPK2-rel_1`) separates it from the canonical Class I PA0141 subfamily (`NCBIfam:TIGR03707` / `InterPro:IPR022486`), which is represented in *V. paradoxus* TBEA6 by the paralog `VPARA_50220` (`A0A0H2LUF2`).
- **Distinct from `ppk` (`A0A0H2M4T4`):** Whereas `ppk` (`VPARA_28600`, `A0A0H2M4T4`) is a 710-aa `PPK1` enzyme (`IPR003414`) that synthesizes polyP from ATP via a phosphohistidine intermediate, `VPARA_00520` (`A0A0H2MPR3`) and `VPARA_50220` (`A0A0H2LUF2`) are paralogous `PF03976` PPK2-family phosphotransferases.
