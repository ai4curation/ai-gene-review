# Curation Notes for *Drosophila melanogaster* `htk` (`UniProtKB:Q9VWP5`)

## 1. Gene Identity & Phylogenetic Context (`PANTHER:PTHR13964:SF27`)
- **Organism**: *Drosophila melanogaster* (`NCBITaxon:7227`)
- **FlyBase / Gene Symbol**: `FB:FBgn0085451` / `htk` (*hat-trick*; CG34422; isoform D `UniProtKB:Q9VWP5`, 2486 aa, sequence version 4).
- **PANTHER Family / Subfamily**: `PANTHER:PTHR13964` (`RBP-RELATED`) / `PANTHER:PTHR13964:SF27` (`HAT-TRICK, ISOFORM D`).
- **Phylogenetic Placement & Complex Switch**: Although PANTHER groups invertebrate `htk` into basal grade `SF27` alongside fungal `SWI1`/`sol1`, `htk` lies on the metazoan branch outside Dikarya node `PANTHER:PTN002303792` and is the single *Drosophila* ortholog of vertebrate `ARID4A`/`ARID4B` (`SF26`/`SF24`), sharing Tudor, ARID, and chromobarrel domains and associating with the *Drosophila* SIN3-RPD3 histone deacetylase complex (`PMID:20566628`) rather than BAP/PBAP (SWI/SNF, whose *Drosophila* ARID subunit is `osa` in `PANTHER:PTHR10591`).
- **MOD Description Check**: Ran `ai-gene-review mod-description-deep-research DROME htk`; Alliance/FlyBase returned `no_curated: 1` (no hand-written FlyBase gene snapshot exists for `FB:FBgn0085451`), so no `-deep-research-flybase.md` file was emitted.

## 2. Biochemical & Genetic Literature Synthesis
1. **SIN3 Corepressor Complex Association**:
   - Spain et al. 2010 (`PMID:20566628`, *J Biol Chem*) affinity-purified *Drosophila* SIN3 187 and SIN3 220 complexes from S2 cells and embryos, identifying Hat-trick (`CG34422`) as an endogenous component of the *Drosophila* SIN3 histone deacetylase complex (`GO:0070822`), establishing evolutionary conservation of Sin3-ARID4 association across protostomes and vertebrates.
2. **Notch Signaling Coactivation via Notch-ICD and Su(H)**:
   - Singh et al. 2019 (`PMID:31142544`, *Development*) identified Htk in a yeast two-hybrid screen as a direct physical interactor of the Notch intracellular domain (`Notch-ICD`, `FB:FBgn0004647`; validated by co-IP) and `Suppressor of Hairless` (`Su(H)`, `FB:FBgn0004837`). Nuclear Htk colocalizes with Notch-ICD, binds chromatin at `Enhancer of split` (`E(spl)`) regulatory regions, and is required in somatic clones for transcriptional activation of Notch target genes without altering Notch protein abundance (`GO:0001221`, `GO:0140297`, `GO:0003682`, `GO:0045944`, `GO:0045747`).
3. **Oocyte Karyosome Heterochromatin Clustering & DSB Maintenance**:
   - Singh et al. 2018 (`PMID:29367451`, *G3*) showed that Htk is enriched in the heterochromatinized karyosome of the *Drosophila* oocyte nucleus where it colocalizes with HP1 (`Su(var)205`); germline `htk` depletion causes diffused karyosomes, elevated double-strand breaks, delayed DSB repair, altered Vasa phosphorylation, and Gurken mislocalization/dorsoventral egg-chamber defects.
4. **Modifier of TDP-43 Motor Neuron Degeneration & Embryonic Nuclear Localization**:
   - Sreedharan et al. 2015 (`PMID:26234214`, *Curr Biol*) recovered loss-of-function alleles of `hat-trick` in a mosaic forward genetic screen as a potent suppressor of age-dependent `TDP-43(Q331K)` motor axon/NMJ degeneration in adult fly legs (reducing TDP-43 protein accumulation post-transcriptionally without blocking Wallerian degeneration).
   - Lye et al. 2014 (`PMID:25294944`, *Development*) mapped YFP-trapped Htk to the nucleus in *Drosophila* embryos (`HDA`).
5. **Residue Architecture (`Q9VWP5`, 2486 aa)**:
   - ARID domain (`aa 296-389`) retains Helix-1/Loop-L1 `311-RGTPL-315` (`Gly312`) and Helix-4 core `Trp350`, but carries `Val364` (`362-CTVSVMNLVKQAYK-375`) in place of the vertebrate ARID5 major-groove AT-recognition threonine (`Thr388` in `ARID5B`), consistent with recruitment to Notch target enhancers via `Su(H)` and `Notch-ICD` rather than intrinsic sequence-specific cis-regulatory DNA recognition.

## 3. Existing Annotation Audit & Family Harmonization (`PTHR13964`)
- **`GO:0000976` (`transcription cis-regulatory region binding`, `IBA` from `PANTHER:PTN000359478`) -> `REMOVE` (`PROPAGATION_BAD`)**:
  - Over-propagated from the lone vertebrate `ARID5B` seed (`UniProtKB:Q14865`) on `PTN000359478`; Htk lacks the ARID5 loop-L2/Helix-5 AT-selective motif (`Val364` vs `Thr388`) and is recruited to `E(spl)` regulatory chromatin via `Su(H)` (`GO:0140297`) and `Notch-ICD` (`GO:0001221`).
- **`GO:0070822` (`Sin3-type complex`, `IDA` from `PMID:20566628`), `GO:0003682` (`chromatin binding`, `IDA` from `PMID:31142544`), `GO:0140297` (`DNA-binding transcription factor binding`, `IPI` with `Su(H)` from `PMID:31142544`), `GO:0001221` (`transcription coregulator binding`, `IPI` with `Notch` from `PMID:31142544`), `GO:0006357` (`regulation of transcription by RNA polymerase II`, `IBA` from `PTN000359478`), `GO:0045944` (`positive regulation of transcription by RNA polymerase II`, `IMP` from `PMID:31142544`) -> `ACCEPT`**.
- **`GO:0045747` (`positive regulation of Notch signaling pathway`, `IGI` from `PMID:31142544`) -> `KEEP_AS_NON_CORE`** (valid pathway-level readout of its transcriptional coactivation of Notch target genes).
- **`GO:0005634` (`nucleus`, `HDA`, `IBA`, `IDA`, `IEA`) & `GO:0003677` (`DNA binding`, `IEA`) -> `KEEP_AS_NON_CORE`**.
- **`GO:0006351` (`DNA-templated transcription`, `IEA`) & `GO:0006355` (`regulation of DNA-templated transcription`, `IEA`) -> `TOO_GENERAL`** (strictly subsumed by accepted `GO:0006357` and `GO:0045944`).
