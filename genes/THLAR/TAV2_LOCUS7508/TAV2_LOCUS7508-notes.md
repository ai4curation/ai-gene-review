# TAV2_LOCUS7508 (APS1 / ATPS1, A0AAU9RRK7) Curation Notes — *Thlaspi arvense*

## Orthology and Domain Architecture
- **Gene symbol / Locus**: `TAV2_LOCUS7508` (`Tarvense_12925`, protein accession `CAH2046571.1`, UniProt `A0AAU9RRK7`, 680 AA, Chromosome 2).
- **Ortholog**: Directpenny-cress ortholog of *Arabidopsis thaliana* **APS1 / ATPS1** (`AT3G22890`, `Q39214`, ATP sulfurylase 1, chloroplastic) and member of the plastidic ATP sulfurylase clade (`APS1`/`APS3`/`APS4`).
- **Conserved Domain Architecture** ([TAV2_LOCUS7508-uniprot.txt](TAV2_LOCUS7508-uniprot.txt)):
  - `FT:DOMAIN 265..428`: ATP-sulfurylase PUA-like domain (`Pfam:PF14306`, `InterPro:IPR025980`)
  - `FT:DOMAIN 438..659`: Sulphate adenylyltransferase catalytic domain (`Pfam:PF01747`, `InterPro:IPR024951`, `InterPro:IPR002650`)
  - **Absence of APS kinase domain**: Like all vascular plant ATP sulfurylases (`APS1`–`APS4`), `TAV2_LOCUS7508` is a monofunctional ATP sulfurylase (`EC 2.7.7.4`) and completely lacks an adenylylsulfate kinase (`PF01583` / `IPR002891`, `EC 2.7.1.25`) domain. In plants, APS kinase activity is encoded by a separate family of four genes (`APK1`–`APK4`).

## Biological Function & miR395 Regulation of Sulfate/Glucosinolate Flux
- **Catalytic Activity & Pathway**: ATP sulfurylase (`EC 2.7.7.4`, `GO:0004781`) catalyzes the first committed step of plastidic sulfate assimilation (`GO:0000103`), activating inorganic sulfate ($\text{SO}_4^{2-}$) with ATP to produce adenosine 5'-phosphosulfate (`APS`) and inorganic pyrophosphate ($\text{PP}_i$) inside the chloroplast stroma ([PMID:8058839](../../../publications/PMID_8058839.md), [PMID:24027241](../../../publications/PMID_24027241.md)).
- **Role in Glucosinolate Biosynthesis**: In Brassicaceae, APS produced by plastidic ATPS1 (`APS1`) is phosphorylated by APS kinase to 3'-phosphoadenosine 5'-phosphosulfate (`PAPS`), the universal sulfonate donor for glucosinolate core sulfation (including pennycress sinigrin/allylglucosinolate) as well as reduced via APR to sulfide for cysteine/methionine synthesis. Disruption of `ATPS1` in *Arabidopsis* reduces the glucosinolate synthesis rate by ~55% ([PMID:24027241](../../../publications/PMID_24027241.md)).
- **miR395 Target Site in Pennycress**:
  - Cross-reference of the 72 pennycress miRNA loci ([PMID:34990041](../../../publications/PMID_34990041.md)) against the `T_arvense_v2` transcriptome ([thlar_mirna_targets.tsv](../../../projects/THLAR_OILSEED/mirna_targets/thlar_mirna_targets.tsv)) identifies a high-confidence `miR395` (`tar-mir-395a`/`b`, mature sequence `CTGAAGTGTTTGGGGGAACTC`) target site in `TAV2_LOCUS7508` at CDS positions `973..993` (expectation score `1.5`, 2 total mispairings, 0 seed mismatches), orthologous to the PARE-seq Category-0 cleavage site in *Arabidopsis* `APS1` (`AT3G22890.1`, `p = 0.00346` in [tardb_ath_degradome.tsv](../../../projects/THLAR_OILSEED/mirna_targets/tardb_ath_degradome.tsv)).
  - **Curation Principle (Actor vs. Substrate)**: `TAV2_LOCUS7508` mRNA is a **substrate** of `miR395`-guided RISC cleavage, not an actor in `GO:0035195` (*miRNA-mediated post-transcriptional gene silencing*). Therefore, `GO:0035195` must never be annotated to `TAV2_LOCUS7508`.

## Review of Existing GOA Annotations (4 IEA rows)
1. `GO:0004781` (*sulfate adenylyltransferase (ATP) activity*, `IEA`) — **ACCEPT** (core molecular function).
2. `GO:0000103` (*sulfate assimilation*, `IEA`) — **ACCEPT** (core biological process).
3. `GO:0009507` (*chloroplast*, `IEA`) — **ACCEPT** (core cellular component; plastid/chloroplast localization supported by N-terminal chloroplast transit peptide homology and experimental import of orthologous APS1 in [PMID:8058839](../../../publications/PMID_8058839.md)).
4. `GO:0004020` (*adenylylsulfate kinase activity*, `IEA`, `TreeGrafter` `PANTHER:PTN004223551`) — **REMOVE** (classic TreeGrafter domain-fusion false positive inherited from metazoan bifunctional PAPS synthases `PAPSS1`/`PAPSS2` in `PTHR11055`; plant `APS1` and `TAV2_LOCUS7508` contain only PUA-like and ATP sulfurylase domains and lack the APS kinase domain).
