# SCP2D1 Gene Review Notes

## Gene Overview

**SCP2D1** (Sterol Carrier Protein 2 Domain Containing 1) - Small 156 AA protein containing an SCP2 sterol-binding domain. Poorly characterized/unstudied protein with function inferred from domain homology.

**Key characteristics:**
- Contains SCP2 (sterol carrier protein 2) domain with large hydrophobic cavity
- NOT an enzyme - functions as lipid carrier/transfer protein
- Highly testis-specific expression (~53-fold enrichment vs other tissues)
- No experimental functional studies - all annotations based on homology (IEA)
- Protein not yet detected - evidence at transcript level only

## Function (Inferred from Homology to SCP2)

### Lipid Binding and Transfer
- **Non-specific lipid transfer protein** in intracellular lipid metabolism
- Binds cholesterol, fatty acids, fatty acyl-CoA in hydrophobic cavity
- Shuttles lipids through cytosol between membranes/organelles
- No catalytic activity - pure carrier function

### Subcellular Localization
- **Cytosolic** (predicted, IBA annotation GO:0005829)
- No peroxisomal targeting sequence (unlike paralog SCP2)
- No transmembrane domains - diffuses freely in cytoplasm
- Not secreted (lacks signal peptide)

## Tissue Expression

**Highly testis-restricted:**
- GTEx: ~53-fold higher in testis vs other tissues
- Human Protein Atlas: "Tissue enriched in testis"
- Most other tissues: extremely low or absent expression
- Suggests specialized role in male reproduction

**Potential roles in testis:**
1. Spermatogenesis - lipid supply for sperm membrane remodeling
2. Steroidogenesis - cholesterol transport for testosterone synthesis in Leydig cells

## Comparison to SCP2

| Feature | SCP2 | SCP2D1 |
|---------|------|--------|
| Size | 13 kDa (from larger precursor) | 156 AA standalone |
| Localization | Peroxisomes + cytosol | Cytosol only |
| PTS signal | Yes (AKL motif) | No |
| Expression | Ubiquitous | Testis-specific |
| Characterized | Yes (well-studied) | No (unstudied) |

## Predicted Protein Interactions (STRING)

**Lipid metabolism enzymes:**
- HADHB - mitochondrial β-oxidation (fatty acids)
- ECI2 - peroxisomal enoyl-CoA isomerase
- AMACR - bile acid metabolism
- ACAT1/ACAT2 - cholesterol esterification

**Cholesterol/membrane proteins:**
- STOML1 - cholesterol transport to endosomes
- EHD3 - endosomal membrane recycling

Note: All interactions PREDICTED, not experimentally validated

## Current Evidence Level

**Very low - uncharacterized protein:**
- No biochemical assays on SCP2D1
- No structural studies of SCP2D1 specifically
- No knockout studies
- No disease associations
- Protein not detected by proteomics (transcript-level evidence only)

All functional assertions are **inferred from homology** to well-studied SCP2.

## Annotation Strategy

**Only 1 GO annotation to review:**
- GO:0005829 (cytosol) - IBA evidence based on phylogenetic inference

**Decision:** ACCEPT
- Consistent with predicted intracellular/cytosolic localization
- No peroxisomal targeting sequence
- Supported by computational predictions and domain analysis

## Core Functions to Define

Since function is largely unknown, use root terms:
1. Lipid binding (predicted from SCP2 domain)
2. Cytosolic localization (IBA supported)

Avoid over-annotation - this is an uncharacterized protein with no experimental data.
