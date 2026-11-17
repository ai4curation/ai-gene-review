# Curation Notes for Human `ARID5A` (`UniProtKB:Q03989`)

## 1. Gene Identity, `MRF-1` Homonym Collision & Phylogenetic Context (`PANTHER:PTHR13964:SF25`)
- **Organism**: *Homo sapiens* (`NCBITaxon:9606`)
- **HGNC / Gene Symbol**: `HGNC:17361` / `ARID5A` (*AT-rich interactive domain 5A*; legacy alias `MRF1`, `MRF-1`, *Modulator recognition factor 1*).
- **CRITICAL HOMONYM COLLISION DISCOVERED IN AFFINAGE (`MRF-1` vs Rat `mrf-1`/`Aif1`)**:
  - Human `ARID5A` carries legacy symbol `MRF-1` (*Modulator recognition factor 1*, cloned as a human CMV enhancer-binding nuclear protein, 594 aa, ~64 kDa).
  - In rat neurobiology literature, `MRF-1` / `mrf-1` (*Microglial response factor-1*) is a completely unrelated **17-kDa EF-hand calcium-binding protein** (`Aif1` / `Iba1`, `UniProtKB:P55009`) expressed in microglia and released extracellularly upon ATP/P2X7 stimulation (`PMID:12363408`: `"The mrf-1 gene encodes a 17-kDa protein with a single calcium-binding (EF-hand) motif and is expressed specifically in microglia"`; `PMID:12420315`).
  - `ARID5A-deep-research-affinage.md` fell directly into this `MRF-1` symbol collision, ingesting `PMID:12363408` and `PMID:12420315` into its `Dated findings` and `Citations` and contaminating its `localization` profile with **`GO:0005576 extracellular region`**! Recorded as `CONFIRMED` `SYMBOL_COLLISION` `source_defects` on `ARID5A-deep-research-affinage.md`.
- **UniProtKB**: `Q03989` (594 aa, sequence version 2; isoforms `Q03989-1`, `Q03989-5`).
- **PANTHER Family / Subfamily**: `PANTHER:PTHR13964` (`RBP-RELATED`) / `PANTHER:PTHR13964:SF25` (`AT-RICH INTERACTIVE DOMAIN-CONTAINING PROTEIN 5A`).

## 2. Structural & Mechanistic Synthesis (`Q03989`, 594 aa)
1. **Dual DNA- and RNA-Binding Extended ARID Domain**:
   - Compact 594-aa protein lacking Tudor, PWWP, chromobarrel, or R2 Sin3-binding domains; contains an N-terminal core ARID domain (`aa 58-150`; `His73` in `72-RHTPI-76`, Helix-4 core `Trp111`, vertebrate ARID5 major-groove AT-recognition segment `123-GSTSAATCTRRHYERL-138` with `Thr125`, `Ser126`, `Cys130`, `Arg133`, `His134`) flanked by positively charged intrinsically disordered N- and C-terminal extensions (`aa 37-183`).
   - von Ehr et al. 2024 (`PMID:38866324`, *J Biol Chem*) used solution NMR, EMSA, RNA Bind-n-Seq, and iCLIP2 to dissect `ARID5A` dual nucleic-acid recognition:
     - **AT-rich dsDNA recognition**: Core ARID favors central `5'-AATA-3'` dsDNA (`Kd` ~0.8-2.3 uM vs weak fast-exchange GC-DNA binding), and `T125A/S126A` substitution at the Loop-L2/Helix-5 junction strongly impairs AT-DNA binding (`GO:0000976`, corroborating `PMID:15640446`).
     - **3'-UTR stem-loop & AU/U-rich RNA recognition**: Minimal core `ARID49-152` binds short structured stem-loops (`Ox40` ADE, `IL6` 129-nt 3'-UTR) only moderately while preferring `(A)CAGGCA(GG)` and AU-rich ssRNA motifs, whereas the basic flanking IDRs (`ARID37-183`) dramatically boost affinity (`<0.1x` substoichiometric binding to the 129-nt human `IL6` 3'-UTR stem-loop RNA) and yield U-rich/AG-rich crosslinks in vivo (`GO:0035613`, `GO:0035925`).
2. **Cytoplasmic 3'-UTR mRNA Stabilization Antagonizing Regnase-1 (`ZC3H12A`)**:
   - Higa et al. 2018 (`PMID:29358370`) showed `ARID5A` enters the nucleus via importin-alpha/beta1 under basal conditions and undergoes `CRM1`-dependent nuclear export to the cytoplasm (`GO:0005829`) with `UPF1` upon LPS inflammatory stimulation.
   - In the cytoplasm, `ARID5A` binds conserved stem-loop and cis-regulatory elements in the 3'-UTRs of `IL6` (`PMID:23676272`, `PMID:32209697`, `PMID:32302067`), `STAT3` (`PMID:27022145`), `TBX21`/`T-bet` (`PMID:27671645`), and `IL-17`-induced transcripts (`PMID:30301788`), competitively blocking `Regnase-1` (`ZC3H12A`) endoribonucleolytic cleavage to promote `IL-6`, `IFN-gamma`, and `IL-17` cytokine production and Th17/Th1 differentiation (`GO:1905870`).
3. **Nuclear Transcriptional Corepression & Coactivation**:
   - Georgescu et al. 2005 (`PMID:15941852`) identified human `MRF1`/`ARID5A` as a nuclear corepressor that physically binds `ESR1` (`ERalpha`), `ESR2` (`ERbeta`), `THRA`, `RXRA`, `RARA`, and `AR` and represses estradiol-stimulated `ERalpha` transcription in an HDAC-independent manner (`GO:0003714`, `GO:0016922`, `GO:0000122`).
   - Amano et al. 2011 (`PMID:21346191`) showed that nuclear `Arid5a` binds directly to the `Col2a1` promoter, physically associates with `SOX9`, and stimulates histone H3 acetylation and chondrocyte-specific transcription (`GO:0006357`).

## 3. Audit of `ARID5A-deep-research-affinage.md`
- Frontmatter: `uniprot_accession: Q03989` (matches), `self_evaluation_pairwise: win`, `faith_pct: 100.0`, `citation_count: 22`.
- **Verdict**: `relevance: HIGH`, `correctness: LOW_QUALITY` (3 structured `source_defects` recorded):
  1. **`WRONG_STATEMENT` (`cause: SYMBOL_COLLISION`, `slot: localization`, `requested_change: CHECK`)**: Emits `GO:0005576 extracellular region` in `- **localization:** GO:0005829 cytosol, GO:0005634 nucleus, GO:0005840 ribosome, GO:0005576 extracellular region` due to conflating human `ARID5A` (`MRF-1`) with rat microglial 17-kDa EF-hand protein `mrf-1`/`Aif1` (`PMID:12420315`).
  2. **`WRONG_STATEMENT` (`cause: SYMBOL_COLLISION`, `slot: dated_findings`, `requested_change: CHECK`)**: Ingests two off-target 2002 rat microglia `mrf-1`/`Aif1` papers (`PMID:12363408` and `PMID:12420315`) as `MRF-1 (Arid5a)` discoveries (`"MRF-1 (Arid5a) is released from microglia into the extracellular space, and this release is markedly enhanced by ATP and PAF (platelet-activating factor) through a Ca2+-dependent mechanism requiring P2X7 receptor activation."`).
  3. **`WRONG_STATEMENT` (`slot: molecular_activity`, `requested_change: CHECK`)**: Emits `GO:0140313 molecular sequestering activity` for competitive 3'-UTR stem-loop mRNA protection against Regnase-1, and omits nuclear hormone receptor corepression (`PMID:15941852`).

## 4. Existing Annotation Decisions (148 Existing Rows + 1 `NEW` Cytosol Row)
- **4 Obsolete Nuclear Receptor Binding `IDA` Rows (`GO:0030331`, `GO:0046965`, `GO:0046966`, `GO:0050681` from `PMID:15941852`) -> `MODIFY`** with `proposed_replacement_terms: [{id: GO:0016922, label: nuclear receptor binding}]`.
- **117 Bare `GO:0005515` (`protein binding`, `IPI`) Rows -> `REMOVE`** per `protein_binding_policy.py`.
- **`GO:0000976` (`IBA` from `PTN000359478`), `GO:0035613` (`RNA stem-loop binding`, `IEA`), `GO:0035925` (`mRNA 3'-UTR AU-rich region binding`, `IDA`), `GO:1905870` (`positive regulation of 3'-UTR-mediated mRNA stabilization`, `IMP`), `GO:0003714` (`transcription corepressor activity`, `IDA`), `GO:0000122` (`IDA`), `GO:0006357` (`IBA`), `GO:0005654` (`nucleoplasm`, `IDA`) -> `ACCEPT`**.
- **`NEW` `GO:0005829` (`cytosol`, `IDA` from `PMID:29358370` & `PMID:27022145`)**: Added to ground `core_functions[0].locations` (`cytosol`), where CRM1-exported `ARID5A` stabilizes target 3'-UTR mRNAs (`GOA` lacked any cytoplasmic/cytosolic CC row for human `ARID5A`!).
- **`GO:0003677` (`IEA`, `TAS`), `GO:0043565` (`IDA`), `GO:0045892` (`TAS`) -> `TOO_GENERAL`** (subsumed by `GO:0000976` and `GO:0000122`).
- **`GO:0032760` (`positive regulation of tumor necrosis factor production`, `IEA`) -> `MARK_AS_OVER_ANNOTATED`**: Masuda et al. 2013 (`PMID:23676272`) explicitly demonstrated that `Arid5a` does NOT bind the `TNF` 3'-UTR and does NOT regulate TNF-alpha production in cultured macrophages, attributing lower serum TNF-alpha in `Arid5a-/-` EAE/LPS mice to indirect downstream loss of IL-6.
- **`GO:0008134` (`transcription factor binding`, `IDA` from `PMID:15941852`), `GO:0003682` (`IEA`), `GO:0005634` (`IBA`, `IEA`), `GO:0005667` (`IEA`), `GO:0005730` (`nucleolus`, `IDA`), `GO:0042802` (`identical protein binding`, `IPI`), and downstream immune/hormone BP rows (`GO:0032729`, `GO:0032740`, `GO:0032755`, `GO:0071222`, `GO:0071391`, `GO:2000318`, `GO:2000556`) -> `KEEP_AS_NON_CORE`**.
