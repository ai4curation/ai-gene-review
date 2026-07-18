# MTHFD1L review notes

UniProt: Q6UB35 (C1TM_HUMAN), gene MTHFD1L (HGNC:21055), synonym FTHFSDC1.
Recommended name: **Monofunctional C1-tetrahydrofolate synthase, mitochondrial**; EC=6.3.4.3
(formate--tetrahydrofolate ligase). 978 aa precursor; mitochondrial transit peptide 1-31.

## Core biology (grounded in local files)

- **Monofunctional enzyme.** Despite belonging to the C1-THF synthase family (whose members are
  usually trifunctional: 5,10-methylene-THF dehydrogenase + 5,10-methenyl-THF cyclohydrolase +
  10-formyl-THF synthetase), MTHFD1L retains **only the 10-formyl-THF synthetase (formate--THF
  ligase) activity**. The N-terminal dehydrogenase/cyclohydrolase domain is present but catalytically
  inactive. [file:human/MTHFD1L/MTHFD1L-uniprot.txt "This monofunctional enzyme consists of two major domains: an N-"]
  and [file:human/MTHFD1L/MTHFD1L-uniprot.txt "Was originally thought to be a trifunctional enzyme but only a"].
- **Catalytic reaction (reversible, ATP-dependent):**
  (6S)-5,6,7,8-tetrahydrofolate + formate + ATP = (6R)-10-formyltetrahydrofolate + ADP + phosphate
  (RHEA:20221, EC 6.3.4.3). [file:human/MTHFD1L/MTHFD1L-uniprot.txt "EC=6.3.4.3 {ECO:0000269|PubMed:16171773};"]
- **Biological role / directionality.** In the compartmentalized mammalian one-carbon (folate) cycle,
  mitochondrial one-carbon units generated from serine (via SHMT2, MTHFD2/MTHFD2L, and the
  dehydrogenase/cyclohydrolase steps) are funneled to **10-formyl-THF, which MTHFD1L hydrolyzes to
  release free formate**; formate is exported to the cytosol and re-activated to 10-formyl-THF by
  cytosolic MTHFD1 for purine/thymidylate synthesis and homocysteine remethylation. Reactome models
  both directions (R-HSA-5696839 formate→10-formyl-THF; R-HSA-6801456 10-formyl-THF→formate) and notes
  "Under most conditions, the majority of one-carbon units for cytoplasmic processes are derived from
  mitochondrial formate." [file:human/MTHFD1L/reactome R-HSA-6801456]. UniProt: "May provide the missing
  metabolic reaction required to link the mitochondria and the cytoplasm in the mammalian model of
  one-carbon folate metabolism complementing thus the enzymatic activities of MTHFD2."
  [file:human/MTHFD1L/MTHFD1L-uniprot.txt "the mitochondria and the cytoplasm in the mammalian model of one-carbon"]
- **Subunit / kinetics.** Homodimer in solution. Km for THF drops sharply with polyglutamylation
  (>500 uM mono → 16 uM tri → 3.6 uM penta), i.e. the physiological substrate is polyglutamylated THF.
  [PMID:16171773 "exists as a homodimer in solution"], [PMID:16171773 "dropped from greater than 500 microM for the monoglutamate to 15 microM and 3.6"].
- **Localization.** Mitochondrion (IDA, V5-tagged construct exclusively in mitochondrial fraction of
  CHO cells). [PMID:12937168 "confirming the mitochondrial localization of the protein"].
  Reactome places the reactions in the mitochondrial matrix (TAS). High-throughput mitochondrial
  proteome studies (PMID:34800366 HTP; HPA IDA) corroborate mitochondrial localization.
- **Tissue expression.** Highest in placenta, thymus, brain; low in liver/skeletal muscle; up-regulated
  in colon adenocarcinoma. [PMID:12937168 "highest in placenta, thymus, and brain"].
- **Disease.** Susceptibility to neural tube defects (mouse Mthfd1l knockout → NTDs; human association
  studies). GO neural-tube / craniofacial annotations here are ISS/IEA transferred from mouse ortholog
  Q3V3R1, not human-experimental.

## Evidence provenance for the two catalytic-activity annotations (both cited to Appling lab)

- PMID:12937168 (Prasannan 2003): identified the human gene; yeast expressing the human cDNA showed
  ~9-fold elevated **10-formyl-THF synthetase activity**, and no increase in dehydrogenase activity.
  Basis for the IDA on GO:0004329 and GO:0009257 (10-formyl-THF biosynthetic process) and the
  folic-acid/mitochondrion IDAs. [PMID:12937168 "overexpressed 10-formyl-THF synthetase activity approximately 9-fold"].
- PMID:16171773 (Walkup & Appling 2005, abstract-only in cache): purified recombinant enzyme;
  "Enzyme assays ... revealed only the presence of 10-formyl-THF synthetase activity"; homodimer;
  full steady-state kinetics. Basis for EXP GO:0004329, ATP binding IDA, formate metabolic process IDA,
  homodimerization IDA. [PMID:16171773 "revealed only the presence of 10-formyl-THF synthetase activity"].

## Annotation assessment summary

Core function is unambiguous and experimentally solid: **formate--tetrahydrofolate ligase activity
(GO:0004329)** + **ATP binding**, in the **mitochondrion/mitochondrial matrix**, contributing to
**one-carbon / tetrahydrofolate interconversion / formate metabolism**.

Watch-outs / over-annotations:
- **GO:0004488 methylenetetrahydrofolate dehydrogenase (NADP+) activity** (IEA, InterPro): the N-terminal
  DH/CH domain is present but this activity was **specifically NOT detected** — annotation is contradicted
  by direct assay. Recommend REMOVE (clearly-wrong IEA; the CAUTION line in UniProt states only synthetase
  activity was found).
- **GO:0016020 membrane** (HDA, PMID:19946888 NK-cell membrane proteome): MTHFD1L is a soluble matrix
  enzyme; membrane call is a proteomics artifact (co-fractionation). MARK_AS_OVER_ANNOTATED (do not REMOVE
  experimental HDA per policy).
- **GO:0005829 cytosol** (IBA): the human enzyme is mitochondrial; the IBA cytosol call reflects the
  cytosolic paralog MTHFD1 within the phylogenetic group. Human MTHFD1L is not cytosolic. Keep as
  non-core / undecided rather than assert core — but the experimental data are firmly mitochondrial.
- **Neural tube closure / embryonic neurocranium / viscerocranium morphogenesis** (ISS + IEA from mouse
  Q3V3R1): real biology in mouse (Mthfd1l KO → NTDs), but downstream developmental consequences of the
  metabolic defect, not the core molecular function → KEEP_AS_NON_CORE.
- **GO:0046394 carboxylic acid biosynthetic process** (IEA ARBA): generic parent of formate biosynthesis;
  over-general. KEEP_AS_NON_CORE / over-annotated.

## Core function term ids (authored)
- MF: GO:0004329 formate-tetrahydrofolate ligase activity (verified current label via OLS)
- MF: GO:0005524 ATP binding (verified)
- BP: GO:0035999 tetrahydrofolate interconversion (verified)
- BP: GO:0015942 formate metabolic process (verified)
- CC: GO:0005759 mitochondrial matrix (verified)
</content>
</invoke>
