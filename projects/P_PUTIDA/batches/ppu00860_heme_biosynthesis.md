---
title: "PSEPK ppu00860 heme-b biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
genes: [hemA, hemL, hemB, hemBB, hemC, hemD, hemE, hemF, hemN, PP_0431, hemH]
autolink_gene_symbols: false
---

# PSEPK ppu00860: heme-b biosynthesis

- Module seed: `heme_biosynthesis`
- KEGG candidate genes considered from the pathway bucket: 46
- Selected glutamyl-tRNA-to-heme-b genes: 11
- Curated review files in this batch: 11
- Corrected module/pathway OpenScientist reports: 0 of 2 (final reruns pending)
- Gene-level OpenScientist reports: 9 of 11

## Required Workflow

- [x] Refactor the module into a reusable multi-route heme-b pathway.
- [ ] Run module-level OpenScientist research from the corrected module.
- [ ] Run module + ppu00860 + PSEPK OpenScientist research from the corrected module.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [ ] Run OpenScientist research for every selected gene.
- [x] Curate every selected GOA row with no pending actions.
- [ ] Validate and render the module, genes, and batch page.
- [ ] Open one non-draft PR for this module/pathway.
- [ ] Shepherd the PR through review, CI, and merge readiness.

## Selected Genes

| Done | Gene | Locus | UniProt | Curation | OpenScientist | Module interpretation | Protein |
|---|---|---|---|---|---|---|---|
| [x] | `hemA` | PP_0732 | Q88PW6 | CURATED | PRESENT | covered: first C5 glutamyl-tRNA reaction | Glutamyl-tRNA reductase |
| [x] | `hemL` | PP_4784 | Q88DP0 | CURATED | PRESENT | covered: second C5 glutamyl-tRNA reaction | Glutamate-1-semialdehyde 2,1-aminomutase |
| [x] | `hemB` | PP_2913 | Q88IT6 | CURATED | PRESENT | covered candidate: Zn/Mg-site ALAD paralog | Delta-aminolevulinate dehydratase |
| [x] | `hemBB` | PP_3322 | Q88HN1 | CURATED | PRESENT | covered candidate: Mg-site ALAD paralog | Delta-aminolevulinate dehydratase |
| [x] | `hemC` | PP_0186 | Q88RE5 | CURATED | PRESENT | covered: hydroxymethylbilane synthesis | Porphobilinogen deaminase |
| [x] | `hemD` | PP_0187 | Q88RE4 | CURATED | PRESENT | covered: uroporphyrinogen III synthesis | Uroporphyrinogen-III synthase |
| [x] | `hemE` | PP_5074 | Q88CV6 | CURATED | PRESENT | covered: coproporphyrinogen III synthesis | Uroporphyrinogen decarboxylase |
| [x] | `hemF` | PP_0073 | Q88RQ6 | CURATED | PENDING | covered: oxygen-dependent late-step variant | Oxygen-dependent coproporphyrinogen-III oxidase |
| [x] | `hemN` | PP_4264 | Q88F35 | CURATED | PENDING | covered: oxygen-independent radical-SAM variant | Coproporphyrinogen-III oxidase |
| [x] | `PP_0431` | PP_0431 | Q88QQ7 | CURATED | PRESENT | covered: HemJ membrane-electron-transfer variant | Protoporphyrinogen IX oxidase |
| [x] | `hemH` | PP_0744 | Q88PV4 | CURATED | PRESENT | covered: terminal ferrochelation | Ferrochelatase |

## Boundary And Adjudication

KT2440 realizes the C5 glutamyl-tRNA entry route through `hemA` and `hemL`; the reusable module does not restrict that route to bacteria because homologous C5 routes also occur in archaea and plastid-bearing eukaryotes. The generalized graph models C5 and C4/Shemin ALA formation as one entry-chemistry axis, followed by one shared ALAD-HemC-HemD-HemE trunk. It selects HemF/HemN and HemJ/HemG/HemY/PPOX late chemistry independently of the entry route, avoiding duplicated trunks and an incorrect hard coupling between C4 entry and oxygen-dependent late enzymes. The KT2440 realization uses `hemF` and `hemN` alternatives, HemJ-family `PP_0431`, and `hemH`.

Both `hemB` and `hemBB` remain selected. Sequence-based records support ALAD activity for both, but `hemB` has a predicted catalytic zinc triad plus magnesium site whereas `hemBB` has a magnesium-site prediction without the zinc triad. This supports distinct metal-site architectures, not a claim that one paralog is physiologically dominant. The module therefore requires an active ALAD-family enzyme without making both paralogs conjunctively required.

`gltX` is excluded as upstream substrate supply: it makes glutamyl-tRNA used by translation and by HemA but is not committed to heme synthesis. The broad KEGG bucket also contains genes outside the protoporphyrin-dependent heme-b boundary:

- Heme O/A and cytochrome conversion: `PP_0109`, `cyoE1`, `cyoE2`.
- Heme storage, utilization, iron handling, or degradation: `bfr-I`, `bfr-II`, `hemO`, `PP_2582`, `PP_1358`, `PP_4856`.
- Siroheme branch: `PP_0188`, `cobA`, `cysG`.
- Corrin/cobalamin branch: `pduO`, `cobO`, `cobB` (Q88MA1), `cobD`, `cobC`, `cobQ`, `cobP`, `cobT`, `PP_1680`, `cobS`, `PP_3409`, `cobM`, `PP_3506`, `cobN`, `PP_3763`, `cobJ`, `cobI`, `cobH`, `cobG`, `cobL`, `cbiD`, `cobK`.

## Known Gaps

No local FEBA/RB-TnSeq fitness records were available for the 11 genes, so essentiality and condition-specific dominance were not inferred. Direct KT2440 experiments are still needed to resolve `hemB` versus `hemBB` flux, the oxygen range over which HemF and HemN contribute, and the native membrane electron acceptor used by PP_0431. Gene-level assignments are therefore conservative where evidence is family- or rule-based rather than strain-specific biochemistry.

Generated UTC: 2026-07-20
