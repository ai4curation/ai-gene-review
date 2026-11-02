# SIRT5: evidence notes

## Paired horse benchmark evidence review

The human reference supplies mechanistic evidence for the corresponding selected horse protein; the human conclusion alone is not validation of the horse sequence. The exact horse comparison is in `genes/HORSE/SIRT5/SIRT5-bioinformatics/RESULTS.md`. Research reports are source leads; annotation decisions cite the underlying publication or experimentally supported UniProt passages. Unresolved source-specific results retain UNDECIDED.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: every existing annotation (68 rows), the description and core functions were re-examined. No ProtNLM2 output was consulted.

### Identity
- Q9NXA8 is the canonical, reviewed 310-aa human SIRT5 product (transit peptide 1-36, sirtuin domain 37-307, active-site His158, acyl-pocket Tyr102/Arg105, Zn ligands C166/C169/C207/C212). Not a fragment or alternative gene model. Isoforms 2-4 exist (VSP_008730/1, VSP_042292, VSP_042291) but no annotation is isoform-specific.

### Evolutionary placement
- PANTHER PTHR11085:SF10 (SIRT5 subfamily). PAINT node PTN000119399 (Eukaryota; seeds human SIRT5 + mouse Sirt5) carries desuccinylase, demalonylase, deglutarylase, mitochondrion, cytosol. PTN000872307 adds mitochondrial matrix.
- The histone deacetylase IBD (GO:0017136) and nucleus IBD come from deep sirtuin nodes (PTN008718612, PTN008492176) seeded by robust deacetylases / nuclear sirtuins, with no SIRT5 seeds. SIRT5 diverged to acidic-acyl specificity: deacetylation ~500-fold weaker than SIRT1 [PMID:22076378 "The catalytic efficiency (kcat/Km) of Sirt5 was about 500-fold lower than that of Sirt1."]; Tyr102/Arg105 bind the acyl carboxylate [PMID:22076378 "Thus, Tyr102 and Arg105 were important for binding succinyl and malonyl groups."]. GO:0017136 IBA therefore MODIFY to the acidic deacylase MFs (FUNCTIONAL_DIVERGENCE).
- Family review interpro/panther/PTHR11085/PTHR11085-review.yaml: no disagreement on subfamily placement (SF10, SIRT5 + horse F6S899).

### Key literature (all full text except where noted)
- Cytosolic and minor nuclear pools: [PMID:23806337 "Subcellular fractionation revealed that a significant fraction of endogenous SIRT5 was present cytosolically both in human cells"; "A very small amount of SIRT5 was also detected in the nuclear fraction, which was particularly evident in the liver samples"].
- No in vivo deacetylation role: [PMID:23806337 "SIRT5 deficiency does not significantly impact global Lys acetylation"]; [PMID:22076378 "For Lys44 and Lys287, the levels of acetylation and succinylation did not change significantly in Sirt5 KO mice"]. Supports accepting the curator NOT protein deacetylation (IDA PMID:22076378) and marking the positive cytochrome-c-based protein deacetylation IDA (PMID:18680753, abstract only) as over-annotated. The best-practice checker warns because it compares a NOT and a positive row of the same term; the two actions are semantically consistent.
- Deglutarylase: [PMID:24703693 "Using this assay, we found SIRT5 is the only HDAC exhibiting significant lysine deglutarylase activity in vitro"].
- IMS and matrix import: [PMID:18680753 "Sirt5 can indeed be translocated into the mitochondrial intermembrane space, but also into the matrix"] (abstract).

### Main changes vs previous version
- Previous version supported every row with the same UniProt FUNCTION block and left 12 rows UNDECIDED; now each row cites the primary evidence.
- UNDECIDED resolved: NOT ADP-ribosyltransferase rows (2) ACCEPT; PMID:23806337 rows (nucleus KEEP_AS_NON_CORE, cytosol ACCEPT, mitochondrion MODIFY); IMS KEEP_AS_NON_CORE; inner membrane MARK_AS_OVER_ANNOTATED; chromatin remodeling REMOVE (IEA derived from the refined histone deacetylase IBA); acyltransferase parent MODIFY to the specific deacylases; NOT protein deacetylation ACCEPT.
- mitochondrion rows MODIFY -> mitochondrial matrix + intermembrane space; cytoplasm MODIFY -> cytosol.
- urea cycle: KEEP_AS_NON_CORE (regulator of CPS1, does not perform a cycle step; GO has no 'regulation of urea cycle' term).
- mitochondrion organization (Reactome) and cardiomyocyte apoptosis (rat projection): MARK_AS_OVER_ANNOTATED.
- zinc and NAD+ binding: KEEP_AS_NON_CORE (entailed by / structural to the enzyme).
- Ketogenesis (mouse HMGCS2, same subfamily ortholog) and ROS regulation (SOD1) KEEP_AS_NON_CORE.

### Relative to review next
- Mouse Sirt5 (Q8K2C6, MGI:1915596): 1:1 ortholog in PTHR11085:SF10 and a PAINT seed of PTN000119399; experimentally characterised (CPS1, HMGCS2, succinylome KO studies). No review exists in the repo (genes/mouse/Sirt5 absent).

### Modules
- No module under modules/ references SIRT5 or Q9NXA8; no GO-CAM index entry found.
