---
title: "Yeast Metabolic Engineering & Bioproduction"
maturity: MATURE
tags: [BIOLOGY_DOMAIN, FLAGSHIP, PIPELINE, EVALUATION]
species: [yeast]
genes: [PDC1, ADH1, ADH2, GPD1, GPD2, HXK1, HXK2, GLK1, PFK1, PFK2, PYC1, PYC2, TDH1, TDH2, TDH3, ZWF1, BNA3, BNA7, DAL3, "DUR1,2", ERG26]
last_reviewed: '2026-11-04'
autolink_gene_symbols: false
manifest:
  slides:
    - href: YEAST_METABOLIC_ENGINEERING/slides/YEAST_METABOLIC_ENGINEERING-slides.html
      description: Yeast metabolic engineering slides
---

# Yeast Metabolic Engineering & Bioproduction

**Bottom line:** All 10 original central-carbon metabolic engineering target
genes (`PDC1`, `ADH1`, `ADH2`, `GPD1`, `GPD2`, `HXK1`, `PFK1`, `PYC1`, `TDH1`,
`ZWF1`) and their 6 key paralogs (`HXK2`, `GLK1`, `PFK2`, `PYC2`, `TDH2`,
`TDH3`) now have curated reviews under `genes/yeast/` and are organized into 5
curated pathway modules (`modules/alcoholic_fermentation.yaml`,
`modules/glycerol_metabolism.yaml`, `modules/emp_glycolysis.yaml`,
`modules/pentose_phosphate_pathway.yaml`, and
`modules/pyruvate_metabolism.yaml`). Applying a curation-aware ChatGEM +
COBRApy audit to the BiGG *S. cerevisiae* genome-scale model `iMM904` across all
540 aligned `genes/yeast/` reviews ([`YEAST_METABOLIC_ENGINEERING/RESULTS.md`](YEAST_METABOLIC_ENGINEERING/RESULTS.md))
exposed concrete model defects that distort metabolic engineering predictions:

1. **`GPD2` (`YOL059W`) Compartment & GPR Misassignment**: `iMM904` assigns
   `GPD1` (`YDL022W`) alone to cytosolic `G3PD1ir` and restricts `GPD2`
   (`YOL059W`) exclusively to mitochondrial matrix `G3PD1irm`, where
   irreversible transport (`GLYC3Ptm`) prevents it from contributing to
   glycerol synthesis. Combined with three cryptic anaerobic redox bypasses in
   `iMM904` (catabolic `GCY1`/`DAK` glycerol-DHA cycling, soluble mitochondrial
   `fadh2_m` fumarate respiration via `GUT2`/Complex II, and unconstrained
   NADH-GOGAT `GLT1`), unmodified `iMM904` secretes zero anaerobic glycerol
   (`EX_glyc_e = 0.0`) and predicts that a single `gpd1Δ` knockout abolishes all
   glycerol production while `gpd2Δ` has no effect. Repairing `G3PD1ir` to
   `YDL022W or YOL059W` (`GPD1 or GPD2`) and closing the non-physiological
   anaerobic loops restores wild-type anaerobic glycerol secretion
   (`1.3114 mmol/gDW/h`), preserves glycerol synthesis in single `gpd1Δ` and
   `gpd2Δ` mutants, and restricts glycerol loss to the `gpd1Δ gpd2Δ` double
   mutant (`PMID:9171333`).
2. **Central-Carbon Flux-Routing Artifacts (`PFK_3`/`FBA3`/`TALA` and `GLUK`)**:
   In standard aerobic FBA on `iMM904`, canonical phosphofructokinase (`PFK`)
   and fructose-bisphosphate aldolase (`FBA`) carry **`0.0` flux** because
   100% of glycolytic flux (`8.9249 mmol/gDW/h`) detours through reverse
   transaldolase (`TALA`) + sedoheptulose-7-phosphate kinase (`PFK_3`) +
   sedoheptulose-1,7-bisphosphate aldolase (`FBA3`), while 87.1% of glucose
   phosphorylation routes through `GLUK` (`GLK1`-only, producing $\beta$-D-G6P)
   rather than `HEX1` (`HXK1 or HXK2 or GLK1`).
3. **Strict `AND` GPR on `PFK1`/`PFK2` vs. Partial Subunit Compensation**:
   `iMM904` models `PFK` with `YGR240C and YMR205C` (`PFK1 and PFK2`), so single
   `pfk1Δ` or `pfk2Δ` knockouts abolish PFK flux (`0.0`) and ethanol
   fermentation (`EX_etoh_e = 0.0`, growth reduced to 24.9% via the pentose
   phosphate shunt), whereas experimental yeast genetics (`PFK1-ai-review.yaml`)
   shows single `pfk1Δ` or `pfk2Δ` mutants still ferment glucose and only the
   `pfk1Δ pfk2Δ` double mutant is glucose-negative.
4. **Proteome-Wide `CLASS_CHANGE` Errors Catching Obsolete/Bacterial Reactions**:
   Across all 540 reviewed yeast genes in `iMM904`, 26 exhibit enzyme class
   discrepancies (`CLASS_CHANGE`), including `DAL3` (`YIR032C`, modeled as
   bacterial ureidoglycolate hydrolase `EC 3.5.3.19` releasing free $\text{NH}_4^+$
   rather than yeast ureidoglycolate lyase `EC 4.3.2.3` releasing urea, which
   falsely makes `dur1,2Δ` 100% viable on allantoin), `BNA3` (`YJL060W`,
   assigned to arylformamidase `FKYNH` `EC 3.5.1.9` instead of `BNA7`/`YDR428C`
   alongside an orphan prokaryotic `ASPOcm`/`QULNS` aspartate-to-quinolinate
   bypass), and `ERG26` (`YGL001C`, tagged with steroid isomerase `EC 5.3.3.1`
   instead of C-3 sterol dehydrogenase/decarboxylase `EC 1.1.1.170`).

## Overview

This project reviews *Saccharomyces cerevisiae* genes central to metabolic engineering for bioproduction and audits their representation in genome-scale metabolic reconstructions (`iMM904`). Recent computational studies (`ecFactory`, 2024; `ChatGEM`, 2025) identify key genetic targets for optimizing production of bioethanol, specialty chemicals, and renewable fuels:

1. **Primary alcohol production pathway** — ethanol fermentation (`PDC1`, `PDC5`, `PDC6`, `ADH1`, `ADH2`)
2. **Byproduct suppression & osmotic/anaerobic redox balance** — glycerol synthesis and catabolism (`GPD1`, `GPD2`, `GPP1`, `GPP2`, `GUT1`, `GUT2`, `GCY1`, `DAK1`, `DAK2`)
3. **Upper & lower glycolysis** — hexokinase/glucokinase and GAPDH paralog pairs (`HXK1`, `HXK2`, `GLK1`, `PFK1`, `PFK2`, `TDH1`, `TDH2`, `TDH3`)
4. **PPP & anaplerotic support** — NADPH supply and cytosolic pyruvate carboxylation (`ZWF1`, `PYC1`, `PYC2`)

## Curated Pathway Modules

| Module YAML | Pathway Scope | Key Reviewed Yeast Genes |
|---|---|---|
| [`modules/alcoholic_fermentation.yaml`](../modules/alcoholic_fermentation.yaml) | Pyruvate decarboxylation to acetaldehyde and NADH-dependent reduction to ethanol | `PDC1`, `PDC5`, `PDC6`, `ADH1`, `ADH2`, `ADH3`, `ADH4`, `ADH5` |
| [`modules/glycerol_metabolism.yaml`](../modules/glycerol_metabolism.yaml) | Biosynthetic glycerol-3-P dehydrogenase/phosphatase redox sink (`GPD1/2`, `GPP1/2`), glycerol kinase/Gut2 shuttle (`GUT1/2`), and catabolic DHA route (`GCY1`, `DAK1/2`) | `GPD1`, `GPD2`, `GPP1`, `GPP2`, `GUT1`, `GUT2`, `GCY1`, `DAK1`, `DAK2` |
| [`modules/emp_glycolysis.yaml`](../modules/emp_glycolysis.yaml) | Embden–Meyerhof–Parnas glycolytic trunk from D-glucose to pyruvate | `HXK1`, `HXK2`, `GLK1`, `PGI1`, `PFK1`, `PFK2`, `FBA1`, `TPI1`, `TDH1`, `TDH2`, `TDH3`, `PGK1`, `GPM1`, `ENO1`, `ENO2`, `CDC19`, `PYK2` |
| [`modules/pentose_phosphate_pathway.yaml`](../modules/pentose_phosphate_pathway.yaml) | Oxidative NADPH-generating branch and non-oxidative pentose phosphate rearrangements | `ZWF1`, `SOL3`, `SOL4`, `GND1`, `GND2`, `RPE1`, `RKI1`, `TKL1`, `TKL2`, `TAL1`, `NQM1` |
| [`modules/pyruvate_metabolism.yaml`](../modules/pyruvate_metabolism.yaml) | Cytosolic pyruvate carboxylation (`PYC1/2`), PDH complex, and acetyl-CoA synthetase bypass | `PYC1`, `PYC2`, `PDA1`, `PDB1`, `LAT1`, `LPD1`, `ACS1`, `ACS2` |

## ChatGEM + COBRApy Curation Audit Summary

Full quantitative tables, simulation provenance, and reproducibility checklists are in [`YEAST_METABOLIC_ENGINEERING/RESULTS.md`](YEAST_METABOLIC_ENGINEERING/RESULTS.md), generated by [`YEAST_METABOLIC_ENGINEERING/run_yeast_gem_audit.py`](YEAST_METABOLIC_ENGINEERING/run_yeast_gem_audit.py) with structured outputs in `projects/YEAST_METABOLIC_ENGINEERING/out/`:

- [`YEAST_METABOLIC_ENGINEERING/out/proteome_ec_gpr_alignment.yaml`](YEAST_METABOLIC_ENGINEERING/out/proteome_ec_gpr_alignment.yaml) — Alignment of 540 reviewed `genes/yeast/` genes against `iMM904` (234 `EXACT_MATCH`, 155 `SAME_CLASS_EC_DIFF`, 88 `MODEL_MISSING_EC`, 26 `CLASS_CHANGE`, 15 `UNIPROT_MISSING_EC`, 11 `BOTH_NO_EC`, 10 `COMPLEX_SUBUNIT_EC_PROPAGATION`, 1 `EC7_TRANSLOCASE_RECLASS`).
- [`YEAST_METABOLIC_ENGINEERING/out/target_genes_audit.yaml`](YEAST_METABOLIC_ENGINEERING/out/target_genes_audit.yaml) — Detailed EC, compartment, and AST-GPR audit for the 16 central-carbon target and paralog genes.
- [`YEAST_METABOLIC_ENGINEERING/out/fba_vs_pfba_routing.yaml`](YEAST_METABOLIC_ENGINEERING/out/fba_vs_pfba_routing.yaml) — Standard FBA vs. parsimonious FBA flux distributions under aerobic and anaerobic glucose conditions, demonstrating the `PFK_3`/`FBA3`/`TALA` and `GLYCDy`/`DHAK` bypasses.
- [`YEAST_METABOLIC_ENGINEERING/out/knockout_and_repair_experiments.yaml`](YEAST_METABOLIC_ENGINEERING/out/knockout_and_repair_experiments.yaml) — Single and double paralog knockouts before and after curation-guided repairs for `GPD1`/`GPD2`, `DAL3`/`DUR1,2`, and `BNA3`/`BNA7`.
- [`YEAST_METABOLIC_ENGINEERING/out/ast_eflux_conditions.yaml`](YEAST_METABOLIC_ENGINEERING/out/ast_eflux_conditions.yaml) — Benchmark of AST-based E-Flux vs. ChatGEM's regex GPR parser (`46._automatic_E_flux.py`) and condition-specific isozyme capacities across aerobic glucose, anaerobic glucose, hyperosmotic stress, and aerobic ethanol regimes.

---

# STATUS

Last updated: 2026-11-04

## Reviewed Central-Carbon Target & Paralog Genes

- [x] `PDC1` (`YLR044C`, `COMPLETE`) — Pyruvate decarboxylase 1 (major cytosolic decarboxylase; `genes/yeast/PDC1/PDC1-ai-review.yaml`)
- [x] `ADH1` (`YOL086C`, `COMPLETE`) — Alcohol dehydrogenase 1 (primary fermentative acetaldehyde reductase; `genes/yeast/ADH1/ADH1-ai-review.yaml`)
- [x] `ADH2` (`YMR303C`, `COMPLETE`) — Alcohol dehydrogenase 2 (glucose-repressed oxidative ethanol dehydrogenase; `genes/yeast/ADH2/ADH2-ai-review.yaml`)
- [x] `GPD1` (`YDL022W`, `COMPLETE`) — Glycerol-3-phosphate dehydrogenase 1 (HOG1-induced osmotic glycerol synthesis; `genes/yeast/GPD1/GPD1-ai-review.yaml`)
- [x] `GPD2` (`YOL059W`, `COMPLETE`) — Glycerol-3-phosphate dehydrogenase 2 (anaerobic NADH redox-sink glycerol synthesis; `genes/yeast/GPD2/GPD2-ai-review.yaml`)
- [x] `HXK1` (`YFR053C`, `DRAFT`) — Hexokinase 1 (glucose-repressed hexokinase isozyme; `genes/yeast/HXK1/HXK1-ai-review.yaml`)
- [x] `HXK2` (`YGL253W`, `DRAFT`) — Hexokinase 2 (predominant glucose-phosphorylating hexokinase on high glucose; `genes/yeast/HXK2/HXK2-ai-review.yaml`)
- [x] `GLK1` (`YCL040W`, `COMPLETE`) — Glucokinase 1 (aldohexose-specific glucokinase; `genes/yeast/GLK1/GLK1-ai-review.yaml`)
- [x] `PFK1` (`YGR240C`, `DRAFT`) — Phosphofructokinase $\alpha$-subunit (`genes/yeast/PFK1/PFK1-ai-review.yaml`)
- [x] `PFK2` (`YMR205C`, `DRAFT`) — Phosphofructokinase $\beta$-subunit (`genes/yeast/PFK2/PFK2-ai-review.yaml`)
- [x] `PYC1` (`YGL062W`, `COMPLETE`) — Pyruvate carboxylase 1 (`genes/yeast/PYC1/PYC1-ai-review.yaml`)
- [x] `PYC2` (`YBR218C`, `COMPLETE`) — Pyruvate carboxylase 2 (`genes/yeast/PYC2/PYC2-ai-review.yaml`)
- [x] `TDH1` (`YJL052W`, `DRAFT`) — Glyceraldehyde-3-phosphate dehydrogenase 1 (stationary/stress-induced isozyme; `genes/yeast/TDH1/TDH1-ai-review.yaml`)
- [x] `TDH2` (`YJR009C`, `DRAFT`) — Glyceraldehyde-3-phosphate dehydrogenase 2 (`genes/yeast/TDH2/TDH2-ai-review.yaml`)
- [x] `TDH3` (`YGR192C`, `DRAFT`) — Glyceraldehyde-3-phosphate dehydrogenase 3 (major glycolytic GAPDH isozyme; `genes/yeast/TDH3/TDH3-ai-review.yaml`)
- [x] `ZWF1` (`YNL241C`, `DRAFT`) — Glucose-6-phosphate dehydrogenase (`genes/yeast/ZWF1/ZWF1-ai-review.yaml`)

## Additional `iMM904` `CLASS_CHANGE` Genes Audited & Repaired in COBRApy

- [x] `BNA3` (`YJL060W`, `DRAFT`) & `BNA7` (`YDR428C`, `COMPLETE`) — Corrected `FKYNH` (`EC 3.5.1.9`) assignment from `BNA3` (kynurenine aminotransferase `EC 2.6.1.7`) to `BNA7` and removed non-yeast prokaryotic `ASPOcm`/`QULNS` bypass.
- [x] `DAL3` (`YIR032C`, `DRAFT`) & `DUR1,2` (`YBR208C`, `DRAFT`) — Corrected `UGLYCH` from bacterial ureidoglycolate hydrolase (`EC 3.5.3.19`) to yeast ureidoglycolate lyase (`EC 4.3.2.3`), restoring essentiality of `DUR1,2` on allantoin.
- [x] `ERG26` (`YGL001C`, `COMPLETE`) — Identified inherited BiGG `EC 5.3.3.1` (steroid isomerase) misannotation on C-3 sterol dehydrogenase/decarboxylase (`EC 1.1.1.170`).

## Progress

- Core target + paralog genes reviewed: 16 / 16 (7 `COMPLETE`, 9 `DRAFT`)
- Proteome-wide reviewed yeast genes aligned to `iMM904`: 540 / 905
- Curated yeast central-carbon modules: 5 (`alcoholic_fermentation`, `glycerol_metabolism`, `emp_glycolysis`, `pentose_phosphate_pathway`, `pyruvate_metabolism`)

---

# NOTES

## 2026-11-04

- Completed ChatGEM + COBRApy curation audit of *S. cerevisiae* `iMM904` across all 16 target/paralog central-carbon genes, 5 curated metabolic modules, and 540 aligned `genes/yeast/` reviews (`projects/YEAST_METABOLIC_ENGINEERING/run_yeast_gem_audit.py` and `projects/YEAST_METABOLIC_ENGINEERING/RESULTS.md`).
- Demonstrated curation-guided model repairs for `GPD1`/`GPD2` anaerobic glycerol secretion, `PFK_3`/`FBA3` glycolytic routing degeneracy, `DAL3`/`DUR1,2` allantoin catabolism, `BNA3`/`BNA7` de novo $\text{NAD}^+$ synthesis, and AST-based E-Flux condition-specific isozyme disambiguation.

## 2025-12-30

- Project initialized
- Selected metabolic engineering & bioproduction as focus area
- Identified 10 candidate genes spanning primary alcohol production, byproduct suppression, and central carbon metabolism
