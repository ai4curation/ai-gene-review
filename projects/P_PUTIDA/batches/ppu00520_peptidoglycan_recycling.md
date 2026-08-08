---
title: "PSEPK ppu00520 peptidoglycan recycling batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00520: peptidoglycan recycling

- Reusable module: `modules/peptidoglycan_recycling.yaml`
- Broad KEGG candidates inspected: 25
- Selected pathway proteins: 8
- Ordered or branched parts: 8
- Direct KT2440 evidence: `anmK`, `amgK`, `murU`, `mupP`
- Module/pathway/taxon provider: OpenScientist

## Workflow

- [x] Separate recycling from de novo UDP-GlcNAc and UDP-MurNAc synthesis.
- [x] Recover AmpG, AmpD, and Mpl genes missed by the broad KEGG bucket.
- [x] Fetch all eight selected PSEPK genes.
- [x] Review every GOA annotation for the five newly promoted genes.
- [x] Integrate the OpenScientist report and direct KT2440 publications.
- [x] Validate module and gene reviews.
- [x] Render module, gene, and project pages.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd the PR through review and CI.

## Satisfiability

| Order | Reaction or role | PSEPK gene | UniProt | Evidence decision |
|---|---|---|---|---|
| 1 | Inner-membrane anhydromuropeptide import | `ampG` | Q88N61 | AmpG family and P. putida pathway model; target transport assay remains open |
| 2 | Terminal GlcNAc removal | `nagZ` | Q88KZ4 | NagZ family and cytoplasmic recycling model |
| 3 | Stem-peptide release | `ampD` | Q88PQ9 | Exact AmpD subfamily and EC 3.5.1.28; separated from other amidase paralogs |
| 4 | anhMurNAc to MurNAc-6-phosphate | `anmK` | Q88QQ4 | Reviewed entry and target-strain deletion phenotype |
| 5 | MurNAc-6-phosphate to MurNAc | `mupP` | Q88M11 | Direct KT2440 biochemistry, metabolomics, and mutant evidence |
| 6 | MurNAc to MurNAc-alpha-1-phosphate | `amgK` | Q88QT3 | Direct KT2440 biochemistry and genetics |
| 7 | MurNAc-alpha-1-phosphate to UDP-MurNAc | `murU` | Q88QT2 | Direct KT2440 biochemistry and genetics |
| 8 | Recovered tripeptide ligation to UDP-MurNAc | `mpl` | Q88QE7 | Exact Mpl family, GO:0106418, and Rhea 29563 |

The anabolic sugar arm is fully satisfiable in KT2440 and directly anchored by
the `anmK`, `amgK`, `murU`, and `mupP` evidence. The peptide arm is present, but
the conversion of mixed AmpD-released stem peptides to the tripeptide accepted
by Mpl may require an unresolved LdcA-like conditioning step. That connection
is recorded as a knowledge gap rather than silently treated as direct.

## Annotation Decisions

- `mupP` TreeGrafter transfer of phosphoglycolate phosphatase activity and DNA
  repair is removed because direct target-specific work establishes the
  MurNAc-6-phosphate reaction.
- Broad kinase, phosphotransferase, hydrolase, transport, and carbohydrate
  process rows are retained as non-core or marked over-annotated when exact
  substrate chemistry is available.
- `ampG` receives a proposed new peptidoglycan-turnover annotation and a request
  for a muropeptide-specific transporter molecular-function term.
- `anmK` and `mupP` require substrate-specific GO molecular-function terms;
  exact EC/Rhea chemistry is retained in prose without inventing identifiers.
- Gene-level locations are retained where supported. They are not promoted to
  generic module-level cytoplasm/cytosol or membrane assertions.

## Boundary Decisions

- MurA and MurB are excluded: they synthesize UDP-MurNAc de novo and are the
  reactions bypassed by the AmgK-MurU shortcut.
- GlmS, GlmM, and GlmU belong to the separate UDP-GlcNAc biosynthesis module.
- Alginate, dTDP-rhamnose, UDP-glucose, and UDP-galactose genes are broad
  ppu00520 map neighbors, not peptidoglycan-recycling parts.
- MurQ is not an alternate required leaf. It is absent from KT2440 and defines
  a catabolic branch used by other bacterial lineages.
- Lytic transglycosylases generate turnover fragments upstream, but their large
  paralog family is outside this focused intracellular salvage boundary.

## Grounding

Every leaf has a KT2440 UniProt exemplar. The module also records reviewed
cross-species exemplars and checkable current PANTHER/PTN nodes where the node
supports the relevant family. The stale `mupP` TreeGrafter node remains visible
in the gene-level GOA provenance but is not used as positive module grounding;
its inherited phosphoglycolate and DNA-repair claims are explicitly rejected.

## Research Status

The OpenScientist module/pathway/taxon report is integrated under
`projects/P_PUTIDA/deep-research/`. Its strongest contribution was recovering
AmpG, AmpD, and Mpl from outside the narrow KEGG candidate subset while keeping
de novo nucleotide-sugar synthesis separate. Claims were checked against the
cached full text of PMID:28351914, PMID:23831760, UniProt records, GOA, Rhea,
and local PANTHER/PAINT data.

## Validation

All eight gene reviews pass `just validate`. The module passes LinkML
`ModuleReview` validation and the dedicated semantic validator. Remaining
semantic messages are non-blocking namespace checks for InterPro/Pfam and a
deliberate AnmK PAINT-node specificity warning: the node supports generic
kinase activity while exact EC/Rhea chemistry is supplied separately. The
module, five newly fetched gene reviews, and project page render successfully.
