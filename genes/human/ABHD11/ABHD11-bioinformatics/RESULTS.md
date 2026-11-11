# PTHR46118 (PROTEIN ABHD11) Phylogeny, Active-Site Conservation, and Coordinate Crosswalk

## 1. PANTHER 19.0 Family and Subfamily Architecture (`PANTHER:PTHR46118`)

- **Official family name**: `PROTEIN ABHD11` (`PANTHER:PTHR46118`)
- **Subfamilies**:
  - `PANTHER:PTHR46118:SF4` (`PROTEIN ABHD11`, clade node `PANTHER:PTN008704070` at `LUCA`): Trans-kingdom subfamily spanning both eukaryotic mitochondrial orthologs/paralogs (`PTN002919262` `Eukaryota` -> `PTN000106239` `Unikonts`) and bacterial cytoplasmic esterases (`PTN008704081` `Eubacteria`: *Escherichia coli* K-12 `ybfF` `UniProtKB:P75736`, *Salmonella enterica* serovar Typhimurium LT2 `ybfF` `UniProtKB:Q8ZQX0`, and *Haemophilus influenzae* `HI_0193` `UniProtKB:Q57427`).
  - `PANTHER:PTHR46118:SF3` (`AB HYDROLASE-1 DOMAIN-CONTAINING PROTEIN`, clade node `PANTHER:PTN002251067` at `Caenorhabditis`): Nematode lineage-specific duplicate `abhd-11.1` (`UniProtKB:O62202`), sister to `SF4` `abhd-11.2` (`UniProtKB:O45707`) below nematode duplication `PANTHER:PTN002251066`.
  - `PANTHER:PTHR46118:SF5` (`AB HYDROLASE-1 DOMAIN-CONTAINING PROTEIN`, clade node `PANTHER:PTN000862953` at `Dictyostelium`): Amoebozoan duplicate `DDB_G0283799` (`UniProtKB:Q54QK2`), sister to `SF4` `DDB_G0278415` (`UniProtKB:Q54Y48`) below amoebozoan duplication `PANTHER:PTN002251098`.

## 2. Verified 1-Based Catalytic Triad and Oxyanion-Hole Alignment Across PTHR46118 Members

Structural alignment against the 1.1-A crystal structure of *Escherichia coli* K-12 YbfF (`UniProtKB:P75736`, `PDB:3BF7`, `PMID:18215690`) and experimentally mapped active-site residues of yeast Eat1 (`UniProtKB:P53208`, `FT ACT_SITE 115 / 139 / 302`) and human ABHD11 (`UniProtKB:Q8NFV4`, `sv=2`, 306 aa) identifies the canonical alpha/beta-hydrolase catalytic triad at beta-5 (`GxSxG` nucleophilic elbow), beta-6 (`Asp`/`Glu` charge-relay acid), and the beta-8-alpha-F loop (`His` general base):

| Accession | Gene | Organism | Subfamily | Length (sv) | Oxyanion Motif | Nucleophile (1-based) | Beta-6 Acid (1-based) | General-Base His (1-based) | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `UniProtKB:Q8NFV4` | `ABHD11` | *Homo sapiens* | `PTHR46118:SF4` | 306 (`sv=2`) | `65-HGLGG-69` | `Ser132` (`VVGHSMGGK`) | `Asp156` (`LIAVDISPV`) | `His287` (`PNAGHWIHA`) | Active glutaryl-lipoyl thioesterase / esterase |
| `UniProtKB:Q8K4F5` | `Abhd11` | *Mus musculus* | `PTHR46118:SF4` | 307 (`sv=1`) | `66-HGLGG-70` | `Ser133` (`VVGHSMGGK`) | `Asp157` (`LIAVDISPV`) | `His288` (`PNASHWIHA`) | Active mitochondrial matrix ortholog |
| `UniProtKB:A0A8I6AS56` | `Abhd11` | *Rattus norvegicus* | `PTHR46118:SF4` | 342 (`sv=1`) | `101-HGLGG-105` | `Ser168` (`VVGHSMGGK`) | `Asp192` (`LIAVDISPV`) | `His323` (`PNASHWIHA`) | Active mitochondrial matrix ortholog |
| `UniProtKB:Q6DRD9` | `abhd11` | *Danio rerio* | `PTHR46118:SF4` | 317 (`sv=1`) | `76-HGLGG-80` | `Ser142` (`LIGHSMGGK`) | `Asp166` (`LIAVDISPV`) | `His297` (`PNAGHWIHA`) | Active mitochondrial matrix ortholog |
| `UniProtKB:Q9W3R8` | `CG2059` | *Drosophila melanogaster* | `PTHR46118:SF4` | 308 (`sv=1`) | `60-HGLGG-64` | `Ser127` (`LLGHSMGGK`) | `Asp151` (`IITIDISPS`) | `His286` (`PKAGHWIHA`) | Active serine carboxylesterase (`PTN000106319`) |
| `UniProtKB:Q9VGJ4` | `CG14717` | *Drosophila melanogaster* | `PTHR46118:SF4` | 306 (`sv=1`) | `50-HDLNL-54` | `Gly120` (`ALGHGMGGR`) | `Asp144` (`ILAIDVCPV`) | `His282` (`RNAGHWVHA`) | Non-catalytic pseudoenzyme (`Ser->Gly120`, `PTN002451174`) |
| `UniProtKB:O45707` | `abhd-11.2` | *Caenorhabditis elegans* | `PTHR46118:SF4` | 299 (`sv=2`) | `54-HGLGG-58` | `Ser124` (`LIGHSMGGK`) | `Asp150` (`VVAVDISPA`) | `His279` (`PDAGHWVHA`) | Active catalytic triad intact |
| `UniProtKB:O62202` | `abhd-11.1` | *Caenorhabditis elegans* | `PTHR46118:SF3` | 297 (`sv=1`) | `44-HGLGG-48` | `Ser114` (`LIGHSMGGK`) | `Asp140` (`IVAVDISPA`) | `His267` (`PKCGHWIHS`) | Active catalytic triad intact |
| `UniProtKB:P53219` | `IMO32` | *Saccharomyces cerevisiae* | `PTHR46118:SF4` | 342 (`sv=1`) | `82-HGLGG-86` | `Ser152` (`IIGHSMGGK`) | `Glu176` (`LVCIENAPV`) | `His319` (`PRAGHWVHA`) | Active mitochondrial matrix alpha/beta-hydrolase |
| `UniProtKB:P53208` | `EAT1` | *Saccharomyces cerevisiae* | `PTHR46118:SF4` | 328 (`sv=1`) | `46-HGLGA-50` | `Ser115` (`ILGHSMGGK`) | `Asp139` (`IIGIDVPPV`) | `His302` (`PNAGHWIQA`) | Active mitochondrial ethanol O-acetyltransferase / thioesterase / esterase |
| `UniProtKB:O94437` | `SPAC22H12.03` | *Schizosaccharomyces pombe* | `PTHR46118:SF4` | 270 (`sv=1`) | `28-HGLGG-32` | `Ser95` (`LVGHSMGGK`) | `Asp119` (`LIAIDISPV`) | `His250` (`PKAGHYIHA`) | Active mitochondrial alpha/beta-hydrolase |
| `UniProtKB:P75736` | `ybfF` | *Escherichia coli* K-12 | `PTHR46118:SF4` | 254 (`sv=1`) | `22-HGLFG-26` | `Ser89` (`LVGHSLGGL`) | `Asp113` (`LIAVDISPA`) | `His234` (`PQAGHAAVH`) | Active bacterial cytoplasmic acyl-CoA/pNP esterase (no mitochondria) |
| `UniProtKB:Q8ZQX0` | `ybfF` | *Salmonella typhimurium* LT2 | `PTHR46118:SF4` | 256 (`sv=1`) | `22-HGLFG-26` | `Ser89` (`LVGHSLGGL`) | `Asp113` (`LIAVDISPA`) | `His234` (`PAAGHAAVH`) | Bacterial cytoplasmic esterase (no mitochondria) |
| `UniProtKB:Q57427` | `HI_0193` | *Haemophilus influenzae* Rd | `PTHR46118:SF4` | 287 (`sv=1`) | `51-HGLGG-55` | `Ser119` (`LLGHSMGGK`) | `Asp143` (`LIAVDISPV`) | `His266` (`PKAGHWVHA`) | Bacterial cytoplasmic esterase (no mitochondria) |
| `UniProtKB:Q54QK2` | `DDB_G0283799` | *Dictyostelium discoideum* | `PTHR46118:SF5` | 365 (`sv=1`) | `89-HGLGG-93` | `Ser158` (`LVGHSLGGK`) | `Asp182` (`IISVDISPS`) | `His314` (`PNASHWIHF`) | Active catalytic triad intact |

Note on beta-6 vs beta-7 acidic residue: UniProt `Q8NFV4` (`FT ACT_SITE 228`), `Q8K4F5` (`229`), `Q6DRD9` (`238`), and `O94437` (`190`) carry an automated `ECO:0000250` homology projection on beta-7, whereas the high-resolution *E. coli* YbfF crystal structure (`PDB:3BF7`, `PMID:18215690`) and *S. cerevisiae* Eat1 (`FT ACT_SITE 139`) establish the conserved beta-6 aspartate/glutamate (`Asp156` in human `Q8NFV4`, `Asp113` in `P75736`, `Asp139` in `P53208`, `Glu176` in `P53219`) as the structural triad acid; the beta-7 position is non-acidic in `P53208` (`Thr204`), `P53219` (`Val239`), and `P75736` (`Val162`).

## 3. Human `ABHD11` (`UniProtKB:Q8NFV4`) Sequence Version and Isoform Coordinate Crosswalk

- **`Q8NFV4` `sv=1` (historical 315-aa canonical precursor used in `PMID:32792488` and `PMID:40664791`)**: Contained a 9-residue N-terminal translation-initiation extension (`SEQUENCE CAUTION` in `ABHD11-uniprot.txt`); catalytic nucleophile numbered `Ser141`, beta-6 acid `Asp165`, and catalytic histidine `His296` (`S141A` and `H296A` mutants in `PMID:32792488` and `PMID:40664791`).
- **`Q8NFV4` `sv=2` (current 306-aa canonical isoform 1 `Q8NFV4-1`)**: 9-aa N-terminal artifact trimmed (`-9` shift relative to `sv=1`); catalytic triad at `Ser132`, `Asp156`, and `His287` (`FT ACT_SITE 132`, `FT ACT_SITE 287`, `FT MUTAGEN 132`, `FT MUTAGEN 287` in `ABHD11-uniprot.txt`).
- **`Q8NFV4-4` (`sv=2` 299-aa isoform 4; historically 308-aa isoform 2/D lacking `VAR_SEQ 42..48`, `-7` shift relative to `Q8NFV4-1`)**: Lacks 7 residues in the N-terminal presequence/disordered region (`Ser125`, `Asp149`, `His280` in `sv=2`; `Ser134`, `His289` in historical 308-aa numbering). Used as the yeast two-hybrid ORF clone in HuRI (`PMID:32296183`).
- **Recombinant mature human ABHD11 (`residues 37..306` of `sv=2` / `46..315` of `sv=1`, 270 aa used in `PMID:32579589`)**: Lacks the 36-aa N-terminal mitochondrial transit peptide (`-36` shift relative to `Q8NFV4-1` `sv=2`), numbering the nucleophile `Ser96` and histidine `His251`.
