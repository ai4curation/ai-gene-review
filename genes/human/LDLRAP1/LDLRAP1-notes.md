# LDLRAP1 (ARH) review notes

UniProt: **Q5SW96** → **LDLRAP1** (aka ARH, ARH1, autosomal recessive
hypercholesterolemia protein).
PANTHER: PTHR11232. Taxon: 9606.

## Core function (standalone summary)

LDLRAP1 is a **cargo-selective clathrin-associated sorting protein (CLASP) / adaptor**
that couples the LDL receptor (and other LDLR-family receptors: VLDLR, LRP2/megalin)
to the clathrin endocytic machinery at the plasma membrane. It is a modular adaptor:
an N-terminal **PID/PTB (phosphotyrosine-binding) domain** reads the **FxNPxY (NPVY)
internalization motif** in the cytoplasmic tail of LDLR, while distinct C-terminal
sequences engage **clathrin** (a clathrin-box LLDLE motif) and the **β2-adaptin subunit
of AP-2**. It also binds phosphoinositides (PtdIns(4,5)P2), coupling cargo capture to
clathrin bud assembly. Loss-of-function mutations cause **autosomal recessive
hypercholesterolemia (ARH)**, phenocopying LDLR deficiency because LDLR internalization
fails specifically in the liver/polarized cells where LDLRAP1 is the dominant adaptor.

## Key evidence (provenance)

- [PMID:12221107 "ARH is a modular adaptor protein that interacts with the LDL receptor,
  clathrin, and AP-2", abstract]:
  - PTB→LDLR NPVY: "The phosphotyrosine binding domain of ARH interacted with the
    internalization sequence (NPVY) in the cytoplasmic tail of LDLR in a
    sequence-specific manner."
  - clathrin: "Recombinant ARH bound purified bovine clathrin with high affinity
    (K(D), approximately 44 nm)." mapped to "a canonical clathrin box sequence (LLDLE)".
  - AP-2: "A highly conserved 20-amino acid sequence in the C-terminal region of ARH
    bound the beta(2)-adaptin subunit of AP-2."
  - adaptor model: "ARH functions as an adaptor protein that couples LDLR to the
    endocytic machinery."
- [PMID:15728179 "Functional dissection of an AP-2 beta2 appendage-binding sequence
  within the autosomal recessive hypercholesterolemia protein", abstract]: maps the
  AP-2 β2-appendage-binding sequence; source of the GO:0035615 clathrin-cargo adaptor
  activity IDA.
- UniProt Q5SW96 CC:FUNCTION: "Adapter protein (clathrin-associated sorting protein
  (CLASP)) required for efficient endocytosis of the LDL receptor (LDLR) in polarized
  cells". CC:SUBUNIT: "Interacts (via PID domain) with LDLR (via NPXY motif)
  (PubMed:12221107). Binds to soluble clathrin trimers ... AP-2 complex." CC:DOMAIN:
  "The PID domain mediates interaction with the NPXY internalization motif of LDLR."
- [PMID:14528014] ARH escorts megalin (LRP2) to/through endosomes → LRP2/VLDLR cargo.
- Reactome R-HSA-8863471 "LDLR is bound by DAB2 and ARH"; R-HSA-8867756 "CLASP proteins
  and cargo are recruited to the nascent clathrin-coated pit" — curated CLASP adaptor role.

## Annotation landscape (GOA, 90 rows)

- **24 × GO:0005515 protein binding (IPI)** — mostly interactome/Y2H screens
  (PMID:16189514, 25416956, 32296183, 27107012, 28514442, 33961781, 39526800, ...).
  These are the uninformative rows the project targets: partner lists, not functions.
  Policy: REMOVE bare protein binding; MODIFY to the specific activity where the partner
  and assay define one (LDLR → GO:0050750; clathrin → GO:0030276; AP-2 → GO:0035612).
- **Informative MF already present:** GO:0035615 clathrin-cargo adaptor activity (IDA),
  GO:0035591 signaling adaptor activity (IDA), GO:0030159 signaling receptor complex
  adaptor activity (IMP), GO:0050750 LDL particle receptor binding, GO:0035612 AP-2
  adaptor complex binding (IDA), GO:0030276 clathrin binding (IDA), GO:0035650 AP-1
  adaptor complex binding (IDA), GO:0001784 phosphotyrosine residue binding (IDA),
  GO:0005546 PtdIns(4,5)P2 binding (IDA).
- **BP:** receptor-mediated endocytosis involved in cholesterol transport (IMP),
  LDL particle clearance (IMP), receptor internalization, cholesterol homeostasis —
  core; these are what the adaptor serves.
- **Likely over-/indirect annotations to scrutinise:** GO:0001540 amyloid-beta binding
  / GO:0042982 APP metabolic process; GO:1904707 positive regulation of vascular smooth
  muscle cell proliferation (PMID:28257760, a miR-19/IL-19 study — indirect/disease
  context); GO:0005883 neurofilament, GO:0030424 axon (ISS/ISO brain-expression based).

## Review plan

1. ACCEPT (core) the adaptor MFs and the specific binding contacts; keep GO:0030674 as
   the general adaptor and GO:0035615 as the specific child.
2. Triage 24 protein-binding rows: REMOVE bare; MODIFY the LDLR/clathrin/AP-2 ones to
   the specific supported term already in the record.
3. BP: ACCEPT endocytosis/LDL-clearance/cholesterol-homeostasis as core or non-core;
   scrutinise VSMC-proliferation and amyloid rows (likely KEEP_AS_NON_CORE or
   MARK_AS_OVER_ANNOTATED / indirect).
4. core_functions: cargo adaptor coupling LDLR NPxY to clathrin/AP-2.
