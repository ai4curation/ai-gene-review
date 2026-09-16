# Sdhaf2 (A0A494B8X4): evidence and exact-input prediction review

The mitochondrial-matrix prediction has a sound sequence and family basis. The assembly-factor name and flavinylation mechanism describe the Sdhaf2 gene correctly, but their complete functional transfer to the shorter alternative product is uncertain. The epithelial-transition and beta-catenin annotations also have real primary evidence; their uncertainty here concerns the exact product, not merely their electronic evidence code.

## Input identity and functional boundary

A0A494B8X4 is a 135-residue mouse Sdhaf2 product. Reference Q8C6I2 is 164 residues. Selected residues 1–122 match reference 1–122 at 121 positions, including all 27 residues of the reference mitochondrial transit peptide; the remaining 13 residues are an alternative tail. The reference C-terminal region is therefore not fully retained. This is not evidence that every shorter Sdhaf2 product must be inactive.

## Biological evidence

- [PMID:38569044 — Drp1 controls complex II assembly and skeletal muscle metabolism by Sdhaf2 action on mitochondria.](https://pubmed.ncbi.nlm.nih.gov/38569044/): Mouse muscle and myocyte experiments connect mitochondrial Sdhaf2 availability to complex-II assembly and activity; they do not isolate the 135-residue alternative product.

> Restoration of Sdhaf2 normalized complex II
> activity, lipid oxidation, and insulin action in Drp1-KD myocytes.

- [PMID:23983127 — Succinate dehydrogenase 5 (SDH5) regulates glycogen synthase kinase 3β-β-catenin-mediated lung cancer metastasis.](https://pubmed.ncbi.nlm.nih.gov/23983127/): The study directly reports a mouse Sdhaf2/SDH5 loss phenotype in lung epithelial cells, so the EMT association is not supported solely by an ARBA assertion.

> In SDH5 knock-out mice, lung epithelial cells exhibited elevated mesenchymal markers, which is characteristic of EMT.


> SDH5 functions as a negative regulator of Wnt-β-catenin signaling.

## Exact non-GO claims

The complete emitted record is preserved in [Sdhaf2-protnlm-source.json](Sdhaf2-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Succinate dehydrogenase assembly factor 2, mitochondrial

UNC (CS 1) as a complete functional enzyme-assembly-factor name for the selected product. Sdhaf2 family/gene identity and mitochondrial targeting are well supported, but full assembly-factor activity is not established for its altered C-terminus. This is not a wrong-paralog assignment. [Sequence comparison](Sdhaf2-bioinformatics/RESULTS.md); [PMID:38569044](https://pubmed.ncbi.nlm.nih.gov/38569044/).

### Function

> Plays an essential role in the assembly of succinate dehydrogenase (SDH), an enzyme complex (also referred to as respiratory complex II) that is a component of both the tricarboxylic acid (TCA) cycle and the mitochondrial electron transport chain, and which couples the oxidation of succinate to fumarate with the reduction of ubiquinone (coenzyme Q) to ubiquinol. Required for flavinylation (covalent attachment of FAD) of the flavoprotein subunit SDHA of the SDH catalytic dimer

UNC (CS 1). The paragraph correctly describes SDHAF2-mediated SDHA maturation at the gene level. The statements about TCA and respiratory chemistry describe the SDH complex, not intrinsic SDHAF2 catalysis. The selected product retains its mitochondrial targeting sequence but lacks the intact reference C-terminal region; whether it supports flavinylation or complex-II assembly is unresolved. [PMID:38569044](https://pubmed.ncbi.nlm.nih.gov/38569044/); [sequence comparison](Sdhaf2-bioinformatics/RESULTS.md).

### Location

> Mitochondrion matrix

CNN (CS 2). The reference transit peptide is entirely conserved and is consistent with the primary mouse mitochondrial-import mechanism. A reasonable family and targeting-sequence inference supports the existing matrix compartment; no exact-product imaging is claimed. [Sequence comparison](Sdhaf2-bioinformatics/RESULTS.md).

## Emitted GO claims

All 3 emitted GO claims are individually assessed in [Sdhaf2-protnlm-predictions-review.yaml](Sdhaf2-protnlm-predictions-review.yaml).

## Family integration

PTHR12469:SF2 supports Sdhaf2 ancestry. The relevant conserved function is flavoprotein maturation, distinct from SDHA catalysis. The precise C-terminal alteration requires a product-specific qualification of functional transfer, whereas the intact N-terminal targeting sequence supports mitochondrial import. No phylogenetic loss event is inferred from an alternative protein product.

## Evidence limits

Both cited papers have cached full text. The 2024 mouse study supports the Sdhaf2 import/assembly mechanism, and the 2013 study supplies the actual EMT and beta-catenin evidence. None assays A0A494B8X4 specifically. The genuine Falcon synthesis is interpreted using this exact sequence boundary; absence of a product-specific assay is not treated as demonstrated loss of function.

Exact sequence mapping: [Sdhaf2-bioinformatics/RESULTS.md](Sdhaf2-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.
