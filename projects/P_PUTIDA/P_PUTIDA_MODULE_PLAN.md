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

3. Current gene-level research uses OpenScientist while the Edison-backed
   Falcon route is unavailable. Use three iterations for batch throughput but
   retain a two-hour provider allowance:

```bash
just deep-research-openscientist PSEPK <gene> --timeout 8100 \
  --extra-args --param timeout=7200 --param max_iterations=3
```

4. Use OpenScientist for the generic reusable-module synthesis as well:

```bash
just module-deep-research-openscientist <module> --timeout 8100 \
  --extra-args --param timeout=7200 --param max_iterations=3
```

5. For species-aware module/pathway research, use the module + pathway + taxon
   wrapper. This keeps generic module research separate from PSEPK-specific
   satisfiability work and injects local candidate genes from the pathway
   partition table when available:

```bash
just module-pathway-deep-research openscientist "central carbon metabolism" \
  ppu00020 PSEPK --project P_PUTIDA --timeout 8100 \
  --extra-args --param timeout=7200 --param max_iterations=3
```

The report is written under the project support folder by default, e.g.
`projects/P_PUTIDA/deep-research/PSEPK__central-carbon-metabolism__ppu00020-deep-research-openscientist.md`.

6. Asta remains a lightweight gene-level fallback, and Falcon remains the
   preferred module-level provider when its Edison route is available again.
7. PaperBLAST remains an optional protein-specific lookup:

```bash
uv run python scripts/fetch_paperblast.py <uniprot_accession>
```

8. Use `perplexity-lite` only as a secondary fallback when Asta is unavailable
   or comparison across providers is useful.
9. Escalate to OpenAI/perplexity/full manual literature only when the first-pass
   provider output leaves a curation-changing question unresolved.

OpenScientist is a long-running research provider, not a short smoke test.
Successful jobs commonly take more than 20 minutes and difficult jobs can use
most or all of the two-hour provider allowance. Do not apply a 180-second
timeout or treat a quiet wrapper as failure. If a five-iteration run exhausts
the allowance, rerun with `max_iterations=3` and the same full timeout.

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

Status as of 2026-07-06:

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
- PR [#1874](https://github.com/ai4curation/ai-gene-review/pull/1874)
  merged.

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

## Previous batch: ppu00010 / entner_doudoroff_and_gluconeogenesis

Batch files:

- `projects/P_PUTIDA/batches/ppu00010_entner_doudoroff_and_gluconeogenesis.tsv`
- `projects/P_PUTIDA/batches/ppu00010_entner_doudoroff_and_gluconeogenesis.md`

Status as of 2026-07-06:

- 38 KEGG `ppu00010` membership candidates extracted for first-pass review.
- 38/38 review folders present.
- 38/38 Asta gene-level retrieval reports present.
- 38/38 review YAMLs curated with no remaining `PENDING` actions.
- Falcon generic module research complete:
  `modules/entner_doudoroff_and_gluconeogenesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__entner_doudoroff_and_gluconeogenesis__ppu00010-deep-research-falcon.md`.
- Module YAML seeded:
  `modules/entner_doudoroff_and_gluconeogenesis.yaml`.

Main curation conclusions from the current batch:

- KT2440 should be treated as ED-centered rather than complete forward EMP
  glycolysis; the module combines the ED branch, shared lower EMP trunk, and
  gluconeogenic bypasses.
- KEGG `ppu00010` is an incomplete satisfiability boundary for KT2440 because
  `edd`, `eda`, `zwf`, and `pgl` are required ED-branch genes but are carried
  through the neighboring `ppu00030`-style boundary.
- The ppu00010 membership table includes peripheral EC/pathway spillover from
  pyruvate dehydrogenase, acetyl-CoA synthetase, aldehyde/alcohol
  dehydrogenases, phosphosugar mutases/epimerases, and periplasmic glucose
  oxidation. These reviews are useful first-pass curation, but not every member
  is a core ED/gluconeogenesis module component.

## Current batch: ppu00622 / benzoate_upper_pathway

Batch files:

- `projects/P_PUTIDA/batches/ppu00622_benzoate_upper_pathway.tsv`
- `projects/P_PUTIDA/batches/ppu00622_benzoate_upper_pathway.md`

Status as of 2026-07-13:

- 6 KEGG `ppu00622` membership candidates extracted for first-pass review.
- 4/6 candidates selected as core upper benzoate genes:
  `benA`, `benB`, `benC`, and `benD`.
- 2/6 candidates (`PP_1791`, `PP_2504`) classified as lower meta-cleavage
  spillover from overlapping KEGG maps and excluded from this module.
- 4/4 selected review folders present and already curated.
- 4/4 selected genes now have OpenScientist gene-level retrieval reports.
- OpenScientist generic module research complete:
  `modules/benzoate_upper_pathway-deep-research-openscientist.md`.
- OpenScientist PSEPK module+pathway research complete:
  `projects/P_PUTIDA/deep-research/PSEPK__benzoate_upper_pathway__ppu00622-deep-research-openscientist.md`.
- Module YAML seeded:
  `modules/benzoate_upper_pathway.yaml`.

Main curation conclusions from this batch:

- The useful module boundary is the benzoate-to-catechol upper pathway:
  BenABC dioxygenation followed by BenD cis-diol dehydrogenation.
- KT2440 satisfies the module with the contiguous single-copy
  `benA`/`benB`/`benC`/`benD` cluster.
- The KEGG `ppu00622` "Xylene degradation" label is misleading for plasmid-free
  KT2440; the biochemical anchor is closer to KEGG M00551 and ppu00362
  benzoate degradation.
- Catechol ortho-cleavage, catechol meta-cleavage, and CoA-dependent benzoate
  routes are separate modules, not parts of this upper-pathway module.

## First batch proposal

Start with central carbon plus aromatic catabolism, because these are core
KT2440 biology and the existing project already has reviewed genes in the
neighborhood (`aceA`, `acnB`, `BenR`, `benA/B/C/D`, `catA/B/C`, `pcaG`, `fcs`,
`hpd`, AAA biosynthesis genes). This gives an immediate test of the metadata
clustering, module satisfiability, and review-escalation workflow before scaling
to the rest of the genome.
