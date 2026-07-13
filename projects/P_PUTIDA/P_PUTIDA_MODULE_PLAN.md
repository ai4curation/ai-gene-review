---
title: "P. putida KT2440 Genome-wide Module Curation Plan"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# P. putida KT2440 Genome-wide Module Curation Plan

## Goal

Curate the *Pseudomonas putida* KT2440 proteome pathway by pathway, using module
logic as the organizing structure. The project should simultaneously improve
gene reviews under `genes/PSEPK/` and reusable module documents under
`modules/`.

The first pass is intentionally light: build a whole-proteome metadata table from
UniProt REST, group genes into pathway/module buckets, and identify holes or
over-annotations before running full `fetch-gene`, GOA review, or deep research.

## First-pass data

Use the project-local downloader:

```bash
uv run python projects/P_PUTIDA/fetch_uniprot_metadata.py
```

Default output:

- `projects/P_PUTIDA/data/psepk_uniprot_metadata.tsv`
- `projects/P_PUTIDA/data/psepk_uniprot_metadata.manifest.txt`

This is a lightweight UniProt REST TSV download for proteome `UP000000556`. It
does not create `genes/PSEPK/<gene>/` folders, fetch GOA, fetch full UniProt text
records, seed YAML, or fetch publications.

Fields used for triage: accession, entry name, gene names, protein name, taxon,
length, reviewed status, annotation score, function comment, EC number, GO IDs,
InterPro, Pfam, PANTHER, KEGG, BioCyc, UniPathway, RefSeq, and UniProt keywords.

Build the curator-facing gene list from the metadata snapshot:

```bash
python3 projects/P_PUTIDA/build_gene_list.py
```

Default output:

- `projects/P_PUTIDA/data/psepk_gene_list.tsv`
- `projects/P_PUTIDA/data/psepk_gene_list.manifest.txt`

Partition genes into first-pass pathway/module buckets:

```bash
python3 projects/P_PUTIDA/partition_pathways.py
```

Default output:

- `projects/P_PUTIDA/data/psepk_pathway_partition.tsv` — one primary bucket per
  gene.
- `projects/P_PUTIDA/data/psepk_pathway_membership.tsv` — overlapping KEGG and
  UniPathway memberships.
- `projects/P_PUTIDA/data/psepk_pathway_buckets.tsv` — bucket-level counts and
  example genes.
- `projects/P_PUTIDA/data/psepk_unknown_bucket.tsv` — unknown-function and
  minimal-signal genes.
- `projects/P_PUTIDA/data/psepk_orphan_bucket.tsv` — EC/domain-family orphans
  without a pathway/module bucket.
- `projects/P_PUTIDA/data/psepk_pathway_partition.manifest.txt`

The partitioner treats organism-specific KEGG `ppu` pathways as the primary
pathway source. Broad KEGG overview maps are retained in the membership table
but excluded from primary assignment. When a gene is in multiple specific KEGG
pathways, the primary bucket is the pathway with the smallest PSEPK gene count,
which favors narrower curation units. UniPathway is used as a fallback pathway
source, followed by metadata heuristics for non-pathway systems such as
transport, regulation, motility, DNA repair, translation, cell envelope, stress
response, and mobile elements.

Build the PR-oriented pathway worklist:

```bash
python3 projects/P_PUTIDA/build_pathway_worklist.py
```

Default output:

- `projects/P_PUTIDA/data/psepk_pathway_worklist.tsv`
- `projects/P_PUTIDA/data/psepk_pathway_worklist.manifest.txt`

Extract a per-pathway checklist for a PR batch:

```bash
python3 projects/P_PUTIDA/extract_pathway_batch.py ppu00400 --module tryptophan_biosynthesis
```

Default output for the first pilot:

- `projects/P_PUTIDA/batches/ppu00400_tryptophan_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/ppu00400_tryptophan_biosynthesis.md`

## Research provider policy

Use the cheapest useful source first:

1. UniProt metadata, local existing reviews, and module context.
2. Full `fetch-gene` only after a module pass selects the gene for curation:

```bash
just fetch-gene PSEPK <gene>
```

3. Gene-level first-pass research with Asta. For this organism, simple retrieval
   is usually enough to identify the relevant primary literature:

```bash
just deep-research-asta PSEPK <gene>
```

4. Module-level research with Falcon when a broader pathway synthesis is needed:

```bash
just module-deep-research-falcon <module>
```

5. For species-aware module/pathway research, use the module + pathway + taxon
   wrapper. This keeps generic module research separate from PSEPK-specific
   satisfiability work and injects local candidate genes from the pathway
   partition table when available:

```bash
just module-pathway-deep-research-falcon "central carbon metabolism" ppu00020 PSEPK
```

The report is written under the project support folder by default, e.g.
`projects/P_PUTIDA/deep-research/PSEPK__central-carbon-metabolism__ppu00020-deep-research-falcon.md`.

6. PaperBLAST remains an optional protein-specific lookup:

```bash
uv run python scripts/fetch_paperblast.py <uniprot_accession>
```

7. Use `perplexity-lite` only as a secondary fallback when Asta is unavailable
   or comparison across providers is useful.
8. Escalate to OpenAI/perplexity/full manual literature only when the first-pass
   provider output leaves a curation-changing question unresolved.

Operational caveat: the repository has a PaperBLAST wrapper, but it depends on
Playwright and the PaperBLAST website can present a Cloudflare challenge. If the
script returns a timeout or challenge page, record that in the module checklist
and use Asta or another fallback rather than pretending PaperBLAST was queried.

Never create a fake `-deep-research-{provider}.md` by hand. If manual notes are
needed, write them as notes or a clearly named manual research file.

## Module-hole-filling workflow

For each module:

1. Define the expected pathway shape in `modules/*.yaml` or identify that a new
   module document is needed. A standalone module must have more than one
   substantive part. If a UniPathway/KEGG bucket is a single gene, single enzyme,
   or single reaction, record the curation in the batch page and fold it into a
   broader multi-step module later rather than creating or retaining a one-part
   `ModuleReview`.
2. Pull candidate PSEPK genes from the metadata table using EC, KEGG `ppu:*`,
   BioCyc monomers, UniPathway, InterPro/Pfam/PANTHER families, GO IDs, keywords,
   protein names, and locus tags.
3. Classify each pathway step as `covered`, `candidate_uncertain`, `gap`,
   `not_expected_in_KT2440`, or `module_needs_revision`.
4. For covered steps, record representative UniProt groundings in the module
   where useful.
5. For gaps and uncertain candidates, run targeted gene review and decide
   whether the gap is a real biological absence, a naming/paralog issue, a
   missing annotation, a bad propagated annotation, or a module-model error.
6. Validate changed modules with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/<module>.yaml
```

## Initial module order

| Phase | Module area | Existing module seed | First-pass question | Expected outputs |
|---|---|---|---|---|
| 0 | Whole-proteome inventory | none | What genes, accessions, ECs, pathways, families, and keywords are present in PSEPK? | Metadata TSV; module-bucket table; selected first batch |
| 1 | Entner-Doudoroff, pentose phosphate, TCA, glyoxylate, anaplerosis | `modules/gluconeogenesis.yaml`, `modules/fatty_acid_beta_oxidation.yaml` as style references | Does the module set capture P. putida central-carbon logic, including no canonical EMP glycolysis? | New or revised central-carbon modules; review selected ED/TCA gaps |
| 2 | Aromatic compound catabolism | likely new beta-ketoadipate / aromatic-catabolism modules | Are benzoate, catechol, protocatechuate, quinate/shikimate, phenylacetate, tyrosine, and ferulate routes satisfiable? | Beta-ketoadipate and related modules; review missing or over-specific ring-cleavage annotations |
| 3 | Amino-acid biosynthesis and nitrogen assimilation | `modules/tryptophan_biosynthesis.yaml`, `modules/methionine_biosynthesis.yaml`, `modules/nitrogen_cycle.yaml` | Which biosynthetic pathways are complete and where do Pseudomonas-specific variants replace textbook enzymes? | Update modules with PSEPK exemplars; review variant enzymes and broad nitrogen terms |
| 4 | Cofactors, vitamins, redox cofactors, metal handling | possible new modules | Are pyrroloquinoline quinone, heme, Fe-S, molybdenum cofactor, siderophore, and lanthanide-related systems represented? | New cofactor/siderophore/REE modules; targeted ped/pvd/lut reviews |
| 5 | Energy metabolism and respiratory chains | `modules/oxphos.yaml` | Which terminal oxidases, dehydrogenases, and anaerobic respiration modules are encoded? | PSEPK respiratory-chain module coverage; EC7/translocase convention checks |
| 6 | Cell envelope, secretion, transport, and efflux | possible new modules | Which outer-membrane porins, TonB receptors, RND pumps, secretion systems, and envelope biogenesis pathways need module treatment? | Transport/envelope worklists; scrutiny of generic transporter annotations |
| 7 | Motility, chemotaxis, pili, biofilm, alginate | possible new modules | Are flagellar assembly, chemotaxis receptors, type IV pilus, alginate, and biofilm regulation wired consistently? | Motility/biofilm modules; gene reviews for receptors/regulators selected by module gaps |
| 8 | Stress response, DNA repair, and regulatory networks | `modules/two_component_relay.yaml`, `modules/gtpase_switch.yaml` as style references | Which global regulators and repair/stress systems are already reviewed, and which are module-critical gaps? | Regulator module updates; targeted sigma/two-component/DNA-repair reviews |
| 9 | Specialized metabolism and biotechnology traits | possible new PHA, solvent tolerance, olefin, plant-interaction modules | Which KT2440 signature traits are absent from reusable modules? | New modules for PHA, solvent tolerance, olefin biosynthesis, and plant-associated traits |
| 10 | Dark proteome and orphan enzymes | none | Which high-confidence proteins remain unassigned to any module and which DUFs look curation-relevant? | Prioritized orphan list; optional bioinformatics analyses |

## Module curation deliverables

Each module batch should leave behind:

- A module checklist in this subfolder naming candidate genes, expected steps,
  and gap decisions.
- Any revised or new `modules/*.yaml` files, only when the reusable module has
  more than one substantive part.
- A short list of genes promoted from metadata-only triage to full review.
- Links to completed gene reviews and validation commands run.
- Notes on GO term gaps, obsolete/broad terms, and cases where a PSEPK enzyme
  fills a pathway step under a different name than the standard model organism.

## Pilot status: ppu00400 / tryptophan_biosynthesis

Pilot batch files:

- `projects/P_PUTIDA/batches/ppu00400_tryptophan_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/ppu00400_tryptophan_biosynthesis.md`

Status as of 2026-07-05 PDT / 2026-07-06 UTC:

- 28 KEGG `ppu00400` candidate genes extracted from pathway membership.
- 28/28 review folders present.
- 28/28 Asta gene-level retrieval reports present.
- 28/28 review YAMLs curated with no remaining `PENDING` actions.
- Falcon generic module research complete:
  `modules/tryptophan_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__tryptophan_biosynthesis__ppu00400-deep-research-falcon.md`.
- Validation complete for all 28 gene reviews with `just validate PSEPK <gene>`.
- Module validation complete with:
- PR merged: [#1874](https://github.com/ai4curation/ai-gene-review/pull/1874).

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/tryptophan_biosynthesis.yaml
```

Main curation conclusions from the pilot:

- The strict tryptophan module is chorismate to L-tryptophan and is covered in
  KT2440 by `trpE`, PP_0420/TrpG-like `pabA`, `trpD`, `trpC`, `trpF`, `trpA`,
  and `trpB`.
- The broad KEGG `ppu00400` map also pulls in shared shikimate genes
  (`aroB`, `aroK`, `aroA`, `aroC`, aroE/aroQ/DAHP-synthase paralogs),
  phenylalanine/tyrosine branch genes (`pheA`, `tyrB`, `amaC`, `phhA`), and
  quinate/aromatic-catabolic genes (`quiC1`, `quiA`). These should be handled as
  neighboring or shared-pathway context, not as core tryptophan module members.
- PP_0420 is the main curation issue: current metadata names it `pabA`, but the
  KT2440 tryptophan-pathway context supports treating it as the TrpG-like
  anthranilate synthase amidotransferase component. Folate/pABA activity remains
  unresolved pending direct evidence.
- Paralog ambiguity remains for aroE, aroQ, and DAHP synthase copies. The pilot
  reviews accept the enzyme-class annotations while avoiding claims about which
  paralog uniquely satisfies upstream shikimate flux.

## Batch status: ppu00010 / entner_doudoroff_and_gluconeogenesis

Batch files:

- `projects/P_PUTIDA/batches/ppu00010_entner_doudoroff_and_gluconeogenesis.tsv`
- `projects/P_PUTIDA/batches/ppu00010_entner_doudoroff_and_gluconeogenesis.md`

Status as of 2026-07-06:

- 38 KEGG `ppu00010` candidate genes extracted from pathway membership.
- 38/38 review folders present.
- 38/38 Asta gene-level retrieval reports present.
- 38/38 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral module seed created:
  `modules/entner_doudoroff_and_gluconeogenesis.yaml`.
- Falcon generic module research complete:
  `modules/entner_doudoroff_and_gluconeogenesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__entner_doudoroff_and_gluconeogenesis__ppu00010-deep-research-falcon.md`.
- Validation complete for all 38 gene reviews with `just validate PSEPK <gene>`
  over the batch list.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/entner_doudoroff_and_gluconeogenesis.yaml
```

Main curation conclusions from this batch:

- KT2440 glucose catabolism is ED/EDEMP-centered, not canonical
  phosphofructokinase-dependent EMP glycolysis. The neutral module therefore
  covers ED entry, lower-EMP trunk reactions, and gluconeogenic return.
- KEGG `ppu00010` is not the same as the strict ED module. The candidate list
  omits the defining ED genes `edd` and `eda`, which were handled through the
  broader central-carbon/PPP context, and pulls in pyruvate dehydrogenase,
  lipoate, alcohol/aldehyde oxidation, acetyl-CoA synthetase, and sugar-epimerase
  side nodes.
- Newly filled reviews include lower-trunk/core-relevant genes (`gapB`, `gpmI`,
  `pyk`) plus adjacent nodes (`aceE`, `aceF`, `acoC`, `lpd`, `lpdG`, `lpdV`,
  `acsA1`, `acsA2`, `aldB-I`, `frmA`, `calA`, `adhP`, `PP_1165`, `PP_2213`,
  `PP_5332`).
- Alias handling matters: the `aldB-II` row resolves to the existing `pedI`
  review for Q88JG9/PP_2680, and `pedE` resolves to the existing `pede` review
  folder. The batch extractor's accession-based resolution avoided duplicate
  review folders.
- The TCA-overlap pyruvate dehydrogenase/lipoate genes filled here reconcile the
  earlier `ppu00020` missing rows.

## Batch status: ppu00020 / tca_cycle

Batch files:

- `projects/P_PUTIDA/batches/ppu00020_tca_cycle.tsv`
- `projects/P_PUTIDA/batches/ppu00020_tca_cycle.md`

Status as of 2026-07-06:

- 30 KEGG `ppu00020` candidate genes extracted from pathway membership.
- 30/30 review folders present.
- 30/30 Asta gene-level retrieval reports present.
- 30/30 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral module seed created:
  `modules/tca_cycle.yaml`.
- Falcon generic module research complete:
  `modules/tca_cycle-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__tca_cycle__ppu00020-deep-research-falcon.md`.
- Validation complete for all 30 gene reviews and the module; the remaining
  warnings are only that Asta retrieval files exist but were not cited where
  they did not provide curation-changing evidence.

Main curation conclusions from this batch:

- The strict oxidative TCA cycle is satisfiable in KT2440. Core cycle coverage
  includes `gltA`, aconitase paralogs (`acnA-I`, `acnB`), NADP-dependent
  isocitrate dehydrogenases (`icd`, `idh`), the OGDH/SucAB/Lpd node, SucCD,
  SdhABCD, fumarases (`PP_0897`, `fumC-I`, `fumC`), `mdh`, and MQO paralogs
  (`mqo1`, `mqo2`, `mqo3`).
- `prpC`, `scpC`, and parts of the acnB neighborhood are methylcitrate or
  propionate side-branch context. They should not be used alone to satisfy the
  core citrate synthase or aconitase steps when the canonical TCA genes are
  present.
- `mqo1`, `mqo2`, and `mqo3` support quinone-coupled malate oxidation
  (`GO:0008924`) and the TreeGrafter `(S)-2-hydroxyglutarate dehydrogenase`
  activity was removed as a paralog/family over-propagation.
- `pycA`/`pycB` are retained as an anaplerotic oxaloacetate-entry node; PycB
  InterPro-derived sodium transport and oxaloacetate decarboxylase annotations
  were removed as OadA-family over-propagation.
- `PP_0897` was given a new TCA-cycle process annotation because its GOA rows
  had the fumarase molecular function but only a broad metabolic process.

## Batch status: ppu00030 / pentose_phosphate_pathway

Batch files:

- `projects/P_PUTIDA/batches/ppu00030_pentose_phosphate_pathway.tsv`
- `projects/P_PUTIDA/batches/ppu00030_pentose_phosphate_pathway.md`

Status as of 2026-07-06:

- 36 KEGG `ppu00030` candidate genes extracted from pathway membership.
- 36/36 review folders present.
- 36/36 Asta gene-level retrieval reports present.
- 36/36 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral module seed created:
  `modules/pentose_phosphate_pathway.yaml`.
- Falcon generic module research complete:
  `modules/pentose_phosphate_pathway-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__pentose_phosphate_pathway__ppu00030-deep-research-falcon.md`.
- Validation complete for all 36 gene reviews with `just validate PSEPK <gene>`
  over the batch list.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/pentose_phosphate_pathway.yaml
```

Main curation conclusions from this batch:

- The strict PPP steps are satisfiable in KT2440, but KEGG `ppu00030` is much
  broader than the strict module. Falcon classifies the pathway in the organism
  as embedded in the ED/EMP/PPP `EDEMP` cycle rather than as an isolated linear
  PPP.
- Core PPP coverage includes glucose-6-phosphate dehydrogenase paralogs
  (`zwf`, `zwfA`, `zwfB`), canonical `pgl`, `gntZ`, `rpe`, `rpiA`, `tal`, and
  `tktA`. These should satisfy the neutral PPP module; ED and peripheral
  glucose-oxidation genes should not.
- KEGG `ppu00030` pulls in ED genes (`edd`, `eda`), peripheral glucose/gluconate
  oxidation genes (`gcd`, `gnuK`, `kguK`, `PP_3382`-`PP_3384`, `ptxD`,
  `PP_1661`), ribose/PRPP genes (`prs`, `rbsK`, `phnN`), EDEMP coupling genes
  (`pgi1`, `pgi2`, `fba`, `fbp`, `PP_3443`), and cell-envelope sugar-node genes
  (`cpsG`, `pgm`, `algC`). These are pathway-adjacent, not strict PPP members.
- `pgm` required an alias correction: UniProt `gpmI`/Q88CX4 has synonym `pgm`,
  but KEGG `ppu00030` `pgm` is PP_3578/Q88GY7 phosphoglucomutase. The review
  folder now targets Q88GY7.
- `ptxD` remains a follow-up ambiguity. The first-pass review accepts the
  phosphonate dehydrogenase EC/name and removes conflicting TreeGrafter
  glyoxylate/hydroxypyruvate reductase calls, while Falcon flags a possible
  peripheral 2-keto-6-phosphogluconate context worth deeper targeted review.

## Batch status: ppu00362 / benzoate_degradation

Batch files:

- `projects/P_PUTIDA/batches/ppu00362_benzoate_degradation.tsv`
- `projects/P_PUTIDA/batches/ppu00362_benzoate_degradation.md`

Status as of 2026-07-06:

- 40 KEGG `ppu00362` candidate genes extracted from pathway membership.
- 40/40 review folders present.
- 40/40 Asta gene-level retrieval reports present.
- 40/40 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral module seed created:
  `modules/benzoate_degradation.yaml`.
- Falcon generic module research complete:
  `modules/benzoate_degradation-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__benzoate_degradation__ppu00362-deep-research-falcon.md`.
- Validation complete for all 40 gene reviews with `just validate PSEPK <gene>`
  over the batch list.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/benzoate_degradation.yaml
uv run python -m ai_gene_review.validation.module_validator modules/benzoate_degradation.yaml
```

Main curation conclusions from this batch:

- The strict benzoate/beta-ketoadipate route is satisfiable in KT2440. Core
  coverage includes benzoate entry via `benA`, `benB`, `benC`, and `benD`;
  catechol ortho cleavage via `catA-I`/`catA-II`, `catB`, and `catC`;
  4-hydroxybenzoate/protocatechuate entry via `pobA`, `pcaG`, `pcaH`, `pcaB`,
  `pcaC`, and `pcaD`; and terminal beta-ketoadipate CoA metabolism via `pcaI`,
  `pcaJ`, and `pcaF`/`paaJ`.
- KEGG `ppu00362` is broader than the strict module. It mixes the benzoate
  funnel with gallate genes (`galB`, `galC`, `galD`), phenylacetate-side nodes,
  fatty-acid-like CoA enzymes, cytochrome P450/ferredoxin side nodes, and generic
  thiolases.
- The side-node fatty-acid, butanoate, and generic thiolase genes were curated
  as enzyme reviews where supported, but they should not be used to satisfy
  strict benzoate or beta-ketoadipate module steps.
- `PP_3648` is a reviewed no-GOA CMD-family case with uncertain pathway role,
  and `PP_1791` remains undecided with no core function because the available
  first-pass evidence does not resolve the family-level synthase/pathway call.

## Batch status: ppu01220 / aromatic_compound_degradation

Batch files:

- `projects/P_PUTIDA/batches/ppu01220_aromatic_compound_degradation.tsv`
- `projects/P_PUTIDA/batches/ppu01220_aromatic_compound_degradation.md`

Status as of 2026-07-06:

- 20 KEGG `ppu01220` candidate genes extracted from pathway membership.
- 20/20 review folders present.
- 20/20 Asta gene-level retrieval reports present.
- 20/20 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral umbrella module seed created:
  `modules/aromatic_compound_degradation.yaml`.
- Falcon generic module research complete:
  `modules/aromatic_compound_degradation-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__aromatic_compound_degradation__ppu01220-deep-research-falcon.md`.
- Validation complete for all 20 gene reviews using the resolved `review_file`
  paths from the batch TSV.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/aromatic_compound_degradation.yaml
uv run python -m ai_gene_review.validation.module_validator modules/aromatic_compound_degradation.yaml
```

Main curation conclusions from this batch:

- `ppu01220` is an umbrella map, not a single linear module. The module should
  be used to separate route-specific aromatic catabolic funnels from broad-map
  cofactor, redox, and side-node enzymes.
- KT2440's core benzoate/4-hydroxybenzoate ortho-cleavage route is satisfiable,
  but KEGG `ppu01220` omits the lower beta-ketoadipate genes `pcaI`, `pcaJ`, and
  `pcaF`. Those genes are present in KT2440 and were already curated in the
  `ppu00362` / `benzoate_degradation` batch.
- High-confidence ppu01220 core candidates include `benA`, `benB`, `benC`,
  `benD`, `pobA`, `catA-I`, `catB`, `catC`, `pcaG`, `pcaH`, `pcaB`, `pcaC`, and
  `pcaD`. `catA-II` is retained as a paralog-ambiguous catechol
  1,2-dioxygenase, and `PP_3648` remains a substrate-ambiguous CMD-family
  protein.
- `ubiX`, `frmA`, `adhP`, `PP_1791`, and `PP_2504` are side-node or
  over-propagated members for this umbrella. The new `ubiX` review accepts
  flavin prenyltransferase activity, proposes ubiquinone biosynthetic process,
  and removes the TreeGrafter carboxy-lyase call as UbiD/UbiX family
  over-propagation.

## Batch status: ppu00622 / benzoate_upper_pathway

Batch files:

- `projects/P_PUTIDA/batches/ppu00622_benzoate_upper_pathway.tsv`
- `projects/P_PUTIDA/batches/ppu00622_benzoate_upper_pathway.md`

Status as of 2026-07-06:

- 6 KEGG `ppu00622` candidate genes extracted from pathway membership.
- 6/6 review folders present.
- 6/6 Asta gene-level retrieval reports present.
- 6/6 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral upper-pathway module seed created:
  `modules/benzoate_upper_pathway.yaml`.
- Falcon generic module research complete:
  `modules/benzoate_upper_pathway-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__benzoate_upper_pathway__ppu00622-deep-research-falcon.md`.
- Validation complete for all 6 gene reviews using the resolved `review_file`
  paths from the batch TSV.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/benzoate_upper_pathway.yaml
uv run python -m ai_gene_review.validation.module_validator modules/benzoate_upper_pathway.yaml
```

Main curation conclusions from this batch:

- The strict upper pathway is satisfiable in KT2440 with `benA`, `benB`,
  `benC`, and `benD`. BenABC supplies benzoate 1,2-dioxygenase activity and
  BenD supplies benzoate cis-dihydrodiol dehydrogenase activity to produce
  catechol.
- KEGG `ppu00622` is named "Xylene degradation" and is broader than this module.
  The PSEPK satisfiable route is the chromosomal BenABCD benzoate-to-catechol
  branch, not a full TOL-plasmid xylene/toluene meta-cleavage pathway.
- `PP_1791` and `PP_2504` are side meta-cleavage context in the KEGG map and
  should not satisfy the BenABCD upper pathway. `catA-II` is downstream
  ortho-cleavage context and outside this module boundary.

## Batch status: ppu00270 / methionine_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/ppu00270_methionine_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/ppu00270_methionine_biosynthesis.md`

Status as of 2026-07-06:

- 46 KEGG `ppu00270` candidate genes extracted from pathway membership.
- 46/46 review folders present.
- 46/46 Asta gene-level retrieval reports present.
- 46/46 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral module present:
  `modules/methionine_biosynthesis.yaml`.
- Falcon generic module research complete:
  `modules/methionine_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__methionine_biosynthesis__ppu00270-deep-research-falcon.md`.
- Validation complete for all 46 gene reviews using the resolved
  `suggested_review_name` paths from the batch TSV.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/methionine_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/methionine_biosynthesis.yaml
```

Main curation conclusions from this batch:

- The strict L-methionine biosynthesis-from-homoserine module is satisfiable in
  KT2440. The primary route is homoserine O-succinylation by `metXS`/MetXW,
  sulfur incorporation by `metZ`, and terminal methylation by `metE` and/or
  `metH`.
- KT2440 also carries secondary or candidate sulfur-incorporation context:
  `metB`, `PP_4348`, `PP_4594`, and `PP_2528`. These should be kept distinct
  from the preferred direct sulfhydrylation route unless deeper evidence
  supports a primary role.
- KEGG `ppu00270` is broader than the scoped module. The batch includes
  upstream aspartate-family precursor genes, cysteine biosynthesis genes,
  methionine salvage and SAM-cycle genes, DNA methyltransferases,
  serine/threonine/BCAA side nodes, and sulfurtransferases.
- Curation fixes included modifying `metXS` toward homoserine
  O-succinyltransferase rather than generic O-acetyltransferase, avoiding
  full-MetE acceptance for `PP_4637`, removing bacterial-inappropriate
  CpG-island methylation process terms from DNA methyltransferases, and removing
  hydroxyglutarate/family over-propagation from `serA`.

## Batch status: ppu00340 / histidine_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/ppu00340_histidine_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/ppu00340_histidine_biosynthesis.md`

Status as of 2026-07-06:

- 20 KEGG `ppu00340` candidate genes extracted from pathway membership.
- 20/20 review folders present.
- 20/20 Asta gene-level retrieval reports present.
- 20/20 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral module updated:
  `modules/histidine_biosynthesis.yaml`.
- Falcon generic module research complete:
  `modules/histidine_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__histidine_biosynthesis__ppu00340-deep-research-falcon.md`.
- Validation complete for all 20 gene reviews using the batch TSV.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/histidine_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/histidine_biosynthesis.yaml
```

Main curation conclusions from this batch:

- KT2440 has the expected de novo histidine biosynthesis route, including the
  short-form `hisG`/`hisZ` ATP phosphoribosyltransferase system, separate
  `hisE` and `hisI` genes, `hisA`, `hisH`/`hisF`, `hisB`, `hisC`, and `hisD`.
- The histidinol-phosphate phosphatase step is the main unresolved module point:
  `PP_3157` and `PP_5147` are both plausible EC 3.1.3.15 candidates, and direct
  KT2440 evidence is still needed to distinguish redundancy from over-annotation.
- KEGG `ppu00340` is broader than the biosynthesis module. The `hutH`, `hutU`,
  `hutI`, `hutF`, and `hutG` genes are histidine utilization/catabolism, while
  `gshA`, `PP_4983`, and `PP_1721` are off-pathway or over-mapped side nodes.
- Module curation fixed a neutral-module error: the HisE pyrophosphohydrolase
  and HisI cyclohydrolase step labels and connection order were reversed. Both
  Falcon reports were regenerated after this correction.

## Batch status: ppu00052 / galactose_leloir_pathway

Batch files:

- `projects/P_PUTIDA/batches/ppu00052_galactose_leloir_pathway.tsv`
- `projects/P_PUTIDA/batches/ppu00052_galactose_leloir_pathway.md`

Status as of 2026-07-06:

- 8 KEGG `ppu00052` candidate genes extracted from pathway membership.
- 8/8 review folders present.
- 8/8 Asta gene-level retrieval reports present.
- 8/8 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral module updated:
  `modules/galactose_leloir_pathway.yaml`.
- Falcon generic module research complete:
  `modules/galactose_leloir_pathway-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__galactose_leloir_pathway__ppu00052-deep-research-falcon.md`.
- Validation complete for all 8 gene reviews using the batch TSV.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/galactose_leloir_pathway.yaml
uv run python -m ai_gene_review.validation.module_validator modules/galactose_leloir_pathway.yaml
```

Main curation conclusions from this batch:

- Canonical Leloir galactose catabolism is not satisfied in KT2440. The
  committed `galK` and `galT` steps are absent, and the PSEPK Falcon report
  supports the expected organism-level call that wild-type KT2440 does not
  natively grow on D-galactose without engineered heterologous routes.
- `galE` is a valid UDP-glucose 4-epimerase but should not be treated as
  evidence for a complete catabolic Leloir cycle in this organism. The existing
  Leloir-pathway BP annotation was marked over-annotated.
- `galU`, `algC`, `cpsG`, and `pgm` are UDP-sugar, glycogen, cell-envelope, or
  central-carbohydrate side nodes. `glk` and `PP_1165` belong with glucose or
  aldose handling rather than galactose pathway satisfaction.
- `PP_0501` remains an uncertain NAD-dependent epimerase/dehydratase family
  protein. The first-pass review leaves it with no core function.
- KEGG `ppu00052` is a broad metabolite map in this organism, not a satisfiable
  Leloir module.

## Batch status: ppu00040 / pentose_glucuronate_interconversions

Batch files:

- `projects/P_PUTIDA/batches/ppu00040_pentose_glucuronate_interconversions.tsv`
- `projects/P_PUTIDA/batches/ppu00040_pentose_glucuronate_interconversions.md`

Status as of 2026-07-06 PDT / 2026-07-07 UTC:

- 8 KEGG `ppu00040` candidate genes extracted from pathway membership.
- 8/8 KEGG candidate review folders present.
- 8/8 KEGG candidate Asta gene-level retrieval reports present.
- 8/8 KEGG candidate review YAMLs curated with no remaining `PENDING` actions.
- 2 additional Falcon-promoted gap-fill genes, `gnl`/PP_1170 and
  `udh`/PP_1171, fetched, Asta-backed, curated, and validated.
- Species-neutral boundary module updated:
  `modules/pentose_glucuronate_interconversions.yaml`.
- Falcon generic module research complete:
  `modules/pentose_glucuronate_interconversions-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__pentose_glucuronate_interconversions__ppu00040-deep-research-falcon.md`.
- Validation complete for the 8 KEGG candidate gene reviews plus the 2
  promoted gap-fill gene reviews.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/pentose_glucuronate_interconversions.yaml
uv run python -m ai_gene_review.validation.module_validator modules/pentose_glucuronate_interconversions.yaml
```

Main curation conclusions from this batch:

- KEGG `ppu00040` is a composite boundary map in KT2440, not one satisfiable
  linear pathway. It conflates PPP pentose-phosphate chemistry, UDP-sugar
  biosynthesis, and oxidative free-hexuronate/aldarate catabolism.
- The well-supported KEGG candidates are `rpe` for PPP/EDEMP context, `galU`
  for UDP-glucose supply, and `udg` for UDP-glucuronate formation. `galU` and
  `udg` should be treated as nucleotide-sugar/cell-envelope precursor nodes, not
  as evidence for free uronate degradation.
- The oxidative hexuronate arm is missing from the initial KEGG candidate set.
  `udh`/PP_1171 is experimentally characterized for glucuronate and
  galacturonate oxidation, and `gnl`/PP_1170 is the strongest first-pass
  lactonase candidate. Both were promoted to full review.
- The aldarate dehydratase step and the correct glucarate-linked KGSADH paralog
  were left as follow-up gaps for the adjoining `ppu00053` pass. `PP_1256`,
  `PP_2585`, and `PP_3602` were kept as predicted
  2,5-dioxovalerate/KGSA dehydrogenases, but none was counted as uniquely
  satisfying the hexuronate arm from the ppu00040 evidence alone.
- `PP_2037` and `PP_2694` are weak KEGG-side candidates: the former has likely
  over-propagated aldolase/adducin-family annotations, and the latter has only
  broad ALDH-family support.

## Batch status: ppu00053 / hexuronate_aldarate_catabolism

Batch files:

- `projects/P_PUTIDA/batches/ppu00053_hexuronate_aldarate_catabolism.tsv`
- `projects/P_PUTIDA/batches/ppu00053_hexuronate_aldarate_catabolism.md`

Status as of 2026-07-06 PDT / 2026-07-07 UTC:

- 8 KEGG `ppu00053` candidate genes extracted from pathway membership.
- 8/8 KEGG candidate review folders present.
- 8/8 KEGG candidate Asta gene-level retrieval reports present.
- 8/8 KEGG candidate review YAMLs curated with no remaining `PENDING` actions.
- `gnl`/PP_1170, promoted during the ppu00040 boundary pass, was retained as
  the non-KEGG UxuL-family lactonase context for this module and rechecked
  against the ppu00053 Falcon report.
- Species-neutral module created:
  `modules/hexuronate_aldarate_catabolism.yaml`.
- Falcon generic module research complete:
  `modules/hexuronate_aldarate_catabolism-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__hexuronate_aldarate_catabolism__ppu00053-deep-research-falcon.md`.
- Validation complete for the 8 KEGG candidate gene reviews plus `gnl`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/hexuronate_aldarate_catabolism.yaml
uv run python -m ai_gene_review.validation.module_validator modules/hexuronate_aldarate_catabolism.yaml
```

Main curation conclusions from this batch:

- KEGG `ppu00053` is best curated in KT2440 as free-hexuronate/aldarate
  catabolism, not as eukaryotic ascorbate metabolism and not as
  UDP-glucuronate nucleotide-sugar biosynthesis.
- The satisfiable oxidative route is `udh`/PP_1171 for hexuronate oxidation,
  `gnl`/PP_1170 as the UxuL-family lactonase candidate, `gudD`/PP_4757 and
  `garD`/PP_3601 as glucarate and galactarate dehydratases,
  `PP_3599`/KdgD for 5-dehydro-4-deoxyglucarate dehydration, and
  `PP_3602`/KgsD as the strongest local aldarate-pathway KGSADH candidate.
- `PP_1256` and `PP_2585` remain valid KGSADH-like enzyme reviews, but Falcon
  treats them as candidate-uncertain paralogs for this specific module because
  they lack the `garD`/`kdgD` neighborhood context that supports `PP_3602`.
- `udg`/PP_2926 is a UDP-glucose 6-dehydrogenase for UDP-glucuronate and
  cell-envelope or polysaccharide precursor chemistry. It is a KEGG side node,
  not a free-aldarate catabolic step.
- GO currently lacks a substrate-resolved UxuL/UxuF molecular-function term for
  glucaro- or galactaro-1,5-lactonase activity, so `gnl` is retained under the
  broader gluconolactonase-family activity while the module records the more
  specific biological hypothesis.

## Batch status: ppu00051 / fructose_mannose_metabolism

Batch files:

- `projects/P_PUTIDA/batches/ppu00051_fructose_mannose_metabolism.tsv`
- `projects/P_PUTIDA/batches/ppu00051_fructose_mannose_metabolism.md`

Status as of 2026-07-06 PDT / 2026-07-07 UTC:

- 18 KEGG `ppu00051` candidate genes extracted from pathway membership.
- 18/18 KEGG candidate review folders present.
- 18/18 KEGG candidate Asta gene-level retrieval reports present.
- 18/18 KEGG candidate review YAMLs curated with no remaining `PENDING`
  actions.
- `fruB`/PP_0793, promoted by the PSEPK Falcon report from the adjacent
  `ppu02060` PTS bucket, was fetched, Asta-backed, curated, and validated as
  the missing PEP-dependent fructose PTS phosphorelay component.
- Species-neutral boundary module created and updated after Falcon:
  `modules/fructose_mannose_metabolism.yaml`.
- Falcon generic module research complete:
  `modules/fructose_mannose_metabolism-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__fructose_mannose_metabolism__ppu00051-deep-research-falcon.md`.
- Validation complete for the 18 KEGG candidate gene reviews plus `fruB`.
  `PP_2037` intentionally remains valid with a no-core-function warning because
  Falcon supports treating it as a likely KEGG spillover artifact.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/fructose_mannose_metabolism.yaml
uv run python -m ai_gene_review.validation.module_validator modules/fructose_mannose_metabolism.yaml
```

Main curation conclusions from this batch:

- KEGG `ppu00051` is a composite boundary map in KT2440, not one coherent
  pathway. It combines fructose PTS entry, GDP-mannose/alginate precursor
  synthesis, alginate polymerization/export, LPS/O-antigen deoxy-sugar
  nucleotide chemistry, and central-carbon spillover genes.
- The fructose PTS entry branch is `fruB`/`fruA` plus `fruK`; Falcon correctly
  flagged that the KEGG `ppu00051` candidate set had `fruA` and `fruK` but
  missed `fruB` because `fruB` is assigned to the separate PTS bucket.
- `PP_1776` was corrected from an AlgA-like/alginate interpretation to a
  WbpW-like GDP-mannose enzyme for the LPS/O-antigen branch. `gmd` and `rmd`
  were correspondingly updated to the GDP-D-rhamnose/LPS branch, including the
  exact Rmd reductase term `GO:0033705`.
- `algA`, `algC`, and `algD` form the GDP-mannose/GDP-mannuronate precursor
  branch for alginate, while `alg8`, `alg44`, `algG`, and `algL` belong with
  alginate polymerization/export and should ultimately be tracked with
  `ppu00543` or a dedicated alginate/EPS module.
- `tpiA`, `fba`, `fbp`, `PP_2037`, and `fucD` are useful context but do not all
  satisfy the same module. `fbp` is relevant to KT2440 fructose flux routing;
  `PP_2037` is retained without a core function as a likely KEGG side artifact.

## Batch status: ppu00061 / fatty_acid_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/ppu00061_fatty_acid_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/ppu00061_fatty_acid_biosynthesis.md`

Status as of 2026-07-06 PDT / 2026-07-07 UTC:

- 19 KEGG `ppu00061` membership candidates extracted from pathway membership.
- 19/19 candidate review folders present.
- 19/19 candidate Asta gene-level retrieval reports present.
- 19/19 candidate review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral FAS-II boundary module created:
  `modules/fatty_acid_biosynthesis.yaml`.
- Falcon generic module research complete:
  `modules/fatty_acid_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__fatty_acid_biosynthesis__ppu00061-deep-research-falcon.md`.
- Validation complete for all 19 candidate gene reviews. `PP_0581`, `PP_1852`,
  and `PP_2540` intentionally remain valid with no-core-function warnings
  because the Falcon-backed first-pass evidence supports only boundary or
  uncertain SDR/reductase context.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/fatty_acid_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/fatty_acid_biosynthesis.yaml
```

Main first-pass curation conclusions from this batch:

- The canonical ACC/FAS-II route is covered by `accA`, `accB`, `accC`, `accD`,
  `fabD`, `fabG`, `fabZ`, `fabF`, `fabA`, `fabB`, `PP_4379`, and `fabV`.
- Falcon confirms that the pseudomonad initiation step should not be modeled as
  FabH-only. `fabB` is now captured as a possible FabH-independent initiator,
  while `PP_4379` remains a candidate KAS III initiator whose essentiality is
  not assumed.
- `PP_3303` remains a plausible FabF/KAS-II-like candidate. `PP_1852` was
  downgraded to an undecided/boundary reductase candidate because `fabV` is the
  best core enoyl-ACP reductase assignment.
- `fadD-I` and `fadD-II` are valid long-chain fatty-acid-CoA ligases for fatty
  acid activation and beta-oxidation/assimilation context, but they are not
  counted as de novo acyl-ACP FAS-II enzymes.
- `PP_2783` is best curated as a p-cumate/aromatic-compound dehydrogenase; its
  TreeGrafter fatty-acid-elongation annotation was removed as an SDR-family
  spillover.
- `PP_0581` and `PP_2540` have insufficient first-pass evidence for a substrate
  resolved fatty-acid biosynthesis function, so they are retained without core
  functions until later biochemical context resolves them.

## Batch status: UPA00094 / fatty_acid_biosynthesis ACP support

Batch files:

- `projects/P_PUTIDA/batches/UPA00094_fatty_acid_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/UPA00094_fatty_acid_biosynthesis.md`

Status as of 2026-07-09 PDT / 2026-07-10 UTC:

- 8 UniPathway `UPA00094` membership candidates extracted from pathway
  membership.
- 8/8 candidate review folders present.
- 8/8 candidate Asta gene-level retrieval reports present.
- 8/8 candidate review YAMLs curated with no remaining `PENDING` actions.
- UniPathway-primary `acpP` / Q88LL5 / PP_1915 was fetched, Asta-backed,
  curated, validated, and rendered in this checkpoint.
- Already-curated `accB`, `fabG`, `fabF`, `PP_3303`, `fabA`, `fabB`, and
  `fabV` were reused as the rest of the UPA00094 FAS-II context.
- `modules/fatty_acid_biosynthesis.yaml` was extended with
  `UniPathway:UPA00094` evidence and an explicit AcpP acyl-carrier annoton.
- The existing generic Falcon report is reused:
  `modules/fatty_acid_biosynthesis-deep-research-falcon.md`.
- The real PSEPK module+pathway Falcon command was run for UPA00094 and failed
  before report generation with Edison HTTP 402 Payment Required. The queued
  output path is:
  `projects/P_PUTIDA/deep-research/PSEPK__fatty_acid_biosynthesis__upa00094-deep-research-falcon.md`.
- Validation complete for `acpP` and the module with:

```bash
just validate PSEPK acpP
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/fatty_acid_biosynthesis.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/fatty_acid_biosynthesis.yaml
```

Main UPA00094 conclusions:

- UPA00094 is an ACP-linked support view of the already completed type-II
  fatty-acid-biosynthesis module, not a separate module.
- `acpP` supplies the cytoplasmic phosphopantetheinylated carrier pool used by
  malonyl-ACP formation, acyl-ACP condensation, reduction, dehydration, and
  enoyl-ACP reduction.
- The other UPA00094 members are already represented by acetyl-CoA-carboxylase
  and Fab-enzyme nodes in the existing FAS-II module.

## Batch status: ppu00071 / bacterial_fatty_acid_beta_oxidation

Batch files:

- `projects/P_PUTIDA/batches/ppu00071_bacterial_fatty_acid_beta_oxidation.tsv`
- `projects/P_PUTIDA/batches/ppu00071_bacterial_fatty_acid_beta_oxidation.md`

Status as of 2026-07-06 PDT / 2026-07-07 UTC:

- 22 KEGG `ppu00071` membership candidates extracted from pathway membership.
- 22/22 candidate review folders present.
- 22/22 candidate Asta gene-level retrieval reports present.
- 22/22 candidate review YAMLs curated with no remaining `PENDING` actions.
- 4 Falcon-promoted gap-fill genes, `PP_0368`, `PP_0370`, `PP_0763`, and
  `hbd`/PP_3755, fetched or rechecked, Asta-backed, curated, and validated.
- `def2`/PP_4559 was fetched, Asta-backed, curated, and validated as a
  Falcon-triggered identifier conflict: current UniProt/GOA/PANTHER support
  peptide deformylase, not CoA ligase, so it is not counted as ppu00071
  beta-oxidation coverage.
- The 7 newly curated candidates validate cleanly: `fadE`, `acd`, `PP_2437`,
  `PP_2793`, `PP_3725`, `alkT`, and `PP_5371`. The full 22-gene batch
  validates with only older non-blocking Asta-citation warnings on some
  pre-existing reviews.
- First-pass split: `fadE`, `PP_2437`, and `PP_2793` are beta-oxidation
  acyl-CoA dehydrogenase candidates; `acd` and `PP_3725` are unresolved or
  specialized acyl-CoA dehydrogenase-family paralogs; `alkT` and `PP_5371` are
  alkane/rubredoxin electron-transfer side nodes rather than core spiral
  enzymes.
- Created `modules/bacterial_fatty_acid_beta_oxidation.yaml` as the PSEPK
  bacterial beta-oxidation seed, leaving the existing
  `modules/fatty_acid_beta_oxidation.yaml` as its metazoan mitochondrial
  cross-species module.
- Falcon generic module research complete:
  `modules/bacterial_fatty_acid_beta_oxidation-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_fatty_acid_beta_oxidation__ppu00071-deep-research-falcon.md`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_fatty_acid_beta_oxidation.yaml
uv run python -m ai_gene_review.validation.module_validator modules/bacterial_fatty_acid_beta_oxidation.yaml
```

Main curation conclusions from this batch:

- KT2440 ppu00071 is satisfiable, but the KEGG-derived membership list is both
  incomplete and noisy. `fadD-I`, `fadD-II`, `fadB`, `fadA`/PP_2137, `bktB`,
  `PP_2437`, and the newly promoted `PP_0368`, `PP_0370`, `PP_0763`, and
  `hbd`/PP_3755 provide the strongest first-pass coverage.
- `PP_0368` and `PP_0370` were promoted as primary ACAD candidates from the
  PSEPK Falcon report, but their current UniProt records still name
  3-methylmercaptopropionyl-CoA dehydrogenase/DMSP chemistry. The reviews keep
  this as a substrate-specificity conflict for later expert or biochemical
  follow-up.
- `gcdH`, `frmA`, `adhP`, and `paaF` should not be interpreted as core
  fatty-acid beta-oxidation in this module. Generic thiolases/acetyltransferases
  such as `PP_0582`, `PP_3355`, and `yqeF` are weak or boundary candidates.
- `alkT` and `PP_5371` are alkane/rubredoxin electron-transfer boundary nodes,
  not beta-oxidation spiral enzymes. The generic Falcon report reinforces that
  alkane monooxygenase/rubredoxin chemistry is upstream substrate-feeding
  context.
- The PP_4559 CoA-ligase claim from Falcon conflicts with current source data:
  `def2`/PP_4559 validates as peptide deformylase. This was explicitly reviewed
  so it is tracked as a resolved identifier conflict, not silently accepted.

## Batch status: UPA00191 / bacterial_fatty_acid_beta_oxidation support

Batch files:

- `projects/P_PUTIDA/batches/UPA00191_bacterial_fatty_acid_beta_oxidation.tsv`
- `projects/P_PUTIDA/batches/UPA00191_bacterial_fatty_acid_beta_oxidation.md`

Status as of 2026-07-09 PDT:

- 1 candidate curated: UniPathway `UPA00191` member `rubA`.
- 1/1 candidate review folder present.
- 1/1 candidate Asta gene-level retrieval report present.
- 1/1 review YAML curated with no remaining `PENDING` actions.
- Existing bacterial fatty-acid beta-oxidation module extended with RubA under
  the alkane/rubredoxin electron-transfer boundary node:
  `modules/bacterial_fatty_acid_beta_oxidation.yaml`.
- Existing generic Falcon module research reused:
  `modules/bacterial_fatty_acid_beta_oxidation-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research for UPA00191 was attempted with the real
  taxon-aware command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_fatty_acid_beta_oxidation__upa00191-deep-research-falcon.md`.
- Validation complete for the gene review and the updated module.
- Gene review page rendered for `rubA`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_fatty_acid_beta_oxidation.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/bacterial_fatty_acid_beta_oxidation.yaml
```

Main curation conclusions from this batch:

- PSEPK `UPA00191` is a support view of the alkane/rubredoxin boundary already
  tracked in the bacterial beta-oxidation module.
- `rubA` is a small rubredoxin electron-transfer protein with
  hydrocarbon/alkane oxidation pathway context.
- The review accepts electron transfer activity and alkane catabolic process
  context, while retaining cytoplasm and iron/metal binding as non-core
  supporting features.
- RubA should not be treated as a beta-oxidation spiral enzyme; it is upstream
  hydrocarbon-oxidation boundary context alongside `alkT` and PP_5371.

## Batch status: UPA00659 / bacterial_fatty_acid_beta_oxidation support

Batch files:

- `projects/P_PUTIDA/batches/UPA00659_bacterial_fatty_acid_beta_oxidation.tsv`
- `projects/P_PUTIDA/batches/UPA00659_bacterial_fatty_acid_beta_oxidation.md`

Status as of 2026-07-09 PDT / 2026-07-10 UTC:

- 4 candidates covered: already-curated `fadE`, `fadB`, and
  `fadA__Q88L01`, plus newly curated UniPathway-primary `PP_4030`.
- 4/4 candidate review folders present.
- 4/4 candidate Asta gene-level retrieval reports present.
- 4/4 review YAMLs curated with no remaining `PENDING` actions.
- Existing bacterial fatty-acid beta-oxidation module extended with PP_4030 as
  an auxiliary dienoyl-CoA isomerase candidate:
  `modules/bacterial_fatty_acid_beta_oxidation.yaml`.
- Existing generic Falcon module research reused:
  `modules/bacterial_fatty_acid_beta_oxidation-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research for UPA00659 was attempted with the real
  taxon-aware command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_fatty_acid_beta_oxidation__upa00659-deep-research-falcon.md`.
- Validation complete for the `PP_4030` gene review and the updated module.
- Gene review page rendered for `PP_4030`.
- Module page rendered:
  `pages/modules/bacterial_fatty_acid_beta_oxidation.html`.
- Project batch page rendered:
  `pages/projects/P_PUTIDA/batches/UPA00659_bacterial_fatty_acid_beta_oxidation.html`.

Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_fatty_acid_beta_oxidation.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/bacterial_fatty_acid_beta_oxidation.yaml
```

Main curation conclusions from this batch:

- PSEPK `UPA00659` is a support view of the existing bacterial
  beta-oxidation module, not a separate pathway.
- `fadE`, `fadB`, and `fadA__Q88L01` already satisfy the core
  dehydrogenation, hydration/oxidation, and thiolysis context.
- `PP_4030` is a cytoplasmic enoyl-CoA hydratase/isomerase-family auxiliary
  candidate. The review accepts fatty acid beta-oxidation context and modifies
  broad `isomerase activity` toward proposed replacement
  `delta(3,5)-delta(2,4)-dienoyl-CoA isomerase activity` based on its PANTHER
  subfamily call.
- Substrate specificity remains unresolved and should be tested against
  saturated and unsaturated fatty-acid beta-oxidation intermediates.

## Batch status: ppu00074 / mycolic_acid_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/ppu00074_mycolic_acid_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/ppu00074_mycolic_acid_biosynthesis.md`

Status as of 2026-07-06 PDT / 2026-07-07 UTC:

- 2 KEGG `ppu00074` membership candidates extracted from pathway membership.
- 2/2 candidate review folders present.
- 2/2 candidate Asta gene-level retrieval reports present.
- 2/2 candidate review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral boundary/absence module created:
  `modules/mycolic_acid_biosynthesis.yaml`.
- Falcon generic module research complete:
  `modules/mycolic_acid_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__mycolic-acid-biosynthesis__ppu00074-deep-research-falcon.md`.
- Validation complete for both candidate gene reviews. `PP_1183` intentionally
  validates with a non-blocking warning because the Asta retrieval was not used
  as direct curation evidence.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/mycolic_acid_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/mycolic_acid_biosynthesis.yaml
```

Main curation conclusions from this batch:

- KT2440 does not have a satisfiable mycolic-acid biosynthesis pathway. The
  ppu00074 assignment is a KEGG spillover from shared upstream chemistry, not an
  organism-level pathway.
- `PP_1183` is best reviewed as an EntD-family
  4'-phosphopantetheinyltransferase for siderophore/NRPS carrier-protein
  activation. It should not be counted as a mycolate PptT/Pks13 activation
  step.
- `fabD` is the malonyl-CoA:ACP transacylase for general bacterial FAS-II
  fatty-acid biosynthesis, already covered by the `ppu00061` pass. It should
  not be counted as evidence of mycolate synthesis in a Gram-negative
  Pseudomonas envelope.
- The diagnostic mycolate machinery is absent/not expected in this target
  taxon, including Pks13, FadD32, CmrA, MmpL3, Ag85/Fbp mycolyltransferases,
  KasA/KasB, InhA, MabA, HadABC, and meromycolate-modification enzymes.
- This batch establishes the project convention for KEGG maps that should be
  curated as `not_expected_in_target_taxon` boundary cases rather than as
  ordinary missing-step pathway gaps.

## Batch status: ppu00130 / ubiquinone_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/ppu00130_ubiquinone_terpenoid_quinone_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/ppu00130_ubiquinone_terpenoid_quinone_biosynthesis.md`

Status as of 2026-07-09 PDT / 2026-07-10 UTC:

- 14 KEGG `ppu00130` membership candidates extracted from pathway membership.
- 14/14 KEGG candidate review folders present and curated.
- 14/14 KEGG candidate Asta gene-level retrieval reports present.
- 3 UniPathway/Falcon-promoted accessory genes curated outside the KEGG
  membership batch: `ubiJ`/PP_5012, `ubiB`/PP_5013, and `ubiK`/PP_5235.
- Species-neutral ubiquinone biosynthesis module created and updated:
  `modules/ubiquinone_biosynthesis.yaml`.
- Falcon generic module research complete:
  `modules/ubiquinone_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__ubiquinone_biosynthesis__ppu00130-deep-research-falcon.md`.
- Validation complete for all 14 KEGG candidate reviews, all 3 promoted
  accessory reviews, and the module. Gene-level warnings are limited to expected
  "Asta not cited" notices where Asta served only as identity/context retrieval.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/ubiquinone_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/ubiquinone_biosynthesis.yaml
```

Main curation conclusions from this batch:

- KT2440 satisfies the strict aerobic ubiquinone biosynthesis module after
  adding the accessory factors `ubiJ`, `ubiB`, and `ubiK`.
- The apparent UbiI gap from the Falcon report resolves to a nomenclature issue:
  `visC`/PP_5197 is a UbiH/Coq6-family, PTHR43876:SF7, GO:0019168
  2-polyprenylphenol hydroxylase candidate and should be treated as the
  UbiI-like C5 hydroxylation step pending deeper experimental confirmation.
- `ubiB` was curated as a kinase-like ATP-dependent accessory/regulatory factor.
  Its bare `protein kinase activity` annotation was marked over-specific because
  current evidence does not establish a classical physiological protein-kinase
  substrate.
- KEGG ppu00130 is broader than strict ubiquinone biosynthesis. `hpd`,
  `PP_1218`, `PP_1644`, `PP_2789`, and `PP_3720` are side nodes for
  homogentisate catabolism, thioesterase activity, or quinone redox utilization
  rather than strict UQ biosynthetic steps.
- `ubiE` remains accepted for the UQ C-methyltransferase step; its
  menaquinone-process annotation is retained as over-annotated/pathway-boundary
  context unless a later menaquinone-specific pass establishes a KT2440 route.

## Batch status: UPA00232 / ubiquinone_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/UPA00232_ubiquinone_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/UPA00232_ubiquinone_biosynthesis.md`

Status as of 2026-07-09 PDT / 2026-07-10 UTC:

- 11 UniPathway `UPA00232` membership genes documented: `coq7`, `ubiG`,
  `ubiE`, `ubiJ`, `ubiB`, `visC`, `ubiH`, `ubiD`, `ubiK`, `ubiC`, and `ubiA`.
- 11/11 review folders present.
- 11/11 Asta gene-level retrieval reports present.
- 11/11 review YAMLs curated with no remaining `PENDING` actions.
- The species-neutral ubiquinone biosynthesis module already covers this
  support bucket:
  `modules/ubiquinone_biosynthesis.yaml`.
- Falcon generic module research is already complete from the `ppu00130`
  checkpoint:
  `modules/ubiquinone_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is already complete from the `ppu00130`
  checkpoint:
  `projects/P_PUTIDA/deep-research/PSEPK__ubiquinone_biosynthesis__ppu00130-deep-research-falcon.md`.
- Validation complete for all 11 gene reviews and the module.
- Batch page rendered:
  `pages/projects/P_PUTIDA/batches/UPA00232_ubiquinone_biosynthesis.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/ubiquinone_biosynthesis.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/ubiquinone_biosynthesis.yaml
```

Main curation conclusions from this batch:

- UPA00232 is the strict UniPathway cross-reference for the already-curated
  ubiquinone biosynthesis module, not a separate route from `ppu00130`.
- The three UniPathway-primary genes `ubiJ`, `ubiB`, and `ubiK` are accessory
  factors for efficient bacterial ubiquinone biosynthesis and remain modeled as
  accessory/context nodes, not independent catalytic steps.
- `visC` remains the UbiI-like C5 hydroxylation candidate in this module.
- The existing `ppu00130` Falcon reports explicitly cover the UbiB/UbiJ/UbiK
  accessory context, so no duplicate UPA00232 Falcon run was launched.

## Batch status: ppu00900 / terpenoid_backbone_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/ppu00900_terpenoid_backbone_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/ppu00900_terpenoid_backbone_biosynthesis.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 17 KEGG `ppu00900` membership candidates extracted from pathway membership.
- 17/17 candidate review folders present and curated.
- 17/17 candidate Asta gene-level retrieval reports present.
- Species-neutral bacterial MEP/prenyl-diphosphate module created:
  `modules/terpenoid_backbone_biosynthesis.yaml`.
- Falcon generic module research complete:
  `modules/terpenoid_backbone_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__terpenoid_backbone_biosynthesis__ppu00900-deep-research-falcon.md`.
- Validation complete for all 17 candidate reviews and the module. Gene-level
  warnings are limited to expected "Asta not cited" notices where Asta served
  only as identity/context retrieval.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/terpenoid_backbone_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/terpenoid_backbone_biosynthesis.yaml
```

Main curation conclusions from this batch:

- KT2440 satisfies the strict bacterial MEP/DOXP terpenoid-backbone route with
  `dxs`, `dxr`, `ispD`, `ispE`, `ispF`, `ispG`, and `ispH`.
- Immediate prenyl-diphosphate extension is covered by `ispA` for FPP, `ispB`
  for octaprenyl diphosphate, and `uppS` for undecaprenyl diphosphate.
- KEGG ppu00900 is broader than the strict module. `ubiX` is a UbiD cofactor
  prenyltransferase in ubiquinone biosynthesis, not a core backbone step.
- The thiolase/acetyl-CoA acetyltransferase entries (`PP_0582`,
  `fadA__Q88L84`, `PP_2215`, `PP_3355`, `bktB`, and `yqeF`) are
  mevalonate-like or fatty-acid-metabolism spillovers from the composite KEGG
  map; they do not establish a native KT2440 mevalonate pathway.
- The PSEPK Falcon report recommended adding `idi`/PP_0854, but local UniProt
  metadata and live UniProt REST both identify PP_0854 as `hisS`/histidyl-tRNA
  synthetase, and no UP000000556 IDI/EC 5.3.3.2 entry was found. This was
  recorded as a Falcon caveat rather than promoted into the module.

## Batch status: ppu00906 / carotenoid_biosynthesis_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00906_carotenoid_biosynthesis_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00906_carotenoid_biosynthesis_boundary.md`

Status as of 2026-07-08 PDT / 2026-07-09 UTC:

- 1 candidate curated: the only KEGG `ppu00906` membership gene, `crtZ`.
- 1/1 candidate review folder present.
- 1/1 candidate Asta gene-level retrieval report present.
- 1/1 review YAML curated with no remaining `PENDING` actions.
- New boundary/partial module created and validated:
  `modules/carotenoid_biosynthesis_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/carotenoid_biosynthesis_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__carotenoid_biosynthesis_boundary__ppu00906-deep-research-falcon.md`.
- Validation complete for the `crtZ` review and the module.
- Gene review page rendered for `crtZ`.
- Module page rendered:
  `pages/modules/carotenoid_biosynthesis_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/carotenoid_biosynthesis_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/carotenoid_biosynthesis_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00906` is a one-gene carotenoid boundary/partial pathway rather
  than evidence for a complete carotenoid biosynthetic route.
- `crtZ`/PP_3246 is retained as a predicted beta-carotene 3-hydroxylase with
  xanthophyll biosynthetic process context, based on TreeGrafter/PANTHER and
  UniProt domain/family evidence.
- Broader carotene metabolic process and generic oxidoreductase activity are
  retained as non-core context because the specific hydroxylase term is more
  informative.
- The batch does not establish upstream carotenoid backbone, desaturation, or
  cyclization steps in KT2440. This remains a module-level satisfiability
  question if later non-KEGG candidates are found.
- Validation has one non-blocking Asta-not-referenced warning because Asta did
  not retrieve useful crtZ-specific primary literature.

## Batch status: ppu00907 / pinene_camphor_geraniol_degradation_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00907_pinene_camphor_geraniol_degradation_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00907_pinene_camphor_geraniol_degradation_boundary.md`

Status as of 2026-07-08 UTC:

- 7 candidates curated or rechecked: all KEGG `ppu00907` membership genes.
- 7/7 candidate review folders present.
- 7/7 candidate Asta gene-level retrieval reports present.
- 7/7 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/pinene_camphor_geraniol_degradation_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/pinene_camphor_geraniol_degradation_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__pinene_camphor_geraniol_degradation_boundary__ppu00907-deep-research-falcon.md`.
- Validation complete for all 7 gene reviews and the module.
- Gene review pages rendered for all 7 candidates.
- Module page rendered:
  `pages/modules/pinene_camphor_geraniol_degradation_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/pinene_camphor_geraniol_degradation_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/pinene_camphor_geraniol_degradation_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00907` is a boundary/absence monoterpene-degradation map, not a
  satisfiable pinene, camphor, or geraniol degradation route.
- `PP_3394` and `mvaB` are HMG-CoA lyase-family paralogs that overlap with
  leucine, butanoate, and isoprenoid-side chemistry.
- `fadA__Q88L84`, `fadB`, `fadA__Q88L01`, `PP_2217`, and `paaF` are
  CoA-thioester thiolase, dehydrogenase, hydratase, or isomerase side nodes
  with stronger placements in fatty-acid beta-oxidation, phenylacetate
  degradation, caprolactam, or other CoA-metabolism boundary maps.
- The batch lacks route-defining monoterpene upper-pathway enzymes, so no new
  pinene/camphor/geraniol-specific gene-review edits were made.
- Validation warnings are non-blocking existing first-pass warnings on overlap
  reviews.

## Batch status: ppu00730 / thiamine_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/ppu00730_thiamine_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/ppu00730_thiamine_biosynthesis.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 13 KEGG `ppu00730` membership candidates extracted from pathway membership.
- 13/13 KEGG candidate review folders present and curated.
- 13/13 KEGG candidate Asta gene-level retrieval reports present.
- Promoted context genes curated: `pet`/PP_3185 and `PP_5105`.
- Species-neutral bacterial thiamine diphosphate biosynthesis module created:
  `modules/thiamine_biosynthesis.yaml`.
- Falcon generic module research complete:
  `modules/thiamine_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__thiamine_biosynthesis__ppu00730-deep-research-falcon.md`.
- Validation complete for the 13 KEGG candidates, the 2 promoted context genes,
  and the module. Gene-level warnings are limited to expected "Asta not cited"
  notices where Asta served only as identity/context retrieval.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/thiamine_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/thiamine_biosynthesis.yaml
```

Main curation conclusions from this batch:

- KT2440 satisfies the strict bacterial thiamine diphosphate biosynthesis module
  through `dxs`, `thiC`, `thiD`, `thiO`, `thiG`, `thiE`, and `thiL`.
- `iscS` and `thiI` are genuine shared sulfur-relay support genes but should not
  be treated as dedicated thiamine-only enzymes; `iscS-II` remains ambiguous for
  thiamine-specific participation.
- `PP_3186` and promoted `pet`/PP_3185 are TenA-family aminopyrimidine
  aminohydrolases best treated as thiamine salvage/context rather than strict
  de novo core.
- `adk` and `rsgA` are KEGG thiamine-map side nodes representing general
  nucleotide homeostasis and ribosome biogenesis, not thiamine-specific steps.
- Falcon correctly flagged missing sulfur-relay metadata. Local metadata
  supports `PP_5105` as the ThiS sulfur carrier and it was promoted into the
  module and gene-review set. No unambiguous `thiF` product or symbol was found
  in local PSEPK metadata; PP_0735/`moeB` is a related MoaD adenylyltransferase
  and was not promoted to ThiF without additional evidence.

## Batch status: UPA00060 / thiamine_biosynthesis support

Batch files:

- `projects/P_PUTIDA/batches/UPA00060_thiamine_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/UPA00060_thiamine_biosynthesis.md`

Status as of 2026-07-09 PDT / 2026-07-10 UTC:

- 9 UniPathway `UPA00060` membership candidates extracted from pathway
  membership.
- 9/9 UniPathway candidate review folders present and curated.
- 9/9 UniPathway candidate Asta gene-level retrieval reports present.
- Reused species-neutral thiamine diphosphate biosynthesis module:
  `modules/thiamine_biosynthesis.yaml`.
- Reused Falcon generic module research from the `ppu00730` checkpoint:
  `modules/thiamine_biosynthesis-deep-research-falcon.md`.
- Reused Falcon PSEPK module+pathway research from the `ppu00730` checkpoint:
  `projects/P_PUTIDA/deep-research/PSEPK__thiamine_biosynthesis__ppu00730-deep-research-falcon.md`.
- Validation complete for the 9 UniPathway candidates and the module.
  Gene-level warnings are limited to expected "Asta not cited" notices where
  Asta served only as identity/context retrieval.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/thiamine_biosynthesis.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/thiamine_biosynthesis.yaml
```

Main curation conclusions from this support batch:

- `UPA00060` is covered by the existing thiamine biosynthesis module rather
  than a new duplicate module.
- Eight UPA00060 members are already primary in KEGG `ppu00730`; `pet`/PP_3185
  is the only UniPathway-primary member in the partition.
- `pet`/PP_3185 and PP_3186 are TenA-family aminopyrimidine aminohydrolases
  best retained as thiamine salvage/context. They support thiamine precursor
  recovery and the broader thiamine diphosphate process but are not strict de
  novo core steps.
- No new Falcon run was performed for this duplicate support view; the completed
  thiamine Falcon reports already cover the relevant module boundary.

## Batch status: ppu00740 / riboflavin_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/ppu00740_riboflavin_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/ppu00740_riboflavin_biosynthesis.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 15 KEGG `ppu00740` membership candidates extracted from pathway membership.
  The worklist primary-bucket count is 14 because `ubiX` is primarily assigned
  outside the strict riboflavin module, but it is retained in this batch as
  boundary context.
- 15/15 candidate review folders present.
- 15/15 candidate Asta gene-level retrieval reports present.
- 15/15 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral riboflavin/FMN/FAD biosynthesis module created:
  `modules/riboflavin_biosynthesis.yaml`.
- Falcon generic module research complete:
  `modules/riboflavin_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__riboflavin_biosynthesis__ppu00740-deep-research-falcon.md`.
- Validation complete for all 15 candidate gene reviews and the module. Gene
  warnings are limited to expected "Asta not cited" notices where Asta served
  only as identity/context retrieval, plus non-blocking boundary-role warnings.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/riboflavin_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/riboflavin_biosynthesis.yaml
```

Main curation conclusions from this batch:

- KT2440 satisfies the strict riboflavin, FMN, and FAD biosynthesis module with
  `ribA`, `ribD`, `ribB`, `ribH`, `ribE`, and `ribF`.
- `ribA` is the sole accepted GTP cyclohydrolase II step in this module.
- `ribAB-I`/PP_0516 and `ribAB-II`/PP_3813 are RibBX enzymes: they retain DHBP
  synthase activity but should not be used to satisfy GTP cyclohydrolase II.
  The TreeGrafter GO:0003935 annotations were removed in both gene reviews.
- `ribC` is retained as a duplicate riboflavin synthase candidate with unresolved
  in vivo contribution relative to `ribE`.
- KEGG `ppu00740` is broader than strict riboflavin/FMN/FAD biosynthesis.
  `ssuE`, `msuE`, `bluB`, `ubiX`, `nudF`, and `had` are boundary or side-node
  entries rather than strict module members.

## Batch status: ppu00750 / vitamin_b6_metabolism

Batch files:

- `projects/P_PUTIDA/batches/ppu00750_vitamin_b6_metabolism.tsv`
- `projects/P_PUTIDA/batches/ppu00750_vitamin_b6_metabolism.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 9 KEGG `ppu00750` membership candidates extracted from pathway membership.
- 9/9 candidate review folders present.
- 9/9 candidate Asta gene-level retrieval reports present.
- 9/9 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral vitamin B6/PLP metabolism module created:
  `modules/vitamin_b6_metabolism.yaml`.
- Falcon generic module research complete:
  `modules/vitamin_b6_metabolism-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__vitamin_b6_metabolism__ppu00750-deep-research-falcon.md`.
- Validation complete for all 9 candidate gene reviews and the module. Gene
  warnings are limited to expected "Asta not cited" notices where Asta served
  only as identity/context retrieval, plus the intentional `PP_0662` no-core
  warning because it remains a weak boundary candidate.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/vitamin_b6_metabolism.yaml
uv run python -m ai_gene_review.validation.module_validator modules/vitamin_b6_metabolism.yaml
```

Main curation conclusions from this batch:

- KT2440 satisfies the strict DXP-dependent de novo vitamin B6/PLP route through
  `epd`, `pdxB`, `serC`, `pdxA`, `pdxJ`, and `pdxH`.
- `serC` was promoted from side context to a genuine shared PLP-pathway enzyme:
  its pyridoxine-biosynthesis annotation is now accepted, while its core
  function remains a shared phosphoserine/phosphohydroxythreonine
  aminotransferase role.
- `pdxY` covers pyridoxal salvage phosphorylation. A broader PdxK-like B6
  salvage kinase was not obvious in local first-pass metadata and remains an
  open hole/follow-up rather than a promoted candidate.
- `thrC` and `PP_0662` are threonine synthase/PLP-enzyme boundary context and
  should not satisfy the committed B6 module.
- `dxs` supplies the DXP precursor but is shared with thiamine and MEP
  metabolism, so it is recorded as boundary input rather than duplicated as a
  dedicated vitamin B6 module member.

## Batch status: ppu00760 / nad_biosynthesis_and_nicotinate_metabolism

Batch files:

- `projects/P_PUTIDA/batches/ppu00760_nad_biosynthesis_and_nicotinate_metabolism.tsv`
- `projects/P_PUTIDA/batches/ppu00760_nad_biosynthesis_and_nicotinate_metabolism.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 30 KEGG `ppu00760` membership candidates extracted from pathway membership.
- 30/30 candidate review folders present.
- 30/30 candidate Asta gene-level retrieval reports present.
- 30/30 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral NAD biosynthesis/nicotinate metabolism module created:
  `modules/nad_biosynthesis_and_nicotinate_metabolism.yaml`.
- Falcon generic module research complete:
  `modules/nad_biosynthesis_and_nicotinate_metabolism-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__nad_biosynthesis_and_nicotinate_metabolism__ppu00760-deep-research-falcon.md`.
- Validation complete for all 30 candidate gene reviews and the module. Gene
  warnings are limited to expected "Asta not cited" notices where Asta served
  only as identity/context retrieval, plus the intentional `PP_3103` no-core
  warning because it remains candidate-uncertain.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/nad_biosynthesis_and_nicotinate_metabolism.yaml
uv run python -m ai_gene_review.validation.module_validator modules/nad_biosynthesis_and_nicotinate_metabolism.yaml
```

Main curation conclusions from this batch:

- KT2440 satisfies de novo NAD+ biosynthesis from L-aspartate through `nadB`,
  `nadA`, `nadC`, `nadD`, and `nadE`. The gene-level review corrected `nadE`
  away from the glutamine-hydrolyzing NAD synthase/glutaminase IEAs to the
  NH3-dependent NAD+ synthase activity supported by UniProt.
- Nicotinate/NMN salvage is covered by `pncB` and `pncC`, but a canonical PncA
  nicotinamidase candidate was not identified in the ppu00760 set and remains
  an explicit salvage gap.
- NADP+ formation/redox balancing is covered by `nadK`, soluble `sthA`, and the
  split membrane Pnt transhydrogenase genes `pntAA`, `pntB`, and `pntAB`.
- Aerobic nicotinate catabolism is covered by the `nic` cluster: `nicA`,
  `nicB`, `nicC`, `nicX`, `nicD`, `nicF`, and `maiA`/NicE.
- `davD`, `sad-I`, `sad-II`, `gabD-II`, `ushA`, `surE`, `PP_2531`, `mazG`,
  `nudC`, and `cobB__Q88BY5` are boundary-only KEGG side nodes; they use
  NAD(P) cofactors, act on general nucleotides, or consume NAD+ but do not
  satisfy core NAD biosynthesis/salvage/nicotinate-catabolism steps.
- `PP_3103` remains candidate-uncertain: UniProt calls it uncharacterized with
  Ntox46/Tre1-like/DUF6861 domains, and no current evidence ties it directly to
  NAD/nicotinate metabolism.

## Batch status: UPA01010 / nad_biosynthesis_and_nicotinate_metabolism support

Batch files:

- `projects/P_PUTIDA/batches/UPA01010_nad_biosynthesis_and_nicotinate_metabolism.tsv`
- `projects/P_PUTIDA/batches/UPA01010_nad_biosynthesis_and_nicotinate_metabolism.md`

Status as of 2026-07-09 PDT / 2026-07-10 UTC:

- 9 UniPathway `UPA01010` membership candidates extracted from pathway
  membership.
- 9/9 UniPathway candidate review folders present and curated.
- 9/9 UniPathway candidate Asta gene-level retrieval reports present. This pass
  added missing Asta retrieval reports for `nicR` and `nicS`.
- Reused species-neutral NAD biosynthesis/nicotinate metabolism module:
  `modules/nad_biosynthesis_and_nicotinate_metabolism.yaml`.
- Reused Falcon generic module research from the `ppu00760` checkpoint:
  `modules/nad_biosynthesis_and_nicotinate_metabolism-deep-research-falcon.md`.
- Reused Falcon PSEPK module+pathway research from the `ppu00760` checkpoint:
  `projects/P_PUTIDA/deep-research/PSEPK__nad_biosynthesis_and_nicotinate_metabolism__ppu00760-deep-research-falcon.md`.
- Validation complete for the 9 UniPathway candidates and the module.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/nad_biosynthesis_and_nicotinate_metabolism.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/nad_biosynthesis_and_nicotinate_metabolism.yaml
```

Main curation conclusions from this support batch:

- `UPA01010` is covered by the existing NAD/nicotinate metabolism module rather
  than a new duplicate module.
- Seven UPA01010 members are the catalytic aerobic nicotinate-catabolism route
  already primary in KEGG `ppu00760`: `nicA`, `nicB`, `nicC`, `nicX`, `nicD`,
  `nicF`, and `maiA`/NicE.
- `nicR` and `nicS` are the UniPathway-primary members in the partition. They
  are adjacent transcriptional-regulator context for the nicotinate-catabolism
  cluster, not catalytic pathway steps.
- No new Falcon run was performed for this duplicate support view; the completed
  NAD/nicotinate Falcon reports already cover the relevant Nic-cluster boundary.

## Batch status: ppu00770 / pantothenate_and_coa_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/ppu00770_pantothenate_and_coa_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/ppu00770_pantothenate_and_coa_biosynthesis.md`
- `projects/P_PUTIDA/batches/UPA00028_pantothenate_and_coa_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/UPA00028_pantothenate_and_coa_biosynthesis.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 24 KEGG `ppu00770` membership candidates extracted from pathway membership.
- UniPathway `UPA00028` adds the pantothenate-biosynthesis subset and the
  UniPathway-only candidate `PP_4452`, for 25 distinct reviewed genes across the
  combined checkpoint.
- 25/25 candidate review folders present.
- 25/25 candidate Asta gene-level retrieval reports present.
- 25/25 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral pantothenate and CoA biosynthesis module created:
  `modules/pantothenate_and_coa_biosynthesis.yaml`.
- Falcon generic module research complete:
  `modules/pantothenate_and_coa_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__pantothenate_and_coa_biosynthesis__ppu00770-deep-research-falcon.md`.
- Validation complete for all 25 candidate gene reviews and the module. Gene
  warnings are limited to expected "Asta not cited" notices where Asta served
  only as identity/context retrieval, plus intentional no-core warnings for
  `PP_2325`, `PP_2998`, and `PP_4452` because these ketopantoate reductase
  paralog calls remain candidate-uncertain.
- Gene review pages rendered for all 25 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/pantothenate_and_coa_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/pantothenate_and_coa_biosynthesis.yaml
```

Main curation conclusions from this batch:

- KT2440 satisfies the strict CoA biosynthesis route from pantothenate through
  `coaX`, `dfp`/CoaBC, `coaD`, and `coaE`. Falcon flagged `coaX`/PP_0438 as the
  strongest species-linked core step because KT2440 PpcoaA has heterologous
  expression evidence.
- Pantothenate assembly is represented by `panB` and `panC`, but the
  physiological behavior is not fully settled: Falcon recovered a reported
  non-auxotrophic `panC` mutant phenotype that suggests salvage, redundancy, or
  medium/context effects.
- The ketopantoate reductase step is candidate-uncertain. `panE` is retained as
  the expected primary candidate, while `PP_2325`, `PP_2998`, and
  UniPathway-only `PP_4452` are no longer treated as core functions on
  electronic annotation alone.
- KT2440 lacks a canonical PanD aspartate decarboxylase in this pathway set, so
  beta-alanine supply is represented as species-specific precursor context via
  pyrimidine reductive catabolism genes `pydA`/`pydX`, `pydB`, `hyuC`, and
  related beta-ureidopropionase context.
- Branched-chain amino-acid enzymes `PP_1157`, `PP_1394`, `ilvH`, `ilvI`,
  `ilvC`, `ilvD`, and `ilvE` supply or interconvert precursor metabolites but
  are not committed pantothenate/CoA steps.
- `PP_0922`, `PP_1183`, and `mazG` are ACP/cofactor or nucleotide boundary nodes
  and should not satisfy strict pantothenate-to-CoA pathway coverage.

## Batch status: ppu00190 / oxphos

Batch files:

- `projects/P_PUTIDA/batches/ppu00190_oxphos.tsv`
- `projects/P_PUTIDA/batches/ppu00190_oxphos.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 54 KEGG `ppu00190` membership candidates extracted from pathway membership;
  44 are primary `ppu00190` bucket genes, with the rest pulled in by overlapping
  heme, phosphate/polyphosphate, central-carbon, and neighboring energy maps.
- 54/54 candidate review folders present.
- 54/54 candidate Asta gene-level retrieval reports present.
- 54/54 review YAMLs curated with no remaining `PENDING` actions.
- Existing species-neutral OXPHOS module reused and validated:
  `modules/oxphos.yaml`.
- Falcon generic module research complete:
  `modules/oxphos-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding. The attempted
  `oxphos` / `ppu00190` / PSEPK run failed before report generation with
  Edison HTTP 402 Payment Required, so no taxon-specific Falcon report was
  created.
- Validation complete for all 54 candidate gene reviews and the module. Gene
  warnings are limited to expected first-pass Asta context notices and
  warnings that core-function context terms, especially complex/location/process
  terms, are not separately accepted as existing annotations.
- Gene review pages rendered for all 54 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/oxphos.yaml
uv run python -m ai_gene_review.validation.module_validator modules/oxphos.yaml
```

Main curation conclusions from this batch:

- KT2440 encodes a broad aerobic respiratory-chain repertoire: proton-pumping
  Complex I (`nuoA`-`nuoN`), type-II NADH dehydrogenase `ndh`, succinate
  dehydrogenase, cytochrome bc1 (`petA`/`petB`/`petC`), aa3 cytochrome c
  oxidase, bo3 ubiquinol oxidase, duplicated cbb3 cytochrome c oxidases,
  cyanide-insensitive oxidase (`cioA`/`cioB`), and the F1Fo ATP synthase operon.
- The bo3 reviews correct donor specificity: GOA's generic
  cytochrome-c oxidase activity calls are modified to cytochrome bo3 ubiquinol
  oxidase activity where the local UniProt/GOA context supports the bo3 branch.
- Complex-I subunit reviews use NADH dehydrogenase (ubiquinone) activity as the
  core complex-level contribution rather than leaving only broad NADH
  dehydrogenase or oxidoreductase terms.
- ATP synthase and respiratory complex subunits are modeled in `core_functions`
  with `contributes_to_molecular_function`, reflecting the module design that
  the complex, not each isolated subunit, enables the emergent activity.
- `ccoQ-I` and `ccoQ-II` have no GOA annotations, but UniProt/module context
  supports recording them as cbb3-type cytochrome c oxidase subunits in this
  first pass.
- KEGG `ppu00190` also includes boundary nodes such as `ppa`, `ppk`, `ppkB`,
  heme O/heme A context genes (`cyoE1`, `cyoE2`, `PP_0105`), and other side
  proteins. These are retained as adjacent respiratory or phosphate/heme context
  and should not be treated as strict OXPHOS catalytic steps without additional
  pathway-specific evidence.

## Batch status: ppu00790 / folate_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/ppu00790_folate_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/ppu00790_folate_biosynthesis.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 32 KEGG `ppu00790` membership candidates extracted from pathway membership;
  19 are primary `ppu00790` bucket genes, with the rest pulled in by overlapping
  riboflavin, molybdenum-cofactor, one-carbon, phenylalanine-hydroxylase, and
  neighboring cofactor maps.
- 32/32 candidate review folders present.
- 32/32 candidate Asta gene-level retrieval reports present.
- 32/32 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral folate biosynthesis module created and validated:
  `modules/folate_biosynthesis.yaml`.
- Falcon generic module research is still outstanding. The attempted
  `folate_biosynthesis` run failed before report generation with Edison HTTP
  402 Payment Required, so no `modules/folate_biosynthesis-deep-research-falcon.md`
  report was created.
- Falcon PSEPK module+pathway research is still outstanding. The attempted
  `folate_biosynthesis` / `ppu00790` / PSEPK run failed before report
  generation with Edison HTTP 402 Payment Required, so no taxon-specific Falcon
  report was created.
- Validation complete for all 32 candidate gene reviews and the module. Gene
  warnings are limited to expected first-pass Asta context notices, context-term
  warnings where a core-function location/process is not represented as an
  accepted existing annotation, and intentional no-core warnings for the
  unresolved MobA-like proteins `PP_2483` and `PP_4230`.
- Gene review pages rendered for all 32 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/folate_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/folate_biosynthesis.yaml
```

Main curation conclusions from this batch:

- KT2440 has a satisfiable strict folate route covering the pterin branch
  (`folE1`, `folE2__Q88JY1`, existing `folE2`/Q88HM9, `folB`, `folK`, and
  PP_0393), pABA branch (`pabB`, `pabC`), condensation/polyglutamylation
  (`folP`, `folC`), and reduction (`folA`). PP_0393 remains an HPPK paralog
  candidate whose division of labor with `folK` is not resolved.
- The two FolE families are separated explicitly: `folE1` and
  `folE2__Q88JY1` are canonical-family GTP cyclohydrolase I paralogs, while
  existing `folE2`/Q88HM9 is the GCYH-IB/FolE2 non-orthologous replacement.
  Their branch-specific contributions to folate, queuosine, and other pterin
  products remain an expert question.
- KEGG `ppu00790` includes queuosine precursor genes (`queD`, `queE`, `queC`,
  `queF`) because of shared pterin/deazapurine chemistry. These are curated as
  tRNA queuosine biosynthesis side-branch enzymes, not strict tetrahydrofolate
  steps.
- The molybdenum-cofactor side of the map is represented by `moaA`, `moaB-I`,
  `moaB-II`, `moaC`, `moaE`, `moeA`, `mobA`, PP_1969, and PP_2482. The MoaA-like
  paralogs are retained as MoCo/pyranopterin candidates, with paralog-specific
  physiological roles unresolved.
- `folM` is retained as an SDR pterin reductase with dihydromonapterin
  reductase and predicted dihydrofolate reductase activity, but `folA` is still
  the canonical strict folate-tail DHFR.
- `PP_2483` and `PP_4230` remain unresolved MobA-like NTP transferase-domain
  proteins. Their broad nucleotidyltransferase GOA annotations are kept as
  non-core until a substrate or product is known.
- `pabB` now removes the electronic `L-tryptophan biosynthetic process`
  transfer, which appears to be an anthranilate-synthase-family spillover; the
  supported role here is aminodeoxychorismate synthase in pABA/folate
  biosynthesis.

## Batch status: UPA00392 / queuosine_biosynthesis_boundary

Batch files:

- `projects/P_PUTIDA/batches/UPA00392_queuosine_biosynthesis_boundary.tsv`
- `projects/P_PUTIDA/batches/UPA00392_queuosine_biosynthesis_boundary.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 4 UniPathway `UPA00392` membership candidates extracted from pathway
  membership; `queA`, `tgt`, and `queG` are primary UPA00392 bucket genes, while
  `queF` is side context from the KEGG `ppu00790` primary partition.
- 4/4 candidate review folders present.
- 4/4 candidate Asta gene-level retrieval reports present.
- 4/4 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral tRNA queuosine biosynthesis boundary module created and
  validated: `modules/queuosine_biosynthesis_boundary.yaml`.
- Falcon generic module research is still outstanding. The attempted
  `queuosine_biosynthesis_boundary` run failed before report generation with
  Edison HTTP 402 Payment Required, so no
  `modules/queuosine_biosynthesis_boundary-deep-research-falcon.md` report was
  created.
- Falcon PSEPK module+pathway research is still outstanding. The attempted
  `queuosine_biosynthesis_boundary` / `UPA00392` / PSEPK run failed before
  report generation with Edison HTTP 402 Payment Required, so no taxon-specific
  Falcon report was created.
- Validation complete for all 4 candidate gene reviews and the module.
- Gene review pages rendered for all 4 candidates, and the module/project pages
  were regenerated.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/queuosine_biosynthesis_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/queuosine_biosynthesis_boundary.yaml
```

Main curation conclusions from this batch:

- KT2440 has a compact, satisfiable tRNA-queuosine route: `queF` reduces preQ0
  to preQ1, `tgt` inserts preQ1 into target tRNAs at wobble position 34, `queA`
  forms epoxyqueuosine-modified tRNA, and `queG` reduces that intermediate to
  queuosine-modified tRNA.
- `queF` is cross-bucket side context from `ppu00790` because KEGG folate
  biosynthesis includes shared pterin/deazaguanine chemistry. For curation it
  belongs in the tRNA queuosine module, not as a strict tetrahydrofolate enzyme.
- Generic parent activities such as `transferase activity`, `isomerase
  activity`, and broad `oxidoreductase activity` are marked as over-annotated
  where a specific QueA or QueG activity is present. QueG iron-sulfur cluster
  binding is retained as non-core cofactor context.

## Batch status: ppu00670 / one_carbon_by_folate

Batch files:

- `projects/P_PUTIDA/batches/ppu00670_one_carbon_by_folate.tsv`
- `projects/P_PUTIDA/batches/ppu00670_one_carbon_by_folate.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 31 KEGG `ppu00670` membership candidates extracted from pathway membership;
  14 are primary `ppu00670` bucket genes, with the rest pulled in by overlapping
  folate, lipoic-acid/glycine-cleavage, methionine-cycle, nucleotide, and
  betaine/osmoprotectant maps.
- 31/31 candidate review folders present.
- 31/31 candidate Asta gene-level retrieval reports present. Initial Asta
  retrievals for PP_0708, `gcvT-I`, `gcvP1`, `purN`, and `betA` failed with
  transient service/network errors, then succeeded on retry.
- 31/31 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral one-carbon-by-folate module created and validated:
  `modules/one_carbon_by_folate.yaml`.
- Falcon generic module research is still outstanding:
  `modules/one_carbon_by_folate-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__one_carbon_by_folate__ppu00670-deep-research-falcon.md`.
- Validation complete for all 31 candidate gene reviews and the module. Gene
  warnings are limited to expected first-pass Asta context notices, context-term
  warnings where a core-function location is not represented as an accepted
  existing annotation, and the intentional no-core warning for PP_0708.
- Gene review pages rendered for all 31 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/one_carbon_by_folate.yaml
uv run python -m ai_gene_review.validation.module_validator modules/one_carbon_by_folate.yaml
```

Main curation conclusions from this batch:

- Strict one-carbon folate carrier interconversion is covered by `folD1`,
  `folD2`, `metF`, PP_4638, and `fau`.
- Folate-dependent consumers are split by endpoint: purine biosynthesis
  (`purN`, `purH`), thymidylate biosynthesis (`thyA`), methionine synthase
  context (`metH`), and folate/pterin reductase context (`folA`, `folM`).
- Two glycine-cleavage clusters are represented:
  `gcvT-I`/`gcvP1`/`gcvH1` and `gcvT`/`gcvP2`/`gcvH2`. The H proteins are curated
  as glycine cleavage complex lipoyl-carrier components rather than assigned an
  independent catalytic molecular function.
- `purU-I`, `purU-II`, and `purU-III` are accepted as
  formyltetrahydrofolate deformylase paralogs, but their electronic direct
  purine-biosynthesis process annotations are marked as over-annotated because
  the direct transformylase chemistry belongs to PurN/PurH.
- `betA` and `betB` are curated as betaine/choline osmoprotectant boundary
  enzymes, not strict folate-carrier steps. PP_0708 remains unresolved: UniProt
  names it as a betaine-aldehyde dehydrogenase, but GOA currently supplies only
  broad oxidoreductase activity, so no core function was assigned in this pass.
- `lpd`, `lpdG`, `lpdV`, `metK`, `ahcY`, and PP_4594 remain relevant pathway
  neighbors from lipoamide and methionine-cycle chemistry rather than strict
  one-carbon-by-folate module steps.

## Batch status: ppu00910 / nitrogen_cycle

Batch files:

- `projects/P_PUTIDA/batches/ppu00910_nitrogen_cycle.tsv`
- `projects/P_PUTIDA/batches/ppu00910_nitrogen_cycle.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 20 KEGG `ppu00910` membership candidates extracted from pathway membership;
  19 are primary `ppu00910` bucket genes, with `gdhB` pulled in from alanine,
  aspartate, and glutamate metabolism.
- 20/20 candidate review folders present.
- 20/20 candidate Asta gene-level retrieval reports present. PP_3148 failed
  once with a transient Asta network error and succeeded on retry.
- 20/20 review YAMLs curated with no remaining `PENDING` actions.
- Existing species-neutral nitrogen-cycle module reused and validated:
  `modules/nitrogen_cycle.yaml`.
- Falcon generic module research is still outstanding:
  `modules/nitrogen_cycle-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__nitrogen_cycle__ppu00910-deep-research-falcon.md`.
- Validation complete for all 20 candidate gene reviews and the module. Gene
  warnings are limited to expected first-pass Asta context notices and the
  intentional no-core warning for PP_3392.
- Gene review pages rendered for all 20 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/nitrogen_cycle.yaml
uv run python -m ai_gene_review.validation.module_validator modules/nitrogen_cycle.yaml
```

Main curation conclusions from this batch:

- KT2440 ppu00910 should be treated as an assimilation and boundary-chemistry
  nitrogen-metabolism map, not as evidence for a complete nitrogen-cycle redox
  repertoire.
- The strict assimilatory nitrate/nitrite branch is represented by `nasA`,
  `nirB`, and `nirD`. `nirD` is modeled as the Rieske/2Fe-2S subunit
  contributing to the NirBD nitrite reductase activity rather than as an
  independently complete catalytic enzyme.
- Central ammonia assimilation is represented by `glnA`, `gltB`, and `gltD`,
  with `gdhA` and `gdhB` marking NADP- and NAD-specific glutamate
  dehydrogenase routes. The `gdhB` electronic aspartate aminotransferase call is
  removed as inconsistent with the NAD-specific glutamate dehydrogenase identity.
- `puuA-I`, `puuA-II`, `spuB`, and `spuI` are curated as polyamine-catabolic
  GS-fold enzymes. Glutamine synthetase and L-glutamine biosynthesis transfers
  are removed where the product/EC supports glutamate-putrescine or
  glutamylpolyamine ligase chemistry.
- `cynT`, PP_0430, `yrpB`, and PP_3392 are carbonic-anhydrase/nitronate
  boundary nodes in KEGG ppu00910. PP_3392 remains unresolved because it has no
  GOA annotations and only broad gamma carbonic-anhydrase-like/hexapeptide-repeat
  evidence.

## Batch status: ppu00920 / sulfur_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00920_sulfur_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00920_sulfur_metabolism_boundary.md`

Status as of 2026-07-08 PDT / 2026-07-09 UTC:

- 54 KEGG `ppu00920` membership candidates extracted from pathway membership.
- 54/54 candidate review folders present. The first pass fetched 36 missing
  review folders and reused 18 already-curated overlap reviews.
- 54/54 candidate Asta gene-level retrieval reports present. `PP_0208`,
  `ssuB`, and `PP_2048` failed once with transient Asta internal-server errors
  and succeeded on retry.
- 54/54 review YAMLs curated with no remaining `PENDING` actions. The pass
  resolved 31 pending reviews plus five no-GOA reviews while leaving 18
  already-curated overlap reviews unchanged.
- Species-neutral sulfur boundary module created and validated:
  `modules/sulfur_metabolism_boundary.yaml`.
- 2026-07-08 extension: PP_0225-PP_0227 (`sctC`, `sctS`, `fliY`) from the
  partitioned `ppu02010` ABC-transporter map were added as a cystine/
  sulfur-compound import part in this module. All three transporter gene reviews
  validate warning-free.
- Falcon generic module research is still outstanding:
  `modules/sulfur_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__sulfur_metabolism_boundary__ppu00920-deep-research-falcon.md`.
- Validation complete for all 54 candidate gene reviews and the module. Gene
  warnings, if rerun through aggregate validation, are expected first-pass Asta
  context notices on Asta-only reviews.
- Gene review pages rendered for all 54 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/sulfur_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/sulfur_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- KT2440 ppu00920 should be treated as a broad sulfur-metabolism boundary
  bucket, not as a single satisfiable route.
- The strongest subroutes are sulfate/thiosulfate import by Sbp/CysAWU
  components and assimilatory sulfate reduction/cysteine supply through CysD,
  CysNC, CysH, PP_0860, CysI, CysQ, CysK, and serine acetyltransferase paralogs.
- Taurine and alkanesulfonate acquisition splits into transporter components
  (`tauA`, `tauB`, `tauC`, `tauB-I`, `ssuA`, `ssuB`, `ssuC`, PP_0170/0171/0172,
  PP_0207/0208, and several SsuA/TauA-like binding proteins) plus
  desulfonation chemistry (`ssuD`, `ssuE`, PP_2765, PP_3219, and `msuE`).
- The later PP_0225-PP_0227 extension records a separate cystine/sulfur-compound
  ABC import system. `fliY` is treated as a periplasmic cystine-binding protein
  here, not as flagellar or ion-channel machinery.
- PP_0053, PP_2677, PP_3822, GlpE/RhdA/SseA, MetB/MetZ/MetXS, and
  PP_2795/PP_3553/PP_2048/PP_3554 are sulfur-redox, sulfurtransferase,
  amino-acid, and organosulfur CoA/AMP side nodes. They should not be collapsed
  into a single complete sulfur pathway without additional evidence.
- PP_0208 is deliberately left `UNDECIDED` for alkanesulfonate transport because
  UniProt names it as a nitrate ABC permease while GOA places it in
  alkanesulfonate transport; this needs targeted transporter evidence.

## Batch status: ppu00930 / caprolactam_degradation_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00930_caprolactam_degradation_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00930_caprolactam_degradation_boundary.md`

Status as of 2026-07-08 PDT / 2026-07-09 UTC:

- 3 KEGG `ppu00930` membership candidates extracted from pathway membership:
  `fadB`, PP_2217, and `paaF`.
- 3/3 candidate review folders present.
- 3/3 candidate Asta gene-level retrieval reports present.
- 3/3 review YAMLs already curated with no remaining `PENDING` actions.
- Species-neutral caprolactam-degradation boundary module created and validated:
  `modules/caprolactam_degradation_boundary.yaml`.
- No Falcon module-level synthesis was run for this checkpoint; Falcon remains
  queued for later module-level passes.
- Validation complete for all 3 candidate gene reviews and the module.
- Gene review pages rendered for all 3 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/caprolactam_degradation_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/caprolactam_degradation_boundary.yaml
```

Main curation conclusions from this batch:

- KT2440 ppu00930 is a boundary/absence caprolactam-degradation bucket, not a
  complete caprolactam degradation route.
- The mapped members are shared CoA-thioester enzymes: `fadB` from fatty-acid
  beta-oxidation, PP_2217 as an enoyl-CoA hydratase-family side node, and `paaF`
  from phenylacetate/CoA-thioester metabolism.
- The batch lacks caprolactam lactamase, 6-aminohexanoate conversion, or other
  route-defining caprolactam upper-pathway genes.

## Batch status: ppu00946 / flavonoid_degradation_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00946_flavonoid_degradation_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00946_flavonoid_degradation_boundary.md`

Status as of 2026-07-08 PDT / 2026-07-09 UTC:

- 7 KEGG `ppu00946` membership candidates extracted from pathway membership.
  `bglX` is a non-primary overlap from the plant-secondary-metabolite bucket;
  PP_3195, PP_3197, PP_3198, PP_3204, PP_3205, and PP_3206 are primary
  `ppu00946` members.
- 7/7 candidate review folders present. The first pass fetched six missing
  review folders and reused already-curated `bglX`.
- 7/7 candidate Asta gene-level retrieval reports present. PP_3198 failed once
  with a transient Asta internal-server error and succeeded on retry.
- 7/7 review YAMLs curated with no remaining `PENDING` actions. The pass
  resolved three pending reviews plus three no-GOA reviews.
- Species-neutral flavonoid-degradation boundary module created and validated:
  `modules/flavonoid_degradation_boundary.yaml`.
- No Falcon module-level synthesis was run for this checkpoint; Falcon remains
  queued for later module-level passes.
- Validation complete for all 7 candidate gene reviews and the module.
- Gene review pages rendered for all 7 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/flavonoid_degradation_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/flavonoid_degradation_boundary.yaml
```

Main curation conclusions from this batch:

- KT2440 ppu00946 is an unresolved aromatic/flavonoid boundary cluster rather
  than a complete flavonoid-degradation route.
- `bglX` is broad periplasmic beta-glucosidase/glycoside context, not
  flavonoid-specific evidence by itself.
- PP_3195-PP_3206 contain sparse hydrolase, redox, cupin, fumarylacetoacetase,
  glyoxalase/VOC, and NAD-dependent epimerase/dehydratase family signals. GOA
  support is too generic to assign substrate-specific flavonoid chemistry.
- The module should be revisited only if substrate-specific enzymology, genetics,
  or pathway-neighborhood evidence connects this cluster to flavonoid-derived
  compounds.

## Batch status: ppu00970 / aminoacyl_trna_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/ppu00970_aminoacyl_trna_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/ppu00970_aminoacyl_trna_biosynthesis.md`

Status as of 2026-07-08 PDT / 2026-07-09 UTC:

- 27 KEGG `ppu00970` membership candidates extracted from pathway membership.
  The batch includes canonical aminoacyl-tRNA synthetases, GatCAB
  transamidation, `fmt`, `selA`, and unresolved PP_0613 amidase-family context.
- 27/27 candidate review folders present. The first pass fetched 23 missing
  review folders and reused existing `fmt`, `selA`, `metG`, and `gltX`.
- 27/27 candidate Asta gene-level retrieval reports present. `thrS` failed once
  with a transient Asta network error and succeeded on retry.
- 27/27 review YAMLs curated with no remaining `PENDING` actions. The pass
  resolved 23 pending reviews while retaining the four already-curated overlaps.
- Species-neutral aminoacyl-tRNA biosynthesis module created and validated:
  `modules/aminoacyl_trna_biosynthesis.yaml`.
- No Falcon module-level synthesis was run for this checkpoint; Falcon remains
  queued for later module-level passes.
- Validation complete for all 27 candidate gene reviews and the module.
- Gene review pages rendered for all 27 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/aminoacyl_trna_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/aminoacyl_trna_biosynthesis.yaml
```

Main curation conclusions from this batch:

- KT2440 has the expected complete core aminoacyl-tRNA charging set, including
  heteromeric GlyRS (`glyQ`/`glyS`) and PheRS (`pheS`/`pheT`), direct
  single-chain synthetases for the remaining protein amino acids, and
  aminoacyl-tRNA editing/deacylase annotations on AlaRS, IleRS, LeuRS, ProRS,
  and ValRS.
- GatCAB (`gatA`, `gatB`, `gatC`) is modeled as tRNA-dependent indirect
  Gln/Asn-tRNA transamidation; `aspS` is non-discriminating and supplies
  Asp-tRNA(Asn) substrate context.
- `fmt` is translation-initiation side chemistry for initiator
  methionyl-tRNA formylation; `selA`/`serS` are selenocysteine-tRNA side
  chemistry; PP_0613 is an unresolved amidase-family side node rather than a
  core aminoacyl-tRNA biosynthesis gene.
- Clear electronic specificity errors were removed where contradicted by
  UniProt/GOA context: glyS was not retained as arginine-tRNA ligase/arginyl-tRNA
  aminoacylation, and glnS was not retained as glutamyl-tRNA aminoacylation.

## Batch status: ppu00975 / siderophore_biosynthesis_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00975_siderophore_biosynthesis_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00975_siderophore_biosynthesis_boundary.md`

Status as of 2026-07-08 PDT / 2026-07-09 UTC:

- 3 KEGG `ppu00975` membership candidates extracted from pathway membership:
  `PP_2800`, `pvdH`, and `pvdY`.
- 3/3 candidate review folders present. The first pass fetched missing `pvdY`
  and reused existing `PP_2800` and `pvdH`.
- 3/3 candidate Asta gene-level retrieval reports present.
- 3/3 review YAMLs curated with no remaining `PENDING` actions. `pvdY` was
  newly curated, and PP_2800 was lightly updated to wire Asta evidence into the
  existing first-pass review.
- Species-neutral siderophore-biosynthesis boundary module created and
  validated: `modules/siderophore_biosynthesis_boundary.yaml`.
- No Falcon module-level synthesis was run for this checkpoint; Falcon remains
  queued for later module-level passes.
- Validation complete for all 3 candidate gene reviews and the module.
- Gene review pages rendered for all 3 candidates.
- Module page rendered:
  `pages/modules/siderophore_biosynthesis_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/siderophore_biosynthesis_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/siderophore_biosynthesis_boundary.yaml
```

Main curation conclusions from this batch:

- The KEGG `ppu00975` membership is best treated as a boundary/partial
  siderophore module, not as a complete siderophore or pyoverdine biosynthesis
  pathway.
- `pvdH` is the strongest pathway-defining member in this batch, supplying
  L-2,4-diaminobutyrate aminotransferase chemistry for pyoverdine precursor
  biosynthesis.
- PP_2800 is a predicted related diaminobutyrate aminotransferase-family enzyme,
  but its physiological substrate and route placement remain unresolved.
- `pvdY` is a predicted hydroxyproline acetylase/MbtK-IucB-like
  N-acyltransferase. Its current first-pass review accepts general siderophore
  biosynthesis support while avoiding a stronger pyoverdine-specific claim
  without direct substrate evidence.
- The module explicitly records the absence of the full NRPS assembly,
  maturation, and export machinery from this KEGG bucket.

## Batch status: ppu00996 / alkaloid_biosynthesis_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00996_alkaloid_biosynthesis_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00996_alkaloid_biosynthesis_boundary.md`

Status as of 2026-07-08 PDT / 2026-07-09 UTC:

- 1 KEGG `ppu00996` membership candidate extracted from pathway membership:
  PP_3358.
- 1/1 candidate review folder present.
- 1/1 candidate Asta gene-level retrieval report present.
- 1/1 review YAML curated with no remaining `PENDING` actions. The checkpoint
  added Asta evidence wiring to the existing PP_3358 first-pass review.
- Species-neutral alkaloid-biosynthesis boundary module created and validated:
  `modules/alkaloid_biosynthesis_boundary.yaml`.
- No Falcon module-level synthesis was run for this checkpoint; Falcon remains
  queued for later module-level passes.
- Validation complete for the PP_3358 gene review and the module.
- Gene review page rendered for PP_3358.
- Module page rendered:
  `pages/modules/alkaloid_biosynthesis_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/alkaloid_biosynthesis_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/alkaloid_biosynthesis_boundary.yaml
```

Main curation conclusions from this batch:

- The KEGG `ppu00996` membership is a one-gene boundary/absence case and should
  not be read as evidence for complete alkaloid biosynthesis in KT2440.
- PP_3358 is best kept as feruloyl-CoA hydratase/lyase activity in
  hydroxycinnamate/vanillin side metabolism.
- The existing PP_3358 review already removes the unsupported isoprenoid
  catabolic process annotation and proposes the specific
  feruloyl-CoA hydratase/lyase term for the broad catalytic annotation.
- PP_3358 also appears in the ppu00627 aminobenzoate-degradation boundary batch;
  ppu00996 should reuse that aromatic side-funnel interpretation rather than
  create an alkaloid process assignment.

## Batch status: ppu00999 / plant_secondary_metabolite_biosynthesis_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00999_plant_secondary_metabolite_biosynthesis_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00999_plant_secondary_metabolite_biosynthesis_boundary.md`

Status as of 2026-07-08 PDT / 2026-07-09 UTC:

- 5 KEGG `ppu00999` membership candidates extracted from pathway membership:
  `aroE__Q88RQ5`, `bglX`, `aroE__Q88IJ7`, PP_3768, and `metK`.
- 5/5 candidate review folders present.
- 5/5 candidate Asta gene-level retrieval reports present.
- 5/5 review YAMLs curated with no remaining `PENDING` actions. The checkpoint
  added Asta evidence wiring to the four existing reviews that still had
  Asta-not-referenced validation warnings.
- Species-neutral plant-secondary-metabolite boundary module created and
  validated: `modules/plant_secondary_metabolite_biosynthesis_boundary.yaml`.
- No Falcon module-level synthesis was run for this checkpoint; Falcon remains
  queued for later module-level passes.
- Validation complete for all 5 candidate gene reviews and the module.
- Gene review pages rendered for all 5 candidates.
- Module page rendered:
  `pages/modules/plant_secondary_metabolite_biosynthesis_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/plant_secondary_metabolite_biosynthesis_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/plant_secondary_metabolite_biosynthesis_boundary.yaml
```

Main curation conclusions from this batch:

- The KEGG `ppu00999` membership is a boundary/absence bucket, not evidence for
  complete plant secondary metabolite biosynthesis in KT2440.
- `aroE__Q88RQ5`, `aroE__Q88IJ7`, and PP_3768 are shikimate-dehydrogenase-like
  enzymes tied to chorismate precursor metabolism.
- `bglX` is a broad periplasmic beta-glucosidase side node shared with
  glycoside-containing substrate maps, including the flavonoid-degradation
  boundary bucket.
- `metK` supplies S-adenosylmethionine and should be treated as general
  methyl-donor supply rather than specialized plant secondary metabolism.
- No plant-secondary-metabolite process annotation should be inferred from this
  KEGG bucket alone.

## Batch status: ppu01040 / unsaturated_fatty_acid_biosynthesis_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu01040_unsaturated_fatty_acid_biosynthesis_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu01040_unsaturated_fatty_acid_biosynthesis_boundary.md`

Status as of 2026-07-08 PDT / 2026-07-08 UTC:

- 3 KEGG `ppu01040` membership candidates extracted from pathway membership:
  `tesA`, `tesB`, and PP_5331.
- 3/3 candidate review folders present.
- 3/3 candidate Asta gene-level retrieval reports present.
- 3/3 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral unsaturated-fatty-acid boundary module created and validated:
  `modules/unsaturated_fatty_acid_biosynthesis_boundary.yaml`.
- No Falcon module-level synthesis was run for this checkpoint; Falcon remains
  queued for later module-level passes.
- Validation complete for all 3 candidate gene reviews and the module.
- Gene review pages rendered for all 3 candidates.
- Module page rendered:
  `pages/modules/unsaturated_fatty_acid_biosynthesis_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/unsaturated_fatty_acid_biosynthesis_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/unsaturated_fatty_acid_biosynthesis_boundary.yaml
```

Main curation conclusions from this batch:

- The KEGG `ppu01040` membership is a boundary/side-node bucket, not direct
  evidence for the canonical bacterial unsaturated-fatty-acid biosynthetic
  branch in KT2440.
- The actual unsaturated-acyl-ACP route remains FabA/FabB context already
  captured in `fatty_acid_biosynthesis`.
- `tesA` is best treated as an SGNH/GDSL lipid ester and fatty acyl-ACP
  hydrolase side node, with broad lipase activity retained as non-core context.
- `tesB` is best treated as a fatty acyl-CoA thioester hydrolase side node in
  acyl-CoA pool metabolism.
- PP_5331 is best treated as a HotDog-family long-chain fatty acyl-CoA
  hydrolase side node.
- No complete unsaturated-fatty-acid biosynthesis process annotation should be
  inferred from this KEGG bucket alone.

## Batch status: ppu01053 / siderophore_biosynthesis_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu01053_siderophore_biosynthesis_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu01053_siderophore_biosynthesis_boundary.md`

Status as of 2026-07-08 PDT / 2026-07-08 UTC:

- 2 KEGG `ppu01053` membership candidates extracted from pathway membership:
  PP_1183 and PP_2170. PP_1183 is not the primary partition gene for this
  bucket, but is included because it is a specific KEGG ppu01053 member.
- 2/2 candidate review folders present.
- 2/2 candidate Asta gene-level retrieval reports present.
- 2/2 review YAMLs curated with no remaining `PENDING` actions.
- Existing species-neutral siderophore boundary module extended and validated:
  `modules/siderophore_biosynthesis_boundary.yaml`.
- No Falcon module-level synthesis was run for this checkpoint; Falcon remains
  queued for later module-level passes.
- Validation complete for both candidate gene reviews and the expanded module.
- Gene review pages rendered for both candidates.
- Module page rerendered:
  `pages/modules/siderophore_biosynthesis_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/siderophore_biosynthesis_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/siderophore_biosynthesis_boundary.yaml
```

Main curation conclusions from this batch:

- The KEGG `ppu01053` membership is a siderophore-group NRPS boundary bucket,
  not a complete siderophore NRPS route in KT2440.
- PP_1183 is best treated as an EntD-family
  4'-phosphopantetheinyltransferase that activates aryl- and
  peptidyl-carrier-protein domains; it supports siderophore carrier-protein
  activation context.
- PP_2170 is best treated as a predicted chorismate mutase in chorismate and
  aromatic-amino-acid precursor metabolism.
- The PP_2170 salicylic-acid biosynthetic process annotation was removed as
  over-propagated from siderophore/salicylate context because current evidence
  supports chorismate mutase activity, not isochorismate or salicylate
  synthase activity.
- Direct experimental or comparative evidence is still needed to decide whether
  PP_2170 physiologically supplies a siderophore aryl-acid precursor in KT2440.

## Batch status: ppu01320 / sulfur_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu01320_sulfur_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu01320_sulfur_metabolism_boundary.md`

Status as of 2026-07-08 PDT / 2026-07-08 UTC:

- 9 KEGG `ppu01320` membership candidates extracted from pathway membership:
  PP_0860, `cysD`, `cysNC`, PP_1703, `cysH`, `cysI`, PP_2677, PP_3822, and
  `cysK`.
- 9/9 candidate review folders present.
- 9/9 candidate Asta gene-level retrieval reports present.
- 9/9 review YAMLs curated with no remaining `PENDING` actions.
- Existing species-neutral sulfur boundary module extended and validated:
  `modules/sulfur_metabolism_boundary.yaml`.
- No Falcon module-level synthesis was run for this checkpoint; Falcon remains
  queued for later module-level passes.
- Validation complete for all 9 candidate gene reviews and the expanded module.
  This checkpoint cleaned inherited Asta-not-referenced warnings in PP_0860,
  `cysD`, `cysNC`, PP_1703, `cysH`, `cysI`, PP_3822, and `cysK`; PP_2677 was
  already warning-free.
- Gene review pages rendered for all 9 candidates.
- Module page rerendered:
  `pages/modules/sulfur_metabolism_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/sulfur_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/sulfur_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- The KEGG `ppu01320` sulfur-cycle membership is a focused subset already
  covered by the broader `sulfur_metabolism_boundary` module, not a separate
  standalone sulfur-cycle module.
- `cysD` and `cysNC` provide sulfate adenylyltransferase / sulfate activation
  context; they are not primary partition genes for ppu01320 but are specific
  KEGG members and belong in the module reuse batch.
- `cysH`, PP_0860, and `cysI` cover activated-sulfate and sulfite-reductase
  assimilation context.
- PP_2677 and PP_3822 remain sulfur-redox boundary nodes: SoxYZ-like carrier
  candidate and cytochrome c-family electron-transfer protein, respectively.
- `cysK` supplies terminal cysteine synthase / L-cysteine biosynthesis context.
- The map should not drive a single monolithic sulfur-cycle process annotation
  across these genes.

## Batch status: ppu01501 / beta_lactam_resistance_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu01501_beta_lactam_resistance_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu01501_beta_lactam_resistance_boundary.md`

Status as of 2026-07-08 PDT / 2026-07-08 UTC:

- 20 KEGG `ppu01501` membership candidates extracted from pathway membership:
  PP_0906, PP_0907, `oprD`, PP_1263, `ftsI`, `ampG`, `ttgC`, `ttgB`,
  `ttgA`, PP_1798, `nagZ`, `ampC`, PP_3455, `mexB`, PP_3582, `mrdA-I`,
  `opmQ`, `mrdA-II`, PP_4923, and `mrcA`.
- 20/20 candidate review folders present. This checkpoint fetched the eight
  missing folders: PP_0906, PP_0907, PP_1263, `ampG`, PP_1798, PP_3455,
  PP_3582, and PP_4923.
- 20/20 candidate Asta gene-level retrieval reports present. This checkpoint ran
  Asta for the 14 missing reports.
- 20/20 review YAMLs curated with no remaining `PENDING` actions. The eight new
  stubs were first-pass curated, and Asta provenance was wired into six older
  warning-bearing reviews (`oprD`, `ftsI`, `nagZ`, `mexB`, `mrdA-I`, and
  `mrdA-II`).
- Species-neutral beta-lactam-resistance boundary module created and validated:
  `modules/beta_lactam_resistance_boundary.yaml`.
- No Falcon module-level synthesis was run for this checkpoint; Falcon remains
  queued for later module-level passes.
- Validation complete for all 20 candidate gene reviews and the module.
- Gene review pages rendered for all 20 candidates.
- Module page rendered:
  `pages/modules/beta_lactam_resistance_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/beta_lactam_resistance_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/beta_lactam_resistance_boundary.yaml
```

Main curation conclusions from this batch:

- KEGG `ppu01501` is a beta-lactam-resistance boundary map, not one linear
  pathway.
- `ampC` is the direct class C beta-lactamase. `ampG` and `nagZ` provide
  peptidoglycan recycling / AmpC-regulatory context rather than beta-lactam
  hydrolysis.
- `ftsI`, `mrdA-I`, `mrdA-II`, and `mrcA` are PBPs and cell-wall biosynthesis
  enzymes; their beta-lactam relevance is target/penicillin-binding context.
- `ttgA`/`ttgB`/`ttgC`, `mexB`, PP_0906, PP_0907, PP_3455, PP_1263, PP_1798,
  PP_3582, and PP_4923 represent RND/MFP/OMF efflux or xenobiotic-export
  boundary context, not beta-lactam-specific catabolic enzymes.
- `oprD` is an OprD/Occ-family porin and `opmQ` is a pyoverdine export OMF;
  both are retained as permeability/export boundary nodes.

## Batch status: ppu01502 / vancomycin_resistance_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu01502_vancomycin_resistance_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu01502_vancomycin_resistance_boundary.md`

Status as of 2026-07-08 PDT / 2026-07-08 UTC:

- 6 KEGG `ppu01502` membership candidates extracted from pathway membership:
  `murF`, `mraY`, `murG`, `ddlB`, `ddlA`, and `dadX`.
- 6/6 candidate review folders present; no new gene fetches were needed for
  this checkpoint.
- 6/6 candidate Asta gene-level retrieval reports present. Asta provenance was
  wired into the two older warning-bearing reviews (`mraY` and `murG`).
- 6/6 review YAMLs curated with no remaining `PENDING` actions and validated
  warning-free.
- Species-neutral vancomycin-resistance boundary/absence module created and
  validated: `modules/vancomycin_resistance_boundary.yaml`.
- No Falcon module-level synthesis was run for this checkpoint; Falcon remains
  queued for later module-level passes.
- Gene review pages rendered for all six candidates.
- Module page rendered:
  `pages/modules/vancomycin_resistance_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/vancomycin_resistance_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/vancomycin_resistance_boundary.yaml
```

Main curation conclusions from this batch:

- KEGG `ppu01502` is a vancomycin-resistance boundary/absence map for KT2440,
  not evidence for a complete acquired vancomycin-resistance pathway.
- `dadX` supplies D-alanine through alanine racemase activity; `ddlA` and
  `ddlB` form the D-Ala-D-Ala dipeptide.
- `murF` completes UDP-MurNAc-pentapeptide, `mraY` forms lipid I, and `murG`
  forms lipid II. These are normal peptidoglycan precursor and vancomycin target
  context.
- The batch does not support modeling a VanHAX D-Ala-D-Lac bypass or assigning a
  true vancomycin-resistance process to KT2440.
- This module intentionally overlaps the strict
  `peptidoglycan_biosynthesis` module but records the resistance-map boundary
  interpretation so ppu01502 does not drive over-annotation.

## Batch status: ppu01503 / cationic_antimicrobial_peptide_resistance_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu01503_cationic_antimicrobial_peptide_resistance_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu01503_cationic_antimicrobial_peptide_resistance_boundary.md`

Status as of 2026-07-08 PDT / 2026-07-08 UTC:

- 21 KEGG `ppu01503` membership candidates extracted from pathway membership:
  PP_0024, `dsbA`, PP_0906, PP_0907, `phoP`, `phoQ`, PP_1202, `ttgB`,
  `ttgA`, PP_1430, `lpxA`, PP_1798, PP_2320, `cpxR`, PP_3455, `mexB`,
  PP_4503, `ppiA`, PP_4592, `amiC`, and PP_4923.
- 21/21 candidate review folders present. This checkpoint fetched the ten
  missing folders: `dsbA`, `phoP`, `phoQ`, PP_1202, PP_1430, PP_2320,
  `cpxR`, PP_4503, `ppiA`, and `amiC`.
- 21/21 candidate Asta gene-level retrieval reports present. This checkpoint
  ran Asta for the ten newly fetched genes and wired Asta provenance into three
  older warning-bearing LPS/lipid A reviews: PP_0024, `lpxA`, and PP_4592.
- 21/21 review YAMLs curated with no remaining `PENDING` actions and validated
  warning-free.
- Species-neutral CAMP-resistance boundary module created and validated:
  `modules/cationic_antimicrobial_peptide_resistance_boundary.yaml`.
- No Falcon module-level synthesis was run for this checkpoint; Falcon remains
  queued for later module-level passes.
- Gene review pages rendered for all 21 candidates.
- Module page rendered:
  `pages/modules/cationic_antimicrobial_peptide_resistance_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/cationic_antimicrobial_peptide_resistance_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/cationic_antimicrobial_peptide_resistance_boundary.yaml
```

Main curation conclusions from this batch:

- KEGG `ppu01503` is a CAMP-resistance boundary map, not one linear pathway.
- PP_1202 is the clearest direct resistance-mechanism node: an MprF/LPG-synthase
  family phosphatidylglycerol lysyltransferase. The TreeGrafter alanyltransferase
  specificity was modified to the lysyltransferase term.
- `lpxA`, PP_0024, and PP_4592 are lipid A / LPS-core context. PP_0024 and
  PP_4592 remain unresolved EptA-like phosphotransferase/hydrolase-family
  candidates pending substrate-specific evidence.
- `phoP`/`phoQ`, `cpxR`, and PP_4503 are two-component regulatory context; the
  first pass kept them as response-regulator/sensor-kinase and transcriptional
  regulation functions.
- PP_0906/PP_0907, `ttgA`/`ttgB`, PP_1798, PP_3455/`mexB`, and PP_4923 are
  broad RND efflux/export boundary nodes reused from the beta-lactam-resistance
  batch, not cationic-peptide-specific enzymes.
- `dsbA`, PP_1430, and `ppiA` are periplasmic protein-folding/proteolysis
  context; PP_2320 and `amiC` are peptidoglycan remodeling context.
- The module should prevent the KEGG resistance-map membership from driving a
  generic CAMP-resistance process annotation across all 21 genes.

## Batch status: ppu02010 / abc_transporters_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary.md`
- `projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary_clusters.tsv`
- `projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary_clusters.md`

Status as of 2026-07-08 PDT / 2026-07-09 UTC:

- 207 KEGG `ppu02010` membership candidates extracted from the ABC-transporter
  map.
- The map is now recorded in the worklist as `PARTITIONED`, not as a single
  satisfiable module.
- Cluster script output partitions the 207 candidates into 74 locus-neighborhood
  systems and 10 coarse product classes.
- Current coverage after the first forty-six ppu02010 checkpoints: 207/207
  review folders present, 207/207 curated review YAMLs, and 207/207 Asta
  reports.
- Completed cluster C02 split 1, PP_0112-PP_0114: `metQ`, `metI`, and
  `metN1`. All three were fetched, Asta-backed, curated, and validated
  warning-free.
- Created and validated `modules/methionine_import_boundary.yaml` for the
  MetNIQ methionine ABC importer, then extended it with the C06
  PP_0219-PP_0221 MetNIQ-like importer.
- Completed cluster C06, PP_0219-PP_0221: `metP`, `metN2`, and `PP_0221`.
  All three were fetched, Asta-backed, curated, rendered, and validated
  warning-free.
- Completed cluster C02 split 2, PP_0117-PP_0120: `znuB`, `znuC`, and
  `PP_0120`. All three were fetched, Asta-backed, curated, and validated
  warning-free.
- Created and validated `modules/zinc_import_boundary.yaml` for the ZnuABC
  high-affinity zinc ABC importer.
- Completed cluster C50, PP_3801-PP_3803: `PP_3801`, `PP_3802`, and
  `PP_3803`. All three were fetched, Asta-backed, curated, and validated
  warning-free.
- Extended and validated `modules/zinc_import_boundary.yaml` with the
  PP_3801-PP_3803 Znu-like cation/zinc ABC import candidate.
- Completed clusters C63, C67, and C71: `PP_4881`, `PP_4882`, `PP_5135`,
  `PP_5136`, `fbpC`, `PP_5195`, and `fbpA`. All seven were fetched,
  Asta-backed, curated, and validated warning-free.
- Created and validated `modules/ferric_iron_abc_import_boundary.yaml` for the
  PP_5135-PP_5137 FbpABC-like ferric/iron importer and the partial
  PP_4881-PP_4882 and PP_5195-fbpA candidates.
- Completed clusters C42, C54, and C72: `PP_3076`, `PP_3077`, `PP_3078`,
  `PP_4146`, `yejA`, `PP_4148`, `PP_4149`, `yejF`, and `dppA-IV`. All nine
  were fetched, Asta-backed, curated, and validated warning-free.
- Created and validated `modules/yej_dpp_like_peptide_abc_import_boundary.yaml`
  for the complete PP_4146-PP_4150 Yej/Dpp-like peptide ABC import candidate,
  the partial PP_3076-PP_3078 Yej-like candidate, and the dppA-IV DppA-family
  singleton.
- Completed cluster C16, PP_0824-PP_0827: `ptxB`, `phnC`, `phnE`, and `ptxC`.
  All four were fetched, Asta-backed, curated, and validated warning-free.
- Extended and validated `modules/phosphonate_phosphinate_metabolism.yaml` with
  the PP_0824-PP_0827 phosphonate ABC import block.
- Completed cluster C07, PP_0225-PP_0227: `sctC`, `sctS`, and `fliY`. All
  three were fetched, Asta-backed, curated, and validated warning-free.
- Extended and validated `modules/sulfur_metabolism_boundary.yaml` with the
  PP_0225-PP_0227 cystine/sulfur-compound ABC import block.
- Completed cluster C10, PP_0280-PP_0283: `PP_0280`, `PP_0281`, `artJ`, and
  `aotP`. All four were fetched, Asta-backed, curated, and validated
  warning-free.
- Created and validated `modules/arginine_ornithine_abc_import_boundary.yaml`
  for the Art/Aot basic amino-acid ABC import boundary.
- Completed cluster C59, PP_4483-PP_4486: `hisP`, `hisM`, `hisQ`, and `argT`.
  All four were fetched, Asta-backed, curated, rendered, and validated
  warning-free.
- Extended and validated `modules/arginine_ornithine_abc_import_boundary.yaml`
  with the His/ArgT basic-amino-acid ABC import part and broadened the module
  title/description from arginine/ornithine-only to basic-amino-acid import.
- Completed clusters C11/C12, PP_0294-PP_0296 plus PP_0304: `cbcV`, `cbcW`,
  `cbcX`, and `caiX`. All four were fetched, Asta-backed, curated, and
  validated warning-free.
- Created and validated
  `modules/osmoprotectant_compatible_solute_transport_boundary.yaml` for the
  Cbc compatible-solute ABC importer plus the related CaiX periplasmic binding
  component, then extended it with the C17 PP_0868-PP_0871 Yeh-like
  compatible-solute importer.
- Completed cluster C17 split, PP_0868-PP_0873: `yehX`, `yehW`, `PP_0870`,
  `PP_0871`, and `potF-I`. All five were fetched, Asta-backed, curated,
  rendered, and validated warning-free.
- Created and validated `modules/polyamine_transport_boundary.yaml` for the
  PP_0873/potF-I putrescine/polyamine binding component.
- Completed cluster C18, PP_0878-PP_0885: `dppF`, `dppD`, `dppC`, `dppB`,
  `dppA-I`, `dppA-II`, and `dppA-III`. All seven were fetched, Asta-backed,
  curated, and validated warning-free.
- Created and validated `modules/dipeptide_abc_import_boundary.yaml` for the
  DppABCDF dipeptide ABC importer, with DppF/DppD as ATP-binding
  energy-coupling subunits, DppC/DppB as permeases, and the three DppA-family
  periplasmic binding proteins represented separately.
- Completed cluster C23, PP_1068-PP_1071: `gltL`, `gltK`, `gltJ`, and `gltI`.
  All four were fetched, Asta-backed, curated, rendered, and validated
  warning-free.
- Created and validated `modules/glutamate_aspartate_abc_import_boundary.yaml`
  for the GltIJKL glutamate/aspartate ABC importer.
- Completed cluster C14, PP_0615-PP_0619: `PP_0615`, `PP_0616`, `PP_0617`,
  `PP_0618`, and `PP_0619`. All five were fetched, Asta-backed, curated,
  rendered, and validated warning-free.
- Completed cluster C25, PP_1137-PP_1141: `livF-I`, `livG`, `livM`, `livH`,
  and `livK`. All five were fetched, Asta-backed, curated, rendered, and
  validated warning-free.
- Completed cluster C26, PP_1297-PP_1300: `yhdW`, `yhdX`, `yhdY`, and `yhdZ`.
  All four were fetched, Asta-backed, curated, rendered, and validated
  warning-free.
- Created and validated
  `modules/yhdwxyz_amino_acid_abc_import_boundary.yaml` for the complete
  predicted YhdWXYZ amino-acid ABC importer with unresolved exact substrate
  specificity.
- Created and validated
  `modules/branched_chain_amino_acid_abc_import_boundary.yaml` for the
  LivFGMHK high-affinity branched-chain amino-acid ABC importer.
- Completed cluster C62, PP_4863-PP_4867: `livF-II`, `braF`, `braE`, `braD`,
  and `PP_4867`. All five were fetched, Asta-backed, curated, rendered, and
  validated warning-free.
- Extended and validated
  `modules/branched_chain_amino_acid_abc_import_boundary.yaml` with a second
  Bra/Liv high-affinity branched-chain amino-acid ABC import part.
- Extended and validated
  `modules/branched_chain_amino_acid_abc_import_boundary.yaml` with a third
  PP_0615-PP_0619 high-affinity branched-chain amino-acid ABC import part.
- Completed cluster C40, PP_2767-PP_2770: `PP_2767`, `PP_2768`, `PP_2769`,
  and `PP_2770`. All four were fetched, Asta-backed, curated, rendered, and
  validated warning-free.
- Extended and validated
  `modules/branched_chain_amino_acid_abc_import_boundary.yaml` with a fourth
  PP_2767-PP_2770 high-affinity branched-chain amino-acid ABC import part.
- Completed cluster C38, PP_2748-PP_2753: `PP_2748`, `PP_2749`, `PP_2750`,
  `PP_2751`, `PP_2752`, and `PP_2753`. All six were fetched, Asta-backed,
  curated, rendered, and validated warning-free.
- Extended and validated
  `modules/branched_chain_amino_acid_abc_import_boundary.yaml` with a fifth
  PP_2748-PP_2753 high-affinity branched-chain amino-acid ABC import part.
- Completed compatible-solute clusters C01, C27, C41, and C48: `PP_0076`,
  `betX`, `opuA`, `PP_2775`, `PP_3558`, and `PP_3559`. All six were fetched,
  Asta-backed, curated, and validated warning-free.
- Extended and validated
  `modules/osmoprotectant_compatible_solute_transport_boundary.yaml` with
  `PP_0076` as a related periplasmic choline-family binding component and
  `opuA`/`PP_2775` as a predicted glycine-betaine/L-proline compatible-solute
  importer, then added `betX` as a related betaine-family binding component and
  `PP_3558`/`PP_3559` as a partial glycine-betaine transporter pair with the
  ATPase partner left unresolved.
- Completed cluster C37, PP_2656-PP_2659: `pstS`, `pstC`, `pstA`, and
  `pstB1`. All four were fetched, Asta-backed, curated, rendered, and validated
  warning-free.
- Completed cluster C73, PP_5326-PP_5329: `pstB2`, `PP_5327`, `PP_5328`, and
  `PP_5329`. All four were fetched, Asta-backed, curated, rendered, and
  validated warning-free.
- Created, extended, and validated `modules/phosphate_import_boundary.yaml` for
  the PP_2656-PP_2659 PstSACB and PP_5326-PP_5329 Pst-like high-affinity
  inorganic phosphate ABC importers.
- Completed cluster C52, PP_3828-PP_3830: `modA`, `modB`, and `modC`. All
  three were fetched, Asta-backed, curated, rendered, and validated
  warning-free.
- Created and validated `modules/molybdate_abc_import_boundary.yaml` for the
  ModABC molybdate ABC importer.
- Completed cluster C61, PP_4841-PP_4845: `urtA`, `urtB`, `urtC`, `urtD`, and
  `urtE`. All five were fetched, Asta-backed, curated, rendered, and validated
  warning-free.
- Created and validated `modules/urea_abc_import_boundary.yaml` for the
  UrtABCDE urea ABC importer.
- Completed cluster C29, PP_2154-PP_2156: `lolC`, `lolD`, and `lolE`. All
  three were fetched, Asta-backed, curated, rendered, and validated
  warning-free.
- Created and validated `modules/lipoprotein_lolcde_localization_boundary.yaml`
  for the LolCDE lipoprotein-release/localization ABC transporter.
- Completed cluster C58, PP_4324-PP_4327: `ccmD`, `ccmC`, `ccmB`, and
  `ccmA`. All four were fetched, Asta-backed, curated, rendered, and validated
  warning-free.
- Created and validated
  `modules/ccm_heme_export_cytochrome_c_maturation_boundary.yaml` for the
  CcmABCD heme export/cytochrome c maturation boundary.
- Completed cluster C20, PP_0958-PP_0962: `mlaF`, `mlaE`, `mlaD`, `ttg2D`,
  and `ttg2E`. All five were fetched, Asta-backed, curated, and validated; the
  only validation warning is the intentional no-core-function warning on
  unresolved STAS-domain accessory candidate `ttg2E`.
- Created and validated `modules/mla_phospholipid_transport_boundary.yaml` for
  the Mla/Ttg2 phospholipid transport and outer-membrane lipid asymmetry
  boundary.
- Completed the Lpt/MsbA lipid/LPS export checkpoint: ppu02010 members `lptB`,
  `PP_0982`, `PP_0983`, and `msbA` plus context `lptA`, `lptC`, `lptD`, and
  `lptE`. All eight were fetched, Asta-backed, curated, rendered, and validated
  warning-free.
- Created and validated `modules/lpt_lps_transport_boundary.yaml` for MsbA
  lipid A-core flipping plus LptBFGC/A/DE LPS transport and outer-membrane
  assembly.
- Completed cluster C28, PP_1778-PP_1779: `PP_1778` and `PP_1779`. Both were
  fetched, Asta-backed, curated, rendered, and validated warning-free.
- Extended `modules/lpt_lps_transport_boundary.yaml` with a separate
  Wzt/KpsT/TagH-like PP_1778-PP_1779 LPS/polysaccharide ABC export candidate,
  kept distinct from canonical LptBFG/MsbA until substrate identity is resolved.
- Completed cluster C66, `ftsX`/`ftsE`: both genes were fetched, Asta-backed,
  curated, rendered, and validated warning-free.
- Created and validated `modules/ftsex_cell_division_boundary.yaml` for the
  FtsEX cell-division ABC-like complex, kept separate from conventional
  transported-substrate ABC systems.
- Completed cluster C03, PP_0140-PP_0142: `PP_0140`, `PP_0141`, and
  `PP_0142`. All three were fetched, Asta-backed, curated, rendered, and
  validated warning-free.
- Created and validated
  `modules/mce_mlad_mlae_like_phospholipid_transport_boundary.yaml` for the
  DRAFT Mce/MlaD-MlaE-like phospholipid transport candidate.
- Completed the PP_5165/`plpB` singleton from C69. `plpB` was fetched,
  Asta-backed, curated, rendered, and validated with the intentional
  no-core-function warning expected for an unresolved NlpA-family lipoprotein.
- Completed the PotF-like singleton paralog group from C30/C43/C49/C53/C74:
  `PP_2195`, `potF-II`, `PP_3719`, `potF-III`, and `potF-IV`. All five were
  fetched, Asta-backed, curated, rendered, and validated warning-free; the
  existing `modules/polyamine_transport_boundary.yaml` module was extended to
  represent these periplasmic putrescine/polyamine-binding components.
- Completed cluster C70, PP_5177-PP_5181: `spuH`, `spuG`, `spuF`, `spuE`,
  and `spuD`. All five were fetched, Asta-backed, curated, and validated
  warning-free; `modules/polyamine_transport_boundary.yaml` was extended to
  separate this complete Spu/Pot spermidine/putrescine ABC importer from the
  unresolved PotF-like singleton binding components.
- Completed cluster C22, PP_1015-PP_1018: `gtsA`, `gtsB`, `gtsC`, and `gtsD`.
  All four were fetched, Asta-backed, curated, rendered, and validated
  warning-free.
- Created and validated `modules/glucose_import_boundary.yaml` for the
  PP_1015-PP_1018 Gts glucose ABC importer.
- Completed cluster C32, PP_2260-PP_2264: `PP_2260`, `PP_2261`, `PP_2262`,
  `PP_2263`, and `PP_2264`. All five were fetched, Asta-backed, curated,
  rendered, and validated warning-free.
- Created and validated `modules/sugar_glycerol_phosphate_import_boundary.yaml`
  for the unresolved sugar/glycerol-phosphate-like ABC importer.
- Completed cluster C33, PP_2454-PP_2459: `rbsB`, `rbsA-I`, `rbsC`, and
  `rbsD`. All four were fetched, Asta-backed, curated, rendered, and validated
  warning-free.
- Created and validated `modules/ribose_import_boundary.yaml` for the
  PP_2454-PP_2456 Rbs D-ribose ABC importer plus the associated PP_2459 RbsD
  D-ribose pyranase accessory enzyme.
- Completed cluster C39, PP_2757-PP_2761: `PP_2757`, `PP_2758`, `rbsA`,
  `PP_2760`, and `PP_2761`. All five were fetched, Asta-backed, curated,
  rendered, and validated warning-free.
- Extended and validated `modules/ribose_import_boundary.yaml` with the
  PP_2758/rbsA/PP_2760/PP_2761 RbsABC D-ribose importer and a separate
  unresolved PP_2757 sugar-binding component.
- Completed cluster C46, PP_3342-PP_3346: `nikA`, `nikB`, `nikC`, `nikD`, and
  `nikE`. All five were fetched, Asta-backed, curated, and validated
  warning-free.
- Created and validated `modules/nickel_import_boundary.yaml` for the NikABCDE
  nickel ABC importer.
- Completed clusters C55/C56, `pvdT` and `pvdE`: both already-curated
  pyoverdine export/precursor-export reviews now have Asta reports. `pvdT` was
  validated warning-free; `pvdE` was updated to cite relevant Falcon support,
  validated warning-free, and rendered.
- Completed clusters C04/C15/C31/C34/C64 secretion/exporter pass: `paxB`,
  `PP_0804`, `PP_2240`, `aprDA`, and `cyaB`. All five were fetched,
  Asta-backed, curated, rendered, and validated warning-free.
- Created, validated, and rendered
  `modules/type_i_protein_secretion_abc_boundary.yaml` for `paxB`, `PP_0804`,
  `aprDA`, and `cyaB`; `PP_2240` was kept outside that module as an unresolved
  generic ABCD-like efflux transporter.
- Completed the final C13/C24/C35/C36/C51/C60/C68 ppu02010 gap pass:
  `PP_0524`, `PP_1078`, `PP_2595`, `PP_2596`, `PP_2628`, `PP_3818`,
  `PP_4542`, and `PP_5157`. All eight were fetched, Asta-backed, curated,
  rendered, and validated.
- Extended, validated, and rendered `modules/phosphate_import_boundary.yaml`
  with `PP_3818` as a PstS-family phosphate-binding singleton with unresolved
  transporter partners.
- No Falcon module-level synthesis was run for the full ABC map; module-level
  Falcon should be used only for coherent substrate/module sub-batches.
- Worklist rebuild and batch/cluster extraction complete with:

```bash
uv run python projects/P_PUTIDA/build_pathway_worklist.py
uv run python projects/P_PUTIDA/extract_pathway_batch.py ppu02010 --module abc_transporters_boundary
uv run python projects/P_PUTIDA/cluster_ppu02010_abc_transporters.py
```

Main curation conclusions from this batch:

- KEGG `ppu02010` is an umbrella transporter map and should not drive one
  generic ABC-transporter module.
- The mixed C02 locus-neighborhood cluster must be split into two biological
  systems: MetQ/MetI/MetN1 methionine import and ZnuB/ZnuC/PP_0120 zinc import.
  `PP_0120` is represented as a ZnuA-family periplasmic high-affinity
  zinc-binding component, and its cell-adhesion annotation was removed as a
  family spillover.
- The C50 PP_3801-PP_3803 locus is a second Znu-like cation/zinc ABC import
  candidate: `PP_3801` is a ZnuA/PsaA-like signal-peptide-bearing
  substrate-binding component, `PP_3802` is the predicted ATP-binding
  energy-coupling subunit, and `PP_3803` is the multi-pass cation permease.
  It extends `zinc_import_boundary`; exact zinc specificity versus another
  transition-metal substrate remains open pending direct uptake evidence.
- The ferric/iron ABC import pass separates one complete FbpABC-like locus,
  PP_5135-PP_5137, from two partial candidate loci, PP_4881-PP_4882 and
  PP_5195-fbpA. PP_5135 TreeGrafter thiamine terms and fbpC
  quaternary-ammonium transport were treated as automated spillovers. Exact
  ferric iron versus iron-chelate substrate and missing ATPase partners for
  C63/C71 remain open.
- The Yej/Dpp-like peptide import pass separates the complete PP_4146-PP_4150
  candidate from the partial PP_3076-PP_3078 candidate and the dppA-IV
  DppA-family singleton. Microcin transport is retained as non-core Yej-family
  context, while generic protein/transmembrane transport annotations were marked
  broad relative to peptide or dipeptide ABC uptake.
- C06 PP_0219-PP_0221 is a second MetNIQ-like methionine import block rather
  than a generic amino-acid transporter. `metP` is the permease, `metN2` is the
  ATP-binding energy-coupling subunit, and `PP_0221` is a MetQ-like lipoprotein
  binding component; exact L- versus D-methionine substrate preference remains
  unresolved.
- The first completed sub-batch is a coherent phosphonate import system:
  `ptxB` is the predicted periplasmic solute-binding component, `phnC` is the
  reviewed ATP-binding energy-coupling component, and `phnE`/`ptxC` are
  predicted permeases.
- The phosphonate module records import as input context for PhnW/PhnX AEP
  catabolism, but the import-to-catabolism edge is a `KNOWLEDGE_GAP`; exact
  transported substrate range and direct AEP handoff remain unverified.
- The second completed sub-batch is a cystine/sulfur-compound import system:
  `sctC` is the ATP-binding component, `sctS` is the permease with L-cystine
  transporter support, and `fliY` is a periplasmic cystine-binding component.
  Ion-channel and monoatomic-ion transport spillovers on `fliY` were removed or
  replaced.
- The C10 Art/Aot block is a basic amino-acid import boundary: PP_0280 and
  PP_0281 are ArtM/ArtQ-like permeases, `artJ` is the periplasmic L-arginine
  substrate-binding component, and `aotP` is the ATP-binding energy-coupling
  subunit. L-arginine transport is the stronger first-pass call; L-ornithine
  transport is retained as a caveated lead from the `aotP` product name.
- The C59 His/ArgT block is a second basic-amino-acid import system: `hisP` is
  the ATP-binding energy-coupling subunit, `hisM` and `hisQ` are inner-membrane
  permeases, and `argT` is the periplasmic lysine/arginine/ornithine
  substrate-binding component. The first-pass process call is basic amino-acid
  transmembrane transport; exact preference among histidine, lysine, arginine,
  and ornithine remains open.
- The third completed sub-batch is a choline/betaine/carnitine-compatible-solute
  transport boundary: `cbcV` is the ATP-binding component, `cbcW` is the
  permease, `cbcX` is the periplasmic substrate-binding component, and `caiX`
  is kept as a related singleton periplasmic binding component with unresolved
  choline versus carnitine preference.
- The C17 locus-neighborhood cluster also needed splitting: PP_0868-PP_0871 is
  a Yeh-like quaternary-amine/glycine-betaine compatible-solute ABC importer,
  while PP_0873/potF-I is a putrescine/polyamine-binding component and belongs
  in a polyamine transport boundary, not in the compatible-solute module.
- The additional PotF-like singleton paralogs `PP_2195`, `potF-II`, `PP_3719`,
  `potF-III`, and `potF-IV` support the same periplasmic putrescine/polyamine
  binding and polyamine-transport component context as `potF-I`, but should not
  be promoted to complete ABC uptake systems until their permease/ATPase
  partners and substrate preferences are resolved.
- The C70 PP_5177-PP_5181 Spu/Pot block is a complete predicted
  spermidine/putrescine ABC importer: `spuH` and `spuG` are inner-membrane
  permeases, `spuF`/PotA is the ATP-binding energy-coupling subunit, and
  `spuE`/`spuD` are periplasmic spermidine/putrescine-family binding subunits.
  Exact substrate range and binding-protein redundancy remain open.
- The C18 Dpp locus is a coherent dipeptide ABC import system: DppF/DppD are
  ATP-binding energy-coupling subunits, DppC/DppB are membrane permeases, and
  DppA-I/DppA-II/DppA-III are related periplasmic substrate-binding
  components. The exact ligand range and redundancy/specialization among the
  three DppA-family binding proteins remain open.
- The C23 GltIJKL locus is a coherent acidic-amino-acid import system: `gltL`
  is the ATP-binding energy-coupling subunit, `gltK` and `gltJ` are
  inner-membrane permeases, and `gltI` is the periplasmic substrate-binding
  component. The first-pass process call is L-glutamate and L-aspartate
  transmembrane transport, with relative substrate preference left open.
- The C26 YhdWXYZ locus is a coherent predicted amino-acid ABC importer:
  `yhdW` is the solute-binding component, `yhdX` and `yhdY` are
  inner-membrane permeases, and `yhdZ` is the ATP-binding energy-coupling
  subunit. The exact amino-acid substrate is unresolved, so it is kept in a
  separate boundary module rather than merged into acidic, branched-chain,
  basic, methionine, or cystine/sulfur-amino-acid import modules.
- The C25 LivFGMHK locus is a coherent high-affinity branched-chain amino-acid
  import system: `livF-I` and `livG` are ATP-binding energy-coupling subunits,
  `livM` and `livH` are inner-membrane permeases, and `livK` is the
  periplasmic leucine/branched-chain amino-acid binding component. The
  first-pass process call is BCAA import with valine, isoleucine, and leucine
  annotations retained where directly supported; phenylalanine, alanine, and
  D-alanine transfer calls were treated as family spillover rather than core
  function.
- The C62 Bra/Liv locus is a second coherent high-affinity branched-chain
  amino-acid import system: `livF-II` and `braF` are ATP-binding energy-coupling
  subunits, `braE` and `braD` are inner-membrane permeases, and `PP_4867` is a
  BraC-like periplasmic amino-acid-binding component. It extends the same BCAA
  import boundary module; exact redundancy or substrate/regulatory differences
  from C25 remain open.
- The C14 PP_0615-PP_0619 locus is a third coherent high-affinity
  branched-chain amino-acid import system: `PP_0615` and `PP_0616` are
  ATP-binding energy-coupling subunits, `PP_0617` and `PP_0618` are
  inner-membrane permeases, and `PP_0619` is a signal-peptide-bearing
  periplasmic leucine-family substrate-binding component. It extends the same
  BCAA import boundary module; exact redundancy or substrate/regulatory
  differences from C25 and C62 remain open.
- The C40 PP_2767-PP_2770 locus is a fourth coherent high-affinity
  branched-chain amino-acid import system: `PP_2767` is the ATP-binding
  energy-coupling subunit, `PP_2768` and `PP_2769` are inner-membrane
  permeases, and `PP_2770` is a signal-peptide-bearing leucine-family
  substrate-binding component. It extends the same BCAA import boundary module;
  exact redundancy or substrate/regulatory differences from C14, C25, and C62
  remain open.
- The C38 PP_2748-PP_2753 locus is a fifth coherent high-affinity
  branched-chain amino-acid import system: `PP_2748` and `PP_2753` are
  ATP-binding energy-coupling subunits, `PP_2749` and `PP_2750` are
  inner-membrane permeases, and `PP_2751`/`PP_2752` are signal-peptide-bearing
  leucine-family substrate-binding components. It extends the same BCAA import
  boundary module; exact redundancy or substrate/regulatory differences from
  C14, C25, C40, and C62 remain open.
- The later compatible-solute pass added `PP_0076` as a singleton
  signal-peptide-bearing choline betaine-binding component with unresolved
  cognate transporter partners, added `opuA`/`PP_2775` as a predicted
  glycine-betaine/L-proline compatible-solute importer, added `betX` as a
  related glycine-betaine binding component, and added `PP_3558`/`PP_3559` as a
  partial glycine-betaine-compatible-solute pair. These extend the
  osmoprotectant boundary rather than creating a separate broad ABC module; the
  C48 ATPase partner remains a knowledge gap.
- The C37 PstSACB and C73 Pst-like blocks are inorganic phosphate importers and
  should remain separate from the PP_0824-PP_0827 Phn/Ptx organic phosphonate
  importer. The combined phosphate module keeps open whether KT2440 has two
  phosphate import modules or paralogous variants of one phosphate-limitation
  transport system.
- The C52 ModABC block is a molybdate importer: `modA` is the periplasmic
  molybdate-binding component, `modB` is the inner-membrane permease, and
  `modC` is the reviewed ATP-binding energy-coupling subunit with EC 7.3.2.5
  support for ATP-dependent molybdate import. ModA's tungstate-binding call is
  retained as non-core family context rather than promoted as the module's
  primary substrate.
- The C61 UrtABCDE block is a urea importer: `urtA` is the periplasmic
  urea-binding component, `urtB` and `urtC` are inner-membrane permeases, and
  `urtD`/`urtE` are ATP-binding energy-coupling subunits. Amino-acid and
  branched-chain amino-acid transport annotations on the locus were treated as
  over-propagated Liv-family spillover rather than promoted as the module's
  substrate.
- The C29 LolCDE block is a lipoprotein-release/localization system: `lolC`
  and `lolE` are the multi-pass membrane permease components, while reviewed
  `lolD` is the ATP-binding energy-coupling subunit. The module captures the
  transfer of mature outer membrane-directed lipoproteins toward LolA and keeps
  this apart from LPS and phospholipid transport modules.
- The C58 CcmABCD block is a heme-handling/export system for c-type cytochrome
  biogenesis: `ccmD`, `ccmC`, and `ccmB` are inner-membrane heme-handling
  components, while reviewed `ccmA` is the ATP-binding energy-coupling subunit
  of CcmAB. The module records heme transport/export and cytochrome c
  maturation while retaining UniProt's caveat that CcmA's exact direct role is
  uncertain.
- The C20 Mla/Ttg2 block is a phospholipid transport/lipid-asymmetry system:
  `mlaF` is the ATP-hydrolyzing energy-coupling subunit, `mlaE` is the
  inner-membrane permease, `mlaD` is the MlaD-domain phospholipid-binding
  component, and `ttg2D` is a MlaC-family periplasmic phospholipid-binding
  component. `ttg2E` remains an unresolved STAS-domain accessory candidate.
  Obsolete UniProt-carried `GO:0005548` was not authored into the reviews or
  module.
- The Lpt/MsbA lipid/LPS export checkpoint separates MsbA lipid A-core flipping
  at the inner membrane from LptBFGC/A/DE LPS transport and outer-membrane
  assembly. `msbA` oligopeptide transport terms were removed as
  PANTHER/ABC-family over-propagation.
- The C28 PP_1778-PP_1779 block is a Wzt/KpsT/TagH-like envelope glycoconjugate
  export candidate. First-pass curation uses LPS/polysaccharide export context
  but keeps the exact LPS, O-antigen, capsule, or related polysaccharide
  substrate open and separate from canonical LptBFG/MsbA.
- The C66 FtsEX block is a cell-division/septal-ring ABC-like system, not a
  conventional transported-substrate pathway. `ftsX` is the multi-pass
  inner-membrane FtsEX component, `ftsE` is the ATP-hydrolyzing cytoplasmic-side
  component, and generic transmembrane transporter/transport terms on `ftsE`
  are over-annotated pending direct substrate evidence.
- The C03 PP_0140-PP_0142 block is a putative Mce/MlaD-MlaE-like phospholipid
  transporter candidate. Direct retrieval was weak, so the module remains
  `DRAFT` and is kept separate from the better supported PP_0958-PP_0962
  Mla/Ttg2 system until genetic or biochemical evidence resolves whether C03 is
  a parallel phospholipid transporter, a remnant system, or a different
  substrate-specific transporter.
- PP_5165/`plpB` is not currently part of the sulfate/thiosulfate import module.
  It is an NlpA/MetQ-family lipoprotein near `cysA`/`cysW`/`cysU`/`sbp-II`,
  but current evidence supports only membrane/lipoprotein identity, not sulfate,
  thiosulfate, methionine, or another substrate-binding role.
- The C22 Gts block is a glucose ABC uptake system. P. putida-specific evidence
  supports PP1015-PP1018 in glucose uptake, so maltose-specific automated calls
  on `gtsD` were removed or replaced with ABC-type monosaccharide/glucose
  transport context. The exact D-glucose, D-mannose, maltose, and related-sugar
  substrate range remains unresolved.
- The C32 PP_2260-PP_2264 block is an unresolved sugar/glycerol-phosphate-like
  ABC importer. The strongest first-pass call is negative curation: ferric-iron,
  iron-transmembrane, and monoatomic-cation transport terms on `PP_2260` and
  `PP_2261` are InterPro FbpC-domain spillovers and were removed. Substrate
  specificity remains open.
- The C33 Rbs block separates transport from utilization: `rbsB`, `rbsA-I`, and
  `rbsC` form a D-ribose ABC importer, while `rbsD` is a cytosolic D-ribose
  pyranase accessory/catabolic enzyme rather than an ABC transporter subunit.
- The C39 ribose-like block supports a second RbsABC D-ribose importer:
  `PP_2758` is the ribose-binding component, `rbsA` is the reviewed
  ATP-binding energy-coupling subunit, and `PP_2760`/`PP_2761` are permeases.
  `PP_2757` remains an adjacent unresolved sugar-binding component with
  possible chemotaxis/contextual linkage rather than a confirmed ribose-import
  subunit.
- The NikABCDE nickel import system is complete: `nikA`
  is the periplasmic nickel-binding component, `nikB` and `nikC` are membrane
  permeases, and `nikD`/`nikE` are ATP-binding energy-coupling subunits. Heme
  binding and peptide/dipeptide transport annotations on this locus were removed
  or marked as over-propagated family spillovers.
- `pvdT` and `pvdE` are pyoverdine export/precursor-export context within the
  ABC map, not a reason to broaden the partial
  `siderophore_biosynthesis_boundary` into a complete pyoverdine
  assembly/export module. `pvdT` belongs to the PvdRT-OpmQ pyoverdine export
  system, while `pvdE` is best treated as pyoverdine precursor export tied to
  periplasmic maturation.
- The secretion/exporter pass separates T1SS/type-I protein secretion ABC
  exporters (`paxB`, `PP_0804`, `aprDA`, `cyaB`) from generic ABCD-like
  `PP_2240`. Lipid transporter calls on T1SS proteins were removed or treated
  as TreeGrafter spillover; peptidase/proteolysis calls from C39 domains were
  retained as non-core processing context where present.
- The final gap pass closes ppu02010 review/Asta coverage. `PP_0524` is a
  periplasmic cobalamin-binding candidate next to a B12-family TonB receptor,
  with the iron-response GOA term removed as family spillover. `PP_3818` is a
  PstS-family phosphate-binding singleton added to the phosphate boundary
  without forcing a complete transporter. `PP_1078` remains an unresolved ABC
  ATP-binding component, while `PP_2595`, `PP_2596`, `PP_2628`, and `PP_4542`
  are unresolved ABCB/type-1-exporter-like transporters with substrate-specific
  lipid or oligopeptide calls removed or over-annotated. `PP_5157` remains a
  cell-envelope solute-binding-family protein with no substrate core function.
- No ppu02010 candidates remain missing. The substrate-unknown ABC bucket is
  retained for future targeted experiments and should not be promoted into a
  broad generic ABC-transporter pathway module.

## Batch status: ppu00220 / arginine_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/ppu00220_arginine_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/ppu00220_arginine_biosynthesis.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 32 candidates curated: 31 KEGG `ppu00220` membership genes plus `argD`, which
  was promoted from UniPathway UPA00068 because it supplies the strict
  acetylornithine aminotransferase step while the partition assigns it to
  `ppu00330`.
- 32/32 candidate review folders present.
- 32/32 candidate Asta gene-level retrieval reports present. `argC1`, `alaA`,
  and `argE` failed once with transient Asta internal-server errors and
  succeeded on retry.
- 32/32 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral arginine-biosynthesis module created and validated:
  `modules/arginine_biosynthesis.yaml`.
- Falcon generic module research is still outstanding:
  `modules/arginine_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__arginine_biosynthesis__ppu00220-deep-research-falcon.md`.
- Validation complete for all 32 candidate gene reviews and the module. Gene
  warnings are limited to expected first-pass Asta context notices.
- Gene review pages rendered for all 32 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/arginine_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/arginine_biosynthesis.yaml
```

Main curation conclusions from this batch:

- The strict route is CarAB carbamoyl-phosphate supply, ArgA/ArgJ
  acetylglutamate formation, ArgB phosphorylation, ArgC1/ArgC2 reduction, ArgD
  aminotransferase, ArgE/PP_3571/ArgJ ornithine formation, ArgF citrulline
  formation, ArgG argininosuccinate formation, and ArgH terminal cleavage to
  L-arginine.
- `argD` is an explicit module-gap fill: it is UniPathway UPA00068-supported and
  carries GO:0003992/GO:0006526, but KEGG partitioning placed it under arginine
  and proline metabolism rather than the ppu00220 membership set.
- `arcA`, `arcB`, and `arcC` are arginine-deiminase/carbamate side-route nodes.
  `arcB` retains ornithine carbamoyltransferase activity but its electronic
  L-arginine biosynthetic process transfer is removed; a `NEW` L-arginine
  catabolic process suggestion is added from its catabolic UniProt identity.
- `ureA`, `ureB`, and `ureC` are urease/urea-catabolism side nodes. They are
  real nitrogen-metabolism functions but not committed arginine biosynthesis.
- `gdhA`, `gdhB`, `glnA`, PP_3148, PP_4399, PP_4547, `puuA-I`, `puuA-II`,
  `spuB`, `spuI`, `alaA`, and `ansB` are retained as precursor, nitrogen, or
  KEGG side-node context rather than strict ppu00220 steps.

## Batch status: ppu00230 / purine_metabolism

Batch files:

- `projects/P_PUTIDA/batches/ppu00230_purine_metabolism.tsv`
- `projects/P_PUTIDA/batches/ppu00230_purine_metabolism.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 65 candidates curated: 36 primary `ppu00230` bucket genes plus 29 KEGG
  membership side nodes whose primary buckets include pyrimidine metabolism,
  one-carbon/folate, sulfur assimilation, arginine/urea/carbamate, nucleotide
  sugar, and cyclic-nucleotide signaling contexts.
- 65/65 candidate review folders present.
- 65/65 candidate Asta gene-level retrieval reports present. `pde` failed once
  with a transient Asta internal-server error and succeeded on retry.
- 65/65 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral purine-metabolism boundary module created and validated:
  `modules/purine_metabolism.yaml`.
- Falcon generic module research is still outstanding:
  `modules/purine_metabolism-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__purine_metabolism__ppu00230-deep-research-falcon.md`.
- Validation complete for all 65 candidate gene reviews and the module. Gene
  warnings are limited to expected first-pass Asta context notices plus a few
  pre-existing nonblocking warnings in previously curated cross-bucket reviews.
- Gene review pages rendered for all 65 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/purine_metabolism.yaml
uv run python -m ai_gene_review.validation.module_validator modules/purine_metabolism.yaml
```

Main curation conclusions from this batch:

- The strict purine core should be split into de novo IMP formation
  (PurF/PurD/PurN or PurT/PurL/PurM/PurK/PurE/PurC/PurB/PurH), AMP branch
  (PurA/PurB), and GMP branch (GuaB/GuaA), rather than treating all KEGG ppu00230
  members as one satisfiability route.
- Salvage and pool maintenance are real purine-module context but separate from
  de novo biosynthesis: PP_0747, Apt, Xpt, Amn/PP_3662, PpnP, YfiH, Ndk, Gmk,
  Dgt, PP_5100, ApaH, NudE/NudF, RelA/SpoT, Ppx, and CyaA.
- Purine catabolism is represented by PP_0591, GuaD, XdhA/XdhB, PucM, PucL,
  PuuE, AllE, and AllA. PaoABC is retained as boundary xanthine/aldehyde
  oxidoreductase context because PaoC is xanthine-dehydrogenase-family, while
  PaoA/PaoB UniProt names emphasize promiscuous aromatic aldehyde
  dehydrogenase subunits.
- Cross-bucket side nodes include NrdA/NrdB ribonucleotide reductase,
  CysD/CysNC sulfate adenylyltransferase, ArcC/urease/carbamate nodes,
  nucleotide-sugar phosphomutases, and cyclic-nucleotide phosphodiesterase.
  These are real functions but not committed purine-biosynthesis steps.
- First-pass removals/corrections include `purC` cobalamin biosynthesis, `purM`
  phosphoribosylamine-glycine ligase activity, `puuE` carbohydrate metabolic
  process, and `yrfG` DNA repair/phosphoglycolate phosphatase transfers.

## Batch status: ppu00240 / pyrimidine_metabolism

Batch files:

- `projects/P_PUTIDA/batches/ppu00240_pyrimidine_metabolism.tsv`
- `projects/P_PUTIDA/batches/ppu00240_pyrimidine_metabolism.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 36 candidates curated: 24 primary `ppu00240` bucket genes plus 12 KEGG
  membership side nodes whose primary buckets include carbamoyl-phosphate
  supply, beta-alanine-generating pyrimidine catabolism, nucleotidase and
  nucleotide-pool housekeeping, purine/phosphorylase context, and dTMP
  one-carbon chemistry.
- 36/36 candidate review folders present.
- 36/36 candidate Asta gene-level retrieval reports present.
- 36/36 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral pyrimidine-metabolism boundary module created and validated:
  `modules/pyrimidine_metabolism.yaml`.
- Falcon generic module research is still outstanding:
  `modules/pyrimidine_metabolism-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__pyrimidine_metabolism__ppu00240-deep-research-falcon.md`.
- Validation complete for all 36 candidate gene reviews and the module. Gene
  warnings are limited to expected first-pass Asta context notices, intentional
  no-core warnings for `PP_3238`, `ygjP`, and `pyrC'`, and the pre-existing
  `thyA` cytosol-location warning.
- Gene review pages rendered for all 36 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/pyrimidine_metabolism.yaml
uv run python -m ai_gene_review.validation.module_validator modules/pyrimidine_metabolism.yaml
```

Tooling note:

- `pyrC'` exposed a shell-quoting edge in the `just` wrappers. Direct CLI fetch
  and render commands were used for that gene:

```bash
uv run --no-dev ai-gene-review fetch-gene PSEPK "pyrC'" --uniprot-id Q88D29 --output-dir .
uv run python -m ai_gene_review.render "genes/PSEPK/pyrC'/pyrC'-ai-review.yaml" -o "genes/PSEPK/pyrC'/pyrC'-ai-review.html"
```

Main curation conclusions from this batch:

- The strict de novo UMP core is CarAB carbamoyl-phosphate supply, PyrB
  aspartate carbamoyltransferase, PyrC dihydroorotase, PyrD quinone-linked
  dihydroorotate dehydrogenase, PyrE orotate phosphoribosyltransferase, and
  PyrF OMP decarboxylase.
- UTP/CTP branch and nucleotide-pool coverage is represented by PyrH, Ndk,
  PyrG, and Cmk; deoxypyrimidine and dTMP branch coverage by NrdA/NrdB, Dcd,
  Dut, and ThyA.
- Salvage and recycling are represented by Upp, PyrR, PpnP, and broad
  nucleotidase/nucleoside-phosphorylase side nodes such as UshA, SurE,
  PP_2531, and PP_3662.
- Reductive pyrimidine catabolism and beta-alanine context are represented by
  PydA/PydX, PydB, HyuC/PP_0614, and YdfG.
- `pyrC'` remains intentionally unresolved because current evidence mixes
  dihydroorotase/pyrimidine-biosynthesis and allantoinase/purine-catabolism
  interpretations; all existing annotations were left `UNDECIDED`.
- `PP_3238` and `ygjP` are retained as conservative annotation-empty
  candidate/context genes pending stronger evidence, with no core functions
  asserted.
- First-pass corrections include making `pyrC`, `pyrD`, `codA`, `pyrB`, and
  `maf-1` more specific where GOA contained broad hydrolase,
  oxidoreductase/deaminase/carbamoyltransferase, or pyrophosphatase terms.

## Batch status: ppu00250 / alanine_aspartate_glutamate_metabolism

Batch files:

- `projects/P_PUTIDA/batches/ppu00250_alanine_aspartate_glutamate_metabolism.tsv`
- `projects/P_PUTIDA/batches/ppu00250_alanine_aspartate_glutamate_metabolism.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 36 candidates curated: 8 primary `ppu00250` bucket genes plus 28 KEGG
  membership side nodes whose primary buckets include arginine, purine,
  pyrimidine, NAD, amino-sugar, nitrogen-assimilation, proline/polyamine,
  lysine-catabolism, succinate-semialdehyde, and biotin contexts.
- 36/36 candidate review folders present.
- 36/36 candidate Asta gene-level retrieval reports present.
- 36/36 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral alanine/aspartate/glutamate boundary module created and
  validated: `modules/alanine_aspartate_glutamate_metabolism.yaml`.
- Falcon generic module research is still outstanding:
  `modules/alanine_aspartate_glutamate_metabolism-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__alanine_aspartate_glutamate_metabolism__ppu00250-deep-research-falcon.md`.
- Validation complete for all 36 candidate gene reviews and the module.
  Warnings are limited to expected first-pass Asta context notices.
- Gene review pages rendered for all 36 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/alanine_aspartate_glutamate_metabolism.yaml
uv run python -m ai_gene_review.validation.module_validator modules/alanine_aspartate_glutamate_metabolism.yaml
```

Main curation conclusions from this batch:

- The strict hub is not a single linear pathway. It contains AlaA alanine
  transamination, GdhA/GdhB glutamate dehydrogenase, GlnA and GS-like paralog
  glutamine synthetase context, GltBD glutamate synthase, AspA aspartase, AsnB
  asparagine synthase, AnsA/PP_1160 asparaginase-family enzymes, and PP_0859
  omega-amidase/2-oxoglutaramate amidase.
- Many KEGG ppu00250 members are real cross-pathway nodes rather than committed
  alanine/aspartate/glutamate core steps: ArgG/ArgH, CarAB/PyrB, PurA/PurB/PurF,
  NadB, GlmS, PutA, PuuA/Spu ligases, DavD/DavT, Sad/GabD enzymes, and PP_2799.
- `davT` is the strongest direct experimental case in the batch. Its IDA/IMP
  annotations and PMID:11679348 support 5-aminovalerate aminotransferase
  activity in lysine catabolism; the broader GABA aminotransferase transfer was
  modified to the specific DavT activity.
- `PP_2799` was curated as a BioA-like biotin-biosynthesis aminotransferase
  based on TreeGrafter/PANTHER, not as a strict ppu00250 hub enzyme.
- `putA` was curated as bifunctional proline catabolism plus transcriptional
  repression; the electronic L-proline biosynthetic process transfer was
  removed as directionally inconsistent.
- First-pass specificity fixes include PP_0859 broad hydrolase to
  2-oxoglutaramate amidase, AspA broad catalytic/lyase terms to aspartate
  ammonia-lyase, and GlmS broad carbohydrate/glycosylation context to amino
  sugar biosynthesis.

## Batch status: ppu00260 / glycine_serine_threonine_metabolism

Batch files:

- `projects/P_PUTIDA/batches/ppu00260_glycine_serine_threonine_metabolism.tsv`
- `projects/P_PUTIDA/batches/ppu00260_glycine_serine_threonine_metabolism.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 66 candidates curated: 16 primary `ppu00260` bucket genes plus 50 KEGG
  membership side nodes whose primary buckets include tryptophan, cysteine and
  methionine, branched-chain amino acid, glyoxylate/glycerate, phospholipid,
  pyoverdine, one-carbon, glycine-cleavage, betaine, and nucleotide/central
  carbon contexts.
- 66/66 candidate review folders present.
- 66/66 candidate Asta gene-level retrieval reports present.
- 66/66 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral glycine/serine/threonine boundary module created and
  validated: `modules/glycine_serine_threonine_metabolism.yaml`.
- Falcon generic module research is still outstanding:
  `modules/glycine_serine_threonine_metabolism-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__glycine_serine_threonine_metabolism__ppu00260-deep-research-falcon.md`.
- Validation complete for all 66 candidate gene reviews and the module.
  Warnings are non-blocking: expected Asta context notices plus a few
  pre-existing carry-in warnings from older curated boundary genes.
- Gene review pages rendered for all 66 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/glycine_serine_threonine_metabolism.yaml
uv run python -m ai_gene_review.validation.module_validator modules/glycine_serine_threonine_metabolism.yaml
```

Main curation conclusions from this batch:

- The strict hub is split across serine biosynthesis (`serA`, `serC`, `serB`),
  homoserine/threonine biosynthesis (`hom`, `thrB`, `thrC`), serine-glycine
  one-carbon chemistry (`glyA1`, `glyA2`), glycine cleavage (`gcvP/H/T`
  clusters plus Lpd-family partners), threonine aldolase (`ltaE`), and
  methylated-glycine/betaine oxidation.
- The `PP_0310`-`PP_0316` neighborhood was curated as a likely
  methylated-glycine/betaine catabolism module: DgcA/DgcB predicted
  dimethylglycine dehydrogenase components, PP_0312/PP_0313 ETF partners, and
  GbcA/GbcB predicted glycine-betaine dioxygenase subunits.
- The `soxB/soxD/soxA/soxG` annotations were represented as tetrameric
  sarcosine oxidase subunit contributions rather than independent whole-complex
  catalytic activity for every subunit.
- `PP_4421` and `PP_4432` received provisional `NEW` first-pass annotations
  because GOA lacked an activity row: `PP_4421` broad transaminase activity
  from UniProt/PANTHER class-III aminotransferase identity, and `PP_4432`
  aminopeptidase activity from Xaa-Pro aminopeptidase/M24 peptidase identity.
- `PP_4423` remains substrate-uncertain; first-pass curation favors a
  succinylglutamate desuccinylase/aspartoacylase-family hydrolase framing, not
  a committed ppu00260 core step.
- Phospholipid nodes (`pcs`, `pssA`, `PP_4677`), pyoverdine/diaminobutyrate
  aminotransferase nodes (`pvdH`, `PP_2800`), `creA`, and threonine-dehydratase
  paralogs (`PP_3191`, `PP_4430`, `ilvA-I`, `ilvA-II`) should remain boundary
  context unless deeper evidence supports pathway-specific roles.

## Batch status: ppu00261 / monobactam_biosynthesis_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00261_monobactam_biosynthesis_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00261_monobactam_biosynthesis_boundary.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 9 candidates curated: all KEGG `ppu00261` membership genes.
- 9/9 candidate review folders present.
- 9/9 candidate Asta gene-level retrieval reports present.
- 9/9 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral monobactam boundary/absence module created and validated:
  `modules/monobactam_biosynthesis_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/monobactam_biosynthesis_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__monobactam_biosynthesis_boundary__ppu00261-deep-research-falcon.md`.
- Validation complete for all 9 candidate gene reviews and the module. Warnings
  are non-blocking: expected Asta context notices plus a pre-existing
  `asd__Q88LE4` core-process reflection warning.
- Gene review pages rendered for all 9 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/monobactam_biosynthesis_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/monobactam_biosynthesis_boundary.yaml
```

Main curation conclusions from this batch:

- `ppu00261` should be handled as a KEGG boundary/absence bucket in KT2440, not
  as evidence for a satisfiable monobactam pathway.
- `dapA__Q88NH2`, `dapA__Q88JL0`, `PP_2036`, `PP_4473`, `asd__Q88LE4`, and
  `dapB` are aspartate-family / diaminopimelate / L-lysine precursor context.
- `cysD` and `cysNC` are sulfate adenylyltransferase subunits in sulfate
  assimilation.
- `PP_3808` is an MbtH-like accessory protein; first-pass support is
  siderophore/NRPS context, not monobactam-specific biosynthesis.
- Duplicate `dapA` review names must be fetched with `ai-gene-review fetch-gene
  PSEPK dapA --uniprot-id <accession> --alias <collision-safe-name>` rather than
  by passing the collision-safe alias directly to `just fetch-gene`.

## Batch status: ppu00280 / branched_chain_amino_acid_degradation

Batch files:

- `projects/P_PUTIDA/batches/ppu00280_branched_chain_amino_acid_degradation.tsv`
- `projects/P_PUTIDA/batches/ppu00280_branched_chain_amino_acid_degradation.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 35 candidates curated: all KEGG `ppu00280` membership genes.
- 35/35 candidate review folders present.
- 35/35 candidate Asta gene-level retrieval reports present.
- 35/35 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral branched-chain amino acid degradation module created and
  validated: `modules/branched_chain_amino_acid_degradation.yaml`.
- Falcon generic module research is still outstanding:
  `modules/branched_chain_amino_acid_degradation-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__branched_chain_amino_acid_degradation__ppu00280-deep-research-falcon.md`.
- Validation complete for all 35 candidate gene reviews and the module. The only
  remaining full-batch warnings are pre-existing Asta-citation warnings on older
  side-pathway reviews, not on the 17 newly curated ppu00280 reviews.
- Gene review pages rendered for all 35 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/branched_chain_amino_acid_degradation.yaml
uv run python -m ai_gene_review.validation.module_validator modules/branched_chain_amino_acid_degradation.yaml
```

Main curation conclusions from this batch:

- Strict BCAA degradation coverage is concentrated in the `ivd`/`mccA`/`mccB`/
  `liuC` L-leucine branch, the `mmsB`/`mmsA-I`/`mmsA-II` L-valine branch, and
  the `bkdAA`/`bkdAB`/`bkdB` BCKDH complex.
- `liuC`, `mccA`, `bkdAA`, `bkdAB`, and `bkdB` needed conservative `NEW`
  first-pass rows for missing process or complex annotations reflected in the
  synthesized core functions.
- `ldh` had a freshly fetched GOA glutamate dehydrogenase activity inconsistent
  with UniProt EC 1.4.1.9; the review modifies it to L-leucine dehydrogenase
  activity.
- `PP_0596`, `aacs`, `atoA`, and `atoB` should be treated as ppu00280 boundary
  or endpoint chemistry, not committed upstream BCAA degradation.
- Fatty-acid beta-oxidation paralogs, thiolases, lipoamide E3 paralogs, and
  beta-ketoadipate CoA-transferases remain cross-bucket spillovers unless
  future evidence supports pathway-specific BCAA roles.

## Batch status: ppu00290 / branched_chain_amino_acid_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/ppu00290_branched_chain_amino_acid_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/ppu00290_branched_chain_amino_acid_biosynthesis.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 18 candidates curated: all KEGG `ppu00290` membership genes.
- 18/18 candidate review folders present.
- 18/18 candidate Asta gene-level retrieval reports present.
- 18/18 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral branched-chain amino acid biosynthesis module created and
  validated: `modules/branched_chain_amino_acid_biosynthesis.yaml`.
- Falcon generic module research is still outstanding:
  `modules/branched_chain_amino_acid_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__branched_chain_amino_acid_biosynthesis__ppu00290-deep-research-falcon.md`.
- Validation complete for all 18 candidate gene reviews and the module. The only
  remaining full-batch warnings are pre-existing Asta-citation warnings on older
  cross-bucket reviews, not on the four newly curated leucine-branch reviews.
- Gene review pages rendered for all 18 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/branched_chain_amino_acid_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/branched_chain_amino_acid_biosynthesis.yaml
```

Main curation conclusions from this batch:

- Strict BCAA biosynthesis coverage is concentrated in the AHAS node
  (`ilvI`/`ilvH`, with PP_1157/PP_1394 retained as side AHAS-like candidates),
  `ilvC`, `ilvD`, `ilvE`, and the leucine branch `leuA`/`leuC`/`leuD`/`leuB`.
- Threonine-dehydratase paralogs (`ilvA-I`, `ilvA-II`, PP_3191, PP_4430) should
  be handled as isoleucine-precursor and threonine-catabolism boundary context
  until direct paralog-specific evidence resolves their main flux role.
- `PP_2930` is serine ammonia-lyase side context; `alaA` and `ldh` are broader
  aminotransferase/dehydrogenase boundary nodes in the KEGG map rather than
  strict committed BCAA biosynthesis steps.
- Authored L-isoleucine biosynthesis terms were refreshed from obsolete
  `GO:0009097` to current `GO:1901705`; machine-sourced GOA IDs and provenance
  text were left intact where appropriate.

## Batch status: ppu00300 / lysine_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/ppu00300_lysine_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/ppu00300_lysine_biosynthesis.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 19 candidates curated: all KEGG `ppu00300` membership genes.
- 19/19 candidate review folders present, with `lysA-II` resolved to the
  existing accession-matched `genes/PSEPK/lysA/` review for Q88CF4.
- 19/19 candidate Asta gene-level retrieval reports present.
- 19/19 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral L-lysine biosynthesis via diaminopimelate module created and
  validated: `modules/lysine_biosynthesis.yaml`.
- Falcon generic module research is still outstanding:
  `modules/lysine_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__lysine_biosynthesis__ppu00300-deep-research-falcon.md`.
- Validation complete for all 19 resolved candidate review folders and the
  module. The only remaining full-batch warnings are pre-existing Asta-citation
  and homoserine-process reflection warnings on older cross-bucket reviews, not
  on the nine newly curated ppu00300 reviews.
- Gene review pages rendered for all 19 resolved candidate review folders.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/lysine_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/lysine_biosynthesis.yaml
```

Main curation conclusions from this batch:

- Strict bacterial L-lysine biosynthesis is the diaminopimelate route through
  shared aspartate-family precursor supply (`PP_4473`, `asd__Q88LE4`), DapA-like
  HTPA synthases (`dapA__Q88NH2`, `dapA__Q88JL0`, PP_2036), `dapB`, the
  DapD/DapC/DapE succinylated branch, DapF epimerases (`dapF__Q88GD4`,
  `dapF__Q88CF3`), and LysA decarboxylases (`lysA-I` and Q88CF4/`lysA`).
- `murE` and `murF` consume meso-diaminopimelate in peptidoglycan precursor
  assembly; they explain KEGG membership but should remain boundary nodes, not
  lysine-biosynthetic steps.
- `hom` and PP_0664 are homoserine-branch enzymes, `aspC` is upstream aspartate
  transamination context, and `aruC` is arginine/ornithine aminotransferase
  context.
- `dapE` needed curation cleanup: remove the arginine-biosynthesis transfer and
  modify acetylornithine deacetylase to succinyl-diaminopimelate desuccinylase
  activity.
- Authored L-lysine biosynthesis terms should use current `GO:0009085`; obsolete
  `GO:0009089` and `GO:0019877` are retained only in provenance or explanatory
  rationale text.

## Batch status: ppu00310 / lysine_degradation

Batch files:

- `projects/P_PUTIDA/batches/ppu00310_lysine_degradation.tsv`
- `projects/P_PUTIDA/batches/ppu00310_lysine_degradation.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 32 candidates curated: all KEGG `ppu00310` membership genes.
- 32/32 candidate review folders present.
- 32/32 candidate Asta gene-level retrieval reports present.
- 32/32 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral lysine degradation and related glutarate/pipecolate module
  created and validated: `modules/lysine_degradation.yaml`.
- Falcon generic module research is still outstanding:
  `modules/lysine_degradation-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__lysine_degradation__ppu00310-deep-research-falcon.md`.
- Validation complete for all 32 candidate gene reviews and the module. The only
  remaining full-batch warnings are inherited Asta-citation warnings on 16 older
  boundary reviews, not on the 11 newly curated ppu00310 reviews.
- Gene review pages rendered for all 32 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/lysine_degradation.yaml
uv run python -m ai_gene_review.validation.module_validator modules/lysine_degradation.yaml
```

Main curation conclusions from this batch:

- The strict L-lysine-to-glutarate Dav route is davB, davA, davT, and davD.
  Existing DavT/DavD curation already captured the 5-aminovalerate and glutarate
  semialdehyde steps; this batch added first-pass DavB/DavA curation and process
  reflection.
- GlaH/CsiD and LhgO are the CoA-independent glutarate and
  L-2-hydroxyglutarate branch connected to L-lysine catabolism.
- PP_4108, hglS, ydiJ, amaD, amaA, amaB, dpkA, and alr should be tracked as
  D-lysine, L-2-aminoadipate, D-2-hydroxyglutarate, and pipecolate side-route
  context rather than collapsing every ppu00310 member into the Dav route.
- PP_4108 is primarily L-2-aminoadipate:2-oxoglutarate transaminase; its
  experimentally observed 5-aminovalerate activity was retained as non-core
  secondary activity because DavT remains the dedicated Dav-route
  5-aminovalerate aminotransferase.
- AmaD lacked a GOA molecular-function annotation beyond cytoplasm; the review
  adds conservative `NEW` D-amino-acid oxidase activity (`GO:0003884`) and
  D-amino acid catabolic process (`GO:0019478`) entries rather than inventing a
  D-lysine-specific GO ID.
- PP_0159 remains unresolved CoA-transferase / glutarate boundary context.
- PatD, Prr, GabD-II, Sad-I, beta-oxidation enzymes, thiolases, and lipoamide
  enzymes are cross-bucket aldehyde, GABA, beta-oxidation, or central-carbon
  spillovers unless future evidence supports a committed lysine-catabolic role.

## Batch status: ppu00330 / arginine_proline_metabolism

Batch files:

- `projects/P_PUTIDA/batches/ppu00330_arginine_proline_metabolism.tsv`
- `projects/P_PUTIDA/batches/ppu00330_arginine_proline_metabolism.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 39 candidates curated: all KEGG `ppu00330` membership genes.
- 39/39 candidate review folders present. The duplicate-safe
  `ocd__Q88H32` folder was populated by fetching the reviewed UniProt `ocd`
  record and normalizing the generated filenames.
- 39/39 candidate Asta gene-level retrieval reports present.
- 39/39 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral arginine/proline boundary module created and validated:
  `modules/arginine_proline_metabolism.yaml`.
- Falcon generic module research is still outstanding:
  `modules/arginine_proline_metabolism-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__arginine_proline_metabolism__ppu00330-deep-research-falcon.md`.
  Both real commands were reattempted on 2026-07-10 PDT and failed before
  report creation with Edison HTTP 402 Payment Required.
- Validation complete for all 39 candidate gene reviews and the module.
  Remaining warnings are non-blocking: Asta-citation notices, broad core
  functions on generic oxidoreductase/transaminase side-node candidates whose
  current GOA lacks the exact MF row, the no-core-function warning for no-GOA
  `PP_2932`, and an inherited `PP_4983` process-reflection warning.
- Gene review pages rendered for all 39 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/arginine_proline_metabolism.yaml
uv run python -m ai_gene_review.validation.module_validator modules/arginine_proline_metabolism.yaml
```

Main curation conclusions from this batch:

- KEGG `ppu00330` is a broad boundary map. It should not be interpreted as a
  single strict pathway; it combines proline biosynthesis/catabolism,
  succinylated arginine catabolism, agmatine/putrescine/polyamine metabolism,
  opine and 2-ketoarginine side chemistry, 5-oxoproline turnover, creatinine
  chemistry, and generic oxidoreductase/aminotransferase spillovers.
- Proline biosynthesis/interconversion is covered by `proB`, `proA`, `proC`,
  `proI`, and `ocd__Q88H32`. `putA` remains the proline
  catabolism/regulation boundary review from the earlier ppu00250 batch.
- The Ast arginine-catabolic route is represented by `astA-I`, `astA-II`,
  `astB`, boundary `argD`, `astD`, and `astE`; this is separate from strict
  acetylated arginine biosynthesis.
- Agmatine, putrescine, and polyamine context is split across `aguA`, `speA`,
  `speB`, `speC`, `nspC`, `PP_4523`, and `spuC-II`.
- `aguA` now modifies the stale `GO:0004668` annotation to current agmatine
  deiminase `GO:0047632`.
- `nspC` removes the propagated diaminopimelate decarboxylase transfer and keeps
  broad carboxy-lyase/norspermidine biosynthesis pending a more specific GO MF
  term for carboxynorspermidine/carboxyspermidine decarboxylase.
- `spuC-II` removes biotin-biosynthesis aminotransferase transfers and is kept
  as a polyamine:pyruvate transaminase candidate pending a better specific GO
  term.
- `aruI` removes acetolactate synthase, valine biosynthesis, complex, and FAD
  binding transfers, retaining the 5-guanidino-2-oxopentanoate decarboxylase
  role.
- `ldcC` is treated as a lysine decarboxylase boundary node, not as a core
  arginine decarboxylase.
- `oplA`/`oplB`, `pip`, `creA`, `ooxA`/`ooxB`, `PP_2588`, `PP_2589`,
  `PP_3146`, `PP_4548`, `PP_5273`, `kauB`, `patD`, `prr`, `codA`, and
  `PP_4983` remain boundary or side-node context unless future module-level
  evidence narrows their physiological role.

## Batch status: UPA00098 / arginine_proline_metabolism

Batch files:

- `projects/P_PUTIDA/batches/UPA00098_arginine_proline_metabolism.tsv`
- `projects/P_PUTIDA/batches/UPA00098_arginine_proline_metabolism.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 5 candidates curated: all UniPathway `UPA00098` membership genes (`proB`,
  `ocd__Q88H32`, `proC`, `proA`, and `proI`).
- 5/5 candidate review folders present.
- 5/5 candidate Asta gene-level retrieval reports present.
- 5/5 review YAMLs curated with no remaining `PENDING` actions.
- Existing arginine/proline module reused and updated:
  `modules/arginine_proline_metabolism.yaml`.
- The proline biosynthesis/interconversion part now explicitly includes
  `proA` and `proC` alongside the previously modeled `proB`, `proI`, and
  `ocd__Q88H32` entries.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/arginine_proline_metabolism-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__arginine_proline_metabolism__upa00098-deep-research-falcon.md`.
- The taxon-aware Falcon command resolved the correct local candidate set:
  `proB`, `ocd__Q88H32`, `proC`, `proA`, and `proI`.
- Validation complete for all five gene reviews and the module. Each gene
  review reports the existing non-blocking Asta-citation warning.
- Gene review pages rendered for all five candidates.
- Module page rendered:
  `pages/modules/arginine_proline_metabolism.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/arginine_proline_metabolism.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/arginine_proline_metabolism.yaml
```

Main curation conclusions from this support batch:

- PSEPK `UPA00098` is a proline biosynthesis/interconversion support bucket
  inside the existing arginine/proline boundary module, not a new standalone
  module.
- `proB` and `proA` route glutamate toward glutamate-5-semialdehyde/P5C.
- `proC` and `proI` reduce pyrroline-5-carboxylate to L-proline.
- `ocd__Q88H32` supplies the ornithine cyclodeaminase route from ornithine to
  proline.

## Batch status: UPA00117 / l_carnitine_dehydrogenation

Batch files:

- `projects/P_PUTIDA/batches/UPA00117_l_carnitine_dehydrogenation.tsv`
- `projects/P_PUTIDA/batches/UPA00117_l_carnitine_dehydrogenation.md`

Status as of 2026-07-09 PDT:

- 1 candidate curated: UniPathway `UPA00117` member `lcdH`.
- 1/1 candidate review folder present.
- 1/1 candidate Asta gene-level retrieval report present.
- 1/1 review YAML curated with no remaining `PENDING` actions.
- The initial one-reaction module seed was retired under the multi-part module
  policy; the gene and pathway curation remain recorded in this batch.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/l_carnitine_dehydrogenation-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__l_carnitine_dehydrogenation__upa00117-deep-research-falcon.md`.
- Validation complete for the gene review. The former one-part module passed
  validation before retirement; no standalone ModuleReview or page is retained.
- Gene review page rendered for `lcdH`.

Main curation conclusions from this batch:

- PSEPK `UPA00117` is satisfiable as a single L-carnitine dehydrogenation
  reaction catalyzed by LcdH.
- `lcdH` is a cytoplasmic NAD+-dependent L-carnitine dehydrogenase that
  oxidizes L-carnitine to 3-dehydrocarnitine.
- The exact molecular-function annotation GO:0047728, carnitine metabolism and
  catabolism process annotations, and cytoplasmic localization were accepted.
- Broad oxidoreductase and NAD-binding terms were retained as non-core cofactor
  context.
- The InterPro-derived GO:0006631 fatty acid metabolic process annotation was
  marked over-annotated because the local evidence supports carnitine
  metabolism rather than direct fatty-acid metabolism.
- Carnitine uptake and downstream 3-dehydrocarnitine utilization remain module
  gaps until a later batch connects specific transporter or catabolic genes.

## Batch status: ppu00332 / carbapenem_biosynthesis_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00332_carbapenem_biosynthesis_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00332_carbapenem_biosynthesis_boundary.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 2 candidates curated: all KEGG `ppu00332` membership genes (`proB` and
  `proA`).
- 2/2 candidate review folders present.
- 2/2 candidate Asta gene-level retrieval reports present.
- 2/2 review YAMLs curated with no remaining `PENDING` actions.
- Species-neutral boundary/absence module created and validated:
  `modules/carbapenem_biosynthesis_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/carbapenem_biosynthesis_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__carbapenem_biosynthesis_boundary__ppu00332-deep-research-falcon.md`.
- Validation complete for both gene reviews and the module. The only gene-review
  warnings are Asta-citation notices inherited from the first-pass review style.
- Gene review pages rendered for both candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/carbapenem_biosynthesis_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/carbapenem_biosynthesis_boundary.yaml
```

Main curation conclusions from this batch:

- KEGG `ppu00332` contains only `proB` and `proA` in PSEPK.
- `proB` and `proA` are ordinary proline-biosynthesis precursor enzymes already
  curated in the ppu00330 arginine/proline batch.
- This batch should be interpreted as pathway absence/boundary context, not as
  evidence that KT2440 has a complete carbapenem antibiotic biosynthesis module.

## Batch status: ppu00350 / tyrosine_catabolism

Batch files:

- `projects/P_PUTIDA/batches/ppu00350_tyrosine_catabolism.tsv`
- `projects/P_PUTIDA/batches/ppu00350_tyrosine_catabolism.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 16 candidates curated: all KEGG `ppu00350` membership genes.
- 16/16 candidate review folders present.
- 16/16 candidate Asta gene-level retrieval reports present.
- 16/16 review YAMLs curated with no remaining `PENDING` actions.
- Existing species-neutral module updated and validated:
  `modules/tyrosine_catabolism.yaml`.
- Falcon generic module research is still outstanding:
  `modules/tyrosine_catabolism-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__tyrosine_catabolism__ppu00350-deep-research-falcon.md`.
- Validation complete for all 16 gene reviews and the module. Remaining
  gene-review warnings are non-blocking first-pass caveats, mostly Asta
  retrieval files that were present but not used as direct evidence because they
  did not retrieve gene-specific support.
- Gene review pages rendered for all 16 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/tyrosine_catabolism.yaml
uv run python -m ai_gene_review.validation.module_validator modules/tyrosine_catabolism.yaml
```

Main curation conclusions from this batch:

- KEGG `ppu00350` is a broad tyrosine-metabolism map. For PSEPK curation it
  should be read as the homogentisate aromatic-amino-acid catabolism module plus
  side-node chemistry, not as one strict pathway.
- The committed homogentisate route is covered by aromatic aminotransferase
  context (`tyrB`, `amaC`, and related paralogs), `hpd`, `hmgA`, `hmgC`, and
  `hmgB`.
- `hmgC` is curated as maleylacetoacetate isomerase and now has a `NEW`
  `GO:0006572` L-tyrosine catabolic process recommendation, since GOA captured
  phenylalanine catabolism but omitted the parallel tyrosine route.
- `hmgB` is the fumarylacetoacetase step. `PP_1709` remains a FAH-family
  acetylpyruvate-hydrolase candidate and should not be used to satisfy the
  terminal homogentisate-pathway step without new evidence.
- `PP_2552` is a PLP-dependent aromatic-L-amino-acid/DOPA decarboxylase side
  node. `peaE`, `davD`, `sad-I`, `gabD-II`, `frmA`, and `adhP` are aldehyde or
  alcohol dehydrogenase boundary nodes. `PP_4983` remains auxin/tryptophan
  2-monooxygenase context rather than a committed tyrosine-catabolic enzyme.

## Batch status: ppu00360 / phenylalanine_metabolism

Batch files:

- `projects/P_PUTIDA/batches/ppu00360_phenylalanine_metabolism.tsv`
- `projects/P_PUTIDA/batches/ppu00360_phenylalanine_metabolism.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 28 candidates curated: all KEGG `ppu00360` membership genes.
- 28/28 candidate review folders present.
- 28/28 candidate Asta gene-level retrieval reports present.
- 28/28 review YAMLs curated with no remaining `PENDING` actions.
- New broad species-neutral module created and validated:
  `modules/phenylalanine_metabolism.yaml`.
- Falcon generic module research is still outstanding:
  `modules/phenylalanine_metabolism-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__phenylalanine_metabolism__ppu00360-deep-research-falcon.md`.
- Validation complete for all 28 gene reviews and the module. Remaining
  gene-review warnings are non-blocking first-pass caveats: Asta retrieval
  files that were present but not used as direct evidence, existing
  boundary-gene no-core warnings, and an inherited `PP_4983`
  process-reflection warning.
- Gene review pages rendered for all 28 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/phenylalanine_metabolism.yaml
uv run python -m ai_gene_review.validation.module_validator modules/phenylalanine_metabolism.yaml
```

Main curation conclusions from this batch:

- KEGG `ppu00360` is a broad phenylalanine-metabolism map in PSEPK, not one
  linear module. It combines PhhA/homogentisate-route entry, the Paa
  phenylacetate degradation pathway, and several side-node enzymes.
- The core Paa phenylacetate branch is `paaK`, `paaA`, `paaB`, `paaC`, `paaD`,
  `paaE`, `paaG`, `paaZ`, `paaH`, `paaF`, and `paaI`.
- New process annotations were added conservatively for missing Paa pathway
  rows: `paaZ`, `paaD`, `paaB`, and `paaI` now have `NEW` `GO:0010124`
  phenylacetate catabolic process recommendations.
- `paaZ` is treated as a bifunctional lower-pathway enzyme. Current GO support
  only safely captures the aldehyde/oxo oxidoreductase half at a broad class
  level; exact GO terms for the PaaZ hydrolase/dehydrogenase half-reactions
  remain a curation/ontology question.
- `paaD` is kept as an accessory phenylacetate degradation enzyme subunit with
  no invented independent molecular function.
- `PP_3726` remains an unresolved enoyl-CoA hydratase/isomerase-family boundary
  gene, not a satisfier for a committed phenylalanine or phenylacetate step.
- `dadA1`, `dadA2`, and `PP_4311` are D-amino-acid dehydrogenase side nodes.
  `katG`, `peaE`, `amaC`, `PP_4983`, and several aminotransferase/dehydrogenase
  entries remain KEGG side or boundary context rather than strict ppu00360
  module members.

## Batch status: ppu00361 / chlorocyclohexane_chlorobenzene_degradation_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00361_chlorocyclohexane_chlorobenzene_degradation_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00361_chlorocyclohexane_chlorobenzene_degradation_boundary.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 3 candidates curated: all KEGG `ppu00361` membership genes.
- 3/3 candidate review folders present.
- 3/3 candidate Asta gene-level retrieval reports present.
- 3/3 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/chlorocyclohexane_chlorobenzene_degradation_boundary.yaml`.
- Falcon generic module research was attempted with the real command and failed
  before report generation while Edison Falcon access returns HTTP 402:
  `modules/chlorocyclohexane_chlorobenzene_degradation_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real command and
  failed before report generation while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__chlorocyclohexane_chlorobenzene_degradation_boundary__ppu00361-deep-research-falcon.md`.
- Validation complete for all 3 gene reviews and the module. The only
  remaining gene-review warning is the non-blocking `catA-II` Asta retrieval
  citation notice.
- Gene review pages rendered for all 3 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/chlorocyclohexane_chlorobenzene_degradation_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/chlorocyclohexane_chlorobenzene_degradation_boundary.yaml
```

Main curation conclusions from this batch:

- KEGG `ppu00361` is not satisfiable as a complete
  chlorocyclohexane/chlorobenzene degradation pathway in PSEPK based on the
  organism-specific membership.
- The three members are the lower catechol ortho-cleavage/beta-ketoadipate
  enzymes `catA`, `catA-II`, and `catB`.
- `catA` and `catA-II` satisfy catechol 1,2-dioxygenase activity
  (`GO:0018576`) and catechol-containing compound catabolism.
- `catB` satisfies muconate cycloisomerase activity (`GO:0018849`) and remains
  explicitly not curated as chloromuconate cycloisomerase; that over-transfer is
  already rejected in the gene review.
- This bucket should be tracked as chlorinated-aromatic map boundary/context,
  not as evidence for KT2440 chlorinated-aromatic upper-pathway capacity.

## Batch status: ppu00380 / tryptophan_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00380_tryptophan_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00380_tryptophan_metabolism_boundary.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 20 candidates curated: all KEGG `ppu00380` membership genes.
- 20/20 candidate review folders present.
- 20/20 candidate Asta gene-level retrieval reports present.
- 20/20 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/tryptophan_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/tryptophan_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__tryptophan_metabolism_boundary__ppu00380-deep-research-falcon.md`.
- Validation complete for all 20 gene reviews and the module. Remaining warnings
  are non-blocking: Asta retrieval citation notices, inherited `katA`/`PP_4983`
  process-reflection warnings, and the unresolved `PP_2932` no-core warning.
- Gene review pages rendered for all 20 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/tryptophan_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/tryptophan_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- KEGG `ppu00380` is a broad tryptophan-metabolism map in PSEPK, not one
  satisfiable dedicated route.
- Primary partition genes are `gcdH` and `katG`, with glutaryl-CoA
  dehydrogenase and catalase-peroxidase core functions rather than dedicated
  tryptophan pathway roles.
- `katE`, `katA`, and `PP_2887` are oxidative-stress/peroxide-detoxification
  boundary nodes.
- `PP_2887` is modified away from catalase activity to `GO:0004601` peroxidase
  activity and from hydrogen peroxide catabolism to cellular oxidant
  detoxification until substrate specificity is assayed.
- Remaining genes are CoA/lipoamide/beta-oxidation/aromatic side nodes or the
  unresolved `PP_2932` amidase-family boundary candidate.

## Batch status: ppu00401 / novobiocin_biosynthesis_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00401_novobiocin_biosynthesis_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00401_novobiocin_biosynthesis_boundary.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 4 candidates curated: all KEGG `ppu00401` membership genes.
- 4/4 candidate review folders present.
- 4/4 candidate Asta gene-level retrieval reports present.
- 4/4 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/novobiocin_biosynthesis_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/novobiocin_biosynthesis_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__novobiocin_biosynthesis_boundary__ppu00401-deep-research-falcon.md`.
- Validation complete for all 4 gene reviews and the module. Remaining warnings
  are non-blocking Asta retrieval citation notices on `tyrB` and `amaC`.
- Gene review pages rendered for all 4 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/novobiocin_biosynthesis_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/novobiocin_biosynthesis_boundary.yaml
```

Main curation conclusions from this batch:

- KEGG `ppu00401` is not satisfiable as a complete novobiocin aminocoumarin
  antibiotic biosynthesis route in PSEPK based on organism-specific membership.
- `hisC` is a histidinol-phosphate aminotransferase in L-histidine biosynthesis.
- `aroA` is the fused EPSP synthase / TyrA-like prephenate dehydrogenase
  supporting chorismate and tyrosine biosynthesis.
- `tyrB` and `amaC` are PLP-dependent aromatic amino acid aminotransferases.
- This bucket should be tracked as secondary-metabolite map boundary/absence
  context, not as evidence that KT2440 encodes a novobiocin biosynthesis gene
  cluster.

## Batch status: ppu00410 / beta_alanine_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00410_beta_alanine_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00410_beta_alanine_metabolism_boundary.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 15 candidates curated: all KEGG `ppu00410` membership genes.
- 15/15 candidate review folders present.
- 15/15 candidate Asta gene-level retrieval reports present.
- 15/15 review YAMLs curated with no remaining `PENDING` actions.
- New broad boundary module created and validated:
  `modules/beta_alanine_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/beta_alanine_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__beta_alanine_metabolism_boundary__ppu00410-deep-research-falcon.md`.
- Validation complete for all 15 gene reviews and the module. Remaining warnings
  are non-blocking Asta retrieval citation notices on older first-pass reviews.
- Gene review pages rendered for all 15 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/beta_alanine_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/beta_alanine_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- KEGG `ppu00410` is a broad beta-alanine metabolism map in PSEPK, not one narrow
  linear route.
- The beta-alanine-relevant spine is reductive pyrimidine catabolism and related
  beta-alanine release/context: `pydX`, `pydA`, `pydB`, `PP_0614`, and `hyuC`.
- `PP_0596` is the beta-alanine/omega-amino-acid transaminase node, and `panC`
  consumes beta-alanine in pantothenate biosynthesis.
- `mmsA-I` and `mmsA-II` are methylmalonate-semialdehyde dehydrogenase nodes that
  overlap valine, thymine, and propanoate side routes.
- `patD` and `prr` are aminobutyraldehyde/polyamine-side aldehyde
  dehydrogenases; `acd`, `fadB`, `PP_2217`, and `paaF` are acyl-CoA,
  fatty-acid beta-oxidation, or phenylacetate side nodes.
- The broad module should keep these contexts visible while avoiding annotation
  of every ppu00410 member as a committed beta-alanine pathway enzyme.

## Batch status: ppu00430 / taurine_hypotaurine_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00430_taurine_hypotaurine_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00430_taurine_hypotaurine_metabolism_boundary.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 5 candidates curated: all KEGG `ppu00430` membership genes.
- 5/5 candidate review folders present.
- 5/5 candidate Asta gene-level retrieval reports present.
- 5/5 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/taurine_hypotaurine_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/taurine_hypotaurine_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__taurine_hypotaurine_metabolism_boundary__ppu00430-deep-research-falcon.md`.
- Validation complete for all 5 gene reviews and the module. Remaining warnings
  are non-blocking Asta retrieval citation notices.
- Gene review pages rendered for all 5 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/taurine_hypotaurine_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/taurine_hypotaurine_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- TauD/AtsK is the pathway-defining ppu00430 enzyme in KT2440, supporting
  taurine dioxygenase activity and sulfur compound catabolism.
- `pta` is phosphate acetyltransferase and should be treated as acetate/acetyl-CoA
  side context.
- `gdhB` is NAD-specific glutamate dehydrogenase and should be treated as
  glutamate/2-oxoglutarate nitrogen-carbon side context.
- `PP_3535` and `ggt` are glutathione hydrolases and should be treated as
  glutathione/sulfur metabolism boundary context, not direct taurine enzymes.
- The module should not infer a complete dedicated taurine/hypotaurine route
  beyond the TauD desulfonation step without additional substrate-specific
  evidence.

## Batch status: ppu00440 / phosphonate_phosphinate_metabolism

Batch files:

- `projects/P_PUTIDA/batches/ppu00440_phosphonate_phosphinate_metabolism.tsv`
- `projects/P_PUTIDA/batches/ppu00440_phosphonate_phosphinate_metabolism.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 2 candidates curated: all KEGG `ppu00440` membership genes.
- 2/2 candidate review folders present.
- 2/2 candidate Asta gene-level retrieval reports present.
- 2/2 review YAMLs curated with no remaining `PENDING` actions.
- New compact module created and validated:
  `modules/phosphonate_phosphinate_metabolism.yaml`.
- Falcon generic module research is still outstanding:
  `modules/phosphonate_phosphinate_metabolism-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__phosphonate_phosphinate_metabolism__ppu00440-deep-research-falcon.md`.
- Validation complete for both gene reviews and the module.
- Gene review pages rendered for both candidates.
- 2026-07-08 extension: PP_0824-PP_0827 (`ptxB`, `phnC`, `phnE`, `ptxC`)
  from the partitioned `ppu02010` ABC-transporter map were added as a
  phosphonate import part in this module. All four transporter gene reviews
  validate warning-free.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/phosphonate_phosphinate_metabolism.yaml
uv run python -m ai_gene_review.validation.module_validator modules/phosphonate_phosphinate_metabolism.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00440` is represented by the PhnWX AEP catabolic route, not by a
  broad C-P lyase or phosphinate metabolism system.
- `phnW` is the upstream 2-aminoethylphosphonate:pyruvate transaminase that
  produces phosphonoacetaldehyde.
- `phnX` is the downstream Mg(2+)-dependent phosphonoacetaldehyde hydrolase that
  releases acetaldehyde and phosphate.
- The later PP_0824-PP_0827 transporter extension records phosphonate uptake
  context, but the exact transported substrate range and direct AEP handoff to
  PhnW remain a `KNOWLEDGE_GAP`.
- The `phnX` TreeGrafter DNA repair annotation is unsupported by the
  PhnX-specific UniProt/HAMAP/Rhea/GOA evidence and was removed.
- The `phnX` TreeGrafter phosphoglycolate phosphatase activity transfer was
  modified to the specific phosphonoacetaldehyde hydrolase activity already
  supported by UniProt/GOA.

## Batch status: ppu00450 / selenocompound_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00450_selenocompound_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00450_selenocompound_metabolism_boundary.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 12 candidates curated: all KEGG `ppu00450` membership genes.
- 12/12 candidate review folders present.
- 12/12 candidate Asta gene-level retrieval reports present.
- 12/12 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/selenocompound_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/selenocompound_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__selenocompound_metabolism_boundary__ppu00450-deep-research-falcon.md`.
- Validation complete for all 12 gene reviews and the module. Remaining warnings
  are non-blocking older side-node warnings: uncited Asta retrieval files,
  unreflected authored core-process terms, one PP_4348 location warning, and the
  known lack of a defined core function for candidate `PP_4637`.
- Gene review pages rendered for all 12 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/selenocompound_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/selenocompound_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00450` is a boundary map, not one broad committed
  selenocompound pathway.
- The selenium-specific spine is `selD` selenophosphate synthase followed by
  `selA` L-seryl-tRNA(Sec) selenium transferase.
- `selD` produces selenophosphate from selenide and ATP; `selA` uses
  selenophosphate to convert L-seryl-tRNA(Sec) to
  L-selenocysteinyl-tRNA(Sec).
- `metG` is canonical methionyl-tRNA synthetase and should remain translation
  boundary context unless selenium-analog substrate evidence is found.
- `cysD`/`cysNC`, `metB`, `mdeA`, `metH`, `metE`, `PP_4348`, `PP_4594`, and
  `PP_4637` should be treated as sulfate, cysteine, methionine,
  transsulfuration, or candidate sulfur-amino-acid side nodes.

## Batch status: ppu00460 / cyanoamino_acid_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00460_cyanoamino_acid_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00460_cyanoamino_acid_metabolism_boundary.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 7 candidates curated: all KEGG `ppu00460` membership genes.
- 7/7 candidate review folders present.
- 7/7 candidate Asta gene-level retrieval reports present.
- 7/7 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/cyanoamino_acid_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/cyanoamino_acid_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__cyanoamino_acid_metabolism_boundary__ppu00460-deep-research-falcon.md`.
- Validation complete for all 7 gene reviews and the module. Remaining warnings
  are non-blocking older side-node warnings on `glyA1`, `glyA2`, `ansA`,
  `PP_1160`, `PP_3535`, and `ggt`.
- Gene review pages rendered for all 7 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/cyanoamino_acid_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/cyanoamino_acid_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00460` is a boundary map, not a complete cyanogenic-glycoside or
  cyanoamino-acid detoxification route.
- `ansA` and `PP_1160` are the asparaginase-family anchors for the primary
  bucket.
- `glyA1` and `glyA2` are serine hydroxymethyltransferase one-carbon side nodes.
- `bglX` is a periplasmic beta-glucosidase/glucan-catabolism side node; no
  KT2440-specific cyanogenic-glycoside substrate evidence was found in the
  first pass.
- `PP_3535` and `ggt` are glutathione hydrolase side nodes already overlapping
  taurine/hypotaurine and glutathione metabolism.

## Batch status: ppu00470 / d_amino_acid_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00470_d_amino_acid_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00470_d_amino_acid_metabolism_boundary.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 21 candidates curated: all KEGG `ppu00470` membership genes.
- 21/21 candidate review folders present.
- 21/21 candidate Asta gene-level retrieval reports present.
- 21/21 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/d_amino_acid_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/d_amino_acid_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__d_amino_acid_metabolism_boundary__ppu00470-deep-research-falcon.md`.
- Validation complete for all 21 gene reviews and the module. Remaining
  warnings are non-blocking older Asta-citation warnings on carried-forward
  side-node reviews.
- Gene review pages rendered for all 21 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/d_amino_acid_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/d_amino_acid_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00470` is a boundary map spanning several D-amino-acid-associated
  contexts, not a single committed D-amino-acid catabolic pathway.
- `murI`, `murD`, `ddlA`, `ddlB`, `dadX`, and `alr` are the peptidoglycan
  D-Glu/D-Ala and alanine-racemase chemistry.
- `dadA1`, `dadA2`, `PP_4311`, and `dauA` are D-amino-acid or D-arginine
  dehydrogenase/oxidoreductase context.
- `proR`, `PP_1255`, `PP_1257`, `PP_1256`, `PP_2585`, and `PP_3602` are
  hydroxyproline/dioxovalerate side-route nodes.
- `dapF__Q88GD4`, `dapF__Q88CF3`, `lysA-I`, `lysA-II`, and `ansB` are
  diaminopimelate/lysine biosynthesis or asparaginase side nodes.
- First-pass review fixes narrowed broad racemase, ligase, lyase, and catalytic
  terms where specific functions were available, retained cofactor/location
  annotations as non-core, and added conservative oxidoreductase function for
  `PP_1255` and `dauA`.

## Batch status: ppu00480 / glutathione_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00480_glutathione_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00480_glutathione_metabolism_boundary.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 31 candidates curated: all KEGG `ppu00480` membership genes.
- 31/31 candidate review folders present.
- 31/31 candidate Asta gene-level retrieval reports present.
- 31/31 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/glutathione_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/glutathione_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__glutathione_metabolism_boundary__ppu00480-deep-research-falcon.md`.
- Validation complete for all 31 gene reviews and the module.
- Gene review pages rendered for all 31 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/glutathione_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/glutathione_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00480` is a broad glutathione-metabolism boundary map, not a single
  linear pathway.
- Glutathione biosynthesis and recycling are covered by `gshA`, `gshB`,
  PP_3253, and `gor`; glutathione turnover/catabolism is represented by
  PP_3535, `ggt`, PP_5211, plus `pxpA1`/`pxpA2` 5-oxoproline salvage context.
- GST-family detoxification and peroxide-detoxification nodes are distinct from
  the biosynthetic/recycling spine. These include PP_0183, `gstA`, PP_1347,
  PP_1821, `gstB`, PP_2474, PP_2536, PP_0777, PP_1686, `gpx`, and PP_2700.
- `zwfA`, `zwfB`, `zwf`, `gntZ`, `icd`, and `idh` are retained as NADPH-supply
  side context rather than glutathione-specific enzymes.
- `pepA` and `pepN` are aminopeptidase side nodes, and `speC`, `ptxD`, and
  `ybgJ` are KEGG spillovers or adjacent context.
- First-pass review fixes removed carbohydrate-metabolism over-propagation from
  `pxpA1`/`pxpA2`, narrowed broad catalytic/ligase terms for `gshB` and
  PP_3253, represented PP_2700 as glutathione-dependent peroxidase chemistry
  rather than the thioredoxin-specific automated term, and kept cofactors and
  locations as non-core annotations.

## Batch status: ppu00500 / starch_sucrose_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00500_starch_sucrose_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00500_starch_sucrose_metabolism_boundary.md`

Status as of 2026-07-07 PDT / 2026-07-07 UTC:

- 18 candidates curated: all KEGG `ppu00500` membership genes.
- 18/18 candidate review folders present.
- 18/18 candidate Asta gene-level retrieval reports present.
- 18/18 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/starch_sucrose_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/starch_sucrose_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__starch_sucrose_metabolism_boundary__ppu00500-deep-research-falcon.md`.
- Validation complete for all 18 gene reviews and the module.
- Gene review pages rendered for all 18 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/starch_sucrose_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/starch_sucrose_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00500` is a bacterial glycogen/alpha-glucan boundary map, not a
  plant-like starch/sucrose pathway.
- The glycogen/alpha-glucan core is covered by `glgA`, `glgB`, `glgX`, `glgP`,
  `malQ`, `treY`, `treZ`, `treSB`, and `glgE`, spanning ADP-glucose glycogen
  synthesis, branching/debranching, phosphorylase catabolism, maltooligosyl
  trehalose chemistry, and the TreS/GlgE maltose-1-phosphate route.
- `bcsA` is the cellulose synthase node, while `glk`, `pgi1`, `pgi2`, `pgm`,
  `galU`, `algC`, and `cpsG` are shared sugar-phosphate, UDP-glucose, alginate,
  or galactose-context enzymes. `bglX` is beta-glucosidase/cellobiose side
  context.
- First-pass review fixes changed `glgA` away from the wrong UDP-glucose-donor
  term to ADP-glucose glycogen synthase activity, removed GH13 hydrolase
  over-propagation from transferase enzymes `glgB` and `glgE`, kept
  carbohydrate/location/cofactor annotations as non-core, and recorded the need
  for a more specific GlgE maltosyltransferase MF term if GO supports one.

## Batch status: ppu00520 / amino_sugar_nucleotide_sugar_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00520_amino_sugar_nucleotide_sugar_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00520_amino_sugar_nucleotide_sugar_metabolism_boundary.md`

Status as of 2026-07-07 PDT / 2026-07-08 UTC:

- 25 candidates curated: all KEGG `ppu00520` membership genes.
- 25/25 candidate review folders present.
- 25/25 candidate Asta gene-level retrieval reports present.
- 25/25 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/amino_sugar_nucleotide_sugar_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/amino_sugar_nucleotide_sugar_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__amino_sugar_nucleotide_sugar_metabolism_boundary__ppu00520-deep-research-falcon.md`.
- Validation complete for all 25 gene reviews and the module.
- Gene review pages rendered for all 25 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/amino_sugar_nucleotide_sugar_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/amino_sugar_nucleotide_sugar_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00520` is a composite amino-sugar and nucleotide-sugar boundary map,
  not a single linear pathway.
- UDP-GlcNAc biosynthesis is covered by `glmS`, `glmM`, and `glmU`.
- De novo peptidoglycan precursor formation is represented by `murA` and
  `murB`; the MurNAc/peptidoglycan recycling shortcut is represented by
  `nagZ`, `mupP`, `anmK`, `amgK`, and `murU`.
- `rfbA`, `rffE`, `galE`, `galU`, and `udg` are nucleotide-sugar side branches,
  while `algA`, `algD`, `algC`, `cpsG`, `glk`, `pgi1`, `pgi2`, `pgm`,
  PP_0501, and PP_1776 are shared carbohydrate or alginate/GDP-mannose context.
- First-pass review fixes removed the UDP-N-acetylgalactosamine process
  over-propagation from `murA`, removed phosphoglucomutase and
  phosphomannomutase spillovers from `glmM`, narrowed broad catalytic/hydrolase
  terms for `murA`, `rffE`, `nagZ`, and `glmM`, and retained cofactor and
  localization annotations as non-core. `rfbA` had to be fetched by accession
  Q88LZ3 because symbol lookup did not resolve it.

## Batch status: ppu00523 / polyketide_sugar_unit_biosynthesis_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00523_polyketide_sugar_unit_biosynthesis_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00523_polyketide_sugar_unit_biosynthesis_boundary.md`

Status as of 2026-07-07 PDT / 2026-07-08 UTC:

- 6 candidates curated: all KEGG `ppu00523` membership genes.
- 6/6 candidate review folders present.
- 6/6 candidate Asta gene-level retrieval reports present.
- 6/6 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/polyketide_sugar_unit_biosynthesis_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/polyketide_sugar_unit_biosynthesis_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__polyketide_sugar_unit_biosynthesis_boundary__ppu00523-deep-research-falcon.md`.
- Validation complete for all 6 gene reviews and the module.
- Gene review pages rendered for all 6 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/polyketide_sugar_unit_biosynthesis_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/polyketide_sugar_unit_biosynthesis_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00523` is a dTDP-deoxy-sugar/dTDP-rhamnose boundary map, not
  evidence for a complete polyketide natural-product sugar-unit biosynthesis
  pathway in KT2440.
- `rfbA` supplies glucose-1-phosphate thymidylyltransferase activity to make
  dTDP-glucose; `rffG` supplies dTDP-glucose 4,6-dehydratase activity upstream
  of the dTDP-4-dehydro-6-deoxyglucose intermediate.
- `rmlC` and `rfbC` are duplicate dTDP-4-dehydrorhamnose 3,5-epimerase
  candidates, while `PP_0500` and `rfbD` are duplicate
  dTDP-4-dehydrorhamnose reductase candidates. Which paralog pair carries the
  dominant flux in each envelope-glycan context remains an open question.
- Generic racemase/epimerase parent annotations on `rmlC` and `rfbC` were
  marked as over-annotated because the specific epimerase activity is present.
  Cytosol, broad polysaccharide, O-antigen, and nucleotide-sugar process
  annotations were retained as non-core context where appropriate.
- `rmlC` and `rfbD` had to be fetched by accession Q88R69 and Q88LZ2 because
  symbol lookup did not resolve their UniProt entries.

## Batch status: ppu00525 / acarbose_validamycin_biosynthesis_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00525_acarbose_validamycin_biosynthesis_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00525_acarbose_validamycin_biosynthesis_boundary.md`

Status as of 2026-07-07 PDT / 2026-07-08 UTC:

- 2 candidates curated: all KEGG `ppu00525` membership genes.
- 2/2 candidate review folders present.
- 2/2 candidate Asta gene-level retrieval reports present.
- 2/2 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/acarbose_validamycin_biosynthesis_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/acarbose_validamycin_biosynthesis_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__acarbose_validamycin_biosynthesis_boundary__ppu00525-deep-research-falcon.md`.
- Validation complete for both gene reviews and the module.
- Gene review pages rendered for both candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/acarbose_validamycin_biosynthesis_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/acarbose_validamycin_biosynthesis_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00525` is a boundary/absence map, not evidence for a complete
  acarbose, validamycin, or aminocyclitol antibiotic biosynthesis pathway in
  KT2440.
- `rfbA` supplies glucose-1-phosphate thymidylyltransferase activity to make
  dTDP-glucose; `rffG` supplies dTDP-glucose 4,6-dehydratase activity in
  deoxy-sugar nucleotide metabolism.
- No additional gene-level edits were needed for this batch because `rfbA` and
  `rffG` were already curated in adjacent nucleotide-sugar batches.

## Batch status: ppu00540 / lipopolysaccharide_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/ppu00540_lipopolysaccharide_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/ppu00540_lipopolysaccharide_biosynthesis.md`

Status as of 2026-07-07 PDT / 2026-07-08 UTC:

- 20 candidates curated: all KEGG `ppu00540` membership genes.
- 20/20 candidate review folders present.
- 20/20 candidate Asta gene-level retrieval reports present.
- 20/20 review YAMLs curated with no remaining `PENDING` actions.
- New LPS/lipid A module created and validated:
  `modules/lipopolysaccharide_biosynthesis.yaml`.
- Falcon generic module research is still outstanding:
  `modules/lipopolysaccharide_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__lipopolysaccharide_biosynthesis__ppu00540-deep-research-falcon.md`.
- Validation complete for all 20 gene reviews and the module.
- Gene review pages rendered for all 20 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/lipopolysaccharide_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/lipopolysaccharide_biosynthesis.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00540` is a combined LPS/lipid A batch rather than a single linear
  pathway. The curated module separates lipid IVA/lipid A biosynthesis,
  Kdo2-lipid A formation, LPS core oligosaccharide assembly, and lipid A/LPS
  remodeling side nodes.
- Lipid A precursor biosynthesis is represented by `lpxA`, `lpxC`, `lpxD`,
  `lpxH`, `lpxB`, and `lpxK`.
- Kdo2-lipid A formation and late acylation are represented by `waaA`,
  `htrB`/`lpxL`, and candidate lipid A acyltransferase `PP_0063`.
- LPS core assembly is represented by `waaC`, `waaF`, `waaG`, and `waaP`.
- Remodeling or unresolved side nodes are represented by `pagL-I`, `pagL-II`,
  `yijP`, `PP_0024`, `PP_4592`, `lpxOA`, and `PP_4570`.
- Broad membrane, cofactor, hydrolase, glycosyltransferase, transferase, and
  acyltransferase parent terms were retained as non-core or marked
  over-annotated when a more specific enzyme term was available. `lpxK`'s LPS
  core-region process annotation was marked over-annotated in favor of lipid A
  biosynthesis, and first-pass UniProt-backed `NEW` annotations were added for
  `PP_0063`, `lpxOA`, and `PP_4570`.

## Batch status: ppu00541 / nucleotide_sugar_biosynthesis_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00541_nucleotide_sugar_biosynthesis_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00541_nucleotide_sugar_biosynthesis_boundary.md`

Status as of 2026-07-07 PDT / 2026-07-08 UTC:

- 26 candidates curated: all KEGG `ppu00541` membership genes.
- 26/26 candidate review folders present.
- 26/26 candidate Asta gene-level retrieval reports present.
- 26/26 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/nucleotide_sugar_biosynthesis_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/nucleotide_sugar_biosynthesis_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__nucleotide_sugar_biosynthesis_boundary__ppu00541-deep-research-falcon.md`.
- Validation complete for all 26 gene reviews and the module.
- Gene review pages rendered for all 26 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/nucleotide_sugar_biosynthesis_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/nucleotide_sugar_biosynthesis_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00541` is a composite nucleotide-sugar boundary map, not a single
  linear pathway.
- ADP-heptose/LPS-core precursor chemistry is represented by `gmhA`, `hldE`,
  and `gmhB`.
- Kdo/CMP-Kdo chemistry is represented by `kdsD`, `PP_1806`, `kdsA1`,
  `kdsA2`, `kdsC`, and `kdsB`; paralog dominance for the API and KdsA pairs
  remains unresolved.
- dTDP-rhamnose/deoxy-sugar chemistry is represented by `rfbA`, `rffG`,
  `rmlC`, `rfbC`, `PP_0500`, and `rfbD`.
- GDP/UDP sugar branches and shared precursor context are represented by
  `algA`, `PP_1776`, `gmd`, `rmd`, `galU`, `udg`, `glmU`, and `rffE`.
- `wbpV`, `wbpM`, and `PP_5212` remain unresolved polysaccharide/redox side
  nodes with no specific first-pass substrate assignment.
- `kdsC`'s CMP-sialic-acid cytidylyltransferase annotation was removed as a
  likely wrong spillover. Broad parent process, cofactor, catalytic, and
  localization terms were kept non-core or marked over-annotated where a
  specific enzyme term was available.

## Batch status: ppu00543 / exopolysaccharide_biosynthesis_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00543_exopolysaccharide_biosynthesis_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00543_exopolysaccharide_biosynthesis_boundary.md`

Status as of 2026-07-08 UTC:

- 11 candidates curated: all KEGG `ppu00543` membership genes.
- 11/11 candidate review folders present.
- 11/11 candidate Asta gene-level retrieval reports present.
- 11/11 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/exopolysaccharide_biosynthesis_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/exopolysaccharide_biosynthesis_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__exopolysaccharide_biosynthesis_boundary__ppu00543-deep-research-falcon.md`.
- Validation complete for all 11 gene reviews and the module.
- Gene review pages rendered for all 11 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/exopolysaccharide_biosynthesis_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/exopolysaccharide_biosynthesis_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00543` is an exopolysaccharide/alginate boundary map, not one
  complete polysaccharide pathway.
- The alginate production core in this batch is represented by `alg8` alginate
  synthase and `alg44` cyclic-di-GMP-binding alginate production factor.
- Alginate O-acetylation/modification context is represented by `algF`, `algJ`,
  `algI`, and `algX`. `algJ` and `algX` received first-pass `NEW` broad
  acyltransferase annotations from UniProt because the fetched GOA block did
  not include the molecular-function line.
- `PP_2124` remains an unresolved glycosyltransferase candidate; its broad
  glycosyltransferase activity was accepted, while its TreeGrafter LPS
  biosynthetic process annotation was marked over-annotated pending substrate
  evidence.
- `PP_0228`, `cysE`, `PP_1110`, and `PP_3136` are serine
  O-acetyltransferase/cysteine-biosynthesis spillovers rather than core
  exopolysaccharide biosynthesis genes.

## Batch status: UPA00286 / alginate_biosynthesis_boundary

Batch files:

- `projects/P_PUTIDA/batches/UPA00286_alginate_biosynthesis_boundary.tsv`
- `projects/P_PUTIDA/batches/UPA00286_alginate_biosynthesis_boundary.md`

Status as of 2026-07-09 PDT:

- 11 UniPathway `UPA00286` members curated: `algB`, `algF`, `algJ`, `algI`,
  `algX`, `algG`, `algE`, `algK`, `alg44`, `alg8`, and `algD`.
- 11/11 candidate review folders present.
- 11/11 candidate Asta gene-level retrieval reports present; missing `algE`
  and `algK` Asta reports were added during this pass.
- 11/11 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/alginate_biosynthesis_boundary.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/alginate_biosynthesis_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted and failed while Edison
  Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__alginate_biosynthesis_boundary__upa00286-deep-research-falcon.md`.
- Validation complete for all 11 gene reviews and the module.
- Gene review pages rendered for all 11 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/alginate_biosynthesis_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/alginate_biosynthesis_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `UPA00286` is satisfiable as a trans-envelope alginate
  biosynthesis/export/regulatory boundary.
- `algD` supplies GDP-mannuronate precursor formation from the
  fructose/mannose-metabolism side, while `alg8` and `alg44` represent
  polymerization and cyclic-di-GMP-linked activation.
- `algF`, `algJ`, `algI`, `algX`, and `algG` represent alginate
  modification/maturation, including O-acetylation context and mannuronan
  C5-epimerase activity.
- `algE` and `algK` are UniPathway-primary export/scaffold context genes, not
  missing members of the KEGG `ppu00543` bucket.
- `algB` is regulatory context for alginate production rather than a catalytic
  biosynthesis step.
- The source memberships are split across `ppu00051`, `ppu00543`, `ppu02020`,
  and UniPathway-only assignments; keeping a dedicated UPA00286 module avoids
  forcing the full operon/regulatory/export boundary into fructose/mannose
  metabolism or the broader exopolysaccharide boundary.

## Batch status: ppu00550 / peptidoglycan_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/ppu00550_peptidoglycan_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/ppu00550_peptidoglycan_biosynthesis.md`

Status as of 2026-07-08 UTC:

- 24 candidates curated: all KEGG `ppu00550` membership genes plus promoted
  `murJ` from UniPathway UPA00219.
- 24/24 candidate review folders present.
- 24/24 candidate Asta gene-level retrieval reports present.
- 24/24 review YAMLs curated with no remaining `PENDING` actions.
- New peptidoglycan module created and validated:
  `modules/peptidoglycan_biosynthesis.yaml`.
- Falcon generic module research is still outstanding:
  `modules/peptidoglycan_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__peptidoglycan_biosynthesis__ppu00550-deep-research-falcon.md`.
- Validation complete for all 24 gene reviews and the module.
- Gene review pages rendered for all 24 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/peptidoglycan_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/peptidoglycan_biosynthesis.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00550` covers peptidoglycan precursor synthesis, lipid-linked
  precursor assembly/recycling, lipid II flipping, polymerization,
  transpeptidation, and remodeling rather than a single enzyme class.
- Cytosolic UDP-MurNAc-peptide precursor assembly is represented by `murA`,
  `murB`, `murC`, `murD`, `murE`, `murF`, `ddlA`, and `ddlB`.
- Lipid-carrier and lipid I/lipid II assembly or recycling is represented by
  `uppS`, `uppP`, `mraY`, and `murG`.
- `murJ` was promoted from UniPathway because lipid II flipping is expected for
  peptidoglycan biosynthesis but absent from the KEGG `ppu00550` membership.
- SEDS-family polymerases are represented by septal `ftsW` and elongation
  `mrdB`/`rodA`; their lipid-linked peptidoglycan transporter annotations were
  removed as over-propagated computational assignments.
- Class A PBPs/glycosyltransferases are represented by `mrcA`, `mrcB`, `pbpC`,
  and `mtgA`; class B PBPs/transpeptidases are represented by `ftsI`,
  `mrdA-I`, and `mrdA-II`.
- `dacA` and `dacB` are carboxypeptidase/remodeling nodes. `ftsI`'s
  glycosyltransferase annotation and the MrdA L,D-transpeptidase annotations
  were removed because the local evidence supports D,D-transpeptidase/PBP
  chemistry.
- `uppP` received a first-pass `NEW` peptidoglycan biosynthetic process lead
  from UniProt because the fetched GOA rows omitted the process context.

## Batch status: ppu00552 / teichoic_acid_biosynthesis_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00552_teichoic_acid_biosynthesis_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00552_teichoic_acid_biosynthesis_boundary.md`

Status as of 2026-07-08 UTC:

- 2 candidates curated: all KEGG `ppu00552` membership genes.
- 2/2 candidate review folders present.
- 2/2 candidate Asta gene-level retrieval reports present.
- 2/2 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/teichoic_acid_biosynthesis_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/teichoic_acid_biosynthesis_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__teichoic_acid_biosynthesis_boundary__ppu00552-deep-research-falcon.md`.
- Validation complete for both gene reviews and the module.
- Gene review pages rendered for both candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/teichoic_acid_biosynthesis_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/teichoic_acid_biosynthesis_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00552` is a teichoic-acid boundary/absence batch, not evidence for
  a complete Gram-positive wall or lipoteichoic-acid biosynthesis pathway in
  KT2440.
- `uppP` is shared undecaprenyl-diphosphatase/BacA carrier recycling and should
  be read as cell-envelope/peptidoglycan context rather than
  teichoic-acid-specific pathway evidence.
- `wbpM` remains an unresolved polysaccharide-biosynthesis/CapD-like membrane
  protein with no specific molecular-function GOA row and no assigned core
  function.

## Batch status: ppu00561 / glycerolipid_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00561_glycerolipid_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00561_glycerolipid_metabolism_boundary.md`

Status as of 2026-07-08 UTC:

- 12 candidates curated: all KEGG `ppu00561` membership genes.
- 12/12 candidate review folders present.
- 12/12 candidate Asta gene-level retrieval reports present.
- 12/12 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/glycerolipid_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/glycerolipid_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__glycerolipid_metabolism_boundary__ppu00561-deep-research-falcon.md`.
- Validation complete for all 12 gene reviews and the module.
- Gene review pages rendered for all 12 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/glycerolipid_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/glycerolipid_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00561` is a broad glycerolipid/glycerophospholipid boundary map,
  not a single linear route.
- Core membrane-lipid precursor assembly is represented by `plsX`, `plsY`,
  `plsB`, `plsC`, `PP_0058`, `dgkA-I`, and `dgkA-II`.
- `plsX` supplies acyl-phosphate for the PlsY route and received a first-pass
  `NEW` phospholipid biosynthetic process lead from UniProt because the fetched
  GOA table omitted that process row.
- `glpK` supplies glycerol/glycerol-3-phosphate context but remains reviewed as
  glycerol catabolism rather than a dedicated membrane-lipid enzyme.
- `calA`, `garK`, `ttuD`, and `lip` are side or boundary nodes. `lip` remains
  an unreviewed alpha/beta-hydrolase candidate with no GOA terms and no assigned
  core function pending substrate evidence.

## Batch status: ppu00562 / inositol_phosphate_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00562_inositol_phosphate_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00562_inositol_phosphate_metabolism_boundary.md`

Status as of 2026-07-08 UTC:

- 4 candidates curated: all KEGG `ppu00562` membership genes.
- 4/4 candidate review folders present.
- 4/4 candidate Asta gene-level retrieval reports present.
- 4/4 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/inositol_phosphate_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/inositol_phosphate_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__inositol_phosphate_metabolism_boundary__ppu00562-deep-research-falcon.md`.
- Validation complete for all four gene reviews and the module.
- Gene review pages rendered for all four candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/inositol_phosphate_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/inositol_phosphate_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00562` is a boundary/absence map, not evidence for a complete
  phosphatidylinositol or inositol-polyphosphate signalling pathway in KT2440.
- `suhB` is the only direct inositol-phosphate enzyme in the KEGG candidate
  set. The review accepts inositol-monophosphatase activity and adds a
  first-pass `NEW` transcription antitermination lead from the UniProt rrnTAC
  function note.
- `suhB` signal-transduction context was marked over-annotated, and
  phosphatidylinositol dephosphorylation was removed as an over-propagated
  process annotation for this bacterial protein.
- `mmsA-I`, `mmsA-II`, and `tpiA` are side nodes from
  valine/thymine/propanoate metabolism and central-carbon metabolism rather
  than inositol-specific pathway enzymes.

## Batch status: ppu00564 / glycerophospholipid_metabolism

Batch files:

- `projects/P_PUTIDA/batches/ppu00564_glycerophospholipid_metabolism.tsv`
- `projects/P_PUTIDA/batches/ppu00564_glycerophospholipid_metabolism.md`

Status as of 2026-07-08 UTC:

- 23 candidates curated: all KEGG `ppu00564` membership genes.
- 23/23 candidate review folders present.
- 23/23 candidate Asta gene-level retrieval reports present.
- 23/23 review YAMLs curated with no remaining `PENDING` actions.
- New broad module created and validated:
  `modules/glycerophospholipid_metabolism.yaml`.
- Falcon generic module research is still outstanding:
  `modules/glycerophospholipid_metabolism-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__glycerophospholipid_metabolism__ppu00564-deep-research-falcon.md`.
- Validation complete for all 23 gene reviews and the module.
- Gene review pages rendered for all 23 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/glycerophospholipid_metabolism.yaml
uv run python -m ai_gene_review.validation.module_validator modules/glycerophospholipid_metabolism.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00564` is a broad glycerophospholipid metabolism map rather than a
  single linear pathway.
- Direct membrane-phospholipid chemistry is covered by the shared
  phosphatidic-acid precursor enzymes (`plsX`, `plsY`, `plsB`, `plsC`,
  `PP_0058`, `dgkA-I`, `dgkA-II`), CDP-DAG formation (`cdsA`),
  phosphatidylglycerol/cardiolipin branch genes (`pgsA`, `pgpA`, `clsA`,
  `clsB`, and candidate `PP_0892`), and PS/PE/PC branch genes (`pssA`,
  `PP_4677`, `psd`, `pcs`).
- `gpsA` and `glpD` are glycerol-3-phosphate precursor/catabolic context;
  `ugpQ` and `pchP` are headgroup-turnover or scavenging context; `eutB` and
  `eutC` are ethanolamine catabolism side nodes.
- `pchP` had no fetched GOA rows, so the review adds first-pass `NEW`
  phosphocholine phosphatase and phosphoethanolamine phosphatase activities from
  the UniProt EC 3.1.3.75 identity.
- PLD-family `PP_5276` remains substrate-unresolved: phosphatidyltransferase
  activity is retained, but cardiolipin biosynthetic process is `UNDECIDED`
  pending paralog/substrate evidence.

## Batch status: ppu00566 / sulfoquinovose_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00566_sulfoquinovose_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00566_sulfoquinovose_metabolism_boundary.md`

Status as of 2026-07-08 UTC:

- 2 candidates curated: all KEGG `ppu00566` membership genes.
- 2/2 candidate review folders present.
- 2/2 candidate Asta gene-level retrieval reports present.
- 2/2 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/sulfoquinovose_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/sulfoquinovose_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__sulfoquinovose_metabolism_boundary__ppu00566-deep-research-falcon.md`.
- Validation complete for both gene reviews and the module.
- Gene review pages rendered for both candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/sulfoquinovose_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/sulfoquinovose_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00566` is a boundary/absence map, not a complete sulfoquinovose
  degradation route.
- `mdh` is central-carbon/TCA malate dehydrogenase spillover in this KEGG map.
- `yihS` is unresolved at substrate level. KEGG assigns K18479 sulfoquinovose
  isomerase (EC 5.3.1.31), while UniProt/GOA assign aldose-ketose/mannose
  isomerase (EC 5.3.1.7; GO:0050089).
- The `yihS` review adds a first-pass `NEW` sulfoquinovose isomerase candidate
  annotation from KEGG notes, marks mannose isomerase `UNDECIDED`, and leaves no
  core function pending substrate assays.

## Batch status: ppu00592 / alpha_linolenic_acid_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00592_alpha_linolenic_acid_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00592_alpha_linolenic_acid_metabolism_boundary.md`

Status as of 2026-07-08 UTC:

- 2 candidates curated: all KEGG `ppu00592` membership genes.
- 2/2 candidate review folders present.
- 2/2 candidate Asta gene-level retrieval reports present.
- 2/2 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/alpha_linolenic_acid_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/alpha_linolenic_acid_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__alpha_linolenic_acid_metabolism_boundary__ppu00592-deep-research-falcon.md`.
- Validation complete for both gene reviews and the module.
- Gene review pages rendered for both candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/alpha_linolenic_acid_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/alpha_linolenic_acid_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00592` is a boundary/absence map, not a complete
  alpha-linolenic-acid-specific pathway.
- The only members are `fadA__Q88L84` and `fadA__Q88L01`, both already reviewed
  as FadA-like acetyl-CoA C-acyltransferase/thiolase enzymes in fatty-acid
  beta-oxidation.
- The batch should be interpreted as generic fatty-acid beta-oxidation side
  context, not as plant oxylipin or alpha-linolenate-specific metabolism.

## Batch status: ppu00620 / pyruvate_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00620_pyruvate_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00620_pyruvate_metabolism_boundary.md`

Status as of 2026-07-08 UTC:

- 54 candidates curated: all KEGG `ppu00620` membership genes.
- 54/54 candidate review folders present.
- 54/54 candidate Asta gene-level retrieval reports present.
- 54/54 review YAMLs curated with no remaining `PENDING` actions.
- New broad boundary module created and validated:
  `modules/pyruvate_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/pyruvate_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__pyruvate_metabolism_boundary__ppu00620-deep-research-falcon.md`.
- Validation complete for all 54 resolved gene reviews and the module.
- Gene review pages rendered for all 54 resolved review files.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/pyruvate_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/pyruvate_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00620` is a broad pyruvate-metabolism boundary map, not one
  satisfiable linear route.
- Direct pyruvate/lactate/glyoxalase nodes are covered by `PP_1389`
  oxaloacetate decarboxylase, `ldhA` NAD-dependent D-lactate dehydrogenase,
  `lldD` membrane L-lactate dehydrogenase, `dld2` FAD/iron-sulfur D-lactate
  dehydrogenase, and `gloA`/`gloB` glyoxalase I/II.
- `glcB`, `maeB`, `ppc`, `pycA`/`pycB`, `mdh`, MQO paralogs, fumarases, and
  thiolases are neighboring glyoxylate, malate/oxaloacetate, TCA, anaplerotic,
  beta-oxidation, or acetyl-CoA side context rather than dedicated pyruvate
  pathway members.
- `PP_1389` kept oxaloacetate decarboxylase as core and removed the
  TreeGrafter methylisocitrate lyase transfer. `lldD` was generalized away from
  the NAD+-specific L-lactate dehydrogenase term to the broader
  L-lactate-dehydrogenase activity, while `dld2` kept cytochrome-linked
  D-lactate dehydrogenase and removed the NAD+-specific D-lactate term.
- `PP_0772` remains unresolved: it is a metallo-beta-lactamase-family protein
  with no fetched GOA rows, so no glyoxalase II or other core function was
  assigned pending substrate assays.
- Alias handling remains important for this broad map: the `aldB-II` membership
  row resolves by accession to the existing `pedI` review, and `pedE` resolves
  to the existing `pede` review folder.

## Batch status: ppu00621 / dioxin_degradation_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00621_dioxin_degradation_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00621_dioxin_degradation_boundary.md`

Status as of 2026-07-08 UTC:

- 2 candidates curated: all KEGG `ppu00621` membership genes.
- 2/2 candidate review folders present.
- 2/2 candidate Asta gene-level retrieval reports present.
- 2/2 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/dioxin_degradation_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/dioxin_degradation_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__dioxin_degradation_boundary__ppu00621-deep-research-falcon.md`.
- Validation complete for both gene reviews and the module.
- Gene review pages rendered for both candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/dioxin_degradation_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/dioxin_degradation_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00621` is a boundary/absence map, not a complete dioxin degradation
  pathway.
- `PP_2504` is the only direct aromatic-catabolism candidate: UniProt names it
  2-hydroxymuconate/4-oxalocrotonate tautomerase (EC 5.3.2.6), but current GOA
  only provides broad isomerase activity.
- `PP_1791` remains unresolved aldolase/synthase-family context. Its
  TreeGrafter 2-isopropylmalate synthase and L-leucine biosynthesis annotations
  are left `UNDECIDED` in the gene review pending substrate evidence.
- The two-member KEGG batch lacks the upper dioxin dioxygenase and downstream
  route needed to claim complete dioxin degradation in KT2440.

## Batch status: ppu00625 / chloroalkane_chloroalkene_degradation_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00625_chloroalkane_chloroalkene_degradation_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00625_chloroalkane_chloroalkene_degradation_boundary.md`

Status as of 2026-07-08 UTC:

- 5 candidates curated: all KEGG `ppu00625` membership genes.
- 5/5 candidate review folders present.
- 5/5 candidate Asta gene-level retrieval reports present.
- 5/5 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/chloroalkane_chloroalkene_degradation_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/chloroalkane_chloroalkene_degradation_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__chloroalkane_chloroalkene_degradation_boundary__ppu00625-deep-research-falcon.md`.
- Validation complete for all five gene reviews and the module.
- Gene review pages rendered for all five candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/chloroalkane_chloroalkene_degradation_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/chloroalkane_chloroalkene_degradation_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00625` is a boundary/absence map, not a complete chloroalkane or
  chloroalkene degradation pathway.
- `fdhA` is the newly curated direct formaldehyde side node. The review accepts
  NAD-dependent formaldehyde dehydrogenase activity, modifies the broad
  oxidoreductase annotation to that specific function, and keeps zinc binding as
  non-core cofactor context.
- `frmA` provides glutathione-dependent formaldehyde detoxification context,
  while `pedE`, `pedH`, and `adhP` are alcohol-dehydrogenase side nodes.
- The batch lacks haloalkane dehalogenase, haloacid dehalogenase, or
  chloroalkene-specific upper-route chemistry, so these genes should not be read
  as evidence for complete chloroalkane/chloroalkene degradation in KT2440.

## Batch status: ppu00626 / naphthalene_degradation_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00626_naphthalene_degradation_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00626_naphthalene_degradation_boundary.md`

Status as of 2026-07-08 UTC:

- 2 candidates curated: all KEGG `ppu00626` membership genes.
- 2/2 candidate review folders present.
- 2/2 candidate Asta gene-level retrieval reports present.
- 2/2 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/naphthalene_degradation_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/naphthalene_degradation_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__naphthalene_degradation_boundary__ppu00626-deep-research-falcon.md`.
- Validation complete for both gene reviews and the module.
- Gene review pages rendered for both candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/naphthalene_degradation_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/naphthalene_degradation_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00626` is a boundary/absence map, not a complete naphthalene
  degradation pathway.
- `frmA` is glutathione-dependent formaldehyde detoxification context, and
  `adhP` is a generic zinc alcohol dehydrogenase with unresolved physiological
  substrate.
- The batch lacks naphthalene dioxygenase, cis-dihydrodiol dehydrogenase,
  salicylate hydroxylase, and catechol/ring-cleavage route enzymes expected for
  a satisfiable naphthalene degradation route.

## Batch status: ppu00627 / aminobenzoate_degradation_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00627_aminobenzoate_degradation_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00627_aminobenzoate_degradation_boundary.md`

Status as of 2026-07-08 UTC:

- 12 candidates curated: all KEGG `ppu00627` membership genes.
- 12/12 candidate review folders present.
- 12/12 candidate Asta gene-level retrieval reports present.
- 12/12 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/aminobenzoate_degradation_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/aminobenzoate_degradation_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__aminobenzoate_degradation_boundary__ppu00627-deep-research-falcon.md`.
- Validation complete for all 12 gene reviews and the module.
- Gene review pages rendered for all 12 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/aminobenzoate_degradation_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/aminobenzoate_degradation_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00627` is a broad aromatic/xenobiotic boundary map, not a complete
  aminobenzoate degradation pathway.
- Directly useful aromatic-catabolism signals are split across gallate
  (`galA`) and lignin-derived ferulate/vanillate side funnels (`fcs`, `PP_3358`,
  `vdh`, `vanA`, `vanB`).
- `PP_2805` is an experimentally characterized Baeyer-Villiger monooxygenase
  with short-chain aliphatic ketone preference; `PP_3657` remains a
  substrate-unresolved p-nitrobenzoate reductase/nitroreductase-family
  oxidoreductase.
- `ubiX`, `PP_2217`, `paaF`, and `PP_2932` are cofactor, acyl-CoA, or
  unresolved side context and should not be interpreted as a coherent
  aminobenzoate route.
- The PP_3358 review now proposes GO:0050547 feruloyl-CoA hydratase/lyase
  activity as the specific replacement for generic catalytic activity and
  removes the unsupported isoprenoid catabolic process annotation.

## Batch status: ppu00630 / glyoxylate_dicarboxylate_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00630_glyoxylate_dicarboxylate_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00630_glyoxylate_dicarboxylate_metabolism_boundary.md`

Status as of 2026-07-08 UTC:

- 62 candidates curated: all KEGG `ppu00630` membership genes.
- 62/62 candidate review folders present.
- 62/62 candidate Asta gene-level retrieval reports present.
- 62/62 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/glyoxylate_dicarboxylate_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/glyoxylate_dicarboxylate_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__glyoxylate_dicarboxylate_metabolism_boundary__ppu00630-deep-research-falcon.md`.
- Validation complete for all 62 resolved gene reviews and the module.
- Gene review pages rendered for all 62 resolved review files.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/glyoxylate_dicarboxylate_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/glyoxylate_dicarboxylate_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00630` is a broad glyoxylate/dicarboxylate boundary map, not one
  satisfiable linear pathway.
- The direct glycolate/glyoxylate chemistry is covered by `glcD`, `glcE`, and
  `glcF` for glycolate oxidation/dehydrogenation, plus `gcl`, `hyi`, and
  `glxR` for glyoxylate carboligase, hydroxypyruvate isomerase, and
  tartronate-semialdehyde reduction.
- `PP_0416` is phosphoglycolate phosphatase/repair context. `PP_0094` is a
  5'-nucleotidase/HAD-family side node whose protein-tyrosine-kinase transfer
  was removed, and `PP_1907` remains an unresolved HAD-family candidate with no
  assigned core function.
- The Fdo/NDH block is respiratory side context rather than a glyoxylate route:
  `fdoG`, `fdoH`, `fdoI`, PP_2185/`Q88KV4`, and PP_2186 support formate
  oxidation, while PP_2183/`Q88KV6` and `PP_2184` are NADH-quinone
  oxidoreductase subunits.
- TCA-cycle, one-carbon/folate, glycine-cleavage, acyl-CoA, catalase, and
  glutamine-synthetase overlaps are kept as neighboring metabolism rather than
  evidence for one consolidated glyoxylate/dicarboxylate module.

## Batch status: ppu00633 / nitrotoluene_degradation_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00633_nitrotoluene_degradation_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00633_nitrotoluene_degradation_boundary.md`

Status as of 2026-07-08 UTC:

- 3 candidates curated: all KEGG `ppu00633` membership genes.
- 3/3 candidate review folders present.
- 3/3 candidate Asta gene-level retrieval reports present.
- 3/3 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/nitrotoluene_degradation_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/nitrotoluene_degradation_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__nitrotoluene_degradation_boundary__ppu00633-deep-research-falcon.md`.
- Validation complete for all three gene reviews and the module.
- Gene review pages rendered for all three candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/nitrotoluene_degradation_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/nitrotoluene_degradation_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00633` is a boundary/absence xenobiotic map, not a complete
  nitrotoluene degradation pathway.
- `nfnB` is a nitroreductase-family oxidoreductase. Its EC-derived
  6,7-dihydropteridine reductase annotation is left `UNDECIDED` pending
  substrate evidence, while broad oxidoreductase activity is retained as the
  safest current core term.
- `PP_2486` and `nemA` are FMN-dependent OYE/NADH-flavin oxidoreductase-family
  proteins. Their seeded broad oxidoreductase annotations are modified toward
  GO:0016628, and FMN binding/cytosol are kept as non-core context.
- The batch lacks route-defining nitrotoluene dioxygenase/reductase specificity
  and downstream ring-cleavage chemistry, so the genes should be treated as
  redox/electrophile-detoxification side candidates until substrate assays
  establish a pathway role.

## Batch status: ppu00640 / propanoate_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00640_propanoate_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00640_propanoate_metabolism_boundary.md`

Status as of 2026-07-08 UTC:

- 33 candidates curated: all KEGG `ppu00640` membership genes.
- 33/33 candidate review folders present.
- 33/33 candidate Asta gene-level retrieval reports present.
- 33/33 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/propanoate_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/propanoate_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__propanoate_metabolism_boundary__ppu00640-deep-research-falcon.md`.
- Validation complete for all 33 gene reviews and the module.
- Gene review pages rendered for all 33 candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/propanoate_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/propanoate_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00640` is a broad propanoate-metabolism boundary map, not one
  linear pathway.
- The interpretable core is propionate/propionyl-CoA activation and
  methylcitrate-cycle chemistry: `prpE`, `prpC`, `prpD`, `prpF`, `acnA-II`,
  `acnB`, and `prpB`.
- `acnB` remains the strongest organism-specific methylcitrate-cycle node:
  existing KT2440 genetics support AcnB as the key dehydratase/hydratase for
  growth on odd-chain fatty acids, and the review now adds a first-pass `NEW`
  propionate catabolic process annotation to match its core function.
- `prpB` is curated as methylisocitrate lyase; the isocitrate lyase row is
  modified toward GO:0046421 because the PrpB/methylcitrate substrate is more
  appropriate than glyoxylate-shunt isocitrate lyase.
- `prpD` is accepted as sequence-supported 2-methylcitrate dehydratase, while
  the module notes the unresolved in vivo division of labor with AcnB.
- `acnA-II` is accepted as an aconitase-family methylcitrate/propionate
  candidate; its broad hydro-lyase row is over-annotation context.
- `prpF` keeps broad isomerase activity because no more specific GO term is
  currently available in the local GOA block.
- `prpE` is propionate-CoA ligase; the ARBA intracellular organelle lumen row is
  removed as taxonomically inappropriate for a bacterial soluble enzyme.
- `yqhD` is retained as broad NAD(P)-dependent alcohol dehydrogenase context;
  methylglyoxal reductase and butanol dehydrogenase substrate-specific calls
  remain `UNDECIDED` pending KT2440-specific evidence.
- `mmsA-I`/`mmsA-II`, `PP_0596`, ACC genes, acetate/acetyl-CoA genes, TCA and
  glyoxylate nodes, beta-oxidation/acyl-CoA enzymes, and BCKDH/lipoamide genes
  are neighboring metabolism and should be interpreted through their native
  modules unless direct propionate-specific evidence is added.

## Batch status: ppu00643 / styrene_degradation_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00643_styrene_degradation_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00643_styrene_degradation_boundary.md`

Status as of 2026-07-08 UTC:

- 5 candidates curated: all KEGG `ppu00643` membership genes.
- 5/5 candidate review folders present.
- 5/5 candidate Asta gene-level retrieval reports present.
- 5/5 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/styrene_degradation_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/styrene_degradation_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__styrene_degradation_boundary__ppu00643-deep-research-falcon.md`.
- Validation complete for all five gene reviews and the module.
- Gene review pages rendered for all five candidates.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/styrene_degradation_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/styrene_degradation_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00643` is a boundary/absence xenobiotic map, not a complete styrene
  degradation pathway.
- The batch lacks the route-defining styrene monooxygenase and styrene oxide
  isomerase steps expected for a complete upper route from styrene to
  phenylacetaldehyde.
- `peaE` is the direct styrene-adjacent node, with phenylacetaldehyde
  dehydrogenase (NAD+) activity; its exact physiological route in KT2440 remains
  broader aromatic-side-chain aldehyde context.
- `hmgA`, `hmgC`, and `hmgB` are the homogentisate pathway enzymes for
  L-phenylalanine, L-tyrosine, and 3-hydroxyphenylacetate degradation, and
  should not be interpreted as styrene upper-route evidence.
- `PP_2932` is an unresolved amidase signature-domain protein with no current
  GOA annotations. The review intentionally keeps no core function pending
  substrate evidence.

## Batch status: ppu00650 / butanoate_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00650_butanoate_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00650_butanoate_metabolism_boundary.md`

Status as of 2026-07-08 UTC:

- 38 candidates curated: all KEGG `ppu00650` membership genes.
- 38/38 candidate review folders present.
- 38/38 candidate Asta gene-level retrieval reports present.
- 38/38 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/butanoate_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/butanoate_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__butanoate_metabolism_boundary__ppu00650-deep-research-falcon.md`.
- Validation complete for all 38 gene reviews and the module.
- Gene review pages rendered for all 38 candidates.
- Module page rendered:
  `pages/modules/butanoate_metabolism_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/butanoate_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/butanoate_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00650` is a broad butanoate/PHA boundary map, not one linear
  butanoate pathway.
- The five primary genes are `bdhA`, `gbd`, `hbdH`, `phaA`, and `phaC`:
  butanediol/polyol redox, 4-hydroxybutyrate redox, 3-hydroxybutyrate redox,
  and medium-chain-length PHA storage polymerization.
- `phaA` is the KT2440 PhaC1 class II PHA synthase despite the confusing gene
  symbol; `phaC` is PhaC2. Existing reviews keep the PHB-specific process
  mapping corrected toward broader poly(3-hydroxyalkanoate) biosynthesis.
- Asta retrieval for `bdhA`, `gbd`, and `hbdH` did not provide useful
  gene-specific KT2440 literature, so these first-pass reviews rely on
  UniProt/GOA EC, InterPro/PANTHER family, and GOA term evidence.
- `sad-I`, `sad-II`, `gabD-II`, `davD`, and `davT` are better understood as
  succinate-semialdehyde/GABA, Dav lysine-catabolism, and amino-acid side
  contexts.
- `aacs`, `hbd`, `bktB`, `PP_2215`, `PP_3355`, `yqeF`, and related hydratase or
  dehydrogenase genes are reusable acetoacetate, thiolase, and acyl-CoA nodes
  shared with beta-oxidation, BCAA degradation, terpenoid, phenylacetate, and
  caprolactam maps.
- TCA succinate dehydrogenase subunits, acetolactate synthase genes, FabV, and
  phenylacetate/caprolactam spillovers should remain interpreted through their
  narrower primary modules unless direct butanoate/PHA evidence is added.

## Batch status: ppu00660 / c5_branched_dibasic_acid_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00660_c5_branched_dibasic_acid_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00660_c5_branched_dibasic_acid_metabolism_boundary.md`

Status as of 2026-07-08 UTC:

- 10 candidates curated: all KEGG `ppu00660` membership genes.
- 10/10 candidate review folders present.
- 10/10 candidate Asta gene-level retrieval reports present.
- 10/10 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/c5_branched_dibasic_acid_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/c5_branched_dibasic_acid_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__c5_branched_dibasic_acid_metabolism_boundary__ppu00660-deep-research-falcon.md`.
- Validation complete for all 10 gene reviews and the module.
- Gene review pages rendered for all 10 candidates.
- Module page rendered:
  `pages/modules/c5_branched_dibasic_acid_metabolism_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/c5_branched_dibasic_acid_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/c5_branched_dibasic_acid_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00660` is a boundary overlap map rather than one dedicated
  C5-branched dibasic acid pathway.
- PP_1157, PP_1394, `ilvI`, and `ilvH` are acetolactate synthase catalytic or
  regulatory nodes. They should be interpreted through branched-chain
  amino-acid biosynthesis, especially valine and isoleucine precursor
  chemistry.
- `leuC`, `leuD`, and `leuB` are the isopropylmalate branch enzymes for
  L-leucine biosynthesis.
- `galC` belongs to gallate catabolism; its ppu00660 membership reflects a
  C5-dicarboxylate-adjacent aldolase intermediate, not BCAA biosynthesis.
- `sucD` and `sucC` are TCA-cycle succinate-CoA ligase subunits and should stay
  anchored to central-carbon succinyl-CoA turnover.
- No new gene-level curation was required: all 10 reviews were already complete
  and valid, with only expected Asta-not-referenced validation warnings in six
  files.

## Batch status: ppu00680 / methane_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00680_methane_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00680_methane_metabolism_boundary.md`

Status as of 2026-07-08 UTC:

- 30 candidates curated: all KEGG `ppu00680` membership genes.
- 30/30 candidate review folders present.
- 30/30 candidate Asta gene-level retrieval reports present.
- 30/30 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/methane_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/methane_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__methane_metabolism_boundary__ppu00680-deep-research-falcon.md`.
- Validation complete for all 30 gene reviews and the module.
- Gene review pages rendered for all 30 candidates.
- Module page rendered:
  `pages/modules/methane_metabolism_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/methane_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/methane_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00680` should be treated as a boundary/absence methane map. The
  candidate set does not establish methane oxidation or methanogenesis in
  KT2440.
- `fdhA`, `frmA`, and newly curated `frmC` form the strongest
  formaldehyde-detoxification context. `frmC` is curated as cytosolic
  S-formylglutathione hydrolase acting downstream of FrmA.
- `fdoG`, `fdoH`, `fdoI`, PP_2185/Q88KV4, and PP_2186 are formate
  dehydrogenase or formate-oxidation/respiratory redox context. PP_2183/Q88KV6
  and PP_2184 are NDH-like electron-transfer side nodes.
- GlyA paralogs, SerA/SerC/SerB, TtuD/HprA, Ppc, PpsA, Eno, Fba, Fbp, GpmI,
  Mdh, Pta, AcsA1/AcsA2, PP_2213, and PP_2533 are folate/serine,
  hydroxypyruvate/glycerate, gluconeogenic, acetate/acetyl-CoA, or unresolved
  central-carbon side nodes.
- Newly curated `peaA` is a predicted exported quinohaemoprotein amine
  dehydrogenase alpha subunit. The review accepts methylamine dehydrogenase
  activity as a complex-level contribution and keeps electron-transfer and heme
  binding as non-core features.
- Validation warnings are non-blocking: mostly Asta-not-referenced notices plus
  preexisting location/process mirror warnings on overlap reviews and a
  no-core-function warning for unresolved PP_2533.

## Batch status: ppu00710 / carbon_fixation_calvin_cycle_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00710_carbon_fixation_calvin_cycle_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00710_carbon_fixation_calvin_cycle_boundary.md`

Status as of 2026-07-08 UTC:

- 13 candidates curated: all KEGG `ppu00710` membership genes.
- 13/13 candidate review folders present.
- 13/13 candidate Asta gene-level retrieval reports present.
- 13/13 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/carbon_fixation_calvin_cycle_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/carbon_fixation_calvin_cycle_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__carbon_fixation_calvin_cycle_boundary__ppu00710-deep-research-falcon.md`.
- Validation complete for all 13 gene reviews and the module.
- Gene review pages rendered for all 13 candidates.
- Module page rendered:
  `pages/modules/carbon_fixation_calvin_cycle_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/carbon_fixation_calvin_cycle_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/carbon_fixation_calvin_cycle_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00710` is a boundary/absence Calvin-cycle map. The batch lacks
  route-defining Rubisco and phosphoribulokinase candidates.
- `rpe`, `rpiA`, `tktA`, and `tal` are non-oxidative pentose-phosphate pathway
  enzymes, not evidence for a committed Calvin-Benson-Bassham cycle.
- `gapA`, `gapB`, `pgk`, `tpiA`, `fba`, and `fbp` are lower EMP or
  gluconeogenic central-carbon enzymes reused in autotrophic map diagrams.
- `ppc` supports anaplerotic carbon fixation through phosphoenolpyruvate
  carboxylase, but this is not Calvin-cycle CO2 assimilation.
- `maeB` and `mdh` remain malic-enzyme and TCA malate/oxaloacetate side nodes.
- No gene-level edits were required in this checkpoint; all 13 reviews were
  already complete and valid. Remaining validation warnings are non-blocking
  deep-research-not-referenced notices.

## Batch status: ppu00780 / biotin_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00780_biotin_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00780_biotin_metabolism_boundary.md`

Status as of 2026-07-08 UTC:

- 16 candidates curated: all KEGG `ppu00780` membership genes.
- 16/16 candidate review folders present.
- 16/16 candidate Asta gene-level retrieval reports present.
- 16/16 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/biotin_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/biotin_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__biotin_metabolism_boundary__ppu00780-deep-research-falcon.md`.
- Validation complete for all 16 gene reviews and the module.
- Gene review pages rendered for all 16 candidates.
- Module page rendered:
  `pages/modules/biotin_metabolism_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/biotin_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/biotin_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00780` is a true biotin-metabolism boundary with a coherent de novo
  biotin biosynthesis core plus side-node context.
- `bioC` and `bioH` define the BioC-BioH pimelate precursor branch that uses
  acyl carrier protein chemistry upstream of BioF.
- `bioF`, `bioA`, `bioD`, and `bioB` form the AON-to-biotin biosynthetic route:
  AON synthase, SAM-dependent aminotransferase, dethiobiotin synthetase, and
  biotin synthase.
- `birA` is retained as biotin metabolism context through biotin-protein ligase
  activity and biotin-operon repression, not as a biotin-biosynthesis enzyme.
- `fabG`, `fabZ`, `fabF`, `fabB`, and `PP_3303` are fatty-acid/acyl-ACP
  boundary nodes; `PP_0581`, `PP_1852`, and `PP_2540` remain unresolved
  SDR/reductase boundary candidates; `PP_2783` is aromatic-catabolism side
  context and should not be forced into biotin or fatty-acid elongation.
- Validation warnings are non-blocking Asta-not-referenced notices for first-pass
  reviews where curation decisions are supported by UniProt/GOA file evidence.

## Batch status: ppu00785 / lipoic_acid_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00785_lipoic_acid_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00785_lipoic_acid_metabolism_boundary.md`

Status as of 2026-07-08 UTC:

- 19 candidates curated: all KEGG `ppu00785` membership genes.
- 19/19 candidate review folders present.
- 19/19 candidate Asta gene-level retrieval reports present.
- 19/19 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/lipoic_acid_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/lipoic_acid_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__lipoic_acid_metabolism_boundary__ppu00785-deep-research-falcon.md`.
- Validation complete for all 19 gene reviews and the module.
- Gene review pages rendered for all 19 candidates.
- Module page rendered:
  `pages/modules/lipoic_acid_metabolism_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/lipoic_acid_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/lipoic_acid_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00785` is best represented as an endogenous protein-lipoylation
  module plus lipoylated-target boundary context, not a list of independent
  lipoate-biosynthesis enzymes.
- `lipB` transfers octanoyl groups from octanoyl-ACP onto lipoyl-domain lysines;
  `lipA` then inserts sulfur atoms to form mature protein-bound lipoyl groups.
- `aceE`/`aceF`/`lpd`, `sucA`/`sucB`/`lpdG`, and
  `bkdAA`/`bkdAB`/`bkdB`/`lpdV` are lipoate-dependent 2-oxoacid dehydrogenase
  contexts tied to pyruvate, TCA, and branched-chain amino-acid metabolism.
- `gcvP1`/`gcvH1`/`gcvT-I` and `gcvP2`/`gcvH2`/`gcvT` are glycine-cleavage
  paralog sets in which GcvH proteins are lipoylated carrier targets.
- `acoC` is retained as an acetoin-cleavage E2-like lipoate-dependent target
  context.
- Validation warnings are non-blocking and mostly reflect Asta-not-referenced
  first-pass reviews plus pre-existing mirror warnings on glycine-cleavage
  overlap reviews.

## Batch status: ppu00860 / porphyrin_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu00860_porphyrin_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu00860_porphyrin_metabolism_boundary.md`

Status as of 2026-07-08 UTC:

- 46 candidates curated: all KEGG `ppu00860` membership genes.
- 46/46 candidate review folders present.
- 46/46 candidate Asta gene-level retrieval reports present.
- 46/46 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/porphyrin_metabolism_boundary.yaml`.
- Falcon generic module research is still outstanding:
  `modules/porphyrin_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding:
  `projects/P_PUTIDA/deep-research/PSEPK__porphyrin_metabolism_boundary__ppu00860-deep-research-falcon.md`.
- Validation complete for all 46 gene reviews and the module.
- Gene review pages rendered for all 46 candidates.
- Module page rendered:
  `pages/modules/porphyrin_metabolism_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/porphyrin_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/porphyrin_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu00860` is best represented as a tetrapyrrole boundary module rather
  than one strict porphyrin pathway.
- The heme/protoporphyrin biosynthetic spine is covered by `gltX`, `hemA`,
  `hemL`, `hemB`, `hemBB`, `hemC`, `hemD`, `hemE`, `hemF`, `hemN`,
  `PP_0431`, and `hemH`. `hemF` and `hemN` represent oxygen-dependent and
  oxygen-independent alternatives for coproporphyrinogen oxidation.
- `cyoE1`, `cyoE2`, and `PP_0109` are heme O/heme A maturation context shared
  with respiratory terminal oxidase assembly, not additional upstream
  porphyrin-synthesis steps.
- The cobalamin/corrinoid branch is large and needs to remain separate from the
  heme spine: `pduO`, `cobO`, `cobB__Q88MA1`, `cobD`, `cobC`, `cobQ`, `cobP`,
  `cobT`, `PP_1680`, `cobS`, `PP_3409`, `cobM`, `PP_3506`, `cobN`,
  `PP_3763`, `cobJ`, `cobI`, `cobH`, `cobG`, `cobL`, `cbiD`, and `cobK`.
- `cobA` and `cysG` occupy the siroheme/precorrin branch point. The first pass
  treats the cysG cobalamin-biosynthesis process annotation as over-broad and
  narrows the molecular-function interpretation toward sirohydrochlorin
  ferrochelatase where appropriate.
- `hemO`, `PP_2582`, and `PP_1358` are heme oxygenase/heme-utilization nodes,
  while `bfr-I`, `bfr-II`, and `PP_4856` are bacterioferritin/ferritin-like
  iron-storage side nodes drawn into the KEGG map by heme/iron chemistry.
- Clear electronic spillovers were removed in this pass: CobD/CobQ transporter
  annotations, CobK DNA binding/topological-change terms, and CobL protein
  methyltransferase activity.
- `PP_0188` remains a no-GOA HemX-family boundary candidate; its catalytic or
  non-catalytic role in tetrapyrrole metabolism is unresolved.
- Validation warnings are non-blocking and mostly reflect Asta-not-referenced
  first-pass reviews, plus a few pre-existing contextual warnings on overlap
  genes.

## Batch status: UPA00252 / porphyrin_metabolism_boundary support

Batch files:

- `projects/P_PUTIDA/batches/UPA00252_porphyrin_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/UPA00252_porphyrin_metabolism_boundary.md`

Status as of 2026-07-09 PDT / 2026-07-10 UTC:

- 2 candidates covered: UniPathway-primary `PP_0189` plus already-curated
  `hemH` ferrochelatase context from the KEGG `ppu00860` batch.
- 2/2 candidate review folders present. `PP_0189` required fetching by
  UniProt accession `Q88RE2` with alias `PP_0189`.
- 2/2 candidate Asta gene-level retrieval reports present.
- 2/2 review YAMLs curated with no remaining `PENDING` actions.
- Existing boundary module extended and validated:
  `modules/porphyrin_metabolism_boundary.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/porphyrin_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__porphyrin_metabolism_boundary__upa00252-deep-research-falcon.md`.
- Validation complete for the `PP_0189` gene review and the updated module.
- Gene review page rendered:
  `genes/PSEPK/PP_0189/PP_0189-ai-review.html`.
- Module page rendered:
  `pages/modules/porphyrin_metabolism_boundary.html`.
- Project batch page rendered:
  `pages/projects/P_PUTIDA/batches/UPA00252_porphyrin_metabolism_boundary.html`.

Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/porphyrin_metabolism_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/porphyrin_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `UPA00252` is best represented as a UniPathway support view of the
  existing porphyrin/tetrapyrrole boundary module rather than as a separate
  pathway.
- `PP_0189` is an inner-membrane HemY_N/TPR-associated support protein for a
  late step of protoheme IX biosynthesis. Its existing broad heme-metabolism
  annotation is modified toward `heme biosynthetic process`, but no molecular
  function is asserted in this first pass.
- `hemH` remains the catalytically explicit ferrochelatase/protoheme synthase
  context node completing heme biosynthesis.

## Batch status: ppu03410 / bacterial_base_excision_repair

Batch files:

- `projects/P_PUTIDA/batches/ppu03410_bacterial_base_excision_repair.tsv`
- `projects/P_PUTIDA/batches/ppu03410_bacterial_base_excision_repair.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 14 candidates curated or rechecked: all KEGG `ppu03410` membership genes.
- 14/14 candidate review folders present. `PP_4812` required fetching by
  UniProt accession `Q88DL3` with alias `PP_4812`.
- 14/14 candidate Asta gene-level retrieval reports present.
- 14/14 review YAMLs curated with no remaining `PENDING` actions. The four
  overlap genes `polA`, `recJ`, `ligA`, and `ligB` were updated only for
  lightweight Asta provenance, with `ligA` cytosol made consistent with its
  core function.
- New boundary module created and validated:
  `modules/bacterial_base_excision_repair.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/bacterial_base_excision_repair-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_base_excision_repair__ppu03410-deep-research-falcon.md`.
- Validation complete for all 14 gene reviews and the module with no remaining
  warnings in the targeted batch validation.
- Gene review pages rendered for all 14 candidates.
- Module page rendered:
  `pages/modules/bacterial_base_excision_repair.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_base_excision_repair.yaml
uv run python -m ai_gene_review.validation.module_validator modules/bacterial_base_excision_repair.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu03410` is a base-excision-repair boundary module, not a flat list
  of BER-specific enzymes. It combines lesion-specific glycosylases, AP-site
  processing enzymes, and shared repair synthesis/ligation machinery.
- The strict lesion-recognition/AP-site-forming core includes `tag`, `PP_0705`,
  `PP_4812`, `ung`, `mutY`, `mutM`, and `nth`, spanning alkylated,
  deaminated, mismatched, and oxidized base repair.
- `PP_2707`, `xthA`, and `PP_5292` are ExoIII-like AP/ExoA-family processing
  candidates. The module records them as BER-boundary AP/exonuclease nodes, but
  the gene reviews stay conservative because current GOA supports generic DNA
  repair and nuclease activities rather than direct BER-specific evidence.
- `polA`, `ligA`, and `ligB` provide shared repair synthesis and nick sealing.
  These overlap cleanly with nucleotide-excision and mismatch-repair batches.
- `recJ` is retained as a shared repair exonuclease side node from KEGG
  `ppu03410`, not as a lesion-specific BER initiation factor.
- `mutY` TreeGrafter transfer of `8-oxo-7,8-dihydroguanine DNA
  N-glycosylase activity` was narrowed because MutY primarily removes adenine
  from oxidized-purine mispairs; `mutM` retains the oxidized-purine lesion
  glycosylase activity.

## Batch status: ppu03420 / bacterial_nucleotide_excision_repair

Batch files:

- `projects/P_PUTIDA/batches/ppu03420_bacterial_nucleotide_excision_repair.tsv`
- `projects/P_PUTIDA/batches/ppu03420_bacterial_nucleotide_excision_repair.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 10 candidates curated: all KEGG `ppu03420` membership genes.
- 10/10 candidate review folders present. `PP_3087` required fetching by
  UniProt accession `Q88IB2` with alias `PP_3087`.
- 10/10 candidate Asta gene-level retrieval reports present.
- 10/10 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/bacterial_nucleotide_excision_repair.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/bacterial_nucleotide_excision_repair-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_nucleotide_excision_repair__ppu03420-deep-research-falcon.md`.
- Validation complete for all 10 gene reviews and the module. Gene warnings
  are non-blocking and limited to expected first-pass Asta context notices plus
  pre-existing cytosol/cytoplasm reflection warnings on overlap genes.
- Gene review pages rendered for all 10 candidates.
- Module page rendered:
  `pages/modules/bacterial_nucleotide_excision_repair.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_nucleotide_excision_repair.yaml
uv run python -m ai_gene_review.validation.module_validator modules/bacterial_nucleotide_excision_repair.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu03420` is a nucleotide-excision-repair boundary module. The strict
  UvrABC core is `uvrA`, `uvrB`, and `uvrC`.
- `mfd` is the transcription-coupled repair input, linking stalled
  transcription complexes to UvrABC repair.
- `uvrD`, `polA`, `ligA`, and `ligB` are real downstream repair-context nodes:
  lesion-containing oligonucleotide removal, repair synthesis, and nick
  sealing. These roles are shared with other DNA repair or replication
  pathways and should not be interpreted as UvrABC core membership.
- `PP_2839` is curated conservatively as a predicted DinG/Rad3-like DNA
  helicase with unresolved pathway specificity.
- `PP_3087` is curated conservatively as a UvrA-family ATPase-like boundary
  member. Current GOA supports ATP binding/hydrolysis and cytoplasm, while its
  precise NER-specific step remains unresolved.

## Batch status: ppu03430 / bacterial_mismatch_repair

Batch files:

- `projects/P_PUTIDA/batches/ppu03430_bacterial_mismatch_repair.tsv`
- `projects/P_PUTIDA/batches/ppu03430_bacterial_mismatch_repair.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 19 candidates curated: all KEGG `ppu03430` membership genes.
- 19/19 candidate review folders present.
- 19/19 candidate Asta gene-level retrieval reports present.
- 19/19 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/bacterial_mismatch_repair.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/bacterial_mismatch_repair-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_mismatch_repair__ppu03430-deep-research-falcon.md`.
- Validation complete for all 19 gene reviews and the module. Gene warnings
  are non-blocking and limited to expected first-pass Asta context notices plus
  cytosol/cytoplasm reflection warnings on a few reviews.
- Gene review pages rendered for all 19 candidates.
- Module page rendered:
  `pages/modules/bacterial_mismatch_repair.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_mismatch_repair.yaml
uv run python -m ai_gene_review.validation.module_validator modules/bacterial_mismatch_repair.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu03430` is a mismatch-repair boundary module rather than a clean
  one-to-one list of specific mismatch-recognition factors.
- `mutS` and `mutL` are the strict core: MutS recognizes mismatched DNA, while
  MutL coordinates downstream strand processing in the MutH-free KT2440 system.
- `uvrD`, `xseA`, `xseB`, `sbcB`, `recJ`, PP_0353, and PP_4768 are helicase
  and exonuclease processing context shared with nucleotide-excision,
  base-excision, homologous-recombination, and replication-proofreading
  modules.
- `dnaN`, `dnaEA`, `dnaQ`, `dnaX`, `holA`, `holB`, `holC`, and `ssb` are
  replisome, beta-clamp, clamp-loader, proofreading, and SSB context. Broad
  polymerase annotations on non-catalytic accessory subunits are treated as
  complex-level contribution or over-annotation rather than standalone
  polymerase activity.
- `ligA` and `ligB` provide NAD-dependent nick-sealing context shared between
  replication and repair. LigA is the primary replication/repair ligase; LigB
  is treated as a repair-associated ligase paralog.

## Batch status: ppu03440 / bacterial_homologous_recombination

Batch files:

- `projects/P_PUTIDA/batches/ppu03440_bacterial_homologous_recombination.tsv`
- `projects/P_PUTIDA/batches/ppu03440_bacterial_homologous_recombination.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 24 candidates curated or rechecked: all KEGG `ppu03440` membership genes.
- 24/24 candidate review folders present. Newly fetched primary folders were
  `recF`, `ruvC`, `ruvA`, `recO`, `recR`, `recD`, `recC`, `priA`, and `recG`.
- 24/24 candidate Asta gene-level retrieval reports present. New Asta reports
  were added for the 12 primary HR genes, including existing reviews `ruvB`,
  `recA`, and `recB`.
- 24/24 review YAMLs curated with no remaining `PENDING` actions. The existing
  `ruvB`, `recA`, and `recB` reviews were updated only with lightweight Asta
  provenance.
- New boundary module created and validated:
  `modules/bacterial_homologous_recombination.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/bacterial_homologous_recombination-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_homologous_recombination__ppu03440-deep-research-falcon.md`.
- Validation complete for all 24 gene reviews and the module. The 12 primary
  ppu03440 reviews validate without warnings; full-batch warnings are limited
  to expected first-pass Asta-context notices and cytosol/cytoplasm reflection
  warnings on shared replication-side overlap genes.
- Gene review pages rendered for all 24 candidates.
- Module page rendered:
  `pages/modules/bacterial_homologous_recombination.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_homologous_recombination.yaml
uv run python -m ai_gene_review.validation.module_validator modules/bacterial_homologous_recombination.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu03440` is a homologous-recombination boundary module rather than a
  clean list of only RecA strand-exchange factors.
- The strict core is RecA filament formation, RecFOR mediator context
  (`recF`, `recO`, `recR`), RecBCD double-strand-end processing (`recB`,
  `recC`, `recD`), RuvAB/RuvC Holliday-junction branch migration/resolution,
  RecG branched-DNA remodeling, and PriA replication restart.
- `ssb`, `recJ`, `polA`, PP_0353, PP_4768, and DNA polymerase III clamp,
  clamp-loader, proofreading, and catalytic subunits are retained as shared
  repair, replication-restart, or repair-synthesis context, not as HR-specific
  strand-exchange factors.
- `ruvA` is curated as the Holliday-junction DNA-binding scaffold; helicase and
  ATP-binding terms were narrowed to subunit-appropriate junction-binding or
  complex-context interpretations.
- `recC` is curated as the RecBCD DNA-recognition/scaffold subunit; helicase
  and ATP-binding terms were treated as subunit-level over-annotations, while
  exodeoxyribonuclease V complex membership and HR repair process terms were
  retained.
- `recD` is curated from RecD/ExoV product and GOA evidence as the 5'-3' DNA
  helicase subunit. Its fetch/provider context includes an odd viral-polyprotein
  InterPro/PANTHER contaminant, so that family label was not used as curation
  evidence.

## Batch status: ppu03450 / bacterial_non_homologous_end_joining

Batch files:

- `projects/P_PUTIDA/batches/ppu03450_bacterial_non_homologous_end_joining.tsv`
- `projects/P_PUTIDA/batches/ppu03450_bacterial_non_homologous_end_joining.md`

Status as of 2026-07-08 UTC:

- 2 candidates curated: all KEGG `ppu03450` membership genes.
- 2/2 candidate review folders present.
- 2/2 candidate Asta gene-level retrieval reports present.
- 2/2 review YAMLs curated with no remaining `PENDING` actions.
- New compact DNA-repair module created and validated:
  `modules/bacterial_non_homologous_end_joining.yaml`.
- Falcon generic module research is still outstanding while Edison Falcon access
  returns HTTP 402:
  `modules/bacterial_non_homologous_end_joining-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding while Edison Falcon
  access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_non_homologous_end_joining__ppu03450-deep-research-falcon.md`.
- Validation complete for both gene reviews and the module.
- Gene review pages rendered for both candidates.
- Module page rendered:
  `pages/modules/bacterial_non_homologous_end_joining.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_non_homologous_end_joining.yaml
uv run python -m ai_gene_review.validation.module_validator modules/bacterial_non_homologous_end_joining.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu03450` is a clean two-gene bacterial non-homologous end-joining
  module rather than a broad DNA-repair/recombination bucket.
- `ku` is curated as the Ku DNA-end-binding subunit: double-stranded DNA
  binding is accepted as core, double-strand break repair via nonhomologous end
  joining is accepted as the core process, and the broad DNA binding/DNA repair
  parent terms are narrowed to the more specific existing terms.
- `ligD` is curated as the multifunctional LigD enzyme: ATP-dependent DNA
  ligase activity is accepted as core, ATP binding is retained as non-core
  substrate context, broad DNA repair/recombination process terms are narrowed
  to NHEJ, and `NEW` DNA-directed DNA polymerase, exonuclease, and NHEJ process
  annotations are added from UniProt domain/keyword metadata.
- Asta was retrieval-only/product-confirming for both genes; UniProt, InterPro,
  PANTHER, and GOA file evidence drove the first-pass curation calls.

## Batch status: ppu02060 / phosphotransferase_system_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu02060_phosphotransferase_system_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu02060_phosphotransferase_system_boundary.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 6 candidates curated: all KEGG `ppu02060` membership genes.
- 6/6 candidate review folders present.
- 6/6 candidate Asta gene-level retrieval reports present.
- 6/6 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/phosphotransferase_system_boundary.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/phosphotransferase_system_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__phosphotransferase_system_boundary__ppu02060-deep-research-falcon.md`.
- Validation complete for all six gene reviews and the module.
- Gene review pages rendered for all six candidates.
- Module page rendered:
  `pages/modules/phosphotransferase_system_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/phosphotransferase_system_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/phosphotransferase_system_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu02060` is a compact boundary around a fructose PTS branch plus
  HPr/Ntr regulatory phosphorelay context, not a generic all-sugar PTS
  transport system.
- `fruBKA` forms the fructose-specific branch: FruB supplies PEP-dependent
  phosphotransfer, FruA imports and phosphorylates fructose, and FruK converts
  fructose 1-phosphate to fructose 1,6-bisphosphate.
- `ptsH`, `ptsP`, and `ptsN` are regulatory/general phosphorelay context.
  `ptsN` is curated as an EIIA/Ntr regulatory PTS protein associated with
  potassium-transport regulation, not as evidence for another substrate-specific
  sugar permease.
- No additional substrate-specific PTS transport annotation is proposed from
  this bucket.

## Batch status: ppu03008 / ribosome_biogenesis_eukaryotes_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu03008_ribosome_biogenesis_eukaryotes_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu03008_ribosome_biogenesis_eukaryotes_boundary.md`

Status as of 2026-07-08 PDT / 2026-07-09 UTC:

- 3 candidates curated: all KEGG `ppu03008` membership genes.
- 3/3 candidate review folders present.
- 3/3 candidate Asta gene-level retrieval reports present.
- 3/3 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/ribosome_biogenesis_eukaryotes_boundary.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/ribosome_biogenesis_eukaryotes_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__ribosome_biogenesis_eukaryotes_boundary__ppu03008-deep-research-falcon.md`.
- Validation complete for all three gene reviews and the module.
- Gene review pages rendered for all three candidates.
- Module page rendered:
  `pages/modules/ribosome_biogenesis_eukaryotes_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/ribosome_biogenesis_eukaryotes_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/ribosome_biogenesis_eukaryotes_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu03008` is not a satisfiable eukaryotic ribosome-biogenesis pathway
  in KT2440; it is best represented as a boundary/absence KEGG cross-map
  artifact.
- `rnc` is native bacterial RNase III context, accepting ribonuclease III
  activity, double-stranded RNA binding, rRNA processing, and cytoplasmic
  localization.
- `orn` is native cytoplasmic oligoribonuclease context, accepting
  3'-5'-RNA exonuclease activity and the RNA exonuclease term while narrowing
  generic exonuclease/nucleic-acid-binding rows.
- `PP_2912` is an inferred RIO-type serine/threonine kinase-like protein. The
  review accepts kinase activity and keeps ATP binding as non-core cofactor
  context, but does not assign a eukaryotic ribosome-biogenesis process.
- No eukaryotic ribosome-biogenesis GO annotation is proposed for any KT2440
  member in this bucket.

## Batch status: ppu03018 / bacterial_rna_degradation

Batch files:

- `projects/P_PUTIDA/batches/ppu03018_bacterial_rna_degradation.tsv`
- `projects/P_PUTIDA/batches/ppu03018_bacterial_rna_degradation.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 17 candidates curated or rechecked: all KEGG `ppu03018` membership genes.
- 17/17 candidate review folders present. Newly fetched primary folders were
  `rhlB`, `deaD`, `rne`, `recQ`, `pcnB`, `pnp`, `rhlE-I`, `rnr`, `rhlE`,
  `rppH`, and `rho`; `rhlB`, `deaD`, `rne`, `recQ`, and `rppH` had to be
  fetched by UniProt accession with symbol aliases.
- 17/17 candidate Asta gene-level retrieval reports present. New Asta reports
  were added for the newly fetched genes plus `hfq`; existing overlap reviews
  were updated with lightweight Asta provenance.
- 17/17 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/bacterial_rna_degradation.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/bacterial_rna_degradation-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_rna_degradation__ppu03018-deep-research-falcon.md`.
- Validation complete for all 17 gene reviews and the module. The only warning
  observed in the batch validation was the pre-existing `ppkB` reflection
  warning for `GO:0006793` phosphorus metabolic process.
- Gene review pages rendered for all 17 candidates.
- Module page rendered:
  `pages/modules/bacterial_rna_degradation.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_rna_degradation.yaml
uv run python -m ai_gene_review.validation.module_validator modules/bacterial_rna_degradation.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu03018` is an RNA-degradation boundary module, not a single linear
  decay pathway.
- The strict RNA-turnover core is RppH 5' end activation, RNase E
  endonucleolytic cleavage, PcnB polyadenylation, PNPase/RNase R
  exonucleolytic decay, and DEAD-box RNA helicase remodeling by RhlB, DeaD,
  RhlE/RhlE-II, and RhlE-I/RhpA.
- `hfq` and `rho` are accepted as RNA-regulatory context: Hfq mediates
  RNA/sRNA stability and Rho mediates ATP-dependent transcription termination,
  but neither is curated as a ribonuclease.
- `eno`, `dnaK`, `groEL`, `ppk`, and `ppkB` are retained as degradosome,
  proteostasis, or polyphosphate side context rather than core RNA-decay
  enzymes.
- `recQ` is curated as a DNA-maintenance helicase spillover. Its inclusion in
  KEGG `ppu03018` remains a pathway-boundary question rather than evidence for
  direct RNA-degradation activity.

## Batch status: ppu03020 / bacterial_rna_polymerase_core

Batch files:

- `projects/P_PUTIDA/batches/ppu03020_bacterial_rna_polymerase_core.tsv`
- `projects/P_PUTIDA/batches/ppu03020_bacterial_rna_polymerase_core.md`

Status as of 2026-07-08 PDT / 2026-07-09 UTC:

- 4 candidates curated: all KEGG `ppu03020` membership genes.
- 4/4 candidate review folders present.
- 4/4 candidate Asta gene-level retrieval reports present.
- 4/4 review YAMLs curated with no remaining `PENDING` actions.
- New compact RNAP core module created and validated:
  `modules/bacterial_rna_polymerase_core.yaml`.
- Falcon generic module research is still outstanding while Edison Falcon access
  returns HTTP 402:
  `modules/bacterial_rna_polymerase_core-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research is still outstanding while Edison Falcon
  access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_rna_polymerase_core__ppu03020-deep-research-falcon.md`.
- Validation complete for all four gene reviews and the module.
- Gene review pages rendered for all four candidates.
- Module page rendered:
  `pages/modules/bacterial_rna_polymerase_core.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_rna_polymerase_core.yaml
uv run python -m ai_gene_review.validation.module_validator modules/bacterial_rna_polymerase_core.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu03020` is a compact bacterial RNAP core-complex module rather than
  a broad transcription/regulation pathway.
- `rpoA`, `rpoB`, and `rpoC` are curated as core RNAP subunits contributing to
  DNA-directed RNA polymerase activity and DNA-templated transcription in the
  GO:0000428 DNA-directed RNA polymerase complex.
- `rpoA` protein dimerization and `rpoC` magnesium/zinc binding are retained as
  non-core subunit assembly/cofactor context.
- `rpoZ` is curated as the omega assembly/stabilization subunit. DNA binding and
  5'-3' RNA polymerase activity are treated as over-broad or complex-level
  propagation, while the core function records contribution to RNAP activity
  through the completed complex.
- The fetched stubs initially had accession-valued `gene_symbol` fields because
  fetches had to use UniProt accessions with aliases; the curated files restore
  the symbols `rpoA`, `rpoB`, `rpoC`, and `rpoZ`.
- Sigma factors, transcription elongation/termination factors, and
  pathway-specific regulators should remain separate regulatory/module context.
- Asta was retrieval-only/product-confirming for all four genes; UniProt,
  HAMAP/InterPro, and GOA file evidence drove the first-pass curation calls.

## Batch status: ppu03030 / bacterial_dna_replication

Batch files:

- `projects/P_PUTIDA/batches/ppu03030_bacterial_dna_replication.tsv`
- `projects/P_PUTIDA/batches/ppu03030_bacterial_dna_replication.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 18 candidates curated or rechecked: all KEGG `ppu03030` membership genes.
- 18/18 candidate review folders present. Newly fetched primary folders were
  `dnaG`, `rnhB`, `PP_3893`, `rnhA`, and `dnaB`; `PP_3893` had to be fetched
  by UniProt accession `Q88G33` with alias `PP_3893`.
- 18/18 candidate Asta gene-level retrieval reports present. New Asta reports
  were added for `dnaG`, `rnhB`, `PP_3893`, `rnhA`, and `dnaB`; existing
  replication/repair overlap reviews were updated with lightweight Asta
  provenance.
- 18/18 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/bacterial_dna_replication.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/bacterial_dna_replication-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_dna_replication__ppu03030-deep-research-falcon.md`.
- Validation complete for all 18 gene reviews and the module.
- Gene review pages rendered for all 18 candidates.
- Module page rendered:
  `pages/modules/bacterial_dna_replication.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_dna_replication.yaml
uv run python -m ai_gene_review.validation.module_validator modules/bacterial_dna_replication.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu03030` is a DNA-replication boundary module, not just a flat list
  of polymerase terms.
- The strict replication story is DnaB/DnaG primosome function, SSB-coated
  single-stranded DNA, Pol III alpha/beta/epsilon/clamp-loader/accessory
  elongation machinery, RNase H and PolA primer/nick processing, and LigA
  NAD-dependent nick sealing.
- `PP_3893` is accepted as a DnaB-like 5'-3' DNA helicase candidate but remains
  unresolved as to whether it is a functional replisome paralog, backup
  helicase, or specialized mobile-element/plasmid-like replication helicase.
- `PP_0353` and `PP_4768` are retained as DnaQ-like exonuclease boundary
  candidates. They should not be promoted to specific DNA polymerase III
  epsilon-subunit roles without stronger evidence.
- `ligB` is a real NAD-dependent DNA ligase but is treated as a repair or
  backup boundary ligase relative to the primary replication/repair ligase
  `ligA`.
- `dnaG` required a UniProt-backed `NEW` primosome-complex annotation because
  UniProt carries `GO:1990077` while the fetched GOA seed did not include the
  complex row.

## Partition status: module:dna_replication_repair_recombination

Partition files:

- `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_partition.tsv`
- `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_partition.md`
- `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_dna_topology_topoisomerase.tsv`
- `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_dna_topology_topoisomerase.md`
- `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_replication_accessory_polymerase.tsv`
- `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_replication_accessory_polymerase.md`
- `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_sos_translesion_alkylation_repair.tsv`
- `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_sos_translesion_alkylation_repair.md`
- `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_repair_helicase_recombination_core.tsv`
- `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_repair_helicase_recombination_core.md`
- `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_nuclease_dnase_toxin_side_nodes.tsv`
- `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_nuclease_dnase_toxin_side_nodes.md`
- `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_architectural_rna_protein_spillovers.tsv`
- `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_architectural_rna_protein_spillovers.md`
- `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_mobile_integrase_recombinase_transposase.tsv`
- `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_mobile_integrase_recombinase_transposase.md`
- `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_retroelement_reverse_transcriptase.tsv`
- `projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_retroelement_reverse_transcriptase.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 93-gene broad functional bucket has been split into 8 curation-scale
  buckets: DNA topology/topoisomerase, replication accessory/polymerase
  candidates, SOS/translesion/alkylation repair, repair
  helicase/recombination candidates, mobile-element recombinases/transposases,
  retroelement reverse transcriptases, nuclease/DNase/toxin side nodes, and
  architectural/RNA/protein-folding spillovers.
- The first `dna_topology_topoisomerase` sub-batch is complete: 9/9 review
  folders present, 9/9 review YAMLs curated, and 9/9 Asta reports present.
- Newly fetched and curated genes in this split were `yacG`, `topA`,
  `PP_3831`, `topB`, `PP_4476`, `parC`, and `parE`; existing `gyrA` and
  `gyrB` reviews were reused as curated DNA gyrase context.
- New boundary module created and validated:
  `modules/dna_topology_topoisomerase_boundary.yaml`.
- The second `sos_translesion_alkylation_repair` sub-batch is complete: 9/9
  review folders present, 9/9 review YAMLs curated, and 9/9 Asta reports
  present.
- Newly fetched and curated genes in this split were `PP_1348`, `lexA1`,
  `polB`, `ogt`, `imuB`, `dnaE2`, and `PP_5679`; existing `dinB` and `lexA2`
  reviews were reused and Asta-backed.
- New boundary module created and validated:
  `modules/dna_damage_response_translesion_repair_boundary.yaml`.
- The third `repair_helicase_recombination_core` sub-batch is complete: 20/20
  review folders present, 20/20 review YAMLs curated, and 20/20 Asta reports
  present.
- This split extends the existing validated
  `modules/bacterial_homologous_recombination.yaml` rather than creating a
  separate module.
- The fourth `nuclease_dnase_toxin_side_nodes` sub-batch is complete: 14/14
  review folders present, 14/14 review YAMLs curated, and 14/14 Asta reports
  present.
- New boundary module created and validated:
  `modules/nuclease_dnase_boundary.yaml`.
- The fifth `replication_accessory_polymerase` sub-batch is complete: 6/6
  review folders present, 6/6 review YAMLs curated, and 6/6 Asta reports
  present.
- This split extends the existing validated
  `modules/bacterial_dna_replication.yaml` rather than creating a separate
  module. `PP_0978` intentionally retains no core function because the only
  functional signal is a ProtNLM-derived Pol III chi-like product name.
- The sixth `architectural_rna_protein_spillovers` sub-batch is complete: 7/7
  review folders present, 7/7 review YAMLs curated, and 7/7 Asta reports
  present. The completed `dnaJ` review was preserved and included only as
  chaperone routing context.
- New boundary module created and validated:
  `modules/dna_bucket_architectural_rna_protein_spillover_boundary.yaml`.
- The seventh `mobile_integrase_recombinase_transposase` sub-batch is complete:
  25/25 review folders present, 25/25 review YAMLs curated, and 25/25 Asta
  reports present.
- The eighth `retroelement_reverse_transcriptase` sub-batch is complete: 3/3
  review folders present, 3/3 review YAMLs curated, and 3/3 Asta reports
  present. The pre-existing `PP_0635` review was preserved and Asta-backed.
- New boundary module created and validated:
  `modules/mobile_genetic_elements_boundary.yaml`.
- Validation complete for the newly curated gene reviews and all touched modules.
- Gene review pages rendered for the newly curated genes.
- Module pages rendered:
  `pages/modules/dna_topology_topoisomerase_boundary.html`,
  `pages/modules/bacterial_dna_replication.html`,
  `pages/modules/dna_damage_response_translesion_repair_boundary.html`,
  `pages/modules/bacterial_homologous_recombination.html`,
  `pages/modules/nuclease_dnase_boundary.html`, and
  `pages/modules/dna_bucket_architectural_rna_protein_spillover_boundary.html`,
  and `pages/modules/mobile_genetic_elements_boundary.html`.
- Partition/worklist regenerated. The umbrella bucket now records 93/93 review
  files, 93/93 curated review YAMLs, and 93/93 Asta reports.

Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/dna_topology_topoisomerase_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/dna_topology_topoisomerase_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/dna_damage_response_translesion_repair_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/dna_damage_response_translesion_repair_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_homologous_recombination.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/bacterial_homologous_recombination.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/nuclease_dnase_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/nuclease_dnase_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_dna_replication.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/bacterial_dna_replication.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/dna_bucket_architectural_rna_protein_spillover_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/dna_bucket_architectural_rna_protein_spillover_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/mobile_genetic_elements_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/mobile_genetic_elements_boundary.yaml
```

Main curation conclusions from this split:

- Do not curate all 93 DNA replication/repair/recombination functional-bucket
  genes as one satisfiable pathway. The compact DNA-topology story is separate
  from canonical DNA replication, BER, NER, mismatch repair, homologous
  recombination, NHEJ, mobile elements, and nuclease/toxin side biology.
- `gyrA` and `gyrB` remain the DNA gyrase negative-supercoiling core and are
  reused from existing reviews.
- `yacG` is a small zinc-binding DNA gyrase inhibitor. Its InterPro-derived
  regulation-of-transcription row is marked over-annotated because the direct
  supported function is gyrase inhibition, not transcription-factor activity.
- `topA`, `topB`, and `PP_3831` are curated as ATP-independent type I
  topoisomerase/topological-change nodes. TopB's repair/recombination
  TreeGrafter rows are retained only as non-core side context, and the
  cytoplasmic-replication-fork row is marked over-annotated.
- `parC` and `parE` are curated as Topo IV subunits for type II topoisomerase
  activity, DNA topological change, and chromosome decatenation/segregation.
  `parE` gains a UniProt-backed `NEW` Topo IV complex-membership row so its
  core complex membership is reflected in `existing_annotations`.
- `PP_4476` remains unresolved: the fetched record has a ProtNLM-derived
  Topoisomerase II RecName but no GOA, InterPro, Pfam, or family support. No GO
  terms are asserted from that name alone.
- `lexA1` is the conventional SOS regulon LexA repressor, while `lexA2`
  regulates the narrower imuA-imuB-dnaE2 cassette.
- `dinB` and `dnaE2` are retained as damage-induced/error-prone polymerase
  context; `dnaE2` gains a UniProt/literature-supported NEW translesion
  synthesis row.
- `polB` is curated as type-B DNA polymerase/proofreading context rather than a
  direct SOS-regulatory node.
- `imuB` and `PP_5679` remain accessory or low-information Y-family/damaged-DNA
  context without overpromoting a standalone catalytic function.
- `ogt` is direct alkylation repair, and `PP_1348` is MutT-like oxidized
  nucleotide-pool sanitation.
- `PP_1103` is the experimentally characterized P. putida Lhr-Core 3'-to-5'
  DNA/RNA:DNA helicase; the other Lhr/DinG/UvrD/Rep/SNF2/DNA2-like entries are
  curated only to the specificity supported by local UniProt/GOA/Asta evidence.
- `sbcC` and `sbcD` are treated as SbcCD ATPase/nuclease context; `rdgC`,
  `radA`, and `recN` are recombination/repair factors.
- `uup` is retained as an ABCF ATPase with ribosome-binding plus possible
  branched-DNA context, not as a clean core homologous-recombination enzyme.
- `PP_0152`, `PP_1410`, `PP_2298`, `PP_4448`, and `PP_5711` remain
  low-evidence boundary candidates with no GO function promoted from ProtNLM or
  domain names alone.
- `endX` and `endA` are EndA/NucM-family DNase/endonuclease candidates; `tatD`
  is a TatD-family metal-dependent nuclease/exonuclease candidate; `PP_2276` is
  FEN/phage-exonuclease boundary context; `PP_1306`, `PP_3883`, and `yajD` are
  HNH/pyocin/YajD-like endonuclease candidates; `PP_1554` and `PP_3890` are
  VRR-NUC broad nuclease candidates.
- `yoeB` is an RNA-toxin/mRNA-interferase side node rather than a transcription
  regulator; `PP_4247` and `PP_5295` are RNA nuclease side nodes; `PP_5086` is
  an SNase-domain DNA endonuclease candidate; and `PP_2838` is retained as
  phosphodiesterase I/FAN1-family context with interstrand cross-link repair
  kept non-core.
- `hda` is a DnaA/Hda-family negative regulator of DNA replication
  reinitiation; `PP_2270` is a T7-like helicase/primase-family 5'-3' DNA
  helicase candidate in replication and primer-synthesis context; `PP_2273` is
  a type-A DNA polymerase boundary member rather than part of the canonical Pol
  III core.
- `rarA` is a RarA/MGS1-family DNA-dependent ATPase associated with stalled
  replication responses, not promoted as a helicase; `rep` is the supported
  Rep-family 3'-5' DNA helicase; and `PP_0978` remains an unpromoted Pol III
  chi-like candidate because the local record has only a ProtNLM-derived product
  name and no GOA/domain/family support.
- `tldD` is curated as TldD/PmbA-family metallopeptidase/proteolysis context.
  `ihfB` and `ihfA` are IHF architectural/regulatory DNA-binding subunits, not
  DNA-repair enzymes.
- `cspD` is curated as cold-shock-domain DNA-binding/negative regulation of DNA
  replication context, while `hrpA` and `hrpB` are RNA-helicase-family proteins.
  `hrpB` gains a conservative `NEW` RNA helicase row from HrpB family evidence.
- `dnaJ` remains DnaK-system co-chaperone/protein-folding context; the review
  was not rewritten beyond adding the Asta retrieval file for coverage.
- Phage integrases, Tyr/Ser recombinases, resolvases, excisionase, Tn/IS
  transposases, and group-II-intron/retroelement reverse transcriptases are
  routed to `modules/mobile_genetic_elements_boundary.yaml`, not to chromosomal
  DNA repair. Broad DNA-binding rows are retained as context unless they are the
  only supported molecular-function evidence for low-specificity
  integrase/excisionase records.
- `PP_2495` is retained as an unresolved YqaJ viral recombinase-domain member:
  it has no fetched GOA rows, no synthetic `existing_annotations` entry, and no
  core GO function asserted in the first-pass review.
- The DNA replication/repair/recombination functional bucket is closed for
  first pass: all 93 partition members now have review files, curated reviews,
  and Asta reports.

## Batch status: module:mobile_genetic_elements / mobile_genetic_elements_boundary first splits

Batch files:

- `projects/P_PUTIDA/batches/module_mobile_genetic_elements_partition.tsv`
- `projects/P_PUTIDA/batches/module_mobile_genetic_elements_partition.md`
- `projects/P_PUTIDA/batches/module_mobile_genetic_elements_transposase_goa_supported.tsv`
- `projects/P_PUTIDA/batches/module_mobile_genetic_elements_transposase_goa_supported.md`
- `projects/P_PUTIDA/batches/module_mobile_genetic_elements_transposase_domain_or_fragment.tsv`
- `projects/P_PUTIDA/batches/module_mobile_genetic_elements_transposase_domain_or_fragment.md`
- `projects/P_PUTIDA/batches/module_mobile_genetic_elements_integrase_mobile_element_context.tsv`
- `projects/P_PUTIDA/batches/module_mobile_genetic_elements_integrase_mobile_element_context.md`
- `projects/P_PUTIDA/batches/module_mobile_genetic_elements_prophage_structural_packaging.tsv`
- `projects/P_PUTIDA/batches/module_mobile_genetic_elements_prophage_structural_packaging.md`
- `projects/P_PUTIDA/batches/module_mobile_genetic_elements_phage_lysis_host_interaction.tsv`
- `projects/P_PUTIDA/batches/module_mobile_genetic_elements_phage_lysis_host_interaction.md`
- `projects/P_PUTIDA/batches/module_mobile_genetic_elements_phage_regulatory_toxin_antitoxin.tsv`
- `projects/P_PUTIDA/batches/module_mobile_genetic_elements_phage_regulatory_toxin_antitoxin.md`
- `projects/P_PUTIDA/batches/module_mobile_genetic_elements_phage_dna_replication_processing.tsv`
- `projects/P_PUTIDA/batches/module_mobile_genetic_elements_phage_dna_replication_processing.md`
- `projects/P_PUTIDA/batches/module_mobile_genetic_elements_low_information_prophage_proteins.tsv`
- `projects/P_PUTIDA/batches/module_mobile_genetic_elements_low_information_prophage_proteins.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The broad `module:mobile_genetic_elements` bucket is partitioned into 8
  curation-scale splits covering GOA-supported transposases/integration
  proteins, domain-only or fragmentary transposase candidates, integrases,
  prophage structural/packaging proteins, phage DNA replication/processing,
  lysis/host-interaction proteins, regulatory/toxin-antitoxin candidates, and
  low-information prophage proteins.
- The first `transposase_goa_supported` split is complete: 18/18 review folders
  present, 18/18 review YAMLs curated, and 18/18 Asta reports present.
- Newly fetched and curated genes were `PP_0014`, `PP_0334`, `PP_0526`,
  `PP_0568`, `PP_1133`, `PP_1931`, `PP_2570`, `PP_2976`, `tnpB`, `PP_3498`,
  `PP_3499`, `PP_3966`, `insN`, `PP_4420`, `PP_4441`, `PP_4444`, `PP_4445`,
  and `PP_5176`.
- The `transposase_domain_or_fragment` split is complete: 22/22 review folders
  present, 22/22 review YAMLs curated, and 22/22 Asta reports present. Newly
  fetched and curated genes were `PP_0015`, `PP_0016`, `PP_0637`, `PP_0638`,
  `PP_0650`, `PP_3113`, `PP_3114`, `PP_3115`, `PP_3500`, `PP_3501`,
  `PP_3964`, `PP_3984`, `PP_3986`, `PP_4024`, `PP_4091`, `PP_4092`,
  `PP_4442`, `PP_4443`, `PP_4459`, `PP_5405`, `PP_5406`, and `PP_5408`.
- The `integrase_mobile_element_context` split is also complete: 3/3 review
  folders present, 3/3 review YAMLs curated, and 3/3 Asta reports present.
  Newly fetched and curated genes were `PP_1963`, `PP_2825`, and `PP_3677`.
- The `prophage_structural_packaging` split is complete: 21/21 review folders
  present, 21/21 review YAMLs curated, and 21/21 Asta reports present. Newly
  fetched and curated genes were `PP_1562`, `PP_1563`, `PP_1565`, `PP_1569`,
  `PP_1574`, `PP_1577`, `PP_2287`, `PP_2288`, `PP_3044`, `PP_3058`,
  `PP_3061`, `PP_3064`, `PP_3862`, `PP_3863`, `PP_3867`, `PP_3869`,
  `PP_3877`, `PP_3879`, `PP_3881`, `PP_3882`, and `PP_4135`.
- The `phage_lysis_host_interaction` split is complete: 2/2 review folders
  present, 2/2 review YAMLs curated, and 2/2 Asta reports present. Newly fetched
  and curated genes were `PP_1561` and `PP_4858`.
- The `phage_regulatory_toxin_antitoxin` split is complete: 3/3 review folders
  present, 3/3 review YAMLs curated, and 3/3 Asta reports present. Newly fetched
  and curated genes were `PP_2500`, `PP_5558`, and `PP_5626`.
- The `phage_dna_replication_processing` split is complete: 6/6 review folders
  present, 6/6 review YAMLs curated, and 6/6 Asta reports present. Newly fetched
  and curated genes were `PP_1551`, `PP_1552`, `PP_2267`, `PP_2268`,
  `PP_3864`, and `PP_3894`.
- The `low_information_prophage_proteins` split is complete: 14/14 review
  folders present, 14/14 review YAMLs curated, and 14/14 Asta reports present.
  Newly fetched and curated genes were `PP_1538`, `PP_1546`, `PP_1557`,
  `PP_1571`, `PP_2285`, `PP_3049`, `PP_3860`, `PP_3861`, `PP_3870`,
  `PP_3871`, `PP_3873`, `PP_3888`, `PP_3906`, and `PP_5637`.
- The reusable curation scripts are
  `projects/P_PUTIDA/curate_mobile_genetic_elements_transposase_goa_first_pass.py`,
  `projects/P_PUTIDA/curate_mobile_genetic_elements_transposase_domain_first_pass.py`,
  `projects/P_PUTIDA/curate_mobile_genetic_elements_integrase_first_pass.py`,
  `projects/P_PUTIDA/curate_mobile_genetic_elements_prophage_structural_packaging_first_pass.py`,
  `projects/P_PUTIDA/curate_mobile_genetic_elements_phage_lysis_regulatory_first_pass.py`,
  `projects/P_PUTIDA/curate_mobile_genetic_elements_low_information_prophage_first_pass.py`,
  and
  `projects/P_PUTIDA/curate_mobile_genetic_elements_phage_dna_processing_first_pass.py`.
- `modules/mobile_genetic_elements_boundary.yaml` was extended with a new
  broad-bucket GOA-supported transposase part and a new broad-bucket integrase
  context part, then extended again with a domain-supported IS66 transposase
  part while preserving the prior DNA-bucket mobile-element boundary annotons.
- New phage boundary modules were created and validated:
  `modules/phage_structural_packaging_boundary.yaml`,
  `modules/phage_lysis_host_interaction_boundary.yaml` and
  `modules/phage_regulation_toxin_antitoxin_boundary.yaml`, and
  `modules/phage_dna_replication_processing_boundary.yaml`.
- Partition/worklist regenerated. The broad mobile bucket now records 89/89
  review files, 89/89 curated review YAMLs, and 89/89 Asta reports; all eight
  partition sub-batches are complete.
- Gene review pages rendered for all 89 curated mobile-bucket genes; module pages
  rendered for `mobile_genetic_elements_boundary`,
  `phage_structural_packaging_boundary`,
  `phage_lysis_host_interaction_boundary`, and
  `phage_regulation_toxin_antitoxin_boundary`, and
  `phage_dna_replication_processing_boundary`.

Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/mobile_genetic_elements_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/mobile_genetic_elements_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/phage_lysis_host_interaction_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/phage_lysis_host_interaction_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/phage_regulation_toxin_antitoxin_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/phage_regulation_toxin_antitoxin_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/phage_dna_replication_processing_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/phage_dna_replication_processing_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/phage_structural_packaging_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/phage_structural_packaging_boundary.yaml
```

Main curation conclusions from this split:

- Explicit GOA-supported transposase records were curated as transposase
  activity in DNA transposition.
- Broad DNA-binding and sequence-specific DNA-binding rows were retained as
  non-core substrate/target-recognition context when a more specific transposase
  activity row was present.
- Four IS3/rve-family records (`PP_0014`, `tnpB`, `PP_4420`, `PP_4445`) have
  nucleic-acid binding, endonuclease/nuclease, DNA integration, recombination,
  and DNA transposition rows but no explicit GOA transposase-activity row. These
  were kept conservative as endonuclease activity in DNA transposition and
  integration, with parent nuclease/hydrolase rows marked over-annotated and no
  synthetic transposase row added.
- The domain-only/fragmentary transposase split is complete as a conservative
  first pass. Six full IS66 multi-domain proteins (`PP_0637`, `PP_3114`,
  `PP_3501`, `PP_3964`, `PP_4091`, and `PP_4443`) have `NEW`
  transposase-activity and DNA-transposition rows from combined IS66 central
  DDE, C-terminal, homeodomain-like, and zinc-finger domain evidence.
- The isolated IS66 Orf2/TnpB-like proteins (`PP_0638`, `PP_3113`, `PP_3500`,
  `PP_3986`, `PP_4024`, `PP_4092`, and `PP_4442`), IS66-C-only `PP_0650`,
  DUF6429 proteins (`PP_3115`, `PP_3984`), TniB/TniQ accessory/product-name
  candidates (`PP_0015`, `PP_0016`, `PP_5408`), product-only `PP_5405`, and
  mixed-domain broad-binding records (`PP_4459`, `PP_5406`) are retained as
  unresolved mobile-element context with no core GO function asserted.
- PP_2825 is the only supported member of the 3-gene integrase split: it has
  phage-integrase family/domain support and is curated as DNA binding directly
  involved in DNA integration, with a `NEW` DNA-integration row added from the
  UniProt flat-file cross-reference missing from the fetched GOA table.
- PP_1963 and PP_3677 are retained as unresolved product-name-only integrase
  candidates. Their reviews intentionally have no core function and therefore
  validate with the expected "No core functions defined" warning.
- The prophage structural/packaging split is complete as a conservative first
  pass. `PP_1563` and `PP_3881` retain terminase large-subunit endonuclease
  activity with a `NEW` virion-assembly process context.
- Domain-supported portal, head-tail connector, tail, tape-measure, tail-fiber,
  baseplate, tail-tube, sheath, capsid, and head proteins (`PP_1565`, `PP_1569`,
  `PP_1574`, `PP_1577`, `PP_2288`, `PP_3044`, `PP_3064`, `PP_3863`,
  `PP_3867`, `PP_3869`, `PP_3877`, `PP_3879`, and `PP_4135`) are curated as
  structural molecule activity in virion assembly.
- `PP_1562`, `PP_2287`, `PP_3058`, `PP_3061`, `PP_3862`, and `PP_3882` are
  retained as unresolved structural/packaging context with no core GO function:
  small terminase/product-only records lack a resolved MF, PP_2287 has mixed
  internal-core/Slt-domain evidence, and PP_3061/PP_3862 may be assembly
  accessory rather than structural components.
- The low-information prophage split is complete. `PP_1571`, `PP_3860`, and
  `PP_3871` have enough HK97 gp10, baseplate J/gp47, or tail-terminator domain
  evidence to be added to the structural/packaging module as structural molecule
  activity in virion assembly.
- `PP_2285` keeps its GOA symbiont-genome-ejection process row as non-core
  context because no GO molecular function is resolved. `PP_1538`, `PP_1546`,
  `PP_1557`, `PP_3049`, `PP_3861`, `PP_3870`, `PP_3873`, `PP_3888`,
  `PP_3906`, and `PP_5637` remain no-core low-information prophage/name-only
  or ambiguous-domain records.
- PP_1561 is curated from HNH nuclease evidence, not from the phage-holin
  product name. Its core function is endonuclease activity; nucleic-acid binding
  and zinc binding are retained as non-core domain/cofactor context.
- PP_4858 remains an unresolved signal-peptide-containing phage infection
  protein candidate with no core GO function asserted; it validates with the
  expected "No core functions defined" warning.
- PP_2500 is curated as a RelE/ParE-family toxin-antitoxin candidate with a
  conservative `NEW` toxin-activity row (`GO:0090729`) from InterPro/PANTHER/
  Pfam/family/keyword support, without asserting a specific RNA or DNA target.
- PP_5558 and PP_5626 are curated as phage-origin DNA-binding regulatory
  proteins. PP_5626 keeps regulation of DNA-templated transcription as process
  context, while its broad DNA-templated transcription row is modified toward
  the regulation term.
- PP_1551 and PP_3894 are curated as phage O-family replication proteins with
  `NEW` DNA replication origin binding from Phage_rep_O/VrpO/winged-helix domain
  evidence, directly involved in DNA replication.
- PP_1552 is curated conservatively as ATP binding in DNA replication context
  from IstB/P-loop NTPase evidence; no ATPase, helicase, or initiator-specific
  molecular activity is asserted in this first pass.
- PP_2267 is curated as a T7-like single-stranded DNA-binding protein. The broad
  DNA-binding GOA row is modified to `GO:0003697`, and a `NEW` DNA replication
  process row is added so the core ssDNA-binding function has explicit process
  support in `existing_annotations`.
- PP_2268 is curated as phage endodeoxyribonuclease activity in DNA-integration
  context; broad viral process is retained as non-core.
- PP_3864 remains an unresolved FluMu DNA-circulation candidate with
  DNA_circ_N/Pfam support but no core GO function asserted; its no-core
  validation warning is intentional.

## Batch status: ppu03060 / bacterial_protein_export

Batch files:

- `projects/P_PUTIDA/batches/ppu03060_bacterial_protein_export.tsv`
- `projects/P_PUTIDA/batches/ppu03060_bacterial_protein_export.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 19 candidates curated or rechecked: all KEGG `ppu03060` membership genes.
- 19/19 candidate review folders present. Missing folders were fetched for the
  Sec, SRP, YidC, signal-peptidase, and Tat candidates; `secD` and `secG`
  required UniProt accession plus alias fallbacks.
- 19/19 candidate Asta gene-level retrieval reports present. New Asta reports
  were added for 17 candidates, including the already fetched `ftsY`; existing
  overlap reviews `secA`, `ffh`, and `ftsY` were updated with lightweight Asta
  provenance.
- 19/19 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/bacterial_protein_export.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/bacterial_protein_export-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_protein_export__ppu03060-deep-research-falcon.md`.
- Validation complete for all 19 gene reviews and the module.
- Gene review pages rendered for all 19 candidates.
- Module page rendered:
  `pages/modules/bacterial_protein_export.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_protein_export.yaml
uv run python -m ai_gene_review.validation.module_validator modules/bacterial_protein_export.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu03060` is a bounded bacterial protein-export module, not a generic
  envelope-transport bucket.
- Sec export is represented by SecA, SecYEG, SecDF-YajC, and SecB. SecA is the
  ATPase motor; SecD, SecF, and SecG are therefore marked as over-annotated for
  standalone protein-transporting ATPase activity even though they remain valid
  export/translocon components.
- Ffh and FtsY capture SRP-dependent membrane-protein targeting, while YidC
  captures membrane-protein insertion.
- LepB and LspA represent signal-peptide processing, including type I signal
  peptidase and lipoprotein signal peptidase activity.
- Two TatABC-like loci are kept as twin-arginine translocation candidates, with
  the two clusters represented separately in the module activities.
- `yajC` and `secB` were kept conservative at the gene-review level where the
  fetched GOA seeds did not include stronger UniProt accessory/translocon or
  unfolded-protein-binding rows.
- Type I secretion and LolCDE are neighboring envelope/export modules, not part
  of this ppu03060 core.

## Batch status: ppu03070 / bacterial_secretion_system_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu03070_bacterial_secretion_system_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu03070_bacterial_secretion_system_boundary.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 42 primary candidates curated or rechecked. KEGG `ppu03070` has 61 total
  specific members, but the Sec/Tat/SRP/YidC overlap is assigned to
  `ppu03060` / `bacterial_protein_export`, so this batch uses
  `extract_pathway_batch.py --primary-only`.
- 42/42 primary review folders present. Seven genes required UniProt accession
  plus alias fallbacks during fetch: `gspF` (`Q88P05`), `PP_1449` (`Q88MW9`),
  `PP_2627` (`Q88JM2`), `PP_3106` (`Q88I93`), `PP_3478` (`Q88H83`),
  `PP_3483` (`Q88H78`), and `hcpC-II` (`Q88FK8`).
- 42/42 Asta gene-level retrieval reports present. `cyaB` already had Asta
  coverage; the remaining 41 reports were added in this pass.
- 42/42 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/bacterial_secretion_system_boundary.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/bacterial_secretion_system_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_secretion_system_boundary__ppu03070-deep-research-falcon.md`.
- Validation complete for all 42 primary gene reviews and the module.
- Gene review pages rendered for all 42 primary candidates.
- Module page rendered:
  `pages/modules/bacterial_secretion_system_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_secretion_system_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/bacterial_secretion_system_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu03070` is a secretion-system boundary bucket rather than an
  inner-membrane protein-export module; the Sec/Tat/SRP/YidC overlap remains
  in ppu03060.
- Xcp/Gsp components represent type-II secretion. Existing broad `protein
  secretion` rows were reviewed, but authored core functions prefer
  type-II-secretion process/complex terms where GOA support is present.
- `PP_1449`/`PP_1450` form a two-partner/type Vb secretion pair; PP_1450 is the
  outer-membrane transporter context, while PP_1449 is treated as the large
  passenger/adhesin-like partner.
- VgrG/Hcp/DotU/TssJ/TssM/ClpV-like loci define multiple T6SS neighborhoods,
  but many candidate effectors have no or minimal GOA rows. These were kept
  conservative, generally at apparatus-component or unresolved-effector level.
- PP_4926/CyaB are retained as type-I-secretion boundary context and not folded
  into the ppu03060 Sec/Tat protein-export module.

## Partition status: ppu02020 / two-component system umbrella

Partition files:

- `projects/P_PUTIDA/batches/ppu02020_two_component_system_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu02020_two_component_system_boundary.md`
- `projects/P_PUTIDA/batches/ppu02020_two_component_system_partition.tsv`
- `projects/P_PUTIDA/batches/ppu02020_two_component_system_partition.md`
- `projects/P_PUTIDA/partition_ppu02020_two_component.py`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- KEGG `ppu02020` has 217 total specific members and 99 primary PSEPK genes.
- The primary-only 99-gene checklist was generated as a partitioning input; all
  99 partition-table genes now have first-pass review and Asta coverage through
  their bucket modules or side-context placements.
- The pathway worklist now marks `kegg:ppu02020` as `PARTITIONED` with no
  single module file.
- `modules/two_component_relay.yaml` remains the reusable His-Asp phosphorelay
  motif; it should not be treated as the organism-specific ppu02020 umbrella.
- The generated partition table splits the 99 genes into 11 buckets:
  dicarboxylate/tricarboxylate transport regulation (19),
  heavy-metal/copper/zinc response and efflux (13), pili/surface adhesion (12),
  iron uptake regulation (10), ECF sigma/anti-sigma systems (10),
  nitrogen/phosphate/potassium homeostasis (10), orphan/generic TCS regulators
  (10), osmotic/envelope/efflux regulation (7), alginate/biofilm regulation
  (6), `dnaA` replication spillover (1), and `etp` protein-phosphatase
  spillover (1).
- The nitrogen/phosphate/potassium homeostasis sub-batch is now complete as a
  first-pass curation batch: `glnD`, `glnL`/NtrB, `ntrC`/GlnG, `phoB`,
  `phoR`, `kdpD`, `kdpE`, `kdpF`, `kdpA`, `kdpB`, and `kdpC` are represented
  in `modules/inorganic_nutrient_homeostasis_regulation_boundary.yaml`.
- Asta gene-level research is present for the ppu02020 nutrient-homeostasis
  genes that were newly fetched in this pass. `glnG` is represented by the
  existing `ntrC` review folder and was not duplicated.
- Falcon taxon-aware module/pathway research was attempted with the real
  `just module-pathway-deep-research-falcon inorganic_nutrient_homeostasis_regulation_boundary ppu02020 PSEPK`
  command and failed with Edison HTTP 402, so this sub-batch does not cite a
  Falcon report.
- The iron uptake regulation sub-batch is also complete as a first-pass
  curation batch: `pfeS-I`, `PP_0534`, `PP_1651`, `pfeS-II`, `fepA`,
  `PP_3576`, `fecI`, `PP_4607`, `PP_4611`, and `PP_4612` are represented in
  `modules/iron_uptake_regulation_boundary.yaml`.
- Asta gene-level research is present for all 10 iron-bucket genes. The
  curation separates PfeS/PfeR-like His-Asp pairs, TonB-dependent FepA
  siderophore-iron uptake, and FecI/FecR-like ECF sigma/anti-sigma regulation
  rather than treating the whole bucket as canonical two-component signaling.
- Falcon taxon-aware module/pathway research was attempted with the real
  `just module-pathway-deep-research-falcon iron_uptake_regulation_boundary ppu02020 PSEPK`
  command and failed with Edison HTTP 402, so this sub-batch does not cite a
  Falcon report.
- The osmotic/envelope/efflux regulation sub-batch is also complete as a
  first-pass curation batch: `ompR`, `envZ`, `PP_2100`, `evgA`, `mdtC`,
  `mdtB`, and `mdtA` are represented in
  `modules/osmotic_envelope_efflux_regulation_boundary.yaml`.
- Asta gene-level research is present for all seven genes. The curation keeps
  EnvZ/OmpR and PP_2100/EvgA-like phosphorelay regulation distinct from the
  MdtABC RND efflux pump context.
- Falcon taxon-aware module/pathway research was attempted with the real
  `just module-pathway-deep-research-falcon osmotic_envelope_efflux_regulation_boundary ppu02020 PSEPK`
  command and failed with Edison HTTP 402, so this sub-batch does not cite a
  Falcon report.
- The alginate/biofilm regulation sub-batch is also complete as a first-pass
  curation batch: `kinB`, `algB`, `algR`, `wspC`, `fleS`, and `PP_4696` are
  represented in `modules/alginate_biofilm_regulation_boundary.yaml`.
- Asta gene-level research is present for all six genes. The curation keeps
  KinB/AlgB alginate transcription control, AlgR-family transcription control,
  WspC/CheR1 biofilm methyltransferase context, and FleS/PP_4696
  surface-behavior regulatory context as a boundary rather than a single
  canonical His-Asp relay.
- Falcon taxon-aware module/pathway research was attempted with the real
  `just module-pathway-deep-research-falcon alginate_biofilm_regulation_boundary ppu02020 PSEPK`
  command and failed with Edison HTTP 402, so this sub-batch does not cite a
  Falcon report.
- The ECF sigma/anti-sigma sub-batch is also complete as a first-pass curation
  batch: `PP_0161`, `PP_0162`, `PP_0351`, `PP_0352`, `PP_0667`, `PP_0703`,
  `PP_0704`, `PP_0866`, `PP_3085`, and `PP_3086` are represented in
  `modules/ecf_sigma_anti_sigma_boundary.yaml`.
- Asta gene-level research is present for all 10 genes. The curation keeps
  local FecR-like anti-sigma/sensor plus ECF sigma-factor pairs separate from
  canonical His-Asp two-component relays, with `PP_0667` and `PP_0866`
  retained as orphan boundary context.
- Falcon taxon-aware module/pathway research was attempted with the real
  `just module-pathway-deep-research-falcon ecf_sigma_anti_sigma_boundary ppu02020 PSEPK`
  command and failed with Edison HTTP 402, so this sub-batch does not cite a
  Falcon report.
- The heavy-metal/copper/zinc response sub-batch is also complete as a
  first-pass curation batch: `czcR-I`, `czrSA`, `czcR-II`, `PP_1437`,
  `czcR-III`, `PP_2157`, `copR-I`, `copR-II`, `copS`, `czcC`, `cusB`,
  `cusA`, and `cusF` are represented in
  `modules/metal_cation_response_efflux_boundary.yaml`.
- Asta gene-level research is present for all 13 genes. The curation keeps
  CusR/CopR-like response regulators, CztS/SilS/CopS-like sensor kinases, and
  the czcC-cusBAF copper/cation RND efflux locus as a metal-response boundary;
  `cusF` had no GOA rows, so missing copper-efflux terms were represented as
  `NEW` review entries backed by UniProt/Asta evidence.
- Falcon taxon-aware module/pathway research was attempted with the real
  `just module-pathway-deep-research-falcon metal_cation_response_efflux_boundary ppu02020 PSEPK`
  command and failed with Edison HTTP 402, so this sub-batch does not cite a
  Falcon report.
- The pili/surface-adhesion sub-batch is also complete as a first-pass
  curation batch: `pilA`, `fimD`, `PP_1890`, `PP_2356`, `PP_2357`,
  `PP_2358`, `PP_2359`, `PP_2360`, `PP_2361`, `PP_2362`, `PP_2363`, and
  `PP_3126` are represented in
  `modules/pili_surface_adhesion_boundary.yaml`.
- Asta gene-level research is present for all 12 genes. The curation keeps
  `pilA` as type IV pilin/twitching-motility and adhesion context, separates
  FimD/Csu-like usher-chaperone pilus assembly from the PP_2356
  phytochrome-like histidine kinase, and retains `PP_3126` as a polysaccharide
  export side node; Csu-like subunits and chaperones with no GOA rows were
  represented with `NEW` review entries backed by UniProt/Asta evidence.
- Falcon taxon-aware module/pathway research was attempted with the real
  `just module-pathway-deep-research-falcon pili_surface_adhesion_boundary ppu02020 PSEPK`
  command and failed with Edison HTTP 402, so this sub-batch does not cite a
  Falcon report.
- The Dct/Tct transport-regulation sub-batch is also complete as a first-pass
  curation batch: `dctD-I`, `PP_0264`, `uhpA`, `dctD-II`, `PP_1067`,
  `PP_1167`, `PP_1168`, `dctP`, `dctA`, `dctD-III`, `dctB`, `PP_1416`,
  `PP_1417`, `PP_1418`, `tctD`, `PP_1421`, `dctA-II`, `dctA-III`, and
  `PP_3124` are represented in
  `modules/dicarboxylate_tricarboxylate_transport_regulation_boundary.yaml`.
- Asta gene-level research is present for all 19 genes. The curation keeps
  DctD/DctB-like regulatory pairs, UhpA side-context regulation, the DctPQM
  TRAP C4-dicarboxylate importer, DctA-family succinate/fumarate/malate
  symporters, the TctABC/TctD-like tricarboxylate locus, and the PP_3124
  short-chain fatty-acid transporter as a transport-regulatory boundary rather
  than one canonical His-Asp relay; TctABC had no GOA rows, so missing
  tricarboxylate transporter/process and membrane-location terms were
  represented with `NEW` review entries backed by UniProt/Asta evidence.
- Falcon taxon-aware module/pathway research was attempted with the real
  `just module-pathway-deep-research-falcon dicarboxylate_tricarboxylate_transport_regulation_boundary ppu02020 PSEPK`
  command and failed with Edison HTTP 402, so this sub-batch does not cite a
  Falcon report.
- The orphan/generic TCS regulator sub-batch is also complete as a first-pass
  curation batch: `PP_0574`, `PP_0887`, `regA`, `PP_1007`, `bvgA`,
  `PP_1181`, `PP_1182`, `PP_2671`, `PP_3412`, and `PP_3413` are represented
  in `modules/orphan_two_component_regulators_boundary.yaml`.
- Asta gene-level research is present for all 10 genes. The curation records
  PP_0887/regA, PP_1182/PP_1181, and PP_3413/PP_3412 as generic adjacent
  TCS branches; keeps PP_0574, bvgA, and PP_2671 as orphan regulatory side
  branches; and treats PP_1007 as FecR-like anti-sigma context rather than a
  canonical His-Asp sensor kinase.
- Falcon taxon-aware module/pathway research was attempted with the real
  `just module-pathway-deep-research-falcon orphan_two_component_regulators_boundary ppu02020 PSEPK`
  command and failed with Edison HTTP 402, so this sub-batch does not cite a
  Falcon report.
- The `dnaA` replication spillover is complete as side context: `dnaA` has a
  first-pass review and Asta report, and
  `modules/bacterial_dna_replication.yaml` now includes DnaA
  replication-origin binding/initiation context from ppu02020.
- The `etp` protein-phosphatase spillover is complete as side context: `etp`
  has a first-pass review and Asta report, and
  `modules/protein_phosphorylation_boundary.yaml` records Etp protein tyrosine
  phosphatase/protein-dephosphorylation context.

Main curation conclusions from this partition:

- Do not open a single 99-gene ppu02020 curation PR.
- True two-component relays, ECF sigma/anti-sigma systems, regulated transport
  operons, efflux systems, pili/surface structures, and housekeeping side nodes
  need separate boundary modules.
- ppu02020-derived first-pass curation coverage is complete for all 99 primary
  genes, but the pathway remains a partitioned umbrella rather than one
  satisfiable module.
- `dnaA` and `etp` are side-context spillovers and should not be used as
  evidence for two-component signaling.

## Partition status: ppu02024 / quorum-sensing umbrella

Partition files:

- `projects/P_PUTIDA/batches/ppu02024_quorum_sensing_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu02024_quorum_sensing_boundary.md`
- `projects/P_PUTIDA/batches/ppu02024_quorum_sensing_partition.tsv`
- `projects/P_PUTIDA/batches/ppu02024_quorum_sensing_partition.md`
- `projects/P_PUTIDA/partition_ppu02024_quorum_sensing.py`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- KEGG `ppu02024` has 84 total specific members and 60 primary PSEPK genes.
- The primary-only 60-gene checklist was generated as a partitioning input, not
  as a curation-complete batch.
- The pathway worklist now marks `kegg:ppu02024` as `PARTITIONED` with no
  single module file.
- The generated partition table splits the 60 genes into 9 buckets:
  branched-chain amino-acid ABC import (25), polyamine ABC import (13),
  peptide/opine/glutathione ABC import (8), QseBC-like two-component
  regulation (5), phosphonate/AEP ABC import (4), RND multidrug efflux (2),
  Fur/iron-regulation spillover (1), surface-adhesion singleton (1), and DMT
  transporter singleton (1).

Main curation conclusions from this partition:

- Do not open a single 60-gene ppu02024 quorum-sensing PR.
- The primary PSEPK membership does not provide a compact LuxI/LuxR
  autoinducer-synthesis/reception module.
- The largest ppu02024 buckets are transport modules that already overlap ABC
  transporter partitioning.
- The most quorum-adjacent concrete submodule is QseBC-like two-component
  regulation (`PP_2713`, `PP_2714`, `kdpE`, `PP_4224`, `qseB`).
- Polyamine import may be biologically adjacent to signaling and biofilm
  behavior, but should be curated as transport unless direct regulatory
  evidence changes the boundary.
- Completed `rnd_multidrug_efflux`: two genes present, Asta-backed, first-pass
  curated, validated, and rendered; new module
  `modules/rnd_multidrug_efflux_boundary.yaml` created, validated, and
  rendered.
- The RND efflux pass treats PP_2064 as the membrane-fusion/adaptor component
  contributing to pump-level efflux activity, while PP_2065 is retained as the
  inner-membrane RND xenobiotic transporter. This remains side-context for the
  ppu02024 umbrella rather than direct quorum-sensing biology.
- Completed `qsebc_like_two_component_regulation`: five genes present,
  Asta-backed, first-pass curated, validated, and rendered; new module
  `modules/qsebc_like_two_component_regulation_boundary.yaml` created,
  validated, and rendered.
- The QseBC-like pass treats PP_2714-PP_2713 and PP_4224-qseB as plausible
  local sensor kinase/response regulator pairs, while kdpE remains a related
  KdpE-like DNA-binding response activator side branch with unresolved sensor
  partner and regulon. This is the most regulatory ppu02024 bucket, but direct
  quorum-signal reception is not established.
- Completed `phosphonate_abc_import`: four genes present, Asta-backed,
  first-pass curated, validated, and rendered; existing module
  `modules/phosphonate_phosphinate_metabolism.yaml` extended, validated, and
  rendered.
- The phosphonate pass treats PP_1722 as the ABC ATP-binding energy-coupling
  subunit, PP_1723 and PP_1724 as 2-aminoethylphosphonate/AEP permeases, and
  PP_1726 as the periplasmic binding component. PP_1726's electronic thiamine
  binding/transport terms were removed or replaced with phosphonate import
  context, while substrate range and direct PhnW handoff remain knowledge gaps.
- Completed `peptide_opine_glutathione_abc_import`: eight genes present,
  Asta-backed, first-pass curated, validated, and rendered; new module
  `modules/peptide_opine_glutathione_abc_import_boundary.yaml` created,
  validated, and rendered.
- The peptide/opine/glutathione pass treats PP_3220-PP_3223 as a compact
  dipeptide-like ABC import locus. gsiA and gsiC carry the glutathione-import
  call, while PP_4454 and PP_4458 retain opine-like/periplasmic-binding context
  without forcing glutathione specificity across the whole locus.
- Completed `polyamine_abc_import`: thirteen genes present, Asta-backed,
  first-pass curated, validated, and rendered; existing module
  `modules/polyamine_transport_boundary.yaml` extended, validated, and
  rendered.
- The polyamine pass treats PP_0411-PP_0414, ydcV/ydcU/ydcT/ydcS, and
  PP_3814-PP_3817 as predicted polyamine ABC import loci. PP_2870 is retained
  as a spermidine/putrescine-binding singleton with unresolved transporter
  partners. PP_3814's TreeGrafter thiamine-specific calls were removed or
  replaced with polyamine binding/transport context. After rebuilding the
  partition and pathway worklist, ppu02024 has 57/60 primary review folders and
  57/60 Asta reports; only the three singleton side-context buckets remain.
- Completed the three remaining ppu02024 singleton side-context buckets.
  `fur__Q88RL0` (PP_0119 Fur-family regulator), `PP_0806` (large surface
  adhesion protein), and `PP_3609` (DMT/YdcZ-family transporter) are present,
  Asta-backed, first-pass curated, validated, and rendered. New modules
  `modules/iron_homeostasis_regulation_boundary.yaml`,
  `modules/surface_adhesion_boundary.yaml`, and
  `modules/dmt_transporter_boundary.yaml` were created, validated, and
  rendered.
- The singleton pass treats PP_0119/fur__Q88RL0 as Fur-family iron-homeostasis
  transcriptional regulation side context, PP_0806 as broad
  surface-adhesion/biofilm-boundary context, and PP_3609 as a generic
  DMT-family membrane transporter with substrate unresolved. After rebuilding
  the partition and pathway worklist, ppu02024 has 60/60 primary review folders
  and 60/60 Asta reports. The pathway remains a partitioned umbrella rather
  than one satisfiable quorum-sensing module.

## Partition status: ppu02025 / biofilm-formation umbrella

Partition files:

- `projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_boundary.md`
- `projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_partition.tsv`
- `projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_partition.md`
- `projects/P_PUTIDA/partition_ppu02025_biofilm.py`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- KEGG `ppu02025` has 62 total specific members and 43 primary PSEPK genes.
- The primary-only 43-gene checklist was generated as a partitioning input; the
  Wsp-like surface-sensing/c-di-GMP, c-di-GMP turnover, Pil/Chp
  twitching-regulation, Gac/Csr/Crp global-regulation, T6SS
  secretion-boundary context, and orphan regulatory-sensor sub-buckets are now
  first-pass complete.
- The pathway worklist now marks `kegg:ppu02025` as `PARTITIONED` with no
  single module file.
- After all six ppu02025 sub-batches, the ppu02025 worklist row has 43/43
  review files, 43/43 curated reviews, and 43/43 Asta gene-level reports.
- The generated partition table splits the 43 genes into 6 buckets: T6SS/biofilm
  context (13), orphan biofilm regulatory sensors (8), global Gac/Csr/Crp
  regulation (6), Wsp-like chemotaxis/c-di-GMP cluster (6), Pil/Chp twitching
  regulation (6), and c-di-GMP turnover (4).
- The Wsp-like chemotaxis/c-di-GMP sub-batch is complete as a first-pass
  curation batch: `PP_1488`, `PP_1489`, `PP_1491`, `PP_1492`, `cheB3`, and
  `PP_1494` are represented in
  `modules/wsp_surface_sensing_c_di_gmp_boundary.yaml`, with already curated
  `wspC`/PP_1490 included as local Wsp/CheR1 methyltransferase context.
- Asta gene-level research is present for all six Wsp-like sub-batch genes. The
  curation keeps this branch as a surface-sensing/c-di-GMP boundary rather than
  the canonical flagellar chemotaxis core.
- Falcon taxon-aware module/pathway research was attempted with the real
  `just module-pathway-deep-research-falcon wsp_surface_sensing_c_di_gmp_boundary ppu02025 PSEPK`
  command and failed with Edison HTTP 402, so this sub-batch does not cite a
  Falcon report.
- The c-di-GMP turnover sub-batch is complete as a first-pass curation batch:
  `PP_0914`, `PP_3581`, `TpbB`, and `pde` are represented in
  `modules/c_di_gmp_turnover_boundary.yaml`. `PP_0914` and `PP_3581` are EAL
  cyclic-guanylate phosphodiesterase candidates, `TpbB` is a membrane-associated
  GGDEF diguanylate cyclase candidate, and `pde` is retained only as broad
  3',5'-cyclic-nucleotide phosphodiesterase side context.
- Asta gene-level research is present for all four c-di-GMP turnover sub-batch
  genes. Falcon taxon-aware module/pathway research was attempted with the real
  `just module-pathway-deep-research-falcon c_di_gmp_turnover_boundary ppu02025 PSEPK`
  command and failed with Edison HTTP 402, so this sub-batch does not cite a
  Falcon report.
- The Pil/Chp twitching-regulation sub-batch is complete as a first-pass
  curation batch: `PP_4987`, `PP_4988`, `pilJ`, `pilI`, `pilH`, and `pilG` are
  represented in `modules/pil_chp_twitching_motility_boundary.yaml`. The pass
  keeps `pilJ` as a PilJ/MCP-like membrane transducer, `PP_4987` and `pilI` as
  CheW-like adaptor candidates, `PP_4988` as the CheA-family histidine kinase,
  and `pilH`/`pilG` as receiver-domain response-regulator candidates.
- Asta gene-level research is present for all six Pil/Chp sub-batch genes. The
  review pass adds `NEW` phosphorelay response regulator activity entries for
  `pilH` and `pilG`, while retaining type IV pilus-dependent motility as
  module/pathway context rather than a directly proven gene-level output for
  every component. Falcon taxon-aware module/pathway research was attempted with
  the real
  `just module-pathway-deep-research-falcon pil_chp_twitching_motility_boundary ppu02025 PSEPK`
  command and failed with Edison HTTP 402, so this sub-batch does not cite a
  Falcon report.
- The Gac/Csr/Crp global-regulation sub-batch is complete as a first-pass
  curation batch: `crp`, `gacS`, `gacA`/`uvrY`, `csrA__Q88M29`, `csrA__Q88G93`,
  and `csrA__Q88EJ0` are represented in
  `modules/global_biofilm_regulation_boundary.yaml`. `gacS` and `gacA` form the
  Gac phosphorelay, the three CsrA paralogs are distinct accession-scoped
  CsrA/RsmA-family mRNA 5-prime UTR-binding regulators, and `crp` is a
  cAMP-responsive CRP-family transcription activator.
- Asta gene-level research is present for all six Gac/Csr/Crp sub-batch genes.
  The `crp` pass adds a `NEW` cAMP-binding annotation from UniProt
  domain/keyword support, while the ppu02025 `uvrY` row is represented by the
  existing `gacA` folder with `uvrY` as an alias. Falcon taxon-aware
  module/pathway research was attempted with the real
  `just module-pathway-deep-research-falcon global_biofilm_regulation_boundary ppu02025 PSEPK`
  command and failed with Edison HTTP 402, so this sub-batch does not cite a
  Falcon report.
- The T6SS/biofilm-context bucket is complete as a first-pass reuse batch:
  `PP_2617`, `PP_2620`, `PP_2623`, `PP_2624`, `PP_3088`, `PP_3093`,
  `PP_3096`, `puuD`, `PP_3100`, `PP_4074`, `PP_4078`, `PP_4080`, and
  `PP_5561` are represented in `modules/bacterial_secretion_system_boundary.yaml`
  rather than a separate biofilm-specific module.
- Asta gene-level research is present for all 13 T6SS-context genes. The pass
  treats TssA/TssB/TssC/TssG/TssK and TagF-family proteins as T6SS apparatus or
  accessory context, and marks the EC-derived urate oxidase activity annotation
  on `puuD`/PP_3099 for removal because the domain evidence supports a
  TssC/VipB-family sheath protein.
- The orphan regulatory-sensor bucket is complete as a conservative first-pass
  curation batch: `PP_1875`, `PP_2664`, `PP_4173`, `PP_4362`, `PP_4363`,
  `PP_4364`, `PP_4781`, and `PP_4824`/`retS` are represented in
  `modules/orphan_biofilm_regulatory_sensors_boundary.yaml`.
- Asta gene-level research is present for all eight orphan regulatory-sensor
  rows. The pass keeps ligand identities, response-regulator partners, and
  target regulons unresolved except for the existing KT2440 `retS` K1-T6SS
  regulatory evidence.

Main curation conclusions from this partition:

- Do not open a single 43-gene ppu02025 biofilm-formation PR.
- The map is a *Pseudomonas aeruginosa* biofilm umbrella and mixes regulatory,
  chemotaxis, c-di-GMP, type IV pilus, and T6SS context.
- T6SS apparatus genes stay with `bacterial_secretion_system_boundary`; this
  reuse batch is first-pass complete and should not be split into a standalone
  biofilm module without a specific regulation question.
- All six ppu02025-derived sub-batches are now first-pass complete. The orphan
  regulatory sensors are retained as an unresolved regulatory-sensor boundary,
  not as direct per-gene biofilm-output assertions.

## Partition status: ppu02030 / bacterial-chemotaxis umbrella

Partition files:

- `projects/P_PUTIDA/batches/ppu02030_bacterial_chemotaxis_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu02030_bacterial_chemotaxis_boundary.md`
- `projects/P_PUTIDA/batches/ppu02030_bacterial_chemotaxis_partition.tsv`
- `projects/P_PUTIDA/batches/ppu02030_bacterial_chemotaxis_partition.md`
- `projects/P_PUTIDA/partition_ppu02030_chemotaxis.py`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- KEGG `ppu02030` has 48 total specific members and 41 primary PSEPK genes.
- The primary-only 41-gene checklist was generated as a partitioning input, not
  as a curation-complete batch.
- The pathway worklist now marks `kegg:ppu02030` as `PARTITIONED` with no
  single module file.
- The generated partition table splits the 41 genes into 5 buckets: orphan
  MCP/aerotaxis receptors (13), known or named MCP receptor panel (9),
  periplasmic binding/transport spillovers (7), core Che signal-transduction
  cluster (6), and chemotaxis adaptation/accessory proteins (6).

Main curation conclusions from this partition:

- Do not open a single 41-gene ppu02030 bacterial-chemotaxis PR.
- The map is a valid biological domain but mixes receptor discovery, core Che
  signaling, adaptation proteins, and transport-binding side context.
- Dipeptide, ribose, and sugar-binding proteins should stay with transport
  modules unless direct receptor-level chemotaxis evidence is selected.
- Completed `chemotaxis_core_che_cluster`: six core Che-cluster genes present,
  Asta-backed, first-pass curated, validated, and rendered; new module
  `modules/bacterial_chemotaxis_core_boundary.yaml` created, validated, and
  rendered.
- Asta retrieval was checked for all six core genes, but PP_4332/PP_4333/cheB1
  curation relied mainly on UniProt, GOA, domain, and local cluster evidence
  because Asta did not return curation-changing organism-specific papers.
- Completed `chemotaxis_adaptation_accessory`: six adaptation/accessory genes
  present, Asta-backed, first-pass curated, validated, and rendered; new module
  `modules/chemotaxis_adaptation_accessory_boundary.yaml` created, validated,
  and rendered.
- The adaptation/accessory pass separates CheR2 from CheR3: CheR2 is the
  chemotaxis receptor methyltransferase supported by UniProt and PMID:23677992,
  while CheR3 remains a broad unresolved methyltransferase candidate. PP_3759 is
  retained as the methylesterase, with response-regulator/phosphorelay
  over-propagation removed or down-weighted.
- Completed `known_named_mcp_receptor_panel`: nine named MCP receptor genes
  present, Asta-backed, first-pass curated, validated, and rendered; new module
  `modules/chemotaxis_receptor_panel_boundary.yaml` created, validated, and
  rendered.
- The receptor-panel pass retains characterized specificity for McpH
  (purine derivatives), McpU (polyamines), McpG (GABA), McpA (proteinogenic
  amino acids), PcaY (C6-ring carboxylic acids), McpP (C2/C3 carboxylates),
  McpS (TCA-cycle intermediates and related organic acids), and McpQ
  (citrate/citrate-metal complexes). CtpL is retained as a named MCP-family
  receptor candidate with unresolved KT2440 ligand specificity.
- Completed `orphan_mcp_aerotaxis_receptors`: thirteen orphan MCP/aerotaxis
  receptor genes present, Asta-backed, first-pass curated, validated, and
  rendered; new module
  `modules/orphan_mcp_aerotaxis_receptors_boundary.yaml` created, validated,
  and rendered.
- The orphan-receptor pass retains generic MCP/sensory-box genes as
  chemotaxis receptor/transducer candidates without assigning ligand
  specificity, retains PP_2111/PP_2257/PP_4521 as aerotaxis receptor
  candidates, and removes PP_2111 SNAP receptor activity, intracellular
  protein transport, and membrane fusion as SNARE-derived electronic spillover.
- Concrete ppu02030 chemotaxis first-pass sub-batches are now complete: core
  Che signaling, adaptation/accessory proteins, named receptors, and the
  orphan MCP/aerotaxis receptor boundary.
- Periplasmic binding/transport spillovers should stay with transport modules
  unless direct receptor-level chemotaxis evidence is selected.

## Partition status: module:chromosome_partition_cell_cycle

Partition files:

- `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_partition.tsv`
- `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_partition.md`
- `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_min_system.tsv`
- `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_min_system.md`
- `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_divisome.tsv`
- `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_divisome.md`
- `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_xer_ftsk.tsv`
- `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_xer_ftsk.md`
- `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_tol_pal.tsv`
- `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_tol_pal.md`
- `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_partition_condensation.tsv`
- `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_partition_condensation.md`
- `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_spillovers.tsv`
- `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_spillovers.md`
- `projects/P_PUTIDA/partition_chromosome_cell_cycle.py`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- The functional `module:chromosome_partition_cell_cycle` bucket has 37 primary
  PSEPK genes from UniProt name/keyword assignment.
- The pathway worklist now marks `module:chromosome_partition_cell_cycle` as
  `PARTITIONED` with no single module file.
- The generated partition table splits the 37 genes into 6 buckets:
  chromosome partition/condensation (11), divisome/Z-ring/septation (12),
  Tol-Pal envelope/division coordination (5), Xer/FtsK chromosome-resolution and
  DNA translocation (4), MinCDE septum-site selection (3), and broad keyword
  spillovers (2).
- Completed `min_system_septum_site_selection_boundary`: `minC`, `minD`, and
  `minE` are fetched, Asta-backed, first-pass curated, validated, and
  represented in `modules/min_system_septum_site_selection_boundary.yaml`.
- Completed `divisome_z_ring_septation_boundary`: `engB`, `PP_1309`, `zapE`,
  `ftsL`, `ftsQ`, `ftsA`, `ftsZ`, `ftsB`, `dedD`, `zipA`, `PP_5090`, and
  `PP_5202` are fetched or reused, Asta-backed, first-pass curated, validated,
  and represented in `modules/divisome_z_ring_septation_boundary.yaml`.
- Completed `chromosome_dimer_resolution_dna_translocation_boundary`: `xerC`,
  `xerD`, `ftsK`, and `PP_2841` are fetched, Asta-backed, first-pass curated,
  validated, and represented in
  `modules/chromosome_dimer_resolution_dna_translocation_boundary.yaml`.
- Completed `tol_pal_cell_division_envelope_coordination_boundary`: `tolQ`,
  `tolR`, `tolA`, `tolB`, `pal`, and `cpoB` are fetched or reused,
  Asta-backed, first-pass curated, validated, and represented in
  `modules/tol_pal_cell_division_envelope_coordination_boundary.yaml`. `tolA`
  was promoted from the broad transport/membrane bucket as hole filling.
- Completed `chromosome_partition_condensation_boundary`: `parB`, `PP_0002`,
  `PP_0693`, `PP_0694`, `PP_2161`, `PP_2412`, `PP_3700`, `smc`,
  `PP_4334`, `PP_4497`, `scpA`, and `PP_5070` are fetched, Asta-backed,
  first-pass curated, validated, and represented in
  `modules/chromosome_partition_condensation_boundary.yaml`. `PP_0002` was
  promoted from `unknown:function_unknown` as the origin-proximal Soj/ParA-like
  hole-fill candidate next to `parB`.
- Closed `side_spillover_general_cell_cycle_terms`: `PP_1105` and `tig` are
  fetched or reused, Asta-backed, first-pass curated, validated, and routed out
  of chromosome/cell-cycle modules. `PP_1105` belongs with ATP-dependent DNA
  ligase/DNA repair context, and `tig` belongs with trigger-factor
  chaperone/cotranslational protein-folding context.
- The aggregate pathway worklist reports 37/37 primary review files and 37/37
  Asta files for this functional bucket.
- The Min-system module validates with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/min_system_septum_site_selection_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/min_system_septum_site_selection_boundary.yaml
```

- The divisome/Z-ring module validates with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/divisome_z_ring_septation_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/divisome_z_ring_septation_boundary.yaml
```

- The Xer/FtsK chromosome dimer resolution module validates with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/chromosome_dimer_resolution_dna_translocation_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/chromosome_dimer_resolution_dna_translocation_boundary.yaml
```

- The Tol-Pal envelope/division module validates with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/tol_pal_cell_division_envelope_coordination_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/tol_pal_cell_division_envelope_coordination_boundary.yaml
```

- The chromosome partition/condensation module validates with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/chromosome_partition_condensation_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/chromosome_partition_condensation_boundary.yaml
```

- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/min_system_septum_site_selection_boundary-deep-research-falcon.md`.
- Falcon generic module research for the divisome/Z-ring boundary was also
  attempted with the real module-level command and failed while Edison Falcon
  access returns HTTP 402:
  `modules/divisome_z_ring_septation_boundary-deep-research-falcon.md`.
- Falcon generic module research for the Xer/FtsK boundary was also attempted
  with the real module-level command and failed while Edison Falcon access
  returns HTTP 402:
  `modules/chromosome_dimer_resolution_dna_translocation_boundary-deep-research-falcon.md`.
- Falcon generic module research for the Tol-Pal boundary was also attempted
  with the real module-level command and failed while Edison Falcon access
  returns HTTP 402:
  `modules/tol_pal_cell_division_envelope_coordination_boundary-deep-research-falcon.md`.
- Falcon generic module research for the chromosome partition/condensation
  boundary was also attempted with the real module-level command and failed
  while Edison Falcon access returns HTTP 402:
  `modules/chromosome_partition_condensation_boundary-deep-research-falcon.md`.

Main curation conclusions from this partition:

- Do not curate the 37-gene chromosome/cell-cycle functional bucket as one
  satisfiable module.
- MinCDE is a coherent first completed sub-batch: MinC inhibits inappropriate
  polar FtsZ ring and septum formation, MinD is the ParA/MinD-family ATPase at
  the cytoplasmic side of the plasma membrane, and MinE provides topological
  specificity by counteracting MinC/MinD inhibition at internal division sites.
- The divisome/Z-ring/septation sub-batch is also complete: FtsZ remains the
  central Z-ring GTPase, FtsA/ZipA are membrane/Z-ring anchors, FtsB/FtsL/FtsQ
  form the conserved divisome subcomplex, ZapA/ZapE/ZapG/EngB are retained as
  accessory or regulatory factors, and DedD/PP_5090 are SPOR/RlpA-like
  peptidoglycan-binding septal boundary proteins.
- The Xer/FtsK chromosome dimer resolution sub-batch is complete: XerC and
  XerD are the core cytoplasmic tyrosine recombinases, FtsK is the septal
  membrane DNA translocase coupling chromosome segregation with division, and
  PP_2841 is retained only as a related integrase-family boundary candidate.
- The Tol-Pal envelope/division coordination sub-batch is complete: TolQ/TolR
  are the inner-membrane energy-coupling arm, TolA is promoted hole filling as
  the missing connector, TolB/Pal are the periplasmic/outer-membrane bridge,
  and CpoB is the adjacent periplasmic envelope-constriction coordinator.
  TolA's chromatin/nucleosome GOA terms were removed as electronic spillover.
- The chromosome partition/condensation sub-batch is complete: parB and
  promoted PP_0002 cover the origin-proximal ParB/Soj-like candidate pair,
  PP_0693/PP_0694 are retained as MksEF-like condensin candidates, ParA-family
  side ATPases remain provisional, and Smc-ScpA-ScpB is the strongest
  condensation/segregation submodule.
- The broad keyword spillovers are closed: PP_1105 is an ATP-dependent DNA
  ligase for DNA repair/contextual DNA metabolism, and tig is trigger factor
  for cotranslational protein folding. Both stay outside chromosome/cell-cycle
  modules unless future evidence ties them directly to a cell-cycle mechanism.

## Partition status: module:motility_chemotaxis_biofilm

Partition files:

- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_partition.tsv`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_partition.md`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_type_iv_pilus_biogenesis_boundary.tsv`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_type_iv_pilus_biogenesis_boundary.md`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_fimbrial_type1_surface_adhesion_extension.tsv`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_fimbrial_type1_surface_adhesion_extension.md`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_hcp_t6ss_product_name_spillover.tsv`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_hcp_t6ss_product_name_spillover.md`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_alginate_envelope_and_lyase_context.tsv`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_alginate_envelope_and_lyase_context.md`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_orphan_mcp_chemotaxis_receptor_candidates.tsv`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_orphan_mcp_chemotaxis_receptor_candidates.md`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_sensory_c_di_gmp_pde_spillover.tsv`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_sensory_c_di_gmp_pde_spillover.md`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_dna_binding_response_regulator_spillover.tsv`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_dna_binding_response_regulator_spillover.md`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_chey_like_membrane_accessory_spillovers.tsv`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_chey_like_membrane_accessory_spillovers.md`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_outer_membrane_flagellation_name_spillover.tsv`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_outer_membrane_flagellation_name_spillover.md`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_flagellar_export_localization_accessory_spillovers.tsv`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_flagellar_export_localization_accessory_spillovers.md`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_c_di_gmp_flagellar_brake_spillover.tsv`
- `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_c_di_gmp_flagellar_brake_spillover.md`
- `projects/P_PUTIDA/partition_motility_chemotaxis_biofilm.py`

Status as of 2026-07-09 PDT / 2026-07-10 UTC:

- The functional `module:motility_chemotaxis_biofilm` bucket has 35 primary
  PSEPK genes from UniProt name/keyword assignment.
- The pathway worklist marks `module:motility_chemotaxis_biofilm` as
  `PARTITIONED` with no single module file.
- The generated partition table splits the 35 genes into 11 buckets: type IV
  pilus biogenesis/assembly (12), fimbrial/type-I-pilus surface-adhesion
  extension (2), Hcp/T6SS product-name spillover (1), alginate envelope/export
  and lyase context (5), orphan MCP chemotaxis receptors (3), sensory c-di-GMP
  phosphodiesterase spillover (1), DNA-binding response-regulator spillover
  (1), CheY-like/membrane accessory spillovers (3), outer-membrane
  flagellation-name spillover (1), flagellar export/localization/accessory
  spillovers (5), and c-di-GMP flagellar brake context (1).
- Completed `type_iv_pilus_biogenesis_boundary`: `PP_0608`, `PP_0609`,
  `PP_0610`, `pilE`, `pilC`, `pilF`, `PP_3480`, `PP_3481`, `pilQ`,
  `PP_5081`, `pilN`, and `PP_5083` are fetched, Asta-backed, first-pass
  curated, validated, rendered, and represented in new
  `modules/type_iv_pilus_biogenesis_boundary.yaml`. The module records `pilD`
  and `pilT` as explicit hole-filling gaps for a later pass.
- Completed `fimbrial_type1_surface_adhesion_extension`: `PP_1888` and `fimI`
  are fetched, Asta-backed, first-pass curated, validated, and represented as
  predicted fimbrial structural-subunit candidates in the existing
  `modules/pili_surface_adhesion_boundary.yaml`.
- Completed `hcp_t6ss_product_name_spillover`: `PP_0655` is fetched,
  Asta-backed, first-pass curated, validated, and routed to
  `modules/bacterial_secretion_system_boundary.yaml` as an Hcp-family type VI
  secretion tube or secreted-effector candidate despite the generic
  fimbrial-protein-related product name.
- Completed `alginate_envelope_and_lyase_context`: `glmP`, `PP_1754`,
  `PP_3350`, `PP_3464`, and `PP_3774` are fetched, Asta-backed, first-pass
  curated, validated, rendered, and represented in
  `modules/alginate_biosynthesis_boundary.yaml` as alginate-efficiency,
  export-domain, and alginate-lyase-domain boundary context.
- Completed `orphan_mcp_chemotaxis_receptor_candidates`: `PP_2310`,
  `PP_3950`, and `PP_4888` are fetched, Asta-backed, first-pass curated,
  validated, rendered, and represented in
  `modules/orphan_mcp_aerotaxis_receptors_boundary.yaml` as ligand-unresolved
  MCP receptor/transducer candidates.
- Completed `sensory_c_di_gmp_pde_spillover`: `PP_2599` is fetched,
  Asta-backed, first-pass curated, validated, rendered, and represented in
  `modules/c_di_gmp_turnover_boundary.yaml` as a sensory HD-GYP/HD-PDEase
  cyclic-guanylate phosphodiesterase candidate rather than an MCP receptor.
- Completed `dna_binding_response_regulator_spillover`: `PP_2403` is fetched,
  Asta-backed, first-pass curated, validated, rendered, and represented in
  `modules/orphan_two_component_regulators_boundary.yaml` as an OmpR/PhoB-family
  DNA-binding response regulator rather than a core CheY output protein.
- Completed `chey_like_membrane_accessory_spillovers`: `PP_3757`, `PP_3771`,
  and `PP_4331` are fetched, Asta-backed, first-pass curated, validated, and
  represented in `modules/chemotaxis_adaptation_accessory_boundary.yaml` as one
  compact CheY-like response-regulator candidate and two conservative membrane
  accessory candidates.
- Completed `outer_membrane_flagellation_name_spillover`: `ycfJ` is fetched,
  Asta-backed, first-pass curated, validated, and represented in
  `modules/transport_envelope_spillover_boundary.yaml` as an outer-membrane
  lipoprotein/surface-antigen-family spillover.
- Completed `flagellar_export_localization_accessory_spillovers`: `PP_4328`,
  `PP_4329`, `PP_4342`, `flhF`, and `PP_4377` are fetched, Asta-backed,
  first-pass curated, validated, and represented in
  `modules/flagellar_export_assembly_boundary.yaml` as hook-control, export,
  localization/number-control, and FlaG accessory context.
- Completed `c_di_gmp_flagellar_brake_spillover`: `ycgR` is fetched,
  Asta-backed, first-pass curated, validated, and represented in
  `modules/flagellar_motor_switch_stator_boundary.yaml` as a PilZ-domain
  c-di-GMP-dependent motor brake.
- The touched modules validate with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/type_iv_pilus_biogenesis_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/type_iv_pilus_biogenesis_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/pili_surface_adhesion_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/pili_surface_adhesion_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_secretion_system_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/bacterial_secretion_system_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/alginate_biosynthesis_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/alginate_biosynthesis_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/orphan_mcp_aerotaxis_receptors_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/orphan_mcp_aerotaxis_receptors_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/c_di_gmp_turnover_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/c_di_gmp_turnover_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/orphan_two_component_regulators_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/orphan_two_component_regulators_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/chemotaxis_adaptation_accessory_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/chemotaxis_adaptation_accessory_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/transport_envelope_spillover_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/transport_envelope_spillover_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/flagellar_export_assembly_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/flagellar_export_assembly_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/flagellar_motor_switch_stator_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/flagellar_motor_switch_stator_boundary.yaml
```

- Falcon generic module research for `pili_surface_adhesion_boundary` was
  attempted with the real module-level command and failed while Edison Falcon
  access returns HTTP 402:
  `modules/pili_surface_adhesion_boundary-deep-research-falcon.md`.
- Falcon generic module research for `type_iv_pilus_biogenesis_boundary` was
  attempted with the real module-level command and failed while Edison Falcon
  access returns HTTP 402:
  `modules/type_iv_pilus_biogenesis_boundary-deep-research-falcon.md`.
- Falcon taxon-aware module/pathway research for
  `orphan_mcp_aerotaxis_receptors_boundary` + `module:motility_chemotaxis_biofilm`
  + PSEPK was attempted with the real command and failed while Edison Falcon
  access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__orphan_mcp_aerotaxis_receptors_boundary__module-motility-chemotaxis-biofilm-deep-research-falcon.md`.
- Falcon taxon-aware module/pathway research for
  `chemotaxis_adaptation_accessory_boundary` + `module:motility_chemotaxis_biofilm`
  + PSEPK was attempted with the real command and failed before report generation
  while Edison Falcon access returns HTTP 402; no report file was produced.
- Falcon taxon-aware module/pathway research for
  `orphan_two_component_regulators_boundary` + `module:motility_chemotaxis_biofilm`
  + PSEPK was attempted with the real command and failed before report generation
  while Edison Falcon access returns HTTP 402; no report file was produced.

Main curation conclusions from this partition:

- Do not curate the 35-gene motility/chemotaxis/biofilm functional bucket as one
  satisfiable module.
- The type IV pilus biogenesis bucket is now a dedicated module, not part of the
  broad pili/surface-adhesion boundary. It includes pilin-like substrate
  candidates, the PilC platform, PilM/PilN/PilO/PilP-like alignment components,
  and the PilQ secretin context.
- `pilD` and `pilT` are the main T4P hole-filling lessons from this pass:
  `pilD` is currently trapped in the transport/membrane bucket and `pilT` is an
  orphan domain-only row, but both should be reviewed before claiming a complete
  type IV pilus maturation and retraction/motility cycle.
- Product-name buckets need domain checking before module assignment: PP_0655
  looked fimbrial by product name, but Hcp1-like/T6SS_Hcp domains route it to
  bacterial secretion-system context.
- PP_1888 and fimI are best handled as an extension of the already curated
  FimD/PP_1890 chaperone-usher pair. Their broad cell-adhesion and pilus
  annotations are retained, but the specific single-species-biofilm process is
  marked over-annotated pending direct KT2440 phenotype evidence.
- The alginate side bucket is keyword-umbrella cleanup rather than a new
  module: glmP belongs with efficient alginate biosynthesis, PP_3350 and
  PP_3464 are export-domain candidates, and PP_1754/PP_3774 are
  alginate-lyase-domain processing candidates within the existing alginate
  boundary.
- PP_2310, PP_3950, and PP_4888 extend the orphan MCP/aerotaxis receptor
  boundary as ligand-unresolved chemotaxis receptor/transducer candidates.
  PP_2599 is a useful negative lesson for this bucket: its product name looks
  chemotaxis-adjacent, but HD-GYP/HD-PDEase and cyclic-di-GMP
  phosphodiesterase-family evidence routes it to c-di-GMP turnover instead.
- PP_2403 is the key response-regulator spillover lesson from this pass: its
  product name looks CheY-like, but OmpR/PhoB DNA-binding response-regulator
  evidence routes it to the orphan/generic TCS boundary rather than to core
  chemotaxis.
- PP_3757 remains in the chemotaxis adaptation/accessory boundary as a compact
  CheY-like receiver-domain candidate. PP_3771 and PP_4331 are retained only as
  conservative membrane accessory candidates, with no process-level chemotaxis
  assertion until direct evidence appears.
- The final flagellar spillover split closes the motility umbrella: ycfJ routes
  to transport/envelope context, PP_4328/PP_4329/PP_4342/flhF/PP_4377 route to
  flagellar export/assembly or localization/accessory context, and ycgR routes
  to flagellar motor braking.
- PP_4329 is distinct from canonical `flhB`/PP_4352; it is retained as a short
  FlhB-family exporter spillover rather than merged into the existing flhB
  annoton.
- `flhF` and PP_4342 are useful over-propagation lessons: FlhF should not carry
  SRP-targeting biology from SRP54-family similarity, and PP_4342 should not
  carry cell-division regulation from MinD/FleN-family similarity without local
  evidence.
- All 35 genes in the motility/chemotaxis/biofilm functional bucket now have
  first-pass curated reviews and Asta reports.

## Partition status: module:cell_envelope_division

Partition files:

- `projects/P_PUTIDA/batches/module_cell_envelope_division_partition.tsv`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_partition.md`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_lps_core_lipid_a_biosynthesis_context.tsv`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_lps_core_lipid_a_biosynthesis_context.md`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_maltose_acetyltransferase_lipid_a_keyword_spillover.tsv`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_maltose_acetyltransferase_lipid_a_keyword_spillover.md`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_cell_division_regulatory_spillovers.tsv`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_cell_division_regulatory_spillovers.md`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_vacj_phospholipid_asymmetry_context.tsv`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_vacj_phospholipid_asymmetry_context.md`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_apbe_fmn_transferase_spillover.tsv`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_apbe_fmn_transferase_spillover.md`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_peptidoglycan_turnover_remodeling_candidates.tsv`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_peptidoglycan_turnover_remodeling_candidates.md`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_outer_membrane_barrel_channel_autotransporter_context.tsv`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_outer_membrane_barrel_channel_autotransporter_context.md`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_named_outer_membrane_lipoprotein_families.tsv`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_named_outer_membrane_lipoprotein_families.md`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_domain_resolved_lipoprotein_spillovers.tsv`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_domain_resolved_lipoprotein_spillovers.md`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_generic_lipoprotein_signal_spillovers.tsv`
- `projects/P_PUTIDA/batches/module_cell_envelope_division_generic_lipoprotein_signal_spillovers.md`
- `projects/P_PUTIDA/partition_cell_envelope_division.py`

Status as of 2026-07-10:

- The functional `module:cell_envelope_division` bucket has 98 primary PSEPK
  genes from UniProt name/keyword assignment.
- The pathway worklist marks `module:cell_envelope_division` as `PARTITIONED`
  with no single module file.
- The generated partition table splits the 98 genes into 11 buckets: Lpt/LPS
  outer-membrane transport context (2), LPS-core/lipid-A biosynthesis context
  (2), maltose-acetyltransferase lipid-A-keyword spillover (1), peptidoglycan
  turnover/remodeling candidates (11), cell-division regulatory spillovers (3),
  VacJ/MlaA phospholipid-asymmetry context (1), ApbE-like envelope
  flavinylation spillover (1), outer-membrane barrels/channels/autotransporters
  (8), named outer-membrane lipoprotein families (9), domain-resolved
  lipoprotein spillovers (30), and generic lipoprotein-signal spillovers (30).
- Completed `lps_core_lipid_a_biosynthesis_context`: `PP_3016` and `PP_3134`
  are fetched, Asta-backed, first-pass curated, validated, rendered, and
  represented in the existing `modules/lipopolysaccharide_biosynthesis.yaml`.
- Completed `maltose_acetyltransferase_lipid_a_keyword_spillover`: `maa` is
  fetched, Asta-backed, first-pass curated, validated, and intentionally kept
  out of the LPS/lipid-A module because the review supports cytosolic maltose
  O-acetyltransferase activity rather than lipid-A or LPS biosynthesis.
- Completed `cell_division_regulatory_spillovers`: `sulA`, `PP_2199`, and
  `PP_2352` are fetched, Asta-backed, first-pass curated, validated, rendered,
  and represented in the existing
  `modules/divisome_z_ring_septation_boundary.yaml`.
- Completed `vacj_phospholipid_asymmetry_context`: `vacJ` is fetched by known
  UniProt accession Q88KX6 with alias `vacJ`, Asta-backed, first-pass curated,
  validated, rendered, and represented in the existing
  `modules/mla_phospholipid_transport_boundary.yaml`.
- Completed `apbe_fmn_transferase_spillover`: `PP_2150` is fetched,
  Asta-backed, first-pass curated, validated, rendered, and represented in the
  existing `modules/ccm_heme_export_cytochrome_c_maturation_boundary.yaml` as
  related envelope flavoprotein maturation context rather than as a CcmABCD
  heme-export subunit.
- Completed `peptidoglycan_turnover_remodeling_candidates`: `amiD`, `ampD`,
  `rlpA__Q88PC1`, `mltF`, `PP_1325`, `PP_2147`, `PP_3562`, `pbpG`,
  `rlpA__Q88DM1`, `PP_4971`, and `PP_5354` are accession-seeded,
  Asta-backed, first-pass curated, validated, rendered, and represented in the
  existing `modules/peptidoglycan_biosynthesis.yaml` as turnover, remodeling,
  binding, or cell-wall assembly candidates.
- Completed `outer_membrane_barrel_channel_autotransporter_context`: `yiaD`,
  `PP_1121`, `PP_1122`, `PP_1880`, `PP_3069`, `PP_3449`, `PP_4291`, and
  `PP_4293` are accession-seeded, Asta-backed, first-pass curated, validated,
  rendered, and represented in the existing
  `modules/transport_envelope_spillover_boundary.yaml`.
- Completed `named_outer_membrane_lipoprotein_families`: `uxpA`, `slyB`,
  `oprI`, `PP_3236`, `yaiW`, `PP_4032`, `PP_4855`, `PP_5037`, and `PP_5226`
  are accession-seeded, Asta-backed, first-pass curated, validated, rendered,
  and represented in the existing
  `modules/transport_envelope_spillover_boundary.yaml`.
- Completed `domain_resolved_lipoprotein_spillovers`: `PP_0116`, `PP_0139`,
  `PP_0512`, `PP_0549`, `PP_0576`, `PP_0753`, `PP_1115`, `PP_1146`,
  `PP_1153`, `PP_1161`, `PP_1238`, `PP_1322`, `PP_1500`, `PP_1519`,
  `PP_1970`, `PP_2003`, `PP_2020`, `PP_2121`, `PP_2191`, `PP_2462`,
  `PP_2730`, `PP_3520`, `PP_4199`, `PP_4564`, `PP_4686`, `PP_4920`,
  `PP_4961`, `PP_5319`, `PP_5333`, and `PP_5639` are accession-seeded,
  Asta-backed, first-pass curated, validated, rendered, and represented in the
  existing `modules/transport_envelope_spillover_boundary.yaml`.
- Completed `generic_lipoprotein_signal_spillovers`: `PP_0091`, `PP_0092`,
  `PP_0277`, `PP_0677`, `PP_1204`, `PP_1498`, `PP_2197`, `PP_2252`,
  `PP_2306`, `PP_2414`, `PP_3008`, `PP_3010`, `PP_3014`, `PP_3158`,
  `PP_3418`, `PP_3519`, `PP_3824`, `PP_4319`, `PP_4962`, `PP_5304`,
  `PP_5449`, `PP_5470`, `PP_5480`, `PP_5504`, `PP_5509`, `PP_5524`,
  `PP_5594`, `PP_5648`, `PP_5661`, and `PP_5710` are accession-seeded,
  Asta-backed, first-pass curated, validated, rendered, and represented in the
  existing `modules/transport_envelope_spillover_boundary.yaml`.
- LptD/LptE were already curated in `modules/lpt_lps_transport_boundary.yaml`
  before this partition pass; this partition records them as existing Lpt/LPS
  transport context rather than reopening that module.
- The updated LPS, divisome, Mla, Ccm/cytochrome-redox boundary, peptidoglycan,
  and transport/envelope spillover modules validate with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/lipopolysaccharide_biosynthesis.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/lipopolysaccharide_biosynthesis.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/divisome_z_ring_septation_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/divisome_z_ring_septation_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/mla_phospholipid_transport_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/mla_phospholipid_transport_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/ccm_heme_export_cytochrome_c_maturation_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/ccm_heme_export_cytochrome_c_maturation_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/peptidoglycan_biosynthesis.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/peptidoglycan_biosynthesis.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/transport_envelope_spillover_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/transport_envelope_spillover_boundary.yaml
```

Main curation conclusions from this partition so far:

- Do not curate the 98-gene cell-envelope/division functional bucket as one
  satisfiable module. It is mostly a name/keyword umbrella that mixes true LPS,
  peptidoglycan, division, phospholipid-asymmetry, envelope-flavinylation,
  outer-membrane, and lipoprotein context.
- `PP_3016` is a conservative WaaZ/Kdo-transferase-family LPS-core biosynthesis
  candidate. The review adds Kdo transferase activity and LPS core-region
  biosynthetic-process recommendations while leaving exact acceptor chemistry
  unresolved.
- `PP_3134` is a LpxA-like/hexapeptide-repeat O-acyltransferase-family
  candidate in lipid-A context. The review modifies broad transferase activity
  toward O-acyltransferase activity and adds lipid A biosynthetic process, but
  does not claim a substrate-specific acyl donor or acceptor.
- `maa` is the first spillover lesson from this umbrella: its UniProt name,
  EC, Mac domain, and GOA all support maltose O-acetyltransferase rather than
  lipid-A acetyltransferase, so it is routed out of LPS/lipid-A curation.
- `sulA` belongs as SOS-linked cell-division-inhibitor/regulatory context, not
  as a structural divisome subunit.
- `PP_2199` and `PP_2352` are additional AFG1/ZapE-family ATPase candidates.
  Their ATPase activity is core, while cell-division/site annotations are kept
  as family-level candidate context because direct FtsZ interaction has not
  been shown for these paralogs.
- `vacJ` is a MlaA/VacJ-family lipoprotein singleton. The review accepts
  intermembrane phospholipid transfer and generic membrane localization, but
  does not author a sharper outer-membrane location until direct local evidence
  is available.
- `PP_2150` is an ApbE-family FAD:protein FMN transferase singleton. The review
  accepts `GO:7770036` flavin transferase activity as core, keeps Mg/Mn binding
  as cofactor context, and places the protein in the Ccm/cytochrome-redox
  boundary only as related envelope flavoprotein maturation context.
- The 11-gene peptidoglycan turnover/remodeling split belongs inside the
  existing peptidoglycan module, but as a distinct turnover/remodeling part:
  amidases (`amiD`, `ampD`), RlpA/Mlt lytic transglycosylases
  (`rlpA__Q88PC1`, `mltF`, `rlpA__Q88DM1`, `PP_4971`), an LpoA-family PBP
  activator candidate (`PP_1325`), a peptidase S11 remodeling enzyme (`pbpG`),
  and sparse CsiV/SleB/SUKH cell-wall candidates (`PP_2147`, `PP_3562`,
  `PP_5354`) should not be conflated with cytosolic precursor synthesis.
- The outer-membrane barrel/channel/autotransporter split belongs in the
  existing transport/envelope spillover boundary, not in peptidoglycan or LPS:
  OmpA-family proteins remain unresolved envelope candidates, autotransporters
  have unresolved passenger functions, PP_3449 is only an outer-membrane
  N4-receptor-like candidate, and Tsx-like PP_4291/PP_4293 get conservative
  porin activity without a nucleoside-transport process claim.
- The named outer-membrane/lipoprotein-family split also belongs in the existing
  transport/envelope spillover boundary: `uxpA` gets specific
  5'-nucleotidase activity, Blc paralogs get lipid binding with stress response
  kept non-core, and `PP_3236`/`yaiW` are intentionally limited to broad
  membrane localization until sharper localization or mechanism evidence is
  available.
- The domain-resolved lipoprotein split also belongs in the existing
  transport/envelope spillover boundary. Most entries receive only broad
  membrane placement; LEA_2/WHy-domain `PP_1115` and `PP_2191` retain
  response-to-desiccation context; `PP_1500` carries peptidase
  activity/proteolysis; `PP_2462` carries candidate peptidase inhibitor
  activity; `PP_4686` carries candidate heme binding; and `PP_5319` is retained
  as membrane lipoprotein context while its alkane catabolic process annotation
  is marked over-annotated.
- The generic lipoprotein/signal-peptide split is complete but remains
  deliberately low-specificity in the transport/envelope spillover boundary:
  all 30 fetched GOA files are header-only, Asta did not resolve specific
  family/domain/function beyond the provided UniProt context, and every gene is
  represented only with broad membrane placement. No outer-membrane specificity,
  molecular function, partner complex, or pathway process is asserted.
- The 98-gene cell-envelope/division functional bucket is now fully
  first-pass-covered. Future work should be targeted follow-up from module
  gaps or stronger neighborhood/literature evidence, not another broad pass
  over this umbrella.

## Partition status: module:stress_detoxification

Partition files:

- `projects/P_PUTIDA/batches/module_stress_detoxification_partition.tsv`
- `projects/P_PUTIDA/batches/module_stress_detoxification_partition.md`
- `projects/P_PUTIDA/batches/module_stress_detoxification_peroxide_peroxiredoxin_detoxification.tsv`
- `projects/P_PUTIDA/batches/module_stress_detoxification_peroxide_peroxiredoxin_detoxification.md`
- `projects/P_PUTIDA/batches/module_stress_detoxification_glutathione_thiol_detoxification.tsv`
- `projects/P_PUTIDA/batches/module_stress_detoxification_glutathione_thiol_detoxification.md`
- `projects/P_PUTIDA/batches/module_stress_detoxification_arsenic_copper_metal_resistance.tsv`
- `projects/P_PUTIDA/batches/module_stress_detoxification_arsenic_copper_metal_resistance.md`
- `projects/P_PUTIDA/batches/module_stress_detoxification_universal_stress_proteins.tsv`
- `projects/P_PUTIDA/batches/module_stress_detoxification_universal_stress_proteins.md`
- `projects/P_PUTIDA/batches/module_stress_detoxification_cold_heat_shock_chaperone_spillovers.tsv`
- `projects/P_PUTIDA/batches/module_stress_detoxification_cold_heat_shock_chaperone_spillovers.md`
- `projects/P_PUTIDA/batches/module_stress_detoxification_thij_dj1_pfpi_detoxification_candidates.tsv`
- `projects/P_PUTIDA/batches/module_stress_detoxification_thij_dj1_pfpi_detoxification_candidates.md`
- `projects/P_PUTIDA/batches/module_stress_detoxification_stress_regulatory_or_misc_spillovers.tsv`
- `projects/P_PUTIDA/batches/module_stress_detoxification_stress_regulatory_or_misc_spillovers.md`
- `projects/P_PUTIDA/partition_stress_detoxification.py`

Status as of 2026-07-10:

- The functional `module:stress_detoxification` bucket has 52 primary PSEPK
  genes from UniProt name/keyword assignment.
- The pathway worklist marks `module:stress_detoxification` as `PARTITIONED`
  with no single module file.
- The generated partition table splits the 52 genes into 7 buckets:
  peroxide/peroxiredoxin detoxification (10), glutathione/thiol detoxification
  (7), arsenic/copper metal resistance (8), universal stress proteins (11),
  cold/heat-shock chaperone spillovers (5), ThiJ/DJ-1/PfpI detoxification
  candidates (3), and stress-regulatory/miscellaneous spillovers (8).
- Completed `peroxide_peroxiredoxin_detoxification`: `osmC`, `PP_0235`,
  `tsaA`, `PP_1235`, `ohr`, `ahpC`, `PP_2943`, `PP_3248`, `tpx`, and `cpo`
  are fetched or rechecked, Asta-backed, first-pass curated, validated, and
  rendered.
- Completed `glutathione_thiol_detoxification`: `PP_0335`, `yffB`,
  `PP_1939`, `PP_2023`, `PP_3742`, `PP_4104`, and `mnaT` are fetched,
  Asta-backed, first-pass curated, validated, rendered, and represented as
  side context in the existing `modules/glutathione_metabolism_boundary.yaml`.
- Completed `arsenic_copper_metal_resistance`: `PP_1927`, `PP_1928`,
  `copB-I`, `copA-I`, `arsH`, `PP_2716`, `copB-II`, and `copA-II` are
  fetched, Asta-backed, first-pass curated, validated, rendered, and represented
  in the new `modules/metal_resistance_detoxification_boundary.yaml`.
- Completed `universal_stress_proteins`: `PP_1269`, `PP_2132`, `PP_2187`,
  `PP_2326`, `PP_2648`, `PP_2745`, `PP_3156`, `PP_3237`, `PP_3288`,
  `PP_3290`, and `PP_3294` are fetched, Asta-backed, first-pass curated,
  validated, rendered, and represented in the new
  `modules/universal_stress_protein_boundary.yaml`.
- Completed `cold_heat_shock_chaperone_spillovers`: `capB`, `cspA-I`,
  `ibpA`, `PP_3313`, and `PP_3314` are fetched, Asta-backed, first-pass
  curated, validated, rendered, and represented as bacterial cold-shock-domain
  and HSP20 holdase side context in the existing
  `modules/integrated_stress_response_boundary.yaml`.
- Completed `thij_dj1_pfpi_detoxification_candidates`: `PP_2491`, `PP_2992`,
  and `PP_3431` are fetched, Asta-backed, first-pass curated, validated,
  rendered, and represented in the new
  `modules/stress_detoxification_spillover_boundary.yaml`.
- Completed `stress_regulatory_or_misc_spillovers`: `srkA`, `dps`, `PP_3269`,
  `paaY`, `PP_3509`, `PP_3963`, `oxyR`, and `PP_5593` are fetched or reused,
  Asta-backed, first-pass curated, validated, rendered, and represented in the
  updated `modules/stress_detoxification_spillover_boundary.yaml`.
- New peroxide-detoxification boundary module created and validated:
  `modules/oxidative_stress_peroxide_detoxification_boundary.yaml`.
- Module page rendered:
  `pages/modules/oxidative_stress_peroxide_detoxification_boundary.html`.
- Updated glutathione boundary module validated:
  `modules/glutathione_metabolism_boundary.yaml`.
- New metal-resistance boundary module created and validated:
  `modules/metal_resistance_detoxification_boundary.yaml`.
- New universal-stress-protein boundary module created and validated:
  `modules/universal_stress_protein_boundary.yaml`.
- Updated integrated-stress boundary module validated:
  `modules/integrated_stress_response_boundary.yaml`.
- Stress-detoxification spillover boundary module created, extended, and validated:
  `modules/stress_detoxification_spillover_boundary.yaml`.
- Validation complete for all 52 stress/detoxification split gene reviews and
  the six touched modules. The pathway worklist records 52 review files, 52
  curated reviews, 52 Asta reports, and zero missing review folders for the
  stress/detoxification bucket. Module validation used:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/oxidative_stress_peroxide_detoxification_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/oxidative_stress_peroxide_detoxification_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/glutathione_metabolism_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/glutathione_metabolism_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/metal_resistance_detoxification_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/metal_resistance_detoxification_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/universal_stress_protein_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/universal_stress_protein_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/integrated_stress_response_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/integrated_stress_response_boundary.yaml
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/stress_detoxification_spillover_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/stress_detoxification_spillover_boundary.yaml
```

Main curation conclusions from this partition:

- Do not curate the 52-gene stress/detoxification functional bucket as one
  satisfiable module. It mixes direct peroxide detoxification, glutathione/thiol
  chemistry, arsenic/copper resistance, universal-stress-protein candidates,
  cold/heat-shock proteins, ThiJ/DJ-1/PfpI proteins, and low-information stress
  spillovers.
- The completed peroxide/peroxiredoxin split is bacterial cellular oxidant
  detoxification context, not peroxisome organelle biology.
- `osmC` and `ohr` are OsmC/Ohr-family peroxide or organic-hydroperoxide
  detoxification candidates. `ohr` gained conservative new peroxidase activity
  and cellular oxidant detoxification recommendations because its seeded GOA
  had only a broad oxidative-stress process row.
- `PP_0235`, `tsaA`, `PP_1235`, `ahpC`, and `tpx` are peroxiredoxin-family
  enzymes. Broad oxidoreductase rows are modified toward peroxiredoxin or
  thioredoxin-dependent peroxiredoxin terms, while broad antioxidant,
  stress-response, and redox-homeostasis terms stay non-core.
- The pre-existing deeper `ahpC` curation was preserved and Asta-backed during
  this pass. The review keeps donor-specific NADH dependence as AhpCF-system
  context rather than a single AhpC-subunit molecular-function claim.
- `PP_2943` is periplasmic cytochrome c551 peroxidase context, `PP_3248` is
  DyP-family heme peroxidase context, and `cpo` is non-heme chloroperoxidase
  context. These remain peroxide-detoxification boundary members but are not
  peroxiredoxins.
- The completed glutathione/thiol split extends the existing glutathione
  boundary but stays conservative: `PP_0335`, `PP_2023`, `PP_3742`, and
  `PP_4104` are GST-family transferase candidates without substrate or process
  assertions; `yffB` is an ArsC-family glutathione-dependent thiol reductase
  candidate with arsenate-reductase specificity unresolved; `PP_1939` is a
  glutathione-independent formaldehyde dehydrogenase candidate and should not
  be treated as core glutathione chemistry; and `mnaT` is a methionine-derivative
  L-amino-acid N-acetyltransferase side node.
- The completed arsenic/copper metal-resistance split separates duplicated
  ArsH/arsenate-reductase pairs from duplicated CopAB copper-resistance pairs:
  `PP_1927` and `arsH` use FMN reductase (NADPH) activity as the core MF;
  `PP_1928` and `PP_2716` receive conservative broad oxidoreductase activity
  plus arsenic-response context because fetched GOA is empty; `copB-I` and
  `copB-II` are outer-membrane copper-binding/homeostasis proteins; and
  `copA-I` and `copA-II` are periplasmic multicopper oxidase-family proteins,
  not P-type copper ATPases in this locus context.
- The completed universal-stress-protein split is deliberately low-specificity:
  cytoplasm GOA rows are accepted where present, but no ATP-binding, molecular
  activity, DNA-damage-response process, or broad stress-response process is
  added. `PP_1269`, `PP_2132`, and `PP_2326` are single-domain USP-family
  candidates; `PP_2648` and the PP_2187/PP_2745/PP_3156/PP_3237/PP_3288/
  PP_3290/PP_3294 set are tandem-domain or larger USP-family candidates, with
  UniProt DNA-damaging-agent resistance comments retained only as context.
- The completed cold/heat-shock spillover split reuses the bacterial
  stress/proteostasis boundary rather than creating a separate pathway module:
  `capB` and `cspA-I` are cold-shock-domain nucleic-acid-binding proteins with
  no resolved specific RNA/DNA target or transcription-process claim; `ibpA`,
  `PP_3313`, and `PP_3314` are HSP20-family unfolded-protein-binding/holdase
  candidates with specific client proteins unresolved; and `PP_3313` retains
  response-to-heat process context from InterPro2GO.
- The completed ThiJ/DJ-1/PfpI split is coherent enough for one compact
  spillover boundary part: `PP_2491`, `PP_2992`, and `PP_3431` all retain
  cytoplasm, `GO:0019172` glyoxalase III activity, and `GO:0051596`
  methylglyoxal catabolic process from TreeGrafter/PANTHER evidence. QuickGO
  confirms `GO:0019172` is the active GSH-independent methylglyoxal-to-D-lactate
  activity; no protein- or nucleotide-deglycase terms are added without
  gene-specific or subfamily-specific support.
- The completed final miscellaneous spillover split is deliberately heterogeneous:
  `srkA` is a cytoplasmic SrkA/RdoA-family Ser/Thr kinase with substrates
  unresolved; `dps` is a Dps-family ferroxidase/iron-binding and DNA-binding
  stress protein, with broad metal-ion oxidoreductase marked over-annotated;
  `paaY` receives conservative acyl-CoA hydrolase and phenylacetate-catabolism
  recommendations from PaaY/thioesterase context; `PP_3509` is retained as
  antibiotic/bleomycin-response context without a molecular-function claim;
  `oxyR` is the oxidative-stress transcription regulator and now has an explicit
  NEW `GO:0034599` cellular response to oxidative stress row; and `PP_3269`,
  `PP_3963`, and `PP_5593` remain curated KGG-repeat unknowns with no proposed
  GO function.

## Partition status: ppu02040 / flagellar-assembly pathway

Partition files:

- `projects/P_PUTIDA/batches/ppu02040_bacterial_flagellar_assembly_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu02040_bacterial_flagellar_assembly_boundary.md`
- `projects/P_PUTIDA/batches/ppu02040_bacterial_flagellar_assembly_partition.tsv`
- `projects/P_PUTIDA/batches/ppu02040_bacterial_flagellar_assembly_partition.md`
- `projects/P_PUTIDA/partition_ppu02040_flagellar_assembly.py`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- KEGG `ppu02040` has 47 total specific members and 47 primary PSEPK genes.
- The primary-only 47-gene checklist was generated as a partitioning input, not
  as a curation-complete batch.
- The pathway worklist now marks `kegg:ppu02040` as `PARTITIONED` with no
  single module file.
- The generated partition table splits the 47 genes into 5 buckets:
  flagellar basal-body/hook/filament structure (15), flagellar export and
  assembly/chaperones (14), flagellar motor/switch/stator proteins (9),
  flagellar sigma/master regulation (6), and nonflagellar transport/envelope
  spillovers (3).
- The `flagellar_motor_switch_stator` bucket is complete as a first-pass
  curation sub-batch: 9/9 genes have review folders, Asta reports,
  first-pass curation, rendered gene pages, and the validated/rendered module
  `modules/flagellar_motor_switch_stator_boundary.yaml`.
- The `flagellar_export_assembly_chaperones` bucket is complete as a
  first-pass curation sub-batch: 14/14 genes have review folders, Asta reports,
  first-pass curation, rendered gene pages, and the validated/rendered module
  `modules/flagellar_export_assembly_boundary.yaml`.
- The `flagellar_basal_body_hook_filament` bucket is complete as a first-pass
  curation sub-batch: 15/15 genes have review folders, Asta reports,
  first-pass curation, rendered gene pages, and the validated/rendered module
  `modules/flagellar_basal_body_hook_filament_boundary.yaml`.
- The `flagellar_regulation_sigma_master_control` bucket is complete as a
  first-pass curation sub-batch: 6/6 genes have review folders, Asta reports,
  first-pass curation, rendered gene pages, and the validated/rendered module
  `modules/flagellar_regulation_boundary.yaml`.
- The `nonflagellar_transport_envelope_spillovers` bucket is complete as a
  first-pass boundary sub-batch: 3/3 genes have review folders, Asta reports,
  first-pass curation, rendered gene pages, and the validated/rendered module
  `modules/transport_envelope_spillover_boundary.yaml`.

Main curation conclusions from this partition:

- Do not open a single 47-gene ppu02040 flagellar-assembly PR for the first
  pass.
- The map is biologically coherent, unlike the quorum/biofilm umbrellas, but
  it mixes several apparatus layers plus regulators and side entries.
- `fliY`, `PP_1087`, and `PP_5157` should stay outside the flagellar apparatus
  core unless direct flagellum-assembly evidence is selected.
- Global sigma/master regulators should be handled separately from structural
  flagellar apparatus proteins.
- The concrete flagellar apparatus first-pass batches are complete:
  motor/switch/stator, export/assembly, and basal-body/hook/filament.
  Regulation is also complete as a separate first-pass module.
- Transport/envelope spillovers should stay outside the flagellar apparatus
  core unless direct evidence emerges.
- The ppu02040 first-pass partition is complete: 47/47 primary genes have
  review folders, curated reviews, Asta reports, and rendered pages, and all 5
  partition buckets have validated/rendered modules or boundary modules.

## Partition status: ppu03010 / ribosome pathway

Partition files:

- `projects/P_PUTIDA/batches/ppu03010_bacterial_ribosome_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu03010_bacterial_ribosome_boundary.md`
- `projects/P_PUTIDA/batches/ppu03010_bacterial_ribosome_partition.tsv`
- `projects/P_PUTIDA/batches/ppu03010_bacterial_ribosome_partition.md`
- `projects/P_PUTIDA/partition_ppu03010_ribosome.py`
- `projects/P_PUTIDA/curate_ppu03010_30s_ribosomal_subunit_first_pass.py`
- `projects/P_PUTIDA/build_ppu03010_30s_ribosomal_subunit_module.py`
- `modules/bacterial_30s_ribosomal_subunit_boundary.yaml`
- `pages/modules/bacterial_30s_ribosomal_subunit_boundary.html`
- `projects/P_PUTIDA/curate_ppu03010_50s_ribosomal_subunit_first_pass.py`
- `projects/P_PUTIDA/build_ppu03010_50s_ribosomal_subunit_module.py`
- `modules/bacterial_50s_ribosomal_subunit_boundary.yaml`
- `pages/modules/bacterial_50s_ribosomal_subunit_boundary.html`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- KEGG `ppu03010` has 54 total specific members and 54 primary PSEPK genes.
- The primary-only 54-gene checklist was generated as a partitioning input, not
  as a curation-complete batch.
- The pathway worklist now marks `kegg:ppu03010` as `PARTITIONED` with no
  single module file.
- The generated partition table splits the 54 genes into 2 buckets: bacterial
  30S small-subunit ribosomal proteins (21) and bacterial 50S large-subunit
  ribosomal proteins (33).
- The 30S sub-batch is now complete: 21/21 review folders, 21/21 curated
  reviews, 21/21 Asta reports, 21/21 rendered gene pages, and a validated/
  rendered `bacterial_30s_ribosomal_subunit_boundary` module.
- The 50S sub-batch is now complete: 33/33 review folders, 33/33 curated
  reviews, 33/33 Asta reports, 33/33 rendered gene pages, and a validated/
  rendered `bacterial_50s_ribosomal_subunit_boundary` module.
- The full ppu03010 first pass is now complete: 54/54 primary ribosomal-protein
  genes have review folders, curated reviews, Asta reports, and rendered gene
  pages; both partition buckets have validated/rendered modules.

Main curation conclusions from this partition:

- Do not open a single 54-gene ppu03010 ribosome PR for the first pass.
- This is a clean ribosomal-protein set; no unknown or side-context bucket was
  needed.
- The ppu03010 first-pass curation unit remains partitioned into 30S and 50S
  protein modules; do not collapse the two completed modules into one 54-gene
  review unit.
- Validation lesson from the 30S sub-batch: specific small-subunit component
  GO terms such as `GO:0015935` and `GO:0022627` are fine as trusted GOA
  `existing_annotations`, but should not be authored into
  `core_functions.locations`; use a schema-accepted location such as
  `GO:0005840` ribosome when present, otherwise omit the core location.
- Validation lesson from the 50S sub-batch is the same for
  `GO:0015934`/`GO:0022625` large-subunit component terms. Also, keep
  ribosomal-protein-specific side annotations narrow: `rplB` generic
  transferase activity is over-annotated, `rpmA` preribosome-precursor assembly
  should be modified to ribosomal large subunit assembly, and zinc binding,
  ribosome binding, and autoregulatory translation-repression terms should stay
  non-core unless deeper evidence changes the interpretation.

## Partition status: ppu04122 / sulfur-relay system

Partition files:

- `projects/P_PUTIDA/batches/ppu04122_sulfur_relay_system_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu04122_sulfur_relay_system_boundary.md`
- `projects/P_PUTIDA/batches/ppu04122_sulfur_relay_system_partition.tsv`
- `projects/P_PUTIDA/batches/ppu04122_sulfur_relay_system_partition.md`
- `projects/P_PUTIDA/partition_ppu04122_sulfur_relay.py`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- KEGG `ppu04122` has 22 total specific members and 19 primary PSEPK genes.
- The primary-only 19-gene checklist was generated as a partitioning input, not
  as a curation-complete batch.
- The pathway worklist now marks `kegg:ppu04122` as `PARTITIONED` with no
  single module file.
- The generated partition table splits the 19 genes into 4 buckets:
  molybdopterin/MoCo sulfur relay (9), Tus/MnmA tRNA thiolation (7),
  rhodanese/mercaptopyruvate sulfurtransferase side nodes (2), and ThiS
  thiamine sulfur-carrier context (1).

Main curation conclusions from this partition:

- Do not open a single 19-gene ppu04122 sulfur-relay PR.
- The map mixes distinct sulfur-carrier systems and sulfurtransferase side
  chemistry.
- `PP_5105` should stay with the thiamine-biosynthesis ThiS gap-fill rather
  than being merged into a generic sulfur-relay module.
- `rhdA` and `sseA` should stay with general sulfur-metabolism
  sulfurtransferase context unless a specific sulfur-relay mechanism is
  selected.
- Completed `tus_mnma_trna_thiolation`: seven genes fetched, Asta-backed,
  first-pass curated, validated, and rendered; new module
  `modules/mnma_tus_trna_thiolation_boundary.yaml` created, validated, and
  rendered.
- Completed `molybdopterin_moco_sulfur_relay`: nine genes present,
  Asta-backed, first-pass curated, and validated; `moeB` and `moaD` were
  fetched, Asta-backed, curated, and rendered; new module
  `modules/molybdopterin_biosynthesis_sulfur_relay_boundary.yaml` created,
  validated, and rendered.
- `tusA-I` and `PP_3994` have empty fetched GOA tables. Their inferred Tus
  sulfur-relay roles are recorded in authored `core_functions` and module
  knowledge gaps rather than as synthetic non-GOA `existing_annotations`,
  because the current validator rejects annotations absent from GOA.
- After the Tus/MnmA and MoCo passes, the ppu04122 worklist row has 19/19
  primary review folders and 19/19 Asta reports; the first-pass ppu04122
  primary curation gaps are closed.
- Remaining ppu04122 work is module-level synthesis once Falcon access is
  available, plus any future decision to revisit `rhdA`/`sseA` as
  sulfur-relay-specific rather than general sulfur-metabolism side nodes.

## Batch status: ppu03250 / viral_life_cycle_hiv1_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu03250_viral_life_cycle_hiv1_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu03250_viral_life_cycle_hiv1_boundary.md`

Status as of 2026-07-08 PDT / 2026-07-09 UTC:

- 1 candidate curated: the only KEGG `ppu03250` membership gene.
- 1/1 candidate review folders present.
- 1/1 candidate Asta gene-level retrieval reports present.
- 1/1 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/viral_life_cycle_hiv1_boundary.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/viral_life_cycle_hiv1_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__viral_life_cycle_hiv1_boundary__ppu03250-deep-research-falcon.md`.
- Validation complete for the ppiA review and the module.
- Gene review page rendered for the candidate.
- Module page rendered:
  `pages/modules/viral_life_cycle_hiv1_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/viral_life_cycle_hiv1_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/viral_life_cycle_hiv1_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu03250` is not a satisfiable HIV-1 or viral life-cycle pathway in
  KT2440; it is best represented as a boundary/absence KEGG cross-map artifact.
- The only mapped member, `ppiA`, is a cyclophilin-family
  peptidyl-prolyl cis-trans isomerase with protein-folding process context.
- The existing `ppiA` review already accepts GO:0003755
  peptidyl-prolyl cis-trans isomerase activity and GO:0006457 protein folding,
  while marking generic isomerase activity as over-annotated relative to the
  specific PPIase function.
- No viral-life-cycle GO annotation is proposed for `ppiA`; this module
  prevents the KEGG pathway name from driving a false bacterial pathway claim.

## Batch status: ppu04146 / peroxisome_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu04146_peroxisome_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu04146_peroxisome_boundary.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 12 candidates curated: all KEGG `ppu04146` membership genes.
- 12/12 candidate review folders present. `sodA` was fetched during this pass.
- 12/12 candidate Asta gene-level retrieval reports present.
- 12/12 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/peroxisome_boundary.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/peroxisome_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__peroxisome_boundary__ppu04146-deep-research-falcon.md`.
- Validation complete for all 12 gene reviews and the module. Gene warnings
  are non-blocking and mostly reflect expected first-pass Asta context notices
  plus pre-existing warnings on overlap genes.
- Gene review pages rendered for all 12 candidates.
- Module page rendered:
  `pages/modules/peroxisome_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/peroxisome_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/peroxisome_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu04146` is a boundary/absence bucket, not a bacterial peroxisome
  organelle module.
- `katA`, `katE`, and `PP_2887` are catalase/catalase-family oxidative-stress
  detoxification context.
- `sodA` and `sodB` are cytoplasmic superoxide dismutases; `sodA` is curated as
  manganese SOD and `sodB` as iron SOD, with KT2440 literature noting a
  condition-dependent SodA/SodB heterodimer.
- `fadD-I` and `fadD-II` are bacterial long-chain fatty-acid CoA ligases, not
  evidence for peroxisomal beta-oxidation localization.
- `icd`, `idh`, `PP_3394`, `mvaB`, and `nudC` are TCA/NADPH, HMG-CoA, and
  NAD/RNA-cap hydrolase side nodes already better represented in neighboring
  bacterial metabolic modules.
- No peroxisome localization, peroxisome organization, peroxin function, or
  peroxisomal matrix import annotation is proposed for KT2440 from this batch.

## Batch status: ppu04141 / protein_processing_er_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu04141_protein_processing_er_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu04141_protein_processing_er_boundary.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 3 candidates curated: all KEGG `ppu04141` membership genes.
- 3/3 candidate review folders present.
- 3/3 candidate Asta gene-level retrieval reports present.
- 3/3 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/protein_processing_er_boundary.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/protein_processing_er_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__protein_processing_er_boundary__ppu04141-deep-research-falcon.md`.
- Validation complete for all three gene reviews and the module.
- Gene review pages rendered for all three candidates.
- Module page rendered:
  `pages/modules/protein_processing_er_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/protein_processing_er_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/protein_processing_er_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu04141` is not a satisfiable endoplasmic-reticulum protein-processing
  pathway in KT2440; it is best represented as a boundary/absence KEGG
  cross-map artifact around conserved heat-shock chaperones.
- `PP_3234` and `PP_3312` are predicted HSP20-family small heat shock proteins.
  Their local GOA tables are empty, so the reviews add conservative `NEW`
  unfolded-protein-binding annotations from HSP20/alpha-crystallin
  family-domain evidence.
- `htpG` is native bacterial Hsp90-family ATP-dependent protein-folding
  chaperone context, with cytoplasmic protein-folding/proteostasis roles.
- No endoplasmic-reticulum protein-processing GO annotation is proposed for any
  KT2440 member in this bucket.

## Batch status: ppu04148 / efferocytosis_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu04148_efferocytosis_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu04148_efferocytosis_boundary.md`

Status as of 2026-07-08 PDT / 2026-07-09 UTC:

- 2 candidates curated: all KEGG `ppu04148` membership genes.
- 2/2 candidate review folders present.
- 2/2 candidate Asta gene-level retrieval reports present.
- 2/2 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/efferocytosis_boundary.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/efferocytosis_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__efferocytosis_boundary__ppu04148-deep-research-falcon.md`.
- Validation complete for both gene reviews and the module.
- Gene review pages rendered for both candidates.
- Module page rendered:
  `pages/modules/efferocytosis_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/efferocytosis_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/efferocytosis_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu04148` is not a satisfiable eukaryotic efferocytosis pathway in
  KT2440; it is best represented as a boundary/absence KEGG cross-map artifact.
- `speC` is native ornithine decarboxylase/polyamine context. The review now
  validates without warnings after anchoring Asta support in an existing
  annotation decision.
- `petA` is native respiratory complex III/oxidative-phosphorylation context.
  The review now validates without warnings after adding explicit `NEW`
  respiratory electron transport chain and respiratory chain complex III rows
  from UniProt evidence and accepting the plasma membrane localization row.
- No efferocytosis GO annotation is proposed for either bacterial gene; the
  module records absence to prevent the KEGG pathway name from driving a false
  pathway claim.

## Batch status: ppu04156 / integrated_stress_response_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu04156_integrated_stress_response_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu04156_integrated_stress_response_boundary.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 4 candidates curated: all KEGG `ppu04156` membership genes.
- 4/4 candidate review folders present.
- 4/4 candidate Asta gene-level retrieval reports present.
- 4/4 review YAMLs curated with no remaining `PENDING` actions.
- New boundary/absence module created and validated:
  `modules/integrated_stress_response_boundary.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/integrated_stress_response_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__integrated_stress_response_boundary__ppu04156-deep-research-falcon.md`.
- Validation complete for all four gene reviews and the module.
- Gene review pages rendered for all four candidates.
- Module page rendered:
  `pages/modules/integrated_stress_response_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/integrated_stress_response_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/integrated_stress_response_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu04156` is not a satisfiable eukaryotic integrated stress response
  signaling pathway in KT2440; it is best represented as a boundary/absence
  KEGG cross-map artifact.
- `groEL`, `dnaK`, and `htpG` are bacterial cytosolic chaperone/proteostasis
  nodes, not ISR signaling components.
- `PP_5211` is native glutathione-specific
  gamma-glutamylcyclotransferase/glutathione-catabolism context and is already
  represented in `glutathione_metabolism_boundary`.
- No integrated-stress-response signaling GO annotation is proposed for any
  KT2440 member in this bucket.

## Batch status: ppu04980 / cobalamin_transport_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu04980_cobalamin_transport_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu04980_cobalamin_transport_metabolism_boundary.md`

Status as of 2026-07-08 PDT / 2026-07-09 UTC:

- 2 candidates curated: all KEGG `ppu04980` membership genes.
- 2/2 candidate review folders present.
- 2/2 candidate Asta gene-level retrieval reports present.
- 2/2 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/cobalamin_transport_metabolism_boundary.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/cobalamin_transport_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__cobalamin_transport_metabolism_boundary__ppu04980-deep-research-falcon.md`.
- Validation complete for both gene reviews and the module.
- Gene review pages rendered for both candidates.
- Module page rendered:
  `pages/modules/cobalamin_transport_metabolism_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/cobalamin_transport_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/cobalamin_transport_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu04980` supports cobalamin metabolism/cofactor context, but not a
  complete cobalamin transport pathway from the two-gene KT2440 membership.
- `pduO` is native corrinoid/cobalamin adenosyltransferase context. The review
  now validates without warnings after anchoring Asta support in an existing
  annotation decision.
- `metH` is native B12-dependent methionine synthase context, linking
  cobalamin cofactor use to methionine biosynthesis and one-carbon/folate
  metabolism. The review now validates without warnings after anchoring Asta
  support in an existing annotation decision.
- No cobalamin transport GO annotation is proposed from this bucket; the module
  records the boundary call explicitly.

## Batch status: ppu04981 / folate_transport_metabolism_boundary

Batch files:

- `projects/P_PUTIDA/batches/ppu04981_folate_transport_metabolism_boundary.tsv`
- `projects/P_PUTIDA/batches/ppu04981_folate_transport_metabolism_boundary.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 6 candidates curated: all KEGG `ppu04981` membership genes.
- 6/6 candidate review folders present.
- 6/6 candidate Asta gene-level retrieval reports present.
- 6/6 review YAMLs curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/folate_transport_metabolism_boundary.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/folate_transport_metabolism_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__folate_transport_metabolism_boundary__ppu04981-deep-research-falcon.md`.
- Validation complete for all six gene reviews and the module. Gene warnings
  are limited to expected first-pass Asta context notices plus pre-existing
  cytosol-location reflection warnings on the SHMT, DHFR, and ThyA reviews.
- Gene review pages rendered for all six candidates.
- Module page rendered:
  `pages/modules/folate_transport_metabolism_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/folate_transport_metabolism_boundary.yaml
uv run python -m ai_gene_review.validation.module_validator modules/folate_transport_metabolism_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `ppu04981` supports folate cofactor maintenance and folate-linked
  one-carbon metabolism, but not a complete folate transport pathway from the
  six-gene KT2440 membership.
- `glyA1` and `glyA2` are serine hydroxymethyltransferase paralogs feeding
  one-carbon units from serine/glycine metabolism into the THF pool.
- `folA` is the canonical dihydrofolate reductase regenerating
  tetrahydrofolate, while `fau` salvages 5-formyltetrahydrofolate back into
  active one-carbon folate chemistry.
- `thyA` consumes 5,10-methylene-THF for dTMP synthesis, and `metH` consumes
  5-methyl-THF in the cobalamin-dependent methionine-synthase reaction.
- No folate transport GO annotation is proposed from this bucket; the module
  records the transport absence/boundary call explicitly.

## Batch status: UPA00212 / mcl_pha_monomer_supply_from_fas

Batch files:

- `projects/P_PUTIDA/batches/UPA00212_mcl_pha_monomer_supply_from_fas.tsv`
- `projects/P_PUTIDA/batches/UPA00212_mcl_pha_monomer_supply_from_fas.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 1 candidate curated: UniPathway `UPA00212` member `phaG`.
- 1/1 candidate review folder present.
- 1/1 candidate Asta gene-level retrieval report present.
- 1/1 review YAML curated with no remaining `PENDING` actions.
- The initial one-reaction module seed was retired under the multi-part module
  policy; the gene and pathway curation remain recorded in this batch.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/mcl_pha_monomer_supply_from_fas-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__mcl_pha_monomer_supply_from_fas__upa00212-deep-research-falcon.md`.
- The taxon-aware Falcon command resolved the correct local candidate set:
  `phaG` / PP_1408 / O85207.
- Validation complete for the gene review. The former one-part module passed
  validation before retirement; no standalone ModuleReview or page is retained.
- Gene review page rendered for `phaG`.

Main curation conclusions from this batch:

- PSEPK `UPA00212` is satisfiable as a single-gene PhaG bridge from de novo
  fatty-acid synthesis to mcl-PHA monomer supply.
- `phaG` supplies 3-hydroxyacyl-CoA monomers from ACP-bound
  fatty-acid-synthesis intermediates for downstream PhaC polymerization.
- The curation is direction-neutral because the physiological mechanism remains
  debated: direct ACP:CoA transacylation versus thioesterase-like release plus
  acyl-CoA ligation.
- PhaC1/PhaC2 polymerization and beta-oxidation/PhaJ-derived monomer supply
  remain adjacent PHA biology outside this single-gene UniPathway member set.

## Batch status: UPA00529 / glycine_betaine_biosynthesis_boundary

Batch files:

- `projects/P_PUTIDA/batches/UPA00529_glycine_betaine_biosynthesis_boundary.tsv`
- `projects/P_PUTIDA/batches/UPA00529_glycine_betaine_biosynthesis_boundary.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 3 candidates curated: all UniPathway `UPA00529` membership genes (`betA`,
  `betB`, and `betI`).
- 3/3 candidate review folders present.
- 3/3 candidate Asta gene-level retrieval reports present.
- 3/3 review YAMLs curated with no remaining `PENDING` actions.
- New glycine betaine biosynthesis boundary module created and validated:
  `modules/glycine_betaine_biosynthesis_boundary.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/glycine_betaine_biosynthesis_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__glycine_betaine_biosynthesis_boundary__upa00529-deep-research-falcon.md`.
- Fixed `scripts/module_pathway_taxon_deep_research_wrapper.py` so
  UniPathway buckets prefer pathway-membership rows before falling back to
  primary partition rows. A dry run and the final real Falcon attempt confirmed
  the corrected UPA00529 prompt includes all three pathway members.
- Validation complete for all three gene reviews and the module.
- Gene review pages rendered for all three candidates.
- Module page rendered:
  `pages/modules/glycine_betaine_biosynthesis_boundary.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/glycine_betaine_biosynthesis_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/glycine_betaine_biosynthesis_boundary.yaml
```

Main curation conclusions from this batch:

- PSEPK `UPA00529` is satisfiable as choline-derived glycine betaine
  biosynthesis with BetA and BetB as catalytic steps.
- `betA` is retained as membrane-associated choline dehydrogenase and as a
  family-assigned betaine-aldehyde dehydrogenase candidate, while `betB` is the
  dedicated NAD+-dependent betaine-aldehyde dehydrogenase.
- `betI` is a TetR/BetI-family HTH transcriptional repressor. It is included as
  regulatory boundary context for `betT`/`betAB` expression, not as a catalytic
  biosynthetic enzyme.
- The BetA/BetB in vivo division of labor and BetI operator/effector details
  remain open biology/curation questions.
- Transporters and unassigned choline dehydrogenase paralogs remain outside
  this UPA00529 module pending separate evidence.

## Batch status: UPA00219 / peptidoglycan_biosynthesis main route

Batch files:

- `projects/P_PUTIDA/batches/UPA00219_peptidoglycan_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/UPA00219_peptidoglycan_biosynthesis.md`

Status as of 2026-07-09 PDT / 2026-07-10 UTC:

- 25 UniPathway `UPA00219` membership candidates extracted from pathway
  membership.
- 25/25 candidate review folders present.
- 25/25 candidate Asta gene-level retrieval reports present.
- 25/25 review YAMLs curated with no remaining `PENDING` actions.
- Missing UniPathway-primary `PP_1451` / Q88MW7 / PP_1451 and `ddl` /
  A0A140FWM5 / PP_5673 were fetched, Asta-backed, curated, and validated in
  this checkpoint.
- Existing peptidoglycan module extended and validated with a standalone `ddl`
  D-Ala-D-Ala ligase annoton and `PP_1451`/`PP_2320` YkuD/L,D-transpeptidase
  remodeling candidates:
  `modules/peptidoglycan_biosynthesis.yaml`.
- Falcon generic module research remains queued because the earlier real
  `just module-deep-research-falcon peptidoglycan_biosynthesis` command failed
  while Edison Falcon access returns HTTP 402:
  `modules/peptidoglycan_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__peptidoglycan_biosynthesis__upa00219-deep-research-falcon.md`.
- The taxon-aware Falcon command resolved the expected local 25-gene candidate
  set for the main UniPathway peptidoglycan route.
- Validation complete for `PP_1451`, `ddl`, and the extended module.

Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/peptidoglycan_biosynthesis.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/peptidoglycan_biosynthesis.yaml
```

Main curation conclusions from this batch:

- PSEPK `UPA00219` is the main UniPathway view of peptidoglycan biosynthesis,
  covering the de novo Mur route, Ddl paralogs, lipid-linked precursor assembly,
  MurJ flipping, SEDS/PBP polymerization and cross-linking, and selected
  remodeling candidates.
- `ddl` is a third cytoplasmic D-Ala-D-Ala ligase paralog to track alongside
  `ddlA` and `ddlB`.
- `PP_1451` is a predicted signal-peptide-bearing YkuD/L,D-transpeptidase-family
  remodeling candidate; its exact substrate and division of labor with `PP_2320`
  remain open.
- UPA00544 should remain the separate MurNAc/anhMurNAc and muropeptide
  recycling/salvage support arm inside the same peptidoglycan module.

## Batch status: UPA00544 / peptidoglycan_biosynthesis recycling support

Batch files:

- `projects/P_PUTIDA/batches/UPA00544_peptidoglycan_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/UPA00544_peptidoglycan_biosynthesis.md`

Status as of 2026-07-09 PDT / 2026-07-10 UTC:

- 6 candidates covered: `amgK`, `murU`, `anmK`, `mpl`, `mupP`, and `nagZ`.
- 6/6 candidate review folders present.
- 6/6 candidate Asta gene-level retrieval reports present.
- 6/6 review YAMLs curated with no remaining `PENDING` actions.
- Missing UniPathway-primary `mpl` / Q88QE7 / PP_0547 was fetched by accession
  alias, curated, and validated in this pass.
- Existing peptidoglycan module extended and validated with a discrete
  recycling/salvage arm:
  `modules/peptidoglycan_biosynthesis.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/peptidoglycan_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__peptidoglycan_biosynthesis__upa00544-deep-research-falcon.md`.
- The taxon-aware Falcon command resolved the expected local candidate set:
  `amgK`, `murU`, `anmK`, `mpl`, `mupP`, and `nagZ`.
- Validation complete for `mpl` and the extended module.
- Gene review page rendered for `mpl`.
- Module page rendered:
  `pages/modules/peptidoglycan_biosynthesis.html`.
- Project batch page rendered:
  `pages/projects/P_PUTIDA/batches/UPA00544_peptidoglycan_biosynthesis.html`.

Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/peptidoglycan_biosynthesis.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/peptidoglycan_biosynthesis.yaml
```

Main curation conclusions from this batch:

- PSEPK `UPA00544` is a recycling/salvage support view inside the existing
  peptidoglycan module, not a separate de novo biosynthesis route.
- The module now separates MurNAc/anhMurNAc and muropeptide recycling from the
  de novo MurA/MurB/MurC-F precursor pathway while allowing both arms to feed
  UDP-MurNAc-peptide and downstream lipid-linked precursor assembly.
- `nagZ` is the beta-N-acetylhexosaminidase for peptidoglycan fragment
  processing; `anmK` handles anhMurNAc phosphorylation; `mupP`, `amgK`, and
  `murU` form the Pseudomonas MurNAc-to-UDP-MurNAc shortcut; and `mpl`
  reattaches recycled L-Ala-gamma-D-Glu-meso-DAP tripeptide to UDP-MurNAc.
- The UPA00544 boundary should remain inside peptidoglycan rather than the
  broader amino-sugar boundary because its satisfiability depends on cell-wall
  turnover products and peptidoglycan precursor salvage.

## Batch status: UPA00637 / osmoregulated_periplasmic_glucan_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/UPA00637_osmoregulated_periplasmic_glucan_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/UPA00637_osmoregulated_periplasmic_glucan_biosynthesis.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 2 candidates curated: all UniPathway `UPA00637` membership genes (`opgH`
  and `opgG`).
- 2/2 candidate review folders present.
- 2/2 candidate Asta gene-level retrieval reports present.
- 2/2 review YAMLs curated with no remaining `PENDING` actions.
- New osmoregulated periplasmic glucan biosynthesis module created and
  validated:
  `modules/osmoregulated_periplasmic_glucan_biosynthesis.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/osmoregulated_periplasmic_glucan_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__osmoregulated_periplasmic_glucan_biosynthesis__upa00637-deep-research-falcon.md`.
- The taxon-aware Falcon command resolved the correct local candidate set:
  `opgH` / PP_5025 / Q88D04 and `opgG` / PP_5026 / Q88D03.
- Validation complete for both gene reviews and the module.
- Gene review pages rendered for both candidates.
- Module page rendered:
  `pages/modules/osmoregulated_periplasmic_glucan_biosynthesis.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/osmoregulated_periplasmic_glucan_biosynthesis.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/osmoregulated_periplasmic_glucan_biosynthesis.yaml
```

Main curation conclusions from this batch:

- PSEPK `UPA00637` is satisfiable as a compact two-gene OPG biosynthesis
  module.
- `opgH` is the inner-membrane GT2/OpgH glucosyltransferase component; its
  current GO molecular function is the broad but informative
  hexosyltransferase activity.
- `opgG` is the periplasmic OpgD/OpgG-family OPG component. The current
  first-pass review accepts carbohydrate binding and beta-glucan/glucan
  biosynthesis while leaving the exact catalytic versus scaffold role
  unresolved.
- The module should remain separate from alginate, lipopolysaccharide,
  peptidoglycan, cellulose, and generic exopolysaccharide curation buckets.
- GO currently gives useful glucan/beta-glucan process coverage, but an
  OPG-specific process term remains a possible future curation request rather
  than a term asserted in this first pass.

## Batch status: UPA00694 / bacterial_cellulose_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/UPA00694_bacterial_cellulose_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/UPA00694_bacterial_cellulose_biosynthesis.md`

Status as of 2026-07-09 PDT / 2026-07-10 UTC:

- 3 candidates covered: already-curated `bcsA` plus newly curated
  UniPathway-primary `bcsB` and `PP_2638`.
- 3/3 candidate review folders present.
- 3/3 candidate Asta gene-level retrieval reports present.
- 3/3 review YAMLs curated with no remaining `PENDING` actions.
- New bacterial cellulose biosynthesis module created and validated:
  `modules/bacterial_cellulose_biosynthesis.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/bacterial_cellulose_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_cellulose_biosynthesis__upa00694-deep-research-falcon.md`.
- The taxon-aware Falcon command resolved the correct local candidate set:
  `bcsA` / PP_2635 / Q88JL4, `bcsB` / PP_2636 / Q88JL3, and `PP_2638` /
  PP_2638 / Q88JL1.
- Validation complete for the new gene reviews and the module.
- Gene review pages rendered for `bcsB` and `PP_2638`.
- Module page rendered:
  `pages/modules/bacterial_cellulose_biosynthesis.html`.
- Project batch page rendered:
  `pages/projects/P_PUTIDA/batches/UPA00694_bacterial_cellulose_biosynthesis.html`.

Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_cellulose_biosynthesis.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/bacterial_cellulose_biosynthesis.yaml
```

Main curation conclusions from this batch:

- PSEPK `UPA00694` is satisfiable as a compact bacterial Bcs cellulose
  biosynthesis module.
- The existing `modules/cellulose_biosynthesis.yaml` is a plant cellulose
  synthase complex module and explicitly excludes bacterial BcsA machinery, so
  UPA00694 required a separate bacterial module.
- `bcsA` is the UDP-forming cellulose synthase catalytic subunit; `bcsB` is the
  single-pass inner-membrane cyclic-di-GMP-binding regulatory subunit tightly
  associated with BcsA; `PP_2638` is a BcsC-like outer-membrane/accessory
  component required for maximal cellulose synthesis.
- The module should remain separate from alginate, OPG, LPS, peptidoglycan, and
  broad exopolysaccharide curation buckets.

## Batch status: UPA00664 + UPA00666 / bacterial_lipoprotein_maturation

Batch files:

- `projects/P_PUTIDA/batches/UPA00664_bacterial_lipoprotein_maturation.tsv`
- `projects/P_PUTIDA/batches/UPA00664_bacterial_lipoprotein_maturation.md`
- `projects/P_PUTIDA/batches/UPA00666_bacterial_lipoprotein_maturation.tsv`
- `projects/P_PUTIDA/batches/UPA00666_bacterial_lipoprotein_maturation.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 2 missing UniPathway candidates curated: `lgt` from `UPA00664` and `lnt`
  from `UPA00666`.
- `lspA` from `UPA00665` was already curated in the `ppu03060` bacterial
  protein-export batch and is reused here as the middle maturation step.
- 3/3 context-gene review folders present across the paired batch pages.
- 3/3 context-gene Asta gene-level retrieval reports present.
- 3/3 context-gene review YAMLs curated with no remaining `PENDING` actions.
- New bacterial lipoprotein maturation module created and validated:
  `modules/bacterial_lipoprotein_maturation.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/bacterial_lipoprotein_maturation-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted separately for both
  UniPathway buckets and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_lipoprotein_maturation__upa00664-deep-research-falcon.md`
  and
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_lipoprotein_maturation__upa00666-deep-research-falcon.md`.
- Validation complete for `lgt`, `lnt`, the existing `lspA` review, and the
  module.
- Gene review pages rendered for `lgt` and `lnt`; `lspA` was already rendered.
- Module page rendered:
  `pages/modules/bacterial_lipoprotein_maturation.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_lipoprotein_maturation.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/bacterial_lipoprotein_maturation.yaml
```

Main curation conclusions from this batch:

- PSEPK has the canonical bacterial Lgt-LspA-Lnt lipoprotein maturation sequence.
- `lgt` is the inner-membrane phosphatidylglycerol--prolipoprotein
  diacylglyceryl transferase first step and carries a specific MF term
  (`GO:0008961`).
- `lspA` is signal peptidase II/prolipoprotein signal peptidase and remains
  primarily owned by the broad protein-export partition, but it is required for
  the lipoprotein maturation sequence.
- `lnt` is the inner-membrane apolipoprotein N-acyltransferase final step. Its
  existing GOA broad acyltransferase parent was marked `MODIFY` with
  `GO:0016410` N-acyltransferase activity as the proposed replacement.
- Lol-dependent lipoprotein trafficking and mature lipoprotein client functions
  remain outside this maturation-chemistry module.

## Batch status: UPA00729 / trna_ms2io6a37_hydroxylation

Batch files:

- `projects/P_PUTIDA/batches/UPA00729_trna_ms2io6a37_hydroxylation.tsv`
- `projects/P_PUTIDA/batches/UPA00729_trna_ms2io6a37_hydroxylation.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 1 candidate curated: UniPathway `UPA00729` member `miaE`.
- 1/1 candidate review folder present.
- 1/1 candidate Asta gene-level retrieval report present.
- 1/1 review YAML curated with no remaining `PENDING` actions.
- The initial one-reaction module seed was retired under the multi-part module
  policy; the gene and pathway curation remain recorded in this batch.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/trna_ms2io6a37_hydroxylation-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__trna_ms2io6a37_hydroxylation__upa00729-deep-research-falcon.md`.
- Validation complete for the gene review. The former one-part module passed
  validation before retirement; no standalone ModuleReview or page is retained.
- Gene review page rendered for `miaE`.

Main curation conclusions from this batch:

- PSEPK `UPA00729` is satisfiable as a single terminal tRNA-modification
  reaction catalyzed by MiaE.
- `miaE` is already experimentally supported by PMID:32785618 and the GOA EXP
  row for GO:0045301.
- The batch records MiaE's non-heme diiron monooxygenase context, but the
  pathway-defining molecular function is the specific tRNA ms2i6A37 hydroxylase
  activity.
- Upstream MiaA/MiaB formation of ms2i6A37 is substrate-supply context and is
  outside this single-gene UPA00729 member set.

## Batch status: UPA00989 / trna_m7g46_methylation

Batch files:

- `projects/P_PUTIDA/batches/UPA00989_trna_m7g46_methylation.tsv`
- `projects/P_PUTIDA/batches/UPA00989_trna_m7g46_methylation.md`

Status as of 2026-07-09 PDT:

- 1 candidate curated: UniPathway `UPA00989` member `trmB`.
- 1/1 candidate review folder present.
- 1/1 candidate Asta gene-level retrieval report present.
- 1/1 review YAML curated with no remaining `PENDING` actions.
- The initial one-reaction module seed was retired under the multi-part module
  policy; the gene and pathway curation remain recorded in this batch.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/trna_m7g46_methylation-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__trna_m7g46_methylation__upa00989-deep-research-falcon.md`.
- Validation complete for the gene review. The former one-part module passed
  validation before retirement; no standalone ModuleReview or page is retained.
- Gene review page rendered for `trmB`.

Main curation conclusions from this batch:

- PSEPK `UPA00989` is satisfiable as a single tRNA-modification reaction
  catalyzed by TrmB.
- `trmB` is a SAM-dependent tRNA
  (guanine(46)-N7)-methyltransferase forming N7-methylguanosine at position 46
  in tRNA.
- The exact molecular-function annotation GO:0008176 and process annotation
  GO:0106004 were accepted as core.
- The broad RNA guanine-N7 methylation parent was retained as non-core context.
- The TreeGrafter `GO:0043527` tRNA methyltransferase-complex annotation was
  marked over-annotated because local first-pass evidence supports the TrmB
  enzyme/reaction but not a stable methyltransferase-complex membership.

## Batch status: UPA00345 / efp_translation_stall_rescue

Batch files:

- `projects/P_PUTIDA/batches/UPA00345_efp_translation_stall_rescue.tsv`
- `projects/P_PUTIDA/batches/UPA00345_efp_translation_stall_rescue.md`

Status as of 2026-07-09 PDT:

- 1 candidate curated: UniPathway `UPA00345` member `efp`.
- 1/1 candidate review folder present.
- 1/1 candidate Asta gene-level retrieval report present.
- 1/1 review YAML curated with no remaining `PENDING` actions.
- The review folder was seeded by accession alias Q88LS0 because the
  symbol-based fetch did not resolve `efp`; the review was then corrected to
  `gene_symbol: efp`.
- New EF-P translation stall rescue module created and validated:
  `modules/efp_translation_stall_rescue.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/efp_translation_stall_rescue-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__efp_translation_stall_rescue__upa00345-deep-research-falcon.md`.
- Validation complete for the gene review and the module.
- Gene review page rendered for `efp`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/efp_translation_stall_rescue.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/efp_translation_stall_rescue.yaml
```

Main curation conclusions from this batch:

- PSEPK `UPA00345` is satisfiable as a single-gene translation-factor module
  centered on EF-P.
- `efp` encodes cytoplasmic elongation factor P, which stimulates peptide-bond
  formation during translational elongation and rescues stalled cytosolic
  ribosomes, especially polyproline stalls.
- EarP-dependent Arg32 rhamnosylation and dTDP-rhamnose supply are activation
  context owned by adjacent modules, not members of the UPA00345 pathway bucket.
- Broad `regulation of translation` and `peptide biosynthetic process`
  annotations were retained as non-core context because the module core is the
  more specific EF-P elongation/stall-rescue function.

## Batch status: UPA00539 / pqq_biosynthesis

Batch files:

- `projects/P_PUTIDA/batches/UPA00539_pqq_biosynthesis.tsv`
- `projects/P_PUTIDA/batches/UPA00539_pqq_biosynthesis.md`

Status as of 2026-07-09 PDT / 2026-07-09 UTC:

- 7 candidates curated: all UniPathway `UPA00539` membership genes.
- 7/7 candidate review folders present.
- 7/7 candidate Asta gene-level retrieval reports present.
- 7/7 review YAMLs curated with no remaining `PENDING` actions.
- New PQQ biosynthesis module created and validated:
  `modules/pqq_biosynthesis.yaml`.
- Falcon generic module research was attempted with the real module-level
  command and failed while Edison Falcon access returns HTTP 402:
  `modules/pqq_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with the real taxon-aware
  command and failed while Edison Falcon access returns HTTP 402:
  `projects/P_PUTIDA/deep-research/PSEPK__pqq_biosynthesis__upa00539-deep-research-falcon.md`.
- Validation complete for all seven gene reviews and the module.
- Gene review pages rendered for all seven candidates.
- Module page rendered:
  `pages/modules/pqq_biosynthesis.html`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/pqq_biosynthesis.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/pqq_biosynthesis.yaml
```

Main curation conclusions from this batch:

- PSEPK `UPA00539` is a satisfiable compact PQQ cofactor-biosynthesis route:
  `pqqA` precursor peptide, `pqqD1`/`pqqD2` PqqA-binding chaperones, `pqqE`
  radical-SAM peptide cyclase, `pqqF` M16-family processing protease, `pqqB`
  maturation oxygenase/hydroxylase, and `pqqC` terminal PQQ synthase.
- `pqqD1` and `pqqD2` were fetched by accession and curated from stubs. Their
  PQQ-biosynthesis process annotations are accepted, while the InterPro-derived
  `quinone binding` molecular-function annotations are marked over-annotated
  because the supported role is PqqA peptide binding/presentation.
- The PqqD1/PqqD2 division of labor remains unresolved in KT2440 and is tracked
  as a module knowledge gap.
- Literature mentions a KT2440 `pqqFABCDEG` region, but the current local
  UniProt/pathway metadata assign PP_0382 as `davA` and do not provide an
  unambiguous UPA00539 `pqqG` member. The module excludes `pqqG` until that
  identifier issue is reconciled.
- Mature PQQ utilization by periplasmic quinoproteins is downstream context, not
  part of the strict biosynthesis module.

## Batch status: module:protein_folding_targeting_turnover / chaperone_folding_holdase_foldase

Batch files:

- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.md`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_chaperone_folding_holdase_foldase.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_chaperone_folding_holdase_foldase.md`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_atp_dependent_protease_turnover.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_cofactor_metal_maturation_chaperones.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_cell_wall_envelope_peptidase_inhibitor.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_peptide_processing_aminopeptidases.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_periplasmic_membrane_secreted_protease_qc.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_dna_damage_or_repair_spillover_proteases.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_phage_mobile_protease_spillovers.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_low_information_peptidase_spillovers.tsv`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 91-gene protein folding/targeting/turnover functional bucket has been
  split into 9 curation-scale buckets: chaperone/foldase/co-chaperone systems,
  ATP-dependent protease turnover, cofactor/metal maturation chaperones,
  cell-wall/envelope peptidase and inhibitor proteins, aminopeptidases,
  periplasmic/membrane/secreted protease quality control, DNA-damage/repair
  spillover proteases, phage/mobile proteases, and low-information peptidase
  spillovers.
- The 13-gene `chaperone_folding_holdase_foldase` split is first-pass complete:
  `hslO`, `surA`, `clpB`, `slyD`, `hscB`, `hscA`, `groES`, `PP_1548`,
  `cspA-II`, `PP_3316`, `grpE`, `cbpM`, and `cbpA`.
- 13/13 candidate review folders are present.
- 13/13 candidate Asta gene-level retrieval reports are present.
- 13/13 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/bacterial_chaperone_protein_folding_boundary.yaml`.
- The worklist generator now treats
  `module:protein_folding_targeting_turnover` as a partitioned umbrella bucket
  and points curators to the partition ledger.
- Validation complete for all thirteen gene reviews and the module. The
  expected residual warnings are provenance/conservatism warnings only:
  `PP_1548` has no core function because the evidence does not support one, and
  older already-curated `surA`/`clpB` reviews do not cite their newly fetched
  Asta retrieval files.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_chaperone_protein_folding_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/bacterial_chaperone_protein_folding_boundary.yaml
```

Main curation conclusions from this split:

- `hslO` is a cytoplasmic redox-regulated Hsp33-family holdase/chaperone with
  unfolded-protein binding and protein-refolding context.
- `surA` remains the periplasmic outer-membrane-protein chaperone/foldase
  context, including peptidyl-prolyl cis-trans isomerase activity.
- `clpB` is an ATP-dependent cytoplasmic disaggregase/refolding factor; the
  review now has an explicit `NEW` `misfolded protein binding` row matching the
  pre-existing core-function call.
- `slyD` is a cytoplasmic FKBP-type PPIase/refolding candidate; broad generic
  isomerase activity is over-annotated relative to the specific PPIase term.
- `hscA`/`hscB` are treated as the Fe-S-cluster maturation chaperone pair:
  HscA provides ATPase/chaperone activity, while HscB stimulates HscA and binds
  the chaperone system.
- `groES` and `grpE` are retained as co-chaperone factors in the GroEL and
  DnaK systems.
- `cbpA`/`cbpM` are kept as a DnaJ-like/curved-DNA-binding regulatory branch:
  CbpA has bent-DNA and chaperone/refolding context, while CbpM is a CbpA
  modulatory protein.
- `cspA-II` is kept as nucleic-acid cold-shock chaperone side context, not as a
  protein-folding factor.
- `PP_1548` is retained as a no-core unresolved DjlA_N/TerB-like candidate
  pending evidence that the product has a functional chaperone role.

## Batch status: module:protein_folding_targeting_turnover / atp_dependent_protease_turnover

Batch files:

- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_atp_dependent_protease_turnover.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_atp_dependent_protease_turnover.md`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 13-gene `atp_dependent_protease_turnover` split is first-pass complete:
  `PP_0680`, `sspB`, `lon-I`, `clpP`, `clpX`, `lon-II`, `PP_3045`,
  `PP_3267`, `clpA`, `clpS`, `PP_4814`, `hslV`, and `hslU`.
- 13/13 candidate review folders are present.
- 13/13 candidate Asta gene-level retrieval reports are present.
- 13/13 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/bacterial_atp_dependent_protein_turnover_boundary.yaml`.
- Validation complete for all thirteen gene reviews and the module. The
  expected residual warnings are provenance/conservatism warnings only:
  already-curated `clpX` does not cite its newly fetched Asta retrieval file,
  and `PP_4814` has no core function because current evidence supports only a
  Lon N-terminal-domain fragment/context.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_atp_dependent_protein_turnover_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/bacterial_atp_dependent_protein_turnover_boundary.yaml
```

Main curation conclusions from this split:

- `PP_0680`, `lon-I`, and `lon-II` are treated as Lon/peptidase S16-family
  ATP-dependent proteases; full-length Lon proteins retain ATP-dependent
  peptidase activity, ATP hydrolysis where annotated, protein quality-control
  or protein-catabolic processes, and secondary DNA-binding context where
  supported.
- `clpP` and `PP_3045` are ClpP-family proteolytic subunits; ATPase binding and
  Clp complex membership are retained, while broad serine endopeptidase class
  terms are non-core relative to the ATP-dependent peptidase/Clp context.
- `PP_3267` has no fetched GOA rows but carries ClpP/TepA and CLP_protease
  domain evidence, so only conservative generic peptidase/proteolysis `NEW`
  rows are added.
- `clpA` is curated as a ClpA-family AAA+ ATPase/unfoldase. The EC-derived
  serine endopeptidase annotation is removed because ClpA is not the catalytic
  ClpP subunit.
- `clpX` retains the preexisting reviewed ClpXP unfoldase/chaperone decisions,
  including correction of the HslUV complex misassignment to Clp complex
  context.
- `clpS` retains the preexisting ClpAP adaptor/N-recognin review, while `sspB`
  now has a `NEW` endopeptidase-regulator activity row to capture its ClpXP
  specificity-enhancing role without using generic protein binding.
- `hslV` is the HslUV catalytic threonine-protease subunit; broad peptidase
  activity is over-annotated relative to threonine-type endopeptidase activity.
- `hslU` is the HslUV AAA+ ATPase/unfoldase and proteasome activator. Its
  peptidase activity annotation is removed because HslV is the catalytic
  peptidase subunit.
- `PP_4814` is retained as a no-core Lon N-terminal-domain protein pending
  stronger evidence for an autonomous adaptor or catalytic role.

## Batch status: module:protein_folding_targeting_turnover / cofactor_metal_maturation_chaperones

Batch files:

- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_cofactor_metal_maturation_chaperones.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_cofactor_metal_maturation_chaperones.md`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 12-gene `cofactor_metal_maturation_chaperones` split is first-pass
  complete: `PP_0588`, `sdhE`, `ureD`, `ureE`, `ureF`, `ureG`, `cobW`, `zinU`,
  `PP_4836`, `yggW`, `PP_5361`, and `PP_5393`.
- 12/12 candidate review folders are present.
- 12/12 candidate Asta gene-level retrieval reports are present.
- 12/12 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/cofactor_metal_maturation_chaperone_boundary.yaml`.
- Validation complete for all twelve gene reviews and the module with no
  warnings.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/cofactor_metal_maturation_chaperone_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/cofactor_metal_maturation_chaperone_boundary.yaml
```

Main curation conclusions from this split:

- `PP_0588` and `PP_4836` are retained as copper-chaperone candidates:
  `PP_0588` through HMA/copper-binding context and `PP_4836` through PCu(A)C
  copper-chaperone assignment.
- `PP_5393` is kept at conservative HMA-domain metal-ion-binding level pending
  stronger evidence for the delivered metal and target protein.
- `sdhE` is an FAD assembly/flavinylation factor for SdhA and related
  flavoproteins; succinate metabolism is kept as non-core pathway context.
- `ureD`, `ureE`, `ureF`, and `ureG` are curated as urease nickel-metallocenter
  maturation factors, with `ureE` as the nickel donor/metallochaperone and
  `ureG` as the GTPase maturation factor.
- `cobW`, `zinU`, and `PP_5361` are treated as ZNG1/CobW-family
  GTP-dependent zinc chaperones. The `cobW` cobalamin-biosynthesis annotation is
  removed because the name/family transfer does not establish a cobalamin-route
  role in KT2440.
- `yggW` is treated as HemW heme-binding and 4Fe-4S cofactor-binding context.
  Coproporphyrinogen oxidase and generic catalytic activity are marked
  over-annotated relative to the heme-chaperone evidence.

## Batch status: module:protein_folding_targeting_turnover / cell_wall_envelope_peptidase_inhibitor

Batch files:

- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_cell_wall_envelope_peptidase_inhibitor.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_cell_wall_envelope_peptidase_inhibitor.md`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 16-gene `cell_wall_envelope_peptidase_inhibitor` split is first-pass
  complete: `PP_0435`, `yfhM`, `PP_1026`, `PP_1442`, `PP_1669`, `PP_1670`,
  `prc`, `PP_2108`, `PP_2364`, `eco`, `PP_4799`, `PP_5057`, `ctpA`,
  `PP_5092`, `PP_5323`, and `PP_5729`.
- 16/16 candidate review folders are present.
- 16/16 candidate Asta gene-level retrieval reports are present.
- 16/16 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/envelope_cell_wall_peptidase_inhibitor_boundary.yaml`.
- Validation complete for all sixteen gene reviews and the module. The expected
  residual warnings are `PP_2108` and `PP_5729` having no core function because
  current evidence is limited to low-information M15A C-terminal-domain or I78
  inhibitor-family context.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/envelope_cell_wall_peptidase_inhibitor_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/envelope_cell_wall_peptidase_inhibitor_boundary.yaml
```

Main curation conclusions from this split:

- `PP_0435`, `PP_1026`, `PP_5057`, and `PP_5323` are retained as M23/M37-family
  metalloendopeptidase candidates. `PP_0435` additionally carries supported
  peptidoglycan turnover, cell-envelope localization, and peptidoglycan binding.
- `PP_1669`, `PP_1670`, and `PP_5092` are NlpC/P60 Peptidase C40-family
  cysteine-type peptidase candidates in exported/envelope context.
- `prc` and `ctpA` are periplasmic S41A-family tail-specific or
  C-terminal-processing serine peptidases. Broad signal-transduction transfer
  was marked over-annotated rather than used as core function.
- `PP_2364` is an M14-family metallocarboxypeptidase candidate, and `PP_4799`
  is a Peptidase S66 muramoyltetrapeptide carboxypeptidase candidate. `PP_4799`
  had no fetched GOA rows, so missing UniProt-supported carboxypeptidase,
  serine-type peptidase, and proteolysis rows were added as `NEW`.
- `yfhM`, `PP_1442`, and `eco` are protease inhibitors: bacterial
  alpha-2-macroglobulin, chagasin/I42 cysteine endopeptidase inhibitor, and
  ecotin serine endopeptidase inhibitor, respectively.
- `PP_2108` and `PP_5729` are left no-core pending stronger evidence for active
  M15A peptidase or peptidase-inhibitor activity.

## Batch status: module:protein_folding_targeting_turnover / peptide_processing_aminopeptidases

Batch files:

- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_peptide_processing_aminopeptidases.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_peptide_processing_aminopeptidases.md`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 13-gene `peptide_processing_aminopeptidases` split is first-pass complete:
  `prlC`, `PP_0203`, `mtfA`, `map`, `apeB`, `PP_1748`, `yegQ`, `PP_2704`,
  `ydcP`, `PP_4752`, `PP_4949`, `pepP`, and `PP_5629`.
- 13/13 candidate review folders are present.
- 13/13 candidate Asta gene-level retrieval reports are present.
- 13/13 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/protein_turnover_peptide_processing_boundary.yaml`.
- Validation complete for all thirteen gene reviews and the module with no
  warnings. A first validation pass caught obsolete `GO:0019877`
  `diaminopimelate biosynthetic process` from UniProt as a process label; the
  generator now removes that authored process row and keeps only the supported
  `GO:0050118` N-acetyldiaminopimelate deacetylase molecular function for
  `PP_2704`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/protein_turnover_peptide_processing_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/protein_turnover_peptide_processing_boundary.yaml
```

Main curation conclusions from this split:

- `map` is the specific initiator methionyl aminopeptidase for nascent-protein
  N-terminal processing; broad metalloaminopeptidase and metal-binding rows are
  non-core context.
- `pepP` and `PP_4752` are M24B-family Xaa-Pro aminopeptidase candidates, with
  `pepP` supported by GOA and `PP_4752` added as a missing `NEW`
  aminopeptidase row from UniProt/domain evidence.
- `apeB`, `PP_1748`, and `mtfA` are M18, M42, and M90/MtfA-family
  aminopeptidase candidates, respectively.
- `prlC` is a cytosolic M3-family oligopeptidase/metalloendopeptidase in
  peptide turnover.
- `yegQ`, `ydcP`, and `PP_5629` are retained at generic peptidase level because
  U32 or DJ-1/PfpI-domain evidence does not establish substrate-specific
  peptidase function.
- `PP_0203` is curated as an M20A dipeptidase/acylase with acetylornithine
  deacetylase/L-arginine-biosynthesis family-transfer context, while `PP_2704`
  is curated as an M20-family N-acetyldiaminopimelate deacetylase without using
  the obsolete process term.
- `PP_4949` is a cytosolic TldD/PmbA/U62-family metallopeptidase candidate.

## Batch status: module:protein_folding_targeting_turnover / periplasmic_membrane_secreted_protease_qc

Batch files:

- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_periplasmic_membrane_secreted_protease_qc.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_periplasmic_membrane_secreted_protease_qc.md`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 12-gene `periplasmic_membrane_secreted_protease_qc` split is first-pass
  complete: `qmcA`, `PP_0759`, `pmbA`, `PP_1232`, `PP_1499`, `PP_4113`,
  `PP_4924`, `PP_5112`, `PP_5115`, `PP_5116`, `PP_5455`, and `PP_5604`.
- 12/12 candidate review folders are present.
- 12/12 candidate Asta gene-level retrieval reports are present.
- 12/12 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/envelope_protease_quality_control_boundary.yaml`.
- Validation complete for all twelve gene reviews and the module. The expected
  residual warnings are `qmcA` and `PP_5455` having no core function because
  current evidence supports only SPFH/band-7 membrane context or an M15A
  C-terminal-domain fragment, respectively.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/envelope_protease_quality_control_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/envelope_protease_quality_control_boundary.yaml
```

Main curation conclusions from this split:

- `PP_0759` and `PP_1232` are M48-family envelope metalloendopeptidase
  candidates. `PP_1232` is BepA-like and periplasmic/membrane associated, so it
  is represented as beta-barrel assembly/quality-control context.
- `pmbA` is a cytosolic TldD/PmbA/U62-family metallopeptidase candidate.
- `PP_1499` is retained as a QEGLA/MATCAP metallopeptidase candidate with
  flavohemoglobin/nitric-oxide regulation context; its substrate remains
  unresolved.
- `PP_4113`, `PP_4924`, and `PP_5604` are S8/S53 or subtilase-family
  serine-type endopeptidase candidates. `PP_4924` is the large
  membrane-associated subtilase/furin-like case with calcium-binding context.
- `PP_5112`, `PP_5115`, and `PP_5116` are M16-family metallopeptidase
  candidates. `PP_5116` had only metal-binding GOA context, so missing
  metallopeptidase/proteolysis rows were added as `NEW`.
- `qmcA` and `PP_5455` are intentionally left no-core pending evidence for a
  direct catalytic protease role.
- Imported obsolete `GO:0051603` protein-catabolism context is not used as an
  authored core process.

## Batch status: module:protein_folding_targeting_turnover / dna_damage_or_repair_spillover_proteases

Batch files:

- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_dna_damage_or_repair_spillover_proteases.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_dna_damage_or_repair_spillover_proteases.md`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 3-gene `dna_damage_or_repair_spillover_proteases` split is first-pass
  complete: `PP_0758`, `PP_2493`, and `PP_2941`.
- 3/3 candidate review folders are present.
- 3/3 candidate Asta gene-level retrieval reports are present.
- 3/3 review YAMLs are curated with no remaining `PENDING` actions.
- This split extends the existing validated
  `modules/dna_bucket_architectural_rna_protein_spillover_boundary.yaml`
  rather than creating a separate module.
- Validation complete for all three gene reviews and the extended module.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/dna_bucket_architectural_rna_protein_spillover_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/dna_bucket_architectural_rna_protein_spillover_boundary.yaml
```

Main curation conclusions from this split:

- `PP_0758` and `PP_2941` are SRAP/HMCES-like abasic-site processing proteins
  with InterPro-backed single-stranded DNA binding and protein-DNA covalent
  cross-link repair. The protease-like signal is treated as family/keyword
  spillover, not as general protein-turnover evidence.
- `PP_2493` had no fetched GOA rows. It is curated conservatively as a
  RadC/UPF0758/JAB/MPN metalloprotease-like protein with `NEW`
  metallopeptidase activity and proteolysis rows from UniProt/domain evidence.
  A direct DNA-repair process was not added from family naming alone.
- The extended module records this as a DNA/repair boundary extension to close
  the overlap between protein-turnover keywords and DNA-damage repair families.

## Batch status: module:protein_folding_targeting_turnover / phage_mobile_protease_spillovers

Batch files:

- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_phage_mobile_protease_spillovers.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_phage_mobile_protease_spillovers.md`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 2-gene `phage_mobile_protease_spillovers` split is first-pass complete:
  `PP_1566` and `PP_3878`.
- 2/2 candidate review folders are present.
- 2/2 candidate Asta gene-level retrieval reports are present.
- 2/2 review YAMLs are curated with no remaining `PENDING` actions.
- This split extends the existing validated
  `modules/phage_structural_packaging_boundary.yaml` rather than creating a
  separate protein-turnover module.
- Validation complete for both gene reviews and the extended module.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/phage_structural_packaging_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/phage_structural_packaging_boundary.yaml
```

Main curation conclusions from this split:

- `PP_1566` had no fetched GOA rows. It is curated with `NEW` generic U35/S78
  prohead peptidase activity, proteolysis, and virion-assembly context from
  UniProt/domain evidence.
- `PP_3878` is a phage minor capsid protein C with Peptidase S49 support.
  Proteolysis is accepted, the generic peptidase row is modified toward
  `GO:0008236` serine-type peptidase activity, and virion-assembly context is
  added.
- Both genes are routed to prophage structural maturation context and are not
  treated as host protein-turnover enzymes.

## Batch status: module:protein_folding_targeting_turnover / low_information_peptidase_spillovers

Batch files:

- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_low_information_peptidase_spillovers.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_low_information_peptidase_spillovers.md`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.tsv`
- `projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 7-gene `low_information_peptidase_spillovers` split is first-pass
  complete: `PP_0831`, `PP_2447`, `PP_2685`, `pfpI`, `PP_2855`, `PP_4583`,
  and `PP_4913`.
- 7/7 candidate review folders are present.
- 7/7 candidate Asta gene-level retrieval reports are present.
- 7/7 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/protein_turnover_peptidase_spillover_boundary.yaml`.
- Validation complete for all seven gene reviews and the module. The expected
  residual warnings are `PP_2447` and `PP_2685` having no core function because
  current evidence is limited to product/domain-level peptidase-family context
  without substrate, process, or catalytic specificity.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/protein_turnover_peptidase_spillover_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/protein_turnover_peptidase_spillover_boundary.yaml
```

Main curation conclusions from this split:

- `PP_0831` had no fetched GOA rows but carries S1/PA, chymotrypsin-like, and
  Trypsin_2 domain evidence, so conservative `NEW` serine-type endopeptidase
  activity and proteolysis rows were added.
- `PP_2447` and `PP_2685` are left no-core unresolved. Both have peptidase-like
  family/domain evidence, but neither has fetched GOA rows or enough substrate
  or pathway information to justify adding a generic GO function in this pass.
- `pfpI` is retained as a generic PfpI/C56-family peptidase/proteolysis
  candidate; broad hydrolase activity is marked over-annotated.
- `PP_2855` is retained as a membrane-associated Peptidase C39 generic
  peptidase/proteolysis candidate. The imported ATP-binding row is kept
  non-core because the local record does not establish an ATPase or transporter
  energy-coupling role.
- `PP_4583` is accepted as an S9A-family serine-type endopeptidase, with
  generic peptidase parent rows marked over-annotated.
- `PP_4913` is accepted as a clan AA retropepsin-like aspartic-type
  endopeptidase with proteolysis context.
- This closes the 91-gene protein folding/targeting/turnover umbrella: all nine
  splits now have review folders, curated reviews, Asta reports, and validated
  module representation.

## Batch status: module:translation_rna_processing / nonribosomal_peptide_synthetase_spillovers

Batch files:

- `projects/P_PUTIDA/batches/module_translation_rna_processing_nonribosomal_peptide_synthetase_spillovers.tsv`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_nonribosomal_peptide_synthetase_spillovers.md`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_partition.tsv`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 4-gene `nonribosomal_peptide_synthetase_spillovers` split is first-pass
  complete: `pvdD`, `pvdJ`, `pvdI`, and `pvdL`.
- 4/4 candidate review folders are present.
- 4/4 candidate Asta gene-level retrieval reports are present.
- 4/4 review YAMLs are curated with no remaining `PENDING` actions.
- This split extends the existing validated
  `modules/siderophore_biosynthesis_boundary.yaml` rather than creating a
  translation/RNA-processing module.
- Validation complete for all four gene reviews and the extended module.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/siderophore_biosynthesis_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/siderophore_biosynthesis_boundary.yaml
```

Main curation conclusions from this split:

- `pvdD` was already curated as the terminal pyoverdine NRPS anchor; this pass
  added Asta coverage and folded it into the extended siderophore module node.
- `pvdJ` and `pvdI` are ferribactin/pyoverdine NRPS subunits with repeated
  adenylation, condensation, and phosphopantetheine carrier domains. Generic
  catalytic activity was modified to NRPS activity, phosphopantetheine binding
  was modified to phosphopantetheine-dependent carrier activity, and broad
  secondary-metabolite context was routed to siderophore/pyoverdine
  biosynthesis.
- `pvdI` enterobactin biosynthesis and enterobactin synthetase complex rows
  were treated as wrong-family over-transfer from another siderophore NRPS
  system.
- `pvdL` was curated as an initiation/early pyoverdine NRPS subunit. Lipid
  biosynthesis was modified to pyoverdine biosynthesis because the FAAL/FAAC
  domain is starter-unit context, not evidence that the gene is a lipid
  biosynthesis enzyme. Actinobacterium-type cell wall biogenesis was removed as
  a taxon/pathway over-transfer.
- Asta retrieval for these NRPS genes was fast but mostly nonspecific; it is
  retained as provenance, while the curation decisions use UniProt/domain
  evidence and the existing pyoverdine NRPS pathway context.
- The `module:translation_rna_processing` umbrella is now first-pass complete:
  all nine splits are curated, Asta-backed, validated, and represented in
  modules or routed boundary views.

## Batch status: module:translation_rna_processing / low_information_rna_binding_or_enzyme_spillovers

Batch files:

- `projects/P_PUTIDA/batches/module_translation_rna_processing_low_information_rna_binding_or_enzyme_spillovers.tsv`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_low_information_rna_binding_or_enzyme_spillovers.md`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_partition.tsv`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 2-gene `low_information_rna_binding_or_enzyme_spillovers` split is
  first-pass complete: `PP_2182` and `PP_2953`.
- 2/2 candidate review folders are present.
- 2/2 candidate Asta gene-level retrieval reports are present.
- 2/2 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/translation_rna_processing_spillover_boundary.yaml`.
- Validation complete for both gene reviews and the module. The expected
  residual warning is that the available Asta files are not cited as biological
  support in annotation decisions, because the retrieval snippets were generic
  rather than gene-functional evidence.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/translation_rna_processing_spillover_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/translation_rna_processing_spillover_boundary.yaml
```

Main curation conclusions from this split:

- `PP_2182` is retained as a ProQ/FinO-domain RNA-chaperone candidate. RNA
  strand annealing activity, RNA strand-exchange activity, post-transcriptional
  regulation of gene expression, and cytosol are accepted or retained, while
  generic RNA binding is kept non-core because the strand-level functions are
  more informative.
- `PP_2953` is routed out of RNA processing as a predicted soluble zinc-type
  alcohol dehydrogenase-like oxidoreductase. NADPH-dependent quinone reductase
  activity and cytosol are accepted; zinc binding is retained as cofactor/domain
  context and generic oxidoreductase activity is marked over-annotated.
- `just fetch-gene` could not populate either review because UniProt REST
  returned HTTP 500 for Q88KV7 and Q88IP6 on 2026-07-10. The local review
  inputs therefore use live QuickGO rows plus explicitly marked fallback
  UniProt-style context assembled from the project gene-list metadata.
- The partition snapshot for `PP_2953` still contains an RNA-binding keyword
  and older RNA-binding/cytoplasm GO IDs, but live QuickGO returned quinone
  reductase, zinc binding, oxidoreductase, and cytosol rows. The review follows
  the live GOA rows and does not force an RNA-processing assignment.
- The `module:translation_rna_processing` umbrella is now first-pass complete:
  all nine splits are curated, Asta-backed, validated, and represented in
  modules or routed boundary views.

## Batch status: module:translation_rna_processing / transcription_rna_polymerase_spillovers

Batch files:

- `projects/P_PUTIDA/batches/module_translation_rna_processing_transcription_rna_polymerase_spillovers.tsv`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_transcription_rna_polymerase_spillovers.md`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_partition.tsv`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 6-gene `transcription_rna_polymerase_spillovers` split is first-pass
  complete: `nusB`, `rapA`, `PP_2266`, `PP_4553`, `dksA`, and `nusA`.
- 6/6 candidate review folders are present.
- 6/6 candidate Asta gene-level retrieval reports are present.
- 6/6 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/transcription_rna_polymerase_spillover_boundary.yaml`.
- Validation complete for all six gene reviews and the module. The expected
  residual warning is that the available Asta files are not cited as biological
  support in annotation decisions, because they were used as fast retrieval
  provenance rather than direct evidence.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/transcription_rna_polymerase_spillover_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/transcription_rna_polymerase_spillover_boundary.yaml
```

Main curation conclusions from this split:

- `nusB` and `nusA` are routed to transcription termination/antitermination
  context. Generic RNA or nucleic-acid binding rows are kept narrow or
  over-annotation-aware, while antitermination and termination process context
  is retained as core where supported.
- `rapA` is retained as an RNA polymerase-associated ATP-dependent regulatory
  factor. Generic hydrolase activity is modified to ATP hydrolysis activity,
  and ATP binding is kept as non-core nucleotide-binding context.
- `dksA` is retained as an RNA polymerase-binding transcription regulator with
  zinc-binding cofactor context and gene-expression regulation process support.
- `PP_2266` is retained as an RNA-polymerase side-node/candidate with
  DNA-directed RNA polymerase activity and transcription process context, but
  it is not folded into the compact canonical RNAP-core module.
- `PP_4553` is retained as an ECF sigma-factor side node. Broad DNA binding and
  generic transcription-factor activity are treated as less informative than
  sigma factor activity and regulation of transcription initiation.
- `just fetch-gene` could not populate `nusB`, `rapA`, `PP_2266`, `PP_4553`, or
  `dksA` because UniProt REST returned HTTP 500 on 2026-07-10. `nusA` fetched
  normally. The fallback reviews are explicitly marked as local UniProt-style
  context assembled from the project gene-list metadata plus live QuickGO rows.
- The `module:translation_rna_processing` umbrella is now first-pass complete:
  all nine splits are curated, Asta-backed, validated, and represented in
  modules or routed boundary views.

## Batch status: module:translation_rna_processing / translation_factors_ribosome_rescue

Batch files:

- `projects/P_PUTIDA/batches/module_translation_rna_processing_translation_factors_ribosome_rescue.tsv`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_translation_factors_ribosome_rescue.md`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_partition.tsv`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 10-gene `translation_factors_ribosome_rescue` split is first-pass
  complete: `hslR`, `selB`, `ettA`, `ychF`, `pth`, `lepA`, `frr`, `arfB`,
  `infA`, and `smpB`.
- 10/10 candidate review folders are present.
- 10/10 candidate Asta gene-level retrieval reports are present.
- 10/10 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/translation_factor_ribosome_rescue_boundary.yaml`.
- Validation complete for all ten gene reviews and the module. The expected
  residual warning is that the available Asta files are not cited as biological
  support in annotation decisions, because they were used as fast retrieval
  provenance rather than direct evidence.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/translation_factor_ribosome_rescue_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/translation_factor_ribosome_rescue_boundary.yaml
```

Main curation conclusions from this split:

- `infA`, `selB`, `lepA`, and `ettA` are retained as initiation,
  selenocysteine-specific elongation, EF-4/back-translocation, and
  ATP-dependent translational-throttle factors.
- `frr`, `pth`, `arfB`, and `smpB` are retained as ribosome recycling,
  peptidyl-tRNA hydrolase, alternative stalled-ribosome rescue, and
  tmRNA/SmpB trans-translation context.
- `hslR` is retained as a heat-shock, ribosomal large-subunit and
  single-stranded-RNA-binding protein; generic DNA binding is marked
  over-annotated.
- `ychF` is retained as a ribosome-associated ATPase; generic GTP-binding and
  broad NTPase/ribosome-binding rows are narrowed or marked non-core where the
  UniProt/HAMAP record supports ATP hydrolysis and large-subunit binding more
  directly.
- All ten standard `just fetch-gene` runs succeeded for this split; no
  fallback UniProt/QuickGO reconstruction was needed.
- The `module:translation_rna_processing` umbrella is now first-pass complete:
  all nine splits are curated, Asta-backed, validated, and represented in
  modules or routed boundary views.

## Batch status: module:translation_rna_processing / aminoacyl_trna_charging_editing_quality_control

Batch files:

- `projects/P_PUTIDA/batches/module_translation_rna_processing_aminoacyl_trna_charging_editing_quality_control.tsv`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_aminoacyl_trna_charging_editing_quality_control.md`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_partition.tsv`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 11-gene `aminoacyl_trna_charging_editing_quality_control` split is
  first-pass complete: `PP_0201`, `PP_0782`, `PP_0784`, `ybaK`, `PP_1091`,
  `ycfH`, `aat`, `PP_4228`, `gluQ`, `dtd`, and `PP_5664`.
- 11/11 candidate review folders are present.
- 11/11 candidate Asta gene-level retrieval reports are present.
- 11/11 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/aminoacyl_trna_quality_control_boundary.yaml`.
- Validation complete for all eleven gene reviews and the module. The expected
  residual warning for genes with GOA rows is that available Asta files are not
  cited as biological support in annotation decisions, because they were used
  as fast retrieval provenance rather than direct evidence.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/aminoacyl_trna_quality_control_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/aminoacyl_trna_quality_control_boundary.yaml
```

Main curation conclusions from this split:

- `PP_0201` and `ybaK` are retained as YbaK-domain aminoacyl-tRNA
  deacylase/editing factors. `PP_0201` remains a candidate call from domain/IEA
  evidence, while `ybaK` has the stronger YbaK/EbsC family assignment.
- `ycfH` is treated as a TatD/YcfH-family candidate tRNA/aminoacyl-tRNA
  deacylase-like hydrolase. Generic TatD-family DNA nuclease and hydrolase rows
  were modified toward aminoacyl-tRNA deacylase activity rather than accepted as
  core DNA nuclease function.
- `dtd` is retained as D-aminoacyl-tRNA deacylase. The specific
  D-aminoacyl-tRNA and Gly-tRNA(Ala) deacylase rows are core, while tRNA
  binding, broad tRNA metabolism, and D-amino acid catabolism are non-core
  context.
- `aat` is retained as the cytoplasmic L/F-transferase in the bacterial N-end
  rule protein-degradation pathway.
- `gluQ` is retained as Glu-Q tRNA(Asp) synthetase in tRNA wobble-base
  modification. Broad aminoacyl-tRNA ligase/aminoacylation rows were narrowed
  or routed to tRNA modification rather than treated as ordinary tRNA(Glu)
  charging for translation.
- `PP_0782`, `PP_0784`, `PP_4228`, and `PP_5664` are GAD/T6SS Tdi1_C-domain
  proteins with protein-language-model glutamyl-tRNA amidotransferase names but
  no GOA/Rhea/HAMAP/GatCAB subunit support. They are kept as unresolved side
  nodes, not curated GatCAB-like enzymes.
- `PP_1091` is a 58 amino acid DUF8197/PA3496-like protein with a
  protein-language-model leucyl-tRNA synthetase name but no canonical LeuRS
  domain or GOA support. It is kept unresolved rather than forced into the
  aminoacyl-tRNA synthetase module.
- All eleven standard `just fetch-gene` runs succeeded for this split; no
  fallback UniProt/QuickGO reconstruction was needed.
- The `module:translation_rna_processing` umbrella is now first-pass complete:
  all nine splits are curated, Asta-backed, validated, and represented in
  modules or routed boundary views.

## Batch status: module:translation_rna_processing / ribonuclease_rna_decay_processing_helicases

Batch files:

- `projects/P_PUTIDA/batches/module_translation_rna_processing_ribonuclease_rna_decay_processing_helicases.tsv`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_ribonuclease_rna_decay_processing_helicases.md`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_partition.tsv`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 12-gene `ribonuclease_rna_decay_processing_helicases` split is
  first-pass complete: `rnpA`, `rng`, `rnt`, `PP_1840`, `PP_2084`, `rnz`,
  `PP_4462`, `srmB`, `rnd`, `PP_4720`, `dbpA`, and `rph`.
- 12/12 candidate review folders are present.
- 12/12 candidate Asta gene-level retrieval reports are present.
- 12/12 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/rna_decay_processing_boundary.yaml`.
- Validation complete for all twelve gene reviews and the module. Expected
  residual warnings are Asta-provenance warnings for genes with GOA rows, plus
  one synthesized-core warning for `rnt` because its core function records
  tRNA processing while GOA currently has broader RNA processing.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/rna_decay_processing_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/rna_decay_processing_boundary.yaml
```

Main curation conclusions from this split:

- `rnpA` is retained as the RNase P protein component contributing to tRNA
  5-prime leader removal in the RNase P complex. Electronic 3-prime tRNA
  processing carryover was modified toward RNase P activity/5-prime
  leader-removal context.
- `rnz`, `rnd`, `rnt`, and `rph` are retained as tRNA 3-prime processing or
  turnover RNases. `rnt` DNA-replication proofreading was removed as a likely
  family-transfer artifact.
- `rng` is retained as an RNase E/G-family RNA nuclease in rRNA/RNA processing
  context.
- `srmB` and `dbpA` are retained as cytosolic DEAD-box RNA helicase boundary
  factors; generic hydrolase rows were modified to RNA helicase activity.
- `PP_2084` is retained primarily as an HMG aldolase/oxaloacetate decarboxylase
  with RraA-like RNase-regulator side context. `PP_1840` and `PP_4462` remain
  unresolved RraB/RraA-like side nodes, and `PP_4720` remains a low-information
  YhbY/CRM-domain RNA-binding candidate.
- All twelve standard `just fetch-gene` runs succeeded or rechecked existing
  material; `rnz` already existed and its GOA cache differs from the current
  remote, but the review already contained all GOA annotations and was not
  force-overwritten.
- The `module:translation_rna_processing` umbrella is now first-pass complete:
  all nine splits are curated, Asta-backed, validated, and represented in
  modules or routed boundary views.

## Batch status: module:translation_rna_processing / rrna_modification_methyltransferase_pseudouridine

Batch files:

- `projects/P_PUTIDA/batches/module_translation_rna_processing_rrna_modification_methyltransferase_pseudouridine.tsv`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_rrna_modification_methyltransferase_pseudouridine.md`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_partition.tsv`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 29-gene `rrna_modification_methyltransferase_pseudouridine` split is
  first-pass complete: `rsmG`, `rsmB`, `rsmA`, `rluD`, `rsmC`, `rlmN`, `rlmF`,
  `PP_1191`, `rsmI`, `rsmH`, `rsuA`, `rsmJ`, `rlmAA`, `rlmD`, `rluC`, `rlmL`,
  `PP_2110`, `rlmM`, `PP_4306`, `rluB`, `rlmG`, `rlmE`, `rlmH`, `rlmB`,
  `rlmJ`, `rsmE`, `PP_5019`, `PP_5114`, and `rlmI`.
- 29/29 candidate review folders are present.
- 29/29 candidate Asta gene-level retrieval reports are present.
- 29/29 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/rrna_modification_ribosome_maturation_boundary.yaml`.
- Validation complete for all 29 gene reviews and the module. Expected residual
  warnings are Asta-provenance warnings for first-pass reviews where UniProt/GOA
  support, not Asta snippets, drove the annotation decisions.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/rrna_modification_ribosome_maturation_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/rrna_modification_ribosome_maturation_boundary.yaml
```

Main curation conclusions from this split:

- Site-specific 16S rRNA methyltransferases are retained for `rsmG`, `rsmB`,
  `rsmA`, `rsmC`, `rsmI`, `rsmH`, `rsmJ`, `rsmE`, `PP_5019`, and `PP_5114`,
  with broad RNA-binding or generic methyltransferase rows kept non-core or
  over-annotation-aware where a sharper term exists.
- Site-specific 23S rRNA methyltransferases are retained for `rlmN`, `rlmF`,
  `rlmAA`, `rlmD`, `rlmL`, `rlmM`, `rlmG`, `rlmE`, `rlmH`, `rlmB`, and
  `rlmJ`. `rlmN` is kept as a dual rRNA/tRNA radical-SAM methyltransferase.
- `rluD`, `PP_1191`, `rsuA`, `rluC`, `PP_2110`, and `rluB` are retained as
  rRNA pseudouridine synthases, using site-specific terms where GOA provides
  them and generic enzyme-directed rRNA pseudouridine synthesis where the target
  site is unresolved.
- `PP_4306` and `rlmI` remain cautious methyltransferase-domain side nodes
  because the first pass does not resolve a specific rRNA target site. No
  target-site claim was invented.
- Existing Falcon-backed curated reviews for `rsmG`, `rsmJ`, `rlmE`, and
  `rlmH` were preserved. This batch added Asta coverage and module placement
  around those prior reviews rather than overwriting their biological synthesis.
- All 29 standard `just fetch-gene` runs succeeded or rechecked existing
  material; no fallback UniProt/QuickGO reconstruction was needed.
- The `module:translation_rna_processing` umbrella is now first-pass complete:
  all nine splits are curated, Asta-backed, validated, and represented in
  modules or routed boundary views.

## Batch status: module:translation_rna_processing / ribosome_assembly_maturation_hibernation

Batch files:

- `projects/P_PUTIDA/batches/module_translation_rna_processing_ribosome_assembly_maturation_hibernation.tsv`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_ribosome_assembly_maturation_hibernation.md`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_partition.tsv`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 24-gene `ribosome_assembly_maturation_hibernation` split is first-pass
  complete: `yigZ`, `rimI`, `der`, `darP`, `hpf`, `rimO`, `era`, `rimM`,
  `prmB`, `PP_1910`, `PP_2956`, `ycaO`, `PP_3810`, `rbfA`, `rimP`, `ybeY`,
  `rsfS`, `prmA`, `PP_4885`, `PP_4996`, `typA`, `rmf`, `PP_5700`, and
  `PP_5726`.
- 24/24 candidate review folders are present.
- 24/24 candidate Asta gene-level retrieval reports are present.
- 24/24 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/bacterial_ribosome_maturation_regulation_boundary.yaml`.
- Validation complete for all 24 gene reviews and the module. Expected residual
  warnings are Asta-provenance warnings, synthesized-core warnings where GOA
  lacks a sharper UniProt/HAMAP-supported term, location-context warnings, and
  no-core warnings for deliberately unresolved zero-GOA side nodes.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/bacterial_ribosome_maturation_regulation_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/bacterial_ribosome_maturation_regulation_boundary.yaml
```

Main curation conclusions from this split:

- `der`, `era`, and `typA` are retained as ribosome-associated GTPase or
  GTPase-like maturation factors, while broad nucleotide-binding rows are
  non-core context.
- `rbfA`, `rimM`, `rimP`, `ybeY`, and `PP_4996` define the 30S/16S-rRNA
  maturation side of the module. `ybeY` metalloendopeptidase was modified toward
  RNA endonuclease activity, and `PP_4996` generic ester-hydrolase activity was
  modified toward nuclease activity.
- `darP` and `PP_1910` are retained as 50S/23S-rRNA maturation or accumulation
  factors, with `PP_1910` relying on UniProt/YceD-family support because GOA
  currently has cytosol only.
- `hpf`, `rmf`, `rsfS`, and `PP_5700` are separated as hibernation,
  translation-silencing, or RHF/RaiA-like interface context rather than
  structural ribosome components.
- `rimI`, `rimO`, `prmB`, `PP_2956`, `ycaO`, and `prmA` are separated as
  ribosomal-protein modification enzymes or cofactors. `rimO` tRNA modification
  was removed as wrong-substrate electronic transfer; `ycaO` has no GOA rows
  and remains an accessory candidate rather than a GO-level activity claim.
- `PP_3810`, `PP_4885`, and `PP_5726` remain low-information S3AE/S2p-like side
  nodes with no defensible first-pass GO-level activity.
- All 24 standard `just fetch-gene` runs succeeded; no fallback UniProt/QuickGO
  reconstruction was needed.
- The `module:translation_rna_processing` umbrella is now first-pass complete:
  all nine splits are curated, Asta-backed, validated, and represented in
  modules or routed boundary views.

## Batch status: module:translation_rna_processing / trna_modification_processing

Batch files:

- `projects/P_PUTIDA/batches/module_translation_rna_processing_trna_modification_processing.tsv`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_trna_modification_processing.md`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_partition.tsv`
- `projects/P_PUTIDA/batches/module_translation_rna_processing_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 30-gene `trna_modification_processing` split is first-pass complete:
  `mnmG`, `mnmE`, `tsaC`, `tsaD`, `cca`, `cmoM`, `selU`, `trmJ`, `tadA`,
  `cmoB`, `trmD`, `tsaB`, `tilS`, `truD`, `yfiP`, `ttcA`, `rluA`, `mnmC`,
  `trhO`, `dusC`, `truA`, `dusA`, `trmK`, `PP_4520`, `trmA`, `truB`,
  `dusB`, `miaA`, `tsaE`, and `trmL`.
- 30/30 candidate review folders are present.
- 30/30 candidate Asta gene-level retrieval reports are present.
- 30/30 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/trna_modification_processing_boundary.yaml`.
- Validation complete for all 30 gene reviews and the module. Expected residual
  warnings are the Asta-provenance warnings: Asta reports are present, but
  annotation decisions cite local GOA and UniProt evidence directly.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/trna_modification_processing_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/trna_modification_processing_boundary.yaml
```

Main curation conclusions from this split:

- `mnmG`, `mnmE`, `cmoM`, `cmoB`, `selU`, `mnmC`, and `trhO` are retained as
  wobble-uridine U34 side-chain modification factors. MnmC is treated as
  bifunctional methyltransferase/oxidoreductase; broad parent terms were
  narrowed where sharper GOA terms exist.
- `tsaC`, `tsaD`, `tsaB`, and `tsaE` are separated as the bacterial t6A37
  biosynthesis system, with TsaC and TsaD carrying the sharper synthase and
  transferase activities and TsaB/TsaE retained as accessory factors.
- `trmJ`, `trmD`, `trmK`, `trmA`, and `trmL` are retained as Trm-family tRNA
  methyltransferases. Broad methyltransferase or RNA-processing rows were
  marked non-core or modified toward site-specific tRNA methyltransferase
  terms where available.
- `truD`, `rluA`, `truA`, and `truB` are retained as tRNA pseudouridine
  synthases. `rluA` is deliberately dual-use, retaining both tRNA
  pseudouridine(32) and 23S rRNA pseudouridine(746) activity.
- `tadA`, `tilS`, `ttcA`, `yfiP`, `PP_4520`, and `miaA` cover adenosine
  deamination, lysidine formation, cytidine thiolation, aminocarboxypropylation,
  and adenosine-37 dimethylallylation side chemistry.
- `dusC`, `dusA`, and `dusB` are retained as Dus-family tRNA dihydrouridine
  synthases, with site-specific U16/U20/U20a terms used where GOA supplies them.
- The existing complete `cca` review was preserved. This batch only added Asta
  coverage, tRNA-processing module placement, and a short notes entry around
  the prior CCA/CCACCA-end processing synthesis.
- All 30 standard `just fetch-gene` runs succeeded or rechecked existing
  material; no fallback UniProt/QuickGO reconstruction was needed.
- The `module:translation_rna_processing` umbrella is now first-pass complete:
  all nine splits are curated, Asta-backed, validated, and represented in
  modules or routed boundary views.

## Batch status: module:regulation_signal_transduction / small_family_metabolic_transcriptional_regulators

Batch files:

- `projects/P_PUTIDA/batches/module_regulation_signal_transduction_small_family_metabolic_transcriptional_regulators.tsv`
- `projects/P_PUTIDA/batches/module_regulation_signal_transduction_small_family_metabolic_transcriptional_regulators.md`
- `projects/P_PUTIDA/batches/module_regulation_signal_transduction_partition.tsv`
- `projects/P_PUTIDA/batches/module_regulation_signal_transduction_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 387-gene `module:regulation_signal_transduction` umbrella has been
  partitioned into 10 curation-scale regulator-family buckets. It is not one
  satisfiable pathway.
- The first 21-gene `small_family_metabolic_transcriptional_regulators` split is
  first-pass complete: `PP_0384`, `PP_0663`, `glpR`, `PP_1307`, `rbsR`,
  `PP_2601`, `PP_2609`, `fnrB`, `fnrC`, `PP_3362`, `ptxS`, `PP_3415`,
  `PP_3532`, `PP_3592`, `PP_4308`, `bkdR`, `ybaO`, `PP_4776`, `PP_5188`,
  `PP_5350`, and `PP_5410`.
- 21/21 candidate review folders are present.
- 21/21 candidate Asta gene-level retrieval reports are present.
- 21/21 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/metabolic_transcriptional_regulator_boundary.yaml`.
- Validation complete for all 21 gene reviews and the module. Expected residual
  warnings are the Asta-provenance warnings: Asta reports are present, but
  annotation decisions cite local GOA and UniProt evidence directly.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/metabolic_transcriptional_regulator_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/metabolic_transcriptional_regulator_boundary.yaml
```

Main curation conclusions from this split:

- The AsnC/Lrp-family entries (`PP_0384`, `PP_0663`, `PP_1307`, `PP_3362`,
  `PP_3532`, `PP_4308`, `bkdR`, `ybaO`, `PP_4776`, and `PP_5188`) are retained
  as sequence-specific DNA-binding transcription regulators with cytosolic
  context where GOA supplies it. Amino-acid response is kept as non-core family
  context, not a resolved cue/regulon.
- The DeoR/LacI/RbsR/PtxS-family entries (`glpR`, `rbsR`, `ptxS`, `PP_3415`,
  and `PP_5410`) are retained as metabolic transcriptional regulators. The
  existing complete `ptxS` review was preserved; the new work only adds Asta and
  module bookkeeping around it.
- The IclR/RpiR entries (`PP_2601`, `PP_2609`, `PP_3592`, and `PP_5350`) retain
  DNA-binding transcription-factor activity and transcription-regulation
  context, while directional activation/repression, 3,4-dihydroxybenzoate, and
  carbohydrate-process rows are kept non-core until regulons are verified.
- `fnrB` and `fnrC` are retained as Crp/Fnr-family redox-responsive
  transcriptional regulator candidates, without assigning a specific oxygen or
  redox regulon in this pass.
- Broad `DNA-templated transcription` rows were consistently treated as
  over-annotated parent-process carryover for transcription regulators; generic
  `DNA binding` was demoted where sharper transcription-regulator or
  sequence-specific DNA-binding terms exist.
- Remaining queued regulation/signal-transduction splits are the large LysR,
  AraC/XylS, GntR, two-component, XRE/phage, MerR/ArsR/MarR, and
  low-information/named regulator buckets.

## Batch status: module:regulation_signal_transduction / sigma_anti_sigma_and_sigma_factors

Batch files:

- `projects/P_PUTIDA/batches/module_regulation_signal_transduction_sigma_anti_sigma_and_sigma_factors.tsv`
- `projects/P_PUTIDA/batches/module_regulation_signal_transduction_sigma_anti_sigma_and_sigma_factors.md`
- `projects/P_PUTIDA/batches/module_regulation_signal_transduction_partition.tsv`
- `projects/P_PUTIDA/batches/module_regulation_signal_transduction_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 16-gene `sigma_anti_sigma_and_sigma_factors` split is first-pass complete:
  `PP_0865`, `PP_0994`, `PP_1008`, `rpoE`, `mucA`, `mucB`, `rpoS`,
  `PP_2088`, `PP_2166`, `PP_2888`, `PP_3005`, `PP_3006`, `PP_4208`, `pvdS`,
  `PP_4608`, and `rpoH`.
- 16/16 candidate review folders are present.
- 16/16 candidate Asta gene-level retrieval reports are present.
- 16/16 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/sigma_anti_sigma_regulation_boundary.yaml`.
- Existing curated `rpoS`, `pvdS`, and `rpoH` YAML decisions were preserved;
  this pass only added Asta retrieval and notes around those reviews. `pvdS`
  retains its pre-existing non-blocking `curator_inference` reference warning.
- Validation complete for all 16 gene reviews and the module.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/sigma_anti_sigma_regulation_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/sigma_anti_sigma_regulation_boundary.yaml
```

Main curation conclusions from this split:

- Generic ECF sigma factors (`PP_0865`, `PP_0994`, `PP_1008`, `rpoE`,
  `PP_2088`, `PP_2888`, `PP_3006`, `PP_4208`, and `PP_4608`) retain
  `GO:0016987` sigma factor activity, `GO:0006352` DNA-templated transcription
  initiation, and `GO:2000142` regulation of DNA-templated transcription
  initiation as the core first-pass representation. Broad `DNA binding`,
  `DNA-binding transcription factor activity`, and generic transcription
  regulation rows are demoted or modified to sharper sigma-factor terms.
- `mucA` is curated as a membrane anti-sigma factor for AlgU/RpoE-family
  transcription control; `mucB` is curated as a periplasmic MucB/RseB
  antisigma-factor-binding partner. The polysaccharide-process row for `mucB`
  is retained as non-core pathway context pending direct regulon evidence.
- `PP_2166` is curated as a STAS-domain anti-anti-sigma factor with positive
  transcription-regulation output.
- `PP_3005` is curated as a membrane RskA-like sigma-K anti-sigma factor; its
  TreeGrafter `GO:0006417` regulation of translation row is removed because the
  domain/product context supports transcriptional sigma antagonism, not
  translation regulation.
- `rpoS`, `pvdS`, and `rpoH` remain governed by their existing deeper curated
  reviews and are placed into the broader sigma/anti-sigma regulation boundary
  without reworking their biological decisions.

## Batch status: module:regulation_signal_transduction / sigma54_enhancer_binding_regulators

Batch files:

- `projects/P_PUTIDA/batches/module_regulation_signal_transduction_sigma54_enhancer_binding_regulators.tsv`
- `projects/P_PUTIDA/batches/module_regulation_signal_transduction_sigma54_enhancer_binding_regulators.md`
- `projects/P_PUTIDA/batches/module_regulation_signal_transduction_partition.tsv`
- `projects/P_PUTIDA/batches/module_regulation_signal_transduction_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 16-gene `sigma54_enhancer_binding_regulators` split is first-pass
  complete: `PP_0051`, `PP_0546`, `PP_0767`, `PP_2259`, `PP_2587`, `PP_2771`,
  `PP_3075`, `PP_3467`, `PP_3503`, `PP_3717`, `PP_3847`, `PP_3905`,
  `PP_4136`, `PP_4647`, `PP_5166`, and `PP_5473`.
- 16/16 candidate review folders are present.
- 16/16 candidate Asta gene-level retrieval reports are present.
- 16/16 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/sigma54_enhancer_binding_regulator_boundary.yaml`.
- Validation complete for all 16 gene reviews and the module. `PP_5473`
  intentionally retains a non-blocking no-core warning because the current
  record is product-name-only, has no GOA rows, and lacks conserved LuxR or
  sigma-54 activator domain support.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/sigma54_enhancer_binding_regulator_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/sigma54_enhancer_binding_regulator_boundary.yaml
```

Main curation conclusions from this split:

- AAA+/sigma-54 enhancer-binding candidates (`PP_0051`, `PP_0546`, `PP_2259`,
  `PP_2771`, `PP_3075`, `PP_3467`, `PP_3503`, and `PP_5166`) are curated as
  DNA-binding transcription activator candidates using `GO:0001216`.
  ATP-binding rows are retained as non-core cofactor context for the sigma-54
  activator mechanism, and exact regulons/signals remain unresolved.
- LuxR/GerE-family entries (`PP_0767`, `PP_2587`, `PP_3717`, `PP_3847`,
  `PP_3905`, `PP_4136`, and `PP_4647`) are curated as DNA-binding
  transcription regulator candidates using `GO:0003700`; ligand, direction, and
  target regulon are not inferred from family name alone.
- `PP_5473` is kept as an unresolved product-name-only LuxR-family membrane
  protein with no asserted core GO function.

## Batch status: module:regulation_signal_transduction / tetr_acrr_transcriptional_regulators

Batch files:

- `projects/P_PUTIDA/batches/module_regulation_signal_transduction_tetr_acrr_transcriptional_regulators.tsv`
- `projects/P_PUTIDA/batches/module_regulation_signal_transduction_tetr_acrr_transcriptional_regulators.md`
- `projects/P_PUTIDA/batches/module_regulation_signal_transduction_partition.tsv`
- `projects/P_PUTIDA/batches/module_regulation_signal_transduction_partition.md`

Status as of 2026-07-10 PDT / 2026-07-10 UTC:

- The 25-gene `tetr_acrr_transcriptional_regulators` split is first-pass
  complete: `PP_0242`, `PP_0594`, `ttgR`, `PP_1497`, `PP_1515`, `PP_1968`,
  `PP_1978`, `PP_2144`, `PP_2475`, `PP_2597`, `PP_2806`, `PP_2824`,
  `PP_2880`, `PP_2951`, `PP_3300`, `PP_3527`, `PP_3731`, `PP_3756`,
  `PP_3960`, `rutR`, `PP_4295`, `PP_4754`, `PP_4859`, `PP_5006`, and
  `PP_5119`.
- 25/25 candidate review folders are present.
- 25/25 candidate Asta gene-level retrieval reports are present.
- 25/25 review YAMLs are curated with no remaining `PENDING` actions.
- New boundary module created and validated:
  `modules/tetr_acrr_transcriptional_regulator_boundary.yaml`.
- Existing curated `ttgR` YAML decisions were preserved; the new work adds Asta
  retrieval and places `ttgR` in the TetR/AcrR boundary as the named local
  repressor of the `ttgABC` efflux locus.
- Validation complete for all 25 gene reviews and the module. Expected residual
  warnings are seven sparse-GOA records (`PP_1978`, `PP_2475`, `PP_2880`,
  `PP_2951`, `rutR`, `PP_4754`, and `PP_4859`) where the curated core function
  uses the sharper `GO:0003700` transcription-factor term even though GOA only
  supplies `DNA binding`, plus the intentional no-core warning for `PP_2597`.
- Module validation complete with:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/tetr_acrr_transcriptional_regulator_boundary.yaml
uv run --no-dev python -m ai_gene_review.validation.module_validator modules/tetr_acrr_transcriptional_regulator_boundary.yaml
```

Main curation conclusions from this split:

- Most TetR/AcrR-family entries are curated as DNA-binding transcription
  regulator candidates. Direct regulons, ligands, substrates, and regulatory
  direction are not inferred from family name alone.
- `ttgR` remains governed by its existing curated review as a TetR-family
  repressor of the adjacent `ttgABC` RND efflux locus.
- `PP_2144` is treated as a PsrA-like TetR-family regulator. Experimental IPI
  GOA rows to PMID:11914368 for promoter binding and activator/repressor
  molecular functions are retained, while broader regulon scope is not inferred
  from the metadata-only publication cache.
- Generic directional `negative regulation` or `positive regulation` rows from
  family/electronic evidence are retained as non-core unless supported by the
  PsrA-like curator annotations.
- `PP_2597` remains unresolved with no asserted core GO function because it has
  no GOA rows, membrane/transmembrane prediction context, and lacks the canonical
  HTH_TetR InterPro row used by the other batch members.

## First batch proposal

Start with central carbon plus aromatic catabolism, because these are core
KT2440 biology and the existing project already has reviewed genes in the
neighborhood (`aceA`, `acnB`, `BenR`, `benA/B/C/D`, `catA/B/C`, `pcaG`, `fcs`,
`hpd`, AAA biosynthesis genes). This gives an immediate test of the metadata
clustering, module satisfiability, and review-escalation workflow before scaling
to the rest of the genome.
