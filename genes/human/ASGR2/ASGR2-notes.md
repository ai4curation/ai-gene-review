# ASGR2 (P07307) Curation & Research Notes

## 1. Gene & Protein Overview
- **Gene symbol**: `ASGR2` (aliases: `CLEC4H2`, HL-2, H2)
- **UniProt accession**: `P07307` (*Homo sapiens*, `NCBITaxon:9606`), 311 amino acids
- **Protein identity**: Asialoglycoprotein receptor 2 (minor subunit H2 of the hepatic Ashwell-Morell receptor), sharing ~58% amino acid sequence identity with the major subunit ASGR1 (`[PMID:3863106, "From the same library, we have isolated and sequenced a clone encoding a second ASGP receptor, H2, with a protein sequence homology of 58% to H1."]`).
- **Isoforms** (`file:genes/human/ASGR2/ASGR2-uniprot.txt`):
  - **Isoform 1 (`P07307-1`, H2a, canonical)**: 311 aa single-pass type II membrane protein containing two mini-exons: a 19-aa cytoplasmic segment (residues 24–42; `VSP_003060`) and a 5-aa extracellular juxtamembrane pentapeptide `EGHGG` (or `EGHRG` with variant Arg-85; residues 82–86; `VSP_003061`). When expressed alone in heterologous cells without ASGR1, H2a is retained in the endoplasmic reticulum quality control compartment, where its ectodomain is cleaved or the full-length precursor is degraded via ubiquitin-proteasome ERAD (`PMID:11408579`, `PMID:29069408`).
  - **Isoform 2 (`P07307-2`, H2b)**: Lacks cytoplasmic residues 24–42 (`VSP_003060`), retaining the extracellular juxtamembrane pentapeptide (residues 82–86).
  - **Isoform 3 (`P07307-3`, H2c; often referred to in older biochemical literature as H2b when comparing with H2a)**: Lacks both cytoplasmic residues 24–42 (`VSP_003060`) and the extracellular juxtamembrane residues 82–86 (`VSP_003061`). Isoforms lacking the 5-aa luminal/extracellular juxtamembrane pentapeptide avoid rapid ER retention/cleavage and hetero-oligomerize with ASGR1 (H1) to form the native hepatic asialoglycoprotein receptor complex at the hepatocyte plasma membrane.

## 2. Domain Architecture & Post-Translational Modifications
- **Topological domains** (`file:genes/human/ASGR2/ASGR2-uniprot.txt`):
  - **Cytoplasmic N-terminal tail (residues 1–58)**: Contains a phenylalanine-based internalization motif `FQDI` at residues 5–8 (`FT   MOTIF           5..8 /note="Endocytosis signal"`), a phosphorylation site at Ser-13 (`Phosphoserine`), and palmitoylated cysteine(s) at Cys-54 (and Cys-58; `S-palmitoyl cysteine`).
  - **Transmembrane signal-anchor (residues 59–79)**: Single-pass type II transmembrane helix (`FT   TRANSMEM        59..79 /note="Helical; Signal-anchor for type II membrane protein"`).
  - **Extracellular domain (residues 80–311)**: Consists of a coiled-coil stalk/neck region and a C-terminal **C-type lectin domain** (CTLD, residues 176–302; `PROSITE:PS50041`) stabilized by three disulfide bonds (177–188, 205–300, 278–292) with three N-glycosylation sites (Asn-102, Asn-170, Asn-305).
- **S-Palmitoylation and Clathrin-Mediated Endocytosis**:
  - Yik et al. (`PMID:12171918`) showed that palmitoylation of ASGR1 (Cys-36) and ASGR2 (Cys-54 and Cys-58) is essential for clathrin-coated pit endocytosis of desialylated glycoproteins and proper dissociation of ligand in sorting endosomes prior to lysosomal delivery (`[PMID:12171918, "We conclude that palmitoylation of the ASGP-R is required for its efficient endocytosis of ligand by the clathrin-dependent endocytic pathway and, in particular, for the proper dissociation and delivery of ligand to lysosomes."]`).

## 3. Carbohydrate Specificity (QPD vs. EPN Motif) & Assembly with ASGR1
- **QPD Galactose/GalNAc Specificity Motif**:
  - Like ASGR1, the C-type lectin domain of ASGR2 carries the canonical galactose/GalNAc-recognizing **QPD** tripeptide (`Gln259-Pro260-Asp261` in sequence `...NWAVTQPDNWHGHELGGSEDCVEVQPDGRWNDDFCLQVYRWVCEKRRNATGEVA`), conferring specificity for terminal **D-galactose (Gal)** and **N-acetyl-D-galactosamine (GalNAc)** residues on desialylated plasma glycoproteins (`[file:genes/human/ASGR2/ASGR2-uniprot.txt, "Mediates the endocytosis of plasma glycoproteins to which the terminal sialic acid residue on their complex carbohydrate moieties has been removed. The receptor recognizes terminal galactose and N-acetylgalactosamine units."]`).
- **Obligate Hetero-Oligomerization with ASGR1 for Cell-Surface Export**:
  - Unlike ASGR1, which can form functional cell-surface homo-oligomers, ASGR2 requires co-expression and hetero-oligomerization with ASGR1 to be efficiently exported from the ER to the plasma membrane (`[PMID:29069408, "This data parallels previous reports demonstrating that co-expression of ASGR1 results in ASGR2 incorporation into ASGR1/ASGR2 heterodimers that are then exported from the ER and are ultimately targeted to the plasma membrane"]`).
  - When expressed in the absence of ASGR1 (e.g., H2a in NIH 3T3 or CHO cells), the unassembled ASGR2 precursor is retained in a juxtanuclear endoplasmic reticulum quality control compartment (`GO:0044322`) and degraded by the ubiquitin-proteasome ERAD pathway (`PMID:11408579`).

## 4. Phylogenetic Context & IBA Propagation Analysis
- **PANTHER Classification**:
  - In PANTHER (`interpro/panther/PTHR22803/PTHR22803-entries.csv`), `ASGR2` (`P07307`) and `ASGR1` (`P07306`) belong to `PANTHER:PTHR22803` (`MANNOSE, PHOSPHOLIPASE, LECTIN RECEPTOR RELATED`), and in related PANTHER subfamily classifications correspond to `PTHR22802:SF433` (ASGR2) and `PTHR22802:SF470` (ASGR1).
  - PAINT IBA annotations from `PTHR22803` ancestral nodes exhibit the exact same over-propagation patterns on `ASGR2` as on `ASGR1`:
  1. **`PANTHER:PTN004568004` (`GO:0005537` D-mannose binding; `GO:0042806` fucose binding)**:
     - Seeded by human `CLEC17A` (`UniProtKB:Q6ZS10`). Over-propagated (`PROPAGATION_BAD` / `FUNCTIONAL_DIVERGENCE`, `OVER_PROPAGATED`) because ASGR2 contains a galactose/GalNAc-specific QPD motif rather than a mannose/fucose-specific EPN motif.
  2. **`PANTHER:PTN001105054` (`GO:0038187` pattern recognition receptor activity; `GO:0006955` immune response)**:
     - Seeded by mammalian and non-mammalian C-type lectin pattern-recognition and immune receptors (`MGI:MGI:1861231` *Clec4n*, `MGI:MGI:1861232` *Clec4d*, `UniProtKB:Q6EIG7` human CLEC6A, `UniProtKB:Q8WXI8` human CLEC4D, `UniProtKB:Q9ULY5` human CLEC4E, `UniProtKB:P06734` human FCER2, `MGI:MGI:1298389` *Clec4a2*, *Drosophila* and zebrafish lectins). Over-propagated (`PROPAGATION_BAD` / `FUNCTIONAL_DIVERGENCE`, `OVER_PROPAGATED`) because ASGR2 is the minor subunit of the hepatocyte Ashwell-Morell endocytic scavenger receptor for endogenous desialylated serum glycoproteins (e.g., vWF) and aged desialylated platelets, mediating homeostatic turnover rather than an innate immune response (`GO:0006955`) or pathogen-associated pattern-recognition receptor activity.
  3. **`PANTHER:PTN001105053` (`GO:0009897` external side of plasma membrane)**:
     - Seeded by human `CD209` (`UniProtKB:Q9NNX6`) and mouse C-type lectins (`MGI:MGI:1916415` *Cd209a*, `MGI:MGI:3588267` *Cd209f*, `MGI:MGI:95497` *Fcer2a*). Valid core localization (`ACCEPT`, `NO_FAILURE_CORE`), as mature ASGR2 (incorporated into ASGR1/ASGR2 heterooligomers) is a type II transmembrane protein whose C-terminal C-type lectin domain resides on the external side of the hepatocyte plasma membrane.

## 5. Summary of Curation Decisions for ASGR2
- **`GO:0004873` (`asialoglycoprotein receptor activity`)** [TAS `PMID:3863106`]: `ACCEPT` (Core MF).
- **`GO:0016192` (`vesicle-mediated transport`)** [IEA `GO_REF:0000108` from `GO:0004873`]: `MODIFY` to `GO:0006898` (`receptor-mediated endocytosis`), the specific core biological process mediated by the ASGR1/ASGR2 receptor complex (`PMID:12171918`, `PMID:29069408`).
- **`GO:0005886` (`plasma membrane`)** [IDA `GO_REF:0000052`, TAS `Reactome:R-HSA-8855711`]: `ACCEPT` (Core CC).
- **`GO:0009897` (`external side of plasma membrane`)** [IBA `GO_REF:0000033`]: `ACCEPT` (Core CC).
- **`GO:0016020` (`membrane`)** [IEA `GO_REF:0000044`]: `MODIFY` to `GO:0005886` (`plasma membrane`), which is already established as the specific core membrane compartment.
- **`GO:0044322` (`endoplasmic reticulum quality control compartment`)** [IDA `PMID:11408579`] & **`GO:0048471` (`perinuclear region of cytoplasm`)** [IDA `PMID:11408579`]: `KEEP_AS_NON_CORE` (Reflects retention of unassembled H2a precursor in the juxtanuclear ER quality control compartment prior to ERAD when expressed without its obligate assembly partner ASGR1 in heterologous fibroblasts).
- **`GO:0007166` (`cell surface receptor signaling pathway`)** [TAS `PMID:3863106`]: `REMOVE` (`PMID:3863106` reported the cloning and sequence homology of H2 to H1 and contains no evidence of signal transduction; ASGR2 is a clathrin-dependent endocytic cargo receptor rather than a signaling receptor).
- **`GO:0005537` (`D-mannose binding`)** [IBA `GO_REF:0000033`]: `REMOVE` (`OVER_PROPAGATED` from `PANTHER:PTN004568004` / `CLEC17A`).
- **`GO:0042806` (`fucose binding`)** [IBA `GO_REF:0000033`]: `REMOVE` (`OVER_PROPAGATED` from `PANTHER:PTN004568004` / `CLEC17A`).
- **`GO:0038187` (`pattern recognition receptor activity`)** [IBA `GO_REF:0000033`]: `REMOVE` (`OVER_PROPAGATED` from myeloid PRRs at `PANTHER:PTN001105054`).
- **`GO:0006955` (`immune response`)** [IBA `GO_REF:0000033`]: `REMOVE` (`OVER_PROPAGATED` from myeloid PRRs at `PANTHER:PTN001105054`).
- **`GO:0005515` (`protein binding`)** [3 IPI rows from `PMID:11408579`, `PMID:11543633`, `PMID:21988832`]: `REMOVE` per the repository's bare `GO:0005515` protein-binding policy.
- **`GO:0005534` (`galactose binding`)** [TAS `file:genes/human/ASGR2/ASGR2-uniprot.txt`]: `NEW` (Captures the direct QPD-motif terminal D-galactose and GalNAc carbohydrate-binding specificity of ASGR2 replacing the removed `D-mannose binding` and `fucose binding` IBA rows; `file:genes/human/ASGR2/ASGR2-uniprot.txt`).
