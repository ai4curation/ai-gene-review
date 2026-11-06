# Curation Notes for *Arabidopsis thaliana* CSD2 (`O78310` / `AT2G28190`)

## 1. Gene Identity & Biochemical Function
- **UniProt ID:** `O78310` (`SODC2_ARATH`)
- **AGI Locus:** `AT2G28190`
- **Gene Symbol:** `CSD2`
- **Protein Name:** Superoxide dismutase [Cu-Zn] 2, chloroplastic (216 AA precursor with N-terminal chloroplast transit peptide `1..62`, mature chain `63..216`, Reviewed Swiss-Prot)
- **Catalytic Activity:** Catalyzes the disproportionation of photochemically generated superoxide radicals into molecular oxygen and hydrogen peroxide (`2 superoxide + 2 H+ = H2O2 + O2`, `EC:1.15.1.1`, `RHEA:20696`) in the chloroplast [PMID:9765550; PMID:15772282].
- **Subcellular Localization:** Imported into the chloroplast (`GO:0009507`) via its 62-AA N-terminal transit peptide (`uniprot:O78310`), localizing to the chloroplast stroma (`GO:0009570`) [PMID:15772282, "CSD1 encodes a Cu/ZnSOD active in the cytosol, and CSD2 encodes a Cu/ZnSOD active in the chloroplast stroma."; PMID:18633119; PMID:20061580] and associating peripherally with the thylakoid membrane (`GO:0009579`) at the site of Photosystem I superoxide generation in the water-water (Mehler-peroxidase) cycle [PMID:16648217]. Copper delivery to plastidic CSD2 requires the envelope P-type ATPase PAA1 (`HMA6`) and thylakoid P-type ATPase PAA2 (`HMA8`) as well as the plastid-targeted CCS metallochaperone [PMID:15772282].
- **Apoplast Contaminant Note (`GO:0048046`):** `CSD2` has a single `HDA` row for `GO:0048046` (`apoplast`) from `PMID:18538804`. Because `CSD2` carries a canonical N-terminal chloroplast transit peptide (`1..62`), lacks a secretory signal peptide, and is an abundant stromal protein, its detection in apoplastic wash fluid reflects chloroplast lysis during vacuum infiltration; `GO:0048046` is therefore `REMOVE`d.

## 2. Post-Transcriptional Regulation by miR398 & The `GO:0035195` Substrate-vs-Actor Mis-Annotation
- **miR398-Guided Cleavage of `CSD2` mRNA:**
  - `CSD2` (`AT2G28190`) contains a conserved `miR398` target site in its coding sequence, which is cleaved by `miR398`-loaded ARGONAUTE1 (AGO1) RISC [PMID:16861386, "After 2 d of coexpression with miR398, CSD1 and CSD2 mRNA decreased substantially, which demonstrated that the miR398 can direct the degradation of CSD1 and CSD2 mRNAs in vivo"].
  - Transgenic *Arabidopsis* plants expressing a `miR398`-resistant form of `CSD2` (`mCSD2` with silent mutations in the `miR398` complementary site) accumulate higher `CSD2` mRNA and protein and display dramatically enhanced tolerance to high light, Cu2+, and methyl viologen-induced oxidative stress compared with wild-type or wild-type `CSD2`-overexpressing lines [PMID:16861386].
- **Audit of `GO:0035195` (`miRNA-mediated post-transcriptional gene silencing`):**
  - Both UniProt/QuickGO (`CSD2-goa.tsv`) and TAIR (`tair.gaf.gz`, recorded in `file:projects/THLAR_OILSEED/mirna_targets/goa_tair_mirna_annotations.tsv`) annotate `CSD2` (`O78310` / `AT2G28190`) as `involved_in` `GO:0035195` (`miRNA-mediated post-transcriptional gene silencing`) with evidence code `IEP` citing `PMID:16861386`.
  - Per GO biological process curation rules, being the cleaved mRNA substrate of `miR398`-loaded RISC does not make the chloroplastic Cu/Zn superoxide dismutase enzyme a participant in the miRNA silencing pathway. Exactly as for `CSD1`, this annotation is `REMOVE`d.
