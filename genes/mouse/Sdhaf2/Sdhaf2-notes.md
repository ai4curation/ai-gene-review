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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined all 3 GOA rows, the description and core functions without using any
ProtNLM2 output.

### Identity of the benchmark accession

- A0A494B8X4 (TrEMBL, 135 aa, Ensembl ENSMUST00000237827 / ENSMUSP00000157391) is an
  **alternative product** of mouse Sdhaf2 (MGI:1913322). The reviewed canonical product is
  **Q8C6I2** (Swiss-Prot SDHF2_MOUSE, 164 aa, isoform 1). This folder is keyed to the
  alternative product; no review of Q8C6I2 exists in the repo.
- Identical to Q8C6I2 over 1-121, then an unrelated 14-residue tail (DTPEEGVGSHCRWL)
  replacing canonical 122-164. Not UniProt isoform 2 (tail GMPYAELHLGIIR) or isoform 3.
- Pfam PF03937 66-141 in Q8C6I2 vs 66-124 in A0A494B8X4 (InterPro API).
- Mapping human Q9NX18 PDB:8DYD helix features (new script
  `Sdhaf2-bioinformatics/map_structure_rereview.py`, results in `RESULTS-rereview.md`):
  transit peptide, Gly78-equivalent (mouse Gly76; PPGL2 G78R abolishes SDHA binding and
  flavination per UniProt Q9NX18) and helices up to human 115-123 are retained; helices
  human 127-132, 135-145 and the C-terminal 155-161 are lost. Activity of the truncated
  product is therefore not assumed (not shown to be lost either).

### Evolutionary grounding

- PANTHER PTHR12469:SF2 (same subfamily as canonical mouse and human SDHAF2). No
  disagreement with `interpro/panther/PTHR12469/PTHR12469-review.yaml` on subfamily placement.
- PAINT: eukaryotic node PTN000279729 has IBDs for GO:0005739, GO:0006099, GO:0006121,
  GO:0034553 (seeds SGD:S000005432 Sdh5, UniProtKB:Q9NX18, AT5G51040). No EMT, Wnt or
  protein-FAD linkage term was propagated: treated as deliberate.
- Gene-level function [PMID:19628817 "Sdh5 is required for SDH-dependent respiration and for
  Sdh1 flavination"]; human mechanism [PMID:32887801 "works in synergy with SDHAF2 to properly
  orient the flavin and capping domains of SDHA"].

### Decisions

- GO:0005759 mitochondrial matrix (IEA SubCell): ACCEPT; retained transit peptide + PAINT node.
  The UniProt SubCell line is ARBA-derived so not quoted.
- GO:0010719 negative regulation of EMT (IEA ARBA): UNDECIDED -> MARK_AS_OVER_ANNOTATED.
  The only evidence (PMID:23983127) is a knockout/knockdown EMT-marker phenotype (necessity,
  not participation) in a single cancer-context study; not in PAINT; unassayed truncated product.
- GO:0090090 negative regulation of canonical Wnt signaling (IEA ARBA): UNDECIDED ->
  MARK_AS_OVER_ANNOTATED, same reasoning.
- Core function: added one, location-only (mitochondrial matrix), with the gene-level
  SDHA-flavinylation role described but no MF asserted for this product.
- PMID:38569044 no longer used as row support (does not assay this product); retained.

### Relative to review next

Same-gene canonical product Q8C6I2 (mouse Sdhaf2, Swiss-Prot); no review in repo
(would be `genes/mouse/Sdhaf2__Q8C6I2/`). Human SDHAF2 (Q9NX18) has a complete review at
`genes/human/SDHAF2/SDHAF2-ai-review.yaml`.

Modules: `modules/mitochondrial_complex_ii.yaml` (sdhaf2_activity part),
`modules/dmel_respiratory_complex_assembly_factors.yaml`.
