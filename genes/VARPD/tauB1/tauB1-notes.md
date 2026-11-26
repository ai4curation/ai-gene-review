# Curation Notes for `tauB1` (`VPARA_03660`, `A0A0H2MNF8`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Overview
- **UniProtKB Accession:** `A0A0H2MNF8` (`A0A0H2MNF8_VARPD`, unreviewed, 262 aa, 28,284 Da)
- **Gene Symbol / Locus Tag:** `tauB1` / `VPARA_03660` (`EMBL:KLN58255.1` on genomic contig `JZWI01000003`, `RefSeq:WP_021006826.1`)
- **Organism:** *Variovorax paradoxus* strain TBEA6 (`NCBITaxon:34073`)
- **Genomic Context:** Encoded as the middle gene of the three-gene `tauA-tauB1-tauC` (`VPARA_03650-VPARA_03670`) taurine ABC importer operon on contig `JZWI01000003` (`KLN58254.1`, `KLN58255.1`, `KLN58256.1`).
- **Domain Architecture & Key Motifs:**
  - ABC transporter ATP-binding domain (`PROSITE:PS50893`, `Pfam:PF00005`, `InterPro:IPR003439`, residues `6..235`).
  - Specific subfamily: `PANTHER:PTHR42788:SF18` (`TAURINE IMPORT ATP-BINDING PROTEIN TAUB`), `InterPro:IPR005889` (`TauB`).
  - Conserved Walker A / P-loop ATP-binding motif at residues `40..47` (`40-GASGCGKT-47`, `FT BINDING 40..47 /ligand="ATP"`).

## 2. Literature & Comparative Evidence
- **[PMID:8808933](https://pubmed.ncbi.nlm.nih.gov/8808933/) (van der Ploeg et al. 1996, *J Bacteriol* 178:5438-5446):** Identified `tauB` within the *E. coli* `tauABCD` operon as the ATP-binding subunit of the taurine ABC uptake system required for utilizing taurine as a sulfur source.
- **[PMID:10781534](https://pubmed.ncbi.nlm.nih.gov/10781534/) (Eichhorn, van der Ploeg & Leisinger 2000, *J Bacteriol* 182:2687-2695):** In-frame deletion and complementation analysis in *E. coli* confirmed that `tauABC` is required for taurine uptake and its subunits cannot form functional hybrid transporters with `ssuABC`.

## 3. Review of Existing GOA Annotations (3 IEA rows)
1. **`GO:0005524` (`ATP binding`, `enables`, IEA `GO_REF:0000120` from `PROSITE-ProRule:PRU00434`, `InterPro:IPR003439`, `UniRule:UR000078649`)** -> **`ACCEPT`**:
   - Core nucleotide-binding activity of the ABC ATPase domain (`PROSITE:PS50893`, residues `6..235`), anchored by the Walker A motif `40-GASGCGKT-47` (`FT BINDING 40..47`).
2. **`GO:0016887` (`ATP hydrolysis activity`, `enables`, IEA `GO_REF:0000120` from `InterPro:IPR003439`, `PANTHER:PTN002531845`, `UniRule:UR000078649`)** -> **`ACCEPT`**:
   - Core intrinsic catalytic activity of the TauB1 subunit, which hydrolyzes ATP to power conformational cycling of the TauC transmembrane permease.
3. **`GO:0055085` (`transmembrane transport`, `involved_in`, IEA `GO_REF:0000118` from `PANTHER:PTN002531845`)** -> **`MODIFY` to `GO:0015734` (`taurine transmembrane transport`)**:
   - Following the `PSEPK/tauB` comparator convention, `GO:0055085` is true but general; membership in `PANTHER:PTHR42788:SF18` (`TAURINE IMPORT ATP-BINDING PROTEIN TAUB`), `InterPro:IPR005889` (`TauB`), and syntenic placement between `tauA` (`VPARA_03650`, `KLN58254.1`) and `tauC` (`VPARA_03670`, `KLN58256.1`) on contig `JZWI01000003` support refinement to `GO:0015734` (`taurine transmembrane transport`).

## 4. Proposed New Annotations
- **`GO:0005886` (`plasma membrane`, `located_in`, IC from `file:VARPD/tauB1/tauB1-uniprot.txt`)** -> **`NEW`**:
   - Peripheral inner-membrane ATP-coupling subunit (`CC -!- SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000256|ARBA:ARBA00004190, ECO:0000256|RuleBase:RU363042}; Peripheral membrane protein`) bound to the cytoplasmic face of the TauC transmembrane permease at the plasma membrane (`GO:0005886`).
- **`GO:0055052` (`ATP-binding cassette (ABC) transporter complex, substrate-binding subunit-containing`, `part_of`, IC from `file:VARPD/tauB1/tauB1-uniprot.txt` and `PMID:8808933`)** -> **`NEW`**:
   - TauB1 (`VPARA_03660`, `KLN58255.1`) assembles with `tauA` (`VPARA_03650`, `KLN58254.1`) and `tauC` (`VPARA_03670`, `KLN58256.1`) into the TauABC importer complex (`GO:0055052`), contributing to complex-level `GO:0015411` (`ABC-type taurine transporter transporter activity`).
