# LPL1 (YOR059C) Gene Review Notes

## Summary
LPL1 encodes a lipid droplet phospholipase B with dual roles in lipid metabolism and protein quality control in S. cerevisiae.

## Key Findings

### Molecular Function
- **Phospholipase B activity** - cleaves both sn-1 and sn-2 positions [PMID:25014274 "The purified Lpl1p showed phospholipase activity with broader substrate specificity, acting on all glycerophospholipids primarily at sn-2 position and later at sn-1 position"]
- Broad substrate specificity: PE, PC, PS, PA, PG
- Contains conserved GXSXG lipase motif essential for activity

### Cellular Localization
- **Lipid droplet** - primary localization confirmed by multiple studies [PMID:25014274, PMID:10515935, PMID:24868093]
- Particularly abundant in stationary phase cells
- Minor ER association detected by high-throughput study [PMID:26928762]

### Biological Roles

#### 1. Lipid Droplet Homeostasis
- Deletion causes enlarged/aberrant lipid droplets [PMID:25014274 "deletion of LPL1 resulted in altered morphology of LDs"]
- Regulates droplet phospholipid composition through hydrolysis
- Overexpression decreases glycerophospholipids and increases free fatty acids

#### 2. Protein Quality Control
- Part of Rpn4-mediated proteotoxic stress response [Weisshaar et al. 2017]
- Required for efficient proteasomal degradation under stress
- Double mutant hac1Δ lpl1Δ shows severe stress sensitivity and accumulates ubiquitinated proteins
- Links lipid droplet function with proteostasis

### Regulation
- Induced by Rpn4 transcription factor under proteotoxic stress
- Contains PACE element in promoter for Rpn4 binding
- Expression increases in stationary phase

## Annotation Review Decisions

### Key Changes Made:
1. **ACCEPT**: phosphatidylcholine, phosphatidylethanolamine, and phosphatidylglycerol reaction-level lipase activities as specific slices of Lpl1's broader B-type glycerophospholipase activity (GO:0102545)
2. **RETIRE/REMOVE**: monoacylglycerol lipase activity, now absent from live GOA, because PAINT places that activity on the ROG1 paralog branch
3. **ACCEPT**: lipid droplet localization from multiple supporting studies
4. **KEEP_AS_NON_CORE**: ER and cytoplasm localizations as minor, broad, or contextual sites

### Missing Annotations Identified:
- B-type glycerophospholipase activity (GO:0102545) as the summarizing core activity
- Lipid droplet organization (GO:0034389)

## Evolutionary Context
- Paralog of ROG1 (monoacylglycerol lipase) in yeast
- Distant homologs in mammals (FAM135A/B) but function not characterized
- Member of conserved ROG1 lipase family

## References
- Selvaraju et al. 2014 (PMID:25014274) - Biochemical characterization
- Weisshaar et al. 2017 (PMID:28100635) - Proteostasis role
- Athenstaedt et al. 1999 (PMID:10515935) - Early lipid droplet localization

## 2026-09-28 IBA re-review

- Re-reviewed the GOA IBAs against `projects/IBA_REVIEW.md`. The `GO:0004622` IBA should be `ACCEPT`: `PANTHER:PTN000280739` plus the LPL1 self-source support conserved phosphatidylcholine lysophospholipase A1 activity as one reaction-level component of experimentally shown B-type glycerophospholipase activity, and the self-source is legitimate rather than circular.
- The `GO:0047372` IBA should remain `REMOVE`. The GOA trace `PANTHER:PTN000773837|SGD:S000003112` is the ROG1 monoacylglycerol-lipase branch called out in the IBA project; Selvaraju et al. showed Lpl1 acts on glycerophospholipids, and I found no direct monoacylglycerol lipase evidence for Lpl1.
- Re-read Weisshaar et al. 2017. Lpl1 is Rpn4-induced and hac1delta lpl1delta cells have protein-degradation defects, but lpl1delta alone did not stabilize CPY* or Delta2-GFP in the assays, so I removed proposed `NEW` rows for `GO:0043161` and `GO:0071218`; the paper supports a lipid-droplet/proteostasis link rather than direct execution of proteasome-mediated catabolism.
- A newer-paper search did not find primary LPL1 studies after Weisshaar et al. that change the phospholipase/lipid-droplet model; recent hits were reviews or database pages.

## 2026-10-01 current-GOA and PAINT refresh

- Forced a fresh GOA/UniProt refresh. The live feed now has 20 LPL1 source assertions: six frozen rows disappeared, 11 frozen rows are retained with GOA qualifier backfills, and nine rows are newly live. The retired rows are the old `GO:0047372` monoacylglycerol-lipase IBA plus five older UniProt mappings for duplicate lipid droplet, broad lipid-metabolism, membrane, lipid-catabolism, and hydrolase assertions. The old monoacylglycerol-lipase removal has therefore been retired upstream, matching the September ROG1-paralog assessment.
- Cached `interpro/panther/PTHR12482/PTHR12482-paint.tsv`. Current PAINT places broad lipase activity at PTN000280657 with both ROG1 and LPL1 seeds, lipid metabolism at the same node from the ROG1 seed, lipid-droplet localization plus PC and PE lysophospholipase activity at the LPL1-specific PTN000280739 node, monoacylglycerol lipase at the ROG1-side PTN000773838 node, and broad cytoplasm at PTN000967933. The LPL1-specific PTN000280739 transfers are sound and retained as reaction-level components of experimentally demonstrated B-type glycerophospholipase activity.
- UniProt and Rhea now add `GO:0004623`, `GO:0008970`, and `GO:0120559` rows from the Selvaraju et al. enzymology. These are supported half-reactions or substrate-specific slices within the same B-type glycerophospholipase sequence, so they are retained as correct reaction-level annotations alongside the broader `GO:0102545` core function.
- Literature search on 2026-10-01 found recent 2025 yeast lipid-droplet papers on Pln1/microlipophagy and lipid-droplet adaptation, but no newer LPL1-specific primary paper that supersedes the Selvaraju 2014 phospholipase/lipid-droplet study or the Weisshaar 2017 Rpn4/proteostasis study.
