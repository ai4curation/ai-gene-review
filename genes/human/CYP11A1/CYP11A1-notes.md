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

## 2026-10-25 full annotation audit

All 46 original rows were assessed. This audit supersedes the earlier blanket exclusion of upstream biosynthetic participation and older protein-binding policy.

- **Catalysis:** supported full-text refresh of PMID:21636783 confirms use of human CYP11A1, adrenodoxin and reductase constructs, not only bovine homologs. The enzyme performs C22 hydroxylation, C20 hydroxylation and C20-C22 cleavage, yielding pregnenolone plus 4-methylpentanal. NADPH-derived electrons arrive via ferredoxin reductase and adrenodoxin; the structural study directly examines human FDX1, so no FDX2-specific role is inferred from it.
- **Process participation:** GO:0006704 is ACCEPT. A shared upstream catalytic step genuinely participates in glucocorticoid synthesis; it need not make the final hormone directly. Cortisol metabolism is refined to cortisol biosynthesis without attributing cortisol hydroxylase or catabolic activity. This corrects the old claim that a pathway-entry enzyme cannot carry downstream pathway membership.
- **Localization:** the active protein is associated with the matrix face of the mitochondrial inner membrane. Matrix annotations are ACCEPT as active topology, unlike STAR's post-import inactive pool. Broad mitochondrion annotations refine to inner membrane. Product release into a compartment is not protein-localization evidence; no freely soluble matrix enzyme is asserted.
- **Secondary function:** DrugBank cross-reference support for vitamin D metabolism was replaced by primary PMID:22683847, including explicitly human keratinocyte products and human serum metabolite detection. Other tissue or purified-enzyme species not specified in the abstract are not relabeled human. This remains KEEP_AS_NON_CORE.
- **Hormonal context:** PMID:1849407 demonstrates cAMP-responsive protein synthesis in human JEG-3 and mouse Y1 cells. This supports a downstream steroidogenic response context, not peptide-hormone binding or receptor activity. Patient variants in PMID:11502818 and PMID:18182448 establish adrenal/gonadal functional consequences with allele-specific residual activity.
- **GO-CAM inspected:** `67b1629100003765` models the human CYP11A1 cholesterol monooxygenase activity within steroid hormone biosynthesis. No substrate-only role or missing process was inferred.
- **Family:** PANTHER:PTHR24279:SF3 official label CHOLESTEROL SIDE-CHAIN CLEAVAGE ENZYME, MITOCHONDRIAL; parent PTHR24279 is merely CYTOCHROME P450. Cached PAINT IBD PTN001547321 supports the inherited process/location context; no broad-P450 tissue-function transfer is made. Both zebrafish tandem duplicates match the same subfamily despite different expression.
- Bare protein binding from PMID:25464930 is REMOVE as uninformative. The source actually includes CYP11A1 interaction validation; this is not a wrong-gene judgment. Broad enzyme/metabolic parents are refined with MODIFY. Heme and its iron remain core cofactor properties.

### Retrieval and validation provenance

Falcon deep research was attempted for human/CYP11A1 with perplexity-lite fallback. Falcon failed authentication (403) and Perplexity returned insufficient_quota (401). No provider research file was fabricated. Manual source-specific findings are recorded here and in reference reviews. Publication caching ran concurrently with research retrieval; initial NCBI 429 failures were retried only for missing records. Existing caches were not force-refreshed except the key abstract-only PMID18403318 and PMID21636783 records needed for source-specific adjudication.

### Reviewed row ledger

1. GO:0006704 (IBA; GO_REF:0000033): ACCEPT — CYP11A1 catalyzes the entry reaction of adrenal glucocorticoid biosynthesis.
2. GO:0008386 (IBA; GO_REF:0000033): ACCEPT — Phylogenetic (IBA) assignment of the defining CYP11A1 molecular function: cholesterol side-chain-cleaving monooxygenase (P450scc). This is the core molecular function and is strongly supported experimentally.
3. GO:0034650 (IBA; GO_REF:0000033): MODIFY — CYP11A1 contributes to the biosynthetic branch of cortisol metabolism.
4. GO:0005743 (IBA; GO_REF:0000033): ACCEPT — Phylogenetic (IBA) localization to the mitochondrial inner membrane, where P450scc is active. This is the established site of action of CYP11A1.
5. GO:0006700 (IBA; GO_REF:0000033): ACCEPT — Phylogenetic (IBA) annotation to C21-steroid hormone biosynthesis. Pregnenolone (the CYP11A1 product) is a C21 steroid, and CYP11A1 initiates the C21-steroid hormone biosynthetic pathway.
6. GO:0071375 (IBA; GO_REF:0000033): KEEP_AS_NON_CORE — Phylogenetic (IBA) annotation reflecting that steroidogenic expression/activity of P450scc is regulated by peptide hormones (e.g. ACTH via cAMP). This is a regulatory cellular response rather than a molecular activity of CYP11A1.
7. GO:0008203 (IBA; GO_REF:0000033): ACCEPT — Phylogenetic (IBA) annotation to cholesterol metabolism. CYP11A1 consumes cholesterol as its substrate, converting it to pregnenolone.
8. GO:0004497 (IEA; GO_REF:0000002): MODIFY — The broad oxidoreductase class is supported, with a characterized cholesterol side-chain-cleavage activity.
9. GO:0005506 (IEA; GO_REF:0000002): ACCEPT — CYP11A1 binds iron as part of its catalytic heme.
10. GO:0005739 (IEA; GO_REF:0000117): MODIFY — CYP11A1 is mitochondrial, with its catalytic site at the inner membrane.
11. GO:0005743 (IEA; GO_REF:0000044): ACCEPT — UniProt subcellular-location (IEA) mapping to the mitochondrial inner membrane, the established location of CYP11A1.
12. GO:0006700 (IEA; GO_REF:0000117): ACCEPT — ARBA (IEA) annotation to C21-steroid hormone biosynthesis, consistent with the IBA/IDA/TAS annotations to the same term.
13. GO:0008386 (IEA; GO_REF:0000120): ACCEPT — Combined-IEA (RHEA/EC 1.14.15.6) mapping to the core cholesterol monooxygenase (side-chain-cleaving) activity.
14. GO:0008395 (IEA; GO_REF:0000117): MODIFY — The broad oxidoreductase class is supported, with a characterized cholesterol side-chain-cleavage activity.
15. GO:0016125 (IEA; GO_REF:0000117): MODIFY — CYP11A1 metabolizes cholesterol, a sterol substrate.
16. GO:0016705 (IEA; GO_REF:0000002): MODIFY — The broad oxidoreductase class is supported, with a characterized cholesterol side-chain-cleavage activity.
17. GO:0016713 (IEA; GO_REF:0000117): MODIFY — The broad oxidoreductase class is supported, with a characterized cholesterol side-chain-cleavage activity.
18. GO:0020037 (IEA; GO_REF:0000120): ACCEPT — Combined-IEA annotation for heme binding, the essential cofactor of this heme-thiolate cytochrome P450.
19. GO:0005515 (IPI; PMID:25464930): REMOVE — The reported neuroligin-3 association does not define a specific CYP11A1 molecular function.
20. GO:0120178 (IDA; PMID:21636783): ACCEPT — Direct experimental (IDA) annotation to steroid hormone biosynthetic process, supported by the structural/biochemical characterization of pregnenolone biosynthesis by the CYP11A1-adrenodoxin complex.
21. GO:0006700 (TAS; Reactome:R-HSA-196108): ACCEPT — Reactome TAS annotation (Pregnenolone biosynthesis) to C21-steroid hormone biosynthesis, consistent with the well-supported core biological process.
22. GO:0016125 (TAS; Reactome:R-HSA-211976): MODIFY — CYP11A1 metabolizes cholesterol, a sterol substrate.
23. GO:0008203 (IEA; GO_REF:0000041): ACCEPT — UniPathway (IEA) mapping to cholesterol metabolic process, consistent with the IBA/IDA/ISS annotations to the same term.
24. GO:0008207 (IEA; GO_REF:0000041): MODIFY — CYP11A1 produces the C21 steroid pregnenolone.
25. GO:0008386 (TAS; Reactome:R-HSA-193054): ACCEPT — Reactome TAS annotation for the first hydroxylation step (cholesterol to 22beta-hydroxycholesterol) catalyzed by CYP11A1, supporting the core cholesterol side-chain-cleaving activity.
26. GO:0008386 (TAS; Reactome:R-HSA-193065): ACCEPT — Reactome TAS annotation for the second hydroxylation step (22beta-hydroxycholesterol to 20alpha,22beta-hydroxycholesterol) catalyzed by CYP11A1.
27. GO:0008386 (TAS; Reactome:R-HSA-193101): ACCEPT — Reactome TAS annotation for the final C20-C22 bond cleavage step (20alpha,22beta-dihydroxycholesterol to pregnenolone) catalyzed by CYP11A1.
28. GO:0005743 (ISS; GO_REF:0000024): ACCEPT — Sequence-similarity (ISS) localization to the mitochondrial inner membrane, transferred from an ortholog. Consistent with the IBA/IEA annotations.
29. GO:0005739 (HTP; PMID:34800366): MODIFY — CYP11A1 is mitochondrial, with its catalytic site at the inner membrane.
30. GO:0005759 (TAS; Reactome:R-HSA-5580269): ACCEPT — The active CYP11A1 protein occupies the matrix face of the inner mitochondrial membrane.
31. GO:0005759 (TAS; Reactome:R-HSA-193054): ACCEPT — The active CYP11A1 protein occupies the matrix face of the inner mitochondrial membrane.
32. GO:0005759 (TAS; Reactome:R-HSA-193065): ACCEPT — The active CYP11A1 protein occupies the matrix face of the inner mitochondrial membrane.
33. GO:0005759 (TAS; Reactome:R-HSA-193101): ACCEPT — The active CYP11A1 protein occupies the matrix face of the inner mitochondrial membrane.
34. GO:0008203 (ISS; GO_REF:0000024): ACCEPT — Sequence-similarity (ISS) annotation to cholesterol metabolic process, transferred from a characterized ortholog. Consistent with the core role.
35. GO:0008386 (ISS; GO_REF:0000024): ACCEPT — Sequence-similarity (ISS) annotation to the core cholesterol monooxygenase (side-chain-cleaving) activity, transferred from a characterized ortholog.
36. GO:0006700 (IDA; PMID:21636783): ACCEPT — Direct experimental (IDA) annotation to C21-steroid hormone biosynthesis, from the structural and biochemical study of pregnenolone biosynthesis by the CYP11A1- adrenodoxin complex with substrate and reaction intermediates.
37. GO:0008203 (IDA; PMID:21636783): ACCEPT — Direct experimental (IDA) annotation to cholesterol metabolic process, from the structural/biochemical characterization of CYP11A1 acting on cholesterol.
38. GO:0008386 (IDA; PMID:21636783): ACCEPT — Direct experimental (IDA) annotation to the core cholesterol side-chain-cleaving activity, from the crystal structures and mechanistic analysis of CYP11A1 with substrate and reaction intermediates.
39. GO:0020037 (IDA; PMID:21636783): ACCEPT — Direct experimental (IDA) annotation to heme binding, from the crystal structure resolving the heme iron of CYP11A1 in the redox complex with adrenodoxin.
40. GO:0042359 (ISS; GO_REF:0000024): KEEP_AS_NON_CORE — CYP11A1 also participates in noncanonical vitamin D hydroxylation.
41. GO:0005739 (ISS; GO_REF:0000024): MODIFY — CYP11A1 is mitochondrial, with its catalytic site at the inner membrane.
42. GO:0006700 (IDA; PMID:11502818): ACCEPT — Direct experimental (IDA) annotation to C21-steroid hormone biosynthesis. This case report demonstrated that a de novo CYP11A1 mutation abolishing enzyme activity causes adrenal insufficiency and 46,XY sex reversal, confirming CYP11A1's essential role in steroid hormone biosynthesis.
43. GO:0006700 (IDA; PMID:18182448): ACCEPT — Direct experimental (IDA) annotation to C21-steroid hormone biosynthesis, from functional analysis of novel CYP11A1 mutations (L141W, V415E) that reduce or abolish P450scc activity and cause combined adrenal and gonadal deficiency.
44. GO:0008203 (IMP; PMID:18182448): ACCEPT — Mutant-phenotype (IMP) annotation to cholesterol metabolic process, based on functional characterization of CYP11A1 loss-of-function mutations impairing cholesterol conversion.
45. GO:0008386 (IDA; PMID:11502818): ACCEPT — Direct experimental (IDA) annotation to the core cholesterol side-chain-cleaving activity, from functional assay of the patient's CYP11A1 mutation.
46. GO:0008386 (IDA; PMID:18182448): ACCEPT — Direct experimental (IDA) annotation to the core cholesterol side-chain-cleaving activity, quantifying residual activity of patient CYP11A1 mutants.

Counts: 32 ACCEPT, 11 MODIFY, 2 KEEP_AS_NON_CORE, 1 REMOVE. No NEW annotations were added. All original seeded annotation fields were preserved.

## 2026-10-25: review evidence follow-up

Replaced EC-only and bare cofactor-header quotations with the curated overall cholesterol-cleavage reaction and explicit heme cofactor statement, both experimentally supported by PMID:21636783 in the source record. No annotation actions or machine source fields changed.

## Root-organelle correction, 2026-10-26

The supported root mitochondrion annotations are retained as ACCEPT, separately from unchanged subcompartment claims. This supersedes earlier journal wording that refined the root location or treated its breadth as non-core. Original annotation payloads, unrelated review decisions and core functions are preserved. Source-specific rationales distinguish curated location/inference, original experimental annotations and source access limits; no new assay or target-table inspection is claimed.
