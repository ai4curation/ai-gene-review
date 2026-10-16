# Provenance: taxonomic scope of experimental GO:0034727 (PMN) annotations

Source: EBI QuickGO REST API (queried Iteration 1).

## Query 1 — UniProt Q2TAZ0 (human ATG2A) GO cross-references
Endpoint: `https://rest.uniprot.org/uniprotkb/Q2TAZ0.json`

Result: 17 GO cross-references. Experimental/direct annotations are all macroautophagy:
- GO:0120013 lipid transfer activity — **IDA**
- GO:0000045 autophagosome assembly — **IMP**
- GO:0034045 phagophore assembly site membrane — **EXP**
- GO:0005789 endoplasmic reticulum membrane — **EXP**
- GO:0044232 organelle membrane contact site — **IDA**
- GO:2000786 positive regulation of autophagosome assembly — **IDA**
- GO:0010508 positive regulation of autophagy — **IMP**

Inferred-only (IBA:GO_Central) process terms (a selective-autophagy cluster):
- **GO:0034727 piecemeal microautophagy of the nucleus — IBA (only)**
- GO:0000422 autophagy of mitochondrion — IBA
- GO:0000425 pexophagy — IBA
- GO:0061709 reticulophagy — IBA
- GO:0061723 glycophagy — IBA

## Query 2 — All GO:0034727 annotations
Endpoint: `.../QuickGO/services/annotation/search?goId=GO:0034727&goUsage=exact`
- Total annotations: **59,856** (overwhelmingly IEA/IBA electronic propagation).

## Query 3 — Experimental-only GO:0034727 annotations
Filter: `evidenceCode=ECO:0000269 (EXP) & descendants`
- Total experimental hits: **44**, taxon distribution: **{559292: 44} = 100% Saccharomyces cerevisiae**.
- Distinct experimentally annotated PMN genes (yeast): ATG1–ATG18 core set, **ATG2**, **NVJ1**, **VAC8**, OSH1–OSH7 (SWH1/HES1/KES1/OSH2/3/6/7), VAM3/6/7, VPS30/33/41, YPT7, CDC48/SHP1, TRS85, SNX4, HSV2, VPS13.

## Interpretation
Experimental support for PMN exists **only** in budding yeast, and depends on the fungal-specific nucleus–vacuole junction (Nvj1–Vac8) and a vacuole. All non-yeast PMN annotations, including human ATG2A, are electronic/phylogenetic inferences (IEA/IBA). The human ATG2A GO:0034727 annotation is therefore a phylogenetic over-propagation of a lineage-restricted process.
