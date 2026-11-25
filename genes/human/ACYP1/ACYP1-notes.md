# ACYP1 notes

## GOA and family

- `ACYP1-goa.tsv` has 4 annotation rows, so the QuickGO fetch did not produce a header-only file.
- Human `ACYP1` and `ACYP2` are the only reviewed human members of `PTHR10029`.
- ACYP1 is `PTHR10029:SF21`; ACYP2 is `PTHR10029:SF20`.
- PAINT has one current `PTHR10029` IBD row, placing `GO:0003998` acylphosphatase activity at `PANTHER:PTN000003030`.
- `just paint-losses human ACYP1` found no IRD or IKR loss on the ACYP1 lineage.
- No production GO-CAM in `gocams/index.tsv` references `UniProtKB:P07311`, and the two human acylphosphatases are alternative monomeric enzymes rather than a multi-part biological module.

## Row calls

- The `GO:0003998` IBA, IEA and TAS rows were accepted. PMID:3026468 purified the human erythrocyte isozyme and reported that it hydrolyzes acyl phosphates [PMID:3026468 "The erythrocyte enzyme shows hydrolytic activity on acyl phosphates with higher affinity than the muscle enzyme for some substrates and phosphorylated inhibitors."]; PMID:7796909 cloned the erythrocyte cDNA and expressed an active recombinant enzyme [PMID:7796909 "kinetic characteristics very similar to those of the native protein"].
- `GO:0006796` is true but too broad and was modified to `GO:0016311` dephosphorylation. QuickGO reported `GO:0016311` as a current biological-process term whose `is_a` ancestors include `GO:0006796`, and PMID:3026468 plus the UniProt catalytic-activity line support hydrolytic removal of phosphate from acyl phosphates [PMID:3026468 "shows hydrolytic activity on acyl phosphates"].
- PMID:1645713 was treated as ACYP1/erythrocyte context, not ACYP2 evidence: acylphosphatase purified from human erythrocytes hydrolyzed the red-cell Ca2+-ATPase phosphoenzyme at enzyme amounts "that fall within the physiological range" and lowered ATP/Ca2+ coupling [PMID:1645713 "A stoichiometry of 2.04 Ca2+/ATP hydrolyzed was calculated in the absence of acylphosphatase; in the presence of acylphosphatase optimal concentration, this ratio was reduced to 0.9."].

## Literature and structures

- Perplexity deep research could not run in this checkout because the wrapper reported `Provider 'perplexity' not available. Available: claude_code`; I recorded a manual deep-research note instead of fabricating a `-deep-research-perplexity.md` provider file.
- The ACYP1 UniProt record cites two structural studies. Yeung et al. crystallized human common-type acylphosphatase and collected 1.45 A diffraction data [PMID:16511269 "Diffraction data were collected to 1.45 A resolution at 100 K."], and Gribenko et al. solved NMR structures while testing charge-charge redesigns that retained activity and oligomeric state [PMID:19196981 "The increase in stability is not accompanied by significant changes in structure, oligomerization state, or, most importantly, activity of the designed AcPh or Cdc42."].
- The structural-paper introduction summarizes the unsettled substrate landscape: acylphosphatase can hydrolyze 1,3-bisphosphoglycerate and pump beta-aspartyl-phosphate intermediates, while "The biological role of acylphosphatase is not fully understood" [PMID:16511269 "The biological role of acylphosphatase is not fully understood."]. The review now records that as a BIOLOGY knowledge gap rather than as a suggested experiment without provenance.
