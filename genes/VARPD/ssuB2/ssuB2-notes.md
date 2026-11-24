# Curation Notes for `ssuB2` (`VPARA_09230`, `A0A0H2MBB8`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Overview
- **UniProtKB Accession:** `A0A0H2MBB8` (`A0A0H2MBB8_VARPD`, unreviewed, 276 aa, 29,405 Da)
- **Gene Symbol / Locus Tag:** `ssuB2` / `VPARA_09230` (`EMBL:KLN57912.1` on genomic contig `JZWI01000005`, `RefSeq:WP_021006427.1`)
- **Organism:** *Variovorax paradoxus* strain TBEA6 (`NCBITaxon:34073`)
- **Genomic Context:** Encoded at the 5' end of the aliphatic sulfonate uptake and desulfonation gene cluster on contig `JZWI01000005` immediately upstream of `ssuC5` (`VPARA_09240`, `KLN57913.1`) and `ssuD` (`VPARA_09250`, `KLN57914.1`), with `ssuA2` (`VPARA_09270`, `KLN57916.1`) and `ssuE` (`VPARA_09290`, `KLN57918.1`) immediately downstream.
- **Domain Architecture & Key Motifs:**
  - ABC transporter ATP-binding domain (`PROSITE:PS50893`, `Pfam:PF00005`, `InterPro:IPR003439`, residues `19..240`).
  - PANTHER subfamily `PTHR42788:SF17` (`ALIPHATIC SULFONATES IMPORT ATP-BINDING PROTEIN SSUB`) and `InterPro:IPR005893` (`Lipoprotein_rel_SsuB`).
  - Conserved Walker A / P-loop nucleotide-binding motif at residues `51..58` (`51-GRSGCGKS-58`, `FT BINDING 51..58 /ligand="ATP"`).

## 2. Literature & Comparative Evidence
- **[PMID:10781534](https://pubmed.ncbi.nlm.nih.gov/10781534/) (Eichhorn, van der Ploeg & Leisinger 2000, *J Bacteriol* 182:2687-2695):** Deletion and complementation analysis of the *E. coli* `ssuEADCB` and `tauABCD` clusters demonstrated that SsuABC mediates aliphatic sulfonate uptake and that its subunits cannot form functional hybrid transporters with TauABC.
- **[PMID:10781557](https://pubmed.ncbi.nlm.nih.gov/10781557/) (Kahnert et al. 2000, *J Bacteriol* 182:2869-2878):** Identified `ssuA`, `ssuB`, and `ssuC` in *P. putida* S-313 as the three subunits of the ABC-type sulfonate transporter (`"The first group consists of ssuA , ssuB , and ssuC , which are the genes for a putative ATP-binding cassette (ABC)-type transport system."`).

## 3. Review of Existing GOA Annotations (3 IEA rows)
1. **`GO:0005524` (`ATP binding`, `enables`, IEA `GO_REF:0000120` from `PROSITE-ProRule:PRU00434`, `InterPro:IPR003439`, `UniRule:UR000078916`)** -> **`ACCEPT`**:
   - Core cofactor/substrate-binding activity of the ABC nucleotide-binding domain (`PROSITE:PS50893`, residues `19..240`), supported by the conserved Walker A motif `51-GRSGCGKS-58` (`FT BINDING 51..58`).
2. **`GO:0016887` (`ATP hydrolysis activity`, `enables`, IEA `GO_REF:0000120` from `InterPro:IPR003439`, `PANTHER:PTN002531750`, `UniRule:UR000078916`)** -> **`ACCEPT`**:
   - Core intrinsic catalytic activity of the SsuB2 ABC ATPase subunit, which hydrolyzes ATP to energize conformational cycling of the SsuC5 transmembrane permease.
3. **`GO:0055085` (`transmembrane transport`, `involved_in`, IEA `GO_REF:0000118` from `PANTHER:PTN002531750`)** -> **`MODIFY` to `GO:0042918` (`alkanesulfonate transmembrane transport`)**:
   - Following the `PSEPK/ssuB` comparator convention, `GO:0055085` is true but overly general; membership in `PANTHER:PTHR42788:SF17` (`ALIPHATIC SULFONATES IMPORT ATP-BINDING PROTEIN SSUB`) and syntenic co-localization with `ssuC5` (`VPARA_09240`), `ssuD` (`VPARA_09250`), `ssuA2` (`VPARA_09270`), and `ssuE` (`VPARA_09290`) on contig `JZWI01000005` support refining the biological process to `GO:0042918` (`alkanesulfonate transmembrane transport`).

## 4. Proposed New Annotations
- **`GO:0005886` (`plasma membrane`, `located_in`, IC from `file:VARPD/ssuB2/ssuB2-uniprot.txt`)** -> **`NEW`**:
   - As the cytoplasmic-face peripheral inner-membrane ATPase subunit (`CC -!- SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000256|ARBA:ARBA00004190, ECO:0000256|RuleBase:RU363044}; Peripheral membrane protein`) associated with the integral inner-membrane permease SsuC5, SsuB2 localizes to the plasma membrane (`GO:0005886`).
- **`GO:0055052` (`ATP-binding cassette (ABC) transporter complex, substrate-binding subunit-containing`, `part_of`, IC from `file:VARPD/ssuB2/ssuB2-uniprot.txt`)** -> **`NEW`**:
   - SsuB2 (`VPARA_09230`, `KLN57912.1`) assembles with the permease `ssuC5` (`VPARA_09240`, `KLN57913.1`) and periplasmic binding protein `ssuA2` (`VPARA_09270`, `KLN57916.1`) into the SsuABC importer complex (`GO:0055052`) and contributes to complex-level `GO:0042959` (`ABC-type alkanesulfonate transporter transporter activity`).
