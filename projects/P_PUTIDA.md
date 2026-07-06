---
title: "P. putida Gene Annotation Review Project"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [PSEPK]
---

# P. putida Gene Annotation Review Project

## Overview

Systematic AI-assisted review of GO annotations for *Pseudomonas putida*, focusing primarily on the well-characterized KT2440 strain (UniProt: PSEPK). *P. putida* is a metabolically versatile soil bacterium of significant interest for bioremediation, industrial biotechnology, and plant growth promotion. Its annotations are predominantly from automated pipelines (InterPro2GO, UniProtKB-KW, TreeGrafter), with very few experimental annotations (~50 from PMIDs), making careful review essential.

## Organism Details

- **Species:** *Pseudomonas putida*
- **Primary strain:** KT2440 (UniProt taxon code: PSEPK)
- **Other strains:** PSEPU (general *P. putida*)
- **Genome:** ~6.2 Mb, ~5,350 protein-coding genes
- **Key biology:** Aromatic compound degradation, solvent tolerance, plant root colonization, polyhydroxyalkanoate (PHA) biosynthesis, rare earth element utilization

## Genome-wide expansion

The next phase expands the project from selected genes to a pathway-by-pathway
review of the KT2440 reference proteome. The working pattern is manual pathway
hole filling: start with a curated module, ask which steps are satisfiable in
PSEPK from lightweight UniProt metadata, then review only the genes needed to
resolve missing, ambiguous, over-propagated, or biologically important steps.

The detailed workplan is in
[P_PUTIDA/P_PUTIDA_MODULE_PLAN.md](P_PUTIDA/P_PUTIDA_MODULE_PLAN.md). It covers
the module order, triage rules, module-editing expectations, and the first-pass
metadata snapshot. This phase deliberately separates metadata discovery from
full gene-review seeding: the first pass uses UniProt REST TSV metadata only,
not full UniProt flat files, GOA downloads, PMID caches, or review YAML stubs.

Lightweight data products:

- `projects/P_PUTIDA/fetch_uniprot_metadata.py` downloads basic UniProt metadata
  for proteome `UP000000556`.
- `projects/P_PUTIDA/data/psepk_uniprot_metadata.tsv` is the current metadata
  snapshot for triage and module clustering.
- `projects/P_PUTIDA/data/psepk_uniprot_metadata.manifest.txt` records the
  query, fields, source URL, and retrieval timestamp.
- `projects/P_PUTIDA/build_gene_list.py` derives a curator-facing gene list from
  the metadata snapshot.
- `projects/P_PUTIDA/data/psepk_gene_list.tsv` is the current whole-proteome
  gene list for module bucketing and fetch planning.
- `projects/P_PUTIDA/partition_pathways.py` joins the gene list to KEGG `ppu`
  pathway mappings and assigns each gene to one primary pathway/module/unknown
  bucket.
- `projects/P_PUTIDA/data/psepk_pathway_partition.tsv` is the current primary
  partition, one row per gene.
- `projects/P_PUTIDA/data/psepk_pathway_membership.tsv` preserves overlapping
  KEGG and UniPathway memberships.
- `projects/P_PUTIDA/data/psepk_pathway_buckets.tsv` summarizes the current
  pathway/module buckets.
- `projects/P_PUTIDA/data/psepk_unknown_bucket.tsv` contains genes with unknown
  function or minimal pathway signal.
- `projects/P_PUTIDA/data/psepk_orphan_bucket.tsv` contains EC/domain-family
  orphans that have some annotation signal but no current pathway bucket.
- `projects/P_PUTIDA/build_pathway_worklist.py` builds the PR-oriented pathway
  queue from the bucket table.
- `projects/P_PUTIDA/data/psepk_pathway_worklist.tsv` tracks module mapping,
  Falcon research status, gene review coverage, Asta coverage, and PR status
  per pathway/module bucket.
- `projects/P_PUTIDA/extract_pathway_batch.py` extracts a per-pathway gene
  checklist from KEGG/UniPathway membership.
- `projects/P_PUTIDA/batches/ppu00400_tryptophan_biosynthesis.md` is the first
  pilot pathway checklist.

For gene-level first-pass research, use Asta as the default provider:

```bash
just deep-research-asta PSEPK <gene>
```

For module-level research, use Falcon by default:

```bash
just module-deep-research-falcon <module>
```

For PSEPK-specific pathway/module satisfiability research, use the taxon-aware
wrapper so the prompt includes the species constraint and local candidate genes
from the pathway partition:

```bash
just module-pathway-deep-research-falcon "<module or module title>" <pathway-or-bucket> PSEPK
```

PaperBLAST can still be used opportunistically for protein-specific literature
lookup, but it is not the main workflow because the current wrapper is
Cloudflare-sensitive in this environment. Use `perplexity-lite` only as a
secondary fallback when Asta is unavailable or provider comparison is useful.

## Completed Reviews

### PSEPK (P. putida KT2440) — 18 genes reviewed

| Gene | Annotations | Function | Notes | PR |
|------|-------------|----------|-------|----|
| **BenR** | 8 | Transcriptional regulator, benzoate catabolism | AraC/XylS family | — |
| **PP_0635** | 9 | Uncharacterized protein | DUF domain analysis | — |
| **ada** | 16 | Methyltransferase, DNA repair | Adaptive response to alkylation | — |
| **ampC** | 5 | Beta-lactamase | Antibiotic resistance | — |
| **ftsY** | 11 | Signal recognition particle receptor | Sec-dependent protein targeting | — |
| **hglS** | 2 | Hydroxyglutarate synthase | Rare enzymatic function | — |
| **mrcA** | 16 | Penicillin-binding protein 1a | Peptidoglycan biosynthesis | — |
| **pedH** | 14 | PQQ-dependent alcohol dehydrogenase | REE/lanthanide utilization | — |
| **quiC1_qsuB** | 8 | Quinate/shikimate dehydrogenase | Aromatic compound catabolism | — |
| **rpoS** | — | Stationary phase sigma factor | GO:0016987 core; added starvation/biofilm terms; DRAFT | [#159](https://github.com/ai4curation/ai-gene-review/pull/159) |
| **fleQ** | — | Flagellar/biofilm master regulator | Sigma-54 associated; added flagellum assembly/biofilm terms | [#162](https://github.com/ai4curation/ai-gene-review/pull/162) |
| **pvdA** | — | L-ornithine N5-monooxygenase | Pyoverdine biosynthesis; COMPLETE | [#163](https://github.com/ai4curation/ai-gene-review/pull/163) |
| **algD** | — | GDP-mannose 6-dehydrogenase | Alginate biosynthesis | [#157](https://github.com/ai4curation/ai-gene-review/pull/157) |
| **gacA** | — | GacS/GacA response regulator | Phosphorelay; biofilm/T6SS regulation | [#155](https://github.com/ai4curation/ai-gene-review/pull/155) |
| **pcaG** | — | Protocatechuate 3,4-dioxygenase α subunit | Iron-binding terms corrected (β subunit) | [#160](https://github.com/ai4curation/ai-gene-review/pull/160) |
| **phaC** | — | PHA synthase (phaC-II, Q88D23) | Corrected to PHA biosynthetic process | [#161](https://github.com/ai4curation/ai-gene-review/pull/161) |
| **cbrB** | — | CbrA/CbrB response regulator | Carbon catabolite repression; COMPLETE | [#158](https://github.com/ai4curation/ai-gene-review/pull/158) |
| **xylR** | — | TOL plasmid regulator (P06519) | Not native KT2440; organism mismatch noted | [#156](https://github.com/ai4curation/ai-gene-review/pull/156) |

### PSEPU (general P. putida) — 1 gene

| Gene | Annotations | Function |
|------|-------------|----------|
| **Q88CC1** | reviewed | Uncharacterized |

## Batch 2 — Selected for Review (50 new genes)

Fifty additional well-characterized KT2440 (taxon 160488) genes selected to broaden
functional coverage beyond the initial aromatic-catabolism/biotechnology focus, into
central carbon metabolism, stress response, DNA repair, motility, and membrane transport.
All were seeded via `fetch-gene` (UniProt + GOA). None overlap with previously present
gene folders.

**Status: reviews complete.** Each gene has a Falcon (Edison Scientific) deep-research
report (`*-deep-research-falcon.md`) and a fully reviewed `*-ai-review.yaml` — all GOA
annotations adjudicated (no `PENDING`), with descriptions, `core_functions`, and
references. The review pass corrected a number of mis-annotations and citation errors
surfaced in the raw reports (e.g. wrong PMIDs in exbB/fur/relA/pilA/hpd; cofactor terms
in fur (Zn→Fe(II)) and icd (NADP-specific); TreeGrafter/InterPro2GO over-propagations in
mdh, sdhA, groES, hfq, pvdQ; sigma-factor GO convention for rpoD/rpoH).

### Stress response, chaperones & global regulation (12)

| Gene | UniProt | Function |
|------|---------|----------|
| **dnaK** | Q88DU2 | Hsp70 chaperone (protein folding) |
| **groEL** | Q88N55 | GroEL chaperonin |
| **groES** | Q88N56 | GroES co-chaperonin |
| **grpE** | Q88DU1 | DnaK nucleotide-exchange factor |
| **htpG** | Q88FB9 | Hsp90 chaperone |
| **rpoH** | Q7CCA6 | Heat-shock sigma factor (σ32) |
| **rpoD** | Q88QU7 | Primary/housekeeping sigma factor (σ70) |
| **fur** | Q88DT9 | Ferric uptake regulator |
| **oxyR** | Q88C74 | Peroxide-responsive transcription regulator |
| **relA** | Q88MB8 | (p)ppGpp synthetase (stringent response) |
| **hfq** | Q88DD3 | RNA chaperone / sRNA-mediated regulation |
| **ppk** | Q88CG4 | Polyphosphate kinase |

### DNA repair & recombination (7)

| Gene | UniProt | Function |
|------|---------|----------|
| **recA** | Q88ME4 | Recombinase / SOS response |
| **recB** | Q88DZ5 | Exonuclease V β subunit |
| **ruvB** | Q88NJ0 | Holliday junction branch-migration helicase |
| **uvrB** | Q88LF9 | Excinuclease ABC subunit B (NER) |
| **uvrC** | Q88FJ7 | Excinuclease ABC subunit C (NER) |
| **mutL** | Q88DD1 | DNA mismatch repair (MutL) |
| **mutS** | Q88ME7 | DNA mismatch repair (MutS) |

### Central carbon metabolism — TCA cycle (8)

| Gene | UniProt | Function |
|------|---------|----------|
| **gltA** | Q88FA4 | Citrate synthase |
| **acnB** | Q88KF1 | Aconitase B |
| **icd** | Q88FS2 | Isocitrate dehydrogenase |
| **sucA** | Q88FA9 | 2-oxoglutarate dehydrogenase E1 |
| **sucC** | Q88FB2 | Succinyl-CoA synthetase β |
| **sdhA** | Q88FA7 | Succinate dehydrogenase flavoprotein |
| **fumC** | Q88M20 | Fumarase C |
| **mdh** | Q88Q44 | Malate dehydrogenase |

### Glycolysis / ED / anaplerotic & overflow metabolism (9)

| Gene | UniProt | Function |
|------|---------|----------|
| **gapA** | Q88P44 | Glyceraldehyde-3-phosphate dehydrogenase |
| **pgk** | Q88D64 | Phosphoglycerate kinase |
| **eno** | Q88MF9 | Enolase |
| **tpiA** | Q88DV4 | Triosephosphate isomerase |
| **pykA** | Q88N54 | Pyruvate kinase |
| **ppc** | Q88MR4 | PEP carboxylase (anaplerotic) |
| **pgl** | Q88P30 | 6-phosphogluconolactonase (ED/PPP) |
| **aceA** | Q88FI0 | Isocitrate lyase (glyoxylate shunt) |
| **pta** | Q88PS4 | Phosphate acetyltransferase (acetate overflow) |

### Chemotaxis & motility (4)

| Gene | UniProt | Function |
|------|---------|----------|
| **cheY** | Q88EW2 | Chemotaxis response regulator |
| **cheZ** | Q88EW3 | CheY-P phosphatase |
| **fliG** | Q88ET5 | Flagellar motor switch (C-ring) |
| **pilA** | Q88Q62 | Type IV pilin |

### Membrane transport, iron & nitrogen acquisition (8)

| Gene | UniProt | Function |
|------|---------|----------|
| **oprD** | Q88NK1 | Outer-membrane porin D |
| **oprE** | Q88R99 | Outer-membrane porin E (anaerobically induced) |
| **tonB** | Q88C75 | TonB (energization of OM transport) |
| **exbB** | Q88C77 | ExbB (TonB system) |
| **amtB** | Q88CE8 | Ammonium transporter |
| **glnK** | Q88CE7 | PII nitrogen-regulatory protein |
| **pvdQ** | Q88IU8 | Pyoverdine maturation acylase |
| **fpvA** | Q88F81 | Ferripyoverdine TonB-dependent receptor |

### Aromatic / aromatic-amino-acid catabolism (2)

| Gene | UniProt | Function |
|------|---------|----------|
| **hpd** | Q88HC7 | 4-hydroxyphenylpyruvate dioxygenase |
| **fcs** | Q88HK0 | Feruloyl-CoA synthetase (ferulate catabolism) |

## Batch 3 — Aromatic Amino Acid (AAA) Biosynthesis Pathway (16 genes)

The shikimate → chorismate → Trp/Phe/Tyr biosynthetic pathway in KT2440 (taxon
160488). Complements the existing aromatic *catabolism* coverage (ben/cat/pca) with the
*anabolic* route to aromatic amino acids. Seeded via `fetch-gene`; Falcon (Edison)
deep-research reports generated per gene. **Status: reviews complete** — all
annotations adjudicated, descriptions/core_functions/references populated (e.g. trpC and
aroQ over-propagation fixes; aroA bifunctional EPSPS/TyrA module captured). Name variants not resolving as primary UniProt
symbols in KT2440 are covered by a resolved paralog (aroD→aroQ, aroF/aroG→aroH, aroL→aroK)
or are differently named / fused in *Pseudomonas* (trpG, pheC, tyrA).

### Shikimate trunk (common pathway, 7)

| Gene | UniProt | Function |
|------|---------|----------|
| **aroH** | Q88LR3 | DAHP synthase (3-deoxy-D-arabino-heptulosonate-7-P synthase) |
| **aroB** | Q88CV2 | 3-dehydroquinate synthase |
| **aroQ** | Q88IJ6 | 3-dehydroquinate dehydratase (type II) |
| **aroE** | Q88IJ7 | Shikimate dehydrogenase |
| **aroK** | Q88CV1 | Shikimate kinase |
| **aroA** | Q88M05 | EPSP synthase (3-phosphoshikimate 1-carboxyvinyltransferase) |
| **aroC** | Q88LU7 | Chorismate synthase |

### Tryptophan branch (6)

| Gene | UniProt | Function |
|------|---------|----------|
| **trpE** | Q88QS1 | Anthranilate synthase component I |
| **trpD** | Q88QR7 | Anthranilate phosphoribosyltransferase |
| **trpC** | Q88QR6 | Indole-3-glycerol-phosphate synthase |
| **trpF** | Q88LE0 | N-(5'-phosphoribosyl)anthranilate isomerase |
| **trpA** | Q88RP7 | Tryptophan synthase α |
| **trpB** | Q88RP6 | Tryptophan synthase β |

### Phe/Tyr branch & aromatic aminotransferases (3)

| Gene | UniProt | Function |
|------|---------|----------|
| **pheA** | Q88M06 | Chorismate mutase / prephenate dehydratase (P-protein) |
| **tyrB** | Q88LG1 | Aromatic-amino-acid aminotransferase |
| **hisC** | Q88P86 | Histidinol-phosphate / aromatic aminotransferase |

## Priority Genes for Future Review

### Aromatic Catabolism (core P. putida biology)
- **benABCD** — Benzoate dioxygenase complex
- **catABC** — Catechol branch of β-ketoadipate pathway  
- **pcaGHBDCIJF** — Protocatechuate branch
- **nahABCDEF** — Naphthalene degradation (if present in KT2440 derivatives)
- **xylXYZ** — Toluene/xylene degradation (TOL plasmid genes)

### Central Metabolism & Biotechnology
- **phaABCZ** — Polyhydroxyalkanoate biosynthesis
- **glk**, **zwf**, **edd**, **eda** — Glucose catabolism (ED pathway, no EMP)
- **gcd** — Glucose dehydrogenase (periplasmic oxidation)
- **PP_1084** (oleC), **PP_1083** (oleD) — Olefin biosynthesis

### Rare Earth Element Biology
- **pedE** — Ca²⁺-dependent ethanol dehydrogenase (counterpart to pedH)
- **lanM** — Lanmodulin (lanthanide-binding protein)
- **lutH/lutABCDEF** — Lanthanide uptake and transport

### Solvent Tolerance
- **ttgABC**, **ttgDEF**, **ttgGHI** — Toluene efflux pumps (RND family)
- **srpABC** — Solvent resistance regulon

### Plant Interactions
- **pvdABCDES** — Pyoverdine siderophore biosynthesis
- **iaaM/iaaH** — Indole-3-acetic acid biosynthesis (auxin)
- **algABCDEFG** — Alginate biosynthesis

### Stress Response & Regulation
- **rpoS** — Stationary phase sigma factor
- **gacA/gacS** — Global regulatory two-component system
- **fleQ** — Flagellar/biofilm master regulator
- **cbrA/cbrB** — Carbon-nitrogen balance regulation

## Related Projects

- [SPKW-PSEPK](SPKW/SPKW-PSEPK.md) — Analysis of UniProtKB-KW annotation patterns in P. putida
- [REE](REE.md) — Rare earth element biology (pedH is a key gene)
- [BIOSENSORS](BIOSENSORS.md) — Biosensor applications (BenR is relevant)

## Notes

- P. putida KT2440 uses the Entner-Doudoroff pathway exclusively for glucose catabolism (no Embden-Meyerhof-Parnas pathway). This is important for annotation review — glycolysis terms may need careful handling.
- Many genes are annotated by homology to *P. aeruginosa* (PSEAE), but functional divergence is common — P. putida is non-pathogenic while P. aeruginosa is an opportunistic pathogen. Virulence-associated annotations transferred by homology should be scrutinized.
- The REE/lanthanide biology is relatively recent science (post-2011). Annotations for pedH and related genes may be incomplete or missing entirely.

---

# STATUS

## Genome-wide pathway/module curation

- [x] Re-scope P_PUTIDA from selected-gene project to genome-wide pathway/module curation umbrella.
- [x] Confirm working species/proteome: PSEPK / *P. putida* KT2440 / UniProt proteome `UP000000556`.
- [x] Confirm research provider policy: Asta for gene-level first-pass research; Falcon for module-level research; PaperBLAST optional; `perplexity-lite` secondary fallback.
- [x] Create module-first workplan in `projects/P_PUTIDA/P_PUTIDA_MODULE_PLAN.md`.
- [x] Refresh lightweight UniProt metadata snapshot before module clustering.
- [x] Build whole-proteome gene list from UniProt metadata.
- [x] Cluster all PSEPK proteins into first-pass module buckets from EC, KEGG, BioCyc, UniPathway, GO, InterPro/Pfam/PANTHER, keywords, and protein names.
- [x] Add species-aware module/pathway deep-research wrapper for module satisfiability work.
- [x] Select first pilot module/pathway batch: KEGG `ppu00400` with `tryptophan_biosynthesis` as the seeded neutral module.
- [x] Complete Falcon module-level research for `tryptophan_biosynthesis`.
- [x] Complete Falcon module + pathway + PSEPK research for `ppu00400`.
- [x] Fetch, run Asta, curate, and validate the first pilot gene batch: 28/28 KEGG `ppu00400` members.
- [x] Open the first module/pathway PR for `ppu00400` / `tryptophan_biosynthesis`: [PR #1874](https://github.com/ai4curation/ai-gene-review/pull/1874).
- [ ] For each later module batch, full `fetch-gene` only the genes selected by module review.
- [ ] Track module satisfiability gaps, over-annotations, missing GO terms, and candidate new module documents.

# NOTES

## 2026-07-05

Started the genome-wide expansion plan. The curation unit is now a pathway/module
rather than an individual gene: use UniProt metadata to build the whole-proteome
map, use modules as expected pathway structure, and spend full gene-review effort
only where the module pass creates an actionable curation question.

Updated provider policy: Asta is the normal gene-level first-pass research
provider for this organism; Falcon is the preferred module-level provider.
PaperBLAST remains useful as an opportunistic lookup, but not the main workflow.

Fetched the UniProt-derived gene list for the KT2440 reference proteome:
`projects/P_PUTIDA/data/psepk_gene_list.tsv` has 5,527 protein records, all with
`PP_` ordered locus tags. The snapshot contains 742 reviewed entries, 4,785
unreviewed entries, 1,452 entries with EC numbers, and 26 suggested review-name
collisions that are disambiguated by accession in the `suggested_review_name`
column.

Partitioned the 5,527 genes into first-pass pathway/module buckets using
organism-specific KEGG `ppu` pathway mappings as the primary source, UniPathway
as a fallback pathway source, and UniProt metadata heuristics for non-pathway
systems and unknowns. Current output has 161 primary buckets and 5,673
many-to-many pathway memberships. Primary assignments: 1,724 KEGG-pathway genes,
40 UniPathway-fallback genes, 1,789 functional-module genes, 1,149 orphan genes
with EC/domain signal, and 825 unknown/minimal-signal genes.

Added `scripts/module_pathway_taxon_deep_research_wrapper.py` and
`templates/module_pathway_taxon_research.md.j2` for module + pathway + taxon
deep research. For PSEPK, the wrapper resolves `projects/P_PUTIDA` automatically,
uses the local pathway partition to add candidate genes, and writes reports under
`projects/P_PUTIDA/deep-research/`.

Built `projects/P_PUTIDA/data/psepk_pathway_worklist.tsv` with 161 pathway/module
bucket rows. Selected the first pilot batch: KEGG `ppu00400` ("Phenylalanine,
tyrosine and tryptophan biosynthesis") seeded by the existing neutral
`modules/tryptophan_biosynthesis.yaml` module. The generated checklist
`projects/P_PUTIDA/batches/ppu00400_tryptophan_biosynthesis.md` has 28 candidate
KEGG members, 20 genes whose primary bucket is `ppu00400`, 15 existing review
files, and 0 existing Asta research files.

Attempted `just module-deep-research-falcon tryptophan_biosynthesis`, but the
command stalled in `uv` dependency/environment bootstrap before reaching
`deep-research-client` or the Falcon provider; the run was interrupted without
creating `modules/tryptophan_biosynthesis-deep-research-falcon.md`. The global
`deep-research-client` executable is not on PATH, so the configured execution
route remains blocked on `uv run` completing successfully.

Later in the same local session, fixed the provider execution route by updating
the deep-research wrappers to call `uvx --from deep-research-client[cyberian]==0.2.7rc1
deep-research-client` instead of bootstrapping the full project environment for
each run. Falcon is documented operationally as a long-running provider for this
project; the first completed Falcon module runs took about 22 minutes each.

Completed Falcon research for the pilot:

- `modules/tryptophan_biosynthesis-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__tryptophan_biosynthesis__ppu00400-deep-research-falcon.md`

Fetched all missing review folders for the 28 KEGG `ppu00400` members and ran
Asta gene-level retrieval for all 28. The regenerated checklist
`projects/P_PUTIDA/batches/ppu00400_tryptophan_biosynthesis.md` now records 28
existing review files, 28 curated review files, and 28 Asta reports.

Completed the first-pass curation of all `ppu00400` batch gene reviews. Newly
curated stubs included the aroE paralogs, aroQ paralogs, aroF-I/aroF-II, `pabA`
(treated as the TrpG-like anthranilate synthase amidotransferase component for
the tryptophan module), `quiA`, `amaC`, `PP_3768`, and `phhA`. The Falcon
module/taxon report recommends keeping the neutral `tryptophan_biosynthesis`
module boundary strict at chorismate to L-tryptophan and treating upstream
shikimate genes, phenylalanine/tyrosine branch genes, and quinate-catabolic
genes as neighboring or shared-pathway context rather than core tryptophan
module members.

Validation run on 2026-07-05 PDT / 2026-07-06 UTC:

- `just validate PSEPK <gene>` for all 28 genes in
  `projects/P_PUTIDA/batches/ppu00400_tryptophan_biosynthesis.tsv`
- `uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/tryptophan_biosynthesis.yaml`

All validations passed. Remaining warnings are non-blocking and mostly note that
the gene reviews do not cite Asta reports directly; that is expected for this
light first pass because Asta is retained as retrieval context rather than used
as a hypothesis source unless it adds curation-changing evidence.

Opened draft PR [#1874](https://github.com/ai4curation/ai-gene-review/pull/1874)
for the `ppu00400` / `tryptophan_biosynthesis` pilot batch.
