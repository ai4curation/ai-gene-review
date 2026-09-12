# LYRM7 (Q5U5X0) review notes

## Identity
- Human LYRM7 = LYR motif-containing protein 7; synonyms C5orf31, MZM1L. HGNC:28072. 104 aa.
- Ortholog of *S. cerevisiae* Mzm1 (SGD:S000002901; PANTHER PTN005318945). Complex I LYR family / MZM1-LYRM7 InterPro family (IPR045298, IPR050435; Pfam PF05347 Complex1_LYR).

## Core function (verified)
- Mitochondrial-matrix **assembly chaperone for respiratory Complex III** (cytochrome bc1 / ubiquinol-cytochrome c reductase). Non-catalytic.
- Specifically a **UQCRFS1 (Rieske Fe-S protein) chaperone**: binds and stabilises UQCRFS1 in the mitochondrial matrix prior to its [2Fe-2S] cluster insertion, translocation and incorporation into the late CIII dimeric intermediate in the inner membrane.
  - [PMID:23168492 "human LYRM7, which we propose to be renamed MZM1L (MZM1-like), works as a human Rieske Fe-S protein (UQCRFS1) chaperone, binding to this subunit within the mitochondrial matrix and stabilizing it prior to its translocation and insertion into the late CIII dimeric intermediate within the mitochondrial inner membrane"]
  - [PMID:23168492 "LYRM7/MZM1L is a novel human CIII assembly factor involved in the UQCRFS1 insertion step, which enables formation of the mature and functional CIII enzyme"]
- LYR motif engages the Fe-S transfer cochaperone HSC20/HSCB (Q8IWL3): the UQCRFS1-LYRM7 intermediate recruits HSC20-HSPA9-ISCU to deliver the [2Fe-2S] cluster to UQCRFS1.
  - [PMID:28380382 "a transient subcomplex involved in CIII assembly, composed of LYRM7 bound to UQCRFS1, interacts with components of an Fe-S transfer complex, consisting of HSC20, its cognate chaperone HSPA9, and the holo-scaffold ISCU. Binding of HSC20 to the LYR motif of LYRM7 in a pre-assembled UQCRFS1-LYRM7 intermediate in the mitochondrial matrix facilitates Fe-S cluster transfer to UQCRFS1"]
  - [PMID:24606901 "members of the LYR motif family which assist assembly of complexes II or III, SDHAF1 and LYRM7, respectively, are HSC20 binding partners"]

## Localisation (verified)
- Mitochondrial matrix (IDA, PMID:23168492; UniProt SUBCELLULAR LOCATION: Mitochondrion matrix). Also mitochondrial membrane (IDA, PMID:23168492 — consistent with association with the inner-membrane CIII intermediate). HTP mito proteome PMID:34800366.

## Disease (context, not a GO annotation here)
- Mitochondrial complex III deficiency, nuclear type 8 (MC3DN8; MIM:615838). Homozygous D25N impairs Rieske Fe-S incorporation into CIII; early-onset encephalopathy/leukoencephalopathy, lactic acidosis, severe CIII activity reduction. [PMID:24014394].

## GOA interactors (IPI WITH/FROM accessions)
- P47985 = UQCRFS1 (Rieske) — the physiological client. Cited by PMID:23168492, 27499296, 28380382, 33961781, 40205054.
- Q8IWL3 = HSCB/HSC20 — the Fe-S cochaperone. Cited by PMID:24606901, 28380382.
- P21673 = SAT1 (diamine acetyltransferase) — from HuRI binary interactome (PMID:32296183); no known mitochondrial/CIII role; likely non-physiological Y2H hit.

## GO term decisions
- MF: **GO:0044183 protein folding chaperone** (IBA + Reactome TAS) is the correct non-catalytic MF. Keep as core. Do NOT invent a catalytic MF.
- BP core: **GO:0034551 mitochondrial respiratory chain complex III assembly** (IDA/IBA/IEA/TAS) — accept as core.
- CC: **GO:0005759 mitochondrial matrix** (IDA + IBA + IEA + TAS) core; GO:0005739 mitochondrion (IEA/HTP) broader-accept; GO:0031966 mitochondrial membrane (IDA) accept as non-core (association with membrane CIII intermediate).
- GO:0006457 protein folding (IEA, inferred from the chaperone MF) — accept, general but sound.
- GO:0045333 cellular respiration (IDA) — LYRM7 is an assembly factor, not itself part of respiration; the phenotype of its loss is impaired respiration. Mark as over-annotated (indirect; complex III assembly is the precise BP).
- GO:0005515 protein binding IPIs — bare, uninformative MF; per policy MARK_AS_OVER_ANNOTATED (do not REMOVE). SAT1 hit noted as likely non-physiological but not removed.
- Note: current CIII complex term is GO:0045275 (GO:0005750 obsolete); no complex-membership annotation is present in this GOA, and LYRM7 is a transient assembly factor, not a stable CIII subunit, so no in_complex is asserted.
