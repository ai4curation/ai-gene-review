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
- Corrected module/pathway OpenScientist reports: 2 of 2
- Gene-level OpenScientist reports: 11 of 11

## Required Workflow

- [x] Refactor the module into a reusable multi-route heme-b pathway.
- [x] Run module-level OpenScientist research from the corrected module.
- [x] Run module + ppu00860 + PSEPK OpenScientist research from the corrected module.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run OpenScientist research for every selected gene.
- [x] Curate every selected GOA row with no pending actions.
- [x] Validate and render the module, genes, and batch page.
- [x] Open one non-draft PR for this module/pathway.
- [x] Shepherd the PR through review, CI, and merge readiness.

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
| [x] | `hemF` | PP_0073 | Q88RQ6 | CURATED | PRESENT | covered: oxygen-dependent late-step variant | Oxygen-dependent coproporphyrinogen-III oxidase |
| [x] | `hemN` | PP_4264 | Q88F35 | CURATED | PRESENT | covered: oxygen-independent radical-SAM variant | Coproporphyrinogen-III oxidase |
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

## OpenScientist Assessment

The final generic module report supports the protoporphyrin-dependent boundary,
the shared HemB-HemE trunk, and independent entry and late-oxidation axes. It
also contains claims that were not adopted: HemB-HemE is called a six-enzyme
trunk, entry chemistry and late-enzyme use are generalized as universally fixed
by oxygen, and membrane association or substrate channeling is extended across
families without equivalent evidence. Its generated pathway figure is treated
as a conceptual summary rather than independent evidence.

The final PSEPK pathway/taxon report supports a complete C5-route realization,
the selected 11 genes, and exclusion of the neighboring cobalamin, siroheme,
heme-use, and heme-modification branches in `ppu00860`. Several recommendations
were not adopted: `gltX` remains upstream substrate supply, HemJ-family
`PP_0431` retains GO:0070818 rather than the report's oxygen-acceptor
GO:0004729, and the existing HemB/HemBB metal-site predictions are retained.
Claims of anaerobic flexibility and proteome-wide absence of additional late
oxidases remain unverified because no KT2440 experiment or archived scan was
provided. The out-of-scope `PP_0109` heme-A-synthase recommendation was not
adjudicated as part of this batch.

## Wave115 Repair Audit

### Reusable Boundary And Logic

The generic module remains a `CONCRETE` chemically defined, leaf-grounded
protoporphyrin-dependent heme-B pathway. Cross-taxon reuse does not make it an
`ABSTRACT` gene-free motif. PSEPK-specific pathway-bucket interpretation and
paralog commentary now live in this batch document rather than in generic
module evidence or notes.

The C5 and C4/Shemin ALA-entry branches are `ONE_OR_MORE`, matching the two
late oxidation axes. This avoids an unsupported assertion that a concrete
organism or compartment can realize exactly one entry system. Minimal route
enumeration still chooses one branch on each independent axis and yields 12
paths: two ALA entries, two coproporphyrinogen-oxidation chemistries, and three
protoporphyrinogen-oxidation chemistries. The shared logical core is ALAD,
HemC, HemD, HemE, and ferrochelatase. Parent-to-child connections preserve the
chemical handoffs across the nested entry, shared-trunk, late-oxidation, and
terminal-ferrochelation nodes.

For the KT2440 realization, `hemA` and `hemL` provide C5 entry, at least one of
`hemB` and `hemBB` provides ALAD activity, `hemC`, `hemD`, and `hemE` form the
shared trunk, `hemF` and `hemN` provide alternative coproporphyrinogen
oxidation chemistries, `PP_0431` provides the HemJ step, and `hemH` performs
ferrochelation. This does not establish relative `hemB`/`hemBB` flux or require
both paralogs. The endpoint-specific GO:0006785 decisions in selected PSEPK
reviews describe this organismal route; they do not make the shared
intermediate-forming reactions exclusive to heme B.

`gltX` remains upstream because it supplies glutamyl-tRNA to translation as
well as HemA. Coproheme synthesis, corrin/cobalamin and siroheme branches,
heme uptake/storage/degradation, and conversion of heme B to heme O, heme A,
or other modified hemes remain outside the module.

### Exact Family And PAINT Grounding

Reviewed UniProt exemplars were rechecked, including bacterial, human, and
Rhodobacter/Cereibacter representatives. Every PANTHER label and representative
member was checked against `panther.obo` and `panther-members.tsv`. The module
adds only local PAINT MF nodes whose GO assertion and experimental seeds are
checkable in the corresponding `*-paint.tsv` file:

| Step | PAINT node | MF |
|---|---|---|
| HemA | `PTN001464796` | GO:0008883 |
| HemL | `PTN000241400` | GO:0042286 |
| eukaryotic ALAS | `PTN000343737` | GO:0003870 |
| ALAD | `PTN000156046` | GO:0004655 |
| HemC/HMBS | `PTN000168159` | GO:0004418 |
| bacterial HemD/UROS | `PTN002866208` | GO:0004852 |
| eukaryotic UROS | `PTN000273375` | GO:0004852 |
| HemE/UROD | `PTN000472929` | GO:0004853 |
| HemF/CPOX | `PTN000079415` | GO:0004109 |
| HemN | `PTN000358335` | GO:0051989 |
| HemG | `PTN002445460` | GO:0070819 |
| eukaryotic PPOX | `PTN000077911` | GO:0004729 |
| HemH/FECH | `PTN000121751` | GO:0004325 |

No PTN is asserted for HemJ because the local PAINT data do not establish a
matching MF node. ALAS, HemD/UROS, and HemF retain exact cross-lineage InterPro
descriptors where a single PANTHER family name would be too narrow or
misleading; their cited PAINT nodes state the underlying PTHR provenance.

### Required Annotation-Reviewer Pass

An independent read-only annotation reviewer audited every GOA row, action,
reason, core function, location decision, endpoint-process claim, and local
evidence file for all 11 pathway anchors. It also checked module boundaries,
route logic, nested connections, family labels/member containment, and every
PTN against local PAINT seeds. No blockers or necessary gene-review changes
were found.

| Gene | Reviewer disposition |
|---|---|
| `hemA` | `NO_CHANGES_NEEDED` |
| `hemL` | `NO_CHANGES_NEEDED` |
| `hemB` | `NO_CHANGES_NEEDED` |
| `hemBB` | `NO_CHANGES_NEEDED` |
| `hemC` | `NO_CHANGES_NEEDED` |
| `hemD` | `NO_CHANGES_NEEDED` |
| `hemE` | `NO_CHANGES_NEEDED` |
| `hemF` | `NO_CHANGES_NEEDED` |
| `hemN` | `NO_CHANGES_NEEDED` |
| `PP_0431` | `NO_CHANGES_NEEDED` |
| `hemH` | `NO_CHANGES_NEEDED` |

### Wave115 OpenScientist Refresh

Both required provider commands were run with the full configured
`timeout=7200` allowance and were never manually cancelled. The generic module
job (`78cc5eec-daef-4ec2-bdb9-c3edd3b1154e`) and the PSEPK `ppu00860`
module+pathway+taxon job (`cfb582a0-062f-4965-a005-88578a183d59`) each remained
quiet until the provider wrapper reached 7200 seconds and returned its explicit
timeout failure. Neither run wrote a partial replacement. The prior complete
generic and PSEPK OpenScientist reports are therefore retained and reused as
retrieval support, with their overreach caveats above unchanged; no new claim
was imported from a timed-out run.

### Final Validation

- Rebased onto `origin/main` at `8abe023124e` before the final pass.
- ModuleReview LinkML validation passes with no issues.
- Semantic module validation passes. Its 30 warnings are advisory: unavailable
  CHEBI lookups, the unconfigured InterPro prefix, and four locally verified
  PAINT nodes beneath broader InterPro-grounded descriptors.
- `just validate PSEPK <gene>` passes for all 11 selected anchors; no gene
  review changed.
- `tests/test_module_logic.py` passes all 34 tests. Direct enumeration asserts
  12 minimal routes, independent `2 x 2 x 3` axes, and the expected five-step
  shared core.
- The module, batch page, and all 11 selected gene reviews render successfully.
- `git diff --check` passes; generated GO cache and unrelated PANTHER member
  noise are excluded.
