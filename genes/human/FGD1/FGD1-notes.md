# FGD1 literature journal

## 2026-10-26 — CDC42 exchange and spatial targeting

FGD1 promotes guanine nucleotide exchange on CDC42. The original human biochemical study used residues 330–710, encompassing the DH and first PH domains. GDP release and GTPγS loading were measured on Sf9-derived CDC42; bacterial CDC42 behaved differently. This is exchange activity, not stimulation of GTP hydrolysis. The same study measured CDC42-dependent actin responses in mouse fibroblast recipients ([PMID:8969170](https://pubmed.ncbi.nlm.nih.gov/8969170/), Methods, Results and Figures 1–4).

The mouse ortholog study used full-length 960-residue Fgd1 and engineered targeting constructs. Its Figure 4 and accompanying Results distinguish cytoplasmic/Golgi pools from recruitment to ruffles and lamellipodia after stimulation. Altered targeting changed actin patterns and cell shape; Table 1 and Figures 6–7 document the construct-dependent effects. Direct binding to cortactin and mAbp1 domains does not establish direct FGD1–actin binding. The study explicitly reports that protein instability prevented endogenous coimmunoprecipitation ([PMID:12913069](https://pubmed.ncbi.nlm.nih.gov/12913069/), Results, Discussion and construct Methods).

Human HPA image assignments independently support cytosolic and peripheral membrane association. These observations support locations without establishing membrane-spanning topology. Reactome target-member routes support cytosolic CDC42 GEF activity; membership in a broader generic GEF set does not establish RAC or RhoA substrate specificity. The four PAINT assertions retain their verified ancestral placement and exact human sequence match, including legitimate target self-WITH evidence.

The integrated review contains 34 decisions and 15 complete reference assessments: 11 ACCEPT, 14 KEEP_AS_NON_CORE, six TOO_GENERAL, two MODIFY and one UNDECIDED. The original Aarskog–Scott positional-cloning abstract establishes genetic association, but the inaccessible original experimental body leaves the animal-organ-morphogenesis assertion explicitly uncertain. No new annotation or publication quotation is added.

The human canonical 961-residue chain, human assay fragment and mouse donor constructs remain separate. There are no curated natural splice or cleavage products in this intake. The [direct source guide](FGD1-direct-source-guide.md), [database source guide](FGD1-database-source-guide.md), [direct notes](FGD1-direct-notes.md) and [database notes](FGD1-database-notes.md) give precise source scopes and access limits. The genuine configured provider invocation produced no report; these are authored notes, not a substitute provider report.

## Ontology refinement after review

Current QuickGO definitions and both typed ancestor and descendant responses support GO:0090630 for exchange-mediated GTPase activation and GO:0032489 for CDC42-specific signaling regulation. The two existing MODIFY decisions and the core process now preserve those distinctions. GO:0005085 and GO:0031267 have no narrower typed descendants in the captured responses. The original term endpoint also supplied a children field; the new explicit descendant receipt makes that boundary easier to audit. See [ontology evidence](FGD1-ontology-evidence.yaml).

The original organ-morphogenesis source remains UNDECIDED: genetic necessity and a multisystem phenotype do not by themselves resolve the protein’s participation in that specific process. The computed workflow status does not remove that source-specific uncertainty. No additional CCPG1 function is inferred from a by-similarity domain comment.

## 2026-11-15 ORGANELLES Golgi batch 2 (Golgi apparatus rows)

- Rows: IEA GO_REF:0000107 (Ensembl, mouse P52734) and ISS GO_REF:0000024 (mouse P52734), both `located_in`,
  both stay KEEP_AS_NON_CORE. Donor paper PMID:12913069 is abstract-only in the cache; the earlier review's
  Figure 4 reading came from an author-uploaded original that I did not re-read.
- Added Egorov et al. 2009 (PMID:19261807, PMC2675621, DOI 10.1091/mbc.e08-11-1136), not previously cited. The
  cached file is the abstract; the PubMed full-text tool returned no body, so I read the PMC HTML article page.
  Not quoted beyond the abstract. What I read: GFP-FGD1 in HeLa and MC3T3 cells lies in cytoplasm, plasma
  membrane and Golgi; overlaps TGN46 more than GM130 (quantified); immuno-EM (nanogold, nanogold/HRP with
  TGN38-HRP, cryo-immunogold) puts it on the trans side of the stack and TGN membranes. FGD1 siRNA in HeLa
  cuts post-Golgi carrier formation by about 70% without blocking transport to or through the Golgi, rescued
  by mouse Fgd1 but not the FGD1-AS mutant; Golgi Cdc42 is lost or reduced in silenced cells.
- No TGN row: all localization is on overexpressed tagged protein, and FGD1 is a recruited soluble GEF that
  stays at the root under the ORGANELLES rules for recruited proteins.
- Judgement call: ACCEPT (core) would also be defensible, because the TGN-export role is a Cdc42 activity
  shown at the Golgi; kept non-core because the core function as written covers the cytosolic and
  plasma-membrane pools. Curation gap (not done here): the Golgi-to-plasma-membrane export role of PMID:19261807
  has no process annotation in GOA or in this review.
