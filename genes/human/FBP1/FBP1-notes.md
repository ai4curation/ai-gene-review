# FBP1 (Fructose-1,6-bisphosphatase 1) - review notes

UniProt P09467 (F16P1_HUMAN); HGNC:3606; EC 3.1.3.11; 338 aa; FBPase class 1 family
(PANTHER PTHR11556:SF11).

## Literature work (2026-10-09)

`just deep-research-falcon human FBP1` failed ("Provider falcon timed out after 600s"); the review below was
written from UniProt, GOA, cached Reactome entries and cached PubMed abstracts/full texts
(fetched with `just fetch-pmid`), not from a deep-research report.

## Core biology

- Catalytic activity: fructose 1,6-bisphosphate + H2O -> fructose 6-phosphate + Pi, Mg2+
  dependent [file:human/FBP1/FBP1-uniprot.txt "Catalyzes the hydrolysis of fructose
  1,6-bisphosphate to fructose 6-phosphate in the presence of divalent cations, acting as a
  rate-limiting enzyme in gluconeogenesis."]
- Recombinant human liver enzyme is active; Asp118/Asp121 metal-pocket residues are catalytic
  [PMID:8387495 "Approximately 50% of the expressed human fructose-1,6-bisphosphatase was
  soluble and enzymatically active"].
- Allosteric inhibition by AMP, competitive inhibition by fructose 2,6-bisphosphate
  [PMID:8387495 "the human enzyme was more sensitive to inhibition by
  fructose-2,6-bisphosphate (Ki = 0.3 microM) and AMP (Ki = 12 microM) than the rat liver
  form"]; homotetramer [PMID:18650089 "In its active form FBPase exists as a homotetramer and
  is allosterically regulated by AMP."].
- Cytosolic; gluconeogenesis step [Reactome:R-HSA-70479 "Cytosolic FBP
  (fructose-1,6-bisphosphatase) tetramers catalyze the physiologically irreversible
  hydrolysis of F1,6PP"].
- Hepatic FBP1 required for fructose tolerance [PMID:36964915 "liver-specific deletion of
  Fbp1 in adult mice leads to fructose intolerance"].
- Moonlighting: nuclear FBP1 represses HIF via the HIF inhibitory domain in ccRCC,
  independent of catalysis [PMID:25043030 "FBP1 restrains cell proliferation, glycolysis and
  the pentose phosphate pathway in a catalytic-activity-independent manner, by inhibiting
  nuclear HIF function via direct interaction with the HIF inhibitory domain."]. Kept as
  non-core.

## Disease

- FBPase deficiency (MIM:229700; MONDO:0009251), autosomal recessive; ClinGen Definitive (AR,
  2025-11-14). [PMID:25601412 "Disease is mainly revealed by hypoglycemia and lactic
  acidosis, both symptoms being characteristic for an enzymatic block in the last steps of
  the gluconeogenesis."]; patient missense proteins inactive [PMID:9382095; PMID:20096900];
  misfolding class of variants [PMID:37507476].

## Annotation decisions (summary)

- ACCEPT: FBPase activity (all lines), gluconeogenesis (all lines), cytosol/cytoplasm.
- MODIFY: phosphatase activity / phosphoric ester hydrolase activity -> GO:0042132;
  carbohydrate metabolic process -> GO:0006094.
- KEEP_AS_NON_CORE: identical protein binding (homotetramer), AMP binding, metal ion binding,
  fructose and fructose 6-phosphate metabolic process, HIF-related nucleus / negative
  regulation of Pol II transcription / TF binding, negative regulation of glycolysis,
  exosome (HDA).
- REMOVE: all bare protein binding IPIs (uninformative; HIF content captured by GO:0061629);
  cellular response to xenobiotic stimulus (in vitro inhibitor chemistry); rodent-expression
  IEA responses to raffinose, salinity, phorbol ester.
- MARK_AS_OVER_ANNOTATED: regulation of gluconeogenesis (enzyme, not regulator), negative
  regulation of cell growth and of Ras signalling (FBP1 is downstream of/repressed by Ras),
  response to Mg2+ (cofactor), monosaccharide binding, extracellular region, response to
  insulin/cAMP/nutrient levels (transcriptional regulation of FBP1, not participation).
- Caveat: PMID:17350621 (EXP for activity) abstract concerns the muscle isozyme; accepted,
  deferring to curator (full text not cached).

## Alignment with dismech

dismech `Fructose-1,6-Bisphosphatase_Deficiency` binds the trigger node to FBP1 (hgnc:3606)
with fructose 1,6-bisphosphate 1-phosphatase activity (GO:0042132) and gluconeogenesis
(GO:0006094) DECREASED in the cytosol (GO:0005829) of hepatocytes. This matches the single
core function here exactly (MF, BP, location). The gluconeogenesis_human and
gluconeogenesis_human_substrates modules carry FBP1 with the same MF and cytosol location.
