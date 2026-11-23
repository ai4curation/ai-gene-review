# ACVR1B manual research and annotation audit, 2026-10-25

Human ACVR1B (P36896), also ALK4/ActRIB/SKR2, was seeded before review. All 81 existing rows have been reviewed, preserving original term, evidence, source, qualifiers and supporting-entity fields. No NEW annotation was added.

## Research provenance

The parent attempted Perplexity and Falcon research. `/tmp/aigr-activin-ACVR1B-deep.log` records Perplexity HTTP 401 `insufficient_quota`; `/tmp/aigr-activin-ACVR1B-falcon.log` records the Falcon authentication failure and failed Perplexity fallback. Providers were not retried. This file is the manual research record; no provider-named report was fabricated.

All original PMID caches were read, along with the curated UniProt function, domain, modification and binding-site statements and available Reactome entries. Full text of PMID:21356369 was inspected specifically because its title emphasizes ALK7 while the annotation concerns ALK4. Target-specific mammalian nervous-system evidence was added from PMID:31676717, including the fetched full text. Targeted attempts to access full publisher text of PMID:18039968 and PMID:7890768 returned unavailable/403 responses; specific unresolved claims remain UNDECIDED.

## Mechanistic synthesis and boundaries

ALK4 is a type-I membrane serine/threonine receptor kinase, not a soluble transcription factor. Type-II activin receptors first bind activin and recruit ALK4; phosphorylation of the ALK4 GS domain activates its downstream kinase signaling [PMID:8622651]. The paper states: “ActR-IB acts as a downstream transducer of activin signals.” It also explicitly says that isolated ActRIB does not bind ligand on its own.

This is compatible with direct ligand contact within the assembled complex. Extracellular ALK4 mutations alter radioligand cross-linking in the presence of ActRII [PMID:12665502]. The contributes_to receptor and activin-binding rows retain their weaker complex-component interpretation; no independent high-affinity ligand capture was invented.

Activated ALK4 binds R-SMADs SMAD2/3, which subsequently leave the receptor and assemble with SMAD4 [PMID:9892009]. SMAD7 and FKBP12 regulate receptor signaling, with recruitment of SMURF1 controlling ubiquitination [PMID:16720724]. SMAD4 binding in a protein interaction screen is not evidence that it is a receptor substrate. Receptor ubiquitination does not prove ubiquitin-binding activity.

Nodal also uses ALK4, with an EGF-CFC coreceptor such as CRIPTO [PMID:11389842; PMID:12052855]. Activin does not share this coreceptor requirement [PMID:14966532]. Myostatin can use ActRIIB with ALK4 or ALK5 [PMID:14517293]. BMP-3b/GDF10 is functionally facilitated by ALK4/ActRIIA and activates SMAD2/3, despite the BMP name [PMID:22155034]. Neither the kinase-family name nor shared type-II receptors establish identical ligand repertoires. SB-431542 inhibits ALK4, ALK5 and ALK7 and therefore does not uniquely implicate ALK4 by itself [PMID:12065756].

## Biological outputs

- Human K562 experiments show activin-dependent hemoglobin accumulation and reduced proliferation [PMID:9032295]. Truncated dominant-negative ALK4 isoforms block the growth arrest and G1 accumulation [PMID:11117535]. The G1/S annotation is refined to negative regulation, not progression through the transition.
- In the full text of PMID:21356369, ALK4 knockdown reduces trophoblast invasion whereas ALK7 or Nodal knockdown increases it. Thus the ALK7-focused title does not invalidate the positive ALK4 migration annotation; the authors connect the ALK4 effect to activin signaling.
- Mouse conditional Alk4 deletion supports development of cortical somatostatin interneurons [PMID:31676717]. This corroborates a gene-specific mammalian role without asserting a direct human neural experiment or identical functions for every member of the broad PAINT family.
- Myostatin/BMP-3b studies support negative adipocyte/osteoblast differentiation contexts, while ALK4 promotes erythroid differentiation elsewhere. Both signs are cell-context dependent, not mutually exclusive universal claims. Mouse HS-72 hybridomas support an activin-triggered apoptotic output [PMID:9884026].

## Unresolved evidence

The direct inhibin-binding row (GO:0034711) remains UNDECIDED. PMID:7890768 explicitly assigns inhibin binding to ActRII and reports failure of the ActRII-SKR2/ALK4 complex to form. InhBP association in PMID:11266516 does not prove direct ALK4-inhibin binding. Full text was inaccessible, so this experimental annotation was not removed on an incomplete source.

The peptidyl-threonine phosphorylation row (GO:0018107) attached to PMID:18039968 also remains UNDECIDED: the abstract describes TTRAP/Alk4 signaling and zebrafish development, but the receptor construct and precise phosphorylation assay could not be verified directly. The receptor's general kinase and autophosphorylation functions have independent biochemical/curated support.

The legacy Reactome R-NUL-1181349 reference is unresolved; it was not silently reassigned to a guessed human identifier. Its plasma-membrane assertion is independently supported by primary receptor-binding experiments.

## Review coverage

Final decisions: MODIFY 31, ACCEPT 28, REMOVE 12, KEEP_AS_NON_CORE 8, UNDECIDED 2. All 81 rows have decisions; no PENDING or NEW rows. Bare protein binding is never ACCEPT; seven such rows are refined to demonstrated receptor/SMAD binding classes and twelve are removed as uninformative, not biologically false.

Two core functions distinguish the specific activin type-I receptor activity from receptor kinase transduction in the nodal/CRIPTO context. Downstream cellular phenotypes remain non-core.

## Annotation audit ledger

Rows are one-based YAML order.

| Row | GO term | Decision | Sources |
|---|---|---|---|
| 1 | GO:0000082 G1/S transition of mitotic cell cycle | MODIFY | PMID:11117535 |
| 2 | GO:0004672 protein kinase activity | MODIFY | PMID:8622651, PMID:12065756 |
| 3 | GO:0004674 protein serine/threonine kinase activity | MODIFY | PMID:8622651, PMID:12065756 |
| 4 | GO:0004674 protein serine/threonine kinase activity | MODIFY | PMID:8622651, PMID:12065756 |
| 5 | GO:0004674 protein serine/threonine kinase activity | MODIFY | PMID:8622651, PMID:12065756 |
| 6 | GO:0004674 protein serine/threonine kinase activity | MODIFY | PMID:8622651, PMID:12065756 |
| 7 | GO:0004674 protein serine/threonine kinase activity | MODIFY | PMID:8622651, PMID:12065756 |
| 8 | GO:0004675 transmembrane receptor protein serine/threonine kinase activity | ACCEPT | PMID:8622651, PMID:9892009, PMID:12065756 |
| 9 | GO:0004675 transmembrane receptor protein serine/threonine kinase activity | ACCEPT | PMID:8622651, PMID:9892009, PMID:12065756 |
| 10 | GO:0005515 protein binding | REMOVE | PMID:11266516 |
| 11 | GO:0005515 protein binding | REMOVE | PMID:11278302 |
| 12 | GO:0005515 protein binding | REMOVE | PMID:11279102 |
| 13 | GO:0005515 protein binding | REMOVE | PMID:11389842 |
| 14 | GO:0005515 protein binding | REMOVE | PMID:12052855 |
| 15 | GO:0005515 protein binding | REMOVE | PMID:12052855 |
| 16 | GO:0005515 protein binding | REMOVE | PMID:12919325 |
| 17 | GO:0005515 protein binding | REMOVE | PMID:14517293 |
| 18 | GO:0005515 protein binding | MODIFY | PMID:8622651, PMID:9032295 |
| 19 | GO:0005515 protein binding | MODIFY | PMID:16720724, PMID:9892009 |
| 20 | GO:0005515 protein binding | REMOVE | PMID:16720724 |
| 21 | GO:0005515 protein binding | REMOVE | PMID:21791611 |
| 22 | GO:0005515 protein binding | REMOVE | PMID:22939624 |
| 23 | GO:0005515 protein binding | REMOVE | PMID:35512704 |
| 24 | GO:0005515 protein binding | MODIFY | PMID:8622651, PMID:9032295 |
| 25 | GO:0005515 protein binding | MODIFY | PMID:8622651, PMID:9032295 |
| 26 | GO:0005515 protein binding | MODIFY | PMID:16720724, PMID:9892009 |
| 27 | GO:0005515 protein binding | MODIFY | PMID:9892009 |
| 28 | GO:0005515 protein binding | MODIFY | PMID:9892009 |
| 29 | GO:0005524 ATP binding | ACCEPT | PMID:12065756, file:human/ACVR1B/ACVR1B-uniprot.txt |
| 30 | GO:0005524 ATP binding | ACCEPT | PMID:12065756, file:human/ACVR1B/ACVR1B-uniprot.txt |
| 31 | GO:0005886 plasma membrane | ACCEPT | PMID:12665502, PMID:9032295 |
| 32 | GO:0005886 plasma membrane | ACCEPT | PMID:12665502, PMID:9032295 |
| 33 | GO:0005886 plasma membrane | ACCEPT | PMID:12665502, PMID:9032295 |
| 34 | GO:0005886 plasma membrane | ACCEPT | PMID:12665502, PMID:9032295 |
| 35 | GO:0005886 plasma membrane | ACCEPT | PMID:12665502, PMID:9032295 |
| 36 | GO:0005886 plasma membrane | ACCEPT | PMID:12665502, PMID:9032295 |
| 37 | GO:0005886 plasma membrane | ACCEPT | PMID:12665502, PMID:9032295 |
| 38 | GO:0006355 regulation of DNA-templated transcription | MODIFY | PMID:8622651, PMID:12665502, PMID:9892009 |
| 39 | GO:0006355 regulation of DNA-templated transcription | MODIFY | PMID:8622651, PMID:12665502, PMID:9892009 |
| 40 | GO:0007165 signal transduction | MODIFY | PMID:8622651, PMID:11389842 |
| 41 | GO:0007165 signal transduction | MODIFY | PMID:8622651, PMID:11389842 |
| 42 | GO:0007178 cell surface receptor protein serine/threonine kinase signaling pathway | MODIFY | PMID:8622651, PMID:11389842 |
| 43 | GO:0007178 cell surface receptor protein serine/threonine kinase signaling pathway | MODIFY | PMID:8622651, PMID:11389842 |
| 44 | GO:0007399 nervous system development | KEEP_AS_NON_CORE | PMID:31676717 |
| 45 | GO:0009986 cell surface | MODIFY | PMID:12665502, PMID:9032295 |
| 46 | GO:0010468 regulation of gene expression | MODIFY | PMID:11117535, PMID:9892009 |
| 47 | GO:0016020 membrane | MODIFY | PMID:12665502, PMID:9032295 |
| 48 | GO:0016361 activin receptor activity, type I | ACCEPT | PMID:8622651, PMID:9892009, PMID:12665502 |
| 49 | GO:0016361 activin receptor activity, type I | ACCEPT | PMID:8622651, PMID:9892009, PMID:12665502 |
| 50 | GO:0016361 activin receptor activity, type I | ACCEPT | PMID:8622651, PMID:9892009, PMID:12665502 |
| 51 | GO:0017002 activin receptor activity | MODIFY | PMID:8622651, PMID:12665502 |
| 52 | GO:0017002 activin receptor activity | MODIFY | PMID:8622651, PMID:12665502 |
| 53 | GO:0018107 peptidyl-threonine phosphorylation | UNDECIDED | PMID:18039968 |
| 54 | GO:0019838 growth factor binding | ACCEPT | PMID:14517293 |
| 55 | GO:0030279 negative regulation of ossification | KEEP_AS_NON_CORE | PMID:22155034 |
| 56 | GO:0030308 negative regulation of cell growth | KEEP_AS_NON_CORE | PMID:11117535, PMID:9032295 |
| 57 | GO:0030334 regulation of cell migration | MODIFY | PMID:21356369 |
| 58 | GO:0031625 ubiquitin protein ligase binding | KEEP_AS_NON_CORE | PMID:16720724 |
| 59 | GO:0032924 activin receptor signaling pathway | ACCEPT | PMID:8622651, PMID:9892009, PMID:12065756 |
| 60 | GO:0032924 activin receptor signaling pathway | ACCEPT | PMID:8622651, PMID:9892009, PMID:12065756 |
| 61 | GO:0032924 activin receptor signaling pathway | ACCEPT | PMID:8622651, PMID:9892009, PMID:12065756 |
| 62 | GO:0032924 activin receptor signaling pathway | ACCEPT | PMID:8622651, PMID:9892009, PMID:12065756 |
| 63 | GO:0032924 activin receptor signaling pathway | ACCEPT | PMID:8622651, PMID:9892009, PMID:12065756 |
| 64 | GO:0032927 positive regulation of activin receptor signaling pathway | ACCEPT | PMID:8622651, PMID:16720724 |
| 65 | GO:0034711 inhibin binding | UNDECIDED | PMID:7890768, PMID:11266516 |
| 66 | GO:0038092 nodal signaling pathway | ACCEPT | PMID:11389842, PMID:12052855 |
| 67 | GO:0043235 signaling receptor complex | MODIFY | PMID:14517293, PMID:8622651 |
| 68 | GO:0045596 negative regulation of cell differentiation | MODIFY | PMID:14517293, PMID:22155034 |
| 69 | GO:0045648 positive regulation of erythrocyte differentiation | KEEP_AS_NON_CORE | PMID:9032295 |
| 70 | GO:0046332 SMAD binding | MODIFY | PMID:9892009, PMID:16720724 |
| 71 | GO:0046777 protein autophosphorylation | ACCEPT | PMID:8622651, file:human/ACVR1B/ACVR1B-uniprot.txt |
| 72 | GO:0048179 activin receptor complex | ACCEPT | PMID:8622651, PMID:12665502, PMID:9032295 |
| 73 | GO:0048179 activin receptor complex | ACCEPT | PMID:8622651, PMID:12665502, PMID:9032295 |
| 74 | GO:0048185 activin binding | ACCEPT | PMID:12665502, PMID:8622651 |
| 75 | GO:0048185 activin binding | ACCEPT | PMID:12665502, PMID:8622651 |
| 76 | GO:0051239 regulation of multicellular organismal process | MODIFY | PMID:9032295, PMID:22155034, PMID:21356369 |
| 77 | GO:0070411 I-SMAD binding | KEEP_AS_NON_CORE | PMID:16720724, PMID:9892009 |
| 78 | GO:0071363 cellular response to growth factor stimulus | ACCEPT | PMID:8622651, PMID:11389842, PMID:14517293 |
| 79 | GO:0097191 extrinsic apoptotic signaling pathway | KEEP_AS_NON_CORE | PMID:9884026 |
| 80 | GO:1901165 positive regulation of trophoblast cell migration | KEEP_AS_NON_CORE | PMID:21356369 |
| 81 | GO:1902554 serine/threonine protein kinase complex | MODIFY | PMID:8622651, PMID:9032295 |

Validation: `just validate human ACVR1B` passed without warnings after the initial review. `just backfill-record-sections genes/human/ACVR1B` derived UniProt record sections. Final follow-up validation and history validation are recorded with the audit history.

Final follow-up: `just validate human ACVR1B` passed with zero warnings, `git diff --check` passed for ACVR1B/SMAD3, and the scaffolded ACVR1B history record validated without issues.
