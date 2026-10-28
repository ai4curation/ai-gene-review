# Gpam (mouse, Q61586) review notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Context: mouse Gpam is the experimentally characterised ortholog of the ProtNLM2
benchmark gene human GPAM (Q9HCL2). This review was written without opening any
ProtNLM2 prediction file and does not use ProtNLM2 output as evidence.

### Process / provenance

- `just fetch-gene mouse Gpam` created the UniProt, GOA (60 rows) and stub files;
  `just fetch-gene-pmids mouse Gpam` cached all 15 GOA PMIDs.
- `just deep-research-falcon mouse Gpam --fallback perplexity-lite` FAILED:
  falcon raised "Failed to authenticate" and the perplexity-lite fallback returned
  HTTP 401 (insufficient quota). No deep-research file exists for this gene. The
  review is built from the cached publications (two with full text: PMID:12417724,
  PMID:18522808), the UniProt record, the PANTHER/PAINT files for PTHR12563 and the
  two cached mouse GO-CAMs.

### Evolutionary grounding

- UniProt places Q61586 in PANTHER PTHR12563:SF16 "GLYCEROL-3-PHOSPHATE
  ACYLTRANSFERASE 1, MITOCHONDRIAL", the same subfamily as human GPAM (Q9HCL2), rat
  Gpam (P97564), bovine and pig GPAM (interpro/panther/PTHR12563/PTHR12563-entries.csv).
  So human/rat-to-mouse transfers are 1:1 orthologue transfers within one subfamily.
- PAINT node PTN000970957 (taxon:6072, Eumetazoa) carries IBDs for GO:0004366
  (G3P O-acyltransferase activity), GO:0005739 (mitochondrion), GO:0006650
  (glycerophospholipid metabolic process) and GO:0019432 (TAG biosynthetic process).
  Mouse Gpam MGI:109162 is itself a seed of every one of these IBDs, so the IBA rows
  are anchored in mouse experimental data (not circular).
- PAINT did NOT propagate GO:0006655 (phosphatidylglycerol biosynthesis) or any
  immune / glucose / growth process. The phosphatidylglycerol rows on mouse come only
  from human (UniProt-curated lysophosphatidylglycerol acyltransferase reaction,
  RHEA:33203, ECO:0000269 PMID:19075029 on human Q9HCL2). Treated as inferred, non-core.

### What is experimentally established in mouse itself

1. Loss of NEM-resistant (mitochondrial) GPAT activity in Gpam-/- liver
   [PMID:12417724 "demonstrating successful elimination of mtGPAT activity"] and dose
   dependent loss of activity after hepatic shRNA knockdown in ob/ob mice [PMID:16935266].
   Together with activity of the recombinant mouse enzyme cited in PMID:12417724
   (palmitoyl-CoA preference, 5.5-fold over 18:1-CoA in Sf9 cells), this establishes
   GO:0004366 in mouse.
2. TAG synthesis: Gpam-/- mice have lower hepatic and plasma TAG and reduced VLDL-TAG
   secretion [PMID:12417724]; hepatocytes lacking GPAT1 cannot incorporate de novo
   synthesised fatty acid into TAG [PMID:23908354]; hearts of Gpat1-/- mice on
   lipogenic diets accumulate 20-80% less TAG [PMID:18522808].
3. Fatty acid partitioning: without GPAT1, acyl-CoAs are diverted to beta-oxidation
   and ketogenesis and hepatic acyl-CoA rises [PMID:15878874, PMID:23908354].
4. sn-1 palmitate positioning in liver/heart PC and PE, with secondary increase of sn-2
   arachidonate [PMID:12417724, PMID:18522808].
5. Location: mouse-specific direct localization data are limited to organelle
   proteomics (mitochondrion; PMID:14651853, PMID:18614015) and the inner-membrane
   proteomic list PMID:12865426. Outer-membrane placement rests on rat liver
   subfractionation [PMID:17493869: active pool in OMM; import into mitochondria but
   not microsomes] and the human cryo-EM structure [PMID:36522428: no TM helices,
   amphipathic patch + N-terminal targeting loop-helix]. OMM is therefore
   orthologue-inferred for mouse, but the inference is strong (same subfamily).

### Annotation decisions (summary)

- ACCEPT: all GO:0004366 rows; GO:0019432 rows; GO:0006654 rows; GO:0005741 rows.
- MODIFY -> GO:0005741: mitochondrion (HDA/IBA/IDA/IMP) and mitochondrial membrane (ISO).
- MODIFY to specific terms: acyltransferase activity / ...non-amino-acyl (-> GO:0004366);
  lipid metabolic process (-> GO:0019432, GO:0006654); phospholipid biosynthetic process
  and glycerophospholipid metabolic process (-> GO:0006654); triglyceride metabolic
  process (-> GO:0019432); positive regulation of TAG biosynthetic process (lateral, ->
  GO:0019432: GPAT1 catalyses the step, it does not regulate it).
- KEEP_AS_NON_CORE: diacylglycerol biosynthesis, CDP-DAG biosynthesis,
  phosphatidylglycerol biosynthesis (human-derived), fatty acid metabolic process,
  acyl-CoA metabolic process, phospholipid homeostasis.
- MARK_AS_OVER_ANNOTATED: T-cell / cytokine / antiviral phenotypes of the knockout
  (PMID:18971390, PMID:19193813: authors themselves attribute them to altered membrane
  lipid composition and PGE2), response to glucose, cellular response to insulin,
  response to activity, fatty acid homeostasis.
- REMOVE: plasma membrane (IEA via the PlsB InterPro entry; bacterial PlsB is an inner
  (plasma) membrane enzyme, not GPAT1); ER membrane (Reactome gene-expression event,
  contradicted by mitochondrial targeting data); mitochondrial inner membrane
  (proteomic co-isolation, contradicted by OMM localization); positive regulation of
  multicellular organism growth (full text attributes lower body weight to reduced
  fat mass, not to growth control).

### Open questions

- Is the less-active GPAT1 pool at ER-mitochondria contact sites/MAV (rat) physiologically
  relevant for LPA transfer to the ER?
- Does mouse GPAT1 have meaningful lysophosphatidylglycerol acyltransferase activity in
  vivo (shown only for human enzyme in vitro)?
