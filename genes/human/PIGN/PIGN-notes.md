# PIGN review notes

Gene: PIGN (HGNC:8967), UniProt O95427, human (NCBITaxon:9606)
Product name: GPI ethanolamine phosphate transferase 1 (GPI-ET-I / GPI-ethanolamine transferase I / PIG-N / MCD4 homolog)

## Verified biology (grounded in PIGN-uniprot.txt, GOA, cached Reactome/PMID)

PIGN is an **ethanolamine phosphate (EtNP) transferase** of the ER that acts in
glycosylphosphatidylinositol (GPI) anchor biosynthesis. It transfers ethanolamine
phosphate from phosphatidylethanolamine (PE) onto the **2-OH of the first
(alpha-1,4-linked) mannose** of the GPI intermediate.

UniProt FUNCTION [file:human/PIGN/PIGN-uniprot.txt]:
"Ethanolamine phosphate transferase that catalyzes an ethanolamine phosphate (EtNP)
transfer from phosphatidylethanolamine (PE) to the 2-OH position of the first
alpha-1,4-linked mannose ... participates in the eighth step of the
glycosylphosphatidylinositol-anchor biosynthesis (By similarity)."

- Family: "Belongs to the PIGG/PIGN/PIGO family. PIGN subfamily." — the three human
  paralogs each add EtNP to a different mannose (PIGN → Man1; PIGO → Man3, the bridging
  EtNP that links the anchor to protein; PIGG → Man2).
- PATHWAY: "Glycolipid biosynthesis; glycosylphosphatidylinositol-anchor biosynthesis."
  (UniPathway UPA00196).
- Localization: "Endoplasmic reticulum membrane ... Multi-pass membrane protein"; the
  UniProt topology has 13 TM helices (multi-pass ER membrane protein), consistent with
  ER membrane (GO:0005789).
- MCAHS1: "Multiple congenital anomalies-hypotonia-seizures syndrome 1 (MCAHS1)
  [MIM:614080]" — autosomal recessive; neonatal hypotonia, seizures, dysmorphism,
  congenital anomalies (PubMed:21493957, variant R709Q).
- A secondary/moonlighting claim: "May act as suppressor of replication stress and
  chromosome missegregation (PubMed:23446422)." This is a screen-derived observation,
  not the core evolved GPI-biosynthesis function.

## GOA MF term (exact current term to use)

GOA (genes/human/PIGN/PIGN-goa.tsv) carries the MF as:
- **GO:0051377 "mannose-ethanolamine phosphotransferase activity"** (verified current,
  MF aspect, not obsolete via QuickGO). This is the exact term used in core_functions.

Core BP: GO:0006506 "GPI anchor biosynthetic process" (verified current, BP aspect).
Core CC: GO:0005789 "endoplasmic reticulum membrane" (verified current, CC aspect).

## Reactome

- R-HSA-162710 "Synthesis of glycosylphosphatidylinositol (GPI)" — pathway; TAS
  support for GO:0006506.
- R-HSA-162798 "mannose(a1-4)glucosaminyl-acyl-PI + phosphatidylethanolamine ->
  (ethanolamineP) mannose(al1-4)glucosaminyl-acyl-PI + diacylglycerol" — the specific
  EtNP-transfer reaction (sixth step of GPI synthesis per Reactome; UniProt calls it the
  eighth step under a finer-grained numbering). Supports the EtNP-transferase MF and ER
  membrane CC. Reactome summary: "a phosphoethanolamine group is transferred from
  phosphatidylethanolamine onto the first mannose of the GPI precursor."

## Annotation-by-annotation decisions

Total GOA lines: 16 (rows 2-18 of TSV).

MF GO:0051377 (IBA, IEA-InterPro, ISS, TAS-Reactome) — core catalytic activity; ACCEPT all.
MF GO:0016740 transferase activity (IEA InterPro) — correct parent, less informative;
  MARK_AS_OVER_ANNOTATED (redundant with the specific GO:0051377).
BP GO:0006506 (IBA, IEA, TAS, ISS) — core biological process; ACCEPT all.
CC GO:0005789 ER membrane (IBA is_active_in, IEA, ISS, TAS) — correct core location; ACCEPT all.
CC GO:0016020 membrane (IEA InterPro; HDA proteomics PMID:19946888) — true but generic;
  MARK_AS_OVER_ANNOTATED (subsumed by ER membrane; HDA is a bulk membrane-proteome MS study).
CC GO:0005829 cytosol (IDA HPA) — PIGN is a multi-pass ER membrane protein; a soluble
  cytosolic pool is not its site of function. HPA IF can pick up antibody background /
  over-expression signal. MARK_AS_OVER_ANNOTATED (do not REMOVE an IDA per policy).
CC GO:0005886 plasma membrane (IDA HPA) — likewise not PIGN's functional site; PIGN acts
  in the ER lumen/membrane, not the PM. MARK_AS_OVER_ANNOTATED.

## References
- file:human/PIGN/PIGN-uniprot.txt — UniProt O95427 (FUNCTION, PATHWAY, SUBCELLULAR
  LOCATION, DISEASE, SIMILARITY). Grounds MF/BP/CC and MCAHS1.
- Reactome R-HSA-162710, R-HSA-162798 (titles left exactly as fetched).
- PMID:19946888 — NK-cell membrane proteome MS; abstract-only; supports generic membrane
  detection (HDA), not ER-specific localization.
- GO_REF:0000002/0000024/0000033/0000052/0000120 — standard pipeline references.
