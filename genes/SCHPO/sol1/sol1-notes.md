# Curation Notes for *Schizosaccharomyces pombe* `sol1` (`UniProtKB:O74365`)

## 1. Gene Identity & Phylogenetic Context (`PANTHER:PTHR13964:SF27`)
- **Organism**: *Schizosaccharomyces pombe* (strain 972 / ATCC 24843; `NCBITaxon:284812`)
- **Systematic ID / Gene Symbol**: `SPBC30B4.04c` / `sol1` (*switch one-like 1*; aliases `swi10`, `snf1`)
- **UniProtKB**: `O74365` (865 aa, sequence version 1)
- **PANTHER Family / Subfamily**: `PANTHER:PTHR13964` (`RBP-RELATED`) / `PANTHER:PTHR13964:SF27` (`HAT-TRICK, ISOFORM D`), Dikarya fungal SWI/SNF branch (`PANTHER:PTN002303792`).
- **Orthology**: 1:1 fission yeast ortholog of *Saccharomyces cerevisiae* `SWI1` (`UniProtKB:P09547`). Note that `mod-description-deep-research` only supports WormBase, FlyBase, and SGD (`worm`, `fly`, `yeast`), so no MOD description file is generated for `SCHPO`.

## 2. Biochemical & Genetic Literature Synthesis
1. **Stoichiometric Subunit of the Fission Yeast SWI/SNF Chromatin-Remodeling Complex**:
   - Bernal & Maldonado 2007 (`PMID:17508131`, *Mol Cell Biochem*) isolated the fission yeast `spSWI/SNF` complex (~7+ subunits including `Sol1`/`spSwi1-like` and catalytic ATPase `Snf22`/`spBrg1`) and showed that purified `spSWI/SNF` promotes RNA polymerase II transcription on reconstituted nucleosome arrays in vitro.
   - Monahan et al. 2008 (`PMID:18622392`, *Nat Struct Mol Biol*) affinity-purified TAP-tagged *S. pombe* SWI/SNF and RSC complexes coupled to mass spectrometry, demonstrating that `Sol1` is one of the 12 core subunits of the *S. pombe* SWI/SNF complex (alongside `Snf22`, `Snf5`, `Swi3`, `Ssr1`/`Ssr2`/`Ssr3`, `Ssn6`-independent auxiliary subunits `Tfg3`, `Arp42`, `Arp9`, `Snf30`, `Snf59`), whereas RSC lacks `Sol1`. Deletion phenotypes and microarray expression profiling showed that `sol1Δ` phenocopies `snf22Δ` (`SWI/SNF` loss), causing cold/heat sensitivity and broad transcriptional deregulation including direct repression of iron-transport genes (`fio1+`, `fip1+`, `frp1+`, `str1+`).
2. **Subcellular Localization**:
   - Matsuyama et al. 2006 (`PMID:16823372`, *Nat Biotechnol*) fission yeast ORFeome YFP localization screen localized Sol1-YFP to the nucleus (`GO:0005634`).
3. **Domain & Residue Architecture (`O74365`, 865 aa)**:
   - Central ARID domain (`InterPro:IPR001606`, aa ~190-281) retains the conserved Helix-1/Loop-L1 `205-RGTPI-209` (`Gly206`) and Helix-4 hydrophobic-core `Trp244` (`PTHR13964` `arid_h4_core_tryptophan`), but lacks the vertebrate ARID5 major-groove AT-rich recognition dyad (`Thr388`/`Ser389` in human `ARID5B`), carrying `Ala258` at the homologous Loop-L2/Helix-5 position (`256-PDAISLLIQYYNSYL-270`). Like budding yeast `SWI1` (`PMID:18644858`, `PMID:32188938`), `Sol1` functions as a non-catalytic architectural/scaffolding subunit of SWI/SNF rather than a sequence-specific cis-regulatory DNA-binding transcription factor.

## 3. Existing Annotation Audit & Family Harmonization (`PTHR13964`)
- **`GO:0000976` (`transcription cis-regulatory region binding`, `IBA` from `PANTHER:PTN000359478`) -> `REMOVE` (`PROPAGATION_BAD`)**:
  - Seeded solely by human `ARID5B` (`UniProtKB:Q14865`, `PTHR13964:SF37`) on the Opisthokont root `PTN000359478`. Fungal SWI/SNF subunits (`SWI1`, `sol1`) lack the vertebrate ARID5 loop-L2/Helix-5 AT-selective major-groove motif (`Ala258` in `sol1` vs `Thr388` in `ARID5B`) and engage nucleosomal DNA non-specifically within the SWI/SNF complex. Matches `genes/yeast/SWI1/SWI1-ai-review.yaml` and `PTHR13964-review.yaml` (`MOVE_IBD` to `PANTHER:PTN009015192`).
- **`GO:0016514` (`SWI/SNF complex`, `IBA` from `PTN002303792`, `IDA` from `PMID:17508131`, `IDA` & `IPI` from `PMID:18622392`) -> `ACCEPT` (all 4 rows)**:
  - `Sol1` is a direct PAINT seed on Dikarya node `PTN002303792` and an experimentally purified stoichiometric subunit of fission yeast SWI/SNF.
- **`GO:0006357` (`regulation of transcription by RNA polymerase II`, `IBA` from `PTN000359478` & `NAS` from `PMID:18622392`), `GO:0006338` (`chromatin remodeling`, `NAS` from `PMID:18622392`), `GO:0045815` (`transcription initiation-coupled chromatin remodeling`, `IC` from `GO:0016514`) -> `ACCEPT`**.
- **`GO:0005634` (`nucleus`, `HDA` from `PMID:16823372`, `IBA` from `PTN000359478`, `IEA` from `GO_REF:0000044`) & `GO:0000785` (`chromatin`, `NAS` from `PMID:18622392`) -> `KEEP_AS_NON_CORE`** (harmonized with `SWI1-ai-review.yaml`).
- **`GO:0003677` (`DNA binding`, `IEA` from `InterPro:IPR001606`) -> `KEEP_AS_NON_CORE`** (reflects non-specific ARID DNA engagement, matching `SWI1-ai-review.yaml`).
