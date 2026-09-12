# OXCT1 (SCOT, P55809) review notes

## Provenance / research state
- No `OXCT1-deep-research-falcon.md` was present, and no deep-research process was running
  in this worktree to produce one. Polled and confirmed absent; grounded the review in the
  UniProt record (`OXCT1-uniprot.txt`), the seeded GOA (`OXCT1-goa.tsv`), and cached
  publications in `publications/` (all abstract-only except PMID:34800366).

## Core biology (verified)
- OXCT1 = succinyl-CoA:3-ketoacid CoA transferase (SCOT), mitochondrial, EC 2.8.3.5.
- Catalyzes the **first, rate-limiting/committed step of ketone-body utilization (ketolysis)
  in extrahepatic tissues**: transfers CoA from succinyl-CoA to acetoacetate, giving
  acetoacetyl-CoA + succinate. Acetoacetyl-CoA is then cleaved by ACAT1 (acetoacetyl-CoA
  thiolase) to 2 acetyl-CoA that enter the TCA cycle.
  - UniProt FUNCTION: "Key enzyme for ketone body catabolism. Catalyzes the first,
    rate-limiting step of ketone body utilization in extrahepatic tissues..." [file:P55809 uniprot]
  - PMID:8751852 abstract: "mediates the rate-determining step of ketolysis in extrahepatic
    tissues, the esterification of acetoacetate to CoA for use in energy production."
  - PMID:10964512 abstract: "the main determinant of the ketolytic capacity of tissues."
  - Reactome R-HSA-74177: "key enzymes for the metabolism of ketone bodies, catalysing the
    first rate-limiting step of ketone body utilisation in peripheral tissues."
- Mitochondrial matrix; homodimer (only one subunit competent to transfer CoA)
  [PMID:10964512, PMID:23420214 subunit]. PDB 3DLX (dimer). Active site Glu344 forms
  glutamyl-CoA thioester intermediate.
- Tissue: abundant in heart, then brain/kidney/skeletal muscle/lung; **undetectable in liver**
  (liver makes ketones but cannot use them) [PMID:9380443 tissue specificity; PMID:8751852
  "no signal is detectable in the human hepatoma cell line HepG2"].
- Disease: SCOT deficiency (SCOTD, MIM:245050) — episodic severe ketoacidosis; many
  loss-of-function missense variants (V133E, C456F, G219E, V221M, G324E, etc.) abolish/reduce
  activity [PMID:9671268, PMID:10964512, PMID:21296660, PMID:33596448, PMID:31073471].

## Annotation-review reasoning
- MF GO:0008260 (succinyl-CoA:3-oxo-acid CoA-transferase activity): CORE. IBA + two IMP
  (PMID:10964512, PMID:8751852 — SCOT-deficiency mutation/expression studies) + IEA(RHEA/EC).
  ACCEPT the IBA and both IMP; ACCEPT the IEA (correct, EC 2.8.3.5 / RHEA:24564,25480).
- GO:0008410 CoA-transferase activity (IEA, InterPro): parent of GO:0008260; correct but less
  informative than the specific term also annotated. MARK_AS_OVER_ANNOTATED (redundant parent).
- BP GO:0046952 ketone body catabolic process: CORE. IEA(InterPro) + IMP(PMID:9671268, SCOT
  deficiency). ACCEPT both — this is the defining biological role.
- CC mitochondrion GO:0005739 (IBA, IEA-SubCell, IDA HPA GO_REF:0000052, HTP PMID:34800366,
  IDA PMID:11756565, NAS PMID:10964512): all consistent. ACCEPT. Note PMID:11756565 is the
  testis-specific paralog SCOT-t (OXCT2) cloning paper, but it localizes the SCOT-t protein to
  sperm-midpiece mitochondria; the annotation is only to "mitochondrion" (correct compartment
  for the SCOT family) and is IDA experimental — do not REMOVE (per policy). ACCEPT as CC support.
- CC GO:0005759 mitochondrial matrix (5x TAS Reactome): correct, more specific compartment.
  R-HSA-74177 is the SCOT reaction; R-HSA-9838035/9838081/9838093/9838289 are generic
  "mitochondrial matrix protein" degradation/binding reactions (LONP1/CLPXP) that annotate
  the matrix location. ACCEPT all as matrix localization (leave Reactome titles as fetched).
- Ensembl-projected IEAs (GO_REF:0000107, from rat B2GV06):
  - GO:0007507 heart development, GO:0007584 response to nutrient, GO:0009410 response to
    xenobiotic, GO:0009725 response to hormone, GO:0014823 response to activity,
    GO:0035774 pos reg insulin secretion (glucose), GO:0042594 response to starvation,
    GO:0045471 response to ethanol, GO:0060612 adipose tissue development.
    These are rat physiology/expression-response phenotypes electronically projected to human.
    They are plausible for a ketolytic enzyme (starvation/ketosis, heart-enriched expression)
    but are not OXCT1's molecular/core function; several are generic "response to X" over-
    annotations from ortholog expression studies. Mark KEEP_AS_NON_CORE (physiology context)
    for the metabolically coherent ones (heart development, response to nutrient/starvation,
    adipose tissue development, insulin-secretion, response to activity/hormone) and
    MARK_AS_OVER_ANNOTATED the weakly-supported generic stress responses (xenobiotic, ethanol).
  - GO:0042802 identical protein binding (IEA, GO_REF:0000107): SCOT is a homodimer, so
    "identical protein binding" is literally true, but it is an uninformative binding term.
    Per policy this is an IEA (not experimental IPI) — MARK_AS_OVER_ANNOTATED; the informative
    fact (homodimer) is captured via the enzyme MF + core_functions in_complex.
</content>
