# tpz1 (O14246) Curation Notes — *Schizosaccharomyces pombe* Shelterin Subunit Tpz1

## 1. Gene & Protein Overview

- **Organism & Identifiers**: *Schizosaccharomyces pombe* (strain 972 / ATCC 24843) `tpz1` (synonyms `mug169`, `SPAC6F6.16c`, `SPAC6F6.18c`; `UniProtKB:O14246`, sequence version 2, **508 aa**; `PANTHER:PTHR14487` / `PANTHER:PTHR14487:SF3` `ADRENOCORTICAL DYSPLASIA PROTEIN HOMOLOG`).
- **Nomenclature Warning**: Do NOT confuse *S. pombe* `tpz1` (`O14246`, the shelterin TPP1/ACD ortholog in `PTHR14487`) with *S. pombe* `tpp1` (`P78875`, trehalose-6-phosphate phosphatase) or `O74458` (`sfc4`, TFIIIC subunit).

## 2. Structural & Mechanistic Architecture of Tpz1 (`O14246`)

Tpz1 is the central architectural hub at the single-stranded/double-stranded junction of the *S. pombe* shelterin complex (`Taz1–Rap1–Poz1–Tpz1–Pot1` plus `Ccq1`) (`PMID:18535244`, `PMID:24013504`, `PMID:25330395`, `PMID:29149597`):

1. **N-terminal OB-fold domain (`aa 1–154`) and the fission-yeast TEL patch (`aa 73–81`, `TEKRITSLR`)**:
   - Like vertebrate ACD/TPP1, Tpz1 carries an N-terminal OB-fold preceded by a conserved hydrophobic `P8-W9-L10` sequence (`MSNCLKHPWLENGLLNLIK...`).
   - Although the surface charge diverged from the vertebrate acidic `DWEEKE` TEL patch to co-evolve with fission yeast telomerase reverse transcriptase Trt1, the structurally homologous OB-fold loop (`T73-E74-K75-R76-I77-T78-S79-L80-R81`) mediates **both** direct Trt1 recruitment to telomeres (`Ile77` and `Arg81` — `tpz1-R81E` causes an ever-shorter-telomere `EST` phenotype and abolishes Trt1 telomere recruitment, rescued by a `Trt1–Tpz1` fusion; `PMID:27253066`) **and** post-recruitment telomerase activation (`Lys75`, `Arg76`, `Thr78` — `tpz1-K75A` impairs telomere elongation despite Trt1 accumulation at telomeres; `PMID:25131669`).

2. **Pot1-binding domain (`aa 155–240`, `PDB:7CUI`; key residue `Ile200`)**:
   - Binds Pot1 (which directly recognizes the 3' G-rich single-stranded telomeric overhang). Separation-of-function mutation `tpz1-I200R` disrupts Tpz1–Pot1 binding and breaks the `Taz1–Rap1–Poz1–Tpz1–Pot1` shelterin bridge, causing runaway telomerase-dependent telomere elongation (`PMID:24013504`).

3. **Central SUMOylation & Stn1/Ten1 (CST) recruitment region (`aa 224–420`; SUMO acceptor `Lys242`)**:
   - Pli1-dependent SUMOylation of Tpz1 at `Lys242` (`tpz1-K242R` / `tpz1-Snm`) peaks in late S phase and recruits the `Stn1–Ten1` (CST) complex to telomeres to restrict telomerase action and promote lagging-strand synthesis (`PMID:24925530`).

4. **C-terminal Ccq1-binding (`aa 422–470`, `PDB:7CUJ`; key residue `Leu449`) and Poz1-binding (`aa 476–508`, `PDB:5WE0`/`5XXE`; key residues `Ile501`, `Arg505`) hooks**:
   - **Ccq1 binding (`Leu449`)**: Required both to switch telomeres out of the telomerase-nonextendible state (`PMID:24013504`) and to couple Rad3(ATR)/Tel1(ATM)-phosphorylated `Ccq1-Thr93–Est1` recruitment to `Tpz1(TEL-patch)–Trt1` engagement in late S phase (`PMID:22101932`, `PMID:25131669`, `PMID:25330395`, `PMID:27253066`), while redundantly protecting telomeres alongside Poz1 (`PMID:18535244`, `PMID:25330395`).
   - **Poz1 binding (`Ile501/Arg505`)**: Triggers an allosteric disorder-to-order transition in Poz1 that promotes Rap1 binding (`PMID:29149597`, `PMID:29160296`), completing the `Taz1–Rap1–Poz1–Tpz1–Pot1` shelterin bridge that defines the telomerase-nonextendible state (`GO:0032211` / `GO:1904357`; `PMID:24013504`, `PMID:25330395`).

## 3. Upstream Source Defect in UniProt `O14246` & Key Annotation Decisions

- **UniProt `CC:FUNCTION` defect (`WRONG_STATEMENT`)**:
  - `tpz1-uniprot.txt` begins `CC -!- FUNCTION: Telomeric DNA-binding protein that is required to protect the 3'-end telomeric overhang...`. However, `Pot1` is the subunit that directly binds the single-stranded 3' overhang, whereas `Tpz1` lacks intrinsic DNA-binding activity and instead binds `Pot1`, `Ccq1`, and `Poz1` (`PMID:18535244`, `PMID:24013504`, `PMID:25131669`). We record a `WRONG_STATEMENT` `source_defects` entry on `file:SCHPO/tpz1/tpz1-uniprot.txt` (`slot: CC:FUNCTION`).
- **GO Annotation Decisions (aligned with `genes/SCHPO/poz1/poz1-ai-review.yaml` and `PANTHER:PTHR14487`)**:
  - **`ACCEPT`**: `GO:0070187` (`shelterin complex`), `GO:0140445` (`chromosome, telomeric repeat region`), `GO:0016233` (`telomere capping`), `GO:0007004` (`telomere maintenance via telomerase`), `GO:1905324` (`telomere-telomerase complex assembly`).
  - **`MODIFY`**:
    - `GO:0005515` (`protein binding` IPI rows with Pot1, Ccq1, Poz1, Trt1) → `GO:0060090` (`molecular adaptor activity`) (or `GO:0070182` `DNA polymerase binding` for Trt1 IPI rows from `PMID:27253066`!).
    - `GO:0000781` (`chromosome, telomeric region`) → `GO:0140445` (`chromosome, telomeric repeat region`).
    - `GO:0000782` (`telomere cap complex`) & `GO:0000783` (`nuclear telomere cap complex`) → `GO:0070187` (`shelterin complex`).
    - `GO:0000723` (`telomere maintenance`) → `GO:0016233` (`telomere capping`) and `GO:0007004` (`telomere maintenance via telomerase`).
    - `GO:0032206` (`positive regulation of telomere maintenance`) → `GO:0032212` (`positive regulation of telomere maintenance via telomerase`).
  - **`KEEP_AS_NON_CORE`**: `GO:0005634` (`nucleus`).
  - **`REMOVE`**:
    - `GO:0005697` (`telomerase holoenzyme complex`, `IEA` `IPR019437`): Tpz1 is a shelterin subunit, not an integral telomerase holoenzyme subunit (`PMID:18535244`, `PMID:25131669`).
    - `GO:0042162` (`telomeric repeat DNA binding`, `IEA` `IPR019437`): Pot1 and Taz1 bind telomeric DNA directly, whereas Tpz1 is a protein–protein bridge (`PMID:18535244`, `PMID:24013504`).
  - **`NEW`**:
    - `GO:0060090` (`molecular adaptor activity`, `IPI`, `PMID:24013504`) — core shelterin bridge connecting Pot1, Poz1, and Ccq1.
    - `GO:0032212` (`positive regulation of telomere maintenance via telomerase`, `IMP`, `PMID:25131669`) — direct OB-fold TEL-patch activation of Trt1 after recruitment (`tpz1-K75A` / `tpz1-R81E`).
    - `GO:0032211` (`negative regulation of telomere maintenance via telomerase`, `IMP`, `PMID:24013504`) — Tpz1–Poz1 (`tpz1-I501R`), Tpz1–Pot1 (`tpz1-I200R`), and Tpz1-K242 SUMOylation (`PMID:24925530`) restrict telomerase-mediated telomere elongation.
