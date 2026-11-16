# Curation Notes for Human `ARID4B` (`UniProtKB:Q4LE39`)

## 1. Gene Identity & Phylogenetic Context (`PANTHER:PTHR13964:SF24`)
- **Organism**: *Homo sapiens* (`NCBITaxon:9606`)
- **HGNC / Gene Symbol**: `HGNC:15550` / `ARID4B` (*AT-rich interactive domain 4B*; aliases `RBP1L1`, `RBBP1L1`, `SAP180`, `BCAA`, `BRCAA1`).
- **UniProtKB**: `Q4LE39` (1312 aa, sequence version 2; 4 splice isoforms `Q4LE39-1`..`Q4LE39-4`).
- **PANTHER Family / Subfamily**: `PANTHER:PTHR13964` (`RBP-RELATED`) / `PANTHER:PTHR13964:SF24` (`AT-RICH INTERACTIVE DOMAIN-CONTAINING PROTEIN 4B`).

## 2. Structural & Mechanistic Synthesis (`Q4LE39`, 1312 aa)
1. **mSin3A-HDAC1 Corepressor Subunit (`SAP180`) Lacking the `LXCXE` RB1-Binding Motif**:
   - Fleischer et al. 2003 (`PMID:12724404`) purified `SAP180` (`ARID4B`) as a stoichiometric subunit of the human `mSin3A` histone deacetylase corepressor complex in K562 cells, mapping two repression domains: a C-terminal R2 domain binding the `mSin3A` HDAC-interaction domain (`HID`) and an N-terminal mSin3A/HDAC-independent repression domain (`GO:0070822`, `GO:0000122`).
   - Unlike paralog `ARID4A` (`957-LVCHE-961`), `ARID4B` lacks a canonical `LXCXE` retinoblastoma pocket-binding motif and interacts with RB1 pathways indirectly via heteromeric assembly with `ARID4A` (`PMID:17043311`, `PMID:23487765`).
   - Terzi Cizmecioglu et al. 2020 (`PMID:33454011`) demonstrated that within mESC `SIN3A` complexes, `ARID4B` physically and functionally partners selectively with `HDAC1` rather than `HDAC2` to execute mesodermal/endodermal gene expression programs at pluripotency exit; Winter et al. 2012 (`PMID:22693453`) showed polymorphic binding to `mSIN3A`, `mSDS3`, and `BRMS1`.
2. **Interdigitated Double Tudor (`Glu50`) & Sequence-Nonspecific ARID dsDNA Binding**:
   - Ren et al. 2021 (`PMID:33675746`, `PDB:6LWB`) solved the solution NMR structure of the `ARID4B` N-terminal interdigitated double Tudor domain (`aa 4-121`), showing that it binds dsDNA electrostatically without sequence preference (`GO:0003677`); substitution `Glu50` (versus `Leu50` in `ARID4A`) forms intramolecular salt bridges that attenuate core Tudor DNA affinity while increasing stability, compensated by a conserved positively charged C-terminal disordered `RGR` extension.
   - Its central ARID domain (`Gly324` in `323-RGTPI-327`, core `Trp362`, `Ser376` in place of ARID5 `Thr388`) likewise lacks the vertebrate ARID5 major-groove AT-selective motif (`PMID:15640446`).
3. **Context-Dependent Chromatin Activation (Androgen Receptor Coactivation & Linker Histone H1 Antagonism)**:
   - Together with `ARID4A`, `ARID4B` maintains maternal imprinting (`H3K9me3`/`H4K20me3`/DNA methylation) at the *Snrpn* PWS/AS imprinting center (`PMID:17043311`) and suppresses myeloid leukemogenesis (`PMID:18728284`).
   - In Sertoli cells (`PMID:23487765`, `PMID:26258622`, `PMID:28207192`), `ARID4B` acts as an essential coactivator of the androgen receptor (`AR`) at `Rhox5` and stem-cell niche effectors (`Gja1`, `Kitl`, `Gdnf`, `Cyp26b1`).
   - In `PTEN`-deficient prostate cancer (`PMID:31551414`), `ARID4B` binds the `PIK3CA` and `PIK3R2` promoters and activates their transcription by reciprocally excluding linker histone H1 to relax chromatin condensation — explicitly **without** intrinsic acetyltransferase/methyltransferase activity and without altering promoter `H3K27ac`, `H4ac`, or `H3K4me3`.
4. **Subcellular Localization Nuance**:
   - Endogenous nuclear/chromatin function is firmly established (`GO:0005634`, `GO:0005654`), whereas cytoplasmic epitope staining (`GO:0005737`, `GO:0005829`) was reported in breast carcinoma (`MCF-7`) cells using anti-`RBP1L1`/`BRCAA1` sera (`PMID:11481388`, `PMID:15247124`) and HPA immunofluorescence (`GO_REF:0000052`).

## 3. Audit of `ARID4B-deep-research-affinage.md`
- Frontmatter: `uniprot_accession: Q4LE39` (matches), `self_evaluation_pairwise: win`, `faith_pct: 100.0`, `citation_count: 16`.
- **Verdict**: `relevance: HIGH`, `correctness: LOW_QUALITY` (2 structured `source_defects` recorded):
  1. **`WRONG_STATEMENT` (`slot: current_model`, `requested_change: CHECK`, `cause: SPECULATION_AS_ASSERTION`)**: Falsely asserts in the mechanistic narrative that `"In cancer, ARID4B binds directly to the promoters of PI3K pathway genes — PIK3CA, PIK3R2, and mTOR — where it competes with histone H1 to modulate chromatin condensation and deposits activating H3K27ac, thereby driving PI3K/AKT/mTOR signaling"`, inventing an enzymatic histone acetyltransferase ("deposits activating H3K27ac") function for non-enzymatic `ARID4B` that is directly refuted by `PMID:31551414` (`"ChIP-qPCR analyses showed that ablation of ARID4B increased binding of histone H1 to the PIK3CA and PIK3R2 promoters (Fig. 2d) without affecting histone H4 acetylation (H4Ac), H3 lysine 27 acetylation (H3K27Ac), or H3 lysine 4 trimethylation (H3K4me3)"`).
  2. **`MISSING_STATEMENT` (`slot: citations`, `requested_change: ADD`)**: Omits both the foundational biochemical purification of `SAP180`/`ARID4B` as a core `mSin3A` corepressor subunit with two repression domains (`PMID:12724404`) and the structural/biochemical characterization of human `ARID4B` Tudor-domain dsDNA binding (`PMID:33675746`).

## 4. Existing Annotation Decisions (21 Existing Rows + 1 `NEW` Row)
- **`NEW` `GO:0003714` (`transcription corepressor activity`, `IDA` from `PMID:12724404`)**: Added to capture the directly assayed transcriptional corepressor activity of human `SAP180`/`ARID4B` via its C-terminal `mSin3A`-binding and N-terminal `mSin3A`-independent repression domains (`PMID:12724404`).
- **`GO:0000976` (`IBA` from `PTN000359478`) -> `REMOVE` (`PROPAGATION_BAD`)**: Over-propagated from `ARID5B`; `ARID4B` lacks the ARID5 major-groove AT-recognition motif (`Ser376` vs `Thr388`) and binds dsDNA non-specifically (`PMID:15640446`, `PMID:33675746`).
- **`GO:0005515` (`protein binding`, `IPI` with `ETS1` `UniProtKB:P14921` from `PMID:20195357`) -> `REMOVE`** per `protein_binding_policy.py` (uninformative bare protein binding from an mRNA-display fragment screen).
- **ComplexPortal-style `FAM60A` `NAS` rows (`GO:0030336`, `GO:0030512` from `PMID:22984288`; `GO:1902455`, `GO:1902459` from `PMID:28554894`) -> `MARK_AS_OVER_ANNOTATED`**: Same `FAM60A`/`SIN3` subunit guilt-by-association over-annotation as on `ARID4A` (notably `PMID:33454011` directly tested `Arid4b`-null mESCs and showed normal self-renewal/pluripotency, directly contradicting `GO:1902459`!).
- **`GO:0003677` (`EXP`, `IEA`, `IMP` — 3 rows), `GO:0070822` (`NAS`), `GO:0000122` (`NAS` x2), `GO:0006357` (`IBA`), `GO:0005654` (`TAS` x2) -> `ACCEPT`**.
- **`GO:0005634` (`IBA`, `IEA`, `NAS`), `GO:0005737` (`EXP`, `IEA`), `GO:0005829` (`IDA`) -> `KEEP_AS_NON_CORE`**.
