# CYP11A1 (P450scc) review notes

UniProtKB:P05108, HGNC:2590, EC 1.14.15.6. Cholesterol side-chain cleavage enzyme,
mitochondrial. Deep research not available (falcon out of credits, HTTP 402); review
grounded in UniProt (`CYP11A1-uniprot.txt`), seeded GOA, and cached publications.

## Core biology

- Mitochondrial inner-membrane cytochrome P450 (heme-thiolate). Catalyzes the first and
  rate-limiting enzymatic step of steroidogenesis: conversion of cholesterol to
  pregnenolone, the precursor of all steroid hormones.
- Three sequential mono-oxygenations: 22-hydroxylation, then 20-hydroxylation to give
  20R,22R-dihydroxycholesterol, then C20–C22 bond scission yielding pregnenolone +
  4-methylpentanal (isocaproaldehyde). [UniProt FUNCTION; PMID:21636783]
- Receives electrons from NADPH via the mitochondrial ferredoxin system: adrenodoxin
  reductase (FDXR) + adrenodoxin/ferredoxin (FDX1/FDX2). Crystal structure of the
  CYP11A1–Adx complex resolves the electron-transfer geometry (2Fe-2S cluster 17.4 Å
  from heme iron). [PMID:21636783 "the [2Fe-2S] cluster of Adx is positioned 17.4 Å away
  from the heme iron of CYP11A1"]
- Cofactor: heme (axial Cys462 thiolate ligand, per UniProt BINDING feature and PDB
  3N9Y/3N9Z/3NA0/3NA1). Iron-ion binding = heme iron.
- Localization: mitochondrion inner membrane, matrix-facing (peripheral membrane
  protein). [UniProt SUBCELLULAR LOCATION]
- Expression: adrenal cortex (HPA "Tissue enriched (adrenal)"), gonad, placenta.

## Disease

- AICSR (adrenal insufficiency, congenital, with 46,XY sex reversal; MIM:613743).
  Loss-of-function CYP11A1 mutations impair all steroidogenesis → adrenal failure;
  46,XY individuals show underandrogenization / sex reversal.
  [PMID:11502818 de novo Gly-Asp insertion after Asp271, complete inactivation;
  PMID:18182448 compound het L141W (38% activity) / V415E (0% activity)]
- Distinguished from congenital lipoid adrenal hyperplasia (StAR mutations): P450scc
  deficiency does not show the massive adrenal enlargement.

## Annotation decisions (summary)

- CORE MF: GO:0008386 cholesterol monooxygenase (side-chain-cleaving) activity — accept
  all copies (IBA, IEA, TAS, IDA, ISS).
- Secondary MF: GO:0020037 heme binding (IDA, IEA) accept; GO:0005506 iron ion binding
  (IEA, = heme iron) accept as non-core. Broad P450 MF parents (GO:0004497,
  GO:0016705, GO:0016713, GO:0008395) are correct-but-general → MARK_AS_OVER_ANNOTATED
  (heme_binding + GO:0008386 already capture the specific function).
- CORE BP: C21-steroid hormone biosynthetic process (GO:0006700), steroid hormone
  biosynthetic process (GO:0120178), cholesterol metabolic process (GO:0008203). Accept.
- Broader/pathway BP: sterol metabolic process (GO:0016125), C21-steroid hormone
  metabolic process (GO:0008207) accept as non-core (correct parents).
- Downstream-product BP: glucocorticoid biosynthetic process (GO:0006704), cortisol
  metabolic process (GO:0034650) — CYP11A1 acts upstream of all these; it produces
  pregnenolone, not cortisol/glucocorticoid directly. IBA over-reaches →
  MARK_AS_OVER_ANNOTATED.
- GO:0042359 vitamin D metabolic process (ISS) — CYP11A1 can act on vitamin D3
  (7-dehydrocholesterol-derived) in vitro/skin, but this is a minor/secondary activity,
  not the core function → KEEP_AS_NON_CORE.
- GO:0071375 cellular response to peptide hormone stimulus (IBA) — reflects ACTH
  regulation of steroidogenic cells (P450scc induced by cAMP, PMID:1849407), a cellular
  response not a CYP11A1 molecular activity → KEEP_AS_NON_CORE.
- CC: mitochondrial inner membrane (GO:0005743, IBA/IEA/ISS) core; mitochondrion
  (GO:0005739) accept as non-core (broader); mitochondrial matrix (GO:0005759, Reactome
  TAS) accept as non-core (matrix-facing peripheral membrane protein).
- GO:0005515 protein binding (IPI, PMID:25464930, NLGN3 Y2H) — bare protein binding,
  uninformative; per policy MARK_AS_OVER_ANNOTATED (not REMOVE).
