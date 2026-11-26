# Curatorial Notes for Zebrafish `accs` (`UniProtKB:A0A8M1N4R4`)

## 1. Identity, Replaced Accession Note, and Phylogeny
- **Gene symbol / IDs**: `accs` (synonyms `fa10f06`, `wu:fa10f06`, `zgc:113217`; `ZFIN:ZDB-GENE-050327-39`, `NCBIGene:541510`, `RefSeq:NP_001014345.3`), located on zebrafish chromosome 25.
- **UniProtKB**: `A0A8M1N4R4` (`A0A8M1N4R4_DANRE`, unreviewed TrEMBL entry in reference proteome `UP000000437`, sequence version 1, 556 aa, `PE 1: Evidence at protein level` via PeptideAtlas), assigned to **`PANTHER:PTHR43795:SF17`** (*1-AMINOCYCLOPROPANE-1-CARBOXYLATE SYNTHASE-LIKE PROTEIN 1*). Note that legacy TrEMBL accession `F1QMK2` listed in PANTHER 19.0 (`PTHR43795-entries.csv`) has been deleted/superseded in UniProtKB by `A0A8M1N4R4` for the same ZFIN gene (`ZDB-GENE-050327-39`).

## 2. Literature Search & Audit of UniProt-Imported References (Supporting `ND` Curation)
- Systematic PubMed and Europe PMC searches for `("accs" OR "fa10f06" OR "zgc:113217" OR "ZDB-GENE-050327-39" OR "A0A8M1N4R4" OR "F1QMK2" OR "541510") AND ("Danio rerio" OR "zebrafish")`:
  - Zero zebrafish-specific publications characterize `accs` enzymatic activity, endogenous substrates, mutant/morphant phenotypes, or subcellular localization (`GO:0005575` `ND` is verified as `TRUE_GAP`).
  - Audit of the two RefSeq-imported nucleotide-sequence PMIDs on `A0A8M1N4R4`:
    1. `PMID:26469318` (Elkon et al. 2015, *Nat Commun* 6:8549): Studies mouse `Rfx1/3` conditional knockout inner-ear hair cells and includes bulk FACS RNA-seq of 5 dpf `ppv3b:GFP` zebrafish hair cells (`Supplementary Data 6`); does not mention or functionally study `accs` (`relevance: LOW`).
    2. `PMID:27189481` (Pasquier et al. 2016, *BMC Genomics* 17:368): PhyloFish multi-tissue RNA-seq de novo transcriptome database across 23 ray-finned fishes (`relevance: LOW`).

## 3. Active-Site Residue Comparison (`A0A8M1N4R4` sv 1 vs Human `Q96QU6` sv 1)
- `Tyr83` / `Trp86` (`Q96QU6` `Tyr132` / `Trp135`): **Retained** — partner-subunit PLP H-bond tyrosine (modeled in AlphaFold2/AutoDock Vina docking on human `ACCS` as sterically impeding productive SAM binding, `PMID:39876065`) and aromatic side-pocket tryptophan.
- `Asp237` (`Q96QU6` `Asp286`): **Retained** — fold-type I pyridinium-stabilizing aspartate.
- `Lys274` (`Q96QU6` `Lys323`): **Retained** (matched by `PROSITE:PS00105` / `InterPro:IPR004838` class-I aminotransferase PLP attachment site) — covalent internal-aldimine Schiff-base lysine.
- `Cys302` (`Q96QU6` `Arg351`): **Diverged / Lost** (`R -> C`) — whereas mammalian `ACCS` orthologs conserve cationic `Arg351` in the partner-monomer substrate pocket (`PMID:39876065` Figure 7), teleost `accs` carries `Cys302` at this position (and appends a distinct ~95-residue C-terminal extension at residues 460..556).
- `Arg408` (`Q96QU6` `Arg457`): **Retained** — conserved substrate alpha-carboxylate-anchoring arginine.

## 4. Annotation Decisions
- `GO:0003824` (`catalytic activity`, `IEA`, `InterPro:IPR004838`): `ACCEPT` — `A0A8M1N4R4` retains the intact catalytic PLP apparatus (`Lys274`, `Asp237`, `Arg408`, `Tyr83`, `Trp86`), but because teleost `accs` substitutes `Cys302` at mammalian pocket residue `Arg351` and has not been biochemically assayed, broad `catalytic activity` (`GO:0003824`) is as specific as warranted without over-claiming mammalian sulfoxide substrate preference.
- `GO:0005575` (`cellular_component`, `ND`, `GO_REF:0000015`): `ACCEPT` (`nd_case: TRUE_GAP`), paired with `[BIOLOGY]` `CC_DARK` knowledge gap.
- `GO:0009693` (`ethylene biosynthetic process`, `IEA`, `ARBA:ARBA00091972`): `REMOVE` (with `WRONG_TERM` `source_defects` on `resource: UNIPROT`, `record: ARBA:ARBA00091972` / `GOA`) — egregious cross-kingdom false positive: vertebrates do not synthesize the land-plant hormone ethylene, and vertebrate `SF17` homologs lack 1-aminocyclopropane-1-carboxylate synthase activity (`PMID:11470512`, `PMID:39876065`).
- `GO:0030170` (`pyridoxal phosphate binding`, `IEA`, `InterPro:IPR004838`, `InterPro:IPR004839`): `ACCEPT` — backed by `PROSITE:PS00105` active-site motif conservation (`Lys274`, `Asp237`) and stoichiometric PLP binding in vertebrate `SF17` ortholog `Q96QU6`.
