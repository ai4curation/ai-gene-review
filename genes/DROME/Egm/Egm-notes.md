# Egm (dACAD9 / Enigma / CG9006) — Drosophila melanogaster — Research Notes

UniProt: Q5U117 (ACAD9_DROME), 639 aa, Reviewed/Swiss-Prot. FlyBase: FBgn0086712.
Ortholog of human ACAD9 (Q9H845). PANTHER subfamily PTHR43884:SF9 "COMPLEX I ASSEMBLY
FACTOR ACAD9, MITOCHONDRIAL". Member of the acyl-CoA dehydrogenase (ACAD) family with a
predicted mitochondrial transit peptide (residues 1-26) and the ACAD9/ACADV-like C-terminal
domain (Pfam PF21343 ACAD9-ACADV_C). EC assigned as 1.3.8.- by similarity to human ACAD9.

## Summary of function (synthesis)

Egm is the single Drosophila ortholog of human ACAD9. Like human ACAD9, its dominant,
essential role is as a mitochondrial respiratory chain complex I (CI) assembly factor and a
core component of the mitochondrial complex I intermediate assembly (MCIA) complex, together
with the fly orthologs of ECSIT (CG10610), NDUFAF1 (CG7598), TMEM126B (CG13392), and TMEM186
(CG4627). It retains an ACAD-family fold and (by similarity to human ACAD9) may retain
residual FAD-dependent acyl-CoA dehydrogenase activity toward long/very-long-chain acyl-CoA,
but the direct enzymatic activity of the fly protein has not been biochemically demonstrated.

## Provenance from cached publications

### PMID:16434470 (Mourikis et al. 2006, PNAS) — "Enigma" characterization. full_text_available: true
- Cloning/identity: Egm = CG9006 = 639-aa ACAD-homologous protein; two null alleles (Egm1, EgmP)
  are lethal and rescued by a WT genomic copy.
  [PMID:16434470 "Egm encodes the CG9006 gene, which corresponds to a 639-aa protein with homology to ACADs, the enzymes that catalyze the first of four reactions that constitute one cycle of the β-oxidation pathway"]
- Subcellular localization: mitochondrial by immunocytochemistry (colocalizes with MitoTracker
  and prohibitin, an inner-membrane marker) and by cell fractionation.
  [PMID:16434470 "In Drosophila Kc-167 and SL2 cells, Egm is found almost exclusively in the mitochondrion."]
  [PMID:16434470 "the endogenous Egm protein is highly enriched in the fraction that contains the mitochondria"]
- Essential gene / disruption phenotype: homozygous nulls die at late larval (third instar) stage;
  develop subcuticular melanotic masses, small eye/wing imaginal discs, malformed fat bodies;
  ~3.9-fold prolonged larval life; halved triglycerides.
  [PMID:16434470 "homozygous null animals ( Egm –/– ) die during the late larval stage (third instar)"]
  [PMID:16434470 "the stored fatty acids in the form of triglycerides are almost halved in larvae lacking zygotically expressed Egm"]
- Lipid homeostasis / beta-oxidation link (INDIRECT/inferred): homology to ACADs + mitochondrial
  localization + reduced triglycerides + upregulated lipase-3 + eye clone phenotype resembling
  scully (a beta-oxidation component). Authors are explicit this is indirect.
  [PMID:16434470 "indirect evidence suggests that this protein may be involved in β-oxidation"]
- Oxidative stress / longevity: heterozygous Egm mutants are more paraquat-resistant and longer-lived
  (female-specific).
  [PMID:16434470 "Egm mutant flies demonstrate a significantly increased resistance to the toxic effects of 7.5 mM paraquat compared with WT flies"]
- Eye development (clonal, cell-autonomous):
  [PMID:16434470 "null Egm –/– clones show an aberrant morphology ( Fig. 3 D-1 ), indicating that Egm is required for eye development in a cell autonomous fashion"]
- NOTE: this 2006 paper predates the discovery that human ACAD9's primary role is CI assembly
  (Nouws 2010). Its FAO/lipid-homeostasis interpretation is best read, in light of later work
  (PMID:34386730 and human ACAD9), as downstream consequences of CI/OXPHOS deficiency in a fly that
  cannot assemble CI, rather than proof of a direct beta-oxidation enzyme role.

### PMID:34386730 (Murari et al. 2021, iScience) — CI biogenesis; dACAD9 assayed. full_text_available: true
- dACAD9 (= CG9006 = Egm) is treated as the fly ACAD9 ortholog and a component of the MCIA complex.
  [PMID:34386730 "Drosophila orthologs of ACAD9 (CG9006), ECSIT (CG10610), NDUFAF1 (CG7598), TMEM126B (CG13392), TMEM186 (CG4627)"]
  [PMID:34386730 "the MCIA complex is known to consist of ACAD9 (Nouws et al., 2010), NDUFAF1 (Vogel et al., 2005), ECSIT (Vogel et al., 2007), TMEM126B (Heide et al., 2012), and TMEM186"]
- MCIA components (including dACAD9) remain associated with the assembled CI holoenzyme and with
  stalled assembly intermediates.
  [PMID:34386730 "all 5 components of the MCIA complex were associated with subcomplexes in FAF4-kd and FAF3-kd samples"]
- FUNCTION (fly): dACAD9 regulates biogenesis of the PP-b (ND2) sub-module; dACAD9 knockdown
  destabilizes the other MCIA members (dNDUFAF1, dECSIT) in assembly intermediates.
  [PMID:34386730 "ACAD9 regulates biogenesis of some sub-assemblies in the PP-b sub-module"]
  [PMID:34386730 "RNAi-mediated knockdown of dACAD9 resulted in a reduction in the amount of dNDUFAF1 and dECSIT that accumulates in AIs in ACAD9-kd samples"]
  [PMID:34386730 "when dACAD9 is disrupted, the paucity of the PP-b sub-module will cause the Q/PP-a AI to stall and accumulate"]
- This directly parallels human ACAD9 in the MCIA complex (Nouws 2010; Formosa 2020) and is the
  basis for the IDA (GO:0160295, MCIA complex) and TAS (GO:0032981, CI assembly) annotations, and
  the ISS transfer of the adaptor-activity term from human ACAD9.

### PMID:18666829 (Findlay et al. 2008, PLoS Biol) — seminal fluid proteomics. full_text_available: true
- Egm was detected among transferred seminal fluid proteins (HEP, GO:0007320 insemination). This is
  a mass-spec detection of the protein in seminal fluid, categorized under "lipid metabolism"
  proteins; it is a proteomic co-occurrence, NOT a demonstrated reproductive function of Egm.
  [PMID:18666829 "Many of these proteins fell into the same functional categories as the previously predicted set, including proteases, protease inhibitors, mediators of an immune response, and proteins involved in lipid metabolism"]
  (Egm is one of the lipid-metabolism-category Sfps in the paper's protein tables.)

### PMID:23667151 (Chow et al. 2013, PNAS) — ER stress natural variation (DGRP). full_text_available: true
- Egm was one of six lipid-metabolism-related association candidates for TM-induced ER-stress survival
  (HMP, GO:0034976). This is a GWAS/association + P-element functional-test candidate; a putative,
  correlative role rather than a mechanistic one.
  [PMID:23667151 "we identified six association candidates ( CG12428 , bgm , Egm , CG9518 , RdgA , and CG5162 ) with known or putative roles in lipid metabolism"]

### PMID:26362788 (Chen et al. 2015, PNAS) — APEX mitochondrial-matrix proteomics. full_text_available: true
- APEX-based proteomic mapping of the Drosophila muscle mitochondrial matrix ("MitoMax"). Egm was
  catalogued in the matrix proteome (source of the IDA GO:0005759 mitochondrial matrix annotation).
  [PMID:26362788 "maps the mitochondrial matrix proteome of Drosophila muscle"]
  (Egm/CG9006 appears in the MitoMax matrix inventory; matrix placement is consistent with a
  peripheral inner-membrane, matrix-facing MCIA factor.)

### PMID:8913755 (Verheyen et al. 1996, Genetics) — Notch modifier screen. full_text_available: FALSE (abstract only)
- Large-scale second-site screen for dominant enhancers/suppressors of activated-Notch rough-eye
  phenotype (137,000 flies, 290 modifiers). Basis for the IGI GO:0001745 compound eye morphogenesis
  annotation (Egm as a Notch-eye modifier). Abstract-only in cache; the specific Egm/CG9006 allele
  data are in the full text not available here.
  [PMID:8913755 "a second-site mutagenesis screen was performed to isolate enhancers and suppressors of the eye phenotype caused by expression of these activated Notch molecules"]

## Interpretation for review decisions

- CORE: CI assembly factor / MCIA complex member. Strong: GO:0160295 (IDA), GO:0032981 (TAS),
  GO:0030674 adaptor activity (ISS from human ACAD9), mitochondrion (IDA x2), mitochondrial matrix (IDA).
- SECONDARY / by-similarity enzymatic: FAD binding (IEA InterPro), oxidoreductase CH-CH (IEA InterPro),
  VLCAD activity (ISS from human ACAD9), medium-chain ACAD activity (IBA), fatty acid metabolic/beta-ox
  (IEA/IBA/IMP). The fly's own dehydrogenase activity is not directly demonstrated; human ACAD9's
  is modest (~18% VLCAD) and its FAO role is secondary/moonlighting. Keep these NON-CORE.
- The IMP FAO/lipid-homeostasis annotations (PMID:16434470) rest on indirect evidence and predate the
  CI-assembly-factor paradigm. The mutant phenotypes (triglyceride loss, lethality) are equally
  explained by CI/OXPHOS failure. Keep as non-core (do not REMOVE experimental annotations).
- Insemination (HEP), ER stress (HMP), compound eye (IGI), oxidative-stress (IMP): pleiotropic /
  systemic-consequence or proteomic-cooccurrence annotations. Keep as non-core; eye/ER/insemination
  are likely secondary to the gene's essential mitochondrial role. IGI eye annotation (PMID:8913755)
  is abstract-only in cache — but it is an experimental (IGI) FlyBase call; keep as non-core.
