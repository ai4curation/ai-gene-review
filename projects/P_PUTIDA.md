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
- `projects/P_PUTIDA/batches/ppu02020_two_component_system_partition.md`
  tracks the ppu02020 umbrella split. All 99 partition-table genes now have
  first-pass review and Asta coverage. Completed outputs include
  `modules/inorganic_nutrient_homeostasis_regulation_boundary.yaml`,
  `modules/iron_uptake_regulation_boundary.yaml`,
  `modules/osmotic_envelope_efflux_regulation_boundary.yaml`,
  `modules/alginate_biofilm_regulation_boundary.yaml`,
  `modules/ecf_sigma_anti_sigma_boundary.yaml`,
  `modules/metal_cation_response_efflux_boundary.yaml`,
  `modules/pili_surface_adhesion_boundary.yaml`,
  `modules/dicarboxylate_tricarboxylate_transport_regulation_boundary.yaml`,
  `modules/orphan_two_component_regulators_boundary.yaml`, and side-context
  placements for `dnaA` in `modules/bacterial_dna_replication.yaml` and `etp`
  in `modules/protein_phosphorylation_boundary.yaml`.

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
- [x] Complete central-carbon batch `ppu00020` / `tca_cycle`: 30/30 candidate genes fetched, Asta-backed, curated, and validated; module and Falcon reports complete.
- [x] Complete central-carbon batch `ppu00030` / `pentose_phosphate_pathway`: 36/36 candidate genes fetched, Asta-backed, curated, and validated; module and Falcon reports complete.
- [x] Complete central-carbon batch `ppu00010` / `entner_doudoroff_and_gluconeogenesis`: 38/38 candidate genes fetched, Asta-backed, curated, and validated; module and Falcon reports complete.
- [x] Complete aromatic-catabolism batch `ppu00362` / `benzoate_degradation`: 40/40 candidate genes fetched, Asta-backed, curated, and validated; module and Falcon reports complete.
- [x] Complete aromatic umbrella batch `ppu01220` / `aromatic_compound_degradation`: 20/20 candidate genes fetched, Asta-backed, curated, and validated; module and Falcon reports complete.
- [x] Complete aromatic upper-pathway batch `ppu00622` / `benzoate_upper_pathway`: 6/6 candidate genes fetched, Asta-backed, curated, and validated; module and Falcon reports complete.
- [x] Complete amino-acid metabolism batch `ppu00220` / `arginine_biosynthesis`: 32 candidate genes fetched, Asta-backed, first-pass curated, validated, and rendered; species-neutral module seeded and validated; `argD` promoted from UniPathway UPA00068 to fill the aminotransferase step; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete amino-acid metabolism batch `ppu00270` / `methionine_biosynthesis`: 46/46 candidate genes fetched, Asta-backed, curated, and validated; module and Falcon reports complete.
- [x] Complete amino-acid metabolism batch `ppu00340` / `histidine_biosynthesis`: 20/20 candidate genes fetched, Asta-backed, curated, and validated; module and Falcon reports complete.
- [x] Complete carbohydrate side-bucket batch `ppu00052` / `galactose_leloir_pathway`: 8/8 extracted candidate genes fetched, Asta-backed, curated, and validated; module and Falcon reports complete.
- [x] Complete carbohydrate boundary batch `ppu00040` / `pentose_glucuronate_interconversions`: 8/8 KEGG candidates plus 2 Falcon-promoted gap-fill genes fetched, Asta-backed, curated, and validated; module and Falcon reports complete.
- [x] Complete aldarate batch `ppu00053` / `hexuronate_aldarate_catabolism`: 8/8 KEGG candidates plus `gnl`/PP_1170 context fetched, Asta-backed, curated, and validated; module and Falcon reports complete.
- [x] Complete carbohydrate boundary batch `ppu00051` / `fructose_mannose_metabolism`: 18/18 KEGG candidates plus Falcon-promoted `fruB`/PP_0793 fetched, Asta-backed, curated, and validated; module and Falcon reports complete.
- [x] Complete lipid/cell-envelope batch `ppu00061` / `fatty_acid_biosynthesis`: 19/19 candidate genes fetched, Asta-backed, curated, and validated; module and Falcon reports complete.
- [x] Complete UniPathway ACP support batch `UPA00094` / `fatty_acid_biosynthesis`: UniPathway-primary `acpP` fetched, Asta-backed, curated, validated, and rendered; already-curated `accB`, `fabG`, `fabF`, `PP_3303`, `fabA`, `fabB`, and `fabV` reused as FAS-II context; existing fatty-acid-biosynthesis module extended with explicit AcpP acyl-carrier activity; generic Falcon module report reused; UPA-specific PSEPK Falcon report failed with Edison HTTP 402 and remains queued for rerun.
- [x] Complete lipid/cell-envelope batch `ppu00071` / `bacterial_fatty_acid_beta_oxidation`: 22/22 KEGG candidates plus 5 Falcon-promoted/conflict genes fetched or rechecked, Asta-backed, curated, and validated; module and Falcon reports complete.
- [x] Complete UniPathway rubredoxin support batch `UPA00191` / `bacterial_fatty_acid_beta_oxidation`: 1/1 RubA pathway member fetched, Asta-backed, curated, validated, and rendered; existing beta-oxidation boundary module extended with RubA as alkane/rubredoxin electron-transfer context; generic Falcon module report reused; UPA-specific PSEPK Falcon report failed with Edison HTTP 402 and remains queued for rerun.
- [x] Complete UniPathway fatty-acid beta-oxidation support batch `UPA00659` / `bacterial_fatty_acid_beta_oxidation`: UniPathway-primary `PP_4030` fetched, Asta-backed, curated, validated, and rendered; already-curated `fadE`, `fadB`, and `fadA__Q88L01` reused as beta-oxidation context; existing beta-oxidation module extended with a PP_4030 auxiliary dienoyl-CoA isomerase candidate; generic Falcon module report reused; UPA-specific PSEPK Falcon report failed with Edison HTTP 402 and remains queued for rerun.
- [x] Complete lipid/cell-envelope/absence batch `ppu00074` / `mycolic_acid_biosynthesis`: 2/2 candidate genes fetched, Asta-backed, curated, and validated; module and Falcon reports complete; pathway marked not expected in KT2440.
- [x] Complete cofactors/redox batch `ppu00130` / `ubiquinone_biosynthesis`: 14/14 KEGG candidates plus 3 UniPathway/Falcon-promoted accessory genes fetched, Asta-backed, curated, and validated; module and Falcon reports complete.
- [x] Complete UniPathway ubiquinone support batch `UPA00232` / `ubiquinone_biosynthesis`: 11/11 UniPathway members present, Asta-backed, curated, validated, and rendered; registered as the strict UbiC/UbiA/UbiD/UbiX/VisC-UbiI/UbiH/Coq7/UbiE/UbiG route plus UbiB/UbiJ/UbiK accessory context already handled by the completed `ppu00130` ubiquinone module and Falcon reports.
- [x] Complete cofactors/redox batch `ppu00900` / `terpenoid_backbone_biosynthesis`: 17/17 KEGG candidates fetched or rechecked, Asta-backed, curated, and validated; module and Falcon reports complete; strict MEP/prenyl-diphosphate module separated from UbiX and thiolase/mevalonate spillovers.
- [x] Complete carotenoid-boundary batch `ppu00906` / `carotenoid_biosynthesis_boundary`: 1/1 KEGG membership gene fetched, Asta-backed, first-pass curated, validated, and rendered; new boundary/partial module seeded and validated; `crtZ` retained as a predicted beta-carotene hydroxylase/xanthophyll-tailoring step rather than evidence for a complete carotenoid biosynthesis pathway.
- [x] Complete monoterpene-degradation boundary batch `ppu00907` / `pinene_camphor_geraniol_degradation_boundary`: 7 KEGG membership genes rechecked, Asta-backed, validated, and rendered; new boundary/absence module seeded and validated; HMG-CoA lyase paralogs and CoA-thioester beta-oxidation/hydration spillovers separated from any claim of complete pinene, camphor, or geraniol degradation.
- [x] Complete cofactors/vitamins batch `ppu00730` / `thiamine_biosynthesis`: 13/13 KEGG candidates plus promoted `pet` and `PP_5105` context genes fetched, Asta-backed, curated, and validated; module and Falcon reports complete; ThiS gap filled and ThiF left unresolved pending stronger evidence.
- [x] Complete UniPathway thiamine support batch `UPA00060` / `thiamine_biosynthesis`: 9/9 UniPathway members present, Asta-backed, curated, validated, and rendered; registered as a support view of the completed `ppu00730` thiamine module, with `pet`/PP_3185 retained as the sole UniPathway-primary thiamine-salvage/context member and existing thiamine Falcon reports reused.
- [x] Complete cofactors/vitamins batch `ppu00740` / `riboflavin_biosynthesis`: 15/15 KEGG membership genes fetched, Asta-backed, curated, and validated; module and Falcon reports complete; RibBX paralogs corrected so `ribAB-I`/`ribAB-II` no longer satisfy GTP cyclohydrolase II.
- [x] Complete cofactors/vitamins batch `ppu00750` / `vitamin_b6_metabolism`: 9/9 KEGG membership genes fetched, Asta-backed, curated, and validated; module and Falcon reports complete; strict PLP route covered by `epd`, `pdxB`, `serC`, `pdxA`, `pdxJ`, and `pdxH`, with `pdxY` salvage and `thrC`/`PP_0662` boundary-only.
- [x] Complete cofactors/vitamins/redox batch `ppu00760` / `nad_biosynthesis_and_nicotinate_metabolism`: 30/30 KEGG membership genes fetched, Asta-backed, curated, and validated; module and Falcon reports complete; strict coverage split into de novo NAD, PncB/PncC salvage, NadK/SthA/Pnt redox interconversion, and nicotinate catabolism, with 11 boundary/uncertain candidates and a PncA nicotinamidase gap.
- [x] Complete UniPathway nicotinate-catabolism support batch `UPA01010` / `nad_biosynthesis_and_nicotinate_metabolism`: 9/9 UniPathway members present, Asta-backed, curated, validated, and rendered; registered as the NicA/NicB/NicC/NicX/NicD/NicF/MaiA catalytic route plus `nicR`/`nicS` regulator context already handled by the completed `ppu00760` NAD/nicotinate module and Falcon reports.
- [x] Complete cofactors/vitamins batch `ppu00770` / `pantothenate_and_coa_biosynthesis`: 24/24 KEGG membership genes plus UniPathway-only `PP_4452` fetched, Asta-backed, curated, validated, and rendered; module and Falcon reports complete; strict coverage split into PanB/PanC pantothenate assembly, CoaX/Dfp/CoaD/CoaE CoA biosynthesis, beta-alanine precursor context, and ACP/nucleotide boundary nodes, with PP_2325/PP_2998/PP_4452 left candidate-uncertain.
- [x] Complete UniPathway support batch `UPA00028` / `pantothenate_and_coa_biosynthesis`: 6/6 pantothenate-biosynthesis cross-reference genes present, Asta-backed, curated, validated, and rendered; handled as the PanB/PanE/PanC pantothenate subset plus UniPathway-only candidate `PP_4452` within the ppu00770 pantothenate/CoA module.
- [x] Complete UniPathway PHA support batch `UPA00212` / `mcl_pha_monomer_supply_from_fas`: 1/1 PhaG pathway member present, Asta-backed, curated, validated, and rendered; new PhaG FAS-to-mcl-PHA monomer-supply module seeded and validated; downstream PhaC polymerization and beta-oxidation/PhaJ routes kept as adjacent PHA context; Falcon generic and PSEPK-specific module reports failed with Edison HTTP 402 and remain queued for rerun.
- [x] Complete UniPathway tRNA-modification support batch `UPA00392` / `queuosine_biosynthesis_boundary`: 3/3 primary UniPathway genes plus `queF` side context present, Asta-backed, curated, validated, and rendered; new tRNA queuosine module seeded and validated; Falcon generic and PSEPK-specific module reports failed with Edison HTTP 402 and remain queued for rerun.
- [x] Complete UniPathway osmoprotection-side batch `UPA00529` / `glycine_betaine_biosynthesis_boundary`: 3/3 glycine-betaine pathway members present, Asta-backed, curated, validated, and rendered; BetA/BetB retained as the catalytic choline-to-glycine-betaine route and BetI as regulatory boundary context; Falcon generic and PSEPK-specific module reports failed with Edison HTTP 402 and remain queued for rerun.
- [x] Complete UniPathway cofactor-biosynthesis support batch `UPA00539` / `pqq_biosynthesis`: 7/7 PQQ-biosynthesis genes present, Asta-backed, curated, validated, and rendered; new PQQ module seeded and validated; `pqqD1`/`pqqD2` curated as PqqA peptide-chaperone factors with generic quinone binding marked over-annotated; ambiguous `pqqG` context excluded pending identifier reconciliation; Falcon generic and PSEPK-specific module reports failed with Edison HTTP 402 and remain queued for rerun.
- [x] Complete UniPathway peptidoglycan-biosynthesis route batch `UPA00219` / `peptidoglycan_biosynthesis`: missing UniPathway-primary `PP_1451` and `ddl` fetched, Asta-backed, curated, validated, and rendered; 23 already-curated peptidoglycan members reused; existing peptidoglycan module extended with the standalone `ddl` paralog and `PP_1451`/`PP_2320` L,D-transpeptidase-family remodeling candidates; Falcon generic and PSEPK-specific module reports failed with Edison HTTP 402 and remain queued for rerun.
- [x] Complete UniPathway peptidoglycan-recycling support batch `UPA00544` / `peptidoglycan_biosynthesis`: UniPathway-primary `mpl` fetched by accession alias, Asta-backed, curated, validated, and rendered; already-curated `amgK`, `murU`, `anmK`, `mupP`, and `nagZ` reused as MurNAc/anhMurNAc and muropeptide recycling context; existing peptidoglycan module extended with a discrete recycling/salvage arm; Falcon generic and PSEPK-specific module reports failed with Edison HTTP 402 and remain queued for rerun.
- [x] Complete UniPathway OPG support batch `UPA00637` / `osmoregulated_periplasmic_glucan_biosynthesis`: 2/2 OPG pathway members present, Asta-backed, curated, validated, and rendered; new OpgH/OpgG osmoregulated periplasmic glucan module seeded and validated; OPG kept distinct from alginate, LPS, peptidoglycan, cellulose, and broad exopolysaccharide modules; Falcon generic and PSEPK-specific module reports failed with Edison HTTP 402 and remain queued for rerun.
- [x] Complete UniPathway bacterial cellulose batch `UPA00694` / `bacterial_cellulose_biosynthesis`: UniPathway-primary `bcsB` and `PP_2638` fetched, Asta-backed, curated, validated, and rendered; already-curated `bcsA` reused as the UDP-forming cellulose synthase catalytic context; new bacterial BcsA/BcsB/BcsC-like module seeded and validated, distinct from the existing plant cellulose module; Falcon generic and PSEPK-specific module reports failed with Edison HTTP 402 and remain queued for rerun.
- [x] Complete UniPathway lipoprotein-maturation support batches `UPA00664` and `UPA00666` / `bacterial_lipoprotein_maturation`: new three-step Lgt-LspA-Lnt module seeded and validated; `lgt` and `lnt` fetched, Asta-backed, curated, validated, and rendered; already-curated `lspA` reused as UPA00665 middle-step context; Falcon generic and both PSEPK-specific module reports failed with Edison HTTP 402 and remain queued for rerun.
- [x] Complete UniPathway tRNA-modification support batch `UPA00729` / `trna_ms2io6a37_hydroxylation`: 1/1 MiaE pathway member present, Asta-backed, curated, validated, and rendered; new single-reaction module seeded and validated; Falcon generic and PSEPK-specific module reports failed with Edison HTTP 402 and remain queued for rerun.
- [x] Complete UniPathway tRNA-modification support batch `UPA00989` / `trna_m7g46_methylation`: 1/1 TrmB pathway member fetched, Asta-backed, curated, validated, and rendered; new single-reaction m7G46 tRNA methylation module seeded and validated; tRNA methyltransferase-complex annotation marked over-annotated; Falcon generic and PSEPK-specific module reports failed with Edison HTTP 402 and remain queued for rerun.
- [x] Complete UniPathway translation-factor support batch `UPA00345` / `efp_translation_stall_rescue`: 1/1 EF-P pathway member fetched by accession alias, Asta-backed, curated, validated, and rendered; new single-gene EF-P stalled-ribosome rescue module seeded and validated; broad translation-regulation/peptide-biosynthesis annotations retained as non-core context; Falcon generic and PSEPK-specific module reports failed with Edison HTTP 402 and remain queued for rerun.
- [x] Complete energy/respiration batch `ppu00190` / `oxphos`: 54 KEGG membership genes fetched, Asta-backed, first-pass curated, validated, and rendered; existing module and generic Falcon module report complete; PSEPK-specific Falcon module+pathway report failed with Edison HTTP 402 and remains queued for rerun.
- [x] Complete energy/inorganic-nitrogen batch `ppu00910` / `nitrogen_cycle`: 20 KEGG membership genes fetched, Asta-backed, first-pass curated, validated, and rendered; existing species-neutral nitrogen-cycle module validated; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete sulfur-metabolism boundary batch `ppu00920` / `sulfur_metabolism_boundary`: 54 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; boundary module seeded, validated, and later extended with the PP_0225-PP_0227 cystine/sulfur-compound ABC import sub-batch from `ppu02010`; sulfate/thiosulfate import and assimilation, cystine/sulfur-compound import, alkanesulfonate/taurine import and desulfonation, sulfur redox, sulfurtransferase, methionine/cysteine, and organosulfur CoA/AMP side nodes kept separated; Falcon module reports remain queued.
- [x] Complete caprolactam-degradation boundary batch `ppu00930` / `caprolactam_degradation_boundary`: 3 KEGG membership genes rechecked, Asta-backed, validated, and rendered; new boundary/absence module seeded and validated; `fadB`, PP_2217, and `paaF` kept as shared CoA-thioester hydratase/beta-oxidation spillovers rather than evidence for complete caprolactam degradation.
- [x] Complete flavonoid-degradation boundary batch `ppu00946` / `flavonoid_degradation_boundary`: 7 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary/uncertain module seeded and validated; `bglX` kept as broad beta-glucosidase context and PP_3195-PP_3206 retained as an unresolved aromatic-compound hydrolase/redox/cupin/dehydratase cluster rather than evidence for a complete flavonoid-degradation route.
- [x] Complete translation batch `ppu00970` / `aminoacyl_trna_biosynthesis`: 27 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new module seeded and validated; canonical aminoacyl-tRNA synthetases separated from GatCAB transamidation, initiator Met-tRNA formylation, selenocysteine-tRNA side chemistry, and unresolved PP_0613 amidase context.
- [x] Partition translation/RNA-processing umbrella bucket `module:translation_rna_processing`: 128 primary genes split into nine curation-scale batches covering rRNA modification, ribosome maturation/hibernation, tRNA modification/processing, RNA decay/helicases, aminoacyl-tRNA quality control, translation factors/ribosome rescue, transcription spillovers, NRPS spillovers, and low-information RNA-binding/enzyme spillovers.
- [x] Complete translation/RNA-processing NRPS spillover split `nonribosomal_peptide_synthetase_spillovers` / `siderophore_biosynthesis_boundary`: 4/4 genes present, Asta-backed, first-pass curated, validated, and routed to pyoverdine/ferribactin NRPS assembly rather than translation; `pvdD` reused as the existing curated anchor, while `pvdJ`, `pvdI`, and `pvdL` were newly fetched and reviewed.
- [x] Complete translation/RNA-processing low-information spillover split `low_information_rna_binding_or_enzyme_spillovers` / `translation_rna_processing_spillover_boundary`: 2/2 genes present, Asta-backed, first-pass curated, validated, and represented in a new boundary module; `PP_2182` retained as a ProQ/FinO RNA-chaperone candidate and `PP_2953` routed out as a NADPH quinone-reductase-like oxidoreductase rather than RNA processing.
- [x] Complete translation/RNA-processing transcription/RNA-polymerase spillover split `transcription_rna_polymerase_spillovers` / `transcription_rna_polymerase_spillover_boundary`: 6/6 genes present, Asta-backed, first-pass curated, validated, and represented in a new boundary module; `nusA`/`nusB`, `rapA`, `dksA`, `PP_2266`, and `PP_4553` were routed to transcription termination/antitermination, RNA polymerase regulation, sigma-factor, or RNAP side-node context rather than translation.
- [x] Complete translation/RNA-processing translation-factor/ribosome-rescue split `translation_factors_ribosome_rescue` / `translation_factor_ribosome_rescue_boundary`: 10/10 genes fetched, Asta-backed, first-pass curated, validated, and represented in a new boundary module; initiation/elongation factors, EttA throttle, ribosome recycling, peptidyl-tRNA hydrolysis, trans-translation, Hsp15, and YchF ribosome-associated ATPase context were kept separate from structural ribosome and RNA-modification modules.
- [x] Complete translation/RNA-processing aminoacyl-tRNA quality-control split `aminoacyl_trna_charging_editing_quality_control` / `aminoacyl_trna_quality_control_boundary`: 11/11 genes fetched, Asta-backed, first-pass curated, validated, and represented in a new boundary module; YbaK/Dtd/YcfH deacylase context, Aat N-end-rule transferase chemistry, Glu-Q tRNA(Asp) modification, and low-information GAD/T6SS or short-fragment side nodes were separated from canonical aminoacyl-tRNA synthetases.
- [x] Complete translation/RNA-processing RNase/RNA-decay/helicase split `ribonuclease_rna_decay_processing_helicases` / `rna_decay_processing_boundary`: 12/12 genes fetched or rechecked, Asta-backed, first-pass curated, validated, and represented in a new boundary module; RNase P/G/T/Z/D/PH activities, SrmB/DbpA DEAD-box helicase context, and RraA/RraB/YhbY-like side nodes were separated from broad RNA-binding/hydrolase spillovers.
- [x] Complete translation/RNA-processing rRNA-modification split `rrna_modification_methyltransferase_pseudouridine` / `rrna_modification_ribosome_maturation_boundary`: 29/29 genes fetched or rechecked, Asta-backed, first-pass curated, validated, and represented in a new boundary module; site-specific Rsm/Rlm/Rlu/Rsu-family rRNA methyltransferases and pseudouridine synthases were separated from dual RlmN/RluF side chemistry, RsmE paralogs, and unresolved PP_4306/RlmI target-site side nodes.
- [x] Complete translation/RNA-processing ribosome-assembly/maturation/hibernation split `ribosome_assembly_maturation_hibernation` / `bacterial_ribosome_maturation_regulation_boundary`: 24/24 genes fetched, Asta-backed, first-pass curated, validated, and represented in a new boundary module; Der/Era/BipA-style GTPases, 30S/50S maturation factors, HPF/RMF/RsfS hibernation or silencing factors, ribosomal-protein modification enzymes, and low-information ribosomal-interface side nodes were separated from structural ribosome and rRNA-modification modules.
- [x] Complete translation/RNA-processing tRNA-modification/processing split `trna_modification_processing` / `trna_modification_processing_boundary`: 30/30 genes fetched or rechecked, Asta-backed, first-pass curated, validated, and represented in a new boundary module; wobble-uridine side-chain chemistry, t6A37 formation, tRNA methylation, pseudouridylation, deamination, lysidine formation, thiolation, dihydrouridine synthesis, aminocarboxypropylation, prenylation, and CCA-end processing were separated from ribosome and RNA-decay modules. This closes the 128-gene translation/RNA-processing umbrella at first pass.
- [x] Complete siderophore-biosynthesis boundary batch `ppu00975` / `siderophore_biosynthesis_boundary`: 3 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary/partial module seeded and validated; PvdH/PP_2800 diaminobutyrate aminotransferase context and PvdY MbtK/IucB-like N-acyltransferase context kept as precursor/tailoring chemistry rather than evidence for a complete siderophore biosynthesis pathway.
- [x] Complete alkaloid-biosynthesis boundary batch `ppu00996` / `alkaloid_biosynthesis_boundary`: 1 KEGG membership gene rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary/absence module seeded and validated; PP_3358 kept as feruloyl-CoA hydratase/lyase in hydroxycinnamate/vanillin side metabolism rather than evidence for a complete alkaloid biosynthesis pathway.
- [x] Complete plant-secondary-metabolite boundary batch `ppu00999` / `plant_secondary_metabolite_biosynthesis_boundary`: 5 KEGG membership genes rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary/absence module seeded and validated; shikimate dehydrogenase paralogs, BglX beta-glucosidase, and MetK SAM synthesis kept as broad precursor/side-node chemistry rather than a complete plant secondary metabolite biosynthesis pathway.
- [x] Complete unsaturated-fatty-acid boundary batch `ppu01040` / `unsaturated_fatty_acid_biosynthesis_boundary`: 3 KEGG membership genes fetched, Asta-backed, first-pass curated, validated, and rendered; new boundary/side-node module seeded and validated; TesA/TesB/PP_5331 kept as lipid ester/acyl-thioester hydrolase side nodes rather than the FabA/FabB unsaturated-acyl-ACP branch.
- [x] Complete siderophore-group NRPS boundary batch `ppu01053` / `siderophore_biosynthesis_boundary`: 2 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; existing siderophore boundary module extended and validated; PP_1183 kept as EntD-family carrier-protein phosphopantetheinyltransferase support and PP_2170 kept as chorismate-mutase precursor context rather than evidence for a complete siderophore-group NRPS route.
- [x] Complete sulfur-cycle boundary batch `ppu01320` / `sulfur_metabolism_boundary`: 9 KEGG membership genes rechecked, Asta-backed, validated, and rendered; existing sulfur boundary module extended and validated; sulfate activation/reduction, sulfite reductase, SoxYZ-like/cytochrome sulfur-redox boundary nodes, and CysK cysteine synthesis treated as subroute context rather than a standalone complete sulfur cycle.
- [x] Complete beta-lactam-resistance boundary batch `ppu01501` / `beta_lactam_resistance_boundary`: 20 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new resistance-boundary module seeded and validated; AmpC hydrolysis, AmpG/NagZ cell-wall recycling, PBP targets, RND/MFP/OMF efflux systems, and OprD/opmQ permeability/export context separated rather than treated as a single pathway.
- [x] Complete vancomycin-resistance boundary batch `ppu01502` / `vancomycin_resistance_boundary`: 6 KEGG membership genes rechecked, Asta-backed, validated, and rendered; new boundary/absence module seeded and validated; DadX, DdlA/DdlB, MurF, MraY, and MurG treated as D-alanine and peptidoglycan precursor/target context rather than a VanHAX D-Ala-D-Lac vancomycin-resistance route.
- [x] Complete cationic-antimicrobial-peptide-resistance boundary batch `ppu01503` / `cationic_antimicrobial_peptide_resistance_boundary`: 21 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new resistance-boundary module seeded and validated; PP_1202 phosphatidylglycerol lysylation separated from LPS/lipid A context, PhoPQ/Cpx-like regulation, RND efflux, periplasmic protein quality control, and peptidoglycan remodeling side nodes.
- [x] Partition ABC-transporter umbrella batch `ppu02010` / `abc_transporters_boundary`:
  207 ABC-transporter candidates clustered into 74 locus-neighborhood systems and
  marked `PARTITIONED` rather than forced into one module; PP_0112-PP_0114
  MetNIQ methionine import (`metQ`, `metI`, `metN1`), PP_0219-PP_0221
  MetNIQ-like methionine import (`metP`, `metN2`, `PP_0221`),
  PP_0117-PP_0120 ZnuABC zinc import (`znuB`, `znuC`, `PP_0120`),
  PP_3801-PP_3803 Znu-like cation/zinc import (`PP_3801`, `PP_3802`,
  `PP_3803`),
  PP_0824-PP_0827 phosphonate import (`ptxB`, `phnC`, `phnE`, `ptxC`),
  PP_0225-PP_0227 cystine/sulfur-compound import (`sctC`, `sctS`, `fliY`),
  PP_0280-PP_0283 arginine/ornithine ABC import (`PP_0280`, `PP_0281`,
  `artJ`, `aotP`), PP_4483-PP_4486 His/ArgT basic-amino-acid ABC import
  (`hisP`, `hisM`, `hisQ`, `argT`), PP_1297-PP_1300 YhdWXYZ unresolved
  amino-acid ABC import (`yhdW`, `yhdX`, `yhdY`, `yhdZ`), PP_0294-PP_0296
  plus PP_0304, PP_0076,
  PP_1741/`betX`, PP_0868-PP_0871, PP_2774-PP_2775, and PP_3558-PP_3559 compatible-solute
  import/binding (`cbcV`, `cbcW`, `cbcX`, `caiX`, `PP_0076`, `betX`, `yehX`,
  `yehW`, `PP_0870`, `PP_0871`, `opuA`, `PP_2775`, `PP_3558`, `PP_3559`),
  PP_0873/`potF-I` plus PotF-like singleton paralogs PP_2195, `potF-II`,
  PP_3719, `potF-III`, and `potF-IV` putrescine/polyamine binding (`potF-I`,
  `PP_2195`, `potF-II`, `PP_3719`, `potF-III`, `potF-IV`), PP_5177-PP_5181
  Spu/Pot spermidine/putrescine ABC import (`spuH`, `spuG`, `spuF`, `spuE`,
  `spuD`), PP_0878-PP_0885
  Dpp dipeptide import (`dppF`, `dppD`, `dppC`, `dppB`, `dppA-I`,
  `dppA-II`, `dppA-III`), PP_1068-PP_1071 GltIJKL glutamate/aspartate import
  (`gltL`, `gltK`, `gltJ`, `gltI`), PP_0615-PP_0619 branched-chain amino-acid
  import (`PP_0615`, `PP_0616`, `PP_0617`, `PP_0618`, `PP_0619`),
  PP_2748-PP_2753 branched-chain amino-acid import (`PP_2748`, `PP_2749`,
  `PP_2750`, `PP_2751`, `PP_2752`, `PP_2753`),
  PP_2767-PP_2770 branched-chain amino-acid import (`PP_2767`, `PP_2768`,
  `PP_2769`, `PP_2770`),
  PP_1137-PP_1141 LivFGMHK branched-chain amino-acid import (`livF-I`,
  `livG`, `livM`, `livH`, `livK`) plus PP_4863-PP_4867 Bra/Liv
  branched-chain amino-acid import (`livF-II`, `braF`, `braE`, `braD`,
  `PP_4867`), PP_2656-PP_2659 PstSACB phosphate import (`pstS`,
  `pstC`, `pstA`, `pstB1`) plus PP_5326-PP_5329 Pst-like phosphate import
  (`pstB2`, `PP_5327`, `PP_5328`, `PP_5329`), PP_3828-PP_3830 ModABC
  molybdate import (`modA`, `modB`, `modC`), PP_4841-PP_4845 UrtABCDE urea
  import (`urtA`, `urtB`, `urtC`, `urtD`, `urtE`), PP_2154-PP_2156 LolCDE
  lipoprotein localization (`lolC`, `lolD`, `lolE`), PP_4324-PP_4327 CcmABCD
  heme export/cytochrome c maturation (`ccmD`, `ccmC`, `ccmB`, `ccmA`),
  `pvdT`/`pvdE` pyoverdine export and precursor-export context,
  `paxB`/`PP_0804`/`aprDA`/`cyaB` type-I-secretion ABC exporter candidates,
  and `PP_2240` as an unresolved generic ABCD-like efflux transporter,
  PP_0958-PP_0962 Mla/Ttg2 phospholipid transport/lipid asymmetry (`mlaF`,
  `mlaE`, `mlaD`, `ttg2D`, `ttg2E`), PP_0140-PP_0142
  Mce/MlaD-MlaE-like phospholipid transport candidate (`PP_0140`, `PP_0141`,
  `PP_0142`), Lpt/MsbA lipid A-core/LPS export
  (`lptB`, `PP_0982`, `PP_0983`, `msbA`), with `lptA`, `lptC`, `lptD`, and
  `lptE` curated as module context, PP_1778-PP_1779 unresolved
  LPS/polysaccharide ABC export candidate (`PP_1778`, `PP_1779`) as a separate
  Lpt/LPS boundary part, `ftsX`/`ftsE` FtsEX cell-division ABC-like boundary
  (`ftsX`, `ftsE`), PP_5165/`plpB` unresolved NlpA-family
  lipoprotein adjacent to the CysAWU/Sbp sulfate-import locus,
  PP_1015-PP_1018 Gts glucose
  import (`gtsA`, `gtsB`, `gtsC`, `gtsD`), PP_2260-PP_2264 unresolved
  sugar/glycerol-phosphate-like import (`PP_2260`, `PP_2261`, `PP_2262`,
  `PP_2263`, `PP_2264`), PP_2454-PP_2459 Rbs ribose import/accessory
  utilization (`rbsB`, `rbsA-I`, `rbsC`, `rbsD`) plus PP_2757-PP_2761 second
  ribose-like RbsABC comparison (`PP_2757`, `PP_2758`, `rbsA`, `PP_2760`,
  `PP_2761`), PP_3076-PP_3078, PP_4146-PP_4150, and dppA-IV Yej/Dpp-like
  peptide ABC import candidates (`PP_3076`, `PP_3077`, `PP_3078`, `PP_4146`,
  `yejA`, `PP_4148`, `PP_4149`, `yejF`, `dppA-IV`), PP_3342-PP_3346 NikABCDE
  nickel import (`nikA`, `nikB`, `nikC`, `nikD`, `nikE`), and PP_4881-PP_4882, PP_5135-PP_5137, and
  PP_5195-fbpA ferric/iron ABC import candidates (`PP_4881`, `PP_4882`,
  `PP_5135`, `PP_5136`, `fbpC`, `PP_5195`, `fbpA`), PP_0524 cobalamin-binding
  candidate, PP_3818 phosphate-binding singleton, PP_1078 ATP-binding
  singleton, PP_2595/PP_2596 plus PP_2628 and PP_4542 unresolved
  ABCB/type-1-exporter-like transporters, and PP_5157 cell-envelope
  solute-binding-family singleton fetched, Asta-backed,
  curated, validated, and integrated into their real biological modules; current
  ppu02010 coverage is 207/207 curated reviews and 207/207 Asta reports, with
  the substrate-unknown ABC bucket retained for future targeted biology.
- [x] Complete cofactors/vitamins batch `ppu00790` / `folate_biosynthesis`: 32 KEGG membership genes fetched, Asta-backed, first-pass curated, validated, and rendered; species-neutral module seeded and validated; Falcon generic and PSEPK-specific module reports failed with Edison HTTP 402 and remain queued for rerun.
- [x] Complete cofactors/one-carbon batch `ppu00670` / `one_carbon_by_folate`: 31 KEGG membership genes fetched, Asta-backed, first-pass curated, validated, and rendered; species-neutral module seeded and validated; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete nucleotide-metabolism batch `ppu00230` / `purine_metabolism`: 65 KEGG membership genes fetched, Asta-backed, first-pass curated, validated, and rendered; species-neutral broad purine-metabolism module seeded and validated; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete nucleotide-metabolism batch `ppu00240` / `pyrimidine_metabolism`: 36 KEGG membership genes fetched, Asta-backed, first-pass curated, validated, and rendered; species-neutral broad pyrimidine-metabolism module seeded and validated; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete amino-acid metabolism batch `ppu00250` / `alanine_aspartate_glutamate_metabolism`: 36 KEGG membership genes fetched, Asta-backed, first-pass curated, validated, and rendered; species-neutral broad alanine/aspartate/glutamate boundary module seeded and validated; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete amino-acid metabolism batch `ppu00260` / `glycine_serine_threonine_metabolism`: 66 KEGG membership genes fetched, Asta-backed, first-pass curated, validated, and rendered; species-neutral broad glycine/serine/threonine boundary module seeded and validated; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete boundary/absence batch `ppu00261` / `monobactam_biosynthesis_boundary`: 9 KEGG membership genes fetched, Asta-backed, first-pass curated, validated, and rendered; species-neutral monobactam boundary module seeded and validated; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete amino-acid degradation batch `ppu00280` / `branched_chain_amino_acid_degradation`: 35 KEGG membership genes fetched, Asta-backed, first-pass curated, validated, and rendered; species-neutral broad BCAA degradation module seeded and validated; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete amino-acid biosynthesis batch `ppu00290` / `branched_chain_amino_acid_biosynthesis`: 18 KEGG membership genes fetched, Asta-backed, first-pass curated, validated, and rendered; species-neutral broad BCAA biosynthesis module seeded and validated; obsolete authored L-isoleucine biosynthesis term usage refreshed to `GO:1901705`; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete amino-acid biosynthesis batch `ppu00300` / `lysine_biosynthesis`: 19 KEGG membership genes fetched, Asta-backed, first-pass curated, validated, and rendered; species-neutral diaminopimelate-route L-lysine biosynthesis module seeded and validated; obsolete authored route-specific lysine/diaminopimelate process usage kept out of new terms in favor of `GO:0009085`; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete amino-acid degradation batch `ppu00310` / `lysine_degradation`: 32 KEGG membership genes fetched, Asta-backed, first-pass curated, validated, and rendered; species-neutral broad lysine degradation and glutarate/pipecolate side-route module seeded and validated; strict Dav route separated from D-lysine, hydroxyglutarate, aldehyde-dehydrogenase, beta-oxidation, and lipoamide spillovers; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete amino-acid metabolism batch `ppu00330` / `arginine_proline_metabolism`: 39 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; species-neutral broad arginine/proline boundary module seeded and validated; proline biosynthesis, Ast arginine catabolism, polyamine/agmatine routes, opine/2-ketoarginine chemistry, and 5-oxoproline/creatinine side nodes separated; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete UniPathway proline-support batch `UPA00098` / `arginine_proline_metabolism`: 5/5 proline biosynthesis/interconversion members present, Asta-backed, curated, validated, and rendered; existing arginine/proline module updated to include `proA` and `proC` explicitly alongside `proB`, `proI`, and `ocd__Q88H32`; Falcon generic and PSEPK-specific module reports failed with Edison HTTP 402 and remain queued for rerun.
- [x] Complete UniPathway L-carnitine support batch `UPA00117` / `l_carnitine_dehydrogenation`: 1/1 LcdH pathway member fetched, Asta-backed, curated, validated, and rendered; new single-reaction cytoplasmic L-carnitine dehydrogenation module seeded and validated; fatty-acid metabolic process annotation marked over-annotated; Falcon generic and PSEPK-specific module reports failed with Edison HTTP 402 and remain queued for rerun.
- [x] Complete boundary/absence batch `ppu00332` / `carbapenem_biosynthesis_boundary`: 2 KEGG membership genes rechecked, Asta-backed, validated, and rendered; species-neutral boundary module seeded and validated; ProB/ProA treated as shared proline-precursor chemistry rather than evidence for carbapenem biosynthesis; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete aromatic-amino-acid batch `ppu00350` / `tyrosine_catabolism`: 16 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; existing tyrosine-catabolism module generalized for PSEPK homogentisate-pathway use; HmgA/HmgC/HmgB separated from aminotransferase, aldehyde-dehydrogenase, DOPA-decarboxylase, and auxin side-node spillovers; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete aromatic-amino-acid batch `ppu00360` / `phenylalanine_metabolism`: 28 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new broad phenylalanine/phenylacetate module seeded and validated; Paa phenylacetate activation/epoxidation/lower-pathway genes separated from homogentisate-route, D-amino-acid dehydrogenase, catalase, aldehyde, and auxin/fatty-acid-like side nodes; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete aromatic/xenobiotic boundary batch `ppu00361` / `chlorocyclohexane_chlorobenzene_degradation_boundary`: 3 KEGG membership genes rechecked, Asta-backed, validated, and rendered; new boundary module seeded and validated; CatA-I/CatA-II/CatB treated as catechol ortho-cleavage/beta-ketoadipate lower-pathway enzymes rather than evidence for a complete chlorocyclohexane or chlorobenzene upper-degradation module; real generic and taxon-aware Falcon commands attempted and blocked by Edison HTTP 402.
- [x] Complete amino-acid boundary batch `ppu00380` / `tryptophan_metabolism_boundary`: 20 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; `gcdH` and `katG` treated as primary glutaryl-CoA dehydrogenase and catalase-peroxidase side nodes, while `katE`, `katA`, and `PP_2887` remain oxidative-stress/peroxide-detoxification boundary genes rather than evidence for a complete tryptophan-catabolic route; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete secondary-metabolite boundary batch `ppu00401` / `novobiocin_biosynthesis_boundary`: 4 KEGG membership genes rechecked, Asta-backed, validated, and rendered; new boundary module seeded and validated; HisC/AroA/TyrB/AmaC treated as shared histidine, shikimate/chorismate, and aromatic-amino-acid enzymes rather than evidence for a complete novobiocin aminocoumarin antibiotic biosynthesis pathway; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete amino-acid boundary batch `ppu00410` / `beta_alanine_metabolism_boundary`: 15 KEGG membership genes rechecked, Asta-backed, validated, and rendered; new broad boundary module seeded and validated; pyrimidine-to-beta-alanine context, beta-alanine transamination, and PanC pantothenate ligation separated from methylmalonate-semialdehyde, aldehyde-dehydrogenase, fatty-acid beta-oxidation, phenylacetate, and acyl-CoA side nodes; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete sulfur/amino-acid boundary batch `ppu00430` / `taurine_hypotaurine_metabolism_boundary`: 5 KEGG membership genes fetched or rechecked, Asta-backed, validated, and rendered; new boundary module seeded and validated; TauD treated as the pathway-defining taurine/sulfonate dioxygenase, with Pta, GdhB, PP_3535, and Ggt kept as acetate, glutamate, and glutathione side context; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete phosphonate batch `ppu00440` / `phosphonate_phosphinate_metabolism`: 2 KEGG membership genes fetched or rechecked, Asta-backed, curated, validated, and rendered; compact PhnWX module seeded and later extended with the PP_0824-PP_0827 phosphonate ABC import sub-batch from `ppu02010` and the PP_1722-PP_1726 AEP/phosphonate ABC import candidate from `ppu02024`; PhnW/PhnX remain the AEP catabolic route and the transporter connections are recorded as uptake context with unresolved exact substrate handoff, not as broad C-P lyase or phosphinate metabolism; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete selenocompound boundary batch `ppu00450` / `selenocompound_metabolism_boundary`: 12 KEGG membership genes fetched or rechecked, Asta-backed, curated, validated, and rendered; new boundary module seeded and validated; SelD/SelA treated as the selenium-specific Sec-tRNA biosynthesis spine, with MetG, CysD/CysNC, MetB, MdeA, MetH, MetE, PP_4348, PP_4594, and PP_4637 kept as methionine, cysteine, sulfate-assimilation, translation, or candidate side context; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete cyanoamino-acid boundary batch `ppu00460` / `cyanoamino_acid_metabolism_boundary`: 7 KEGG membership genes fetched or rechecked, Asta-backed, curated, validated, and rendered; new boundary module seeded and validated; AnsA/PP_1160 treated as asparaginase-family anchors, with GlyA1/GlyA2, BglX, PP_3535, and Ggt kept as one-carbon, carbohydrate/glucan, or glutathione side context; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete D-amino-acid boundary batch `ppu00470` / `d_amino_acid_metabolism_boundary`: 21 KEGG membership genes fetched or rechecked, Asta-backed, curated, validated, and rendered; new boundary module seeded and validated; peptidoglycan D-Glu/D-Ala enzymes, D-amino-acid dehydrogenases/racemases, hydroxyproline/dioxovalerate side route, diaminopimelate/lysine biosynthesis, and asparaginase context kept separated; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete glutathione boundary batch `ppu00480` / `glutathione_metabolism_boundary`: 31 KEGG membership genes fetched or rechecked, Asta-backed, curated, validated, and rendered; new boundary module seeded and validated; glutathione biosynthesis/reductase/turnover nodes separated from GST/peroxidase detoxification, NADPH supply, aminopeptidase, allophanate/5-oxoproline, SpeC, and PtxD side context; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete carbohydrate/alpha-glucan boundary batch `ppu00500` / `starch_sucrose_metabolism_boundary`: 18 KEGG membership genes fetched or rechecked, Asta-backed, curated, validated, and rendered; new boundary module seeded and validated; bacterial glycogen/alpha-glucan and trehalose/GlgE-route genes separated from cellulose synthesis, shared UDP-glucose/sugar-phosphate precursor enzymes, and beta-glucosidase side context; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete amino-sugar/nucleotide-sugar boundary batch `ppu00520` / `amino_sugar_nucleotide_sugar_metabolism_boundary`: 25 KEGG membership genes fetched or rechecked, Asta-backed, curated, validated, and rendered; new boundary module seeded and validated; UDP-GlcNAc biosynthesis, de novo UDP-MurNAc/peptidoglycan precursor chemistry, MurNAc recycling, nucleotide-sugar side branches, alginate/GDP-mannose context, and shared sugar-phosphate enzymes kept separated; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete polyketide-sugar/deoxy-sugar boundary batch `ppu00523` / `polyketide_sugar_unit_biosynthesis_boundary`: 6 KEGG membership genes fetched or rechecked, Asta-backed, curated, validated, and rendered; new boundary/absence module seeded and validated; dTDP-rhamnose chemistry separated from unsupported complete polyketide natural-product glycosylation, with duplicate RmlC/RmlD-like paralog pairs kept as unresolved flux questions; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete acarbose/validamycin boundary batch `ppu00525` / `acarbose_validamycin_biosynthesis_boundary`: 2 KEGG membership genes rechecked, Asta-backed, validated, and rendered; new boundary/absence module seeded and validated; RfbA/RffG treated as shared dTDP-sugar precursor enzymes rather than evidence for complete acarbose, validamycin, or aminocyclitol antibiotic biosynthesis; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete LPS/lipid A batch `ppu00540` / `lipopolysaccharide_biosynthesis`: 20 KEGG membership genes fetched, Asta-backed, first-pass curated, validated, and rendered; new LPS module seeded and validated; lipid A precursor synthesis, Kdo2-lipid A/core bridge, LPS core assembly, and lipid A/LPS remodeling side nodes separated; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Partition functional cell-envelope/division bucket `module:cell_envelope_division`: 98 primary genes split into 11 curation-scale buckets spanning Lpt/LPS transport context, LPS-core/lipid-A candidates, peptidoglycan remodeling, cell-division regulatory spillovers, VacJ/MlaA context, ApbE-like flavinylation, outer-membrane barrels/channels/autotransporters, named outer-membrane lipoproteins, domain-resolved lipoproteins, and generic lipoprotein-signal spillovers; all 98 have review files and Asta coverage; LPS-core/lipid-A split complete with `PP_3016` and `PP_3134` added to the LPS module and `maa` routed out as maltose O-acetyltransferase; cell-division regulatory spillover split complete with `sulA`, `PP_2199`, and `PP_2352` added to the divisome/Z-ring boundary as regulatory or candidate ZapE-like context; VacJ/MlaA singleton complete with `vacJ` added to the Mla phospholipid-transport boundary; ApbE/FMNylylation singleton complete with `PP_2150` added to the Ccm/cytochrome-redox boundary as related envelope flavoprotein maturation context; peptidoglycan turnover/remodeling split complete with 11 genes added to the peptidoglycan module; outer-membrane barrel/channel/autotransporter, named-lipoprotein, domain-resolved lipoprotein, and generic lipoprotein/signal-peptide splits complete with 77 genes added to the transport/envelope spillover boundary.
- [x] Partition functional stress/detoxification bucket `module:stress_detoxification`: 52 primary genes split into 7 curation-scale buckets spanning peroxide/peroxiredoxin detoxification, glutathione/thiol detoxification, arsenic/copper resistance, universal stress proteins, cold/heat-shock proteins, ThiJ/DJ-1/PfpI candidates, and miscellaneous stress-regulatory spillovers; all 52 have review files, curated reviews, and Asta coverage. The splits are represented in `modules/oxidative_stress_peroxide_detoxification_boundary.yaml`, `modules/glutathione_metabolism_boundary.yaml`, `modules/metal_resistance_detoxification_boundary.yaml`, `modules/universal_stress_protein_boundary.yaml`, `modules/integrated_stress_response_boundary.yaml`, and `modules/stress_detoxification_spillover_boundary.yaml`.
- [x] Partition functional regulation/signal-transduction bucket `module:regulation_signal_transduction`: 387 primary genes split into 11 curation-scale regulator-family buckets spanning LysR, AraC/XylS, GntR, TetR/AcrR, small-family metabolic regulators, MerR/ArsR/MarR metal-redox-stress regulators, two-component sensors/response regulators, XRE/Cro/phage/toxin-antitoxin regulators, sigma-54 enhancer-binding regulators, and ECF/sigma/anti-sigma factors plus low-information/named regulatory spillovers. All 11 splits are complete: `small_family_metabolic_transcriptional_regulators` with 21/21 curated, Asta-backed reviews and validated `modules/metabolic_transcriptional_regulator_boundary.yaml`; `sigma_anti_sigma_and_sigma_factors` with 16/16 curated, Asta-backed reviews and validated `modules/sigma_anti_sigma_regulation_boundary.yaml`; `sigma54_enhancer_binding_regulators` with 16/16 curated, Asta-backed reviews and validated `modules/sigma54_enhancer_binding_regulator_boundary.yaml`; `tetr_acrr_transcriptional_regulators` with 25/25 curated, Asta-backed reviews and validated `modules/tetr_acrr_transcriptional_regulator_boundary.yaml`; `merr_arsr_marr_metal_redox_regulators` with 25/25 curated, Asta-backed reviews and validated `modules/metal_redox_stress_transcription_regulator_boundary.yaml`; `xre_cro_phage_toxin_antitoxin_regulators` with 28/28 curated, Asta-backed reviews and validated `modules/phage_regulation_toxin_antitoxin_boundary.yaml`; `gntr_transcriptional_regulators` with 29/29 curated, Asta-backed reviews and validated `modules/gntr_transcriptional_regulator_boundary.yaml`; `arac_xyls_transcriptional_regulators` with 40/40 curated or preserved, Asta-backed reviews and validated `modules/arac_xyls_transcriptional_regulator_boundary.yaml`; `low_information_or_named_transcriptional_regulators` with 32/32 fetched or preserved, Asta-backed reviews and validated `modules/transcriptional_regulator_spillover_boundary.yaml`; `two_component_sensors_response_regulators` with 48/48 fetched or preserved, Asta-backed reviews and validated `modules/orphan_two_component_regulators_boundary.yaml`; and `lysr_transcriptional_regulators` with 107/107 fetched or preserved, Asta-backed reviews and validated `modules/lysr_transcriptional_regulator_boundary.yaml`. The MerR/ArsR/MarR split keeps arsR1/arsR2 named arsenite regulatory context, soxR as redox-sensitive MerR-family context, generic paralogs as transcription-regulator candidates, and five weak no-GOA product-name-only records as no-core unresolved. The XRE/Cro/toxin-antitoxin split separates MqsRA/HigA, LexA-like, Cro/C1-cupin, simple Cro/C1, and non-phage regulatory spillovers, with PP_5680 retained as no-core unresolved. The GntR split separates FadR/GntR C-terminal, UTRA/HutC-like, and PLP/aminotransferase-domain regulators while leaving regulons, effectors, regulatory direction, and PLP-domain substrate chemistry unresolved. The AraC/XylS split preserves existing curated `ada` and `BenR` anchor reviews, adds 38 new Asta-backed regulator reviews, separates named, DJ-1/PfpI or INH-QAR, RmlC/cupin, arabinose-binding-domain, and other sensor-domain regulators, and leaves regulons, effectors, regulatory direction, and PP_4602 kinase side context unresolved unless gene-specific evidence supports them. The low-information/named split preserves HexR as a curated anchor, adds conservative missing regulator molecular-function rows where supported, and leaves PP_1762, PP_2738, PP_4528, PP_5232, and PP_5343 no-core unresolved. The two-component split preserves `colR` as the curated ColRS anchor, extends the orphan/generic TCS boundary with `colS`, generic histidine kinases, DNA-binding response regulators, and receiver-only/noncanonical regulators, and leaves cues, regulons, transporter outputs, and HD-GYP/cyclic-di-GMP activity unresolved unless supported as side context. The LysR split preserves `pcaQ`, `galR`, and `catR` as curated anchors, adds 104 new Asta-backed regulator reviews, treats direct pathway-process terms on regulator genes as pathway-association over-annotation unless gene-specific activation evidence supports the claim, and leaves regulons, effectors, and regulatory direction unresolved for generic paralogs.
- [x] Partition functional transport/membrane/efflux bucket `module:transport_membrane_efflux`: 779 primary genes split into 26 curation-scale buckets spanning Lpt/LPS transport context, TonB-ExbB-ExbD energy transduction, TonB-dependent receptors, protein export/secretion and outer-membrane assembly, RND tripartite efflux, MFS and DMT transporters, ABC transporter classes, ion/metal transporters and antiporters, non-ABC solute transporters, membrane redox/electron-transfer proteins, membrane signaling/channels/c-di-GMP spillovers, envelope-polysaccharide export/flippase context, stress-resistance membrane spillovers, membrane-associated enzyme side nodes, domain-resolved membrane proteins, and low-information membrane proteins. The partition ledger is `projects/P_PUTIDA/batches/module_transport_membrane_efflux_partition.tsv`.
- [x] Complete first transport/membrane/efflux sub-batch `tonb_exbb_exbd_energy_transduction`: 7 genes fetched or rechecked, Asta-backed, first-pass curated, validated, and represented in `modules/tonb_dependent_transport_boundary.yaml`; existing `exbB` and `tonB` anchors were preserved with added Asta provenance, `PP_0696` and `PP_1512` are TonB energy-transducer candidates, `PP_1898` is an ExbB/TolQ-like proton-channel candidate, `PP_1899` and `exbD` are ExbD/TolR-family energy-coupling candidates, and receptor partners/substrates remain unresolved as TonB-system pairing questions.
- [x] Complete second transport/membrane/efflux sub-batch `tonb_dependent_outer_membrane_receptors`: 30 genes fetched or rechecked, Asta-backed, first-pass curated, validated, and represented in the expanded `modules/tonb_dependent_transport_boundary.yaml`; existing `fpvA` was preserved with added Asta provenance, ferric-siderophore receptors were retained as siderophore/ferric-complex uptake receptors, CntO paralogs were shifted from siderophore-iron over-annotations toward pseudopaline-metal/nickel/zinc context, `PP_1006` was treated as heme receptor context, `PP_0525` as B12/cobalamin context, `oprC` as copper-receptor context, and generic TonB receptor paralogs were left ligand-unresolved with broad NEW transporter terms where needed.
- [x] Complete third transport/membrane/efflux sub-batch `protein_export_secretion_outer_membrane_assembly`: 15 genes fetched, Asta-backed, first-pass curated, validated, and represented in `modules/protein_export_secretion_outer_membrane_assembly_boundary.yaml`; BamA/B/D/E and the BamE-domain candidate were separated from LolA/LolB lipoprotein localization, Type-II/Type-V secretion components, SecYEG accessory context, prepilin peptidase context, and HlyD-family membrane-fusion candidates with unresolved cognate partners and substrates.
- [x] Complete fourth transport/membrane/efflux sub-batch `rnd_tripartite_efflux_and_mfp_omf_systems`: 42 genes fetched or rechecked, Asta-backed, first-pass curated, validated, and represented in the expanded `modules/rnd_multidrug_efflux_boundary.yaml`; Czc metal-efflux loci, Mex/Opr and generic RND systems, MFS/Emr/EamA side contexts, type-I secretion and TolC-like components, PvdR pyoverdine export, and FieF CDF metal efflux were separated while keeping MFP/OMF roles component-level unless stronger substrate or partner evidence is available.
- [x] Complete fifth transport/membrane/efflux sub-batch `mfs_drug_metabolite_transporters`: 80 genes fetched or rechecked, Asta-backed, first-pass curated, validated, and represented in `modules/mfs_drug_metabolite_transport_boundary.yaml`; named aromatic/carboxylate, alpha-ketoglutarate/symporter/compatible-solute, drug/xenobiotic efflux, sugar/cyanate, generic MFS, and PP_1700 acyltransferase side contexts were separated while keeping substrate, direction, and coupling calls conservative unless product, family, or prior evidence supports them.
- [x] Complete sixth transport/membrane/efflux sub-batch `dmt_eama_small_drug_metabolite_transporters`: 21 genes fetched, Asta-backed, first-pass curated, validated, and represented in `modules/dmt_eama_transport_boundary.yaml`; SugE/EmrE SMR-family efflux candidates, RarD-like EamA permeases, amino-acid/vitamin-associated EamA candidates, diverse-substrate candidates, and generic EamA/DMT membrane permeases were separated, with `emrE` choline/betaine TreeGrafter rows modified toward broader SMR-family efflux context.
- [x] Complete seventh transport/membrane/efflux sub-batch `outer_membrane_porins_channels_autotransporters`: 38 genes fetched or rechecked, Asta-backed, first-pass curated, validated, and represented by the extended `modules/transport_envelope_spillover_boundary.yaml`; OprD/Opd substrate-selective porins, OprB carbohydrate porins, GlpF/AqpZ channels, FadL fatty-acid porin context, EstP autotransporter esterase, TamA assembly context, and low-resolution porin/outer-membrane candidates were separated, with `pcaP` sphingoid-catabolism and `oprG` host-outer-membrane over-annotations corrected.
- [x] Complete eighth transport/membrane/efflux sub-batch `amino_acid_peptide_polyamine_abc_importers`: 15 genes fetched, Asta-backed, first-pass curated, validated, and represented in `modules/amino_acid_peptide_polyamine_abc_transport_boundary.yaml`; Glt/Gln-like permease/binding-protein pairs, arginine/amino-acid permeases, EhuB/EhuC/EhuD ectoine-family components, a branched-chain amino-acid membrane component, and the PP_4748-PP_4751 binding/permease/ATPase importer were separated, with `PP_5024` ion-channel rows modified toward ABC amino-acid importer context.
- [x] Complete ninth transport/membrane/efflux sub-batch `metal_siderophore_anion_abc_transporters`: 11 genes fetched, Asta-backed, first-pass curated, validated, and represented in `modules/metal_siderophore_anion_abc_transport_boundary.yaml`; PP_2416/PP_2417 iron-import context, PP_2592/PP_2593/fatD ferric-siderophore import, generic metal/phosphate ATPase and substrate-binding context, and PP_4688/PP_4689 heme/hemin import were separated, with non-siderophore-labeled siderophore-iron rows broadened.
- [x] Complete tenth transport/membrane/efflux sub-batch `sugar_nucleoside_abc_transporters`: singleton `PP_1030` fetched, Asta-backed, first-pass curated, validated, and represented in `modules/sugar_nucleoside_abc_transport_boundary.yaml`; kept as a low-resolution predicted sugar ABC ATPase with ATP hydrolysis as the conservative function and substrate, partner components, and localization unresolved.
- [x] Complete eleventh transport/membrane/efflux sub-batch `generic_abc_transporters`: 33 genes fetched, Asta-backed, first-pass curated, validated, and represented in `modules/generic_abc_transport_boundary.yaml`; MacB/ABC-3-like components, fused ABCB/type-I-exporter-like proteins, binding-protein-dependent importer pieces, sulfonate, amino-acid, cobalamin, heme/hemin spillovers, and non-ABC outliers (`PP_0386`, `PP_1737`, `PP_3213`, `rbbA`) were separated while keeping substrate and partner calls conservative.
- [x] Complete twelfth transport/membrane/efflux sub-batch `ion_metal_monovalent_cation_antiporters_potassium_systems`: 26 genes fetched or rechecked, Asta-backed, first-pass curated, validated, and represented in `modules/monovalent_cation_antiporter_boundary.yaml`; Trk/Kup potassium uptake, NhaA/NhaB/NhaP sodium/proton antiporters, Kef potassium/proton antiporters, Mrp multicomponent antiporter subunits, K/Na/Ca exchanger and potassium-channel candidates, and conservative NhaC-like/DASS-related side candidates were separated. The parent 102-gene ion/metal bucket is now subpartitioned in `projects/P_PUTIDA/batches/module_transport_membrane_efflux_ion_metal_partition.tsv`.
- [x] Complete thirteenth transport/membrane/efflux sub-batch `ion_metal_p_type_metal_atpases`: 5 genes fetched, Asta-backed, first-pass curated, validated, and represented in `modules/p_type_metal_atpase_transport_boundary.yaml`; CadA-family zinc/cadmium export ATPases, CadA-II copper export, MgtA magnesium import, and PP_4261 as an unresolved type-IB copper/cation ATPase candidate were separated.
- [x] Complete fourteenth transport/membrane/efflux sub-batch `ion_metal_chromate_fluoride_and_other_inorganic_channels`: 3 genes fetched, Asta-backed, first-pass curated, validated, and represented in `modules/inorganic_ion_channel_resistance_boundary.yaml`; PP_2556 CHR-family chromate transport, reviewed FluC fluoride channel/detoxification context, and PP_4986 HlyIII-family pore-forming candidate context were separated.
- [x] Complete fifteenth transport/membrane/efflux sub-batch `ion_metal_transition_metal_magnesium_cobalt_transporters`: 15 genes fetched, Asta-backed, first-pass curated, validated, and represented in `modules/transition_metal_magnesium_cobalt_transport_boundary.yaml`; CDF/ZIP zinc and mixed-metal transporters, CbiM/CbtA cobalt components, CorA/MgtE magnesium-cobalt transporters, NiCoT/Rcn nickel-cobalt efflux/response context, and CorC/CNNM-UPF0053 low-resolution metal-transporter candidates were separated.
- [x] Complete sixteenth transport/membrane/efflux sub-batch `ion_metal_sodium_solute_symporters_and_mate_efflux`: 14 genes fetched, Asta-backed, first-pass curated, validated, and represented in `modules/sodium_solute_symporter_mate_boundary.yaml`; AGCS amino-acid:sodium symport, GltS glutamate:sodium symport, ArcD arginine-ornithine antiport, ActP acetate transport, PutP sodium/proline symport, TcyP cystine transport, MATE xenobiotic efflux, broad SSF candidates, PP_3331 low-confidence symporter context, and PP_0670 ACR3 arsenite/antimonite context were separated.
- [x] Complete seventeenth transport/membrane/efflux sub-batch `ion_metal_membrane_metalloenzymes_and_envelope_side_nodes`: 14 genes fetched, Asta-backed, first-pass curated, validated, and represented in `modules/transport_membrane_enzyme_spillover_boundary.yaml`; membrane protease/metalloprotease context, lipid/cell-wall glycosylation side nodes, TamB envelope assembly context, and CopD/CycZ-like copper/cytochrome membrane side nodes were separated from ion-transport assertions.
- [x] Complete eighteenth transport/membrane/efflux sub-batch `ion_metal_membrane_redox_electron_transfer_spillovers`: 25 genes fetched or rechecked, Asta-backed, first-pass curated, validated, and represented in `modules/membrane_redox_electron_transfer_boundary.yaml`; c-type and b561 cytochromes, ferredoxin/iron-sulfur proteins, Ccm cytochrome-c maturation proteins, Hmp nitric-oxide detoxification, MsrQ protein-repair electron transfer, CumA/azurin copper-redox proteins, and the PP_0180 OFeT/FTR1-like ferrous-iron transporter were separated. All ion/metal sub-splits are now first-pass curated.
- [x] Complete nineteenth transport/membrane/efflux sub-batch `amino_acid_quaternary_amine_nucleobase_transporters`: 55 genes fetched or rechecked, Asta-backed, first-pass curated, validated, and represented in `modules/amino_acid_amine_nucleobase_transport_boundary.yaml`; GltP/YveA acidic-amino-acid symporters, APC/GabP amino-acid and amine permeases, LysE/Rht exporters, BCCT choline/betaine/carnitine transporters, NCS nucleobase/purine/xanthine/uracil permeases, Amt/Rh ammonium and urea channels, BrnQ/AzlC branched-chain transporters, PP_1060 glutamate synthase, PP_4226 Tre1-like side context, and PP_2721 low-confidence unresolved context were separated.
- [x] Complete twentieth transport/membrane/efflux sub-batch `carbohydrate_nucleoside_transporters`: 14 genes fetched, Asta-backed, first-pass curated, validated, and represented in `modules/carbohydrate_nucleoside_transport_boundary.yaml`; GntP-family gluconate transporters, CodB/cytosine and NCS1 nucleobase permeases, PnuC nicotinamide-riboside transport, PP_1740 beta-glucanase side context, PP_3142 membrane sugar-transferase side context, PP_3048 prophage structural context, and unresolved PP_0138 SpmB/Gate-domain membrane context were separated.
- [x] Complete twenty-first transport/membrane/efflux sub-batch `organic_acid_aromatic_anion_transporters`: 7 genes fetched, Asta-backed, first-pass curated, validated, and represented in `modules/organic_acid_aromatic_anion_transport_boundary.yaml`; CitMHS citrate transport, BenE benzoate transport, BhbP hydroxybutyrate/monocarboxylate context, PP_3247 unresolved bile-acid/Na+ symporter-family context, and LldP lactate/proton symport were separated, with BhbP gluconate specificity broadened.
- [x] Complete twenty-second transport/membrane/efflux sub-batch `inorganic_nutrient_transporters`: 13 genes fetched, Asta-backed, first-pass curated, validated, and represented in `modules/inorganic_nutrient_transport_boundary.yaml`; SulP/CysZ sulfate or organosulfate transporters, YjbB/PiT phosphate transport, ModR molybdate-responsive transcription regulation, NasS nitrate-binding side context, PhoU phosphate-transport accessory/regulatory context, and unresolved PP_5475 nitrite-transporter-name-only context were separated.
- [x] Complete twenty-third transport/membrane/efflux sub-batch `lipoprotein_envelope_accessory_spillovers`: 3 genes fetched, Asta-backed, first-pass curated, validated, and represented by an extension to `modules/transport_envelope_spillover_boundary.yaml`; PP_1501 unresolved product-name-only lipoprotein, PP_2304 PpiD PPIase/folding-chaperone, and csgG CsgG curli assembly/transport context were separated.
- [x] Complete twenty-fourth transport/membrane/efflux sub-batch `envelope_polysaccharide_export_and_flippase_context`: 13 genes fetched, Asta-backed, first-pass curated, validated, and represented in `modules/envelope_polysaccharide_export_boundary.yaml`; ArnT/GtrA and bactoprenol-linked glycan transfer context, Wzz/Wzy/O-antigen and polysaccharide export context, Wzy O-antigen polymerase, and peptidoglycan or unresolved transglycosylase side nodes were separated.
- [x] Complete twenty-fifth transport/membrane/efflux sub-batch `stress_resistance_membrane_spillovers`: 20 genes fetched, Asta-backed, first-pass curated, validated, and represented by an extension to `modules/stress_detoxification_spillover_boundary.yaml`; Pqi paraquat-response proteins, PP_1264 xenobiotic-efflux context, TerB toxic-stress context, holin/phage release side nodes, CidA/CidB holin-regulator context, and unresolved VasX/CptA/ToxA toxin-domain membrane side nodes were separated.
- [x] Complete twenty-sixth transport/membrane/efflux sub-batch `membrane_redox_electron_transfer_proteins`: 24 genes fetched or rechecked, Asta-backed, first-pass curated, validated, and represented by an extension to `modules/membrane_redox_electron_transfer_boundary.yaml`; DsbB/DsbD disulfide-redox proteins, thioredoxin/glutaredoxin redox proteins, Rnf/Nqr ion-translocating oxidoreductase subunits, ETF carriers, cytochrome bd oxidase context, qhnDH QH-AmDH context, Ccm/Cco cytochrome maturation/heme-handling context, PP_4236 DsbE/Lgt redox-lipoprotein context, and low-information membrane redox/enzyme side nodes were separated.
- [x] Complete twenty-seventh transport/membrane/efflux sub-batch `membrane_signaling_channels_c_di_gmp_spillovers`: 39 genes fetched or rechecked, Asta-backed, first-pass curated, validated, and represented by an extension to `modules/c_di_gmp_turnover_boundary.yaml`; GGDEF diguanylate cyclases, EAL cyclic-guanylate phosphodiesterases, low-confidence CSS/PsiE/GGDEF-EAL c-di-GMP candidates, MscS/MscL mechanosensitive channels, chloride/bestrophin channel candidates, FecR/ECF-sigma regulatory sensors, and low-information membrane signaling side nodes were separated.
- [x] Complete twenty-eighth transport/membrane/efflux sub-batch `membrane_associated_enzymes_and_side_nodes`: 42 genes fetched, Asta-backed, first-pass curated, validated, and represented by an extension to `modules/transport_membrane_enzyme_spillover_boundary.yaml`; membrane peptidase/protease side nodes, lipid oxidoreductases/hydroxylases, acyltransferases/lipid-transfer proteins, peptidoglycan/glycosyltransferase side nodes, kinase/phosphatase signaling proteins, sulfatase/hydrolase candidates, detoxification/sulfurtransferase side nodes, secreted/toxin-associated transferase or nuclease candidates, HflK/HflC FtsH-modulator context, and low-information membrane enzyme candidates were separated. PP_1695 transporter rows were marked over-annotated, PP_5219 substrate specificity was broadened, and PP_4560/PP_5293 product-name artifacts were not promoted to unsupported RNase or orotate functions.
- [x] Complete twenty-ninth transport/membrane/efflux sub-batch `other_domain_resolved_membrane_proteins`: 83 genes fetched, Asta-backed, first-pass curated, validated, and represented in new `modules/transport_membrane_domain_spillover_boundary.yaml`; TauE/TSUP, AI-2E/PerM, DctM/TRAP, CstA, MMPL, FUSC, and other broad transporter candidates were separated from isolated ABC permease/binding-protein side nodes, metal/TerC/GDT1/MgtC homeostasis proteins, envelope/cell-shape/curli/biofilm side nodes, cytosolic nucleic-acid/tRNA/transcription spillovers, NRPS/RHS/toxin side nodes, and low-information DoxX/SURF1/DedA/PAP2/MAPEG membrane-domain proteins.
- [x] Complete thirtieth transport/membrane/efflux sub-batch `low_information_membrane_proteins`: 67 genes fetched, Asta-backed, first-pass curated, validated, and represented in new `modules/low_information_membrane_protein_boundary.yaml`; clear low-information transporter candidates, ArsB arsenical pumps, the YfdC formate/nitrite transporter-family candidate, a TonB-domain energy-transducer singleton, envelope/outer-membrane/biofilm/toxin side nodes, and domain-only membrane proteins left unresolved were separated. This closes the queued transport/membrane/efflux split list.
- [x] Partition and close functional DNA replication/repair/recombination bucket `module:dna_replication_repair_recombination`: 93 primary genes split into 8 curation-scale buckets spanning DNA topology/topoisomerase proteins, replication accessory candidates, SOS/translesion/alkylation repair, repair helicase/recombination candidates, mobile-element recombinases/transposases, reverse transcriptases, nuclease/toxin side nodes, and architectural/RNA/protein-folding spillovers; all 93 have review files, curated reviews, and Asta coverage; represented by validated `modules/dna_topology_topoisomerase_boundary.yaml`, an extension to `modules/bacterial_dna_replication.yaml`, `modules/dna_damage_response_translesion_repair_boundary.yaml`, an extension to `modules/bacterial_homologous_recombination.yaml`, `modules/nuclease_dnase_boundary.yaml`, `modules/dna_bucket_architectural_rna_protein_spillover_boundary.yaml`, and `modules/mobile_genetic_elements_boundary.yaml`.
- [x] Close functional mobile genetic elements bucket `module:mobile_genetic_elements`: 89 primary genes split into 8 curation-scale buckets spanning GOA-supported transposases/integration proteins, domain-only or fragmentary transposase candidates, integrases, prophage structural/packaging proteins, phage DNA replication/processing, lysis/host-interaction proteins, regulatory/toxin-antitoxin candidates, and low-information prophage proteins. All eight splits are complete: 89/89 review folders present, 89/89 curated reviews, and 89/89 Asta reports; represented by `modules/mobile_genetic_elements_boundary.yaml`, `modules/phage_structural_packaging_boundary.yaml`, `modules/phage_lysis_host_interaction_boundary.yaml`, `modules/phage_regulation_toxin_antitoxin_boundary.yaml`, and `modules/phage_dna_replication_processing_boundary.yaml`, with low-information/name-only records retained as no-core unresolved context rather than forced into unsupported functions.
- [x] Close functional protein folding/targeting/turnover bucket `module:protein_folding_targeting_turnover`: 91 primary genes split into 9 curation-scale buckets spanning chaperones/foldases/co-chaperones, ATP-dependent proteolysis, cofactor and metal-protein maturation, envelope and cell-wall peptidase context, aminopeptidases, periplasmic/membrane/secreted protease quality control, repair spillovers, phage/mobile proteases, and low-information peptidase candidates. All nine splits are complete: 91/91 review folders present, 91/91 curated reviews, and 91/91 Asta reports; represented by validated `modules/bacterial_chaperone_protein_folding_boundary.yaml`, `modules/bacterial_atp_dependent_protein_turnover_boundary.yaml`, `modules/cofactor_metal_maturation_chaperone_boundary.yaml`, `modules/envelope_cell_wall_peptidase_inhibitor_boundary.yaml`, `modules/protein_turnover_peptide_processing_boundary.yaml`, `modules/envelope_protease_quality_control_boundary.yaml`, `modules/protein_turnover_peptidase_spillover_boundary.yaml`, an extension to `modules/dna_bucket_architectural_rna_protein_spillover_boundary.yaml`, and an extension to `modules/phage_structural_packaging_boundary.yaml`. No-core unresolved context is retained for `PP_1548`, `PP_4814`, `PP_2108`, `PP_5729`, `qmcA`, `PP_5455`, `PP_2447`, and `PP_2685`; the final low-information peptidase split keeps class-specific S1/S9A serine and clan AA aspartic protease calls where supported, generic PfpI/C39 peptidase calls where only broad family support exists, and avoids unsupported substrate/pathway assertions.
- [x] Complete nucleotide-sugar boundary batch `ppu00541` / `nucleotide_sugar_biosynthesis_boundary`: 26 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; ADP-heptose, Kdo/CMP-Kdo, dTDP-rhamnose, GDP/UDP sugar branches, and unresolved polysaccharide/redox side nodes separated; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete exopolysaccharide/alginate boundary batch `ppu00543` / `exopolysaccharide_biosynthesis_boundary`: 11 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; alginate polymerization, O-acetylation/modification, unresolved glycosyltransferase context, and serine O-acetyltransferase cysteine-biosynthesis spillovers separated; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete UniPathway alginate-biosynthesis boundary batch `UPA00286` / `alginate_biosynthesis_boundary`: 11/11 UniPathway members present, Asta-backed, curated, validated, and rendered; new trans-envelope alginate module seeded and validated; `algE` and `algK` Asta retrieval added this pass; members split across `ppu00051`, `ppu00543`, `ppu02020`, and UniPathway-only export/scaffold context consolidated without treating the set as a single enzyme-only route; Falcon generic and PSEPK-specific module reports failed with Edison HTTP 402 and remain queued for rerun.
- [x] Complete peptidoglycan batch `ppu00550` / `peptidoglycan_biosynthesis`: 24 KEGG/UniPathway-selected genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new peptidoglycan module seeded and validated; cytosolic Mur/Ddl precursor assembly, lipid carrier and lipid I/II assembly, MurJ flipping, SEDS polymerases, PBPs/transpeptidases, and carboxypeptidase/remodeling side nodes separated; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete teichoic-acid boundary batch `ppu00552` / `teichoic_acid_biosynthesis_boundary`: 2 KEGG membership genes rechecked, Asta-backed, validated, and rendered; new boundary/absence module seeded and validated; `wbpM` and `uppP` treated as unresolved envelope-polysaccharide context and shared undecaprenyl carrier recycling rather than evidence for complete teichoic-acid biosynthesis; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete glycerolipid boundary batch `ppu00561` / `glycerolipid_metabolism_boundary`: 12 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; PlsX/PlsY/PlsB/PlsC/PP_0058/DgkA lipid precursor chemistry separated from glycerol-entry and side-node enzymes; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete inositol-phosphate boundary batch `ppu00562` / `inositol_phosphate_metabolism_boundary`: 4 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary/absence module seeded and validated; SuhB inositol-monophosphatase/rrnTAC context separated from TpiA and MmsA side nodes; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete glycerophospholipid batch `ppu00564` / `glycerophospholipid_metabolism`: 23 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new broad module seeded and validated; phosphatidic-acid/CDP-DAG precursor chemistry, PG/cardiolipin, PS/PE/PC, glycerophosphodiester turnover, glycerol-3-phosphate supply, and ethanolamine side nodes kept separated; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete sulfoquinovose boundary batch `ppu00566` / `sulfoquinovose_metabolism_boundary`: 2 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary/absence module seeded and validated; `yihS` kept as an unresolved KEGG sulfoquinovose-isomerase versus UniProt/GOA mannose-isomerase specificity conflict, while `mdh` remains TCA malate-dehydrogenase side context; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete alpha-linolenic-acid boundary batch `ppu00592` / `alpha_linolenic_acid_metabolism_boundary`: 2 KEGG membership genes rechecked, Asta-backed, validated, and rendered; new boundary/absence module seeded and validated; both candidates are FadA-like thiolases supporting generic fatty-acid beta-oxidation rather than a complete alpha-linolenic-acid-specific pathway; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete pyruvate-metabolism boundary batch `ppu00620` / `pyruvate_metabolism_boundary`: 54 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new broad boundary module seeded and validated; direct pyruvate, lactate, glyoxalase, malate/oxaloacetate, pyruvate dehydrogenase/lipoate, acetate/acetyl-CoA, thiolase, and alcohol/aldehyde side nodes kept separated; Falcon module reports remain queued.
- [x] Complete dioxin-degradation boundary batch `ppu00621` / `dioxin_degradation_boundary`: 2 KEGG membership genes rechecked, Asta-backed, validated, and rendered; new boundary/absence module seeded and validated; `PP_1791` remains substrate-unresolved aldolase/synthase context and `PP_2504` is 2-hydroxymuconate/4-oxalocrotonate tautomerase side context rather than evidence for complete dioxin degradation; Falcon module reports remain queued.
- [x] Complete chloroalkane/chloroalkene boundary batch `ppu00625` / `chloroalkane_chloroalkene_degradation_boundary`: 5 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary/absence module seeded and validated; FdhA/FrmA formaldehyde detoxification and PedE/PedH/AdhP alcohol oxidation kept as side context rather than evidence for a complete chloroalkane/chloroalkene degradation route; Falcon module reports remain queued.
- [x] Complete naphthalene-degradation boundary batch `ppu00626` / `naphthalene_degradation_boundary`: 2 KEGG membership genes rechecked, Asta-backed, validated, and rendered; new boundary/absence module seeded and validated; `frmA` formaldehyde detoxification and `adhP` generic alcohol dehydrogenase kept as side context rather than evidence for a complete naphthalene degradation route; Falcon module reports remain queued.
- [x] Complete aminobenzoate-degradation boundary batch `ppu00627` / `aminobenzoate_degradation_boundary`: 12 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; gallate, ferulate/vanillate, nitroaromatic redox, UbiX/prenyl-FMN, Baeyer-Villiger monooxygenase, CoA-hydratase, and unresolved amidase side nodes kept separated rather than forced into one aminobenzoate route; Falcon module reports remain queued.
- [x] Complete glyoxylate/dicarboxylate boundary batch `ppu00630` / `glyoxylate_dicarboxylate_metabolism_boundary`: 62 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; glycolate/glyoxylate `GlcDEF`-`Gcl`-`Hyi`-`GlxR`, phosphoglycolate `PP_0416`, formate-dehydrogenase/Fdo and NDH side nodes, and overlap TCA/one-carbon/acyl-CoA context kept separated; Falcon module reports remain queued.
- [x] Complete nitrotoluene-degradation boundary batch `ppu00633` / `nitrotoluene_degradation_boundary`: 3 KEGG membership genes fetched, Asta-backed, first-pass curated, validated, and rendered; new boundary/absence module seeded and validated; `nfnB` nitroreductase-family context and `PP_2486`/`nemA` OYE/NADH-flavin oxidoreductase side nodes kept separated from any claim of complete nitrotoluene degradation; Falcon module reports remain queued.
- [x] Complete propanoate-metabolism boundary batch `ppu00640` / `propanoate_metabolism_boundary`: 33 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; Prp/methylcitrate propionyl-CoA assimilation, AcnB/PrpD/AcnA-II dehydratase/aconitase context, methylmalonate-semialdehyde/valine-thymine side routes, acetate/acyl-CoA activation, fatty-acid beta-oxidation, ACC, TCA/glyoxylate, and BCKDH/lipoamide overlap nodes kept separated; Falcon module reports remain queued.
- [x] Complete styrene-degradation boundary batch `ppu00643` / `styrene_degradation_boundary`: 5 KEGG membership genes rechecked, Asta-backed, validated, and rendered; new boundary/absence module seeded and validated; `peaE` phenylacetaldehyde dehydrogenase, `hmgA`/`hmgC`/`hmgB` homogentisate-route enzymes, and unresolved `PP_2932` amidase-family context kept separated from any claim of complete styrene degradation; Falcon module reports remain queued.
- [x] Complete butanoate-metabolism boundary batch `ppu00650` / `butanoate_metabolism_boundary`: 38 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; `bdhA`, `gbd`, `hbdH`, `phaA`/PhaC1, and `phaC`/PhaC2 treated as the primary short-chain redox and PHA-storage nodes, with succinate-semialdehyde/GABA, acetoacetate/acyl-CoA, beta-oxidation, phenylacetate/caprolactam, BCAA/acetolactate, and TCA genes kept as spillover context; Falcon module reports remain queued.
- [x] Complete C5-branched-dibasic-acid boundary batch `ppu00660` / `c5_branched_dibasic_acid_metabolism_boundary`: 10 KEGG membership genes rechecked, Asta-backed, validated, and rendered; new boundary module seeded and validated; AHAS/acetolactate and LeuCD/LeuB nodes tied back to branched-chain amino-acid biosynthesis, `galC` kept as gallate-catabolism aldolase context, and `sucD`/`sucC` kept as TCA succinyl-CoA ligase context; Falcon module reports remain queued.
- [x] Complete methane-metabolism boundary batch `ppu00680` / `methane_metabolism_boundary`: 30 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary/absence module seeded and validated; formaldehyde/formate detoxification and oxidation, folate/serine one-carbon chemistry, central-carbon/acetate side nodes, respiratory redox context, and PeaA amine-dehydrogenase context kept separated from any claim of complete methane oxidation or methanogenesis; Falcon module reports remain queued.
- [x] Complete Calvin-cycle carbon-fixation boundary batch `ppu00710` / `carbon_fixation_calvin_cycle_boundary`: 13 KEGG membership genes rechecked, Asta-backed, validated, and rendered; new boundary/absence module seeded and validated; non-oxidative PPP, lower EMP/gluconeogenesis, PEPC anaplerotic carbon fixation, MaeB malic-enzyme, and Mdh/TCA side nodes separated from any claim of a complete Calvin-Benson-Bassham cycle; Falcon module reports remain queued.
- [x] Complete biotin-metabolism boundary batch `ppu00780` / `biotin_metabolism_boundary`: 16 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; BioC/BioH pimelate precursor chemistry, BioF/BioA/BioD/BioB biotin biosynthesis, and BirA biotin ligase/repressor context separated from fatty-acid/SDR side nodes; Falcon module reports remain queued.
- [x] Complete lipoic-acid-metabolism boundary batch `ppu00785` / `lipoic_acid_metabolism_boundary`: 19 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; LipB/LipA endogenous protein lipoylation separated from pyruvate, 2-oxoglutarate, branched-chain 2-oxoacid, glycine-cleavage, acetoin-cleavage, and Lpd redox target context; Falcon module reports remain queued.
- [x] Complete porphyrin/tetrapyrrole boundary batch `ppu00860` / `porphyrin_metabolism_boundary`: 46 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; heme/protoporphyrin biosynthesis, heme O/A maturation, cobalamin/corrinoid biosynthesis, siroheme biosynthesis, heme oxygenase/utilization, bacterioferritin/iron storage, and unresolved HemX-family side nodes kept separated; Falcon module reports remain queued.
- [x] Complete UniPathway protoheme support batch `UPA00252` / `porphyrin_metabolism_boundary`: UniPathway-primary `PP_0189` fetched by accession alias, Asta-backed, curated, validated, and rendered; already-curated `hemH` retained as ferrochelatase context; existing porphyrin/tetrapyrrole boundary module extended with a late protoheme-support node; Falcon generic and PSEPK-specific module reports failed with Edison HTTP 402 and remain queued for rerun.
- [x] Complete PTS boundary batch `ppu02060` / `phosphotransferase_system_boundary`: 6 KEGG membership genes fetched or rechecked, Asta-backed, curated, validated, and rendered; new boundary module seeded and validated; `fruBKA` retained as the fructose-specific PTS uptake/catabolic-entry branch and `ptsH`/`ptsP`/`ptsN` retained as HPr/Ntr regulatory phosphorelay context, not a generic all-sugar PTS transport system; real Falcon module commands attempted and blocked by Edison HTTP 402.
- [x] Complete folate transport/metabolism boundary batch `ppu04981` / `folate_transport_metabolism_boundary`: 6 KEGG membership genes rechecked, Asta-backed, curated, validated, and rendered; new boundary module seeded and validated; GlyA1/GlyA2 retained as serine hydroxymethyltransferase one-carbon donors, FolA/Fau as folate cofactor maintenance/salvage, ThyA as folate-dependent dTMP synthesis, and MetH as 5-methyl-THF/cobalamin methionine-synthase context; no folate transporter is present in the KT2440 membership; real Falcon module commands attempted and blocked by Edison HTTP 402.
- [x] Complete base-excision-repair boundary batch `ppu03410` / `bacterial_base_excision_repair`: 14 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; Tag/AlkA/MPG/Ung/MutY/MutM/Nth retained as BER lesion-recognition/AP-site core, ExoIII-like PP_2707/xthA/PP_5292 as AP/ExoA processing candidates, PolA/LigA/LigB as repair synthesis and nick sealing, and RecJ as a shared repair-exonuclease side node; real Falcon module commands attempted and blocked by Edison HTTP 402.
- [x] Complete nucleotide-excision-repair boundary batch `ppu03420` / `bacterial_nucleotide_excision_repair`: 10 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; UvrA/UvrB/UvrC retained as the strict UvrABC NER core, Mfd as transcription-coupled repair input, UvrD/PolA/LigA/LigB as post-incision repair context, and PP_2839/PP_3087 as unresolved helicase/UvrA-like boundary nodes; real Falcon module commands attempted and blocked by Edison HTTP 402.
- [x] Complete mismatch-repair boundary batch `ppu03430` / `bacterial_mismatch_repair`: 19 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; MutS/MutL retained as the strict mismatch-recognition/coordination core, with UvrD, exonucleases, SSB, DNA polymerase III/clamp-loader/proofreading subunits, and ligases treated as shared repair/replication context; real Falcon module commands attempted and blocked by Edison HTTP 402.
- [x] Complete homologous-recombination boundary batch `ppu03440` / `bacterial_homologous_recombination`: 24 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; RecA/RecFOR, RecBCD, RuvABC, RecG, and PriA retained as the strict HR/restart core, with SSB, RecJ, PolA, DnaQ-like exonucleases, and Pol III replication-restart proteins treated as shared repair/replication context; real Falcon module commands attempted and blocked by Edison HTTP 402.
- [x] Complete DNA-repair batch `ppu03450` / `bacterial_non_homologous_end_joining`: 2 KEGG membership genes fetched, Asta-backed, first-pass curated, validated, and rendered; new compact Ku/LigD NHEJ module seeded and validated; broad DNA repair/recombination terms narrowed to double-strand-break repair via nonhomologous end joining, with LigD polymerase and exonuclease activities added from UniProt metadata; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete peroxisome boundary/absence batch `ppu04146` / `peroxisome_boundary`: 12 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary/absence module seeded and validated; catalases/SODs retained as cytoplasmic ROS detoxification, FadD/Icd/Idh/HMG-CoA lyase/NudC retained as bacterial side-node metabolism, and no peroxisome localization or peroxisome-biogenesis annotation proposed; real Falcon module commands attempted and blocked by Edison HTTP 402.
- [x] Complete boundary/absence batch `ppu03008` / `ribosome_biogenesis_eukaryotes_boundary`: 3 KEGG membership genes fetched or rechecked, Asta-backed, curated, validated, and rendered; new boundary module seeded and validated; `rnc` retained as RNase III/rRNA-processing context, `orn` retained as oligoribonuclease/RNA-fragment-turnover context, and `PP_2912` retained as RIO-type kinase-like context, not evidence for a eukaryotic ribosome-biogenesis pathway in KT2440; real Falcon module commands attempted and blocked by Edison HTTP 402.
- [x] Complete RNA-degradation boundary batch `ppu03018` / `bacterial_rna_degradation`: 17 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; RppH/RNase E/PcnB/PNPase/RNase R and DEAD-box helicases retained as the RNA-turnover core, Hfq/Rho kept as RNA-regulatory context, and enolase/chaperone/polyphosphate/RecQ members kept as side or spillover nodes; real Falcon module commands attempted and blocked by Edison HTTP 402.
- [x] Complete information-processing batch `ppu03020` / `bacterial_rna_polymerase_core`: 4 KEGG membership genes fetched by UniProt accession aliases, Asta-backed, first-pass curated, validated, and rendered; new compact RNAP core module seeded and validated; missing RNAP complex annotations added from UniProt metadata; omega treated as an assembly/contributing subunit rather than standalone catalytic enzyme; Falcon module reports remain queued while Edison Falcon access returns HTTP 402.
- [x] Complete DNA-replication boundary batch `ppu03030` / `bacterial_dna_replication`: 18 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; DnaB/DnaG primosome, SSB, Pol III core/clamp-loader/proofreading, RNase H/PolA primer processing, and LigA nick sealing retained as the strict replication story, with PP_3893, DnaQ-like exonuclease candidates, and LigB kept as unresolved boundary side nodes; real Falcon module commands attempted and blocked by Edison HTTP 402.
- [x] Complete protein-export boundary batch `ppu03060` / `bacterial_protein_export`: 19 KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; SecA/SecYEG/SecDF-YajC/SecB retained as Sec export machinery, Ffh/FtsY as SRP targeting, YidC as membrane insertase, LepB/LspA as signal peptidases, and two TatABC-like loci as twin-arginine export; type I secretion and LolCDE kept as neighboring modules; real Falcon module commands attempted and blocked by Edison HTTP 402.
- [x] Complete bacterial secretion-system boundary batch `ppu03070` / `bacterial_secretion_system_boundary`: 42 primary KEGG membership genes fetched or rechecked, Asta-backed, first-pass curated, validated, and rendered; new boundary module seeded and validated; Xcp/Gsp type-II secretion, PP_1449/PP_1450 two-partner/type Vb secretion, multiple T6SS loci/effectors, and PP_4926/CyaB type-I secretion context separated from the Sec/Tat/SRP/YidC ppu03060 protein-export module; real Falcon module commands attempted and blocked by Edison HTTP 402.
- [x] Partition two-component-system umbrella `ppu02020`: 99 primary genes split into 11 curation-scale buckets; `modules/two_component_relay.yaml` retained as a reusable motif rather than a PSEPK umbrella module; completed first-pass sub-buckets now include nutrient homeostasis, iron uptake regulation, osmotic/envelope/efflux regulation, alginate/biofilm regulation, ECF sigma/anti-sigma regulation, metal/copper response, pili/surface adhesion, Dct/Tct transport regulation, orphan/generic TCS regulation, and the `dnaA`/`etp` side-context spillovers; ppu02020 has 99/99 review files and Asta reports.
- [x] Partition quorum-sensing umbrella `ppu02024`: 60 primary genes split into 9 curation-scale buckets; no single LuxI/LuxR quorum-sensing module is represented by the primary PSEPK set; largest buckets are BCAA ABC import, polyamine ABC import, peptide/opine/glutathione ABC import, and QseBC-like two-component regulation.
- [x] Complete ppu02024-derived `rnd_multidrug_efflux_boundary` sub-batch: 2 genes fetched, Asta-backed, first-pass curated, validated, and rendered; new module created, validated, and rendered; PP_2064 treated as membrane-fusion/adaptor component contributing to pump-level efflux, and PP_2065 retained as the RND xenobiotic transporter.
- [x] Complete ppu02024-derived `qsebc_like_two_component_regulation_boundary` sub-batch: 5 genes fetched, Asta-backed, first-pass curated, validated, and rendered; new module created, validated, and rendered; PP_2714-PP_2713 and PP_4224-qseB treated as local sensor kinase/response regulator pairs, with kdpE retained as an unresolved KdpE-like side branch.
- [x] Complete ppu02024-derived `phosphonate_abc_import` sub-batch: 4 genes fetched, Asta-backed, first-pass curated, validated, and rendered; existing `phosphonate_phosphinate_metabolism` module extended, validated, and rendered; PP_1722-PP_1726 treated as a second AEP/phosphonate ABC import candidate with substrate range and direct PhnW handoff left as a knowledge gap.
- [x] Complete ppu02024-derived `peptide_opine_glutathione_abc_import_boundary` sub-batch: 8 genes fetched, Asta-backed, first-pass curated, validated, and rendered; new module created, validated, and rendered; PP_3220-PP_3223 treated as a dipeptide-like ABC importer and gsiA/PP_4454/gsiC/PP_4458 treated as a mixed Gsi/opine-like ABC import boundary with substrate range unresolved.
- [x] Complete ppu02024-derived `polyamine_abc_import` sub-batch: 13 genes fetched, Asta-backed, first-pass curated, validated, and rendered; existing `polyamine_transport_boundary` module extended, validated, and rendered; PP_0411-PP_0414, ydcV/ydcU/ydcT/ydcS, and PP_3814-PP_3817 treated as polyamine ABC import candidates, with PP_2870 retained as a binding-protein singleton.
- [x] Complete ppu02024 singleton side-contexts: `fur__Q88RL0`, `PP_0806`, and `PP_3609` fetched, Asta-backed, first-pass curated, validated, and rendered; new iron-homeostasis regulation, surface-adhesion, and DMT-transporter boundary modules created, validated, and rendered. ppu02024 is now 60/60 primary genes first-pass curated and remains a partitioned umbrella, not one satisfiable quorum-sensing module.
- [x] Partition biofilm-formation umbrella `ppu02025`: 43 primary genes split into 6 curation-scale buckets; the P. aeruginosa biofilm map mixes Gac/Csr/Crp regulation, Wsp-like chemotaxis/c-di-GMP signaling, c-di-GMP turnover, T6SS context, orphan regulatory sensors, and Pil/Chp twitching regulation.
- [x] Complete ppu02025-derived `wsp_surface_sensing_c_di_gmp_boundary` sub-batch: 6 Wsp-like cluster genes fetched, Asta-backed, first-pass curated, validated, and rendered; new module created, validated, and rendered with already curated `wspC` included as local cluster context; real Falcon module command attempted and blocked by Edison HTTP 402.
- [x] Complete ppu02025-derived `c_di_gmp_turnover_boundary` sub-batch: PP_0914, PP_3581, TpbB, and pde fetched or refreshed, Asta-backed, first-pass curated, validated, and rendered; new module created, validated, and rendered; PP_0914/PP_3581 retained as EAL c-di-GMP phosphodiesterase candidates, TpbB as a GGDEF diguanylate cyclase candidate, and pde only as broad cyclic-nucleotide phosphodiesterase side context; real Falcon module command attempted and blocked by Edison HTTP 402.
- [x] Complete ppu02025-derived `pil_chp_twitching_motility_boundary` sub-batch: PP_4987, PP_4988, pilJ, pilI, pilH, and pilG fetched, Asta-backed, first-pass curated, validated, and rendered; new module created, validated, and rendered; PP_4988 retained as the CheA-family histidine kinase, PP_4987/pilI as CheW-like adaptors, pilJ as a PilJ/MCP-like membrane transducer, and pilH/pilG as receiver-domain response-regulator candidates; real Falcon module command attempted and blocked by Edison HTTP 402.
- [x] Complete ppu02025-derived `global_biofilm_regulation_boundary` sub-batch: crp and three CsrA paralogs fetched, gacS/gacA Asta-backed, six reviews validated, and new global Gac/Csr/Crp regulatory module created, validated, and rendered; crp gets a new cAMP-binding call, the CsrA paralogs are retained as accession-scoped mRNA 5-prime UTR-binding post-transcriptional regulators, and uvrY is represented by the existing gacA folder; real Falcon module command attempted and blocked by Edison HTTP 402.
- [x] Complete ppu02025 T6SS/biofilm-context reuse batch: 13 T6SS apparatus/accessory genes fetched, Asta-backed, first-pass curated, validated, and wired into `modules/bacterial_secretion_system_boundary.yaml`; puuD/PP_3099 is treated as a likely TssC/VipB-family sheath protein and its EC-derived urate oxidase activity annotation is marked for removal.
- [x] Complete ppu02025-derived `orphan_biofilm_regulatory_sensors_boundary` sub-batch: PP_1875, PP_2664, PP_4173, PP_4362, PP_4363, PP_4364, PP_4781, and PP_4824/retS Asta-backed, first-pass curated, validated, and rendered; new module created, validated, and rendered; orphan histidine kinase/Hpt/SpoIIE/STAS entries are retained as unresolved regulatory-sensor context rather than direct per-gene biofilm-output assertions.
- [x] Partition bacterial-chemotaxis umbrella `ppu02030`: 41 primary genes split into 5 curation-scale buckets; the map mixes named MCP receptors, orphan MCP/aerotaxis receptors, core Che signal transduction, adaptation/accessory proteins, and periplasmic binding/transport spillovers.
- [x] Complete ppu02030-derived `bacterial_chemotaxis_core_boundary` sub-batch: 6 core Che-cluster genes present, Asta-backed, first-pass curated, validated, and rendered; new module created, validated, and rendered; CheW-like PP_4332/PP_4333 kept as adaptor/accessory candidates with CheW-specific MF gap noted.
- [x] Complete ppu02030-derived `chemotaxis_adaptation_accessory_boundary` sub-batch: 6 adaptation/accessory genes fetched, Asta-backed, first-pass curated, validated, and rendered; new module created, validated, and rendered; CheR2 retained as the chemotaxis receptor methyltransferase, CheR3 left as an unresolved broad methyltransferase candidate, and PP_3759 response-regulator over-propagation removed.
- [x] Complete ppu02030-derived `chemotaxis_receptor_panel_boundary` sub-batch: 9 named MCP receptor genes present, Asta-backed, first-pass curated, validated, and rendered; new module created, validated, and rendered; characterized receptor specificities retained for McpH, McpU, McpG, McpA, PcaY, McpP, McpS, and McpQ, while CtpL remains ligand-unresolved.
- [x] Complete ppu02030-derived `orphan_mcp_aerotaxis_receptors_boundary` sub-batch: 13 orphan MCP/aerotaxis receptor genes fetched, Asta-backed, first-pass curated, validated, and rendered; new boundary module created, validated, and rendered; generic MCP ligand specificity left unresolved, and PP_2111 SNARE-derived transport/fusion over-annotations removed.
- [x] Partition functional chromosome/cell-cycle bucket `module:chromosome_partition_cell_cycle`: 37 primary genes split into 6 curation-scale buckets; no single satisfiable module should cover the whole umbrella.
- [x] Complete `module:chromosome_partition_cell_cycle`-derived `min_system_septum_site_selection_boundary` sub-batch: `minC`, `minD`, and `minE` fetched, Asta-backed, first-pass curated, validated, and represented in a new validated MinCDE module; real Falcon module command attempted and blocked by Edison HTTP 402.
- [x] Complete `module:chromosome_partition_cell_cycle`-derived `divisome_z_ring_septation_boundary` sub-batch: 12 genes fetched or reused, Asta-backed, first-pass curated, validated, and represented in a new validated divisome/Z-ring module; PP_5202 septin-ring over-propagation removed; real Falcon module command attempted and blocked by Edison HTTP 402.
- [x] Complete `module:chromosome_partition_cell_cycle`-derived `chromosome_dimer_resolution_dna_translocation_boundary` sub-batch: `xerC`, `xerD`, `ftsK`, and `PP_2841` fetched, Asta-backed, first-pass curated, validated, and represented in a new validated Xer/FtsK chromosome dimer resolution module; `PP_2841` kept as an integrase-family boundary candidate; real Falcon module command attempted and blocked by Edison HTTP 402.
- [x] Complete `module:chromosome_partition_cell_cycle`-derived `tol_pal_cell_division_envelope_coordination_boundary` sub-batch: `tolQ`, `tolR`, `tolB`, `pal`, and `cpoB` plus promoted hole-filling `tolA` fetched or reused, Asta-backed, first-pass curated, validated, and represented in a new validated Tol-Pal envelope/division module; `tolA` chromatin/nucleosome spillovers removed; real Falcon module command attempted and blocked by Edison HTTP 402.
- [x] Complete `module:chromosome_partition_cell_cycle`-derived `chromosome_partition_condensation_boundary` sub-batch: `parB`, `PP_0693`, `PP_0694`, `PP_2161`, `PP_2412`, `PP_3700`, `smc`, `PP_4334`, `PP_4497`, `scpA`, and `PP_5070` plus promoted hole-filling `PP_0002` fetched, Asta-backed, first-pass curated, validated, and represented in a new validated chromosome partition/condensation boundary module; `parB` sporulation spillover removed, `smc` sister-chromatid cohesion modified toward bacterial chromosome organization/condensation, and unresolved ParA-family candidates kept provisional.
- [x] Close `module:chromosome_partition_cell_cycle` broad spillovers: `PP_1105` and `tig` fetched or reused, Asta-backed, first-pass curated, validated, and intentionally routed out of chromosome/cell-cycle modules; `PP_1105` kept as ATP-dependent DNA ligase/DNA repair context, and `tig` kept as trigger-factor cotranslational protein-folding context.
- [x] Partition functional motility/chemotaxis/biofilm bucket `module:motility_chemotaxis_biofilm`: 35 primary genes split into 11 curation-scale buckets spanning type IV pilus biogenesis, fimbrial/type-I-pilus extension, Hcp/T6SS product-name spillover, alginate envelope/lyase context, orphan MCPs, sensory c-di-GMP phosphodiesterase spillover, DNA-binding response-regulator spillover, CheY-like/membrane accessory spillovers, outer-membrane flagellation-name spillover, flagellar export/localization/accessory spillovers, and c-di-GMP flagellar brake context.
- [x] Complete `module:motility_chemotaxis_biofilm` type IV pilus biogenesis sub-batch: 12 genes fetched, Asta-backed, first-pass curated, validated, rendered, and represented in new `modules/type_iv_pilus_biogenesis_boundary.yaml`; `pilD` and `pilT` retained as explicit hole-filling gaps; real Falcon module command attempted and blocked by Edison HTTP 402.
- [x] Complete first `module:motility_chemotaxis_biofilm` sub-batches: `PP_1888` and `fimI` fetched, Asta-backed, first-pass curated, validated, and wired into `modules/pili_surface_adhesion_boundary.yaml`; `PP_0655` fetched, Asta-backed, validated, and routed to `modules/bacterial_secretion_system_boundary.yaml` as an Hcp/T6SS-family product-name spillover; real Falcon module command for `pili_surface_adhesion_boundary` attempted and blocked by Edison HTTP 402.
- [x] Complete `module:motility_chemotaxis_biofilm` alginate envelope/export and lyase context sub-batch: `glmP`, `PP_1754`, `PP_3350`, `PP_3464`, and `PP_3774` fetched, Asta-backed, first-pass curated, validated, rendered, and wired into `modules/alginate_biosynthesis_boundary.yaml`.
- [x] Complete `module:motility_chemotaxis_biofilm` orphan MCP/c-di-GMP split: `PP_2310`, `PP_3950`, and `PP_4888` fetched, Asta-backed, first-pass curated, validated, rendered, and wired into `modules/orphan_mcp_aerotaxis_receptors_boundary.yaml`; `PP_2599` fetched, Asta-backed, curated as a sensory HD-GYP/HD-PDEase cyclic-guanylate phosphodiesterase candidate, validated, rendered, and routed to `modules/c_di_gmp_turnover_boundary.yaml`.
- [x] Complete `module:motility_chemotaxis_biofilm` chemotaxis accessory/response-regulator split: `PP_2403`, `PP_3757`, `PP_3771`, and `PP_4331` fetched, Asta-backed, first-pass curated, validated, and wired into boundary modules; `PP_2403` routes to `modules/orphan_two_component_regulators_boundary.yaml` as an OmpR/PhoB-family DNA-binding response regulator, while `PP_3757`, `PP_3771`, and `PP_4331` extend `modules/chemotaxis_adaptation_accessory_boundary.yaml` as one compact CheY-like candidate and two conservative membrane accessory candidates.
- [x] Complete `module:motility_chemotaxis_biofilm` final flagellar spillover split: `ycfJ`, `PP_4328`, `PP_4329`, `PP_4342`, `flhF`, `PP_4377`, and `ycgR` fetched, Asta-backed, first-pass curated, validated, and wired into boundary modules; `ycfJ` routes to `modules/transport_envelope_spillover_boundary.yaml`, `PP_4328`/`PP_4329`/`PP_4342`/`flhF`/`PP_4377` extend `modules/flagellar_export_assembly_boundary.yaml`, and `ycgR` extends `modules/flagellar_motor_switch_stator_boundary.yaml`.
- [x] Partition flagellar-assembly pathway `ppu02040`: 47 primary genes split into 5 curation-scale buckets; the map is biologically coherent but should be curated as regulation, export/assembly, basal-body/hook/filament, motor/switch/stator, and nonflagellar spillover sub-batches.
- [x] Complete ppu02040-derived `flagellar_motor_switch_stator_boundary` sub-batch: 9 motor/switch/stator genes present, Asta-backed, first-pass curated, validated, and rendered; new module created, validated, and rendered; PP_4335/PP_4336 treated as MotD/MotC aliases for the MotCD stator, and FliL paralog roles remain unresolved.
- [x] Complete ppu02040-derived `flagellar_export_assembly_boundary` sub-batch: 14 export/assembly/chaperone genes fetched, Asta-backed, first-pass curated, validated, and rendered; new module created, validated, and rendered; FliI retained as the export ATPase, FlhA/FlhB/FliPQR as the membrane export gate, FliK as hook-length control, and FlgA/PP_4396/FliS/FliT as assembly-support factors.
- [x] Complete ppu02040-derived `flagellar_basal_body_hook_filament_boundary` sub-batch: 15 basal-body/hook/filament genes present, Asta-backed, first-pass curated, validated, and rendered; new module created, validated, and rendered; FliF/FliE retained as MS-ring/early basal-body components, FlgB/C/F/G as rod components, FlgJ as periplasmic peptidoglycan hydrolase, FlgI/FlgH as P/L rings, FlgE/FlgK/FlgL as hook/junction, and FliC/FliD as filament/cap.
- [x] Complete ppu02040-derived `flagellar_regulation_boundary` sub-batch: 6 sigma/master regulator genes present, Asta-backed, first-pass curated, validated, and rendered; new module created, validated, and rendered; RpoD kept as broad housekeeping sigma context, RpoN/FleQ/AtoC as sigma-54-associated regulatory context, FliA as sigma-28 late-output regulator, and FlgM as the anti-sigma checkpoint.
- [x] Complete ppu02040-derived `transport_envelope_spillover_boundary` bucket: 3 nonflagellar transport/envelope genes present, Asta-backed, first-pass curated, validated, and rendered; boundary module created, validated, and rendered; `fliY`, `PP_1087`, and `PP_5157` kept outside the flagellar apparatus core.
- [x] Complete ppu02040 first-pass partition: all 47 primary genes have review folders, curated reviews, Asta reports, and rendered pages; all 5 partition buckets have validated/rendered modules or boundary modules.
- [x] Partition ribosome pathway `ppu03010`: 54 primary genes split into 30S small-subunit and 50S large-subunit batches; no unknown/spillover bucket was needed because every primary member is a ribosomal protein.
- [x] Complete ppu03010-derived `bacterial_30s_ribosomal_subunit_boundary` sub-batch: 21 small-subunit ribosomal-protein genes present, Asta-backed, first-pass curated, validated, and rendered; new module created, validated, and rendered; specific small-subunit GOA component terms are retained in `existing_annotations`, while authored core-function locations use only schema-accepted location terms.
- [x] Complete ppu03010-derived `bacterial_50s_ribosomal_subunit_boundary` sub-batch: 33 large-subunit ribosomal-protein genes present, Asta-backed, first-pass curated, validated, and rendered; new module created, validated, and rendered; generic transferase activity on `rplB` marked as over-annotated, `rpmA` preribosome-precursor assembly modified toward ribosomal large-subunit assembly, and zinc/autoregulation/ribosome-binding terms kept as non-core where appropriate.
- [x] Complete ppu03010 first-pass partition: all 54 primary ribosomal-protein genes have review folders, curated reviews, Asta reports, and rendered pages; both 30S and 50S partition buckets have validated/rendered modules.
- [x] Partition sulfur-relay pathway `ppu04122`: 19 primary genes split into 4 buckets; the map mixes molybdopterin/MoCo sulfur-carrier chemistry, Tus/MnmA tRNA thiolation, ThiS thiamine sulfur-carrier context, and general rhodanese/mercaptopyruvate sulfurtransferase side nodes.
- [x] Complete ppu04122-derived `mnma_tus_trna_thiolation_boundary` sub-batch: 7 genes fetched, Asta-backed, first-pass curated, validated, and rendered; new module created, validated, and rendered; `tusA-I` and `PP_3994` remain core-function/module-gap recommendations because their fetched GOA tables are empty and validator policy rejects synthetic non-GOA `existing_annotations`.
- [x] Complete ppu04122-derived `molybdopterin_biosynthesis_sulfur_relay_boundary` sub-batch: 9 genes present, Asta-backed, first-pass curated, and validated; `moeB` and `moaD` fetched, researched, curated, and rendered; new module created, validated, and rendered; ppu04122 now has 19/19 primary review folders and 19/19 Asta reports.
- [x] Complete boundary/absence batch `ppu03250` / `viral_life_cycle_hiv1_boundary`: 1 KEGG membership gene already fetched, Asta-backed, curated, validated, and rendered; new boundary module seeded and validated; `ppiA` retained as cyclophilin-family peptidyl-prolyl cis-trans isomerase/protein-folding context, not evidence for an HIV-1 or viral life-cycle pathway in KT2440; real Falcon module commands attempted and blocked by Edison HTTP 402.
- [x] Complete boundary/absence batch `ppu04141` / `protein_processing_er_boundary`: 3 KEGG membership genes fetched or rechecked, Asta-backed, curated, validated, and rendered; new boundary module seeded and validated; `PP_3234` and `PP_3312` retained as HSP20-family small heat shock protein/unfolded-protein-binding context and `htpG` retained as bacterial Hsp90-family ATP-dependent chaperone context, not evidence for endoplasmic-reticulum protein processing in KT2440; real Falcon module commands attempted and blocked by Edison HTTP 402.
- [x] Complete boundary/absence batch `ppu04148` / `efferocytosis_boundary`: 2 KEGG membership genes already fetched, Asta-backed, curated, validated, and rendered; new boundary module seeded and validated; `speC` retained as ornithine decarboxylase/polyamine context and `petA` retained as respiratory complex III context, not evidence for eukaryotic efferocytosis in KT2440; real Falcon module commands attempted and blocked by Edison HTTP 402.
- [x] Complete boundary/absence batch `ppu04156` / `integrated_stress_response_boundary`: 4 KEGG membership genes rechecked, Asta-backed, curated, validated, and rendered; new boundary module seeded and validated; `groEL`, `dnaK`, and `htpG` retained as bacterial cytosolic chaperone/proteostasis context and `PP_5211` retained as glutathione gamma-glutamylcyclotransferase context, not evidence for eukaryotic integrated stress response signaling in KT2440; real Falcon module commands attempted and blocked by Edison HTTP 402.
- [x] Complete boundary batch `ppu04980` / `cobalamin_transport_metabolism_boundary`: 2 KEGG membership genes already fetched, Asta-backed, curated, validated, and rendered; new boundary module seeded and validated; `pduO` retained as corrinoid/cobalamin adenosyltransferase context and `metH` retained as B12-dependent methionine synthase/methionine-biosynthesis context, not evidence for a complete cobalamin transport pathway in KT2440; real Falcon module commands attempted and blocked by Edison HTTP 402.
- [ ] For each later module batch, full `fetch-gene` only the genes selected by module review.
- [ ] Track module satisfiability gaps, over-annotations, missing GO terms, and candidate new module documents.

# NOTES

## 2026-07-11

Completed the tenth regulation/signal-transduction split,
`two_component_sensors_response_regulators`. The 47 missing review folders were
fetched, Asta was generated for all 48 split members including the existing
curated `colR` anchor, and all 48 gene reviews validate. The existing
`modules/orphan_two_component_regulators_boundary.yaml` was extended rather than
replaced, preserving its ppu02020/motility-derived orphan TCS content and adding
four regulation-bucket parts: ColRS, generic histidine kinases, DNA-binding
response regulators, and receiver-only/noncanonical response regulators. The
pass keeps transporter-like regions, PP_2942 HD-GYP phosphodiesterase context,
osmosensory labels, ATP/nucleotide binding, and localization rows non-core or
over-annotated unless gene-specific evidence supports a pathway-level claim.

Completed the eleventh and final regulation/signal-transduction split,
`lysr_transcriptional_regulators`. The 104 missing review folders were fetched,
Asta was generated for all 107 split members including existing curated
`pcaQ`, `galR`, and `catR` anchors, and all 107 gene reviews validate. The new
`modules/lysr_transcriptional_regulator_boundary.yaml` validates and separates
named/pathway-associated LysR regulators, named side-context regulators, and
generic LysR-family transcription regulators. The pass treats direct metabolic
pathway-process annotations on regulator genes as pathway-association
over-annotation unless a gene-specific review supports positive transcriptional
activation, and leaves regulons, effectors, and regulatory direction unresolved
for generic paralogs. The regulation/signal-transduction bucket is now fully
first-pass curated across all 11 split rows.

Partitioned the open `module:transport_membrane_efflux` umbrella. The 779
primary genes are now split into 26 curation-scale rows covering TonB-dependent
uptake, RND/MFS/DMT/ABC transport families, ion/metal transporters, non-ABC
solute transporters, protein export/secretion, outer-membrane receptors and
porins, membrane redox proteins, envelope-polysaccharide export context,
stress-resistance membrane spillovers, and low-information membrane proteins.
As the first transport sub-batch, completed
`tonb_exbb_exbd_energy_transduction`: fetched five missing review folders,
generated Asta for all seven genes, preserved the existing `exbB` and `tonB`
anchors with added Asta provenance, curated the five new reviews, and created
validated `modules/tonb_dependent_transport_boundary.yaml`.

Completed the second transport sub-batch,
`tonb_dependent_outer_membrane_receptors`: fetched the 29 missing receptor
review folders, generated Asta for all 30 genes including the preserved `fpvA`
anchor, curated the 29 initialized reviews, added Asta provenance to `fpvA`,
and expanded/validated `modules/tonb_dependent_transport_boundary.yaml` with a
30-gene receptor panel. Main decisions: ferric-siderophore/FecA/FpvA-like
receptors retain siderophore/ferric-complex uptake terms; CntO paralogs are
treated as pseudopaline-metal/nickel/zinc receptor context rather than
ferric-siderophore-specific core function; `PP_1006`, `PP_0525`, and `oprC`
are separated as heme, B12/cobalamin, and copper-receptor context; and generic
TonB receptor paralogs keep ligand specificity unresolved with broad transporter
NEW rows where the core term was not present in GOA.

Completed the third transport sub-batch,
`protein_export_secretion_outer_membrane_assembly`: fetched all 15 missing
review folders, generated Asta for all 15 genes, curated and validated every
review, and created validated
`modules/protein_export_secretion_outer_membrane_assembly_boundary.yaml`. Main
decisions: BamA/B/D/E are core BAM outer-membrane assembly factors, `PP_5038` is
a BamE-domain assembly candidate without a full BAM-complex claim, LolA/LolB are
kept as lipoprotein-localization factors, `PP_0607` and `PP_0573` are Type-II and
Type-V secretion side components, `PP_0575` is a prepilin/type-IV endopeptidase
candidate, `PP_0855` is SecYEG accessory context, and HlyD-family MFP candidates
are retained as broad transport/efflux-complex components with partners and
substrates unresolved.

Completed the fourth transport sub-batch,
`rnd_tripartite_efflux_and_mfp_omf_systems`: fetched or rechecked all 42
review folders, generated Asta for every member, curated and validated every
review, patched Asta provenance into the existing `tolC` anchor, and expanded
validated `modules/rnd_multidrug_efflux_boundary.yaml`. Main decisions: CzcA/B/C
paralogous loci are treated as cation/metal-efflux tripartite systems rather
than generic xenobiotic pumps; MexC/MexD/OprJ, MexF/OprN with PP_3425, and the
PP_3299/PP_3301/PP_3302 locus are retained as RND efflux systems with substrate
specificity kept conservative; MFS/Emr/EamA candidates are kept as adjacent
non-RND efflux context; type-I secretion and TolC-like OMF/MFP proteins are
component-level contributors; `pvdR` is pyoverdine export membrane-fusion
context; and `fieF` is a CDF metal/cation efflux transporter.

Completed the fifth transport sub-batch,
`mfs_drug_metabolite_transporters`: fetched 78 missing review folders,
generated Asta for all 80 genes including the existing `pcaK` and `nicT`
anchors, preserved those anchors with added Asta provenance, curated and
validated every review, and created validated
`modules/mfs_drug_metabolite_transport_boundary.yaml`. Main decisions: named
aromatic/carboxylate transporters such as `pcaK`, `benK`, and `mhpT` are
separated from alpha-ketoglutarate/symporter/compatible-solute context,
Bcr/CmlA/EmrB/QacA/fosmidomycin efflux, sugar/cyanate candidates, and
low-resolution generic MFS proteins; `PP_1700` is retained as a membrane
acyltransferase side node; and TreeGrafter lactose, sodium, and hexuronate
substrate-specific rows were corrected or treated as over-annotations where
they exceeded the supported product/family evidence.

Completed the sixth transport sub-batch,
`dmt_eama_small_drug_metabolite_transporters`: fetched all 21 missing review
folders, generated Asta for every member, curated and validated every review,
and created validated `modules/dmt_eama_transport_boundary.yaml`. Main
decisions: `sugE` and `emrE` are SMR-family efflux candidates; RarD-like,
AA/vitamin-associated, diverse-substrate, and generic EamA/DMT proteins keep
broad transporter terms unless product/family evidence supports a stronger
claim; `PP_3776` had no GOA rows and was given conservative NEW membrane,
transmembrane-transporter, and transmembrane-transport rows; and `emrE`
TreeGrafter choline/betaine rows were modified toward broader SMR-family
xenobiotic/drug efflux context.

Completed the seventh transport sub-batch,
`outer_membrane_porins_channels_autotransporters`: fetched 33 missing review
folders, generated Asta for all 38 members including the preserved `oprE`,
`oprF`, `galP`, `nicP`, and `aqpZ` anchors, curated and validated all reviews,
and extended validated `modules/transport_envelope_spillover_boundary.yaml`.
Main decisions: OprD/Opd-family porins retain broad porin/transmembrane
transport unless product names support substrate context; OprB paralogs retain
carbohydrate transport; `glpF` and `aqpZ` are glycerol and water channels;
`PP_1689` is FadL/OmpP1-family long-chain fatty-acid porin context; `estP` is
an outer-membrane autotransporter carboxylesterase/acyl-CoA hydrolase; `PP_2892`
is TamA/TAM autotransporter-assembly context; `pcaP` sphingoid catabolism was
removed; and `oprG` host-outer-membrane context was modified to bacterial
outer-membrane localization.

Completed the eighth transport sub-batch,
`amino_acid_peptide_polyamine_abc_importers`: fetched all 15 missing review
folders, generated Asta for every member, curated and validated all reviews,
and created validated
`modules/amino_acid_peptide_polyamine_abc_transport_boundary.yaml`. Main
decisions: permeases are treated as inner-membrane ABC importer components,
periplasmic binding proteins as cell-envelope substrate-binding contributors,
and `PP_4751` as the ATP-hydrolyzing energy-coupling component; `PP_4428`
retains EhuB-family ectoine-binding/transport context; `PP_2384` is a
branched-chain amino-acid ABC membrane-component candidate; and `PP_5024`
ligand-gated ion-channel/ion-transport rows were modified toward ABC
amino-acid importer context.

Completed the ninth transport sub-batch,
`metal_siderophore_anion_abc_transporters`: fetched all 11 missing review
folders, generated Asta for every member, curated and validated all reviews,
and created validated `modules/metal_siderophore_anion_abc_transport_boundary.yaml`.
Main decisions: PP_2416/PP_2417 are kept as broad iron ABC ATPase/permease
context; PP_2592/PP_2593/fatD retain ferric-siderophore/FatD import context;
PP_2731, PP_2821, PP_3804, and PP_4933 remain low-resolution metal/phosphate
ATPase or substrate-binding context; PP_4688/PP_4689 are heme/hemin permease and
binding components; and siderophore-iron import rows on PP_2417 and PP_4688 were
broadened where the product did not support a siderophore-specific claim.

Completed the tenth transport sub-batch, `sugar_nucleoside_abc_transporters`.
The singleton `PP_1030` review folder was fetched, Asta was generated, and the
review/module validate. The only supported function retained is ATP hydrolysis
for a predicted sugar ABC transporter ATPase; no specific sugar, nucleoside,
partner permease/substrate-binding protein, complex membership, or localization
is asserted from the current low-information UniProt metadata.

Completed the eleventh transport sub-batch, `generic_abc_transporters`: fetched
all 33 missing review folders, generated Asta for every member, curated and
validated all reviews warning-free, and created validated
`modules/generic_abc_transport_boundary.yaml`. The split is a residual boundary,
not a single pathway: it separates MacB/ABC-3-like efflux or export components,
fused ABCB/type-I-exporter-like proteins, binding-protein-dependent importer
pieces, a PP_3635-PP_3637 sulfonate ABC-importer candidate, amino-acid ATPase
spillovers (`PP_3597`, `PP_4425`, `glnQ`), `hmuV` heme/hemin ATPase context,
and non-ABC outliers including `PP_0386` c-di-GMP phosphodiesterase, `PP_1737`
MlaA-family phospholipid transfer, `PP_3213` THI5-like thiamine-biosynthesis
context, and `rbbA` ribosome-associated ATPase.

Subpartitioned the 102-gene transport ion/metal parent bucket and completed the
first 26-gene sub-batch, `ion_metal_monovalent_cation_antiporters_potassium_systems`.
All members were fetched or rechecked, Asta-backed, first-pass curated,
validated, and represented in
`modules/monovalent_cation_antiporter_boundary.yaml`. The module separates
Trk/Kup potassium uptake, NhaA/NhaB/NhaP sodium/proton antiporters, Kef
potassium/proton antiporters, Mrp multicomponent antiporter subunits, PP_0928
K/Na/Ca exchanger context, PP_4304 and PP_3293 potassium-channel candidates,
and conservative side calls for PP_3556 (NhaC-like sodium/proton antiporter
candidate) and yfbS (DASS-related symporter candidate rather than potassium
channel regulator). Remaining ion/metal sub-splits cover P-type metal ATPases,
transition-metal/Mg/Co transporters, chromate/fluoride/inorganic channels,
sodium-solute/MATE systems, membrane redox spillovers, and membrane
metalloenzyme/envelope side nodes.

Completed two additional ion/metal sub-splits. The 5-gene
`ion_metal_p_type_metal_atpases` batch was fetched, Asta-backed, curated,
validated, and represented in
`modules/p_type_metal_atpase_transport_boundary.yaml`, separating CadA-family
zinc/cadmium export ATPases, CadA-II copper export, MgtA magnesium import, and
PP_4261 as an unresolved type-IB copper/cation ATPase candidate. The 3-gene
`ion_metal_chromate_fluoride_and_other_inorganic_channels` batch was also
fetched, Asta-backed, curated, validated, and represented in
`modules/inorganic_ion_channel_resistance_boundary.yaml`, separating PP_2556
CHR-family chromate transport, reviewed FluC fluoride channel/detoxification,
and PP_4986 as an HlyIII-family pore-forming candidate with unresolved
physiological substrate. Remaining ion/metal sub-splits are transition-metal/
Mg/Co transporters, sodium-solute/MATE systems, membrane redox spillovers, and
membrane metalloenzyme/envelope side nodes.

Completed the 15-gene
`ion_metal_transition_metal_magnesium_cobalt_transporters` sub-split: all
members were fetched, Asta-backed, first-pass curated, validated, and represented
in `modules/transition_metal_magnesium_cobalt_transport_boundary.yaml`. The
module separates CDF/ZIP zinc and mixed-metal transporters (`PP_0026`,
`PP_0947`, `PP_1227`, `PP_1836`), CbiM/CbtA cobalt transporter components
(`PP_0629`, `cbtA`), CorA/MgtE magnesium-cobalt transporters (`PP_1843`,
`cmaX`, `PP_2955`, `mgtE`), NiCoT/Rcn nickel-cobalt efflux/response context
(`PP_2968`, `PP_3928`), and low-resolution cation/CNNM-UPF0053 candidates
(`PP_0683`, `corC`, `PP_5322`). The sodium-solute/MATE systems were completed
next; remaining ion/metal sub-splits are membrane redox spillovers and membrane
metalloenzyme/envelope side nodes.

Completed the 14-gene `ion_metal_sodium_solute_symporters_and_mate_efflux`
sub-split: all members were fetched, Asta-backed, first-pass curated, validated,
and represented in `modules/sodium_solute_symporter_mate_boundary.yaml`. The
module separates AGCS amino-acid:sodium symport (`PP_0496`), MATE xenobiotic
efflux (`PP_0569`, `norM`), PP_0670 ACR3 arsenite/antimonite transport, GltS
glutamate:sodium symport (`gltS`), ArcD arginine-ornithine antiport (`arcD-I`,
`arcD-II`), ActP acetate transport (`actP-I`, `actP-II`, `actP-III`), broad or
low-confidence SSF/symporter candidates (`PP_3331`, `PP_4524`), PutP sodium/
proline symport (`putP`), and TcyP cystine transport (`tcyP`). The membrane
metalloenzyme/envelope side-node split was completed next.

Completed the 14-gene `ion_metal_membrane_metalloenzymes_and_envelope_side_nodes`
sub-split: all members were fetched, Asta-backed, first-pass curated, validated,
and represented in `modules/transport_membrane_enzyme_spillover_boundary.yaml`.
The module separates membrane protease/metalloprotease entries (`PP_0093`,
`PP_0144`, `rseP`, `htpX`, `ypfJ`, `ftsH`), lipid/cell-wall glycosylation and
phospholipid side nodes (`PP_1526`, `wbpL`, `PP_1838`, `PP_2974`, `ybhN`), TamB
envelope assembly context (`PP_2893`), and CopD/CycZ-like copper/cytochrome
membrane side nodes (`PP_1124`, `PP_4263`). This left membrane redox spillovers
as the final ion/metal sub-split.

Completed the 25-gene `ion_metal_membrane_redox_electron_transfer_spillovers`
sub-split: all members were fetched or rechecked, Asta-backed, first-pass
curated, validated, and represented in
`modules/membrane_redox_electron_transfer_boundary.yaml`. The module is a
boundary rather than one canonical pathway: it separates c-type cytochrome
electron carriers (`PP_0125`, `cc`, `PP_1841`, `PP_2675`, `PP_3332`,
`PP_4970`, `PP_5267`), membrane cytochrome b561 proteins (`PP_2010`,
`PP_2886`, `yceJ`), ferredoxin/iron-sulfur redox proteins (`PP_1083`, `fdxA`,
`PP_3543`, `PP_4259`, `yfhL`), Ccm cytochrome-c maturation (`ccmE`, `ccmH`),
Hmp nitric-oxide detoxification, MsrQ protein-repair electron transfer, CumA/
azurin copper-redox proteins (`cumA`, `PP_4870`), PP_4289 membrane c-type
cytochrome context, PP_0111 SCO/SenC redox-homeostasis context, PP_4203 ETF-QO,
and PP_0180 as the OFeT/FTR1-like ferrous-iron transporter. Metal/heme/FAD/Fe-S
binding rows were kept as supporting context rather than standalone core
functions where a more informative redox, transport, maturation, detoxification,
or repair role was available. All ion/metal sub-splits are now first-pass
curated.

Completed the 55-gene `amino_acid_quaternary_amine_nucleobase_transporters`
sub-split: all members were fetched or rechecked, Asta-backed, first-pass
curated, validated, and represented in
`modules/amino_acid_amine_nucleobase_transport_boundary.yaml`. The boundary
module separates GltP/YveA acidic-amino-acid symporters, APC/GabP amino-acid
and amine permeases, LysE/Rht exporters, BCCT choline/betaine/carnitine
compatible-solute transporters, NCS nucleobase/purine/xanthine/uracil
permeases, Amt/Rh ammonium and urea channels, BrnQ/AzlC branched-chain
transporters, PP_1060 glutamate synthase side context, PP_4226 Tre1-like side
context, and PP_2721 low-confidence unresolved context. The `gltP`
promoter-binding/transcription rows were removed as AauR regulator
misassignment based on the cached PMID:18310026 abstract, `uacT` xanthine terms
were broadened to nucleobase transport, and older manually added non-GOA `hutT`
rows were normalized so the histidine transporter evidence is represented as
authored `NEW` recommendations rather than pseudo-GOA annotations.

Completed the 14-gene `carbohydrate_nucleoside_transporters` sub-split: all
members were fetched, Asta-backed, first-pass curated, validated, and
represented in `modules/carbohydrate_nucleoside_transport_boundary.yaml`. The
module separates GntP-family gluconate transporters (`PP_0652`, `gntT`),
CodB/cytosine transporters (`codB`, `PP_4921`), broader NCS1 nucleobase
permeases (`PP_0709`, `PP_3641`, `PP_3655`, `pydP`, `PP_4309`), PnuC
nicotinamide-riboside transport (`PP_2860`), PP_1740 beta-glucanase/carbohydrate
hydrolysis side context, PP_3142 membrane sugar-transferase side context, and
PP_3048 prophage structural/virion-assembly side context. PP_0138 is retained as
an unresolved SpmB/Gate-domain membrane protein rather than being forced into a
nucleoside transporter function from the product name alone.

Completed the 7-gene `organic_acid_aromatic_anion_transporters` sub-split: all
members were fetched, Asta-backed, first-pass curated, validated, and represented
in `modules/organic_acid_aromatic_anion_transport_boundary.yaml`. The module
separates CitN/CitMHS citrate transport (`citN`), BenE benzoate transporters
(`PP_1820`, `benE-I`, `benE-II`), BhbP hydroxybutyrate/monocarboxylate context,
PP_3247 as an unresolved bile-acid/Na+-symporter-family transporter, and LldP
lactate/proton symport. BhbP's inherited gluconate transporter/process rows were
modified to broad monocarboxylate transport because the product is
D-beta-hydroxybutyrate permease and no beta-hydroxybutyrate-specific GO term was
available locally.

Completed the 13-gene `inorganic_nutrient_transporters` sub-split: all members
were fetched, Asta-backed, first-pass curated, validated, and represented in
`modules/inorganic_nutrient_transport_boundary.yaml`. The module separates
SulP-family sulfate or organosulfate transporter candidates (`PP_0075`,
`PP_0101`, `PP_0718`, `PP_1407`, `PP_4112`), CysZ proton-dependent sulfate
transport, YjbB/PiT phosphate transport (`yjbB`, `pitB`, `PP_4103`), ModR
molybdate-responsive transcription regulation, NasS nitrate-binding side
context (`PP_2094`), PhoU phosphate-transport accessory/regulatory context, and
PP_5475 as unresolved nitrite-transporter-name-only context. ModR's molybdate
transport row was marked over-annotated because ModR is a ModE-family regulator,
not a transporter; CysZ cysteine-biosynthesis context was kept out of the core
transporter function.

Completed the 3-gene `lipoprotein_envelope_accessory_spillovers` sub-split: all
members were fetched, Asta-backed, first-pass curated, validated, and represented
by an extension to `modules/transport_envelope_spillover_boundary.yaml`. The
split leaves `PP_1501` as unresolved product-name-only lipoprotein context,
treats `PP_2304` as PpiD peptidyl-prolyl cis-trans isomerase/folding-chaperone
context, and treats `csgG` as CsgG curli assembly/transport component context
with a conservative protein-secretion process call.

Completed the 13-gene
`envelope_polysaccharide_export_and_flippase_context` sub-split: all members
were fetched, Asta-backed, first-pass curated, validated, and represented in
`modules/envelope_polysaccharide_export_boundary.yaml`. The module separates
PP_0033-PP_0035 ArnT/GtrA and bactoprenol-linked glycan transfer context,
PP_3127-PP_3141 Wzz/Wzy/O-antigen and polysaccharide export/glycosyltransferase
context, `wzy` O-antigen polymerase context, and yceG/PP_5334 peptidoglycan or
unresolved transglycosylase side nodes. PP_3127's inherited protein tyrosine
kinase row was removed, and PP_0033's protein O-linked glycosylation row was
removed while the iron-response row was kept only as over-annotated context.

Completed the 20-gene `stress_resistance_membrane_spillovers` sub-split: all
members were fetched, Asta-backed, first-pass curated, validated, and represented
by an extension to `modules/stress_detoxification_spillover_boundary.yaml`. The
extension separates PqiA/PqiB-family paraquat-response membrane proteins,
PP_1264 as a FUSC/ArAE-family xenobiotic-efflux protein, PP_1487 as TerB-family
toxic-stress context, PP_1559/PP_3040/PP_3884 as phage/pyocin holin release
context, CidA/CidB as holin-regulator context, PP_3865 as phage-tail/virion
assembly context, and CptA/VasX/ToxA-domain proteins as unresolved membrane
toxin-domain side nodes. CidA's inherited hydrolase row was removed because
CidA regulates murein hydrolases rather than being the hydrolase enzyme.

Completed the 24-gene `membrane_redox_electron_transfer_proteins` sub-split: all
members were fetched or rechecked, Asta-backed, first-pass curated, validated, and
represented by an extension to `modules/membrane_redox_electron_transfer_boundary.yaml`.
The extension separates DsbB/DsbD disulfide-redox proteins, thioredoxin/glutaredoxin
redox proteins, Rnf/Nqr membrane ion-translocating oxidoreductase subunits, ETF
electron-transfer carrier subunits, PP_3338 cytochrome bd oxidase context, qhnDH
QH-AmDH gamma-subunit context, PP_1460/cycH/ccmF/ccoS cytochrome maturation or
heme-handling context, PP_4236 DsbE/Lgt redox-lipoprotein context, and PP_0251/
PP_4260 as low-information membrane redox/enzyme side nodes. The main first-pass
caution is to keep component-level redox/maturation context separate from unsupported
substrate-specific transporter claims.

Completed the 39-gene `membrane_signaling_channels_c_di_gmp_spillovers`
sub-split: all members were fetched or rechecked, Asta-backed, first-pass curated,
validated, and represented by an extension to
`modules/c_di_gmp_turnover_boundary.yaml`. The extension separates EC/product/GOA-
supported GGDEF diguanylate cyclases, EAL cyclic-guanylate phosphodiesterases,
low-confidence CSS/PsiE/GGDEF-EAL c-di-GMP candidates, MscS/MscL mechanosensitive
channels, chloride/bestrophin channel candidates, FecR/ECF-sigma regulatory sensors,
and low-information membrane signaling side nodes. `mscL` was preserved as the
Falcon-backed anchor review and only carried forward to `COMPLETE` with added Asta
provenance; PP_3315 and PP_3432 were intentionally kept low-confidence rather than
promoted to unsupported c-di-GMP enzyme functions.

Completed the 42-gene `membrane_associated_enzymes_and_side_nodes` sub-split:
all members were fetched, Asta-backed, first-pass curated, validated, and
represented by an extension to
`modules/transport_membrane_enzyme_spillover_boundary.yaml`. The extension
separates membrane peptidase/protease side nodes, lipid oxidoreductase and
hydroxylase candidates, acyltransferase/lipid-transfer proteins, peptidoglycan
and cell-envelope glycosyltransferase side nodes, kinase/phosphatase signaling
proteins, sulfatase/broad hydrolase candidates, detoxification/sulfurtransferase
side nodes, secreted/toxin-associated transferase or nuclease candidates, HflK/
HflC FtsH-modulator context, and low-information membrane enzyme candidates.
The main curation lessons are to treat histidine-kinase sensor-transporter rows
as over-propagated family context when no transport role is supported, broaden
PP_5219 away from unsupported glyceryl-ether monooxygenase specificity, and keep
misleading product-name artifacts such as PP_4560 ribonuclease BN and PP_5293
orotate phosphoribosyltransferase from becoming unsupported core functions.

Completed the 83-gene `other_domain_resolved_membrane_proteins` sub-split: all
members were fetched, Asta-backed, first-pass curated, validated, and represented
in new `modules/transport_membrane_domain_spillover_boundary.yaml`. The boundary
separates TauE/TSUP, AI-2E/PerM, DctM/TRAP, CstA, MMPL, FUSC, and other broad
transporter candidates from isolated ABC permease/binding-protein side nodes,
metal/TerC/GDT1/MgtC homeostasis proteins, envelope/cell-shape/curli/biofilm
side nodes, cytosolic nucleic-acid/tRNA/transcription spillovers, NRPS/RHS/toxin
side nodes, and low-information DoxX/SURF1/DedA/PAP2/MAPEG membrane-domain
proteins. The main curation lesson is to keep this as a boundary module: broad
transporter activity is used only for clear transporter-family profiles, isolated
ABC permeases and FatB-like binding proteins are component-level context with
unresolved partners/substrates, and domain-only membrane proteins are not promoted
to substrate-specific pathway functions.

Completed the 67-gene `low_information_membrane_proteins` sub-split: all members
were fetched, Asta-backed, first-pass curated, validated, and represented in new
`modules/low_information_membrane_protein_boundary.yaml`. The boundary separates
clear low-information transporter candidates, ArsB arsenical pumps, YfdC
formate/nitrite transporter context, a TonB-domain energy-transducer singleton,
envelope/outer-membrane/biofilm/toxin side nodes, and domain-only membrane
proteins left unresolved. The main curation lesson is to resist upgrading weak
product names into pathway claims: ArsB, YfdC, TonB-domain, and clearer PACE/
FUSC/PIN/MFS/TerC/AI-2E-like families get transport context, while most small
or domain-only membrane proteins stay as localization or unresolved boundary
members. This closes the remaining queued transport/membrane/efflux split.

## 2026-07-10

Completed the ninth regulation/signal-transduction split,
`low_information_or_named_transcriptional_regulators`. The 31 missing review
folders were fetched, Asta was generated for all 32 split members including the
pre-existing curated `hexR` anchor, and the new
`modules/transcriptional_regulator_spillover_boundary.yaml` validates. The split
uses conservative `NEW` molecular-function rows only where product/domain
evidence supports a missing DNA-binding transcription-regulator or repressor
function. `PP_1762`, `PP_2738`, `PP_4528`, `PP_5232`, and `PP_5343` remain
no-core unresolved, producing the only five expected validation warnings.
`sahR` keeps methyltransferase-domain annotations as non-core context pending
evidence for catalytic relevance.

Completed the eighth regulation/signal-transduction split,
`arac_xyls_transcriptional_regulators`. All 40 genes are represented in
`modules/arac_xyls_transcriptional_regulator_boundary.yaml`: existing curated
`ada` and `BenR` reviews were preserved as anchor cases, and the other 38 genes
were fetched, Asta-backed, first-pass curated, and validated. DNA-binding
transcription factor activity is the shared core function, generic DNA binding
is marked over-annotated, broad transcription rows are modified toward
regulation of DNA-templated transcription, and cytoplasm/cytosol locations are
kept as non-core annotation context rather than promoted into core functions.
The split separates named regulators, DJ-1/PfpI or INH-QAR-associated
regulators, RmlC/cupin-associated regulators, arabinose-binding-domain
regulators, and other sensor-domain candidates. Target regulons, effector
ligands, regulatory direction, and the PP_4602 kinase side call remain
unresolved unless supported by gene-specific evidence.

Completed the seventh regulation/signal-transduction split,
`gntr_transcriptional_regulators`. All 29 genes fetched normally, Asta reports
are present, and the first-pass reviews plus
`modules/gntr_transcriptional_regulator_boundary.yaml` validate with no
warnings. The module separates FadR/GntR C-terminal regulators, UTRA/HutC-like
regulators, and PLP/aminotransferase-domain GntR regulators. DNA-binding
transcription factor activity is the shared core function, generic DNA binding
is marked over-annotated, broad transcription rows are modified toward
regulation of DNA-templated transcription, PLP binding is retained as non-core
domain/cofactor context, and CsiR/VanR names are kept without asserting direct
regulons.

Completed the sixth regulation/signal-transduction split,
`xre_cro_phage_toxin_antitoxin_regulators`. All 28 genes fetched normally, Asta
reports are present, and the first-pass reviews plus the extended
`modules/phage_regulation_toxin_antitoxin_boundary.yaml` validate. The module
now separates MqsRA/HigA-like toxin-antitoxin regulators, LexA-like Cro/C1
regulator candidates, Cro/C1-cupin candidates, simple Cro/C1 candidates, and
non-phage regulatory spillovers. `mqsR` is curated as toxin activity with
translation inhibition, while quorum-sensing and biofilm terms are kept as
over-annotated phenotype/output context. `PP_5680` remains no-core unresolved,
and RodZ/CdaR/PucR/LuxR/PuuR-like spillovers are not forced into phage-specific
biology.

Completed the fifth regulation/signal-transduction split,
`merr_arsr_marr_metal_redox_regulators`. All 25 genes fetched normally, Asta
reports are present, and the first-pass reviews validate. The new
`modules/metal_redox_stress_transcription_regulator_boundary.yaml` separates
named arsenic/redox regulators (`arsR1`, `arsR2`, `soxR`), MerR-family metal
regulator candidates, ArsR-family metal-responsive regulator candidates,
MarR/EmrR stress or efflux regulator candidates, and weak product-name-only
records. The expected residual warnings are the five intentional no-core calls
for `PP_1578`, `PP_2296`, `PP_3866`, `PP_4102`, and `PP_5592`, where GOA rows
are absent and the current domain evidence is not coherent enough to assert
DNA-binding transcription factor activity.

Partitioned `module:translation_rna_processing` into nine curation-scale
buckets: rRNA modification, ribosome maturation/hibernation, tRNA modification
and processing, RNA decay/helicases, aminoacyl-tRNA quality control,
translation factors/ribosome rescue, transcription spillovers, pyoverdine NRPS
spillovers, and low-information RNA-binding/enzyme spillovers.

Completed the first translation/RNA-processing split,
`nonribosomal_peptide_synthetase_spillovers`. Fetched `pvdJ`, `pvdI`, and
`pvdL`, ran Asta for `pvdD`, `pvdJ`, `pvdI`, and `pvdL`, first-pass curated the
three new reviews, validated all four batch reviews, and extended
`modules/siderophore_biosynthesis_boundary.yaml` with a
PvdL/PvdI/PvdJ/PvdD ferribactin/pyoverdine NRPS assembly node.

Main lesson from this split: the word `non-ribosomal` pulled pyoverdine NRPS
genes into the translation/RNA bucket, but these are siderophore-biosynthesis
genes. Asta was fast but mostly returned generic database/annotation papers for
`pvdJ`/`pvdI`/`pvdL`, so the review decisions use Asta as retrieval provenance
and rely on UniProt/domain evidence plus the existing pyoverdine NRPS pathway
context. `pvdL` lipid and Actinobacterium-cell-wall annotations were treated as
over-propagated side signals rather than accepted pathway assignments.

Completed the second translation/RNA-processing split,
`low_information_rna_binding_or_enzyme_spillovers`. `PP_2182` and `PP_2953`
could not be populated through `just fetch-gene` because UniProt REST returned
HTTP 500 for Q88KV7 and Q88IP6, so the review inputs use live QuickGO rows plus
explicitly marked fallback UniProt-style context assembled from the project gene
list. Asta ran for both genes but returned mostly generic retrieval, so it is
recorded as provenance only. `PP_2182` is kept as a ProQ/FinO RNA-chaperone
candidate with RNA strand annealing/exchange and post-transcriptional
regulation context. `PP_2953` is routed out of RNA processing as a predicted
NADPH quinone-reductase-like oxidoreductase; the older partition snapshot's
RNA-binding signal is not supported by the current live GOA rows.

Completed the third translation/RNA-processing split,
`transcription_rna_polymerase_spillovers`. `nusA` fetched normally, while
`nusB`, `rapA`, `PP_2266`, `PP_4553`, and `dksA` hit UniProt REST HTTP 500
during `just fetch-gene`, so those review inputs use live QuickGO rows plus
explicitly marked fallback UniProt-style context assembled from the project
gene list. Asta ran for all six genes and is recorded as provenance; annotation
support stays anchored to UniProt/HAMAP/domain context and live GOA rows. The
new `modules/transcription_rna_polymerase_spillover_boundary.yaml` separates
Nus termination/antitermination factors, RapA/DksA RNA-polymerase regulatory
factors, and sigma/RNAP side nodes from the translation/RNA-processing module.

Completed the fourth translation/RNA-processing split,
`translation_factors_ribosome_rescue`. All ten genes (`hslR`, `selB`, `ettA`,
`ychF`, `pth`, `lepA`, `frr`, `arfB`, `infA`, and `smpB`) fetched normally,
ran through Asta, and validate with no remaining `PENDING` actions. The new
`modules/translation_factor_ribosome_rescue_boundary.yaml` separates conserved
translation initiation/elongation/throttle factors, ribosome recycling and
stalled-ribosome rescue, trans-translation, and ribosome-associated stress/NTPase
side nodes. The expected residual validation warning is that Asta reports are
not cited as direct biological support in individual annotation decisions.

Completed the fifth translation/RNA-processing split,
`aminoacyl_trna_charging_editing_quality_control`. All eleven genes (`PP_0201`,
`PP_0782`, `PP_0784`, `ybaK`, `PP_1091`, `ycfH`, `aat`, `PP_4228`, `gluQ`,
`dtd`, and `PP_5664`) fetched normally, ran through Asta, and validate with no
remaining `PENDING` actions. The new
`modules/aminoacyl_trna_quality_control_boundary.yaml` separates YbaK/Dtd/YcfH
deacylase and editing context, Aat L/F-transferase N-end-rule chemistry, Glu-Q
tRNA(Asp) modification, and unresolved GAD/T6SS Tdi1_C or short-fragment side
nodes. The expected residual validation warning is that Asta reports are not
cited as direct biological support in individual annotation decisions.

Completed the sixth translation/RNA-processing split,
`ribonuclease_rna_decay_processing_helicases`. All twelve genes (`rnpA`, `rng`,
`rnt`, `PP_1840`, `PP_2084`, `rnz`, `PP_4462`, `srmB`, `rnd`, `PP_4720`,
`dbpA`, and `rph`) are fetched or rechecked, ran through Asta, and validate
with no remaining `PENDING` actions. The new
`modules/rna_decay_processing_boundary.yaml` separates RNase P/G/T/Z/D/PH
tRNA/rRNA processing activities, SrmB/DbpA DEAD-box RNA helicase context, and
RraA/RraB/YhbY-like side nodes. The main correction is `rnpA`: 3-prime tRNA
processing carryover was modified toward RNase P 5-prime leader-removal
context. `rnt` DNA-replication proofreading was removed as a family-transfer
artifact. The expected residual validation warning is that Asta reports are not
cited as direct biological support in individual annotation decisions.

Completed the seventh translation/RNA-processing split,
`rrna_modification_methyltransferase_pseudouridine`. All 29 genes (`rsmG`,
`rsmB`, `rsmA`, `rluD`, `rsmC`, `rlmN`, `rlmF`, `PP_1191`, `rsmI`, `rsmH`,
`rsuA`, `rsmJ`, `rlmAA`, `rlmD`, `rluC`, `rlmL`, `PP_2110`, `rlmM`,
`PP_4306`, `rluB`, `rlmG`, `rlmE`, `rlmH`, `rlmB`, `rlmJ`, `rsmE`,
`PP_5019`, `PP_5114`, and `rlmI`) are fetched or rechecked, ran through Asta,
and validate with no remaining `PENDING` actions. The new
`modules/rrna_modification_ribosome_maturation_boundary.yaml` separates
site-specific 16S/23S rRNA methyltransferases, rRNA pseudouridine synthases,
dual RlmN/RluF-like RNA-modification chemistry, RsmE-family paralogs, and
unresolved methyltransferase-domain side nodes. Existing Falcon-backed reviews
for `rsmG`, `rsmJ`, `rlmE`, and `rlmH` were preserved and only folded into the
Asta-backed split/module bookkeeping. The expected residual validation warning
is that Asta reports are not cited as direct biological support in many
individual annotation decisions.

Completed the eighth translation/RNA-processing split,
`ribosome_assembly_maturation_hibernation`. All 24 genes (`yigZ`, `rimI`,
`der`, `darP`, `hpf`, `rimO`, `era`, `rimM`, `prmB`, `PP_1910`, `PP_2956`,
`ycaO`, `PP_3810`, `rbfA`, `rimP`, `ybeY`, `rsfS`, `prmA`, `PP_4885`,
`PP_4996`, `typA`, `rmf`, `PP_5700`, and `PP_5726`) fetched normally, ran
through Asta, and validate with no remaining `PENDING` actions. The new
`modules/bacterial_ribosome_maturation_regulation_boundary.yaml` separates
ribosome-associated GTPases and binding factors, 30S maturation factors, 50S
maturation factors, hibernation/translation-silencing factors, ribosomal-protein
modification enzymes, and unresolved ribosomal-interface/S2p-like side nodes.
Main corrections were conservative: `rimO` tRNA modification was removed as a
wrong substrate transfer, `ybeY` metalloendopeptidase and `PP_4996` generic
hydrolase rows were narrowed toward RNA/nuclease context, and zero-GOA entries
such as `ycaO`, `PP_3810`, `PP_4885`, `PP_5700`, and `PP_5726` were left
unresolved rather than forced into GO-level activities.

Completed the ninth and final translation/RNA-processing split,
`trna_modification_processing`. All 30 genes (`mnmG`, `mnmE`, `tsaC`, `tsaD`,
`cca`, `cmoM`, `selU`, `trmJ`, `tadA`, `cmoB`, `trmD`, `tsaB`, `tilS`,
`truD`, `yfiP`, `ttcA`, `rluA`, `mnmC`, `trhO`, `dusC`, `truA`, `dusA`,
`trmK`, `PP_4520`, `trmA`, `truB`, `dusB`, `miaA`, `tsaE`, and `trmL`) are
fetched or rechecked, ran through Asta, and validate with no remaining
`PENDING` actions. The new
`modules/trna_modification_processing_boundary.yaml` separates wobble-uridine
side-chain chemistry, t6A37 biosynthesis, Trm methyltransferases, Tru/Rlu
pseudouridine synthases, TadA/TilS/TtcA/MiaA/DTW-domain base-modification
enzymes, Dus-family dihydrouridine synthases, and Cca CCA/CCACCA-end
processing. The existing complete `cca` review was preserved and only updated
with Asta/module bookkeeping. This closes the 128-gene translation/RNA-processing
umbrella at first pass; all nine splits now have review files, Asta reports,
curation decisions, validation, and module or routed-boundary representation.

Completed the `outer_membrane_barrel_channel_autotransporter_context` split from
the cell-envelope/division umbrella. Fetched by accession with stable aliases,
ran Asta, first-pass curated, validated, and rendered `yiaD`, `PP_1121`,
`PP_1122`, `PP_1880`, `PP_3069`, `PP_3449`, `PP_4291`, and `PP_4293`.

Extended `modules/transport_envelope_spillover_boundary.yaml` with a new
outer-membrane barrel/channel/autotransporter part. Main decisions: OmpA-family
`yiaD`, `PP_1121`, and `PP_1122` are outer-membrane envelope-context candidates;
`PP_1121`/`PP_1122` calcium binding is non-core repeat evidence; `PP_1880` and
`PP_3069` are autotransporter candidates with unresolved passenger functions;
`PP_3449` received only a conservative new outer-membrane component annotation;
and Tsx-like `PP_4291`/`PP_4293` received conservative new porin activity
without asserting a nucleoside-transport process.

Regenerated
`projects/P_PUTIDA/batches/module_cell_envelope_division_partition.{tsv,md}`,
the outer-membrane barrel/channel batch page, and
`projects/P_PUTIDA/data/psepk_pathway_worklist.tsv`. The cell-envelope worklist
now records 29 review files, 29 curated reviews, and 29 Asta reports inside the
98-gene partitioned umbrella.

Completed the `named_outer_membrane_lipoprotein_families` split from the same
cell-envelope/division umbrella. Fetched, ran Asta, first-pass curated,
validated, and rendered `uxpA`, `slyB`, `oprI`, `PP_3236`, `yaiW`, `PP_4032`,
`PP_4855`, `PP_5037`, and `PP_5226`.

Extended `modules/transport_envelope_spillover_boundary.yaml` again with a named
lipoprotein-family part. Main decisions: `uxpA` gets specific
5'-nucleotidase activity rather than only broad hydrolase activity; `slyB`,
`oprI`, `PP_4855`, and `PP_5226` are outer-membrane lipoprotein candidates with
unresolved mechanism; `PP_3236` and `yaiW` receive only broad membrane
localization because local evidence lacks a direct outer-membrane line; and
Blc/lipocalin paralogs `PP_4032` and `PP_5037` keep lipid binding as core while
stress response is non-core family context.

After regenerating the partition and worklist again, `module:cell_envelope_division`
now records 38 review files, 38 curated reviews, and 38 Asta reports.

Completed the `domain_resolved_lipoprotein_spillovers` split from the same
cell-envelope/division umbrella. Fetched by accession with stable aliases, ran
Asta, first-pass curated, validated, and rendered all 30 genes:
`PP_0116`, `PP_0139`, `PP_0512`, `PP_0549`, `PP_0576`, `PP_0753`,
`PP_1115`, `PP_1146`, `PP_1153`, `PP_1161`, `PP_1238`, `PP_1322`,
`PP_1500`, `PP_1519`, `PP_1970`, `PP_2003`, `PP_2020`, `PP_2121`,
`PP_2191`, `PP_2462`, `PP_2730`, `PP_3520`, `PP_4199`, `PP_4564`,
`PP_4686`, `PP_4920`, `PP_4961`, `PP_5319`, `PP_5333`, and `PP_5639`.

Extended `modules/transport_envelope_spillover_boundary.yaml` with a
domain-resolved lipoprotein-family part. Main decisions: most entries receive
only broad membrane placement; LEA_2/WHy-domain `PP_1115` and `PP_2191` retain
response-to-desiccation process context; `PP_1500` keeps peptidase activity and
proteolysis; `PP_2462` gains candidate peptidase inhibitor activity; `PP_4686`
gains candidate heme binding; and `PP_5319` is kept as membrane lipoprotein
context while its alkane catabolic process annotation is marked
over-annotated.

Completed the final `generic_lipoprotein_signal_spillovers` split from the
cell-envelope/division umbrella. Fetched by accession with stable aliases, ran
Asta, first-pass curated, validated, and rendered all 30 genes:
`PP_0091`, `PP_0092`, `PP_0277`, `PP_0677`, `PP_1204`, `PP_1498`,
`PP_2197`, `PP_2252`, `PP_2306`, `PP_2414`, `PP_3008`, `PP_3010`,
`PP_3014`, `PP_3158`, `PP_3418`, `PP_3519`, `PP_3824`, `PP_4319`,
`PP_4962`, `PP_5304`, `PP_5449`, `PP_5470`, `PP_5480`, `PP_5504`,
`PP_5509`, `PP_5524`, `PP_5594`, `PP_5648`, `PP_5661`, and `PP_5710`.

Extended `modules/transport_envelope_spillover_boundary.yaml` with a generic
lipoprotein/signal-peptide part. Main decisions: all 30 fetched GOA files are
header-only, Asta retrieved no specific family/domain/function beyond the
provided UniProt context, and every gene receives only a broad membrane
candidate annotation. No outer-membrane specificity, molecular function,
partner complex, or pathway process is asserted in this pass.

Partitioned `module:stress_detoxification` into seven curation-scale buckets:
peroxide/peroxiredoxin detoxification, glutathione/thiol detoxification,
arsenic/copper resistance, universal stress proteins, cold/heat-shock proteins,
ThiJ/DJ-1/PfpI candidates, and miscellaneous stress-regulatory spillovers.

Completed the first stress/detoxification split,
`peroxide_peroxiredoxin_detoxification`. Fetched or rechecked, ran Asta,
first-pass curated, validated, and rendered all 10 genes: `osmC`, `PP_0235`,
`tsaA`, `PP_1235`, `ohr`, `ahpC`, `PP_2943`, `PP_3248`, `tpx`, and `cpo`.
Seeded and validated `modules/oxidative_stress_peroxide_detoxification_boundary.yaml`.
Main decisions: OsmC/Ohr-family proteins stay conservative peroxide or organic
hydroperoxide detoxification candidates; PP_0235/tsaA/PP_1235/ahpC/tpx are
peroxiredoxin or thioredoxin-dependent peroxiredoxin context; PP_2943 is
periplasmic cytochrome c551 peroxidase; PP_3248 is DyP-family heme
peroxidase; and cpo is a non-heme chloroperoxidase. Broad antioxidant,
stress-response, redox-homeostasis, heme-binding, and electron-transfer rows
are retained as non-core context where they are not the primary function.

Completed the second stress/detoxification split,
`glutathione_thiol_detoxification`. Fetched, ran Asta, first-pass curated,
validated, and rendered all 7 genes: `PP_0335`, `yffB`, `PP_1939`, `PP_2023`,
`PP_3742`, `PP_4104`, and `mnaT`. Extended
`modules/glutathione_metabolism_boundary.yaml` with a stress-bucket
glutathione/thiol side-context part. Main decisions: GST-family entries receive
conservative transferase-family calls without substrate/process assertions;
`yffB` is an ArsC-family glutathione-dependent thiol reductase candidate with
unresolved arsenate-reductase specificity; `PP_1939` is retained as a
glutathione-independent formaldehyde dehydrogenase candidate; and `mnaT` keeps
the specific L-amino-acid N-acetyltransferase activity while broad
transferase/acyltransferase parents are modified toward that term.

Completed the third stress/detoxification split,
`arsenic_copper_metal_resistance`. Fetched, ran Asta, first-pass curated,
validated, and rendered all 8 genes: `PP_1927`, `PP_1928`, `copB-I`,
`copA-I`, `arsH`, `PP_2716`, `copB-II`, and `copA-II`. Seeded and validated
`modules/metal_resistance_detoxification_boundary.yaml`. Main decisions:
`PP_1927` and `arsH` use `GO:0052873` FMN reductase (NADPH) activity as the
core MF while broader oxidoreductase rows are modified to that term; `PP_1928`
and `PP_2716` receive conservative broad oxidoreductase activity plus
arsenic-response process context because their fetched GOA tables are empty;
`copB-I` and `copB-II` stay outer-membrane copper-binding/homeostasis proteins;
and `copA-I` and `copA-II` stay periplasmic multicopper oxidase-family proteins
with broad oxidoreductase activity rather than being treated as P-type copper
ATPases.

Completed the fourth stress/detoxification split,
`universal_stress_proteins`. Fetched, ran Asta, first-pass curated, validated,
and rendered all 11 genes: `PP_1269`, `PP_2132`, `PP_2187`, `PP_2326`,
`PP_2648`, `PP_2745`, `PP_3156`, `PP_3237`, `PP_3288`, `PP_3290`, and
`PP_3294`. Seeded and validated `modules/universal_stress_protein_boundary.yaml`.
Main decisions: preserve cytoplasm annotations where present; group
single-domain and tandem-domain USP-family proteins separately; keep UniProt
DNA-damaging-agent resistance comments as contextual by-similarity evidence;
and avoid adding ATP-binding, molecular-function, or stress-response process
terms without direct support.

Completed the fifth stress/detoxification split,
`cold_heat_shock_chaperone_spillovers`. Fetched, ran Asta, first-pass curated,
validated, and rendered all 5 genes: `capB`, `cspA-I`, `ibpA`, `PP_3313`, and
`PP_3314`. Extended and validated
`modules/integrated_stress_response_boundary.yaml` with cold-shock-domain
nucleic-acid-binding side nodes and HSP20-family unfolded-protein-binding
holdase side nodes. Main decisions: `capB` and `cspA-I` retain conservative
nucleic acid binding plus cytosolic/cytoplasmic localization without promoting
a specific transcription/RNA target claim; `ibpA`, `PP_3313`, and `PP_3314`
receive conservative HSP20 unfolded-protein-binding calls; and `PP_3313`
retains response-to-heat process context.

Regenerated
`projects/P_PUTIDA/batches/module_stress_detoxification_partition.{tsv,md}`,
the cold/heat-shock spillover batch page, and
`projects/P_PUTIDA/data/psepk_pathway_worklist.tsv`. The stress/detoxification
worklist now records 42 review files, 41 Asta reports, and 10 remaining missing
review folders across the ThiJ/DJ-1/PfpI and miscellaneous spillover splits.

Completed the sixth stress/detoxification split,
`thij_dj1_pfpi_detoxification_candidates`. Fetched, ran Asta, first-pass
curated, validated, and rendered all 3 genes: `PP_2491`, `PP_2992`, and
`PP_3431`. Created and validated
`modules/stress_detoxification_spillover_boundary.yaml` with an HSP31-like
glyoxalase III/methylglyoxal-detoxification part. Main decisions: accept
cytoplasm, `GO:0019172` glyoxalase III activity, and `GO:0051596`
methylglyoxal catabolic process from TreeGrafter/PANTHER evidence; treat
glyoxalase III as the GSH-independent methylglyoxal-to-D-lactate activity; and
avoid adding protein- or nucleotide-deglycase terms without gene-specific or
subfamily-specific support.

Regenerated the stress partition/worklist again. The stress/detoxification
worklist now records 45 review files, 44 Asta reports, and 7 remaining missing
review folders, all in the final miscellaneous stress-regulatory spillover
split.

Completed the seventh and final stress/detoxification split,
`stress_regulatory_or_misc_spillovers`. Fetched the seven missing reviews, ran
Asta for all 8 genes, first-pass curated, validated, and rendered `srkA`, `dps`,
`PP_3269`, `paaY`, `PP_3509`, `PP_3963`, `oxyR`, and `PP_5593`. Extended and
validated `modules/stress_detoxification_spillover_boundary.yaml` with SrkA/OxyR
regulatory context, Dps ferroxidase/DNA-binding context, PaaY
phenylacetate-route thioesterase context, PP_3509 bleomycin-response context,
and a low-information KGG-repeat unknown group.

Main decisions for the final split: `srkA` is retained as an ATP/magnesium-
dependent Ser/Thr kinase without substrate claims; `dps` keeps ferroxidase,
ferric-iron-binding, and a NEW DNA-binding row while the broad metal-ion
oxidoreductase parent is marked over-annotated; `paaY` gets conservative NEW
`GO:0016289` acyl-CoA hydrolase activity and `GO:0010124` phenylacetate
catabolic process; `PP_3509` keeps response to antibiotic and gets a NEW
response-to-bleomycin process, with no molecular function asserted; `oxyR` gets
a NEW `GO:0034599` cellular response to oxidative stress row tied to the
peroxide-defense regulon; and `PP_3269`, `PP_3963`, and `PP_5593` remain
curated unknown KGG-repeat stress-induced proteins with no proposed GO function.

Regenerated the stress partition/worklist after closing the final split. The
stress/detoxification bucket now records 52/52 review files, 52/52 curated
reviews, 52/52 Asta reports, and zero missing review folders.

Partitioned `module:dna_replication_repair_recombination` into eight
curation-scale buckets and completed the first DNA-topology/topoisomerase split.
Fetched missing review folders, ran Asta, first-pass curated, validated, and
rendered `yacG`, `topA`, `PP_3831`, `topB`, `PP_4476`, `parC`, and `parE`;
existing `gyrA` and `gyrB` reviews were reused. Created and validated
`modules/dna_topology_topoisomerase_boundary.yaml`.

Main decisions for the DNA-topology split: `gyrA`/`gyrB` remain the DNA gyrase
negative-supercoiling core; `yacG` is a zinc-binding gyrase inhibitor rather
than a direct transcription regulator; `topA`, `topB`, and `PP_3831` are type I
topoisomerase/topological-change nodes; `parC`/`parE` form Topo IV for
chromosome decatenation/segregation, with a UniProt-backed NEW Topo IV complex
membership row added for `parE`; and `PP_4476` remains an unresolved
low-evidence candidate with no GO terms asserted from a ProtNLM name alone.

Regenerated
`projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_partition.{tsv,md}`,
the DNA-topology sub-batch page, and
`projects/P_PUTIDA/data/psepk_pathway_worklist.tsv`. At that point the broad
DNA bucket recorded 13 review files, 13 curated reviews, and 9 Asta reports;
the next targets were the SOS/translesion/alkylation and
repair-helicase/recombination splits.

Completed the second DNA replication/repair/recombination split,
`sos_translesion_alkylation_repair`. Reused curated `dinB` and `lexA2`, fetched
the seven missing review folders, ran Asta for all 9 genes, first-pass curated,
validated, and rendered `PP_1348`, `lexA1`, `polB`, `ogt`, `imuB`, `dnaE2`,
and `PP_5679`. Created and validated
`modules/dna_damage_response_translesion_repair_boundary.yaml`.

Main decisions for the SOS/translesion split: `lexA1` is the conventional SOS
regulon LexA repressor while `lexA2` regulates the imuA-imuB-dnaE2 cassette;
`dinB` and `dnaE2` are retained as error-prone/translesion DNA polymerase
context, with a new translesion-synthesis row added for `dnaE2`; `polB` is a
type-B DNA polymerase/proofreading context rather than a direct SOS regulator;
`imuB` and `PP_5679` remain accessory or low-information damaged-DNA/Y-family
context; `ogt` is direct alkylation repair; and `PP_1348` is MutT-like
oxidized-nucleotide-pool sanitation.

Regenerated the DNA partition/worklist again. At that point the broad DNA
bucket recorded 20 curated review files and 18 Asta reports; the next active
target was `repair_helicase_recombination_core`, followed by the
nuclease/DNase/toxin split. Mobile-element and reverse-transcriptase genes
remained queued for a separate mobile-genetic-elements pass.

Completed the third DNA replication/repair/recombination split,
`repair_helicase_recombination_core`. Fetched all 20 missing review folders,
ran Asta for all 20, first-pass curated the split, validated the gene reviews,
and extended `modules/bacterial_homologous_recombination.yaml` with a
supplemental repair-helicase/recombination boundary part.

Main decisions for the repair-helicase/recombination split: `PP_1103` is the
experimentally characterized Lhr-Core 3'-to-5' DNA/RNA:DNA helicase; `dinG`,
`PP_1061`, `PP_2565`, `PP_3681`, `PP_1937`, `PP_2146`, and `PP_3691` are
curated as Lhr/DinG/UvrD/Rep/SNF2/DNA2-like helicase candidates at the
specificity supported by local evidence; `sbcC`/`sbcD` are SbcCD ATPase/nuclease
context; `rdgC`, `radA`, and `recN` are recombination/repair factors; `uup` is
kept as an ABCF ATPase with ribosome-binding plus possible branched-DNA context;
and `PP_0152`, `PP_1410`, `PP_2298`, `PP_4448`, and `PP_5711` remain
low-evidence boundary candidates with no GO functions promoted from ProtNLM or
domain names alone.

Regenerated the DNA partition/worklist again. At that point the broad DNA bucket
recorded 40 curated review files and 38 Asta reports; the next active target
was `nuclease_dnase_toxin_side_nodes`, followed by the compact
replication-accessory/polymerase split. Mobile-element and reverse-transcriptase
genes remained queued for a separate mobile-genetic-elements pass.

Completed the fourth DNA replication/repair/recombination split,
`nuclease_dnase_toxin_side_nodes`. Fetched all 14 review folders, ran Asta for
all 14, first-pass curated the split, validated the gene reviews, and created
and validated `modules/nuclease_dnase_boundary.yaml`.

Main decisions for the nuclease/DNase/toxin split: `endX` and `endA` are
EndA/NucM-family DNase/endonuclease candidates; `tatD` is a TatD-family
metal-dependent nuclease/exonuclease candidate; `PP_2276` is retained as
FEN/phage-exonuclease boundary context; `PP_1306`, `PP_3883`, and `yajD` are
HNH/pyocin/YajD-like endonuclease candidates; `PP_1554` and `PP_3890` are
VRR-NUC broad nuclease candidates; `yoeB` is an RNA-toxin/mRNA-interferase side
node rather than a transcription regulator; `PP_4247` and `PP_5295` are RNA
nuclease side nodes; `PP_5086` is an SNase-domain DNA endonuclease candidate;
and `PP_2838` is retained as phosphodiesterase I/FAN1-family context with
interstrand cross-link repair kept non-core.

Regenerated the DNA partition/worklist again. At that point the broad DNA bucket
recorded 54 curated review files and 52 Asta reports; the next active target was
the compact replication-accessory/polymerase split. Mobile-element and
reverse-transcriptase genes remained queued for a separate mobile-genetic-elements
pass.

Completed the fifth DNA replication/repair/recombination split,
`replication_accessory_polymerase`. Fetched all six review folders, ran Asta for
all six, first-pass curated the split, validated the gene reviews, rendered the
gene pages, and extended and validated `modules/bacterial_dna_replication.yaml`.

Main decisions for the replication-accessory/polymerase split: `hda` is a
DnaA/Hda-family negative regulator of replication reinitiation; `PP_2270` is a
T7-like helicase/primase-family 5'-3' DNA helicase candidate in replication and
primer-synthesis context; `PP_2273` is a type-A DNA polymerase boundary member
rather than part of the canonical Pol III core; `rarA` is a RarA/MGS1-family
DNA-dependent ATPase associated with stalled replication responses, not promoted
as a helicase; `rep` is the supported Rep-family 3'-5' DNA helicase; and
`PP_0978` remains an unpromoted Pol III chi-like candidate because the local
record has only a ProtNLM-derived product name and no GOA/domain/family support.

Regenerated the DNA partition/worklist again after the replication-accessory
split. At that point the broad DNA bucket recorded 60 curated review files and
58 Asta reports; the next non-mobile cleanup target was the
architectural/RNA/protein-folding spillover split.

Completed the sixth DNA replication/repair/recombination split,
`architectural_rna_protein_spillovers`. Fetched the six missing review folders,
ran Asta for all seven genes including the pre-existing `dnaJ` review, curated
`tldD`, `ihfB`, `ihfA`, `cspD`, `hrpA`, and `hrpB`, preserved the completed
`dnaJ` review, validated the six new reviews plus `dnaJ`, rendered the gene
pages, and created and validated
`modules/dna_bucket_architectural_rna_protein_spillover_boundary.yaml`.

Main decisions for the architectural/RNA/protein spillover split: `tldD` is a
TldD/PmbA-family metallopeptidase/proteolysis node; `ihfB` and `ihfA` are IHF
architectural/regulatory DNA-binding subunits, not DNA-repair enzymes; `cspD`
is a cold-shock-domain DNA-binding replication-inhibitor context; `hrpA` is an
RNA helicase; `hrpB` gains a conservative `NEW` RNA helicase row from HrpB
family evidence; and `dnaJ` remains DnaK-system co-chaperone/protein-folding
context.

Completed the final mobile-genetic-elements pass for the DNA
replication/repair/recombination bucket. Fetched the missing mobile-element and
reverse-transcriptase review folders, ran Asta for all 28 mobile/RT members
including the pre-existing `PP_0635` review, curated 25
integrase/recombinase/transposase genes plus `PP_1250` and `PP_1846`,
validated the edited reviews and the reused `PP_0635` review, and created and
validated `modules/mobile_genetic_elements_boundary.yaml`.

Main decisions for the mobile/RT split: phage integrases, Tyr/Ser
recombinases, resolvases, excisionase, Tn/IS transposases, and group-II-intron
or retroelement reverse transcriptases are routed to mobile genetic element
biology, not chromosomal DNA repair. Broad DNA-binding rows are retained as
substrate/context unless they are the only supported molecular-function evidence
for low-specificity integrase/excisionase records. `PP_2495` remains an
unresolved YqaJ viral recombinase-domain member with no GOA rows and no
synthetic core GO function asserted.

Regenerated the DNA partition/worklist again. The broad DNA bucket now records
93/93 review files, 93/93 curated reviews, and 93/93 Asta reports; all eight
DNA-bucket splits are first-pass complete.

## 2026-07-09

Partitioned the functional `module:cell_envelope_division` bucket. Generated
`projects/P_PUTIDA/batches/module_cell_envelope_division_partition.{tsv,md}`
and per-sub-batch ledgers from
`projects/P_PUTIDA/partition_cell_envelope_division.py`. The 98 genes split
into Lpt/LPS transport context, LPS-core/lipid-A biosynthesis context,
peptidoglycan turnover/remodeling candidates, cell-division regulatory
spillovers, VacJ/MlaA phospholipid-asymmetry context, ApbE-like envelope
flavinylation, outer-membrane barrels/channels/autotransporters, named
outer-membrane lipoprotein families, domain-resolved lipoprotein spillovers,
and generic lipoprotein-signal spillovers.

Completed the first cell-envelope split against the existing LPS module.
Fetched, ran Asta, curated, validated, and rendered `PP_3016`, `PP_3134`, and
`maa`. `PP_3016` is now a conservative WaaZ/Kdo-transferase-family LPS-core
biosynthesis candidate, and `PP_3134` is a LpxA-like O-acyltransferase/lipid-A
biosynthesis candidate with exact substrate unresolved. `maa` is the important
negative lesson from the split: despite lipid-A/fold-level metadata spillover,
its review supports cytosolic maltose O-acetyltransferase activity rather than
LPS/lipid-A biosynthesis. Updated, validated, and rendered
`modules/lipopolysaccharide_biosynthesis.yaml` with the two LPS candidates and
kept `maa` outside the module.

Completed the second cell-envelope split,
`cell_division_regulatory_spillovers`. Fetched, ran Asta, curated, validated,
and rendered `sulA`, `PP_2199`, and `PP_2352`, then extended the existing
`modules/divisome_z_ring_septation_boundary.yaml`. `sulA` is retained as a
SulA-family SOS-response cell-division inhibitor/regulatory side context, while
`PP_2199` and `PP_2352` are retained as additional AFG1/ZapE-family ATPase
candidates. Unlike canonical `zapE`, the two paralogs lack direct
FtsZ-interaction evidence, so their cell-division/site annotations are kept as
candidate family context rather than promoted to fully characterized core
roles.

Completed the third cell-envelope split,
`vacj_phospholipid_asymmetry_context`. `just fetch-gene` could not resolve
`vacJ` by symbol or ordered locus, so the review was seeded from the known
UniProt accession Q88KX6 with alias `vacJ`. Fetched GOA/UniProt, ran Asta,
curated, validated, and rendered `vacJ`, then extended
`modules/mla_phospholipid_transport_boundary.yaml`. The review accepts
intermembrane phospholipid transfer and generic membrane localization for the
MlaA/VacJ-family lipoprotein, keeping the location conservative until direct
outer-membrane localization evidence is available.

Completed the fourth cell-envelope split,
`apbe_fmn_transferase_spillover`. Fetched, ran Asta, curated, validated, and
rendered `PP_2150`, then extended
`modules/ccm_heme_export_cytochrome_c_maturation_boundary.yaml`. The review
accepts `GO:7770036` flavin transferase activity as the core function, modifies
the broad transferase annotation to that specific activity, and keeps metal-ion
binding as cofactor context. The module records PP_2150 as ApbE-family
inner-membrane/periplasmic-side flavoprotein maturation context, not as a
CcmABCD heme-export subunit.

Completed the fifth cell-envelope split,
`peptidoglycan_turnover_remodeling_candidates`. Fetched by accession plus alias,
ran Asta, curated, validated, and rendered all 11 genes: `amiD`, `ampD`,
`rlpA__Q88PC1`, `mltF`, `PP_1325`, `PP_2147`, `PP_3562`, `pbpG`,
`rlpA__Q88DM1`, `PP_4971`, and `PP_5354`. Extended
`modules/peptidoglycan_biosynthesis.yaml` with a distinct turnover/remodeling
part covering amidases, RlpA/Mlt lytic transglycosylases, an LpoA-family PBP
activator candidate, a peptidase S11 PBP/remodeling enzyme, and sparse
CsiV/SleB/SUKH cell-wall candidates. All 11 gene reviews and the updated module
validate cleanly.

Partitioned the functional `module:chromosome_partition_cell_cycle` bucket.
Generated
`projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_partition.{tsv,md}`
and the completed Min-system sub-batch files
`projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_min_system.{tsv,md}`
from `projects/P_PUTIDA/partition_chromosome_cell_cycle.py`. The 37 genes split
into chromosome partition/condensation, Xer/FtsK chromosome-resolution and DNA
translocation, divisome/Z-ring/septation, MinCDE septum-site selection, Tol-Pal
envelope/division coordination, and two broad keyword spillovers.

Completed the first MinCDE sub-batch. Fetched, ran Asta, curated, and validated
`minC`, `minD`, and `minE`; fixed the `minD` review symbol from the accession
alias to `minD`; created and validated
`modules/min_system_septum_site_selection_boundary.yaml`. The real Falcon
module command was run and failed before report generation with Edison HTTP 402
Payment Required; the queued report path is
`modules/min_system_septum_site_selection_boundary-deep-research-falcon.md`.

Completed the second chromosome/cell-cycle sub-batch,
`divisome_z_ring_septation_boundary`. Fetched, ran Asta, curated, and validated
the 11 missing genes (`engB`, `PP_1309`, `zapE`, `ftsL`, `ftsQ`, `ftsA`,
`ftsB`, `dedD`, `zipA`, `PP_5090`, and `PP_5202`) and reused the already
curated `ftsZ` review. Created and validated
`modules/divisome_z_ring_septation_boundary.yaml`, regenerated the partition
outputs including
`projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_divisome.{tsv,md}`,
and removed the PP_5202 bacterial ZapA `septin ring assembly` over-propagation.
The real Falcon module command was run and failed before report generation with
Edison HTTP 402 Payment Required; the queued report path is
`modules/divisome_z_ring_septation_boundary-deep-research-falcon.md`.

Completed the third chromosome/cell-cycle sub-batch,
`chromosome_dimer_resolution_dna_translocation_boundary`. Fetched, ran Asta,
curated, and validated `xerD`, `PP_2841`, `ftsK`, and `xerC`. Created and
validated
`modules/chromosome_dimer_resolution_dna_translocation_boundary.yaml`,
regenerated the partition outputs including
`projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_xer_ftsk.{tsv,md}`,
and added `GO:0015616 DNA translocase activity` as a new precise FtsK core
activity. `xerC` and `xerD` are treated as the core XerCD tyrosine recombinase
pair, `ftsK` as the septal membrane DNA translocase, and `PP_2841` as a
related integrase-family boundary candidate outside the core dimer-resolution
system. The real Falcon module command was run and failed before report
generation with Edison HTTP 402 Payment Required; the queued report path is
`modules/chromosome_dimer_resolution_dna_translocation_boundary-deep-research-falcon.md`.

Completed the fourth chromosome/cell-cycle sub-batch,
`tol_pal_cell_division_envelope_coordination_boundary`. Fetched, ran Asta,
curated, and validated `tolQ`, `tolR`, `tolB`, and `cpoB`; reused and
revalidated the existing curated `pal` review after adding Asta retrieval; and
promoted `tolA` from the broad `module:transport_membrane_efflux` bucket as a
missing core Tol-Pal connector needed for module satisfiability. Created and
validated `modules/tol_pal_cell_division_envelope_coordination_boundary.yaml`
and generated
`projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_tol_pal.{tsv,md}`.
The `tolA` review removes nucleosome, nucleosome assembly, DNA binding, and
structural constituent of chromatin annotations as H1/H5-like InterPro
over-propagations. The real Falcon module command was run and failed before
report generation with Edison HTTP 402 Payment Required; the queued report path
is `modules/tol_pal_cell_division_envelope_coordination_boundary-deep-research-falcon.md`.

Completed the fifth chromosome/cell-cycle sub-batch,
`chromosome_partition_condensation_boundary`. Fetched, ran Asta, curated, and
validated `parB`, `PP_0693`, `PP_0694`, `PP_2161`, `PP_2412`, `PP_3700`,
`smc`, `PP_4334`, `PP_4497`, `scpA`, and `PP_5070`; promoted `PP_0002` from
`unknown:function_unknown` as the origin-proximal Soj/ParA-like candidate next
to `parB`. Created and validated
`modules/chromosome_partition_condensation_boundary.yaml` and generated
`projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_partition_condensation.{tsv,md}`.
The `parB` review removes the sporulation process spillover; `smc` modifies
sister-chromatid cohesion toward bacterial chromosome organization/condensation;
and PP_0693/PP_0694 plus the ParA-family side ATPases remain candidate
partition/condensin roles rather than all being forced into the core
chromosomal ParAB system. The real Falcon module command was run and failed
before report generation with Edison HTTP 402 Payment Required; the queued
report path is
`modules/chromosome_partition_condensation_boundary-deep-research-falcon.md`.

Closed the remaining broad keyword spillovers from
`module:chromosome_partition_cell_cycle`. Fetched, ran Asta, curated, and
validated `PP_1105`; added the missing Asta retrieval provenance to the
existing curated `tig` review and revalidated it. Generated
`projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_spillovers.{tsv,md}`.
`PP_1105` is retained as ATP-dependent DNA ligase (EC 6.5.1.1) with DNA repair
context, and `tig` remains trigger factor, a ribosome-associated FKBP-type
PPIase/chaperone for de novo cotranslational protein folding. Neither is
represented in a chromosome/cell-cycle module. The aggregate pathway worklist
now reports 37/37 primary review files and 37/37 Asta files for
`module:chromosome_partition_cell_cycle`.

Also fixed the pathway worklist review locator to prefer the direct
`suggested_review_name` review folder before accession/symbol fallback. This
prevents duplicate-symbol reviews such as `quiC1` and `quiC1_qsuB` from being
miscounted; the ppu00400 worklist row now correctly reports 20/20 primary Asta
files.

Partitioned the functional `module:motility_chemotaxis_biofilm` bucket.
Generated
`projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_partition.{tsv,md}`
and per-sub-batch ledgers from
`projects/P_PUTIDA/partition_motility_chemotaxis_biofilm.py`. The 35 genes now
split into type IV pilus biogenesis/assembly (12), fimbrial/type-I-pilus
surface-adhesion extension (2), Hcp/T6SS product-name spillover (1), alginate
envelope/export and lyase context (5), orphan MCP chemotaxis receptors (3),
sensory c-di-GMP phosphodiesterase spillover (1), DNA-binding
response-regulator spillover (1), CheY-like/membrane accessory spillovers (3),
outer-membrane flagellation-name spillover (1), flagellar
export/localization/accessory spillovers (5), and c-di-GMP flagellar brake
context (1).

Completed the first motility/biofilm sub-batches. Fetched, ran Asta, curated,
and validated `PP_1888` and `fimI`, then extended
`modules/pili_surface_adhesion_boundary.yaml` with their predicted fimbrial
structural-subunit roles next to the already curated `fimD`/`PP_1890`
chaperone-usher pair. Fetched, ran Asta, curated, and validated `PP_0655`, but
routed it out of the fimbrial module: its Hcp1-like/T6SS_Hcp domains support an
Hcp-family type VI secretion tube or secreted-effector candidate, so
`modules/bacterial_secretion_system_boundary.yaml` now carries the PP_0655
boundary context. The real Falcon module command
`just module-deep-research-falcon pili_surface_adhesion_boundary` was run and
failed before report generation with Edison HTTP 402 Payment Required; the
queued report path is
`modules/pili_surface_adhesion_boundary-deep-research-falcon.md`.

Completed the type IV pilus biogenesis sub-batch from the motility umbrella.
Fetched, ran Asta, first-pass curated, validated, and rendered `PP_0608`,
`PP_0609`, `PP_0610`, `pilE`, `pilC`, `pilF`, `PP_3480`, `PP_3481`, `pilQ`,
`PP_5081`, `pilN`, and `PP_5083`. Created, validated, and rendered
`modules/type_iv_pilus_biogenesis_boundary.yaml`, with pilin-like components,
PilC/PilM/PilN/PilO/PilP-like alignment/platform components, and PilQ/PilF
secretin/scaffold context. The module records `pilD` and `pilT` as explicit
hole-filling gaps rather than silently broadening the curated 12-gene batch.
The real Falcon module command
`just module-deep-research-falcon type_iv_pilus_biogenesis_boundary` was run
and failed before report generation with Edison HTTP 402 Payment Required; the
queued report path is
`modules/type_iv_pilus_biogenesis_boundary-deep-research-falcon.md`.

Completed the alginate envelope/export and lyase context sub-batch from the
same motility umbrella. Fetched, ran Asta, first-pass curated, validated, and
rendered `glmP`, `PP_1754`, `PP_3350`, `PP_3464`, and `PP_3774`. Extended
`modules/alginate_biosynthesis_boundary.yaml` with glmP as an
alginate-efficiency membrane factor, PP_3350/PP_3464 as alginate
export-domain candidates, and PP_1754/PP_3774 as alginate-lyase-domain
processing/catabolic candidates. The regenerated alginate sub-batch ledger now
marks all five as `CURATED` with Asta present.

Completed the orphan MCP/c-di-GMP split from the motility umbrella. Fetched,
ran Asta, first-pass curated, validated, and rendered `PP_2310`, `PP_2599`,
`PP_3950`, and `PP_4888`. Extended
`modules/orphan_mcp_aerotaxis_receptors_boundary.yaml` with `PP_2310` and
`PP_3950` as ligand-unresolved MCP transducer candidates and `PP_4888` as an
MCP receptor candidate. Routed `PP_2599` out of the MCP receptor panel and into
`modules/c_di_gmp_turnover_boundary.yaml` because its GAF/HAMP/HD-GYP/HD-PDEase
and cyclic-di-GMP phosphodiesterase-family evidence supports a sensory
cyclic-guanylate phosphodiesterase candidate. This left the chemotaxis
accessory/response-regulator and flagellar spillover groups for the final
motility pass. The real taxon-aware Falcon command
`just module-pathway-deep-research-falcon orphan_mcp_aerotaxis_receptors_boundary module:motility_chemotaxis_biofilm PSEPK`
was run and failed before report generation with Edison HTTP 402 Payment
Required; the queued report path is
`projects/P_PUTIDA/deep-research/PSEPK__orphan_mcp_aerotaxis_receptors_boundary__module-motility-chemotaxis-biofilm-deep-research-falcon.md`.

Completed the chemotaxis accessory/response-regulator split from the motility
umbrella. Fetched, ran Asta, first-pass curated, and validated `PP_2403`,
`PP_3757`, `PP_3771`, and `PP_4331`. Routed `PP_2403` out of chemotaxis into
`modules/orphan_two_component_regulators_boundary.yaml` because its OmpR/PhoB
DNA-binding response-regulator architecture is stronger than the CheY-like
product-name spillover. Extended
`modules/chemotaxis_adaptation_accessory_boundary.yaml` with `PP_3757` as a
compact CheY-like receiver-domain candidate and with `PP_3771`/`PP_4331` only
as low-confidence membrane accessory candidates. This left only the flagellar
spillover group for the final motility pass. The real
taxon-aware Falcon commands
`just module-pathway-deep-research-falcon chemotaxis_adaptation_accessory_boundary module:motility_chemotaxis_biofilm PSEPK`
and
`just module-pathway-deep-research-falcon orphan_two_component_regulators_boundary module:motility_chemotaxis_biofilm PSEPK`
were run and failed before report generation with Edison HTTP 402 Payment
Required; no Falcon report files were produced for those two attempts.

Completed the final flagellar spillover split from the motility umbrella.
Fetched, ran Asta, first-pass curated, and validated `ycfJ`, `PP_4328`,
`PP_4329`, `PP_4342`, `flhF`, `PP_4377`, and `ycgR`. Routed `ycfJ` to
`modules/transport_envelope_spillover_boundary.yaml` as an outer-membrane
lipoprotein/surface-antigen-family spillover rather than a core flagellar
regulator. Extended `modules/flagellar_export_assembly_boundary.yaml` with
`PP_4328` as a FliK-like hook-control candidate, `PP_4329` as a short
FlhB-family exporter distinct from canonical `flhB`/PP_4352, `PP_4342` as a
FlhG/FleN-family ATPase candidate with the MinD-family cell-division overcall
removed, `flhF` as a flagellar-biosynthesis GTPase with SRP-targeting
spillovers removed, and `PP_4377` as a FlaG-domain accessory candidate. Routed
`ycgR` to `modules/flagellar_motor_switch_stator_boundary.yaml` as a PilZ-domain
c-di-GMP-dependent flagellar motor brake. The regenerated motility ledger now
reports 35/35 genes with curated reviews and Asta reports.

Completed the UniPathway `UPA00060` / `thiamine_biosynthesis` support-bucket
registration. Added the missing worklist mapping, regenerated
`projects/P_PUTIDA/data/psepk_pathway_worklist.tsv`, and generated
`projects/P_PUTIDA/batches/UPA00060_thiamine_biosynthesis.{tsv,md}`. All 9
UniPathway members already had review folders, Asta reports, and curated YAMLs;
`pet`/PP_3185 is the only UniPathway-primary member and is retained as
TenA-family thiamine salvage/context inside the existing thiamine module.

No duplicate Falcon run was needed for `UPA00060`: the completed `ppu00730`
generic and PSEPK-specific Falcon reports already cover the thiamine module
boundary. Revalidated the 9 UPA00060 gene reviews and the existing
`modules/thiamine_biosynthesis.yaml`; the only gene-level warnings were the
expected "Asta not cited" first-pass notices where Asta served as
identity/context retrieval.

Completed the UniPathway `UPA01010` / `nad_biosynthesis_and_nicotinate_metabolism`
support-bucket registration. Added the worklist mapping, generated
`projects/P_PUTIDA/batches/UPA01010_nad_biosynthesis_and_nicotinate_metabolism.{tsv,md}`,
and added missing Asta retrieval reports for the two UniPathway-primary
regulator genes `nicR` and `nicS`. The seven catalytic members (`nicA`, `nicB`,
`nicC`, `nicX`, `nicD`, `nicF`, and `maiA`) already belonged to the completed
`ppu00760` NAD/nicotinate module.

No duplicate Falcon run was needed for `UPA01010`: the completed `ppu00760`
generic and PSEPK-specific Falcon reports already cover the aerobic
nicotinate-catabolism branch. Revalidated all 9 UPA01010 gene reviews and the
existing `modules/nad_biosynthesis_and_nicotinate_metabolism.yaml`; all passed.

Completed the UniPathway `UPA00232` / `ubiquinone_biosynthesis` support-bucket
registration. No new gene curation was needed: all 11 UniPathway members
(`coq7`, `ubiG`, `ubiE`, `ubiJ`, `ubiB`, `visC`, `ubiH`, `ubiD`, `ubiK`,
`ubiC`, and `ubiA`) already had review folders, Asta reports, curated YAMLs, and
rendered pages from the prior `ppu00130` ubiquinone checkpoint. Added the
worklist mapping to `ubiquinone_biosynthesis`, generated
`projects/P_PUTIDA/batches/UPA00232_ubiquinone_biosynthesis.{tsv,md}`, and
validated all 11 gene reviews plus the existing module.

Main UPA00232 lesson: this is not a separate pathway from `ppu00130`; it is the
strict UniPathway cross-reference for the same ubiquinone route. The three
UniPathway-primary genes `ubiJ`, `ubiB`, and `ubiK` remain accessory/context
factors inside the existing module, while `visC` remains the UbiI-like
2-polyprenylphenol hydroxylase candidate. The completed `ppu00130` generic and
PSEPK Falcon reports are reused for this support bucket rather than launching a
duplicate Falcon job.

Completed the combined first-pass `UPA00664` / `UPA00666`
`bacterial_lipoprotein_maturation` checkpoint. Fetched, ran Asta, curated,
validated, and rendered the two missing UniPathway members: `lgt` / Q88CN8 /
PP_5142 and `lnt` / Q88DN4 / PP_4790. Reused already-curated `lspA` / Q88Q91 /
PP_0604 as the UniPathway UPA00665 middle step. Created and validated
`modules/bacterial_lipoprotein_maturation.yaml`, registered worklist mappings
for UPA00664, UPA00665, and UPA00666, and generated paired batch checklists:
`projects/P_PUTIDA/batches/UPA00664_bacterial_lipoprotein_maturation.{tsv,md}`
and
`projects/P_PUTIDA/batches/UPA00666_bacterial_lipoprotein_maturation.{tsv,md}`.

Falcon was attempted with the real commands for the shared
`bacterial_lipoprotein_maturation` module and for both taxon-aware UniPathway
buckets. All three failed before report generation with Edison HTTP 402 Payment
Required:
`modules/bacterial_lipoprotein_maturation-deep-research-falcon.md`,
`projects/P_PUTIDA/deep-research/PSEPK__bacterial_lipoprotein_maturation__upa00664-deep-research-falcon.md`,
and
`projects/P_PUTIDA/deep-research/PSEPK__bacterial_lipoprotein_maturation__upa00666-deep-research-falcon.md`
remain queued for a later provider rerun.

Main lipoprotein-maturation lessons: PSEPK has the canonical Lgt-LspA-Lnt
inner-membrane maturation sequence. `lgt` has the specific
phosphatidylglycerol-prolipoprotein diacylglyceryl transferase MF term; `lspA`
remains the signal peptidase II context already owned by the broad protein
export batch; and `lnt` should use the more specific `GO:0016410`
N-acyltransferase activity rather than the broad InterPro2GO acyltransferase
parent. Lol-dependent trafficking and mature lipoprotein functions stay outside
this module.

Completed the first-pass `UPA00637` /
`osmoregulated_periplasmic_glucan_biosynthesis` checkpoint. Fetched, ran Asta,
curated, validated, and rendered both UniPathway members: `opgH` / Q88D04 /
PP_5025 and `opgG` / Q88D03 / PP_5026. Created and validated
`modules/osmoregulated_periplasmic_glucan_biosynthesis.yaml`, registered the
worklist mapping, and generated
`projects/P_PUTIDA/batches/UPA00637_osmoregulated_periplasmic_glucan_biosynthesis.{tsv,md}`.

Both Falcon calls for `osmoregulated_periplasmic_glucan_biosynthesis` failed
before report generation with Edison HTTP 402 Payment Required: the generic
module report
`modules/osmoregulated_periplasmic_glucan_biosynthesis-deep-research-falcon.md`
and the taxon-aware report
`projects/P_PUTIDA/deep-research/PSEPK__osmoregulated_periplasmic_glucan_biosynthesis__upa00637-deep-research-falcon.md`
remain queued for a later provider rerun. The real taxon-aware command resolved
the expected two-gene candidate set.

Main UPA00637 lessons: the pathway is a compact OPG cell-envelope glycan module
with `opgH` as the inner-membrane GT2/OpgH hexosyltransferase and `opgG` as a
periplasmic OpgD/OpgG-family carbohydrate-binding OPG component. Keep this
module separate from alginate, LPS, peptidoglycan, cellulose, and generic
exopolysaccharide buckets. GO has useful generic glucan/beta-glucan process
terms, but no OPG-specific process term was introduced in this first pass.

Completed the first-pass `UPA00694` /
`bacterial_cellulose_biosynthesis` checkpoint. Fetched, ran Asta, curated,
validated, and rendered the two UniPathway-primary members `bcsB` / Q88JL3 /
PP_2636 and `PP_2638` / Q88JL1. Reused already-curated `bcsA` / Q88JL4 /
PP_2635 as the UDP-forming cellulose synthase catalytic member. Created and
validated `modules/bacterial_cellulose_biosynthesis.yaml`, registered the
worklist mapping, and generated
`projects/P_PUTIDA/batches/UPA00694_bacterial_cellulose_biosynthesis.{tsv,md}`.

Both Falcon calls for `bacterial_cellulose_biosynthesis` failed before report
generation with Edison HTTP 402 Payment Required: the generic module report
`modules/bacterial_cellulose_biosynthesis-deep-research-falcon.md` and the
taxon-aware report
`projects/P_PUTIDA/deep-research/PSEPK__bacterial_cellulose_biosynthesis__upa00694-deep-research-falcon.md`
remain queued for a later provider rerun. The real taxon-aware command resolved
the expected three-gene candidate set: `bcsA` / PP_2635 / Q88JL4, `bcsB` /
PP_2636 / Q88JL3, and `PP_2638` / PP_2638 / Q88JL1.

Main UPA00694 lessons: use a bacterial Bcs module, not the existing plant
cellulose synthase complex module. `bcsA` supplies the UDP-forming cellulose
synthase catalytic step, `bcsB` is a single-pass inner-membrane/c-di-GMP
regulatory subunit tightly associated with BcsA, and `PP_2638` is a BcsC-like
outer-membrane/export accessory required for maximal bacterial cellulose
synthesis. Keep this separate from alginate, OPG, LPS, peptidoglycan, and broad
exopolysaccharide buckets.

Completed the first-pass `UPA00286` / `alginate_biosynthesis_boundary`
checkpoint. Added missing Asta retrieval reports for `algE` / Q88NC8 / PP_1284
and `algK` / Q88NC7 / PP_1285, created and validated
`modules/alginate_biosynthesis_boundary.yaml`, registered the worklist mapping,
and generated
`projects/P_PUTIDA/batches/UPA00286_alginate_biosynthesis_boundary.{tsv,md}`.
All 11 UniPathway members now have review folders, Asta reports, curated YAMLs,
and focused validation coverage.

Both Falcon calls for `alginate_biosynthesis_boundary` were run with the real
commands and failed before report generation while Edison Falcon access returns
HTTP 402 Payment Required. The generic module report
`modules/alginate_biosynthesis_boundary-deep-research-falcon.md` and the
taxon-aware report
`projects/P_PUTIDA/deep-research/PSEPK__alginate_biosynthesis_boundary__upa00286-deep-research-falcon.md`
remain queued for a later provider rerun.

Main UPA00286 lessons: this is a trans-envelope alginate
biosynthesis/export/regulatory boundary rather than a single enzyme-only route.
It consolidates `algD` precursor formation, `alg8`/`alg44`
polymerization/activation, `algF`/`algJ`/`algI`/`algX`/`algG`
modification/maturation, `algE`/`algK` export/scaffold context, and `algB`
regulation. The members are split across `ppu00051`, `ppu00543`, `ppu02020`,
and UniPathway-only buckets in the source pathway maps, so this dedicated module
is preferable to forcing `UPA00286` into fructose/mannose metabolism or the
broader exopolysaccharide boundary.

Completed the first-pass `UPA00098` /
`arginine_proline_metabolism` support checkpoint. Reused the existing broad
arginine/proline metabolism module but updated its proline
biosynthesis/interconversion part to explicitly include all five UniPathway
members: `proB`, `proA`, `proC`, `proI`, and `ocd__Q88H32`. Generated
`projects/P_PUTIDA/batches/UPA00098_arginine_proline_metabolism.{tsv,md}` and
registered the worklist mapping.

All five UPA00098 gene reviews were already present, Asta-backed, curated, and
valid. Focused validation passed for `proB`, `ocd__Q88H32`, `proC`, `proA`,
and `proI`; each has the existing non-blocking warning that annotation reviews
do not directly cite the available Asta file.

Both Falcon calls for the UPA00098 support pass failed before report generation
with Edison HTTP 402 Payment Required: the generic module report
`modules/arginine_proline_metabolism-deep-research-falcon.md` and the
taxon-aware report
`projects/P_PUTIDA/deep-research/PSEPK__arginine_proline_metabolism__upa00098-deep-research-falcon.md`
remain queued for a later provider rerun. The taxon-aware command resolved the
expected five-gene candidate set.

Main UPA00098 lessons: the pathway is not a new standalone module. It is the
proline biosynthesis/interconversion subroute within the existing
arginine/proline boundary: `proB` and `proA` route glutamate toward
glutamate-5-semialdehyde/P5C, `proC` and `proI` reduce P5C to proline, and
`ocd__Q88H32` supplies the ornithine cyclodeaminase route from ornithine to
proline.

Completed the first-pass `UPA00117` / `l_carnitine_dehydrogenation`
checkpoint. Fetched, Asta-backed, curated, validated, and rendered `lcdH` /
Q88R32 / PP_0302. Created and validated
`modules/l_carnitine_dehydrogenation.yaml`, registered the worklist mapping,
and generated
`projects/P_PUTIDA/batches/UPA00117_l_carnitine_dehydrogenation.{tsv,md}`.

Both Falcon calls for `l_carnitine_dehydrogenation` failed before report
generation with Edison HTTP 402 Payment Required: the generic module report
`modules/l_carnitine_dehydrogenation-deep-research-falcon.md` and the
taxon-aware report
`projects/P_PUTIDA/deep-research/PSEPK__l_carnitine_dehydrogenation__upa00117-deep-research-falcon.md`
remain queued for a later provider rerun. The taxon-aware command resolved the
expected single-gene candidate set: `lcdH` / PP_0302 / Q88R32.

Main UPA00117 lessons: this is a satisfiable single-enzyme carnitine
metabolism module. LcdH is the cytoplasmic NAD+-dependent L-carnitine
dehydrogenase that oxidizes L-carnitine to 3-dehydrocarnitine. The
InterPro-derived fatty-acid metabolic process annotation was marked
over-annotated because the local evidence supports carnitine metabolism, not a
direct fatty-acid metabolism role. Carnitine uptake and downstream
3-dehydrocarnitine utilization remain adjacent context until a later batch
connects specific genes.

Completed the first-pass `UPA00212` /
`mcl_pha_monomer_supply_from_fas` checkpoint. The existing `phaG` review was
already curated and valid, with direct support from PMID:9727022, UniProt, and
the gene-level Falcon report; ran Asta for current first-pass provider coverage
and confirmed it did not add curation-changing direct evidence. Created and
validated `modules/mcl_pha_monomer_supply_from_fas.yaml`, registered the
worklist mapping, and generated
`projects/P_PUTIDA/batches/UPA00212_mcl_pha_monomer_supply_from_fas.{tsv,md}`.

Both Falcon calls for `mcl_pha_monomer_supply_from_fas` failed before report
generation with Edison HTTP 402 Payment Required: the generic module report
`modules/mcl_pha_monomer_supply_from_fas-deep-research-falcon.md` and the
taxon-aware report
`projects/P_PUTIDA/deep-research/PSEPK__mcl_pha_monomer_supply_from_fas__upa00212-deep-research-falcon.md`
remain queued for a later provider rerun. The taxon-aware command did resolve
the expected candidate set: `phaG` / PP_1408 / O85207.

Main UPA00212 lessons: this is a satisfiable single-gene PhaG bridge from de
novo fatty-acid synthesis to medium-chain-length PHA monomer supply. PhaG
supplies 3-hydroxyacyl-CoA monomers from ACP-bound fatty-acid-synthesis
intermediates, but the module remains direction-neutral because the
physiological mechanism is still debated. PhaC1/PhaC2 polymerization and
alternative beta-oxidation/PhaJ monomer supply remain adjacent PHA biology
outside this single-gene UniPathway member set.

Completed the first-pass `UPA00729` /
`trna_ms2io6a37_hydroxylation` checkpoint. The existing `miaE` review already
accepted the experimental and electronic GO:0045301 tRNA hydroxylase
annotations and validated cleanly; ran Asta for current gene-level coverage,
created and validated `modules/trna_ms2io6a37_hydroxylation.yaml`, registered
the worklist mapping, and regenerated
`projects/P_PUTIDA/batches/UPA00729_trna_ms2io6a37_hydroxylation.{tsv,md}`.

Both Falcon calls for `trna_ms2io6a37_hydroxylation` failed before report
generation with Edison HTTP 402 Payment Required: the generic module report
`modules/trna_ms2io6a37_hydroxylation-deep-research-falcon.md` and the
taxon-aware report
`projects/P_PUTIDA/deep-research/PSEPK__trna_ms2io6a37_hydroxylation__upa00729-deep-research-falcon.md`
remain queued for a later provider rerun.

Main UPA00729 lessons: this is a satisfiable single-enzyme terminal tRNA
hypermodification step. MiaE is a non-heme diiron monooxygenase that
hydroxylates ms2i6A37 in selected tRNAs to ms2io6A37. Upstream MiaA/MiaB
formation of the ms2i6A37 substrate is recorded as substrate-supply context,
not part of the current one-gene UniPathway membership set.

Completed the first-pass `UPA00989` / `trna_m7g46_methylation` checkpoint.
Fetched, Asta-backed, curated, validated, and rendered `trmB` / Q88CS7 /
PP_5103. Created and validated `modules/trna_m7g46_methylation.yaml`,
registered the worklist mapping, and generated
`projects/P_PUTIDA/batches/UPA00989_trna_m7g46_methylation.{tsv,md}`.

Both Falcon calls for `trna_m7g46_methylation` failed before report generation
with Edison HTTP 402 Payment Required: the generic module report
`modules/trna_m7g46_methylation-deep-research-falcon.md` and the taxon-aware
report
`projects/P_PUTIDA/deep-research/PSEPK__trna_m7g46_methylation__upa00989-deep-research-falcon.md`
remain queued for a later provider rerun. The taxon-aware command resolved the
expected single-gene candidate set: `trmB` / PP_5103 / Q88CS7.

Main UPA00989 lessons: this is a satisfiable single-enzyme tRNA-modification
module. TrmB is the SAM-dependent tRNA
(guanine(46)-N7)-methyltransferase that forms m7G46 in tRNA. The broad RNA
guanine-N7 methylation parent was retained as non-core context, while the
TreeGrafter tRNA methyltransferase-complex annotation was marked
over-annotated because first-pass evidence supports the enzyme/reaction but
not a stable PSEPK methyltransferase complex.

Completed the first-pass `UPA00345` / `efp_translation_stall_rescue`
checkpoint. The usual symbol-based fetch did not resolve `efp`, so the review
folder was seeded by accession alias Q88LS0 and then corrected to
`gene_symbol: efp`. Fetched, Asta-backed, curated, validated, and rendered
`efp` / Q88LS0 / PP_1858. Created and validated
`modules/efp_translation_stall_rescue.yaml`, registered the worklist mapping,
and generated
`projects/P_PUTIDA/batches/UPA00345_efp_translation_stall_rescue.{tsv,md}`.

Both Falcon calls for `efp_translation_stall_rescue` failed before report
generation with Edison HTTP 402 Payment Required: the generic module report
`modules/efp_translation_stall_rescue-deep-research-falcon.md` and the
taxon-aware report
`projects/P_PUTIDA/deep-research/PSEPK__efp_translation_stall_rescue__upa00345-deep-research-falcon.md`
remain queued for a later provider rerun. The taxon-aware command resolved the
expected single-gene candidate set: `efp` / PP_1858 / Q88LS0.

Main UPA00345 lessons: this is a satisfiable single-gene translation-factor
module. EF-P is a cytoplasmic elongation factor that stimulates peptide-bond
formation and rescues stalled cytosolic ribosomes, especially polyproline
stalls. EarP-dependent Arg32 rhamnosylation and dTDP-rhamnose supply are
activation context owned by adjacent modules, not members of the UPA00345
single-gene bucket. Broad `regulation of translation` and `peptide biosynthetic
process` annotations were retained as non-core context.

Completed the first-pass `UPA00191` / `bacterial_fatty_acid_beta_oxidation`
support checkpoint. Fetched, Asta-backed, curated, validated, and rendered
`rubA` / Q88C68 / PP_5315. Extended
`modules/bacterial_fatty_acid_beta_oxidation.yaml` with RubA under the existing
alkane/rubredoxin electron-transfer boundary node, registered the worklist
mapping, and generated
`projects/P_PUTIDA/batches/UPA00191_bacterial_fatty_acid_beta_oxidation.{tsv,md}`.

The generic Falcon module report already exists for
`bacterial_fatty_acid_beta_oxidation`, so it was reused. The UPA00191-specific
Falcon module+pathway+PSEPK call was attempted and failed before report
generation with Edison HTTP 402 Payment Required; the expected output
`projects/P_PUTIDA/deep-research/PSEPK__bacterial_fatty_acid_beta_oxidation__upa00191-deep-research-falcon.md`
remains queued for a later provider rerun. The taxon-aware command resolved the
expected single-gene candidate set: `rubA` / PP_5315 / Q88C68.

Main UPA00191 lessons: RubA is a small cytoplasmic rubredoxin electron-transfer
protein with an alkane/hydrocarbon oxidation pathway context. This support
bucket extends the upstream alkane/rubredoxin boundary of the beta-oxidation
module and should not be interpreted as a core beta-oxidation spiral step. The
review accepts electron-transfer activity and alkane catabolic process context,
while keeping metal/iron binding and cytoplasm as non-core supporting features.

Completed the first-pass `UPA00252` / `porphyrin_metabolism_boundary` support
checkpoint. The usual symbol-based fetch did not resolve `PP_0189`, so the
review folder was seeded by accession alias Q88RE2. Fetched, Asta-backed,
curated, validated, and rendered `PP_0189`; reused already-curated `hemH` as
the ferrochelatase/protoheme context member. Extended
`modules/porphyrin_metabolism_boundary.yaml` with a `PP_0189` late-protoheme
support annoton, registered the worklist mapping, and generated
`projects/P_PUTIDA/batches/UPA00252_porphyrin_metabolism_boundary.{tsv,md}`.

Both Falcon calls for `porphyrin_metabolism_boundary` / `UPA00252` were
attempted and failed before report generation with Edison HTTP 402 Payment
Required: the generic module report
`modules/porphyrin_metabolism_boundary-deep-research-falcon.md` and the
taxon-aware report
`projects/P_PUTIDA/deep-research/PSEPK__porphyrin_metabolism_boundary__upa00252-deep-research-falcon.md`
remain queued for a later provider rerun. The taxon-aware command resolved the
expected two-gene candidate set: `PP_0189` / PP_0189 / Q88RE2 and `hemH` /
PP_0744 / Q88PV4.

Main UPA00252 lessons: this is best treated as a protoheme/heme support view of
the existing porphyrin/tetrapyrrole boundary module, not a standalone pathway.
`PP_0189` is an inner-membrane HemY_N/TPR-associated support protein annotated
by UniProt to a late step of protoheme IX synthesis, but first-pass evidence
does not justify assigning a specific molecular function. Its broad `heme
metabolic process` annotation was narrowed to proposed replacement `heme
biosynthetic process`; `hemH` remains the catalytically explicit ferrochelatase
step completing protoheme formation.

Completed the first-pass `UPA00659` /
`bacterial_fatty_acid_beta_oxidation` support checkpoint. Fetched,
Asta-backed, curated, validated, and rendered `PP_4030`; reused already-curated
`fadE`, `fadB`, and `fadA__Q88L01` as the core beta-oxidation context members.
Extended `modules/bacterial_fatty_acid_beta_oxidation.yaml` with a PP_4030
auxiliary dienoyl-CoA isomerase candidate node, registered the worklist
mapping, and generated
`projects/P_PUTIDA/batches/UPA00659_bacterial_fatty_acid_beta_oxidation.{tsv,md}`.

The generic Falcon module report already exists for
`bacterial_fatty_acid_beta_oxidation`, so it was reused. The UPA00659-specific
Falcon module+pathway+PSEPK call was attempted and failed before report
generation with Edison HTTP 402 Payment Required; the expected output
`projects/P_PUTIDA/deep-research/PSEPK__bacterial_fatty_acid_beta_oxidation__upa00659-deep-research-falcon.md`
remains queued for a later provider rerun. The taxon-aware command resolved the
expected four-gene candidate set: `fadE` / PP_1893 / Q88LN6, `fadB` /
PP_2136 / Q88L02, `fadA__Q88L01` / PP_2137 / Q88L01, and `PP_4030` /
PP_4030 / Q88FQ7.

Main UPA00659 lessons: this is a UniPathway support view of the existing
bacterial beta-oxidation module. `fadE`, `fadB`, and `fadA__Q88L01` already
cover the dehydrogenation, hydratase/dehydrogenase, and thiolase core. PP_4030
adds a cytoplasmic enoyl-CoA hydratase/isomerase-family auxiliary candidate,
with broad `isomerase activity` modified toward proposed replacement
`delta(3,5)-delta(2,4)-dienoyl-CoA isomerase activity` from the PANTHER
subfamily call. Substrate specificity remains unresolved.

Completed the first-pass `UPA00529` /
`glycine_betaine_biosynthesis_boundary` checkpoint. Fetched and Asta-backed
the missing UniPathway-only regulator `betI`, tightened the existing `betA` and
`betB` reviews so their rationale is glycine-betaine/osmoprotection rather
than folate one-carbon context, curated `betI` as a TetR/BetI-family
DNA-binding transcriptional repressor, and created/validated
`modules/glycine_betaine_biosynthesis_boundary.yaml`. Regenerated
`projects/P_PUTIDA/batches/UPA00529_glycine_betaine_biosynthesis_boundary.{tsv,md}`
and the pathway worklist.

Both Falcon calls for `glycine_betaine_biosynthesis_boundary` failed before
report generation with Edison HTTP 402 Payment Required: the generic module
report `modules/glycine_betaine_biosynthesis_boundary-deep-research-falcon.md`
and the taxon-aware report
`projects/P_PUTIDA/deep-research/PSEPK__glycine_betaine_biosynthesis_boundary__upa00529-deep-research-falcon.md`
remain queued for a later provider rerun. While rerunning the taxon-aware
command, fixed `scripts/module_pathway_taxon_deep_research_wrapper.py` so
UniPathway buckets use the membership table before falling back to primary
partition rows; the corrected UPA00529 prompt now includes `betA`, `betB`, and
`betI` instead of only the primary UniPathway row.

Main UPA00529 lessons: the satisfiable catalytic route is BetA choline
dehydrogenase producing betaine aldehyde and BetB NAD+-dependent betaine
aldehyde dehydrogenase producing glycine betaine. BetA's family-assigned
second oxidation is retained but tracked as an in vivo division-of-labor
question because BetB is the dedicated BADH. BetI belongs in the module as a
regulatory boundary component repressing `betT`/`betAB`, not as a catalytic
glycine-betaine biosynthesis enzyme. Transporters and unassigned choline
dehydrogenase paralogs remain outside this UPA00529 module until separately
assigned.

Completed the first-pass `UPA00539` / `pqq_biosynthesis` checkpoint. Created
and validated `modules/pqq_biosynthesis.yaml`, fetched the two missing PqqD
paralog review folders (`pqqD1` and `pqqD2`) by UniProt accession with the
correct aliases, ran Asta for all seven UPA00539 genes (`pqqE`, `pqqD1`,
`pqqC`, `pqqB`, `pqqA`, `pqqF`, and `pqqD2`), curated the new PqqD reviews, and
regenerated `projects/P_PUTIDA/batches/UPA00539_pqq_biosynthesis.{tsv,md}`.
All seven gene reviews and the new module validate cleanly.

Both Falcon calls for `pqq_biosynthesis` failed before report generation with
Edison HTTP 402 Payment Required: the generic module report
`modules/pqq_biosynthesis-deep-research-falcon.md` and the taxon-aware report
`projects/P_PUTIDA/deep-research/PSEPK__pqq_biosynthesis__upa00539-deep-research-falcon.md`
remain queued for a later provider rerun.

Main UPA00539 lessons: the satisfiable KT2440 PQQ route is PqqA precursor
peptide supply, PqqD-family PqqA presentation to PqqE, PqqE radical-SAM Glu-Tyr
cross-linking, PqqF proteolytic processing, PqqB oxygenase/hydroxylase
maturation chemistry, and PqqC terminal pyrroloquinoline-quinone synthase
activity. The two KT2440 PqqD paralogs are retained as PQQ-biosynthesis
components, but their division of labor remains unresolved. Generic
`GO:0048038` quinone binding on PqqD1/PqqD2 is marked over-annotated because
the supported role is PqqA peptide binding/presentation. Literature mentions a
`pqqFABCDEG` region, but current local UniProt/pathway metadata assign PP_0382
as `davA`, not an unambiguous UPA00539 `pqqG`; the module therefore excludes
`pqqG` until identifiers are reconciled.

Completed the first-pass `UPA00219` / `peptidoglycan_biosynthesis` main
UniPathway route checkpoint. Fetched the two missing UniPathway-primary review
folders, `PP_1451` / Q88MW7 / PP_1451 and `ddl` / A0A140FWM5 / PP_5673, ran
Asta, curated and validated both reviews, and reused the 23 already-curated
peptidoglycan members in the batch. Extended and validated
`modules/peptidoglycan_biosynthesis.yaml` with the standalone `ddl` paralog and
the `PP_1451`/`PP_2320` YkuD/L,D-transpeptidase-family remodeling candidates,
registered the worklist mapping, and generated
`projects/P_PUTIDA/batches/UPA00219_peptidoglycan_biosynthesis.{tsv,md}`.

The generic peptidoglycan Falcon report remains absent after the earlier real
`just module-deep-research-falcon peptidoglycan_biosynthesis` run failed with
Edison HTTP 402 Payment Required. The real taxon-aware Falcon command for
`peptidoglycan_biosynthesis` / UPA00219 / PSEPK was run and resolved the
expected 25-gene candidate set, but Edison again returned HTTP 402 before
report generation. The queued report path is
`projects/P_PUTIDA/deep-research/PSEPK__peptidoglycan_biosynthesis__upa00219-deep-research-falcon.md`.

Main UPA00219 lessons: this is the main UniPathway route view of the existing
peptidoglycan module, while UPA00544 is the recycling/salvage arm. `ddl` is a
third cytoplasmic D-Ala-D-Ala ligase paralog to track alongside `ddlA` and
`ddlB`; `PP_1451` is best kept as a predicted signal-peptide-bearing
YkuD/L,D-transpeptidase-family remodeling candidate pending substrate and
paralog-specific evidence.

Completed the first-pass `UPA00544` / `peptidoglycan_biosynthesis` recycling
checkpoint. Fetched the missing UniPathway-primary `mpl` / Q88QE7 / PP_0547
review folder by accession alias, ran Asta, curated and validated
`genes/PSEPK/mpl/mpl-ai-review.yaml`, and reused already-curated `amgK`,
`murU`, `anmK`, `mupP`, and `nagZ` as the rest of the recycling/salvage set.
Extended and validated `modules/peptidoglycan_biosynthesis.yaml` with a
discrete MurNAc/anhMurNAc and muropeptide recycling arm, registered the worklist
mapping, and generated
`projects/P_PUTIDA/batches/UPA00544_peptidoglycan_biosynthesis.{tsv,md}`.

Both Falcon calls for `peptidoglycan_biosynthesis` / UPA00544 were run with the
real commands and failed before report generation while Edison Falcon access
returns HTTP 402 Payment Required. The generic module report
`modules/peptidoglycan_biosynthesis-deep-research-falcon.md` and the
taxon-aware report
`projects/P_PUTIDA/deep-research/PSEPK__peptidoglycan_biosynthesis__upa00544-deep-research-falcon.md`
remain queued for a later provider rerun. The taxon-aware command resolved the
expected six-gene candidate set: `amgK`, `murU`, `anmK`, `mpl`, `mupP`, and
`nagZ`.

Main UPA00544 lessons: this is a recycling/salvage view inside the
peptidoglycan module, not a separate pathway. `nagZ` starts muropeptide
processing as a beta-N-acetylhexosaminidase, `anmK` handles anhMurNAc,
`mupP`/`amgK`/`murU` provide the Pseudomonas MurNAc-to-UDP-MurNAc shortcut, and
`mpl` reattaches recycled L-Ala-gamma-D-Glu-meso-DAP tripeptide to UDP-MurNAc.
Keep this separated from de novo MurA/MurB/MurC-F precursor synthesis while
letting both arms feed the same lipid-linked peptidoglycan route.

Completed the first-pass `UPA00094` / `fatty_acid_biosynthesis` ACP support
checkpoint. Fetched the UniPathway-primary `acpP` / Q88LL5 / PP_1915 review
folder, ran Asta, curated and validated `genes/PSEPK/acpP/acpP-ai-review.yaml`,
and reused already-curated `accB`, `fabG`, `fabF`, `PP_3303`, `fabA`, `fabB`,
and `fabV` as FAS-II context. Extended and validated
`modules/fatty_acid_biosynthesis.yaml` with `UniPathway:UPA00094` evidence and
an explicit AcpP acyl-carrier annoton, registered the worklist mapping, and
generated `projects/P_PUTIDA/batches/UPA00094_fatty_acid_biosynthesis.{tsv,md}`.

The existing generic fatty-acid-biosynthesis Falcon report is reused from
`modules/fatty_acid_biosynthesis-deep-research-falcon.md`. The real taxon-aware
Falcon command for `fatty_acid_biosynthesis` / UPA00094 / PSEPK was run and
resolved the expected eight-gene set (`accB`, `fabG`, `acpP`, `fabF`,
`PP_3303`, `fabA`, `fabB`, and `fabV`), but Edison returned HTTP 402 Payment
Required before report generation. The queued report path is
`projects/P_PUTIDA/deep-research/PSEPK__fatty_acid_biosynthesis__upa00094-deep-research-falcon.md`.

Main UPA00094 lessons: this is an ACP-linked support view of the already
completed type-II fatty-acid-biosynthesis module, not a separate pathway. The
only UniPathway-primary unresolved member was `acpP`; adding AcpP explicitly
makes the module satisfiability model show the carrier pool that all malonyl-ACP
and acyl-ACP reactions depend on. The other UPA00094 members are already covered
by acetyl-CoA-carboxylase and Fab enzyme parts in the existing FAS-II module.

Completed the RNA-degradation `ppu03018` / `bacterial_rna_degradation`
checkpoint. Registered the new module mapping, created and validated
`modules/bacterial_rna_degradation.yaml`, fetched the missing primary review
folders (`rhlB`, `deaD`, `rne`, `recQ`, `pcnB`, `pnp`, `rhlE-I`, `rnr`,
`rhlE`, `rppH`, and `rho`), ran Asta for those genes plus the already fetched
`hfq`, curated and validated the new reviews, and added Asta provenance to the
existing overlap reviews (`ppkB`, `groEL`, `eno`, `dnaK`, `hfq`, and `ppk`).
The batch checklist now has 17/17 review folders, 17/17 curated reviews, and
17/17 Asta reports. The real Falcon module and module+pathway commands were
attempted and both failed at Edison task creation with HTTP 402.

Main ppu03018 lesson: this is an RNA-turnover boundary module centered on
RppH-mediated 5' end activation, RNase E cleavage, PcnB polyadenylation,
PNPase/RNase R exonucleolytic decay, and DEAD-box RNA helicase remodeling.
`hfq` and `rho` are retained as RNA-stability/transcription-termination
context rather than ribonucleases. `eno`, `dnaK`, `groEL`, `ppk`, and `ppkB`
are useful degradosome/proteostasis/polyphosphate side context, while `recQ`
is curated as a DNA-maintenance helicase spillover and not as an RNA-degradation
enzyme.

Completed the DNA-replication `ppu03030` / `bacterial_dna_replication`
checkpoint. Registered the new module mapping, created and validated
`modules/bacterial_dna_replication.yaml`, fetched the five missing primary
review folders (`dnaG`, `rnhB`, `PP_3893`, `rnhA`, and `dnaB`), ran Asta for
those five genes, curated and validated the new reviews, and added Asta
provenance to the existing overlap reviews (`dnaN`, `polA`, `PP_0353`, `ssb`,
`holC`, `dnaEA`, `holB`, `dnaQ`, `dnaX`, `ligA`, `PP_4768`, `holA`, and
`ligB`). The batch checklist now has 18/18 review folders, 18/18 curated
reviews, and 18/18 Asta reports. The real Falcon module and module+pathway
commands were attempted and both failed at Edison task creation with HTTP 402.

Main ppu03030 lesson: this is a DNA-replication boundary module centered on
the DnaB/DnaG primosome, SSB, DNA polymerase III elongation/proofreading/clamp
machinery, RNase H/PolA primer processing, and LigA nick sealing. `PP_3893` is
a DnaB-like 5'-3' helicase candidate but remains physiologically unresolved;
`PP_0353` and `PP_4768` are DnaQ-like exonuclease boundary candidates rather
than confidently assigned Pol III epsilon subunits; `ligB` is retained as a
repair-associated ligase paralog secondary to LigA. `dnaG` also exposed a
useful data-state issue: UniProt carries `GO:1990077` primosome complex, but
the fetched GOA seed did not, so the review adds a UniProt-backed `NEW`
annotation instead of dropping primosome membership from the core function.

Completed the protein-export `ppu03060` / `bacterial_protein_export`
checkpoint. Registered the new module mapping, created and validated
`modules/bacterial_protein_export.yaml`, fetched the missing review folders
for the Sec, SRP, YidC, signal-peptidase, and Tat candidates, and used
UniProt-accession alias fallbacks for `secD` (`Q88PL5`) and `secG`
(`A0A140FWQ9`). Asta reports were added for 17 genes, including the already
fetched `ftsY`, and the existing overlap reviews `secA`, `ffh`, and `ftsY`
were updated with lightweight Asta provenance. The batch checklist now has
19/19 review folders, 19/19 curated reviews, and 19/19 Asta reports. The real
Falcon module and module+pathway commands were attempted and both failed at
Edison task creation with HTTP 402.

Main ppu03060 lesson: this is a bounded bacterial protein-export module
spanning SecA/SecYEG/SecDF-YajC/SecB Sec export, Ffh/FtsY SRP targeting, YidC
membrane-protein insertion, LepB/LspA signal-peptide processing, and two
TatABC-like loci. SecD, SecF, and SecG expose a useful over-propagation case:
GOA carries protein-transporting ATPase activity, but SecA is the ATPase motor,
so those subunits are marked as over-annotated for standalone ATPase activity.
`yajC` and `secB` were kept conservative at the gene-review level because the
fetched GOA seeds did not contain the stronger UniProt accessory/translocon or
unfolded-protein-binding rows. Type I secretion and LolCDE are neighboring
envelope/export modules, not part of this ppu03060 core.

Completed the bacterial secretion-system boundary `ppu03070` /
`bacterial_secretion_system_boundary` checkpoint. Registered the new module
mapping, created and validated
`modules/bacterial_secretion_system_boundary.yaml`, regenerated the batch as a
primary-only 42-gene set, fetched the missing review folders, and used
UniProt-accession alias fallbacks for `gspF` (`Q88P05`), `PP_1449`
(`Q88MW9`), `PP_2627` (`Q88JM2`), `PP_3106` (`Q88I93`), `PP_3478`
(`Q88H83`), `PP_3483` (`Q88H78`), and `hcpC-II` (`Q88FK8`). Asta reports are
present for all 42 genes; `cyaB` already had Asta coverage and the remaining
41 reports were added in this pass. The batch checklist now has 42/42 review
folders, 42/42 curated reviews, and 42/42 Asta reports. The real Falcon module
and module+pathway commands were attempted and both failed at Edison task
creation with HTTP 402.

Main ppu03070 lesson: this is not the same module as inner-membrane protein
export. KEGG `ppu03070` has 61 total specific members, but the primary curation
batch keeps the 19 Sec/Tat/SRP/YidC overlap genes in ppu03060 and focuses here
on Xcp/Gsp type-II secretion, the PP_1449/PP_1450 two-partner/type Vb secretion
pair, multiple VgrG/Hcp/DotU/TssJ/TssM/ClpV-like T6SS loci and effectors, and
the PP_4926/CyaB type-I secretion tail. Many T6SS candidates have little or no
GOA support, so their first-pass gene reviews intentionally keep core functions
description-only or apparatus-level rather than inventing effector specificity.

Started the `ppu02020` / KEGG two-component-system umbrella by partitioning it
instead of making a 99-gene curation batch. Generated the primary-only
checklist `projects/P_PUTIDA/batches/ppu02020_two_component_system_boundary.md`
and the reproducible partition outputs
`projects/P_PUTIDA/batches/ppu02020_two_component_system_partition.tsv` and
`projects/P_PUTIDA/batches/ppu02020_two_component_system_partition.md` from
`projects/P_PUTIDA/partition_ppu02020_two_component.py`. The pathway worklist
now marks `kegg:ppu02020` as `PARTITIONED` rather than
`NEEDS_MODULE_MAPPING`.

Main ppu02020 lesson: KEGG's two-component-system map is an umbrella, not a
single satisfiable module. The 99 primary genes split into 11 buckets: Dct/Tct
dicarboxylate/tricarboxylate transport regulation (19), heavy metal/copper/zinc
response and efflux (13), pili/surface adhesion (12), iron uptake regulation
(10), ECF sigma/anti-sigma systems (10), nitrogen/phosphate/potassium
homeostasis (10), orphan/generic TCS regulators (10), osmotic/envelope/efflux
regulation (7), alginate/biofilm regulation (6), plus `dnaA` and `etp` as
one-gene side-context spillovers. `modules/two_component_relay.yaml` remains a
generic motif; concrete PSEPK work should select submodule batches from the
partition table.

Completed the ppu02020-derived `alginate_biofilm_regulation_boundary`
sub-batch. Fetched `kinB`, `algB`, `algR`, `wspC`, `fleS`, and `PP_4696` by
UniProt accession with aliases, ran Asta gene-level retrieval, curated all six
reviews, and created/validated `modules/alginate_biofilm_regulation_boundary.yaml`.
The curation keeps KinB/AlgB alginate transcription control, AlgR-family
response-regulator transcription control, WspC/CheR1 biofilm methyltransferase
context, and FleS/PP_4696 surface-behavior regulatory context as a boundary
rather than a single canonical His-Asp relay. The real Falcon
module/pathway/taxon command for this sub-batch failed with Edison HTTP 402, so
no Falcon report is cited.

Completed the ppu02020-derived `ecf_sigma_anti_sigma_boundary` sub-batch.
Fetched `PP_0161`, `PP_0162`, `PP_0351`, `PP_0352`, `PP_0667`, `PP_0703`,
`PP_0704`, `PP_0866`, `PP_3085`, and `PP_3086` by UniProt accession with
aliases, ran Asta gene-level retrieval, curated all ten reviews, and
created/validated `modules/ecf_sigma_anti_sigma_boundary.yaml`. The curation
keeps local FecR-like anti-sigma/sensor plus ECF sigma-factor pairs separate
from canonical His-Asp two-component relays, with `PP_0667` and `PP_0866`
retained as orphan boundary context. The real Falcon module/pathway/taxon
command failed with Edison HTTP 402, so no Falcon report is cited.

Completed the ppu02020-derived `metal_cation_response_efflux_boundary`
sub-batch. Fetched `czcR-I`, `czrSA`, `czcR-II`, `PP_1437`, `czcR-III`,
`PP_2157`, `copR-I`, `copR-II`, `copS`, `czcC`, `cusB`, `cusA`, and `cusF`
by UniProt accession with aliases, ran Asta gene-level retrieval, curated all
13 reviews, and created/validated
`modules/metal_cation_response_efflux_boundary.yaml`. The curation separates
CusR/CopR-like response regulators, CztS/SilS/CopS-like sensor kinases, and
the czcC-cusBAF copper/cation RND efflux locus; `cusF` had no GOA rows, so
missing copper-efflux terms were represented as `NEW` review entries backed by
UniProt/Asta evidence. The real Falcon module/pathway/taxon command failed
with Edison HTTP 402, so no Falcon report is cited.

Completed the ppu02020-derived `pili_surface_adhesion_boundary` sub-batch.
Fetched `fimD`, `PP_1890`, `PP_2356`, `PP_2357`, `PP_2358`, `PP_2359`,
`PP_2360`, `PP_2361`, `PP_2362`, `PP_2363`, and `PP_3126` by UniProt
accession with aliases, reused the existing `pilA` review, ran Asta
gene-level retrieval for all 12 genes, curated all 12 reviews, and
created/validated `modules/pili_surface_adhesion_boundary.yaml`. The curation
keeps `pilA` as a type IV pilin/twitching-motility and adhesion node, separates
FimD/Csu-like usher-chaperone pilus-assembly context from the PP_2356
phytochrome-like histidine kinase, and keeps `PP_3126` as a polysaccharide
exporter side node. The Csu-like subunits and chaperones with no GOA rows were
represented with `NEW` review entries backed by UniProt/Asta evidence. The
real Falcon module/pathway/taxon command failed with Edison HTTP 402, so no
Falcon report is cited.

Completed the ppu02020-derived
`dicarboxylate_tricarboxylate_transport_regulation_boundary` sub-batch. Fetched
`dctD-I`, `PP_0264`, `uhpA`, `dctD-II`, `PP_1067`, `PP_1167`, `PP_1168`,
`dctP`, `dctA`, `dctD-III`, `dctB`, `PP_1416`, `PP_1417`, `PP_1418`, `tctD`,
`PP_1421`, `dctA-II`, `dctA-III`, and `PP_3124` by UniProt accession with
aliases, ran Asta gene-level retrieval for all 19 genes, curated all 19
reviews, and created/validated
`modules/dicarboxylate_tricarboxylate_transport_regulation_boundary.yaml`. The
curation separates DctD/DctB-like regulatory pairs, UhpA side-context
regulation, the DctPQM TRAP C4-dicarboxylate importer, DctA-family
succinate/fumarate/malate symporters, the TctABC/TctD-like tricarboxylate
locus, and the PP_3124 short-chain fatty-acid transporter side node. TctABC
had no GOA rows, so missing tricarboxylate transporter/process and membrane
location terms were represented as `NEW` review entries backed by UniProt/Asta
evidence. The real Falcon module/pathway/taxon command failed with Edison HTTP
402, so no Falcon report is cited.

Completed the ppu02020-derived
`orphan_two_component_regulators_boundary` sub-batch. Fetched `PP_0574`,
`PP_0887`, `regA`, `PP_1007`, `bvgA`, `PP_1181`, `PP_1182`, `PP_2671`,
`PP_3412`, and `PP_3413` by UniProt accession with aliases, ran Asta
gene-level retrieval for all 10 genes, curated all 10 reviews, and
created/validated `modules/orphan_two_component_regulators_boundary.yaml`. The
curation records PP_0887/regA, PP_1182/PP_1181, and PP_3413/PP_3412 as
generic adjacent TCS branches; keeps PP_0574, bvgA, and PP_2671 as orphan
regulatory side branches; and treats PP_1007 as FecR-like anti-sigma context
rather than a canonical His-Asp sensor kinase. The real Falcon
module/pathway/taxon command failed with Edison HTTP 402, so no Falcon report
is cited.

Closed the ppu02020 side-context spillovers. Fetched and Asta-backed `dnaA`
and `etp`, curated both first-pass reviews, added `dnaA` to
`modules/bacterial_dna_replication.yaml` as replication-origin
recognition/initiation context, and created
`modules/protein_phosphorylation_boundary.yaml` for Etp protein tyrosine
phosphatase context. The ppu02020 partition now has 99/99 review files and
Asta reports; all buckets are first-pass complete while the pathway remains a
partitioned umbrella rather than one satisfiable two-component-system module.

Partitioned the `ppu02024` / KEGG quorum-sensing umbrella. Generated the
primary-only checklist `projects/P_PUTIDA/batches/ppu02024_quorum_sensing_boundary.md`
and the reproducible partition outputs
`projects/P_PUTIDA/batches/ppu02024_quorum_sensing_partition.tsv` and
`projects/P_PUTIDA/batches/ppu02024_quorum_sensing_partition.md` from
`projects/P_PUTIDA/partition_ppu02024_quorum_sensing.py`. The pathway worklist
now marks `kegg:ppu02024` as `PARTITIONED` rather than
`NEEDS_MODULE_MAPPING`.

Main ppu02024 lesson: the primary PSEPK membership does not define a single
LuxI/LuxR quorum-sensing module. The 60 primary genes split into 9 buckets:
branched-chain amino-acid ABC import (25), polyamine ABC import (13),
peptide/opine/glutathione ABC import (8), QseBC-like two-component regulation
(5), phosphonate/AEP ABC import (4), RND multidrug efflux (2), plus singleton
Fur/iron regulation, surface adhesion, and DMT transporter side contexts. The
most quorum-adjacent concrete submodule is the QseBC-like regulatory group;
the largest buckets should be handled as transport modules.

Completed the ppu02024-derived `rnd_multidrug_efflux_boundary` side-context
sub-batch. Fetched and ran Asta for `PP_2064` and `PP_2065`, curated both
reviews with `projects/P_PUTIDA/curate_ppu02024_rnd_multidrug_efflux_first_pass.py`,
validated and rendered both gene pages, and created, validated, and rendered
`modules/rnd_multidrug_efflux_boundary.yaml`. Main decisions: PP_2064 is a
membrane-fusion/adaptor component that contributes to complex-level efflux
activity and should not be treated as a standalone transmembrane transporter;
PP_2065 is the inner-membrane RND xenobiotic efflux transporter. After
rebuilding the partition and pathway worklist, ppu02024 has 27/60 primary
review folders and 27/60 Asta reports; the remaining strongest concrete
sub-batches are QseBC-like two-component regulation, peptide/opine/glutathione
ABC import, and polyamine ABC import.

Completed the ppu02024-derived
`qsebc_like_two_component_regulation_boundary` sub-batch. Fetched and ran Asta
for `PP_2713`, `PP_2714`, `kdpE`, `PP_4224`, and `qseB`, curated all five
reviews with
`projects/P_PUTIDA/curate_ppu02024_qsebc_like_two_component_first_pass.py`,
validated and rendered all five gene pages, and created, validated, and rendered
`modules/qsebc_like_two_component_regulation_boundary.yaml`. Main decisions:
PP_2714-PP_2713 and PP_4224-qseB are plausible local sensor kinase/response
regulator pairs; kdpE is retained as a related KdpE-like DNA-binding response
activator, but its sensor partner and target regulon remain unresolved. Broad
generic kinase/transferase/DNA-binding annotations were down-weighted where
more specific phosphorelay or cis-regulatory-binding terms were available.
After rebuilding the partition and pathway worklist, ppu02024 has 32/60
primary review folders and 32/60 Asta reports; the strongest remaining concrete
sub-batches are peptide/opine/glutathione ABC import and polyamine ABC import.

Completed the ppu02024-derived `phosphonate_abc_import` sub-batch. Fetched and
ran Asta for `PP_1722`, `PP_1723`, `PP_1724`, and `PP_1726`, curated all four
reviews with
`projects/P_PUTIDA/curate_ppu02024_phosphonate_abc_import_first_pass.py`,
validated and rendered the four gene pages, and extended, validated, and
rendered `modules/phosphonate_phosphinate_metabolism.yaml`. Main decisions:
PP_1722 is treated as the ABC ATP-binding energy-coupling subunit; PP_1723 and
PP_1724 are the 2-aminoethylphosphonate/AEP permeases; PP_1726 is the
periplasmic binding component. PP_1726's electronic thiamine-binding/transport
terms were removed or replaced with phosphonate import context. After
rebuilding the partition and pathway worklist, ppu02024 has 36/60 primary
review folders and 36/60 Asta reports; the remaining strongest concrete
sub-batches are polyamine ABC import and peptide/opine/glutathione ABC import.

Completed the ppu02024-derived
`peptide_opine_glutathione_abc_import_boundary` sub-batch. Fetched and ran
Asta for `PP_3220`, `PP_3221`, `PP_3222`, `PP_3223`, `gsiA`, `PP_4454`,
`gsiC`, and `PP_4458`, using UniProt accession fallback for `gsiC` (`Q88EK7`).
Curated all eight reviews with
`projects/P_PUTIDA/curate_ppu02024_peptide_opine_glutathione_abc_import_first_pass.py`,
validated and rendered all eight gene pages, and created, validated, and
rendered `modules/peptide_opine_glutathione_abc_import_boundary.yaml`. Main
decisions: PP_3220-PP_3223 are treated as a compact dipeptide-like ABC import
locus; gsiA and gsiC carry the glutathione-import call; PP_4454 and PP_4458
retain opine-like/periplasmic-binding context without forcing glutathione
specificity across the whole locus. After rebuilding the partition and pathway
worklist at that checkpoint, ppu02024 had 44/60 primary review folders and
44/60 Asta reports; the next large concrete sub-batch was polyamine ABC import.

Completed the ppu02024-derived `polyamine_abc_import` sub-batch. Fetched and
ran Asta for `potA`, `PP_0412`, `PP_0413`, `PP_0414`, `ydcV`, `ydcU`,
`ydcT`, `ydcS`, `PP_2870`, `PP_3814`, `PP_3815`, `PP_3816`, and `PP_3817`,
using UniProt accession aliases to keep the partition names stable. Curated
all thirteen reviews with
`projects/P_PUTIDA/curate_ppu02024_polyamine_abc_import_first_pass.py`,
validated and rendered all thirteen gene pages, and extended, validated, and
rendered `modules/polyamine_transport_boundary.yaml`. Main decisions:
PP_0411-PP_0414, ydcV/ydcU/ydcT/ydcS, and PP_3814-PP_3817 are treated as
predicted polyamine ABC import loci; PP_2870 is retained as a
spermidine/putrescine-binding singleton with unresolved transporter partners.
PP_3814's TreeGrafter thiamine-specific calls were removed or replaced with
polyamine binding/transport context. After rebuilding the partition and pathway
worklist, ppu02024 has 57/60 primary review folders and 57/60 Asta reports;
only the three singleton side-context buckets remain.

Completed the three remaining ppu02024 singleton side-context buckets. Fetched
and ran Asta for `fur__Q88RL0` (PP_0119 Fur-family regulator), `PP_0806`
(large surface adhesion protein), and `PP_3609` (DMT/YdcZ-family transporter).
Curated all three reviews with
`projects/P_PUTIDA/curate_ppu02024_singleton_side_contexts_first_pass.py`,
validated and rendered the gene pages, and created, validated, and rendered
`modules/iron_homeostasis_regulation_boundary.yaml`,
`modules/surface_adhesion_boundary.yaml`, and
`modules/dmt_transporter_boundary.yaml`. Main decisions: PP_0119/fur__Q88RL0
is Fur-family iron-homeostasis transcriptional regulation side context, PP_0806
is broad surface-adhesion/biofilm-boundary context, and PP_3609 is a generic
DMT-family membrane transporter with substrate unresolved. After rebuilding the
partition and pathway worklist, ppu02024 has 60/60 primary review folders and
60/60 Asta reports. The pathway remains a partitioned umbrella rather than one
satisfiable quorum-sensing module.

Partitioned the `ppu02025` / KEGG biofilm-formation umbrella. Generated the
primary-only checklist
`projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_boundary.md`
and the reproducible partition outputs
`projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_partition.tsv`
and
`projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_partition.md`
from `projects/P_PUTIDA/partition_ppu02025_biofilm.py`. The pathway worklist
now marks `kegg:ppu02025` as `PARTITIONED` rather than
`NEEDS_MODULE_MAPPING`.

Main ppu02025 lesson: this is a *Pseudomonas aeruginosa* biofilm umbrella, not
a single satisfiable PSEPK pathway. The 43 primary genes split into 6 buckets:
T6SS/biofilm context (13), orphan biofilm regulatory sensors (8), global
Gac/Csr/Crp biofilm regulation (6), Wsp-like chemotaxis/c-di-GMP cluster (6),
Pil/Chp twitching regulation (6), and c-di-GMP turnover (4). The clearest
biofilm-specific next submodules are Wsp-like surface sensing, c-di-GMP
turnover, Gac/Csr/Crp global regulation, and Pil/Chp twitching regulation;
T6SS apparatus genes are handled by reusing the secretion-system boundary rather
than by creating a separate biofilm-specific module.

Completed the ppu02025-derived `wsp_surface_sensing_c_di_gmp_boundary`
sub-batch. Fetched `PP_1488`, `PP_1489`, `PP_1491`, `PP_1492`, `cheB3`, and
`PP_1494`, ran Asta gene-level retrieval for all six, curated all six reviews,
and created/validated `modules/wsp_surface_sensing_c_di_gmp_boundary.yaml`.
The module keeps the PP_1488-PP_1494 Wsp-like branch as surface-sensing and
c-di-GMP context rather than the canonical flagellar chemotaxis core, with
already curated `wspC`/PP_1490 included as local methyltransferase context.
The real Falcon module/pathway/taxon command failed with Edison HTTP 402, so no
Falcon report is cited. The ppu02025 partition now has 10/43 review files,
10/43 curated reviews, and 7/43 Asta reports.

Completed the ppu02025-derived `c_di_gmp_turnover_boundary` sub-batch. Fetched
`PP_0914`, `PP_3581`, and `TpbB`, refreshed `pde`, ran Asta gene-level
retrieval for the three new reviews, curated all four bucket reviews, and
created/validated `modules/c_di_gmp_turnover_boundary.yaml`. The module keeps
`PP_0914` and `PP_3581` as EAL-domain cyclic-guanylate phosphodiesterase
candidates, `TpbB` as a membrane-associated GGDEF diguanylate cyclase candidate,
and `pde` only as broad 3',5'-cyclic-nucleotide phosphodiesterase side context
because the available evidence does not establish c-di-GMP-specific EAL-type
hydrolysis for pde. The real Falcon module/pathway/taxon command failed with
Edison HTTP 402, so no Falcon report is cited. The ppu02025 partition now has
13/43 review files, 13/43 curated reviews, and 10/43 Asta reports.

Completed the ppu02025-derived `pil_chp_twitching_motility_boundary` sub-batch.
Fetched `PP_4987`, `PP_4988`, `pilJ`, `pilI`, `pilH`, and `pilG`, ran Asta
gene-level retrieval for all six, curated the six reviews, and created/validated
`modules/pil_chp_twitching_motility_boundary.yaml`. The module keeps `pilJ` as a
PilJ/MCP-like membrane transducer, `PP_4987` and `pilI` as CheW-like adaptor
candidates, `PP_4988` as the CheA-family histidine kinase, and `pilH`/`pilG` as
small receiver-domain response-regulator candidates. The review pass adds `NEW`
phosphorelay response regulator activity entries for `pilH` and `pilG` because
the existing GOA only captured the phosphorelay process. Type IV
pilus-dependent motility is retained as module/pathway context rather than a
directly proven gene-level output for every component. The real Falcon
module/pathway/taxon command failed with Edison HTTP 402, so no Falcon report is
cited. The ppu02025 partition now has 19/43 review files, 19/43 curated reviews,
and 16/43 Asta reports.

Completed the ppu02025-derived `global_biofilm_regulation_boundary` sub-batch.
Fetched `crp`, `csrA__Q88M29`, `csrA__Q88G93`, and `csrA__Q88EJ0`, added Asta
gene-level retrieval for those four plus the existing `gacS` and `gacA` reviews,
curated the four newly fetched reviews, and created/validated
`modules/global_biofilm_regulation_boundary.yaml`. The module treats `gacS` and
`gacA`/`uvrY` as the Gac phosphorelay, the three CsrA paralogs as distinct
accession-scoped CsrA/RsmA-family mRNA 5-prime UTR-binding regulators, and `crp`
as a cAMP-responsive CRP-family transcription activator. The `crp` pass adds a
`NEW` cAMP-binding annotation from UniProt domain/keyword support; `gacA` remains
the local folder for the ppu02025 `uvrY` row. The real Falcon
module/pathway/taxon command failed with Edison HTTP 402, so no Falcon report is
cited. At this checkpoint, before the T6SS reuse batch below, the ppu02025
partition had 23/43 review files, 23/43 curated reviews, and 22/43 Asta
reports. The four strongest biofilm-specific ppu02025 sub-buckets were
first-pass complete; orphan regulatory sensors remained deferred.

Completed the ppu02025 T6SS/biofilm-context reuse batch. Fetched `PP_2617`,
`PP_2620`, `PP_2623`, `PP_2624`, `PP_3088`, `PP_3093`, `PP_3096`, `puuD`,
`PP_3100`, `PP_4074`, `PP_4078`, `PP_4080`, and `PP_5561`, ran Asta
gene-level retrieval for all 13, curated all 13 reviews, and extended
`modules/bacterial_secretion_system_boundary.yaml` with the TssA/TssB/TssC,
TssG/TssK, and TagF-like entries. `puuD`/PP_3099 is interpreted as a likely
TssC/VipB-family sheath protein despite its EC-derived uricase product name, so
the IEA urate oxidase activity annotation is marked for removal. The ppu02025
partition now has 36/43 review files, 36/43 curated reviews, and 35/43 Asta
reports before the orphan regulatory-sensor bucket below.

Completed the ppu02025-derived `orphan_biofilm_regulatory_sensors_boundary`
sub-batch. Fetched and/or reused `PP_1875`, `PP_2664`, `PP_4173`, `PP_4362`,
`PP_4363`, `PP_4364`, `PP_4781`, and `retS`/PP_4824, ran Asta for all eight
rows, curated the seven new reviews, wired Asta provenance into the existing
`retS` review, and created/validated
`modules/orphan_biofilm_regulatory_sensors_boundary.yaml`. The pass keeps most
ligands, partners, and regulons unresolved, accepts the supported sensor
kinase/HPt/phosphatase/anti-sigma functions, and treats `retS` as the
gene-specific K1-T6SS regulatory exception. The ppu02025 partition now has
43/43 review files, 43/43 curated reviews, and 43/43 Asta reports.

Partitioned the `ppu02030` / KEGG bacterial-chemotaxis umbrella. Generated the
primary-only checklist
`projects/P_PUTIDA/batches/ppu02030_bacterial_chemotaxis_boundary.md` and the
reproducible partition outputs
`projects/P_PUTIDA/batches/ppu02030_bacterial_chemotaxis_partition.tsv` and
`projects/P_PUTIDA/batches/ppu02030_bacterial_chemotaxis_partition.md` from
`projects/P_PUTIDA/partition_ppu02030_chemotaxis.py`. The pathway worklist now
marks `kegg:ppu02030` as `PARTITIONED` rather than `NEEDS_MODULE_MAPPING`.

Main ppu02030 lesson: KEGG's bacterial-chemotaxis map is a real biological
domain but still too broad for one satisfiable curation module. The 41 primary
genes split into 5 buckets: orphan MCP/aerotaxis receptors (13), known or named
MCP receptor panel (9), periplasmic binding/transport spillovers (7), core Che
signal-transduction cluster (6), and chemotaxis adaptation/accessory proteins
(6). The clearest next chemotaxis-specific submodules are the core Che cluster,
the named receptor panel, and the adaptation/accessory group; dipeptide, ribose,
and sugar-binding proteins should stay with transport modules unless direct
chemotaxis evidence is selected.

Completed the ppu02030-derived `bacterial_chemotaxis_core_boundary`
sub-batch. Fetched the missing core-cluster reviews (`PP_4332`, `PP_4333`, and
`cheB1`), ran Asta for all six core genes (`PP_4332`, `PP_4333`, `cheB1`,
`cheA`, `cheZ`, and `cheY`), curated the three new reviews with
`projects/P_PUTIDA/curate_ppu02030_chemotaxis_core_che_cluster_first_pass.py`,
validated and rendered all six review pages, and created/validated/rendered
`modules/bacterial_chemotaxis_core_boundary.yaml`. Asta retrieval was checked
but did not provide curation-changing organism-specific literature for the new
CheW/CheB reviews, so those decisions rely on UniProt, GOA, domain, and local
cluster evidence. The main module gap is that GO lacks a useful CheW
adaptor/scaffold molecular-function term, so PP_4332 and PP_4333 are retained
as chemotaxis adaptor/accessory candidates without falling back to generic
protein binding. At that checkpoint, after rebuilding the partition and pathway
worklist, ppu02030 had 15/41 primary review folders and 13/41 Asta reports; the
remaining concrete chemotaxis buckets were the named MCP receptor panel and the
adaptation/accessory group.

Completed the ppu02030-derived `chemotaxis_adaptation_accessory_boundary`
sub-batch. Fetched six reviews (`PP_0802`, `PP_2128`, `PP_3759`, `cheR3`,
`cheR2`, and `PP_4393`), ran Asta for all six, fetched/cached PMID:23677992 for
the CheR2/CheR3 specificity question, curated the reviews with
`projects/P_PUTIDA/curate_ppu02030_chemotaxis_adaptation_accessory_first_pass.py`,
validated and rendered all six review pages, and created/validated/rendered
`modules/chemotaxis_adaptation_accessory_boundary.yaml`. Main decisions:
CheV-like PP_0802, PP_2128, and PP_4393 are retained as chemotaxis signal
transduction/adaptation accessory proteins without inventing a specific MF;
CheR2 is retained as chemotaxis receptor methyltransferase and chemotaxis
support from PMID:23677992, while CheR3 is left at broad SAM-dependent
methyltransferase because the same paper supports high specificity for CheR2;
PP_3759 is retained as protein-glutamate methylesterase/chemotaxis context, but
standalone two-component receiver activity and phosphorelay signaling are
removed or marked over-propagated. After rebuilding the partition and pathway
worklist, ppu02030 has 21/41 primary review folders and 19/41 Asta reports;
the remaining concrete chemotaxis sub-batch is the named MCP receptor panel,
while orphan MCP/aerotaxis receptors stay deferred.

Completed the ppu02030-derived `chemotaxis_receptor_panel_boundary` sub-batch.
Fetched seven missing reviews (`mcpH`, `ctpL`, `mcpU`, `mcpG`, `mcpA`, `mcpP`,
and `mcpQ`), using the Q88N45 accession alias fallback for `mcpG`; ran Asta for
all nine named receptors (`mcpH`, `ctpL`, `mcpU`, `mcpG`, `mcpA`, `pcaY`,
`mcpP`, `mcpS`, and `mcpQ`); fetched/cached direct receptor PMIDs 26355499,
26662997, 30425146, 29758259, 25921834, 26048936, and 26463109; curated the
seven new reviews with
`projects/P_PUTIDA/curate_ppu02030_chemotaxis_receptor_panel_first_pass.py`;
validated and rendered all nine receptor pages; and created/validated/rendered
`modules/chemotaxis_receptor_panel_boundary.yaml`. Main decisions: McpH is the
purine-derivative receptor, McpU the polyamine receptor, McpG the GABA receptor,
McpA the amino-acid receptor, McpP the C2/C3 carboxylate receptor, McpQ the
citrate/citrate-metal receptor, and the existing PcaY and McpS reviews cover
C6-ring carboxylic acids and TCA-cycle intermediates, respectively. CtpL is
kept as a named MCP-family receptor candidate, but no KT2440 ligand specificity
is asserted. After rebuilding the partition and pathway worklist, ppu02030 has
28/41 primary review folders and 28/41 Asta reports. The remaining uncurated
chemotaxis-specific sub-batch is the orphan MCP/aerotaxis receptor boundary;
periplasmic-binding transport spillovers remain assigned to transport modules
unless direct chemotaxis evidence is selected.

Completed the ppu02030-derived
`orphan_mcp_aerotaxis_receptors_boundary` sub-batch. Fetched and ran Asta for
all thirteen genes (`PP_0317`, `PP_0584`, `PP_0779`, `PP_1819`, `PP_1940`,
`PP_2111`, `ctpH`, `PP_2257`, `PP_2823`, `PP_3414`, `PP_3557`, `PP_4521`,
and `PP_5021`), curated every GOA row with
`projects/P_PUTIDA/curate_ppu02030_orphan_mcp_aerotaxis_receptors_first_pass.py`,
validated and rendered all thirteen receptor pages, and created, validated, and
rendered `modules/orphan_mcp_aerotaxis_receptors_boundary.yaml`. Main
decisions: generic orphan MCP/sensory receptors are retained as chemotaxis
receptor/transducer candidates without assigning ligand specificity; PP_2111,
PP_2257, and PP_4521 are retained as aerotaxis receptor candidates; and
PP_2111 SNAP receptor activity, intracellular protein transport, and membrane
fusion are removed as SNARE-derived electronic spillover. After rebuilding the
partition and pathway worklist, ppu02030 has 41/41 primary review folders and
41/41 Asta reports. The ppu02030 chemotaxis first-pass sub-batches are now
complete, with periplasmic-binding transport spillovers left in transport
modules unless direct receptor-level chemotaxis evidence is selected.

Partitioned the `ppu02040` / KEGG flagellar-assembly pathway. Generated the
primary-only checklist
`projects/P_PUTIDA/batches/ppu02040_bacterial_flagellar_assembly_boundary.md`
and the reproducible partition outputs
`projects/P_PUTIDA/batches/ppu02040_bacterial_flagellar_assembly_partition.tsv`
and
`projects/P_PUTIDA/batches/ppu02040_bacterial_flagellar_assembly_partition.md`
from `projects/P_PUTIDA/partition_ppu02040_flagellar_assembly.py`. The pathway
worklist now marks `kegg:ppu02040` as `PARTITIONED` rather than
`NEEDS_MODULE_MAPPING`.

Main ppu02040 lesson: unlike quorum sensing or biofilm, this is a coherent
flagellar biology map, but the first-pass curation unit should still be smaller
than 47 genes. The primary set splits into 5 buckets: basal-body/hook/filament
structure (15), flagellar export and assembly/chaperones (14),
motor/switch/stator proteins (9), sigma/master regulation (6), and
nonflagellar transport/envelope spillovers (3). `fliY`, `PP_1087`, and
`PP_5157` should stay outside the flagellar apparatus core unless direct
flagellum-assembly evidence is selected.

Completed the ppu02040-derived `flagellar_motor_switch_stator_boundary`
sub-batch. Fetched missing `PP_4335`, `PP_4336`, `fliN`, `fliM`, `fliL`,
and `PP_5209` (the last by UniProt Q88CH2 with alias `PP_5209`), ran Asta
for all nine motor/switch/stator genes, curated the six missing reviews with
`projects/P_PUTIDA/curate_ppu02040_flagellar_motor_switch_stator_first_pass.py`,
validated and rendered all nine reviews, and added/validated/rendered
`modules/flagellar_motor_switch_stator_boundary.yaml`. Main decisions:
PP_4336/PP_4335 are the MotC/MotD-like MotCD stator pair in the main
flagellar cluster; `motA`/`motB` remain the second MotAB stator;
`fliG`/`fliM`/`fliN` form the C-ring switch; `fliL` and `PP_5209` are
retained as FliL-family motor-support candidates with unresolved
paralog-specific roles. Asta reports were present but not used as evidence
where retrieval did not add curation-changing support. After rebuilding the
partition and pathway worklist, ppu02040 has 20/47 primary review folders and
11/47 Asta reports; the `flagellar_motor_switch_stator` partition bucket is
9/9 present, curated, and Asta-backed.

Completed the ppu02040-derived `flagellar_export_assembly_boundary` sub-batch.
Fetched `flhA`, `flhB`, `fliR`, `fliQ`, `fliP`, `fliO`, `fliK`, `fliJ`,
`fliI`, `fliH`, `fliT`, `fliS`, `flgA`, and `PP_4396` by explicit UniProt
accession aliases, ran Asta for all 14, curated the reviews with
`projects/P_PUTIDA/curate_ppu02040_flagellar_export_assembly_first_pass.py`,
validated and rendered all 14 reviews, and added/validated/rendered
`modules/flagellar_export_assembly_boundary.yaml`. Main decisions: FlhA/FlhB
and FliP/FliQ/FliR form the membrane export-gate core with FliO as accessory
context; FliI is the protein-exporting ATPase and the ATP-synthase-like
TreeGrafter/orthology terms were removed as over-propagated; FliH and FliJ are
kept as cytosolic-side export-energy/accessory factors; FliK is retained as
hook-length control despite an empty GOA table; and FliS, FliT, FlgA, and
PP_4396/FlgN-like are assembly-support factors. After rebuilding the partition
and pathway worklist, ppu02040 has 34/47 primary review folders and 25/47 Asta
reports; the `flagellar_export_assembly_chaperones` partition bucket is 14/14
present, curated, and Asta-backed. Remaining concrete ppu02040 apparatus work
is the `flagellar_basal_body_hook_filament` bucket; regulation and
transport/envelope spillovers should stay separate.

Completed the ppu02040-derived
`flagellar_basal_body_hook_filament_boundary` sub-batch. Fetched missing
reviews for `fliF`, `fliE`, `fliD`, `flgJ`, `flgI`, `flgH`, `flgG`, `flgF`,
`flgD`, `flgC`, and `flgB`, ran Asta for all 15 structural genes including the
previously curated `fliC`, `flgL`, `flgK`, and `flgE`, curated the 11 new
reviews with
`projects/P_PUTIDA/curate_ppu02040_flagellar_basal_body_hook_filament_first_pass.py`,
validated and rendered all 15 review pages, and added/validated/rendered
`modules/flagellar_basal_body_hook_filament_boundary.yaml`. Main decisions:
FliF/FliE are the MS-ring/early basal-body scaffold; FlgB, FlgC, FlgF, and
FlgG are rod-family structural proteins; FlgJ is treated as a periplasmic
glycosyl-bond hydrolase for peptidoglycan clearance rather than as a specific
amidase; FlgI/FlgH form the P and L rings; FlgE/FlgK/FlgL cover the
hook/hook-filament junction; and FliC/FliD cover filament/cap structure. After
rebuilding the partition and pathway worklist, ppu02040 has 45/47 primary
review folders, 45/47 curated reviews, and 40/47 Asta reports. The three
concrete flagellar apparatus sub-batches are complete for first pass; the
remaining ppu02040 work is the regulation bucket and the nonflagellar
transport/envelope spillovers.

Completed the ppu02040-derived `flagellar_regulation_boundary` sub-batch.
Fetched the missing `atoC` review by UniProt Q88ET2 with alias `atoC`, ran
Asta for all six regulation genes (`rpoD`, `rpoN`, `fliA`, `atoC`, `fleQ`, and
`flgM`), curated the new `atoC` review with
`projects/P_PUTIDA/curate_ppu02040_flagellar_regulation_first_pass.py`,
validated and rendered all six regulation pages, and added/validated/rendered
`modules/flagellar_regulation_boundary.yaml`. Main decisions: `rpoD` remains
broad housekeeping sigma context rather than a flagellum-specific regulator;
`rpoN` is the sigma-54 layer; `fleQ` is the experimentally supported master
activator and c-di-GMP-responsive switch; `atoC` is retained conservatively as
a predicted phosphorylation-responsive sigma-54-associated transcriptional
activator with unresolved KT2440 target specificity; `fliA` is sigma-28 late
flagellar output; and `flgM` is the anti-sigma-28 checkpoint. After rebuilding
the partition and pathway worklist, ppu02040 has 46/47 primary review folders,
46/47 curated reviews, and 46/47 Asta reports. The remaining ppu02040 bucket is
`nonflagellar_transport_envelope_spillovers`, which should stay outside the
flagellar apparatus core unless direct evidence emerges.

Completed the ppu02040-derived `transport_envelope_spillover_boundary` bucket.
Fetched the missing `PP_1087` review by UniProt Q88NW6, ran Asta, curated it
with
`projects/P_PUTIDA/curate_ppu02040_transport_envelope_spillovers_first_pass.py`,
and added a minimal cell-envelope core function to the existing `PP_5157`
review so the spillover set validates without core-function warnings. Created,
validated, and rendered
`modules/transport_envelope_spillover_boundary.yaml`. Main decisions: `fliY`
remains a periplasmic cystine-binding transport component despite its
flagellar-looking symbol; `PP_1087` is an OmpA-family outer-membrane/envelope
protein with no direct flagellar apparatus evidence; and `PP_5157` is an
unresolved cell-envelope solute-binding family protein. After rebuilding the
partition and pathway worklist, ppu02040 has 47/47 primary review folders,
47/47 curated reviews, and 47/47 Asta reports. All five ppu02040 partition
buckets now have validated/rendered modules or boundary modules.

Partitioned the `ppu03010` / KEGG ribosome pathway. Generated the primary-only
checklist `projects/P_PUTIDA/batches/ppu03010_bacterial_ribosome_boundary.md`
and the reproducible partition outputs
`projects/P_PUTIDA/batches/ppu03010_bacterial_ribosome_partition.tsv` and
`projects/P_PUTIDA/batches/ppu03010_bacterial_ribosome_partition.md` from
`projects/P_PUTIDA/partition_ppu03010_ribosome.py`. The pathway worklist now
marks `kegg:ppu03010` as `PARTITIONED` rather than `NEEDS_MODULE_MAPPING`.

Main ppu03010 lesson: this is a clean bacterial ribosome protein set, not an
umbrella pathway. The 54 primary genes split naturally into 30S small-subunit
proteins (21) and 50S large-subunit proteins (33); no unknown or side-context
bucket was needed. First-pass curation should select one subunit batch at a
time so ribosome complex membership, rRNA binding, and translation contribution
annotations stay tractable.

Completed the ppu03010-derived `bacterial_30s_ribosomal_subunit_boundary`
sub-batch. Fetched the 21 30S genes by UniProt accession aliases, ran Asta for
each gene, curated all existing GOA rows with
`projects/P_PUTIDA/curate_ppu03010_30s_ribosomal_subunit_first_pass.py`, and
created/rendered `modules/bacterial_30s_ribosomal_subunit_boundary.yaml` using
`projects/P_PUTIDA/build_ppu03010_30s_ribosomal_subunit_module.py`. Validation
lesson: `GO:0015935` and `GO:0022627` are retained as trusted existing GOA
component annotations where present, but the stricter author-written
`core_functions.locations` enum rejects them, so core functions either use
`GO:0005840` ribosome or omit a location. After rebuilding the partition and
pathway worklist, the 30S bucket has 21/21 review folders, 21/21 curated
reviews, and 21/21 Asta reports.

Completed the ppu03010-derived `bacterial_50s_ribosomal_subunit_boundary`
sub-batch. Fetched the 33 50S genes by UniProt accession aliases, ran Asta for
each gene, curated all existing GOA rows with
`projects/P_PUTIDA/curate_ppu03010_50s_ribosomal_subunit_first_pass.py`, and
created/rendered `modules/bacterial_50s_ribosomal_subunit_boundary.yaml` using
`projects/P_PUTIDA/build_ppu03010_50s_ribosomal_subunit_module.py`. Main
decisions: structural constituent/translation/ribosome and large-subunit
membership terms are retained as core; specific rRNA, 5S rRNA, and tRNA binding
terms are retained; `rplB` generic transferase activity is marked
over-annotated; `rpmA` assembly of large subunit precursor of preribosome is
modified toward ribosomal large subunit assembly; zinc binding, ribosome
binding, and autoregulatory mRNA/translation-repression terms are kept as
non-core where present. After rebuilding the partition and pathway worklist,
ppu03010 has 54/54 primary review folders, 54/54 curated reviews, and 54/54
Asta reports, with validated/rendered 30S and 50S modules.

Partitioned the `ppu04122` / KEGG sulfur-relay system. Generated the
primary-only checklist
`projects/P_PUTIDA/batches/ppu04122_sulfur_relay_system_boundary.md` and the
reproducible partition outputs
`projects/P_PUTIDA/batches/ppu04122_sulfur_relay_system_partition.tsv` and
`projects/P_PUTIDA/batches/ppu04122_sulfur_relay_system_partition.md` from
`projects/P_PUTIDA/partition_ppu04122_sulfur_relay.py`. The pathway worklist
now marks `kegg:ppu04122` as `PARTITIONED` rather than
`NEEDS_MODULE_MAPPING`.

Main ppu04122 lesson: this is a sulfur-transfer umbrella, not one generic
pathway. The 19 primary genes split into 4 buckets: molybdopterin/MoCo sulfur
relay (9), Tus/MnmA tRNA thiolation (7), rhodanese/mercaptopyruvate
sulfurtransferase side nodes (2), and ThiS thiamine sulfur-carrier context (1).
`PP_5105` should stay with the thiamine-biosynthesis ThiS gap-fill, while
`rhdA` and `sseA` stay with sulfur-metabolism sulfurtransferase context unless
a more specific sulfur-relay mechanism is selected.

Completed the ppu04122-derived `mnma_tus_trna_thiolation_boundary` sub-batch.
Fetched the seven Tus/MnmA bucket genes (`tusA-I`, `tusA`, `tusD`,
`PP_3994`, `PP_3995`, `tusE`, and `mnmA`), ran Asta, curated the reviews with
`projects/P_PUTIDA/curate_ppu04122_tus_mnma_trna_thiolation_first_pass.py`,
validated and rendered the gene pages, and created/validated/rendered
`modules/mnma_tus_trna_thiolation_boundary.yaml`. The two sparse genes are
handled conservatively: `tusA-I` and `PP_3994` have empty fetched GOA tables, so
their inferred Tus sulfur-relay roles are recorded in `core_functions` and the
module knowledge gaps rather than as synthetic non-GOA `existing_annotations`.
After rebuilding the pathway worklist, ppu04122 now has 17/19 review folders
and 17/19 Asta reports; the remaining missing review folders are `moeB` and
`moaD` in the molybdopterin/MoCo sulfur-relay bucket.

Completed the ppu04122-derived
`molybdopterin_biosynthesis_sulfur_relay_boundary` sub-batch. Fetched the two
remaining missing ppu04122 review folders (`moeB` and `moaD`), ran Asta for
both, curated them with
`projects/P_PUTIDA/curate_ppu04122_moco_sulfur_relay_first_pass.py`, validated
and rendered the reviews, validated the full nine-gene MoCo bucket, and
created/validated/rendered
`modules/molybdopterin_biosynthesis_sulfur_relay_boundary.yaml`. The key
MoeB correction is to keep the MoaD adenylyltransferase/Ubl-activating-enzyme
role and remove TreeGrafter rhodanese/sulfotransferase over-propagations. The
MoaD sulfur-carrier role is recorded in `core_functions` and the module because
the fetched GOA rows cover the MoCo process and molybdopterin-synthase complex
but not the more informative sulfur-carrier molecular function. After rebuilding
the partition and pathway worklist, ppu04122 now has 19/19 primary review
folders and 19/19 Asta reports.

Completed the boundary/absence `ppu04141` /
`protein_processing_er_boundary` checkpoint. Registered the new module mapping,
created and validated `modules/protein_processing_er_boundary.yaml`, fetched
the missing `PP_3234` and `PP_3312` review folders, ran Asta for `PP_3234`,
`PP_3312`, and `htpG`, curated and validated all three reviews, regenerated the
three-gene batch checklist, rebuilt the pathway worklist, and rendered the
three gene pages plus the module page. The real Falcon module and
module+pathway commands were attempted and both failed at Edison task creation
with HTTP 402.

Main ppu04141 lesson: this is a bacterial heat-shock/proteostasis boundary
bucket, not endoplasmic-reticulum protein processing. `PP_3234` and `PP_3312`
are predicted HSP20-family small heat shock proteins and received conservative
`NEW` unfolded-protein-binding annotations from domain/family evidence. `htpG`
remains the bacterial Hsp90-family ATP-dependent protein-folding chaperone. No
ER protein-processing GO annotation is proposed for KT2440 from this bucket.

Completed the boundary/absence `ppu04156` /
`integrated_stress_response_boundary` checkpoint. Registered the new module
mapping, created and validated
`modules/integrated_stress_response_boundary.yaml`, confirmed Asta retrievals
for `groEL`, `dnaK`, `htpG`, and `PP_5211`, added Asta provenance to the
already-curated `groEL` and `dnaK` reviews, regenerated the four-gene batch
checklist, rebuilt the pathway worklist, and rendered the four gene pages plus
the module page. The real Falcon module and module+pathway commands were
attempted and both failed at Edison task creation with HTTP 402.

Main ppu04156 lesson: this is a bacterial stress/proteostasis plus glutathione
turnover boundary bucket, not eukaryotic integrated stress response signaling.
`groEL`, `dnaK`, and `htpG` are cytosolic chaperone/protein-quality-control
nodes. `PP_5211` remains a glutathione-specific
gamma-glutamylcyclotransferase already represented in the glutathione
metabolism boundary. No ISR-signaling GO annotation is proposed for KT2440 from
this bucket.

Completed the PTS `ppu02060` /
`phosphotransferase_system_boundary` checkpoint. Registered the new module
mapping, fetched the missing `ptsH`, `ptsN`, and `ptsP` review folders (with
`ptsN` fetched by UniProt accession `Q88PA0` plus alias), ran Asta for those
three genes, curated and validated all six candidate reviews, created and
validated `modules/phosphotransferase_system_boundary.yaml`, regenerated the
six-gene batch checklist, rebuilt the pathway worklist, and rendered the six
gene pages plus the module page. The real Falcon module and module+pathway
commands were attempted and both failed at Edison task creation with HTTP 402.

Main ppu02060 lesson: `fruBKA` is the concrete fructose-specific PTS branch:
FruB supplies PEP-dependent phosphotransfer, FruA imports/phosphorylates
fructose, and FruK converts fructose 1-phosphate into central metabolism.
`ptsH`, `ptsP`, and `ptsN` are HPr/Ntr regulatory phosphorelay context. PtsN is
not treated as evidence for a second substrate-specific sugar transporter.

Completed the boundary `ppu04981` /
`folate_transport_metabolism_boundary` checkpoint. Registered the new module
mapping, created and validated
`modules/folate_transport_metabolism_boundary.yaml`, confirmed all six mapped
members `glyA1`, `glyA2`, `metH`, `folA`, `thyA`, and `fau` were already
fetched, Asta-backed, and curated, regenerated the six-gene batch checklist,
rebuilt the pathway worklist, and rendered the six gene pages plus the module
page. The real Falcon module and module+pathway commands were attempted and
both failed at Edison task creation with HTTP 402.

Main ppu04981 lesson: this is a folate-metabolism boundary bucket, not a
complete folate transport pathway. GlyA1/GlyA2 feed one-carbon units into THF,
FolA regenerates tetrahydrofolate, Fau salvages 5-formyl-THF, ThyA consumes
5,10-methylene-THF for dTMP synthesis, and MetH consumes 5-methyl-THF in the
cobalamin-dependent methionine-synthase reaction. No folate transport GO
annotation is proposed from this bucket.

Completed the nucleotide-excision-repair `ppu03420` /
`bacterial_nucleotide_excision_repair` checkpoint. Registered the new module
mapping, created and validated
`modules/bacterial_nucleotide_excision_repair.yaml`, fetched the four missing
review folders (`polA`, `mfd`, `PP_2839`, and `PP_3087`; `PP_3087` required
the UniProt accession alias `Q88IB2`), ran Asta for the seven missing
gene-level reports, curated and validated all 10 reviews with no remaining
`PENDING` actions, regenerated the batch checklist, rebuilt the pathway
worklist, and rendered the 10 gene pages plus the module page. The real Falcon
module and module+pathway commands were attempted and both failed at Edison
task creation with HTTP 402.

Main ppu03420 lesson: the strict bacterial NER core is UvrA/UvrB/UvrC. Mfd is
the transcription-coupled repair entry point; UvrD, PolA, LigA, and LigB are
post-incision removal, repair-synthesis, and nick-sealing context shared with
other DNA-repair/replication pathways. PP_2839 and PP_3087 remain KEGG
boundary nodes with conservative helicase/UvrA-family ATPase curation until
their precise NER-specific roles are resolved.

Completed the mismatch-repair `ppu03430` /
`bacterial_mismatch_repair` checkpoint. Registered the new module mapping,
created and validated `modules/bacterial_mismatch_repair.yaml`, fetched 17
missing review folders, ran Asta for all 19 KEGG membership genes including
the pre-existing `mutS` and `mutL` reviews, curated and validated all 19
reviews with no remaining `PENDING` actions, regenerated the batch checklist,
rebuilt the pathway worklist, and rendered the 19 gene pages plus the module
page. The real Falcon module and module+pathway commands were attempted and
both failed at Edison task creation with HTTP 402.

Main ppu03430 lesson: the strict KT2440 mismatch-repair core is MutS/MutL.
The rest of the KEGG bucket is real but shared repair/replication context:
UvrD helicase, ExoVII/ExoI/RecJ and DnaQ-like exonucleases, SSB, DNA
polymerase III processivity/clamp-loader/proofreading subunits, and
NAD-dependent ligases. Pol III accessory subunits were treated as complex-level
contributors rather than standalone polymerase enzymes where appropriate.

Completed the homologous-recombination `ppu03440` /
`bacterial_homologous_recombination` checkpoint. Registered the new module
mapping, created and validated
`modules/bacterial_homologous_recombination.yaml`, fetched the nine missing
primary review folders (`recF`, `ruvC`, `ruvA`, `recO`, `recR`, `recD`,
`recC`, `priA`, and `recG`), ran Asta for the 12 primary HR genes, curated and
validated all 12 primary reviews, added Asta provenance to the existing `ruvB`,
`recA`, and `recB` reviews, regenerated the 24-gene batch checklist, rebuilt
the pathway worklist, and rendered the 24 gene pages plus the module page. The
real Falcon module and module+pathway commands were attempted and both failed
at Edison task creation with HTTP 402.

Main ppu03440 lesson: this is a homologous-recombination boundary module. The
strict core is RecA filament activity, RecFOR mediator context, RecBCD
double-strand-end processing, RuvAB/RuvC Holliday-junction processing, RecG
branched-DNA remodeling, and PriA replication restart. SSB, RecJ, PolA, DnaQ-
like exonucleases, and DNA polymerase III clamp/clamp-loader/proofreading
subunits are real KEGG members but are shared repair or replication-restart
context rather than HR-specific strand-exchange factors. `ruvA` helicase/ATPase
terms and `recC` helicase/ATPase terms were treated as subunit-level
over-annotations; RecD's product/domain context includes an odd viral-polyprotein
InterPro/PANTHER contaminant, so curation relies on the RecD/ExoV UniProt and
GOA evidence rather than that family label.

Completed the peroxisome boundary/absence `ppu04146` /
`peroxisome_boundary` checkpoint. Registered the new module mapping, created
and validated `modules/peroxisome_boundary.yaml`, fetched the missing `sodA`
review folder, ran Asta for `sodA` and `sodB`, curated and validated the
remaining `sodA` review plus all 12 batch members, regenerated the batch
checklist, rebuilt the pathway worklist, and rendered the 12 gene pages plus
the module page. The real Falcon module and module+pathway commands were
attempted and both failed at Edison task creation with HTTP 402.

Main ppu04146 lesson: this is not a bacterial peroxisome module. KT2440 has no
eukaryotic peroxisome organelle, peroxin import system, or peroxisomal matrix
compartment. The KEGG map is useful only as a boundary bucket containing
cytoplasmic catalase/SOD oxidative-stress enzymes, membrane-associated FadD
fatty-acid activation enzymes, Icd/Idh NADPH-generating TCA context, HMG-CoA
lyase side nodes, and NudC NAD/RNA-cap hydrolase context.

## 2026-07-08

Completed the first-pass `ppu00920` / `sulfur_metabolism_boundary` checkpoint.
Created and validated `modules/sulfur_metabolism_boundary.yaml`, registered the
KEGG mapping, fetched the 36 missing review folders, ran Asta for all 37 missing
gene-level reports plus the already-present `ssuD` gap, retried transient Asta
failures until all 54 candidates had retrieval reports, curated the 31 pending
reviews plus five no-GOA reviews, validated all 54 batch gene reviews and the
module, rendered all 54 gene pages, and refreshed the batch page.

Main ppu00920 lessons: this is a boundary sulfur-metabolism map rather than one
linear pathway. The strongest subroutes are sulfate/thiosulfate import
(`sbp-I`, `sbp-II`, `cysA`, `cysW`, `cysU`) and assimilatory sulfate reduction
to cysteine (`cysD`, `cysNC`, `cysH`, PP_0860, `cysI`, `cysQ`, `cysK`, and
serine acetyltransferase paralogs). Taurine/alkanesulfonate import and
desulfonation are represented by Tau/Ssu transporter components, `ssuD`,
`ssuE`, PP_2765, PP_3219, and `msuE`. PP_0053, PP_2677, PP_3822,
GlpE/RhdA/SseA, MetB/MetZ/MetXS, and PP_2795/PP_3553/PP_2048/PP_3554 remain
separate sulfur-redox, sulfurtransferase, amino-acid, and organosulfur side
nodes rather than evidence for a single complete KEGG route.

Completed the first-pass `ppu00930` /
`caprolactam_degradation_boundary` checkpoint. Created and validated
`modules/caprolactam_degradation_boundary.yaml`, registered the KEGG mapping,
regenerated the three-gene checklist, validated the already-curated `fadB`,
PP_2217, and `paaF` reviews plus the module, rendered all three gene pages plus
the module page, and refreshed the batch page.

Main ppu00930 lesson: this KEGG map is a boundary/absence caprolactam-degradation
bucket in KT2440. The only mapped members are shared CoA-thioester enzymes:
`fadB` from fatty-acid beta-oxidation, PP_2217 as an enoyl-CoA hydratase-family
side node, and `paaF` from phenylacetate/CoA-thioester metabolism. The batch
lacks caprolactam lactamase or 6-aminohexanoate upper-pathway enzymes, so it
does not support a complete caprolactam degradation module.

Completed the first-pass `ppu00946` / `flavonoid_degradation_boundary`
checkpoint. Created and validated `modules/flavonoid_degradation_boundary.yaml`,
registered the KEGG mapping, fetched the six missing review folders, ran and
retried Asta until all seven candidates had retrieval reports, curated the three
pending reviews plus three no-GOA reviews, validated all seven candidate reviews
and the module, rendered all seven gene pages plus the module page, and
refreshed the batch page.

Main ppu00946 lesson: this is an unresolved aromatic/flavonoid boundary cluster,
not a complete flavonoid-degradation route. `bglX` is already curated as a
periplasmic beta-glucosidase and is broad glycoside/carbohydrate context.
PP_3195-PP_3206 include a predicted S9 hydrolase/peptidase, a glyoxalase/VOC
protein, a Rieske ferredoxin, a cupin-domain protein, a fumarylacetoacetase-like
hydrolase, and an NAD-dependent epimerase/dehydratase. GOA support is sparse and
mostly generic, so these remain candidate aromatic-compound side nodes pending
substrate-specific evidence.

Completed the first-pass `ppu00970` / `aminoacyl_trna_biosynthesis` checkpoint.
Created and validated `modules/aminoacyl_trna_biosynthesis.yaml`, registered the
KEGG mapping, fetched 23 missing review folders, ran Asta for the 24 genes that
were missing it including the existing `fmt` review, retried transient Asta
failure on `thrS`, curated the 23 pending reviews, validated all 27 candidate
reviews and the module, rendered all 27 gene pages plus the module page, and
refreshed the batch page.

Main ppu00970 lesson: KT2440 has a complete core aminoacyl-tRNA charging set,
including heteromeric GlyRS (`glyQ`/`glyS`) and PheRS (`pheS`/`pheT`), direct
single-chain synthetases for the remaining protein amino acids, and editing
annotations on AlaRS/IleRS/LeuRS/ProRS/ValRS. GatCAB (`gatA`, `gatB`, `gatC`)
is kept as indirect Gln/Asn-tRNA transamidation, `fmt` as initiator
methionyl-tRNA formylation, and `selA`/`serS` as selenocysteine-tRNA side
chemistry. PP_0613 remains an unresolved amidase-family side node rather than a
core aminoacyl-tRNA biosynthesis gene. First-pass removals were limited to clear
electronic specificity errors such as glyS arginyl-tRNA transfer and glnS
glutamyl-tRNA aminoacylation.

Completed the first-pass `ppu00975` / `siderophore_biosynthesis_boundary`
checkpoint. Created and validated
`modules/siderophore_biosynthesis_boundary.yaml`, registered the KEGG mapping,
fetched and curated missing `pvdY`, added Asta evidence wiring to the existing
PP_2800 review, validated all three candidate reviews and the module, rendered
the three gene pages plus the module page, and refreshed the batch page.

Main ppu00975 lesson: this KEGG bucket is a boundary/partial siderophore module,
not the complete pyoverdine or siderophore biosynthesis pathway. `pvdH` is the
best-resolved L-2,4-diaminobutyrate aminotransferase tied to pyoverdine
precursor chemistry; PP_2800 remains a related predicted diaminobutyrate
aminotransferase side candidate; `pvdY` is a predicted MbtK/IucB-like
N-acyltransferase/hydroxyproline acetylase with conservative general
siderophore-biosynthesis support. No stronger pyoverdine-specific assignment
was made for `pvdY` without direct substrate evidence.

Completed the first-pass `ppu00996` / `alkaloid_biosynthesis_boundary`
checkpoint. Created and validated `modules/alkaloid_biosynthesis_boundary.yaml`,
registered the KEGG mapping, revalidated and rerendered PP_3358 after wiring in
Asta evidence, regenerated the validated one-gene batch, rendered the module
page, and refreshed the project/batch pages.

Main ppu00996 lesson: KT2440 ppu00996 is a one-gene boundary/absence case, not
a satisfiable alkaloid biosynthesis route. PP_3358 is already reviewed as
feruloyl-CoA hydratase/lyase in hydroxycinnamate/vanillin side metabolism and
is also represented in the aminobenzoate-degradation boundary batch; the
alkaloid map should not drive any additional pathway process annotation.

Completed the first-pass `ppu00999` /
`plant_secondary_metabolite_biosynthesis_boundary` checkpoint. Created and
validated `modules/plant_secondary_metabolite_biosynthesis_boundary.yaml`,
registered the KEGG mapping, revalidated and rerendered all five candidate
reviews after wiring Asta support into the four warning-bearing reviews,
regenerated the validated batch, rendered the module page, and refreshed the
project/batch pages.

Main ppu00999 lesson: KT2440 ppu00999 is a boundary/absence bucket made of
generic precursor and side-node enzymes. `aroE__Q88RQ5`, `aroE__Q88IJ7`, and
PP_3768 are shikimate-dehydrogenase-like enzymes upstream of chorismate; `bglX`
is a broad periplasmic beta-glucosidase; `metK` supplies SAM. These are valid
functions, but the batch does not support a plant secondary metabolite
biosynthesis process in KT2440.

Completed the first-pass `ppu01040` /
`unsaturated_fatty_acid_biosynthesis_boundary` checkpoint. Created and
validated `modules/unsaturated_fatty_acid_biosynthesis_boundary.yaml`,
registered the KEGG mapping, fetched and Asta-reviewed `tesA`, `tesB`, and
PP_5331, curated and validated the three review YAMLs, regenerated the
validated batch, rendered the gene and module pages, and refreshed the project
pages.

Main ppu01040 lesson: the KEGG bucket is thioesterase/acyl-pool side context,
not the canonical bacterial unsaturated-fatty-acid biosynthetic branch. `tesA`
is an SGNH/GDSL fatty acyl-ACP/lipid-ester hydrolase side node; `tesB` is a
fatty acyl-CoA hydrolase; PP_5331 is a HotDog-family long-chain fatty acyl-CoA
hydrolase. The actual UFA biosynthetic branch remains FabA/FabB context in
`fatty_acid_biosynthesis`.

Completed the first-pass `ppu01053` / `siderophore_biosynthesis_boundary`
checkpoint. Extended and revalidated
`modules/siderophore_biosynthesis_boundary.yaml` to include the ppu01053
siderophore-group NRPS membership, registered the KEGG mapping, fetched and
Asta-reviewed PP_2170, rechecked PP_1183, curated and validated both review
YAMLs, regenerated the validated two-gene batch, rendered PP_1183, PP_2170, and
the updated module page, and refreshed the project pages.

Main ppu01053 lesson: this is another siderophore boundary bucket rather than a
satisfiable NRPS route. PP_1183 is an EntD-family 4'-phosphopantetheinyl
transferase that can activate aryl- and peptidyl-carrier proteins for
siderophore assembly. PP_2170 is a predicted chorismate mutase; the
salicylic-acid biosynthetic process annotation was removed as over-propagated,
and the gene is retained only as chorismate/aromatic-amino-acid precursor
context pending direct evidence for siderophore precursor supply.

Completed the first-pass `ppu01320` / `sulfur_metabolism_boundary` checkpoint.
Extended and revalidated `modules/sulfur_metabolism_boundary.yaml` to cite the
ppu01320 sulfur-cycle membership, registered the KEGG mapping, regenerated the
validated nine-gene batch, cleaned inherited Asta-provenance warnings in the
eight warning-bearing reviews, revalidated all nine review YAMLs, rendered all
nine gene pages, rendered the updated module page, and refreshed the project
pages.

Main ppu01320 lesson: this KEGG sulfur-cycle map is a focused subset already
covered by the broader sulfur-metabolism boundary. It combines CysD/CysNC/CysH
activated-sulfate reduction, PP_0860/CysI sulfite reductase components,
PP_2677/PP_3822 sulfur-redox boundary nodes, and CysK cysteine synthesis. It
should not be treated as a standalone complete sulfur cycle in KT2440.

Completed the first-pass `ppu01501` / `beta_lactam_resistance_boundary`
checkpoint. Created and validated `modules/beta_lactam_resistance_boundary.yaml`,
registered the KEGG mapping, fetched the eight missing review folders, ran Asta
for the 14 missing gene-level reports, curated the eight new stubs, wired Asta
provenance into six older reviews, validated all 20 review YAMLs and the module,
regenerated the validated batch, rendered all 20 gene pages and the module page,
and refreshed the project pages.

Main ppu01501 lesson: the KEGG beta-lactam-resistance map is a resistance
boundary rather than a linear pathway. AmpC is the direct beta-lactamase;
AmpG/NagZ provide peptidoglycan recycling and AmpC-regulatory context; FtsI,
MrdA-I/MrdA-II, and MrcA are PBP/cell-wall targets; TtgABC, MexB, PP_0906,
PP_0907, PP_3455, and the OMF proteins PP_1263/PP_1798/PP_3582/PP_4923 are
efflux or xenobiotic-export context; OprD and OpmQ are permeability/export
boundary nodes, not beta-lactam-specific enzymes.

Completed the first-pass `ppu01502` / `vancomycin_resistance_boundary`
checkpoint. Created and validated
`modules/vancomycin_resistance_boundary.yaml`, registered the KEGG mapping,
regenerated the validated six-gene batch, wired Asta provenance into the two
older warning-bearing reviews (`mraY` and `murG`), revalidated all six review
YAMLs and the module, rendered all six gene pages, rendered the new module page,
and refreshed the project worklist.

Main ppu01502 lesson: the KEGG vancomycin-resistance map is an envelope
target/precursor boundary for KT2440, not evidence for a complete vancomycin
resistance pathway. DadX supplies D-alanine, DdlA/DdlB form D-Ala-D-Ala, MurF
completes UDP-MurNAc-pentapeptide, and MraY/MurG build lipid I/lipid II. The
first-pass curation found no VanHAX D-Ala-D-Lac bypass to model as resistance.

Completed the first-pass `ppu01503` /
`cationic_antimicrobial_peptide_resistance_boundary` checkpoint. Created and
validated `modules/cationic_antimicrobial_peptide_resistance_boundary.yaml`,
registered the KEGG mapping, fetched the ten missing review folders, ran Asta
for those ten genes, curated all ten new stubs, wired Asta provenance into three
older warning-bearing LPS/lipid A reviews (PP_0024, `lpxA`, and PP_4592),
validated all 21 review YAMLs and the module, regenerated the validated batch,
rendered all 21 gene pages, rendered the new module page, and refreshed the
project worklist.

Main ppu01503 lesson: the KEGG CAMP-resistance map is a resistance boundary
rather than a single pathway. PP_1202 is the clearest direct surface-charge
modification node as a phosphatidylglycerol lysyltransferase. `lpxA`, PP_0024,
and PP_4592 provide lipid A/LPS-core context; `phoP`/`phoQ`, `cpxR`, and
PP_4503 are regulatory context; PP_0906/PP_0907, `ttgA`/`ttgB`, PP_1798,
PP_3455/`mexB`, and PP_4923 are broad efflux/export context; `dsbA`, PP_1430,
and `ppiA` are periplasmic folding/protein-quality-control context; PP_2320
and `amiC` are peptidoglycan-remodeling context. The batch should not drive a
generic CAMP-resistance annotation across all members.

Partitioned the `ppu02010` ABC-transporter umbrella map. The batch contains 207
membership genes across 74 locus-neighborhood clusters, so it is now recorded as
`PARTITIONED` rather than forced into a single module. The cluster report is in
`projects/P_PUTIDA/batches/ppu02010_abc_transporters_boundary_clusters.md` and
retains a general/unknown ABC bucket for unresolved loci.

Completed the first concrete `ppu02010` sub-batch, cluster C16
PP_0824-PP_0827. Fetched `ptxB`, `phnC`, `phnE`, and `ptxC`, ran Asta for all
four, curated and validated their review YAMLs warning-free, and extended
`modules/phosphonate_phosphinate_metabolism.yaml` with a phosphonate ABC import
part. The module now links import to PhnW/PhnX AEP catabolism as a
`KNOWLEDGE_GAP`: phosphonate uptake is supported, but exact substrate range and
direct AEP handoff remain unverified.

Completed the second `ppu02010` sub-batch, cluster C07 PP_0225-PP_0227. Fetched
`sctC`, `sctS`, and `fliY`, ran Asta for all three, curated and validated their
review YAMLs warning-free, and extended `modules/sulfur_metabolism_boundary.yaml`
with a cystine/sulfur-compound ABC import part. The important correction was
`fliY`: despite the flagellar-looking symbol, the KT2440 product is a
signal-peptide-bearing periplasmic cystine-binding protein, so ion-channel and
monoatomic-ion-transport InterPro2GO spillovers were removed or replaced with
cystine transport/periplasmic binding context.

Completed the third `ppu02010` sub-batch, clusters C11/C12 PP_0294-PP_0296 plus
PP_0304. Fetched `cbcV`, `cbcW`, `cbcX`, and `caiX`, ran Asta for all four,
curated and validated their review YAMLs warning-free, and created
`modules/osmoprotectant_compatible_solute_transport_boundary.yaml`. The module
keeps the complete CbcV/CbcW/CbcX choline/betaine/carnitine compatible-solute
ABC importer separate from singleton CaiX, which is treated as a related
periplasmic binding component with unresolved choline versus carnitine
preference.

Completed the fourth `ppu02010` sub-batch, cluster C46 PP_3342-PP_3346. Fetched
`nikA`, `nikB`, `nikC`, `nikD`, and `nikE`, ran Asta for all five, curated and
validated their review YAMLs warning-free, and created
`modules/nickel_import_boundary.yaml`. The module represents NikA as the
periplasmic nickel-binding component, NikB/NikC as membrane permeases, and
NikD/NikE as ATP-binding energy-coupling subunits; heme and dipeptide/peptide
transport annotations on this locus were treated as family-transfer spillovers.

Completed the split C02 `ppu02010` sub-batch, PP_0112-PP_0120. Fetched `metQ`,
`metI`, `metN1`, `znuB`, `znuC`, and `PP_0120`, ran Asta for all six, curated
and validated their review YAMLs warning-free, and created
`modules/methionine_import_boundary.yaml` plus
`modules/zinc_import_boundary.yaml`. The important modeling decision was to
split the locus-neighborhood cluster into the MetNIQ methionine importer and
the ZnuABC zinc importer, rather than treating it as a mixed methionine/zinc
ABC system. PP_0120 is retained under its locus review name while represented
as a ZnuA-family high-affinity zinc-binding component; the cell-adhesion
annotation was removed as an adhesin-family spillover.

Completed the C06 `ppu02010` sub-batch, PP_0219-PP_0221. Fetched `metP`,
`metN2`, and `PP_0221`, ran Asta for all three, curated and validated their
review YAMLs warning-free, rendered the gene pages, and extended
`modules/methionine_import_boundary.yaml` with a second MetNIQ-like methionine
ABC import part. This keeps PP_0219-PP_0221 in the methionine import boundary
rather than creating a separate broad amino-acid transport module; exact L- vs
D-methionine substrate preference remains unresolved.

Completed the C17 `ppu02010` sub-batch, PP_0868-PP_0873. Fetched `yehX`,
`yehW`, `PP_0870`, `PP_0871`, and `potF-I`, ran Asta for all five, curated and
validated their review YAMLs warning-free, and rendered the gene pages. The
cluster was split biologically: PP_0868-PP_0871 extends
`modules/osmoprotectant_compatible_solute_transport_boundary.yaml` as a
Yeh-like quaternary-amine/glycine-betaine compatible-solute importer, while
PP_0873/potF-I seeds `modules/polyamine_transport_boundary.yaml` as a
putrescine/polyamine substrate-binding component with unresolved transporter
partners.

Completed the C18 `ppu02010` Dpp dipeptide-import sub-batch, PP_0878-PP_0885.
Fetched `dppF`, `dppD`, `dppC`, `dppB`, `dppA-I`, `dppA-II`, and `dppA-III`,
ran Asta for all seven, curated and validated their review YAMLs warning-free,
and created `modules/dipeptide_abc_import_boundary.yaml`. The module represents
DppF/DppD as ATP-binding energy-coupling subunits, DppC/DppB as membrane
permeases, and the three DppA-family proteins as separate periplasmic binding
components with unresolved substrate partitioning.

Completed compatible-solute `ppu02010` clusters C01, C27, C41, and C48. Fetched
`PP_0076`, `betX`, `opuA`, `PP_2775`, `PP_3558`, and `PP_3559`, ran Asta for
all six, curated and validated their review YAMLs warning-free, and extended
`modules/osmoprotectant_compatible_solute_transport_boundary.yaml`. `PP_0076`
and `betX` are kept as related periplasmic binding components with unresolved
cognate transporter partners; `opuA`/`PP_2775` is modeled as a predicted
glycine-betaine/L-proline compatible-solute ABC importer; `PP_3558`/`PP_3559`
is modeled as a partial glycine-betaine transporter pair with the ATPase partner
left unresolved.

Completed the C37 `ppu02010` sub-batch, PP_2656-PP_2659. Fetched `pstS`,
`pstC`, `pstA`, and `pstB1`, ran Asta for all four, curated and validated their
review YAMLs warning-free, rendered the gene pages, and seeded
`modules/phosphate_import_boundary.yaml`. This module keeps PstSACB inorganic
phosphate import separate from the earlier Phn/Ptx organic phosphonate import
block.

Completed the C73 `ppu02010` sub-batch, PP_5326-PP_5329. Fetched `pstB2`,
`PP_5327`, `PP_5328`, and `PP_5329`, ran Asta for all four, curated and
validated their review YAMLs warning-free, rendered the gene pages, and extended
`modules/phosphate_import_boundary.yaml` with a second Pst-like phosphate ABC
import part. `PP_5329` is treated as the periplasmic phosphate-binding
component; its cell-adhesion IEA was removed as a family spillover. The module
keeps open whether KT2440 has two separately regulated phosphate import modules
or paralogous variants of one phosphate-limitation transport system.

Completed the C22 `ppu02010` sub-batch, PP_1015-PP_1018. Fetched `gtsA`,
`gtsB`, `gtsC`, and `gtsD`, ran Asta for all four, curated and validated their
review YAMLs warning-free, rendered the gene pages, and created
`modules/glucose_import_boundary.yaml`. The P. putida glucose-catabolism paper
supports PP1015-PP1018 as a glucose ABC uptake system, so maltose-specific IEA
calls on `gtsD` were removed or replaced with ABC-type monosaccharide/glucose
transport context; mannose and related sugar range remains an open question.

Completed the C33 `ppu02010` sub-batch, PP_2454-PP_2459. Fetched `rbsB`,
`rbsA-I`, `rbsC`, and `rbsD`, ran Asta for all four, curated and validated
their review YAMLs warning-free, rendered the gene pages, and created
`modules/ribose_import_boundary.yaml`. The module separates the RbsB/RbsA-I/RbsC
D-ribose ABC importer from the nearby reviewed RbsD D-ribose pyranase accessory
enzyme; the then-queued PP_2757-PP_2761 ribose-like comparison was resolved in
the C39 pass below.

Completed the C39 `ppu02010` sub-batch, PP_2757-PP_2761. Fetched `PP_2757`,
`PP_2758`, `rbsA`, `PP_2760`, and `PP_2761`, ran Asta for all five, curated and
validated their review YAMLs warning-free, rendered the gene pages, and extended
`modules/ribose_import_boundary.yaml`. The updated module records
PP_2758/rbsA/PP_2760/PP_2761 as a second RbsABC D-ribose importer while keeping
PP_2757 as an adjacent unresolved sugar-binding component rather than forcing it
into the core ribose-import call.

Completed the C32 `ppu02010` sub-batch, PP_2260-PP_2264. Fetched `PP_2260`,
`PP_2261`, `PP_2262`, `PP_2263`, and `PP_2264`, ran Asta for all five, curated
and validated their review YAMLs warning-free, rendered the gene pages, and
created `modules/sugar_glycerol_phosphate_import_boundary.yaml`. The module
keeps the substrate unresolved, because the locus combines a
glycerol-phosphate-named ATPase with sugar-transporter permease/binding
components; ferric-iron and monoatomic-cation GOA spillovers on `PP_2260` and
`PP_2261` were removed.

Completed the C10 `ppu02010` sub-batch, PP_0280-PP_0283. Fetched `PP_0280`,
`PP_0281`, `artJ`, and `aotP`, ran Asta for all four, curated and validated
their review YAMLs warning-free, and created
`modules/arginine_ornithine_abc_import_boundary.yaml`. The module represents
PP_0280/PP_0281 as ArtM/ArtQ-like permeases, `artJ` as the periplasmic
L-arginine substrate-binding component, and `aotP` as the ATP-binding
energy-coupling subunit; ornithine transport is retained as a caveated lead from
the `aotP` product name rather than direct substrate evidence.

Completed the C23 `ppu02010` sub-batch, PP_1068-PP_1071. Fetched `gltL`,
`gltK`, `gltJ`, and `gltI`, ran Asta for all four, curated and validated their
review YAMLs warning-free, and created
`modules/glutamate_aspartate_abc_import_boundary.yaml`. The module represents
GltL as the ATP-binding energy-coupling subunit, GltK/GltJ as inner-membrane
permeases, and GltI as the periplasmic substrate-binding component of a
predicted glutamate/aspartate ABC uptake system.

Completed the C25 `ppu02010` sub-batch, PP_1137-PP_1141. Fetched `livF-I`,
`livG`, `livM`, `livH`, and `livK`, ran Asta for all five, curated and
validated their review YAMLs warning-free, and created
`modules/branched_chain_amino_acid_abc_import_boundary.yaml`. The module
represents LivF/LivG as ATP-binding energy-coupling subunits, LivM/LivH as
inner-membrane permeases, and LivK as the periplasmic
leucine/branched-chain amino-acid binding component of a predicted high-affinity
BCAA ABC uptake system.

Completed the C62 `ppu02010` sub-batch, PP_4863-PP_4867. Fetched `livF-II`,
`braF`, `braE`, `braD`, and `PP_4867`, ran Asta for all five, curated and
validated their review YAMLs warning-free, and extended
`modules/branched_chain_amino_acid_abc_import_boundary.yaml` with a second
Bra/Liv high-affinity BCAA ABC import part. The module represents LivF-II/BraF
as ATP-binding energy-coupling subunits, BraE/BraD as inner-membrane permeases,
and PP_4867 as a BraC-like periplasmic amino-acid-binding component. The
relative substrate/regulatory differences from the LivFGMHK block remain open.

Completed the C14 `ppu02010` sub-batch, PP_0615-PP_0619. Fetched `PP_0615`,
`PP_0616`, `PP_0617`, `PP_0618`, and `PP_0619`, ran Asta for all five, curated
and validated their review YAMLs warning-free, and extended
`modules/branched_chain_amino_acid_abc_import_boundary.yaml` with a third
high-affinity BCAA ABC import part. The module represents PP_0615/PP_0616 as
ATP-binding energy-coupling subunits, PP_0617/PP_0618 as inner-membrane
permeases, and PP_0619 as a signal-peptide-bearing periplasmic leucine-family
substrate-binding component.

Completed the C59 `ppu02010` sub-batch, PP_4483-PP_4486. Fetched `hisP`,
`hisM`, `hisQ`, and `argT`, ran Asta for all four, curated and validated their
review YAMLs warning-free, and extended
`modules/arginine_ornithine_abc_import_boundary.yaml` into a broader
basic-amino-acid ABC import boundary. The module represents HisP as the
ATP-binding energy-coupling subunit, HisM/HisQ as inner-membrane permeases, and
ArgT as the periplasmic lysine/arginine/ornithine substrate-binding component;
the exact histidine, lysine, arginine, and ornithine substrate preference remains
open.

Completed the C52 `ppu02010` sub-batch, PP_3828-PP_3830. Fetched `modA`,
`modB`, and `modC`, ran Asta for all three, curated and validated their review
YAMLs warning-free, and created `modules/molybdate_abc_import_boundary.yaml`.
The module represents ModA as the signal-peptide-bearing periplasmic
molybdate-binding component, ModB as the inner-membrane permease, and ModC as
the ATP-binding energy-coupling subunit with reviewed EC 7.3.2.5 support for
ATP-dependent molybdate import.

Completed the C61 `ppu02010` sub-batch, PP_4841-PP_4845. Fetched `urtA`,
`urtB`, `urtC`, `urtD`, and `urtE`, ran Asta for all five, curated and
validated their review YAMLs warning-free, and created
`modules/urea_abc_import_boundary.yaml`. The module represents UrtA as the
signal-peptide-bearing periplasmic urea-binding component, UrtB/UrtC as
inner-membrane permeases, and UrtD/UrtE as ATP-binding energy-coupling subunits.
Amino-acid and branched-chain amino-acid transport annotations on the locus were
treated as family-transfer spillover.

Completed the C29 `ppu02010` sub-batch, PP_2154-PP_2156. Fetched `lolC`,
`lolD`, and `lolE`, ran Asta for all three, curated and validated their review
YAMLs warning-free, and created
`modules/lipoprotein_lolcde_localization_boundary.yaml`. The module represents
LolC/LolE as the multi-pass membrane permease components and reviewed LolD as
the ATP-binding energy-coupling subunit that drives transfer of mature outer
membrane-directed lipoproteins to LolA.

Completed the C58 `ppu02010` sub-batch, PP_4324-PP_4327. Fetched `ccmD`,
`ccmC`, `ccmB`, and `ccmA`, ran Asta for all four, curated and validated their
review YAMLs warning-free, and created
`modules/ccm_heme_export_cytochrome_c_maturation_boundary.yaml`. The module
represents CcmD/CcmC/CcmB as inner-membrane heme-handling components for
c-type cytochrome biogenesis and CcmA as the ATP-binding energy-coupling
subunit of CcmAB, while retaining UniProt's caveat that CcmA's exact direct
transport role remains uncertain.

Completed the C20 `ppu02010` sub-batch, PP_0958-PP_0962. Fetched `mlaF`,
`mlaE`, `mlaD`, `ttg2D`, and `ttg2E`, ran Asta for all five, curated and
validated the reviews, and created
`modules/mla_phospholipid_transport_boundary.yaml`. The module represents
MlaF/MlaE/MlaD as the MlaFEDB phospholipid transport core, Ttg2D as a
MlaC-family periplasmic phospholipid-binding component, and Ttg2E as an
unresolved STAS-domain accessory candidate.

Completed the Lpt/MsbA `ppu02010` lipid/LPS export checkpoint. Fetched `lptB`,
`PP_0982`, `PP_0983`, and `msbA` plus module-context `lptA`, `lptC`, `lptD`,
and `lptE`; ran Asta for all eight; curated and validated the reviews; and
created `modules/lpt_lps_transport_boundary.yaml`. The module separates MsbA
lipid A-core flipping at the inner membrane from LptBFGC/A/DE LPS transport and
outer-membrane assembly, and removes the oligopeptide over-propagation on
`msbA`.

Completed the C03 `ppu02010` sub-batch, PP_0140-PP_0142. Fetched `PP_0140`,
`PP_0141`, and `PP_0142`, ran Asta for all three, curated and validated the
reviews, and created
`modules/mce_mlad_mlae_like_phospholipid_transport_boundary.yaml`. The module
records a DRAFT Mce/MlaD-MlaE-like phospholipid transport candidate distinct
from the better supported PP_0958-PP_0962 Mla/Ttg2 system.

Completed the PP_5165/`plpB` `ppu02010` singleton from C69. Fetched `plpB`, ran
Asta, and curated the one membrane GOA row as non-core for an unresolved
NlpA-family lipoprotein. Despite its locus-neighborhood proximity to
`cysA`/`cysW`/`cysU`/`sbp-II`, the review does not add `plpB` to the sulfate
import module because the current evidence does not establish a sulfate,
thiosulfate, methionine, or other substrate-binding role. The expected
no-core-function warning is retained.

Completed the PotF-like polyamine-binding singleton group from C30/C43/C49/C53/C74.
Fetched `PP_2195`, `potF-II`, `PP_3719`, `potF-III`, and `potF-IV`, ran Asta
for all five, curated the polyamine-transport, polyamine-binding, and
periplasmic-space GOA rows, rendered and validated the reviews, and extended
`modules/polyamine_transport_boundary.yaml`. The module now records these as
periplasmic putrescine/polyamine substrate-binding components with unresolved
permease/ATPase partners rather than complete ABC uptake systems.

Completed the C70 Spu/Pot polyamine-import sub-batch, PP_5177-PP_5181. Fetched
`spuH`, `spuG`, `spuF`, `spuE`, and `spuD`, ran Asta for all five, curated and
validated their GOA rows warning-free, and extended
`modules/polyamine_transport_boundary.yaml`. The module now separates this
complete predicted spermidine/putrescine ABC importer from the unresolved
PotF-like singleton binding components.

Completed the C26 YhdWXYZ amino-acid ABC-import sub-batch, PP_1297-PP_1300.
Fetched `yhdW`, `yhdX`, `yhdY`, and `yhdZ`, ran Asta for all four, curated and
validated their GOA rows warning-free, and created
`modules/yhdwxyz_amino_acid_abc_import_boundary.yaml`. The module records a
complete predicted amino-acid ABC importer while keeping the exact transported
amino-acid substrate unresolved; ppu02010 now shows 161/207 curated reviews and
159/207 Asta reports.

Completed the C40 PP_2767-PP_2770 branched-chain amino-acid ABC-import
sub-batch. Fetched `PP_2767`, `PP_2768`, `PP_2769`, and `PP_2770`, ran Asta
for all four, curated and validated the reviews warning-free, and extended
`modules/branched_chain_amino_acid_abc_import_boundary.yaml` with a fourth
predicted high-affinity BCAA importer. The module represents PP_2767 as the
ATP-binding energy-coupling component, PP_2768/PP_2769 as permeases, and
PP_2770 as the leucine-family substrate-binding component; ppu02010 now shows
165/207 curated reviews and 163/207 Asta reports.

Completed the C38 PP_2748-PP_2753 branched-chain amino-acid ABC-import
sub-batch. Fetched `PP_2748`, `PP_2749`, `PP_2750`, `PP_2751`, `PP_2752`, and
`PP_2753`, ran Asta for all six, curated and validated the reviews
warning-free, and extended `modules/branched_chain_amino_acid_abc_import_boundary.yaml`
with a fifth predicted high-affinity BCAA importer. The module represents
PP_2748/PP_2753 as ATP-binding energy-coupling components, PP_2749/PP_2750 as
permeases, and PP_2751/PP_2752 as duplicated leucine-family substrate-binding
components; ppu02010 now shows 171/207 curated reviews and 169/207 Asta
reports.

Completed the C50 PP_3801-PP_3803 Znu-like cation/zinc ABC-import sub-batch.
Fetched `PP_3801`, `PP_3802`, and `PP_3803`, ran Asta for all three, curated
and validated the reviews warning-free, and extended
`modules/zinc_import_boundary.yaml` with a second Znu-like import candidate.
The module represents PP_3801 as the ZnuA-like signal-peptide-bearing
substrate-binding component, PP_3802 as the ATP-binding energy-coupling
component, and PP_3803 as the multi-pass permease; ppu02010 now shows 174/207
curated reviews and 172/207 Asta reports.

Completed the C63/C67/C71 ferric/iron ABC-import pass. Fetched `PP_4881`,
`PP_4882`, `PP_5135`, `PP_5136`, `fbpC`, `PP_5195`, and `fbpA`, ran Asta for all
seven, curated and validated the reviews warning-free, and created
`modules/ferric_iron_abc_import_boundary.yaml`. The module separates the complete
PP_5135-PP_5137 FbpABC-like importer from the partial PP_4881-PP_4882 and
PP_5195-fbpA candidates whose ATPase partners remain unresolved; thiamine
spillover terms on `PP_5135` and quaternary-ammonium transport on `fbpC` were
removed. ppu02010 now shows 181/207 curated reviews and 179/207 Asta reports.

Completed the C42/C54/C72 Yej/Dpp-like peptide ABC-import pass. Fetched
`PP_3076`, `PP_3077`, `PP_3078`, `PP_4146`, `yejA`, `PP_4148`, `PP_4149`,
`yejF`, and `dppA-IV`, ran Asta for all nine, curated and validated the reviews
warning-free, and created `modules/yej_dpp_like_peptide_abc_import_boundary.yaml`.
The module separates the complete PP_4146-PP_4150 Yej/Dpp-like candidate from
the partial PP_3076-PP_3078 candidate and the dppA-IV DppA-family singleton;
microcin transport is retained as non-core Yej-family context pending direct
substrate evidence. ppu02010 now shows 190/207 curated reviews and 188/207 Asta
reports.

Completed the C28 PP_1778-PP_1779 LPS/polysaccharide ABC-export candidate.
Fetched `PP_1778` and `PP_1779`, ran Asta for both, curated and validated both
reviews warning-free, and extended `modules/lpt_lps_transport_boundary.yaml`
with a separate Wzt/KpsT/TagH-like candidate node rather than merging it into
the canonical LptBFG/MsbA system. `PP_1778` is the ABC-2 multi-pass permease and
`PP_1779` is the ATP-hydrolyzing export subunit; exact LPS versus O-antigen,
capsule, or related envelope-polysaccharide substrate remains open. ppu02010
now shows 192/207 curated reviews and 190/207 Asta reports.

Completed the C66 `ftsX`/`ftsE` FtsEX cell-division ABC-like pass. Fetched
`ftsX` and `ftsE`, ran Asta for both, curated and validated both reviews
warning-free, and created `modules/ftsex_cell_division_boundary.yaml`. The pass
treats FtsEX as a cell-division/septal-ring ABC-like complex, not a conventional
transported-substrate ABC system; `ftsE` transmembrane transporter and transport
terms were marked over-annotated pending direct substrate evidence. ppu02010 now
shows 194/207 curated reviews and 192/207 Asta reports.

Completed the C55/C56 `pvdT`/`pvdE` pyoverdine-export Asta backfill. Ran Asta
for both already-curated reviews, validated `pvdT`, updated `pvdE` to cite the
relevant Falcon deep-research evidence rather than the weak Asta retrieval, and
validated/rendered `pvdE` warning-free. No new broad pyoverdine export module
was created; the existing siderophore boundary remains a partial biosynthesis/
precursor module. ppu02010 now shows 194/207 curated reviews and 194/207 Asta
reports.

Completed the C04/C15/C31/C34/C64 secretion/exporter pass. Fetched `paxB`,
`PP_0804`, `PP_2240`, `aprDA`, and `cyaB`, ran Asta for all five, curated,
validated, and rendered all five reviews, and created/validated/rendered
`modules/type_i_protein_secretion_abc_boundary.yaml`. The module includes
`paxB`, `PP_0804`, `aprDA`, and `cyaB` as T1SS/type-I-secretion ABC exporter
candidates; `PP_2240` is treated separately as an unresolved ABCD-like efflux
transporter. Asta was mostly retrieval-only/product confirmation, so UniProt,
InterPro, and GOA drove the first-pass calls. ppu02010 now shows 199/207
curated reviews and 199/207 Asta reports.

Completed the final ppu02010 gap pass. Fetched `PP_0524`, `PP_1078`,
`PP_2595`, `PP_2596`, `PP_2628`, `PP_3818`, `PP_4542`, and `PP_5157`, ran
Asta for all eight, curated/validated/rendered all eight reviews, and extended
`modules/phosphate_import_boundary.yaml` with `PP_3818` as a phosphate-binding
singleton. `PP_0524` was treated as a cobalamin-binding candidate with the
iron-response GOA term removed; `PP_1078`, `PP_2595`, `PP_2596`, `PP_2628`,
and `PP_4542` remain substrate-unknown ABC-family transporter candidates; and
`PP_5157` remains a cell-envelope solute-binding-family protein without a
substrate core function. ppu02010 now shows 207/207 curated reviews and
207/207 Asta reports.

Completed the compact DNA-repair `ppu03450` /
`bacterial_non_homologous_end_joining` checkpoint. Registered the new module
mapping, created and validated
`modules/bacterial_non_homologous_end_joining.yaml`, fetched `ku` and `ligD`,
ran Asta for both, curated/validated/rendered both reviews, regenerated the
two-gene batch checklist, rebuilt the pathway worklist, and rendered the module
page.

Main ppu03450 lesson: this KEGG map is a clean two-gene Ku/LigD bacterial NHEJ
module, not a broad DNA-repair bucket. `ku` is curated for double-stranded DNA
end binding and NHEJ participation; broad DNA binding and DNA repair terms are
narrowed to the specific dsDNA/NHEJ calls. `ligD` is curated as the
ATP-dependent DNA ligase component, with missing `NEW` DNA-directed DNA
polymerase, exonuclease, and NHEJ process annotations added from UniProt domain
and keyword evidence. Asta mostly confirmed target identity and did not add
gene-specific literature.

Completed the boundary/absence `ppu03008` /
`ribosome_biogenesis_eukaryotes_boundary` checkpoint. Registered the new module
mapping, created and validated
`modules/ribosome_biogenesis_eukaryotes_boundary.yaml`, fetched missing review
folders for `PP_2912` and `orn`, ran Asta for all three candidates, curated and
validated `rnc`, `PP_2912`, and `orn`, regenerated the three-gene batch
checklist, rebuilt the pathway worklist, and rendered the three gene pages and
module page. The real Falcon module and module+pathway commands were attempted
and both failed at Edison task creation with HTTP 402.

Main ppu03008 lesson: this is a bacterial RNA-processing boundary bucket, not a
eukaryotic ribosome-biogenesis pathway. `rnc` is RNase III for rRNA processing,
`orn` is cytoplasmic oligoribonuclease for small RNA-fragment turnover, and
`PP_2912` is an inferred RIO-type serine/threonine kinase-like protein with an
unresolved organism-specific role. No eukaryotic ribosome-biogenesis GO
annotation is proposed for KT2440 from this bucket.

Completed the compact information-processing `ppu03020` /
`bacterial_rna_polymerase_core` checkpoint. Registered the new module mapping,
created and validated `modules/bacterial_rna_polymerase_core.yaml`, fetched the
four core RNAP genes by UniProt accession with symbol aliases (`rpoA`, `rpoB`,
`rpoC`, `rpoZ`), ran Asta for all four, curated/validated/rendered all four
reviews, regenerated the batch checklist, rebuilt the pathway worklist, and
rendered the module page.

Main ppu03020 lesson: this KEGG map is a compact bacterial RNAP core-complex
bucket, not a broad transcription/regulation pathway. `rpoA`, `rpoB`, and
`rpoC` are curated as core contributors to DNA-directed RNA polymerase activity
and DNA-templated transcription in the GO:0000428 RNAP complex. `rpoZ` is kept
as the omega assembly/stabilization subunit: its DNA binding and 5'-3' RNA
polymerase activity rows are treated as over-broad/complex-level propagation
rather than independent omega catalytic activities. Sigma factors and
pathway-specific transcription regulators remain outside this compact module.

Completed the boundary/absence `ppu03250` /
`viral_life_cycle_hiv1_boundary` checkpoint. Registered the new module mapping,
created and validated `modules/viral_life_cycle_hiv1_boundary.yaml`, confirmed
the single mapped member `ppiA` was already fetched, Asta-backed, curated, and
valid, regenerated the one-gene batch checklist, rebuilt the pathway worklist,
and rendered the `ppiA` and module pages. The real Falcon module and
module+pathway commands were attempted and both failed at Edison task creation
with HTTP 402.

Main ppu03250 lesson: this is a KEGG cross-map artifact for KT2440, not a
satisfiable viral pathway. The only PSEPK member is `ppiA`, a
cyclophilin-family peptidyl-prolyl cis-trans isomerase involved in protein
folding. The module records explicit pathway absence/boundary status so `ppiA`
does not acquire viral-life-cycle annotations from the HIV-1 map.

Completed the boundary/absence `ppu04148` / `efferocytosis_boundary`
checkpoint. Registered the new module mapping, created and validated
`modules/efferocytosis_boundary.yaml`, confirmed the two mapped members `speC`
and `petA` were already fetched, Asta-backed, and curated, cleaned up their
validation warnings, regenerated the two-gene batch checklist, rebuilt the
pathway worklist, and rendered the `speC`, `petA`, and module pages. The real
Falcon module and module+pathway commands were attempted and both failed at
Edison task creation with HTTP 402.

Main ppu04148 lesson: this is also a KEGG cross-map artifact for KT2440. The
mapped genes are native bacterial side nodes: `speC` is ornithine decarboxylase
for putrescine/polyamine biosynthesis, and `petA` is the Rieske iron-sulfur
subunit of respiratory complex III. The module records explicit
efferocytosis-pathway absence so neither gene is promoted to a eukaryotic
apoptotic-cell-clearance process.

Completed the boundary `ppu04980` /
`cobalamin_transport_metabolism_boundary` checkpoint. Registered the new module
mapping, created and validated
`modules/cobalamin_transport_metabolism_boundary.yaml`, confirmed the two mapped
members `pduO` and `metH` were already fetched, Asta-backed, and curated,
anchored Asta support in both existing annotation reviews to clear validation
warnings, regenerated the two-gene batch checklist, rebuilt the pathway
worklist, and rendered the `pduO`, `metH`, and module pages. The real Falcon
module and module+pathway commands were attempted and both failed at Edison task
creation with HTTP 402.

Main ppu04980 lesson: this is a cobalamin-metabolism boundary bucket, not a
complete cobalamin transport pathway. The mapped genes are two native enzymatic
contexts: `pduO` is corrinoid/cobalamin adenosyltransferase in cobalamin or
cobamide metabolism, and `metH` is cobalamin-dependent methionine synthase
linking cobalamin cofactor use to methionine biosynthesis and one-carbon/folate
metabolism. No cobalamin transport GO annotation is proposed from this two-gene
bucket.

Completed the first-pass `ppu00550` / `peptidoglycan_biosynthesis` checkpoint.
Created and validated `modules/peptidoglycan_biosynthesis.yaml`, registered the
KEGG mapping, promoted `murJ` from UniPathway UPA00219 as the expected lipid II
flippase, fetched all missing review folders, ran Asta for all 24 candidates,
curated the 14 remaining stubs, validated all 24 batch gene reviews and the
module, rendered all 24 gene pages, and refreshed the batch page.

Main ppu00550 lessons: the strict peptidoglycan route is covered by Mur/Ddl
cytosolic precursor enzymes, UppS/UppP/MraY/MurG lipid-carrier and lipid I/II
assembly, `murJ` lipid II flipping, SEDS-family polymerases `ftsW` and `mrdB`,
class A PBPs `mrcA`, `mrcB`, `pbpC`, and `mtgA`, class B PBPs/transpeptidases
`ftsI`, `mrdA-I`, and `mrdA-II`, plus carboxypeptidase/remodeling nodes `dacA`
and `dacB`. Transporter over-propagation on `ftsW`/`mrdB`, glycosyltransferase
over-propagation on `ftsI`, and L,D-transpeptidase over-propagation on
`mrdA-I`/`mrdA-II` were removed. `uppP` received a first-pass `NEW`
peptidoglycan biosynthetic process lead from UniProt because the local GOA block
omitted that process row.

Completed the first-pass `ppu00552` /
`teichoic_acid_biosynthesis_boundary` checkpoint. Created and validated
`modules/teichoic_acid_biosynthesis_boundary.yaml`, registered the KEGG mapping,
regenerated the two-gene checklist, validated `wbpM` and `uppP`, rendered both
gene pages, and refreshed the batch page.

Main ppu00552 lessons: this is a boundary/absence batch in Gram-negative KT2440,
not support for a complete wall or lipoteichoic-acid pathway. `uppP` is shared
undecaprenyl carrier recycling and peptidoglycan/cell-envelope context; `wbpM`
is still an unresolved polysaccharide-biosynthesis/CapD-like membrane protein
with no specific molecular-function GOA row and no assigned core function.

Completed the first-pass `ppu00561` / `glycerolipid_metabolism_boundary`
checkpoint. Created and validated `modules/glycerolipid_metabolism_boundary.yaml`,
registered the KEGG mapping, fetched the eight missing review folders, ran or
retried Asta until all 12 candidates had retrieval reports, curated the eight
new stubs, validated all 12 batch gene reviews and the module, rendered all 12
gene pages, and refreshed the batch page.

Main ppu00561 lessons: this is a broad glycerolipid/glycerophospholipid boundary
map. Core lipid precursor assembly is `plsX`, `plsY`, `plsB`, `plsC`, `PP_0058`,
`dgkA-I`, and `dgkA-II`; `glpK` is glycerol-entry/glycerol-catabolism context;
`calA`, `garK`, `ttuD`, and `lip` are side or boundary nodes. `plsX` received a
first-pass `NEW` phospholipid biosynthetic process lead from UniProt because the
local GOA table omitted the process row. `lip` remains an unreviewed
alpha/beta-hydrolase candidate with no GOA terms or assigned core function
pending substrate evidence.

Completed the first-pass `ppu00562` /
`inositol_phosphate_metabolism_boundary` checkpoint. Created and validated
`modules/inositol_phosphate_metabolism_boundary.yaml`, registered the KEGG
mapping, fetched `suhB`, ran Asta, curated the new `suhB` stub, validated all
four batch gene reviews and the module, rendered all four gene pages, and
refreshed the batch page.

Main ppu00562 lessons: this is a boundary/absence map, not a complete
phosphatidylinositol or inositol-polyphosphate signalling pathway in KT2440.
`suhB` is the only direct inositol-phosphate enzyme; its review accepts
inositol-monophosphatase activity, marks signal transduction as over-annotated,
removes phosphatidylinositol dephosphorylation, and adds a first-pass `NEW`
transcription antitermination lead from the UniProt rrnTAC function note.
`mmsA-I`, `mmsA-II`, and `tpiA` remain side nodes from valine/thymine/propanoate
or central-carbon metabolism.

Completed the first-pass `ppu00564` / `glycerophospholipid_metabolism`
checkpoint. Created and validated `modules/glycerophospholipid_metabolism.yaml`,
registered the KEGG mapping, regenerated the 23-gene checklist, fetched 13
missing review folders, ran Asta for those genes plus `gpsA`, curated all new
stubs, validated all 23 batch gene reviews and the module, rendered all 23 gene
pages, and refreshed the batch page.

Main ppu00564 lessons: this is a broad glycerophospholipid metabolism map, not
one linear route. The direct membrane-phospholipid core includes the reused
PlsX/PlsY/PlsB/PlsC/PP_0058/DgkA precursor chemistry plus `cdsA`, `pgsA`,
`pgpA`, `clsA`, `clsB`, `pssA`, `PP_4677`, `psd`, and `pcs`. `gpsA` and
`glpD` are glycerol-3-phosphate supply/catabolism context, `ugpQ` and `pchP`
are headgroup-turnover/scavenging context, and `eutB`/`eutC` are ethanolamine
catabolism side nodes. PLD-family `PP_0892` is accepted as a candidate
cardiolipin synthase from TreeGrafter/PANTHER context; `PP_5276` remains a
substrate-unresolved phosphatidyltransferase candidate with cardiolipin
biosynthesis marked undecided.

Completed the first-pass `ppu00566` /
`sulfoquinovose_metabolism_boundary` checkpoint. Created and validated
`modules/sulfoquinovose_metabolism_boundary.yaml`, registered the KEGG mapping,
fetched `yihS`, ran Asta, curated the `yihS` stub, validated both batch gene
reviews and the module, rendered both gene pages, and refreshed the batch page.

Main ppu00566 lessons: KT2440 does not have a complete sulfoquinovose
degradation pathway from this KEGG membership. `mdh` is a reviewed
NAD-dependent malate dehydrogenase with TCA-cycle core function and should be
read as central-carbon spillover. `yihS` is the curation question: KEGG assigns
PP_1014 to K18479 sulfoquinovose isomerase (EC 5.3.1.31), but UniProt/GOA
currently assign EC 5.3.1.7 mannose isomerase. The review adds a first-pass
`NEW` sulfoquinovose isomerase candidate lead from KEGG notes, leaves mannose
isomerase `UNDECIDED`, and does not assign a core function pending substrate
evidence.

Completed the first-pass `ppu00592` /
`alpha_linolenic_acid_metabolism_boundary` checkpoint. Created and validated
`modules/alpha_linolenic_acid_metabolism_boundary.yaml`, registered the KEGG
mapping, regenerated the two-gene checklist, validated and rendered both
existing FadA review pages, and refreshed the batch page.

Main ppu00592 lessons: this is a boundary/absence map, not evidence for a
complete alpha-linolenic-acid-specific route in KT2440. Both KEGG candidates,
`fadA__Q88L84` and `fadA__Q88L01`, are already curated as FadA-like
3-ketoacyl-CoA thiolases in fatty-acid beta-oxidation. The pathway should be
read as generic beta-oxidation side context, not plant oxylipin or
alpha-linolenate-specific metabolism.

Completed the first-pass `ppu00620` / `pyruvate_metabolism_boundary`
checkpoint. Created and validated `modules/pyruvate_metabolism_boundary.yaml`,
registered the KEGG mapping, regenerated the 54-gene checklist, fetched 10
missing review folders, ran Asta for those genes plus `ppc`, curated the 10 new
stubs, validated all 54 resolved batch gene reviews and the module, rendered all
54 resolved review pages, and refreshed the batch page.

Main ppu00620 lessons: this is a broad boundary map, not one pyruvate pathway.
The direct pyruvate/lactate/glyoxalase tail is covered by `PP_1389`, `ldhA`,
`lldD`, `dld2`, `gloA`, and `gloB`; `glcB` is glyoxylate-shunt spillover,
`maeB` is malate-to-pyruvate/NADPH context, and `ycgM` is only a provisional
acetylpyruvate hydrolase candidate. `PP_0772` remains an unresolved
metallo-beta-lactamase-family candidate with no GOA rows and no assigned core
function. Several overlap rows resolve to prior reviews, including `aldB-II` as
`pedI`, so accession-based batch resolution is required for validation and
rendering.

Completed the first-pass `ppu00621` / `dioxin_degradation_boundary` checkpoint.
Created and validated `modules/dioxin_degradation_boundary.yaml`, registered
the KEGG mapping, regenerated the two-gene checklist, validated and rendered
`PP_1791` and `PP_2504`, and refreshed the batch page.

Main ppu00621 lessons: this is another boundary/absence xenobiotic map, not a
complete dioxin degradation route in KT2440. `PP_2504` has UniProt EC 5.3.2.6
2-hydroxymuconate/4-oxalocrotonate tautomerase context but only broad
isomerase GOA, while `PP_1791` remains an unresolved aldolase/synthase-family
candidate with leucine-biosynthesis annotations left undecided in the gene
review.

Completed the first-pass `ppu00625` /
`chloroalkane_chloroalkene_degradation_boundary` checkpoint. Created and
validated `modules/chloroalkane_chloroalkene_degradation_boundary.yaml`,
registered the KEGG mapping, fetched `fdhA`, ran Asta for `fdhA`, curated the
new `fdhA` stub, regenerated the five-gene checklist, validated all five batch
gene reviews and the module, rendered all five gene pages, and refreshed the
batch page.

Main ppu00625 lessons: this is a boundary/absence xenobiotic map, not support
for a complete chloroalkane or chloroalkene degradation route in KT2440. The
membership is formaldehyde/alcohol oxidation side context: `fdhA` is a
glutathione-independent NAD-dependent formaldehyde dehydrogenase, `frmA` is
glutathione-dependent formaldehyde detoxification, `pedE` and `pedH` are
periplasmic PQQ alcohol dehydrogenases, and `adhP` is a broad zinc alcohol
dehydrogenase. The batch lacks dehalogenase or chloroalkene-specific upper-route
chemistry.

Completed the first-pass `ppu00626` / `naphthalene_degradation_boundary`
checkpoint. Created and validated `modules/naphthalene_degradation_boundary.yaml`,
registered the KEGG mapping, regenerated the two-gene checklist, validated and
rendered `frmA` and `adhP`, and refreshed the batch page.

Main ppu00626 lessons: this is a boundary/absence xenobiotic map, not a
complete naphthalene degradation route in KT2440. The only KEGG members are
`frmA`, a glutathione-dependent formaldehyde detoxification enzyme, and `adhP`,
a broad zinc alcohol dehydrogenase with unresolved physiological substrate.
The batch lacks naphthalene dioxygenase, cis-dihydrodiol dehydrogenase,
salicylate hydroxylase, and ring-cleavage route enzymes.

Completed the first-pass `ppu00627` / `aminobenzoate_degradation_boundary`
checkpoint. Created and validated `modules/aminobenzoate_degradation_boundary.yaml`,
registered the KEGG mapping, fetched `PP_2805`, `vdh`, `PP_3358`, and
`PP_3657`, ran Asta for those four plus `galA`, `fcs`, `vanA`, and `vanB`,
curated the four new stubs, regenerated the 12-gene checklist, validated all 12
batch gene reviews and the module, rendered all 12 gene pages, and refreshed
the batch page.

Main ppu00627 lessons: this is a boundary aromatic/xenobiotic map, not one
complete aminobenzoate degradation route. The useful biology belongs to several
separate side funnels: `galA` gallate catabolism; `fcs`, `PP_3358`, `vdh`,
`vanA`, and `vanB` ferulate/vanillin/vanillate catabolism; `PP_2805`
Baeyer-Villiger monooxygenase side chemistry; `PP_3657` nitroreductase-family
redox context; `ubiX` prenyl-FMN cofactor formation; and `PP_2217`/`paaF`/`PP_2932`
CoA-thioester or unresolved amidase side nodes. `PP_3358` now uses the specific
feruloyl-CoA hydratase/lyase term and drops the unsupported isoprenoid process.

Completed the first-pass `ppu00630` /
`glyoxylate_dicarboxylate_metabolism_boundary` checkpoint. Created and
validated `modules/glyoxylate_dicarboxylate_metabolism_boundary.yaml`,
registered the KEGG mapping, fetched 16 missing review folders using accession
folders for PP_2183 (`Q88KV6`) and PP_2185 (`Q88KV4`), ran Asta for those genes
plus `aceA`, curated the 16 new stubs, regenerated the 62-gene checklist,
validated all 62 batch gene reviews and the module, rendered all 62 resolved
review pages, and refreshed the batch page.

Main ppu00630 lessons: this is a broad central-carbon boundary map, not one
linear glyoxylate/dicarboxylate pathway. The direct glycolate/glyoxylate route
is `glcD`/`glcE`/`glcF` glycolate oxidase/dehydrogenase plus `gcl`, `hyi`, and
`glxR` for glyoxylate carboligase/tartronate-semialdehyde chemistry. `PP_0416`
is direct phosphoglycolate repair context, while `PP_0094` and `PP_1907` are
HAD/nucleotidase-side or unresolved nodes. `fdoG`/`fdoH`/`fdoI`,
PP_2185/`Q88KV4`, PP_2186, PP_2183/`Q88KV6`, and `PP_2184` are formate
oxidation or respiratory NDH side context. TCA, one-carbon, glycine-cleavage,
acyl-CoA, catalase, and glutamine-synthetase overlaps remain neighboring
biology rather than core members of a single glyoxylate route.

Completed the first-pass `ppu00633` /
`nitrotoluene_degradation_boundary` checkpoint. Created and validated
`modules/nitrotoluene_degradation_boundary.yaml`, registered the KEGG mapping,
fetched `nfnB`, `PP_2486`, and `nemA`, ran Asta for all three, curated the new
stubs, regenerated the three-gene checklist, validated all three gene reviews
and the module, rendered all three gene pages, and refreshed the batch page.

Main ppu00633 lessons: this is a boundary/absence xenobiotic map, not evidence
for a complete nitrotoluene degradation pathway in KT2440. `nfnB` is retained
as a nitroreductase-family oxidoreductase with the EC-derived
6,7-dihydropteridine reductase call left undecided pending substrate evidence.
`PP_2486` and `nemA` are OYE/NADH-flavin oxidoreductase-family side nodes; their
broad oxidoreductase GOA rows are refined to the UniProt-supported CH-CH donor
and NAD(P)-acceptor oxidoreductase parent. The batch lacks route-defining
nitrotoluene upper-pathway and downstream ring-cleavage enzymes.

Completed the first-pass `ppu00640` / `propanoate_metabolism_boundary`
checkpoint. Created and validated `modules/propanoate_metabolism_boundary.yaml`,
registered the KEGG mapping, fetched `prpB`, `acnA-II`, `prpF`, `prpD`,
`prpE`, and `yqhD`, ran or retried Asta until all six had retrieval reports,
curated the six initialized stubs, regenerated the 33-gene checklist, validated
all 33 batch gene reviews and the module, rendered all 33 gene pages, and
refreshed the batch page. `acnB` also received a first-pass `NEW` propionate
catabolic process annotation so its methylcitrate-cycle core function is
reflected in the existing-annotation block.

Main ppu00640 lessons: this is a broad propanoate boundary map whose interpretable
core is the Prp/methylcitrate route, not every KEGG member. `prpE`, `prpC`,
`prpD`, `prpF`, `acnA-II`, `acnB`, and `prpB` provide propionate/propionyl-CoA
activation and methylcitrate-cycle chemistry, but AcnB carries the strongest
organism-specific evidence for the key odd-chain-fatty-acid methylcitrate
dehydratase/hydratase role. `prpD`, `prpF`, and `acnA-II` are retained as
sequence-supported route candidates with unresolved in vivo division of labor.
`mmsA-I`/`mmsA-II`, `PP_0596`, and `yqhD` are methylmalonate-semialdehyde,
beta-alanine/valine-thymine, or broad alcohol-dehydrogenase side context.
ACC, acetate/acetyl-CoA, TCA/glyoxylate, beta-oxidation/acyl-CoA, and
BCKDH/lipoamide genes remain neighboring metabolism rather than one linear
propanoate pathway.

Completed the first-pass `ppu00643` / `styrene_degradation_boundary` checkpoint.
Created and validated `modules/styrene_degradation_boundary.yaml`, registered
the KEGG mapping, regenerated the five-gene checklist, validated all five gene
reviews and the module, rendered all five gene pages, refreshed the batch page,
and generalized `PP_2932` wording from a stale ppu00330-only note to an
unresolved amidase-family side-candidate note spanning the current KEGG boundary
contexts.

Main ppu00643 lessons: this is a boundary/absence xenobiotic map, not evidence
for complete styrene degradation in KT2440. The expected styrene upper-route
steps, styrene monooxygenase and styrene oxide isomerase, are not represented in
the five-gene KEGG membership. `peaE` is the only direct styrene-adjacent enzyme,
capturing phenylacetaldehyde dehydrogenase activity. `hmgA`, `hmgC`, and `hmgB`
belong to the already-curated homogentisate route for L-phenylalanine,
L-tyrosine, and 3-hydroxyphenylacetate degradation. `PP_2932` remains an
unresolved amidase-family candidate with no GOA annotations or core function.

Completed the first-pass `ppu00650` / `butanoate_metabolism_boundary`
checkpoint. Created and validated `modules/butanoate_metabolism_boundary.yaml`,
registered the KEGG mapping, fetched `bdhA`, `gbd`, and `hbdH`, ran Asta for
the five primary ppu00650 genes including `phaA` and `phaC`, curated the three
new dehydrogenase stubs, regenerated the 38-gene checklist, validated all 38
gene reviews and the module, rendered all 38 gene pages plus the module page,
and refreshed the batch page.

Main ppu00650 lessons: this is a broad butanoate/PHA boundary map. The primary
genes are three short-chain redox enzymes, `bdhA` (predicted
(R,R)-butanediol dehydrogenase), `gbd` (4-hydroxybutyrate dehydrogenase), and
`hbdH` (3-hydroxybutyrate dehydrogenase), plus the class II PHA polymerases
`phaA`/PhaC1 and `phaC`/PhaC2. Asta retrieval for the three new dehydrogenases
was mostly generic, so their reviews deliberately stay anchored to UniProt/GOA
EC and family evidence. The remaining ppu00650 members are better interpreted
through their native modules: succinate-semialdehyde/GABA aldehyde oxidation,
acetoacetate/acyl-CoA activation, beta-oxidation and thiolase chemistry,
phenylacetate/caprolactam side enzymes, BCAA/acetolactate precursor chemistry,
and TCA succinate dehydrogenase.

Completed the first-pass `ppu00660` /
`c5_branched_dibasic_acid_metabolism_boundary` checkpoint. Created and
validated `modules/c5_branched_dibasic_acid_metabolism_boundary.yaml`,
registered the KEGG mapping, regenerated the 10-gene checklist, validated all
10 already-curated gene reviews plus the module, rendered all 10 gene pages
plus the module page, and refreshed the batch page.

Main ppu00660 lessons: the map is a boundary overlap rather than a standalone
C5-branched dibasic acid route. PP_1157, PP_1394, `ilvI`, and `ilvH` are
AHAS/acetolactate synthase catalytic or regulatory nodes that belong with
valine and isoleucine precursor biosynthesis. `leuC`, `leuD`, and `leuB` are
the leucine isopropylmalate branch. `galC` is gallate catabolism, while `sucD`
and `sucC` are TCA-cycle succinate-CoA ligase subunits. No additional gene
review edits were needed for this checkpoint.

Completed the first-pass `ppu00680` / `methane_metabolism_boundary` checkpoint.
Created and validated `modules/methane_metabolism_boundary.yaml`, registered
the KEGG mapping, fetched the two missing review folders (`frmC` by accession
Q88MF4 and `peaA` by symbol), ran Asta for both, curated both new review stubs,
regenerated the 30-gene checklist, validated all 30 gene reviews and the
module, rendered all 30 gene pages plus the module page, and refreshed the
batch page.

Main ppu00680 lessons: this is a boundary/absence map for KT2440, not evidence
for methane oxidation or methanogenesis. The useful C1 biology is downstream
formaldehyde and formate handling: `fdhA`, `frmA`, and newly curated `frmC`
support formaldehyde detoxification, while `fdoGHI`, PP_2185, and PP_2186 are
formate dehydrogenase/oxidation context. GlyA/serine, hydroxypyruvate,
gluconeogenic, acetate/acetyl-CoA, and NDH-like redox genes are side contexts.
Newly curated `peaA` is a predicted exported quinohaemoprotein amine
dehydrogenase alpha subunit; its partner subunits and in vivo substrate remain
open questions.

Completed the first-pass `ppu00710` /
`carbon_fixation_calvin_cycle_boundary` checkpoint. Created and validated
`modules/carbon_fixation_calvin_cycle_boundary.yaml`, registered the KEGG
mapping, regenerated the 13-gene checklist, validated all 13 already-curated
gene reviews plus the module, rendered all 13 gene pages plus the module page,
and refreshed the batch page.

Main ppu00710 lessons: the KT2440 candidate set is a Calvin-cycle
boundary/absence case. It contains non-oxidative pentose-phosphate enzymes
(`rpe`, `rpiA`, `tktA`, `tal`), lower EMP/gluconeogenic enzymes (`gapA`,
`gapB`, `pgk`, `tpiA`, `fba`, `fbp`), PEPC anaplerotic carbon fixation (`ppc`),
malic enzyme (`maeB`), and TCA malate dehydrogenase (`mdh`), but no
route-defining Rubisco or phosphoribulokinase support for a complete
Calvin-Benson-Bassham cycle. No additional gene-review edits were needed.

Completed the first-pass `ppu00780` / `biotin_metabolism_boundary` checkpoint.
Created and validated `modules/biotin_metabolism_boundary.yaml`, registered the
KEGG mapping, fetched the seven missing BioC/BioH/BioF/BioA/BioD/BioB/BirA
review folders, ran Asta for those genes, curated all seven new stubs, validated
the complete 16-gene batch plus the module, rendered all 16 gene pages plus the
module page, and refreshed the batch page.

Main ppu00780 lessons: KT2440 has a coherent BioC/BioH pimelate precursor route
feeding the BioF/BioA/BioD/BioB de novo biotin biosynthesis branch. `birA` is
part of the broader biotin metabolism boundary through biotin-protein ligation
and biotin-operon repression, not biotin synthesis itself. The FAS-II enzymes
and SDR/reductase candidates in the KEGG map (`fabG`, `fabZ`, `fabF`, `fabB`,
`PP_3303`, `PP_0581`, `PP_1852`, `PP_2540`, `PP_2783`) should remain acyl-ACP
precursor or unrelated side-node context rather than committed biotin pathway
steps.

Completed the first-pass `ppu00785` / `lipoic_acid_metabolism_boundary`
checkpoint. Created and validated `modules/lipoic_acid_metabolism_boundary.yaml`,
registered the KEGG mapping, fetched the two missing `lipA` and `lipB` review
folders, ran Asta for both, curated both stubs, validated the complete 19-gene
batch plus the module, rendered all 19 gene pages plus the module page, and
refreshed the batch page.

Main ppu00785 lessons: the strict endogenous lipoate/lipoylation spine is
`lipB` octanoyl transfer followed by `lipA` radical-SAM sulfur insertion. The
remaining KEGG genes are lipoate-dependent targets or redox partners: PDH
(`aceE`, `aceF`, `lpd`), OGDH (`sucA`, `sucB`, `lpdG`), BCKDH (`bkdAA`,
`bkdAB`, `bkdB`, `lpdV`), glycine cleavage (`gcvP1`, `gcvH1`, `gcvT-I`,
`gcvP2`, `gcvH2`, `gcvT`), and acetoin-cleavage E2-like `acoC`. These should
not be interpreted as additional lipoate-biosynthesis enzymes.

Completed the first-pass `ppu00860` / `porphyrin_metabolism_boundary`
checkpoint. Created and validated
`modules/porphyrin_metabolism_boundary.yaml`, registered the KEGG mapping,
fetched or rechecked all 46 review folders, ran Asta for every candidate with
retries for intermittent provider failures, curated all ppu00860 review YAMLs,
validated the complete 46-gene batch plus the module, rendered all 46 gene
pages plus the module page, and refreshed the batch page.

Main ppu00860 lessons: this KEGG bucket is a tetrapyrrole boundary, not one
linear porphyrin pathway. The heme/protoporphyrin spine (`gltX`, `hemA`,
`hemL`, `hemB`, `hemBB`, `hemC`, `hemD`, `hemE`, `hemF`, `hemN`, `PP_0431`,
`hemH`) should be kept separate from heme O/A maturation (`cyoE1`, `cyoE2`,
`PP_0109`), the large cobalamin/corrinoid branch, the siroheme branch (`cobA`,
`cysG`), heme oxygenase/utilization nodes (`hemO`, `PP_2582`, `PP_1358`), and
bacterioferritin/iron-storage side nodes. The first pass removed clear
electronic spillovers in CobD/CobQ transporter annotations, CobK DNA terms, and
CobL protein-methyltransferase terms, and narrowed HemN/CysG annotations toward
oxygen-independent coproporphyrinogen dehydrogenase and sirohydrochlorin
ferrochelatase respectively. `PP_0188` remains an unresolved HemX-family
boundary candidate.

## 2026-07-07

Completed the first-pass `ppu00543` /
`exopolysaccharide_biosynthesis_boundary` checkpoint. Created and validated
`modules/exopolysaccharide_biosynthesis_boundary.yaml`, registered the KEGG
mapping, fetched the four missing review folders, ran or retried Asta until all
11 candidates had retrieval reports, curated the four new stubs, validated all
11 batch gene reviews and the module, rendered all 11 gene pages, and refreshed
the batch page.

Main ppu00543 lessons: this is an alginate/exopolysaccharide boundary map. The
core alginate-production nodes are `alg8` and `alg44`; O-acetylation and
periplasmic modification context is `algF`, `algJ`, `algI`, and `algX`;
`PP_2124` is only an unresolved glycosyltransferase candidate; and `PP_0228`,
`cysE`, `PP_1110`, and `PP_3136` are serine O-acetyltransferase/cysteine
biosynthesis spillovers. `algJ` and `algX` received first-pass `NEW` broad
acyltransferase annotations from UniProt, while `PP_2124`'s LPS biosynthetic
process annotation was marked over-annotated pending substrate evidence.

Completed the first-pass `ppu00541` /
`nucleotide_sugar_biosynthesis_boundary` checkpoint. Created and validated
`modules/nucleotide_sugar_biosynthesis_boundary.yaml`, registered the KEGG
mapping, fetched the missing review folders by accession, ran Asta for the newly
selected genes, curated the new stubs, validated all 26 batch gene reviews and
the module, rendered all 26 gene pages, and refreshed the batch page.

Main ppu00541 lessons: the KEGG map is a composite nucleotide-sugar boundary
rather than a single pathway. ADP-heptose/LPS-core precursor chemistry is
covered by `gmhA`, `hldE`, and `gmhB`; Kdo/CMP-Kdo chemistry by `kdsD`,
`PP_1806`, `kdsA1`, `kdsA2`, `kdsC`, and `kdsB`; dTDP-rhamnose chemistry by
`rfbA`, `rffG`, `rmlC`, `rfbC`, `PP_0500`, and `rfbD`; and GDP/UDP sugar or
shared precursor branches by `algA`, `PP_1776`, `gmd`, `rmd`, `galU`, `udg`,
`glmU`, and `rffE`. `wbpV`, `wbpM`, and `PP_5212` were left as unresolved side
nodes with no forced substrate claim. `kdsC`'s CMP-sialic-acid
cytidylyltransferase annotation was removed as a likely wrong spillover, and
broad parent terms were kept non-core or marked over-annotated where specific
enzyme terms were available.

Completed the first-pass `ppu00540` / `lipopolysaccharide_biosynthesis`
checkpoint. Created and validated `modules/lipopolysaccharide_biosynthesis.yaml`,
registered the KEGG mapping, fetched all 20 missing review folders by accession,
ran Asta for all 20 genes, curated all 20 stubs, validated all 20 gene reviews
and the module, rendered all 20 gene pages, and refreshed the batch page.

Main ppu00540 lessons: the KEGG map combines de novo lipid IVA/lipid A
biosynthesis (`lpxA`, `lpxC`, `lpxD`, `lpxH`, `lpxB`, `lpxK`), Kdo2-lipid A and
late acylation (`waaA`, `htrB`/`lpxL`, `PP_0063`), LPS core assembly (`waaC`,
`waaF`, `waaG`, `waaP`), and remodeling/unresolved side nodes (`pagL-I`,
`pagL-II`, `yijP`, `PP_0024`, `PP_4592`, `lpxOA`, `PP_4570`). Broad membrane,
cofactor, hydrolase, glycosyltransferase, transferase, and acyltransferase
parent terms were kept non-core or marked over-annotated where a specific
enzyme term was available. `lpxK`'s LPS-core process was marked over-annotated
in favor of lipid A biosynthesis, and first-pass UniProt-backed `NEW`
annotations were added for `PP_0063`, `lpxOA`, and `PP_4570`.

Completed the first-pass `ppu00525` /
`acarbose_validamycin_biosynthesis_boundary` checkpoint. Created and validated
`modules/acarbose_validamycin_biosynthesis_boundary.yaml`, registered the KEGG
mapping, extracted the two KEGG ppu00525 membership genes, revalidated/rendered
`rfbA` and `rffG`, and updated the batch page. No new gene edits were needed
because both genes were already curated in the adjacent nucleotide-sugar work.

Main ppu00525 lesson: the KEGG map is an absence/boundary record. KT2440 has
only shared dTDP-sugar precursor enzymes from this pathway: `rfbA` for
dTDP-glucose formation and `rffG` for dTDP-glucose 4,6-dehydration. This should
not be interpreted as a complete acarbose, validamycin, or aminocyclitol
antibiotic biosynthesis pathway.

Completed the first-pass `ppu00523` /
`polyketide_sugar_unit_biosynthesis_boundary` checkpoint. Created and validated
`modules/polyketide_sugar_unit_biosynthesis_boundary.yaml`, registered the KEGG
mapping, extracted the six KEGG ppu00523 membership genes, fetched five missing
review folders, ran Asta for the five missing gene-level reports, curated all
five new stubs, validated all six batch member reviews and the module, and
rendered all six gene pages. `rmlC` and `rfbD` required accession-based fetching
with Q88R69 and Q88LZ2 because symbol lookup did not resolve them.

Main ppu00523 lessons: the KEGG map is a dTDP-deoxy-sugar/dTDP-rhamnose
boundary, not evidence that KT2440 has a complete polyketide sugar-unit or
natural-product glycosylation pathway. `rfbA` supplies dTDP-glucose, `rffG`
forms the dTDP-4-dehydro-6-deoxyglucose intermediate, `rmlC`/`rfbC` are duplicate
epimerase candidates, and `PP_0500`/`rfbD` are duplicate reductase candidates.
Generic racemase/epimerase parent terms were marked over-annotated on
`rmlC`/`rfbC`, while cytosol, broad polysaccharide, O-antigen, and
nucleotide-sugar process terms were retained as non-core context.

Completed the first-pass `ppu00520` /
`amino_sugar_nucleotide_sugar_metabolism_boundary` checkpoint. Created and
validated `modules/amino_sugar_nucleotide_sugar_metabolism_boundary.yaml`,
registered the KEGG mapping, extracted all 25 KEGG ppu00520 membership genes,
fetched the seven missing review folders, ran Asta for the 11 missing
gene-level reports, curated all seven new stubs, validated all 25 batch member
reviews and the module, and rendered all 25 gene pages. `rfbA` required
accession-based fetching with Q88LZ3 because symbol lookup did not resolve it.

Main ppu00520 lessons: the KEGG map is a composite envelope-precursor boundary.
`glmS`, `glmM`, and `glmU` cover UDP-GlcNAc biosynthesis; `murA` and `murB`
cover the de novo UDP-MurNAc/peptidoglycan precursor branch; `nagZ`, `mupP`,
`anmK`, `amgK`, and `murU` cover peptidoglycan/MurNAc recycling; `rfbA`,
`rffE`, `galE`, `galU`, and `udg` are nucleotide-sugar side branches; and
`algA`, `algD`, `algC`, `cpsG`, `glk`, `pgi1`, `pgi2`, `pgm`, PP_0501, and
PP_1776 are shared carbohydrate or alginate/GDP-mannose context. First-pass
fixes removed the UDP-N-acetylgalactosamine process from `murA`, removed
phosphoglucomutase/phosphomannomutase spillovers from `glmM`, narrowed broad
catalytic/hydrolase terms for `murA`, `rffE`, `nagZ`, and `glmM`, and retained
cofactor/localization terms as non-core.

Completed the first-pass `ppu00500` / `starch_sucrose_metabolism_boundary`
checkpoint. Created and validated
`modules/starch_sucrose_metabolism_boundary.yaml`, registered the KEGG mapping,
extracted all 18 KEGG ppu00500 membership genes, fetched the 10 missing review
folders, ran Asta for those 10 missing gene-level reports, curated all 10 new
stubs, validated all 18 batch member reviews and the module, and rendered all
18 gene pages.

Main ppu00500 lessons: the KEGG map is a bacterial alpha-glucan boundary rather
than plant-like starch/sucrose metabolism. Core glycogen/alpha-glucan and
trehalose/GlgE-route genes are `glgA`, `glgB`, `glgX`, `glgP`, `treY`, `treZ`,
`treSB`, `glgE`, and `malQ`; `bcsA` is cellulose synthesis; `glk`, `pgi1`,
`pgi2`, `pgm`, `galU`, `algC`, and `cpsG` are shared sugar-phosphate or
UDP-glucose precursor context; `bglX` is beta-glucosidase/cellobiose side
context. First-pass fixes changed `glgA` from UDP-glucose-donor to ADP-glucose
glycogen-synthase chemistry, removed GH13 hydrolase over-propagation from
transferase enzymes `glgB` and `glgE`, and kept broad carbohydrate/location/
cofactor terms as non-core.

Completed the first-pass `ppu00330` / `arginine_proline_metabolism` checkpoint.
Created and validated `modules/arginine_proline_metabolism.yaml`, registered the
KEGG mapping, extracted all 39 KEGG ppu00330 membership genes, fetched the 32
missing review folders, ran Asta for those 32 missing gene-level reports,
curated the 31 pending GOA review stubs plus the no-GOA `PP_2932` stub,
validated all 39 batch member reviews and the module, and rendered all 39 gene
pages. The duplicate-safe `ocd__Q88H32` folder was resolved by fetching the
reviewed UniProt `ocd` record and normalizing the generated filenames.

Main ppu00330 lessons: the KEGG map is a broad boundary rather than one linear
pathway. Proline biosynthesis is covered by `proB`, `proA`, `proI`, and the
ornithine cyclodeaminase `ocd__Q88H32`; the Ast arginine-catabolic route is
`astA-I`/`astA-II`, `astB`, boundary `argD`, `astD`, and `astE`; and
agmatine/putrescine/polyamine context is split across `aguA`, `speA`, `speB`,
`speC`, `nspC`, `PP_4523`, and `spuC-II`. First-pass corrections include
modifying `aguA` away from stale `GO:0004668` to agmatine deiminase
`GO:0047632`, removing the diaminopimelate-decarboxylase transfer from `nspC`,
removing biotin-biosynthesis aminotransferase transfers from `spuC-II`, removing
acetolactate/valine/FAD transfers from `aruI`, and keeping `ldcC` as a lysine
decarboxylase boundary rather than a core arginine decarboxylase. OplA/OplB,
Pip, creatinase, opine oxidase, and several generic oxidoreductase or
aminotransferase loci remain useful ppu00330 side-node context.

Full-batch ppu00330 validation has no errors. Remaining warnings are
non-blocking first-pass caveats: Asta-citation notices, broad core functions for
generic oxidoreductase/transaminase candidates whose current GOA lacks an exact
MF row, `PP_2932` having no GOA/core function, and an inherited `PP_4983`
process-reflection warning. Falcon module-level synthesis remains queued for
`arginine_proline_metabolism` / `ppu00330` while Edison Falcon access is
returning HTTP 402 in the current session.

Completed the boundary/absence `ppu00332` / `carbapenem_biosynthesis_boundary`
checkpoint. Created and validated `modules/carbapenem_biosynthesis_boundary.yaml`,
registered the KEGG mapping, extracted the two-member batch, revalidated and
rendered `proB` and `proA`, and recorded the pathway as shared proline-precursor
chemistry rather than evidence for a carbapenem biosynthesis module in KT2440.
Falcon module-level synthesis remains queued for `carbapenem_biosynthesis_boundary`
/ `ppu00332` while Edison Falcon access is returning HTTP 402.

Completed the first-pass `ppu00350` / `tyrosine_catabolism` checkpoint. Updated
the existing `modules/tyrosine_catabolism.yaml` from a human/hepatic framing to
a species-neutral homogentisate-pathway module that can also cover PSEPK,
registered the KEGG mapping, extracted all 16 KEGG ppu00350 membership genes,
fetched the five missing review folders, ran Asta for the six genes lacking
Asta reports, curated all five pending stubs, validated the full 16-gene batch
and the module, and rendered all 16 gene pages.

Main ppu00350 lessons: the strict tyrosine/phenylalanine homogentisate route is
covered by the existing aromatic aminotransferases plus `hpd`, `hmgA`, `hmgC`,
and `hmgB`. `hmgC` now has an added `NEW` tyrosine-catabolism process
recommendation to mirror its phenylalanine/homogentisate role. `PP_1709` is
kept as a FAH-family acetylpyruvate-hydrolase candidate and not used as the
fumarylacetoacetase step because `hmgB` already carries that role. `PP_2552`,
`peaE`, aldehyde dehydrogenases, and `PP_4983` remain ppu00350 boundary or
side-node context rather than committed homogentisate-pathway members. Falcon
module-level synthesis remains queued for `tyrosine_catabolism` / `ppu00350`
while Edison Falcon access is returning HTTP 402.

Completed the first-pass `ppu00360` / `phenylalanine_metabolism` checkpoint.
Created and validated `modules/phenylalanine_metabolism.yaml`, registered the
KEGG mapping, extracted all 28 KEGG ppu00360 membership genes, fetched the 13
missing review folders, ran Asta for the 14 genes lacking Asta at batch start,
curated the 12 pending GOA stubs plus the no-GOA `paaD` stub, validated all 28
batch member reviews and the module, and rendered all 28 gene pages.

Main ppu00360 lessons: the strict PSEPK phenylalanine/phenylacetate content is
split between PhhA/homogentisate-route entry and the Paa phenylacetate
degradation operon. The Paa activation/epoxidation/lower-pathway set is `paaK`,
`paaA`, `paaB`, `paaC`, `paaD`, `paaE`, `paaG`, `paaZ`, `paaH`, `paaF`, and
`paaI`. First-pass corrections include adding missing `NEW`
phenylacetate-catabolism process recommendations for `paaZ`, `paaD`, `paaB`,
and `paaI`, narrowing broad `paaG` catalytic activity to isomerase-class
activity, and treating `paaZ` as a bifunctional enzyme where GO currently only
captures a broad aldehyde/oxo oxidoreductase class. `PP_3726` remains an
unresolved enoyl-CoA hydratase/isomerase-family boundary gene with no core
function assigned. `dadA1`, `dadA2`, and `PP_4311` are D-amino-acid
dehydrogenase side nodes, not committed phenylalanine catabolic steps. Falcon
module-level synthesis remains queued for `phenylalanine_metabolism` /
`ppu00360` while Edison Falcon access is returning HTTP 402.

Completed the boundary `ppu00361` /
`chlorocyclohexane_chlorobenzene_degradation_boundary` checkpoint. Created and
validated `modules/chlorocyclohexane_chlorobenzene_degradation_boundary.yaml`,
registered the KEGG mapping, extracted the three-member batch, revalidated and
rendered `catA-II`, `catA`/catA-I, and `catB`, and recorded this KEGG map as
catechol ortho-cleavage/beta-ketoadipate lower-pathway context rather than
evidence for a complete chlorinated-aromatic upper pathway in KT2440.

Main ppu00361 lessons: the PSEPK KEGG membership is only the CatA/CatB lower
branch. `catA` and `catA-II` satisfy catechol 1,2-dioxygenase activity, and
`catB` satisfies muconate cycloisomerase activity. The existing `catB` review
already rejects the chloromuconate cycloisomerase over-transfer, which is the
critical curation point for this bucket. Real generic module and taxon-aware
module/pathway Falcon commands were attempted on 2026-07-09 PDT / 2026-07-10
UTC and failed before report generation with Edison HTTP 402, so the Falcon
report paths remain queued rerun targets.

Completed the boundary `ppu00380` / `tryptophan_metabolism_boundary` checkpoint.
Created and validated `modules/tryptophan_metabolism_boundary.yaml`, registered
the KEGG mapping, extracted all 20 KEGG ppu00380 membership genes, fetched the
two missing review folders (`katE`, `PP_2887`), ran Asta for `katE`,
`PP_2887`, and the previously curated `katA`, curated the two new
catalase-family stubs, validated the full 20-gene batch and the module, and
rendered all 20 gene pages.

Main ppu00380 lessons: the PSEPK KEGG map is a broad boundary bucket, not a
satisfiable dedicated tryptophan pathway in the first-pass curation. The primary
partition genes are `gcdH` and `katG`, whose core functions are glutaryl-CoA
dehydrogenase activity and catalase-peroxidase peroxide detoxification,
respectively. `katE` is curated as a monofunctional catalase. `PP_2887` is
curated more cautiously as a catalase-related peroxidase: the catalase activity
transfer is modified to `GO:0004601` peroxidase activity, and hydrogen peroxide
catabolism is narrowed to cellular oxidant detoxification pending substrate
assays. Remaining members are CoA-metabolism, lipoamide, beta-oxidation,
aromatic-amino-acid, or unresolved amidase side nodes. Falcon module-level
synthesis remains queued for `tryptophan_metabolism_boundary` / `ppu00380` while
Edison Falcon access is returning HTTP 402.

Completed the boundary/absence `ppu00401` / `novobiocin_biosynthesis_boundary`
checkpoint. Created and validated `modules/novobiocin_biosynthesis_boundary.yaml`,
registered the KEGG mapping, extracted the four-member batch, revalidated and
rendered `hisC`, `aroA`, `tyrB`, and `amaC`, and recorded the KEGG map as shared
histidine, shikimate/chorismate, and aromatic-amino-acid metabolism rather than
evidence for a complete novobiocin aminocoumarin antibiotic biosynthesis module
in KT2440.

Main ppu00401 lessons: every KT2440 member is already assigned a non-novobiocin
core function. `hisC` is histidinol-phosphate aminotransferase in histidine
biosynthesis, `aroA` is the fused EPSP synthase / TyrA-like prephenate
dehydrogenase supporting chorismate and tyrosine biosynthesis, and `tyrB` plus
`amaC` are PLP-dependent aromatic amino acid aminotransferases. The batch
validates without errors; only `tyrB` and `amaC` retain non-blocking
Asta-citation warnings. Falcon module-level synthesis remains queued for
`novobiocin_biosynthesis_boundary` / `ppu00401` while Edison Falcon access is
returning HTTP 402.

Completed the broad boundary `ppu00410` / `beta_alanine_metabolism_boundary`
checkpoint. Created and validated `modules/beta_alanine_metabolism_boundary.yaml`,
registered the KEGG mapping, extracted all 15 KEGG ppu00410 membership genes,
revalidated and rendered all 15 already curated/Asta-backed reviews, and recorded
the map as beta-alanine-associated chemistry plus several side-node inclusions
rather than one narrow linear route.

Main ppu00410 lessons: the most beta-alanine-relevant spine is reductive
pyrimidine catabolism and related beta-alanine release/context (`pydX`, `pydA`,
`pydB`, `PP_0614`, `hyuC`), beta-alanine/omega-amino-acid transamination
(`PP_0596`), and beta-alanine-consuming pantothenate ligation (`panC`). The
remaining ppu00410 members are boundary nodes: `mmsA-I`/`mmsA-II` are
methylmalonate-semialdehyde dehydrogenases tied to valine/thymine/propanoate
context, `patD` and `prr` are aminobutyraldehyde/polyamine-side aldehyde
dehydrogenases, and `acd`, `fadB`, `PP_2217`, and `paaF` belong with acyl-CoA,
fatty-acid beta-oxidation, or phenylacetate chemistry. The batch validates
without errors; remaining warnings are non-blocking Asta-citation notices on
older first-pass reviews. Falcon module-level synthesis remains queued for
`beta_alanine_metabolism_boundary` / `ppu00410` while Edison Falcon access is
returning HTTP 402.

Completed the `ppu00430` / `taurine_hypotaurine_metabolism_boundary` checkpoint.
Created and validated `modules/taurine_hypotaurine_metabolism_boundary.yaml`,
registered the KEGG mapping, extracted the five-member batch, fetched the three
missing review folders (`tauD`, `PP_3535`, `ggt`), ran Asta for `tauD`, `pta`,
`PP_3535`, and `ggt`, curated the three new stubs, validated all five gene
reviews and the module, and rendered all five gene pages.

Main ppu00430 lessons: TauD/AtsK is the pathway-defining enzyme, with direct
KT2440 support for alpha-ketoglutarate-dependent taurine dioxygenase activity
and sulfur compound catabolism. The other KEGG ppu00430 members are boundary
context: `pta` is phosphate acetyltransferase for acetate/acetyl-CoA metabolism,
`gdhB` is NAD-specific glutamate dehydrogenase linking glutamate and
2-oxoglutarate metabolism, and `PP_3535` plus `ggt` are
gamma-glutamyltransferase-family glutathione hydrolases. The batch validates
without errors; remaining warnings are non-blocking Asta-citation notices on
older first-pass reviews and the newly curated TauD/GGT-family stubs. Falcon
module-level synthesis remains queued for
`taurine_hypotaurine_metabolism_boundary` / `ppu00430` while Edison Falcon access
is returning HTTP 402.

Completed the `ppu00440` / `phosphonate_phosphinate_metabolism` checkpoint.
Created and validated `modules/phosphonate_phosphinate_metabolism.yaml`,
registered the KEGG mapping, extracted the two-member batch, fetched `phnX`, ran
Asta for `phnX` and `phnW`, curated the new `phnX` stub, validated both gene
reviews and the module, and rendered both gene pages.

Main ppu00440 lessons: this KT2440 map is a compact PhnWX
2-aminoethylphosphonate catabolic route. `phnW` catalyzes the PLP-dependent
AEP:pyruvate transamination step that produces phosphonoacetaldehyde, and
`phnX` hydrolyzes phosphonoacetaldehyde to acetaldehyde and phosphate. The
`phnX` TreeGrafter DNA repair process annotation is unsupported and was removed;
the phosphoglycolate phosphatase activity transfer was modified to the
PhnX-specific phosphonoacetaldehyde hydrolase activity. The batch validates
without errors. Falcon module-level synthesis remains queued for
`phosphonate_phosphinate_metabolism` / `ppu00440` while Edison Falcon access is
returning HTTP 402.

Completed the `ppu00450` / `selenocompound_metabolism_boundary` checkpoint.
Created and validated `modules/selenocompound_metabolism_boundary.yaml`,
registered the KEGG mapping, extracted the 12-member batch, fetched missing
folders for `selA`, `selD`, and `metG`, ran Asta for those three genes, curated
their initialized stubs, validated all 12 gene reviews and the module, and
rendered all 12 gene pages.

Main ppu00450 lessons: the selenium-specific route in KT2440 is the SelD/SelA
Sec-tRNA biosynthesis spine. `selD` synthesizes selenophosphate from selenide
and ATP, and `selA` uses selenophosphate to convert L-seryl-tRNA(Sec) to
L-selenocysteinyl-tRNA(Sec). `metG` remains canonical methionyl-tRNA
synthetase; `cysD`, `cysNC`, `metB`, `mdeA`, `metH`, `metE`, `PP_4348`,
`PP_4594`, and `PP_4637` are sulfur, methionine, sulfate-assimilation,
translation, or candidate side nodes rather than evidence for a broad dedicated
selenocompound pathway. The batch validates without errors; remaining warnings
are non-blocking older side-node warnings. Falcon module-level synthesis remains
queued for `selenocompound_metabolism_boundary` / `ppu00450` while Edison Falcon
access is returning HTTP 402.

Completed the `ppu00460` / `cyanoamino_acid_metabolism_boundary` checkpoint.
Created and validated `modules/cyanoamino_acid_metabolism_boundary.yaml`,
registered the KEGG mapping, extracted the seven-member batch, fetched and ran
Asta for the only missing member (`bglX`), curated its initialized stub,
validated all seven gene reviews and the module, and rendered all seven gene
pages.

Main ppu00460 lessons: this is a boundary map in KT2440. `ansA` and `PP_1160`
are the asparaginase-family primary bucket genes, but the first pass does not
support a complete cyanogenic-glycoside or cyanoamino-acid detoxification route.
`glyA1` and `glyA2` are SHMT one-carbon side context, `bglX` is a periplasmic
beta-glucosidase/glucan-catabolism side node, and `PP_3535` plus `ggt` are
glutathione hydrolase side nodes overlapping taurine/glutathione metabolism. The
batch validates without errors; remaining warnings are non-blocking older
side-node warnings. Falcon module-level synthesis remains queued for
`cyanoamino_acid_metabolism_boundary` / `ppu00460` while Edison Falcon access is
returning HTTP 402.

Completed the `ppu00470` / `d_amino_acid_metabolism_boundary` checkpoint.
Created and validated `modules/d_amino_acid_metabolism_boundary.yaml`,
registered the KEGG mapping, extracted the 21-member batch, fetched and ran
Asta for the nine missing initialized members plus `proR`, curated the nine new
stubs, validated all 21 gene reviews and the module, and rendered all 21 gene
pages.

Main ppu00470 lessons: this is a broad boundary map rather than one linear
D-amino-acid catabolic route. `murI`, `murD`, `ddlA`, `ddlB`, `dadX`, and `alr`
cover peptidoglycan D-Glu/D-Ala supply and alanine racemase chemistry; `dadA1`,
`dadA2`, `PP_4311`, and `dauA` are D-amino-acid/D-arginine
dehydrogenase-context enzymes; `proR`, `PP_1255`, `PP_1257`, `PP_1256`,
`PP_2585`, and `PP_3602` are hydroxyproline/dioxovalerate side-route nodes; and
`dapF__Q88GD4`, `dapF__Q88CF3`, `lysA-I`, `lysA-II`, and `ansB` are diaminopimelate/lysine
biosynthesis or asparaginase side context. The batch validates without errors;
remaining warnings are non-blocking older Asta-citation warnings on carried
forward side-node reviews. Falcon module-level synthesis remains queued for
`d_amino_acid_metabolism_boundary` / `ppu00470` while Edison Falcon access is
returning HTTP 402.

Completed the `ppu00480` / `glutathione_metabolism_boundary` checkpoint.
Created and validated `modules/glutathione_metabolism_boundary.yaml`, registered
the KEGG mapping, extracted the 31-member batch, fetched the 20 missing review
folders, ran Asta for those 20 missing gene-level reports, curated the 20 new
stubs, regenerated the worklist and batch docs, validated all 31 gene reviews
and the module, and rendered all 31 gene pages.

Main ppu00480 lessons: this is a broad glutathione boundary map rather than a
single route. The strict glutathione core is split across `gshA`, `gshB`,
PP_3253, `gor`, `PP_3535`, `ggt`, and PP_5211, with `pxpA1`/`pxpA2` as
5-oxoproline salvage subunits. GST and peroxide-detoxification context is
separate: PP_0183, `gstA`, PP_1347, PP_1821, `gstB`, PP_2474, PP_2536,
PP_0777, PP_1686, `gpx`, and PP_2700. `zwfA`, `zwfB`, `zwf`, `gntZ`, `icd`,
and `idh` are NADPH-supply side context; `pepA` and `pepN` are aminopeptidase
side nodes; `speC`, `ptxD`, and `ybgJ` are non-glutathione spillovers. First-pass
fixes removed carbohydrate-metabolism spillover from `pxpA1`/`pxpA2`, narrowed
generic catalytic/ligase terms for `gshB` and PP_3253, treated PP_2700 as
glutathione-dependent peroxidase chemistry rather than accepting the
thioredoxin-specific automated wording, and kept cofactor/location rows
non-core. Falcon module-level synthesis remains queued for
`glutathione_metabolism_boundary` / `ppu00480` while Edison Falcon access is
returning HTTP 402.

Completed the first-pass `ppu00310` / `lysine_degradation` checkpoint. Created
and validated `modules/lysine_degradation.yaml`, registered the KEGG mapping,
extracted all 32 KEGG ppu00310 membership genes, fetched the 11 missing review
folders, ran Asta for the 14 genes that lacked Asta at batch start, curated the
11 new stubs, validated all 32 resolved candidate review folders and the module,
and rendered all 32 gene pages.

Main ppu00310 lessons: the strict L-lysine-to-glutarate Dav route is davB,
davA, davT, and davD. GlaH/CsiD and LhgO are the CoA-independent
glutarate/L-2-hydroxyglutarate branch. PP_4108, hglS, ydiJ, amaD, amaA, amaB,
dpkA, and alr are D-lysine, 2-aminoadipate, D-2-hydroxyglutarate, and
pipecolate side-route context. PP_0159 remains unresolved CoA-transferase /
glutarate boundary context. PatD, Prr, GabD-II, Sad-I, beta-oxidation enzymes,
thiolases, and lipoamide enzymes are cross-bucket aldehyde, GABA,
beta-oxidation, or central-carbon spillovers unless future evidence supports a
committed lysine-catabolic role.

Full-batch ppu00310 validation has no errors. The remaining warnings are 16
pre-existing Asta-citation notices on older boundary reviews, not on the 11
newly curated reviews. Falcon module-level synthesis remains queued for
`lysine_degradation` / `ppu00310` while Edison Falcon access is returning HTTP
402 in the current session.

Completed the first-pass `ppu00300` / `lysine_biosynthesis` checkpoint.
Created and validated `modules/lysine_biosynthesis.yaml`, registered the KEGG
mapping, extracted all 19 KEGG ppu00300 membership genes, fetched the nine
missing review folders, ran Asta for those nine, curated the new stubs,
validated all 19 resolved candidate review folders and the module, and rendered
all 19 gene pages.

Main ppu00300 lessons: strict bacterial L-lysine biosynthesis is the
diaminopimelate route through shared aspartate-family precursor supply,
DapA/DapB, the DapD/DapC/DapE succinylated branch, DapF epimerase, and LysA
decarboxylase. The KEGG map also pulls in peptidoglycan ligases (`murE`,
`murF`), homoserine-branch enzymes (`hom`, PP_0664), upstream aspartate
transamination (`aspC`), and arginine/ornithine aminotransferase context
(`aruC`). `dapE` exposed a family-over-propagation issue: remove the
arginine-biosynthesis transfer and modify acetylornithine deacetylase to
succinyl-diaminopimelate desuccinylase activity. Use current `GO:0009085` for
authored L-lysine biosynthesis terms; older `GO:0009089` and `GO:0019877` are
obsolete.

Falcon module-level synthesis remains queued for `lysine_biosynthesis` /
`ppu00300` while Edison Falcon access is returning HTTP 402 in the current
session.

Completed the first-pass `ppu00290` /
`branched_chain_amino_acid_biosynthesis` checkpoint. Created and validated
`modules/branched_chain_amino_acid_biosynthesis.yaml`, registered the KEGG
mapping, extracted all 18 KEGG ppu00290 membership genes, fetched the four
missing leucine-branch review folders, ran Asta for those four, curated the new
stubs, refreshed authored obsolete `GO:0009097` L-isoleucine biosynthesis usage
to `GO:1901705` in older side reviews, validated all 18 candidate gene reviews
and the module, and rendered all 18 gene pages.

Main ppu00290 lessons: strict BCAA biosynthesis is centered on AHAS
(`ilvI`/`ilvH`, with PP_1157/PP_1394 as side AHAS-like candidates), `ilvC`,
`ilvD`, `ilvE`, and the leucine branch `leuA`/`leuC`/`leuD`/`leuB`. The KEGG
map also pulls in threonine-dehydratase paralogs (`ilvA-I`, `ilvA-II`,
PP_3191, PP_4430), serine ammonia-lyase (`PP_2930`), alanine aminotransferase
(`alaA`), and leucine dehydrogenase (`ldh`) as precursor, catabolic, or
boundary context rather than all as strict committed BCAA biosynthesis steps.
Full-batch validation warnings are limited to pre-existing Asta-citation
warnings on older reviews; the new leucine-branch reviews validate cleanly.

Falcon module-level synthesis remains queued for
`branched_chain_amino_acid_biosynthesis` / `ppu00290` while Edison Falcon access
is returning HTTP 402 in the current session.

Completed the first-pass `ppu00280` /
`branched_chain_amino_acid_degradation` checkpoint. Created and validated
`modules/branched_chain_amino_acid_degradation.yaml`, registered the KEGG
mapping, extracted all 35 KEGG ppu00280 membership genes, fetched the 17 missing
review folders, ran Asta for those 17, curated the new stubs, validated all 35
candidate gene reviews and the module, and rendered all 35 gene pages.

Main ppu00280 lessons: the strict BCAA degradation center is the
`ivd`/`mccA`/`mccB`/`liuC` leucine branch, the
`mmsB`/`mmsA-I`/`mmsA-II` valine branch, and the
`bkdAA`/`bkdAB`/`bkdB` BCKDH complex context. KEGG also pulls in many boundary
nodes: beta-alanine transamination (`PP_0596`), acetoacetate/acyl-CoA endpoint
handling (`aacs`), beta-ketoadipate CoA-transferases (`atoA`/`atoB`), fatty-acid
beta-oxidation paralogs, generic thiolases, and lipoamide E3 paralogs. Those
remain boundary context unless gene-level evidence supports a committed BCAA
role. Added conservative `NEW` rows for missing complex/process terms in
`liuC`, `mccA`, `bkdAA`, `bkdAB`, and `bkdB`; corrected `ldh` from a fetched
glutamate dehydrogenase activity to L-leucine dehydrogenase activity.

Falcon module-level synthesis remains queued for
`branched_chain_amino_acid_degradation` / `ppu00280` while Edison Falcon access
is returning HTTP 402 in the current session.

Completed the first-pass `ppu00261` / `monobactam_biosynthesis_boundary`
checkpoint. Created and validated
`modules/monobactam_biosynthesis_boundary.yaml`, registered the KEGG mapping,
extracted all 9 KEGG ppu00261 membership genes, fetched the five missing review
folders, ran Asta for those five, curated the five new stubs so the full batch
has no remaining `PENDING` actions, validated all 9 gene reviews and the module,
and rendered all 9 gene pages.

Main ppu00261 lessons: the KEGG "Monobactam biosynthesis" bucket is mostly a
boundary/absence case for KT2440. The Dap/aspartate-family genes are
L-lysine/diaminopimelate precursor biology, `cysD`/`cysNC` are sulfate
activation side nodes, and `PP_3808` is best treated as MbtH-like
siderophore/NRPS context. None of these should be promoted to monobactam or
generic antibiotic biosynthesis without pathway-specific evidence. The two
collision-safe `dapA` review names also exposed a fetch workflow detail: use the
underlying CLI with `--uniprot-id` and `--alias` rather than passing
`dapA__Q88NH2` or `dapA__Q88JL0` directly to `just fetch-gene`.

Falcon module-level synthesis remains queued for
`monobactam_biosynthesis_boundary` / `ppu00261` while Edison Falcon access is
returning HTTP 402 in the current session.

Completed the first-pass `ppu00260` /
`glycine_serine_threonine_metabolism` checkpoint. Created and validated
`modules/glycine_serine_threonine_metabolism.yaml`, added the KEGG mapping to
the worklist, extracted all 66 KEGG ppu00260 membership genes (16 primary bucket
genes plus 50 cross-bucket side nodes), fetched the 28 missing review folders,
ran Asta for those 28 plus existing curated `pvdH`, curated the 27 pending
review YAMLs plus annotation-empty `PP_4432`, validated all 66 gene reviews, and
rendered all 66 gene pages.

Falcon module-level synthesis remains queued for
`glycine_serine_threonine_metabolism` / `ppu00260`: no generic module or
PSEPK-specific module+pathway Falcon report was generated for this checkpoint
while Edison Falcon access is returning HTTP 402 in the current session.

Main ppu00260 lessons: this KEGG map combines the real serine-family amino-acid
hub with many substrate-sharing side pathways. The strict center covers serine
biosynthesis, homoserine/threonine biosynthesis, serine-glycine one-carbon
chemistry, glycine cleavage, threonine aldolase, and methylated-glycine/betaine
catabolism. First-pass corrections included treating the `dgcA/dgcB` and
`gbcA/gbcB` pairs as predicted multicomponent dimethylglycine/glycine-betaine
oxidation systems, representing `soxB/soxD/soxA/soxG` as sarcosine oxidase
subunits contributing to the complex activity, adding provisional `NEW`
activity annotations for sparse `PP_4421` and annotation-empty `PP_4432`, and
keeping phospholipid (`pcs`, `pssA`, `PP_4677`), pyoverdine/diaminobutyrate
(`pvdH`, `PP_2800`), creatine (`creA`), and threonine-dehydratase paralog nodes
as boundary context rather than strict glycine/serine/threonine core steps.

Completed the first-pass `ppu00250` /
`alanine_aspartate_glutamate_metabolism` checkpoint. Created and validated
`modules/alanine_aspartate_glutamate_metabolism.yaml`, added the KEGG mapping to
the worklist, extracted all 36 KEGG ppu00250 membership genes (8 primary bucket
genes plus 28 cross-bucket side nodes), fetched the 9 missing review folders,
ran Asta for those 9 missing gene-level reports, curated the 9 newly fetched
review YAMLs so all 36 batch members now have no `PENDING` actions, validated
the module and all 36 gene reviews, and rendered all 36 gene pages.

Falcon module-level synthesis remains queued for
`alanine_aspartate_glutamate_metabolism` / `ppu00250`: no generic module or
PSEPK-specific module+pathway Falcon report was generated for this checkpoint
while Edison Falcon access is returning HTTP 402 in the current session.

Main ppu00250 lessons: the KEGG alanine/aspartate/glutamate map is a hub map.
The direct hub includes alanine transamination, glutamate/glutamine nitrogen
assimilation, aspartate/asparagine reactions, and omega-amidase context. The
membership set also contains many real donor/acceptor side nodes from arginine,
purine, pyrimidine, NAD, amino-sugar, proline/polyamine, lysine-catabolism, and
biotin pathways. First-pass corrections included modifying `davT` GABA
aminotransferase transfer to 5-aminovalerate aminotransferase, removing the
`putA` L-proline biosynthesis transfer, treating `PP_2799` as BioA-like biotin
aminotransferase context, and marking broad AspA/GlmS parent-process transfers
as over-annotations.

Completed the first-pass `ppu00240` / `pyrimidine_metabolism` checkpoint.
Created and validated `modules/pyrimidine_metabolism.yaml`, added the KEGG
mapping to the worklist, extracted all 36 KEGG ppu00240 membership genes (24
primary pyrimidine bucket genes plus 12 cross-bucket side nodes), fetched the 18
missing review folders, and ran Asta for the 19 genes missing gene-level
retrieval reports. Curated the 18 pending or annotation-empty review YAMLs so
all 36 batch members now have no `PENDING` actions, validated the module and all
36 gene reviews, and rendered all 36 gene pages.

Falcon module-level synthesis remains queued for `pyrimidine_metabolism` /
`ppu00240`: no generic module or PSEPK-specific module+pathway Falcon report was
generated for this checkpoint while Edison Falcon access is returning HTTP 402
in the current session.

Main ppu00240 lessons: the KEGG pyrimidine map is another broad nucleotide
bucket, not a single satisfiable linear pathway. The strict de novo UMP route is
CarAB precursor supply plus PyrB, PyrC, PyrD, PyrE, and PyrF. Downstream
pyrimidine-pool chemistry splits into UMP/UDP/UTP/CTP generation, the
ribonucleotide-reduction and dTMP branch, salvage/recycling, and reductive
pyrimidine catabolism. `pyrC'` remains unresolved because existing evidence
mixes dihydroorotase/pyrimidine-biosynthesis and allantoinase/purine-catabolism
interpretations. The apostrophe in `pyrC'` also exposed a tooling edge: direct
CLI fetch/render commands are safer than the `just` recipes for symbols that
contain shell metacharacters.

Completed the first-pass `ppu00230` / `purine_metabolism` checkpoint. Created
and validated `modules/purine_metabolism.yaml`, added the KEGG mapping to the
worklist, extracted all 65 KEGG ppu00230 membership genes (36 primary purine
bucket genes plus 29 cross-bucket side nodes), fetched the 44 missing review
folders, and ran Asta for the 47 genes missing gene-level retrieval reports.
`pde` failed once with a transient Asta internal-server error and succeeded on
the single retry. Curated the 44 pending review YAMLs so all 65 batch members
now have no `PENDING` actions, validated the module and all 65 gene reviews,
and rendered all 65 gene pages.

Falcon module-level synthesis remains queued for `purine_metabolism` /
`ppu00230`: no generic module or PSEPK-specific module+pathway Falcon report was
generated for this checkpoint while Edison Falcon access is returning HTTP 402
in the current session.

Main ppu00230 lessons: the KEGG purine map is a broad nucleotide-metabolism
bucket, not one linear pathway. The strict purine core spans PRPP/de novo IMP
formation and branches to AMP/GMP via PurF, PurD, PurN/PurT, PurL, PurM,
PurK/PurE, PurC, PurB, PurH, PurA, GuaB, and GuaA. Salvage and nucleotide-pool
maintenance are represented by Apt, PP_0747, Xpt, Amn/PP_3662, PpnP, YfiH,
Ndk, Gmk, PP_5100, Dgt, ApaH, NudE/NudF, Ppx, CyaA, RelA, and SpoT. Purine
catabolism is represented by PP_0591, GuaD, XdhA/XdhB, PucM, PucL, PuuE,
AllE, and AllA, while PaoABC remains boundary xanthine/aldehyde-oxidoreductase
context. Cross-bucket spillovers include ribonucleotide reductase, sulfate
adenylyltransferase, urease/carbamate, nucleotide-sugar, and cyclic-nucleotide
side nodes. First-pass corrections removed unsupported electronic transfers
such as `purC` cobalamin biosynthesis, `purM` PurD/GAR-synthetase activity,
`puuE` carbohydrate metabolism, and `yrfG` DNA repair/phosphoglycolate
phosphatase.

Completed the first-pass `ppu00220` / `arginine_biosynthesis` checkpoint. Created
and validated `modules/arginine_biosynthesis.yaml`, added a reproducible
`--extra-gene` option to the batch extractor, extracted 31 KEGG membership genes
plus UniPathway-supported `argD`, fetched the 20 missing review folders, ran
Asta for all missing gene-level reports, curated the 20 pending review YAMLs so
all 32 batch members now have no `PENDING` actions, validated the module and all
32 gene reviews, and rendered all 32 gene pages.

Falcon module-level synthesis remains queued for `arginine_biosynthesis` /
`ppu00220`: no generic module or PSEPK-specific module+pathway Falcon report was
generated for this checkpoint while Edison Falcon access is returning HTTP 402
in the current session.

Main ppu00220 lessons: the strict acetylated bacterial arginine route is covered
by CarAB carbamoyl-phosphate supply, ArgA/ArgJ acetylglutamate formation, ArgB,
ArgC1/ArgC2, UniPathway-promoted ArgD, ArgE/PP_3571/ArgJ ornithine formation,
ArgF, ArgG, and ArgH. `argD` is the key module-gap gene because it is
UniPathway UPA00068-supported but partitioned under `ppu00330`. The KEGG map also
pulls in arginine-deiminase/carbamate chemistry (`arcA`, `arcB`, `arcC`),
urease (`ureA`, `ureB`, `ureC`), glutamate/glutamine nitrogen assimilation, and
polyamine GS-fold side nodes; these are curated as real functions or boundary
context rather than strict arginine-biosynthesis steps. `arcB` now carries a
new L-arginine catabolic process suggestion and removes the electronic
L-arginine biosynthesis transfer from the strict module interpretation.

Completed the first-pass `ppu00190` / `oxphos` checkpoint. Reused and validated
the existing species-neutral `modules/oxphos.yaml`, completed generic Falcon
module research in `modules/oxphos-deep-research-falcon.md`, fetched the 49
missing review folders, ran Asta for the remaining gene-level reports, curated
all 54 KEGG membership reviews to `DRAFT` with no `PENDING` actions, validated
the module and all 54 gene reviews, and rendered all 54 gene pages.

The taxon-aware Falcon module+pathway call for `oxphos` / `ppu00190` / PSEPK did
not produce a report: Edison returned HTTP 402 Payment Required before research
started. The batch is therefore recorded as a local/UniProt/Asta plus generic
module-Falcon first pass, with the PSEPK-specific Falcon synthesis left queued
for a later provider rerun.

Main ppu00190 lessons: KT2440 has a broad aerobic respiratory-chain repertoire,
including proton-pumping Complex I (`nuoA`-`nuoN`), type-II NADH dehydrogenase
`ndh`, succinate dehydrogenase, cytochrome bc1 (`petA`/`petB`/`petC`), aa3,
bo3, duplicated cbb3, and cyanide-insensitive terminal oxidase branches plus
the F1Fo ATP synthase operon. The first pass corrected donor-specific terminal
oxidase semantics by modifying bo3 subunit annotations from generic
cytochrome-c oxidase activity to cytochrome bo3 ubiquinol oxidase activity, and
used `contributes_to_molecular_function` in core functions for respiratory and
ATP synthase complex subunits. KEGG ppu00190 also pulls in heme-biogenesis,
polyphosphate, pyrophosphatase, and other boundary nodes that should not be
treated as strict OXPHOS catalytic steps without pathway-specific evidence.

Completed the first-pass `ppu00790` / `folate_biosynthesis` checkpoint. Created
and validated `modules/folate_biosynthesis.yaml`, fetched all 32 KEGG membership
review folders including duplicate-symbol `folE2__Q88JY1`, ran Asta for all
missing gene-level reports, curated the 25 pending review YAMLs so all 32 batch
members now have no `PENDING` actions, validated the module and all 32 gene
reviews, and rendered all 32 gene pages.

Both Falcon calls for `folate_biosynthesis` failed before report generation with
Edison HTTP 402 Payment Required: the generic module report
`modules/folate_biosynthesis-deep-research-falcon.md` and the taxon-aware report
`projects/P_PUTIDA/deep-research/PSEPK__folate_biosynthesis__ppu00790-deep-research-falcon.md`
remain queued for a later provider rerun.

Main ppu00790 lessons: the strict folate route is covered by GTP cyclohydrolase
I/FolE paralogs (`folE1`, `folE2__Q88JY1`, and existing `folE2`/Q88HM9),
FolB, HPPK candidates (`folK` and PP_0393), the pABA branch (`pabB`, `pabC`),
FolP, FolC, and FolA. KEGG ppu00790 also pulls in queuosine (`queD/E/C/F`),
molybdenum-cofactor (`moaA/B/C/E`, `moeA`, `mobA`, PP_1969, PP_2482), BH4/
phenylalanine-hydroxylase (`phhA`, `phhB`), riboflavin (`ribA`, `ribAB-I/II`),
and MobA-like side nodes. PP_2483 and PP_4230 remain unresolved MobA-like
nucleotidyltransferase-domain proteins with no core substrate/function assigned;
`pabB` now removes the stray electronic tryptophan-biosynthesis transfer in
favor of the pABA/folate role.

Completed the first-pass `UPA00392` /
`queuosine_biosynthesis_boundary` checkpoint. Created and validated
`modules/queuosine_biosynthesis_boundary.yaml`, fetched missing primary
UniPathway genes `queA`, `tgt`, and `queG`, ran Asta for those genes, reused and
cleaned the existing `queF` review as side context from `ppu00790`, curated all
four UPA00392 batch reviews, and validated the module plus all four gene
reviews, then rendered the four gene pages and the module/project pages.

Both Falcon calls for `queuosine_biosynthesis_boundary` failed before report
generation with Edison HTTP 402 Payment Required: the generic module report
`modules/queuosine_biosynthesis_boundary-deep-research-falcon.md` and the
taxon-aware report
`projects/P_PUTIDA/deep-research/PSEPK__queuosine_biosynthesis_boundary__upa00392-deep-research-falcon.md`
remain queued for a later provider rerun.

Main UPA00392 lessons: the satisfiable KT2440 tRNA-queuosine route is
`queF` preQ1 synthesis, `tgt` preQ1 insertion at tRNA wobble position 34, `queA`
epoxyqueuosine formation, and `queG` epoxyqueuosine reduction. `queF` is best
modeled as deazaguanine/preQ1 precursor supply rather than a strict folate
enzyme, and QueG iron-sulfur/cobalamin information is cofactor context rather
than a separate pathway step.

Completed the first-pass `ppu00670` / `one_carbon_by_folate` checkpoint. Created
and validated `modules/one_carbon_by_folate.yaml`, fetched all 31 KEGG membership
review folders, ran Asta for all missing gene-level reports, curated the 22
pending review YAMLs so all 31 batch members now have no `PENDING` actions, and
validated the module plus all 31 gene reviews, then rendered all 31 gene pages.

Falcon module-level synthesis remains queued for `one_carbon_by_folate`: no
generic module or PSEPK-specific module+pathway Falcon report was generated for
this checkpoint while Edison Falcon access is returning HTTP 402 in the current
session.

Main ppu00670 lessons: the strict folate one-carbon carrier chemistry is covered
by `folD1`, `folD2`, `metF`, PP_4638, and `fau`; folate-dependent consumers are
represented by `purN`, `purH`, `thyA`, `metH`, `folA`, and `folM`; and glycine
cleavage provides C1 input through the two GCV clusters (`gcvT-I`/`gcvP1`/`gcvH1`
and `gcvT`/`gcvP2`/`gcvH2`). `purU-I`, `purU-II`, and `purU-III` are retained as
formyl-tetrahydrofolate hydrolase paralogs but their direct purine-biosynthesis
process annotations are marked as over-annotated. `betA`, `betB`, PP_0708,
`lpd`/`lpdG`/`lpdV`, `metK`, `ahcY`, and PP_4594 are boundary nodes. PP_0708 is
left without a core function because its current GOA support is only generic
oxidoreductase activity despite a betaine-aldehyde dehydrogenase protein name.

Completed the first-pass `ppu00910` / `nitrogen_cycle` checkpoint. Reused and
validated `modules/nitrogen_cycle.yaml`, fetched the 15 missing review folders,
ran Asta for all 16 missing gene-level reports including already-curated `nasA`,
curated the 14 pending review YAMLs plus no-GOA PP_3392 so all 20 batch members
now have no `PENDING` actions, validated all 20 gene reviews, and rendered all
20 gene pages.

Falcon module-level synthesis remains queued for `nitrogen_cycle` / `ppu00910`:
the current session has Edison Falcon access returning HTTP 402 for module
research, so this checkpoint is recorded as a local/UniProt/GOA/Asta first pass
plus the existing validated species-neutral nitrogen-cycle module.

Main ppu00910 lessons: KT2440 ppu00910 is primarily an assimilation and
side-chemistry map rather than a complete nitrogen-cycle redox repertoire. The
strict assimilatory nitrate/nitrite branch is represented by `nasA`, `nirB`, and
`nirD`; central ammonia assimilation is represented by `glnA`, `gltB`, `gltD`,
`gdhA`, and `gdhB`; and carbonic-anhydrase/nitronate nodes (`cynT`, PP_0430,
`yrpB`, PP_3392) are boundary reactions. `puuA-I`, `puuA-II`, `spuB`, and `spuI`
are curated as polyamine-catabolic GS-fold enzymes; electronic glutamine
synthetase transfers are removed where the product/EC supports
glutamate-putrescine or glutamylpolyamine ligase chemistry. PP_3392 remains
without a core function because it has no GOA annotations and only a broad gamma
carbonic-anhydrase-like/hexapeptide-repeat identity.

Completed the `ppu00770` / `pantothenate_and_coa_biosynthesis` checkpoint plus
the supporting UniPathway `UPA00028` bucket. Created and validated
`modules/pantothenate_and_coa_biosynthesis.yaml`, ran both Falcon reports,
fetched all 24 KEGG membership candidates plus UniPathway-only `PP_4452`, ran
Asta for the selected genes, curated the pending/new reviews, and rendered the
affected gene pages. Validation is clean except for expected first-pass Asta
context warnings and intentional no-core warnings on the uncertain reductase
candidates `PP_2325`, `PP_2998`, and `PP_4452`.

The main ppu00770 conclusion is that KT2440 has a coherent strict CoA route:
PanB/PanC for pantothenate assembly and `coaX`, `dfp`/CoaBC, `coaD`, and `coaE`
for conversion of pantothenate to CoA. Falcon identified `coaX` as the strongest
species-linked step. The ketopantoate reductase node remains unresolved:
`panE` is the expected primary candidate, while `PP_2325`, `PP_2998`, and
`PP_4452` look like electronically propagated paralog calls without
KT2440-specific evidence. KT2440 also lacks the canonical PanD beta-alanine
route in this pathway set, so `pydA`/`pydX`, `pydB`, `hyuC`, and related
beta-alanine metabolism genes are recorded as species-specific precursor
context rather than strict core pantothenate/CoA enzymes.

Completed the `ppu00760` / `nad_biosynthesis_and_nicotinate_metabolism`
checkpoint. Created and validated
`modules/nad_biosynthesis_and_nicotinate_metabolism.yaml`, ran both Falcon
reports, fetched all 30 KEGG membership candidates, ran Asta for the selected
genes, curated the 23 pending/new review files, and revalidated all 30 gene
reviews plus the module. The remaining gene-review warnings are expected:
first-pass Asta files are referenced as identity/context retrieval rather than
annotation-level evidence, and `PP_3103` deliberately has no core function.

The main ppu00760 conclusion is that KT2440 satisfies de novo NAD biosynthesis
through `nadB`, `nadA`, `nadC`, `nadD`, and ammonia-dependent `nadE`; nicotinate
salvage through `pncB` plus NMN amidohydrolase `pncC`; NADP/redox balancing
through `nadK`, `sthA`, and the split Pnt transhydrogenase genes; and aerobic
nicotinate catabolism through the `nic` cluster (`nicA`, `nicB`, `nicC`,
`nicX`, `nicD`, `nicF`, `maiA`). Falcon flagged `davD`, `sad-I`, `sad-II`,
`gabD-II`, `ushA`, `surE`, `PP_2531`, `mazG`, `nudC`, and `cobB__Q88BY5` as
boundary-only and `PP_3103` as candidate-uncertain. A canonical PncA
nicotinamidase was not found in the candidate set and is now recorded as an
explicit salvage gap.

Completed the `ppu00750` / `vitamin_b6_metabolism` checkpoint. Created and
validated `modules/vitamin_b6_metabolism.yaml`, ran both Falcon reports,
fetched all 9 KEGG membership candidates, ran Asta for the newly selected genes,
curated the batch reviews, updated `serC` for its shared PLP-pathway role, and
validated the 9 gene reviews plus the module.

The main ppu00750 conclusion is that KT2440 satisfies the strict
DXP-dependent de novo vitamin B6/PLP route through `epd`, `pdxB`, `serC`,
`pdxA`, `pdxJ`, and `pdxH`. `pdxY` covers pyridoxal salvage phosphorylation.
`thrC` and `PP_0662` remain threonine synthase/PLP-enzyme boundary context, not
committed B6 biosynthetic steps. `dxs` supplies the shared DXP precursor but is
already represented in the thiamine and MEP backbone context; no obvious
PdxK-like broader B6 kinase candidate was found in local metadata.

Completed the `ppu00740` / `riboflavin_biosynthesis` checkpoint. Created and
validated `modules/riboflavin_biosynthesis.yaml`, ran both Falcon reports,
fetched or rechecked all 15 KEGG membership candidates, ran Asta for the selected
genes, curated the 15 reviews, and rendered the updated RibBX gene pages.

The main ppu00740 conclusion is that KT2440 satisfies strict riboflavin, FMN,
and FAD biosynthesis through `ribA`, `ribD`, `ribB`, `ribH`, `ribE`, and `ribF`,
with `ribC` retained as a duplicate riboflavin synthase candidate. The critical
lesson was `ribAB-I`/PP_0516 and `ribAB-II`/PP_3813: Falcon recovered
KT2440-specific RibBX evidence showing DHBP synthase activity but no GTP
cyclohydrolase II activity, so GO:0003935 was removed for both genes and the
module now satisfies that step only with `ribA`. `ssuE`, `msuE`, `bluB`,
`ubiX`, `nudF`, and `had` are boundary or side-node entries rather than strict
riboflavin/FMN/FAD biosynthesis members.

Completed the `ppu00730` / `thiamine_biosynthesis` checkpoint. Created and
validated `modules/thiamine_biosynthesis.yaml`, ran both Falcon reports, fetched
or rechecked all 13 KEGG candidates, promoted `pet`/PP_3185 and `PP_5105`,
ran Asta for the selected genes, and validated the 15 curated reviews plus the
module.

The main ppu00730 conclusion is that KT2440 satisfies the strict bacterial
thiamine diphosphate biosynthesis module through `dxs`, `thiC`, `thiD`, `thiO`,
`thiG`, `thiE`, and `thiL`. `iscS` and `thiI` are shared sulfur-relay support
genes rather than thiamine-specific core enzymes; `PP_3186` and `pet` are
TenA-family salvage context; `adk` and `rsgA` are KEGG side nodes. Falcon
correctly flagged a ThiS/ThiF sulfur-relay gap: local metadata supports
`PP_5105` as ThiS, while no unambiguous `thiF` product or symbol was found, so
PP_0735/`moeB` was not promoted without stronger evidence.

Completed the `ppu00900` / `terpenoid_backbone_biosynthesis` checkpoint. Created
and validated `modules/terpenoid_backbone_biosynthesis.yaml`, ran both Falcon
reports, fetched and curated the previously missing MEP/prenyl genes (`dxs`,
`ispA`, `ispH`, `ispB`, `ispE`, `ispG`, `uppS`, `dxr`, `ispF`), added Asta for
`ispD`, and validated all 17 candidate reviews plus the module.

The main ppu00900 conclusion is that KT2440 satisfies the strict bacterial
MEP/DOXP route plus immediate prenyl-diphosphate extension: `dxs`, `dxr`,
`ispD`, `ispE`, `ispF`, `ispG`, `ispH`, `ispA`, `ispB`, and `uppS`. `ubiX`
remains a ubiquinone-biosynthesis boundary enzyme. The thiolase and
acetyl-CoA acetyltransferase entries (`PP_0582`, `fadA__Q88L84`, `PP_2215`,
`PP_3355`, `bktB`, `yqeF`) remain fatty-acid/mevalonate-like spillovers and do
not support a native KT2440 mevalonate pathway. Falcon suggested `idi`/PP_0854
as a gap, but local and live UniProt checks identify PP_0854 as `hisS` and find
no UP000000556 IDI/EC 5.3.3.2 entry, so that recommendation was rejected.

Completed the first-pass `ppu00906` / `carotenoid_biosynthesis_boundary`
checkpoint. Created and validated
`modules/carotenoid_biosynthesis_boundary.yaml`, registered the KEGG mapping,
fetched `crtZ`/PP_3246, ran Asta, curated the four GOA annotations, validated
the review and module, rendered the gene and module pages, and refreshed the
batch page.

Main ppu00906 lesson: the KEGG map contains only `crtZ`, so this is a
one-gene carotenoid boundary/partial pathway. `crtZ` is retained as a predicted
beta-carotene 3-hydroxylase in xanthophyll biosynthesis; broader carotene
metabolism and generic oxidoreductase annotations are non-core context. The
batch does not establish a complete carotenoid backbone/desaturation/cyclization
route in KT2440.

Completed the first-pass `ppu00907` /
`pinene_camphor_geraniol_degradation_boundary` checkpoint. Created and
validated `modules/pinene_camphor_geraniol_degradation_boundary.yaml`,
registered the KEGG mapping, regenerated the seven-gene checklist, validated the
already-curated reviews plus the module, rendered all seven gene pages plus the
module page, and refreshed the batch page.

Main ppu00907 lesson: this KEGG map is boundary overlap with lower
CoA-thioester and HMG-CoA side chemistry. `PP_3394` and `mvaB` are HMG-CoA
lyase-family paralogs, while `fadA__Q88L84`, `fadB`, `fadA__Q88L01`, `PP_2217`,
and `paaF` are fatty-acid/phenylacetate/CoA-thioester spillovers. The batch
lacks route-defining pinene, camphor, or geraniol upper-pathway enzymes, so no
new monoterpene-specific gene-review edits were needed.

Completed the `ppu00130` / `ubiquinone_biosynthesis` checkpoint. Created and
validated `modules/ubiquinone_biosynthesis.yaml`, ran both Falcon reports,
curated the 14 KEGG ppu00130 candidate reviews, promoted `ubiJ`, `ubiB`, and
`ubiK` from UniPathway/Falcon accessory-factor evidence, and validated all 17
reviews plus the module.

The main ppu00130 conclusion is that KT2440 satisfies the strict aerobic
ubiquinone biosynthesis module after adding the accessory factors. The apparent
UbiI gap is a nomenclature issue: `visC`/PP_5197 is the UbiH/Coq6-family,
PTHR43876:SF7, GO:0019168 2-polyprenylphenol hydroxylase candidate and is
treated as the UbiI-like C5 hydroxylation step pending deeper experimental
confirmation. KEGG ppu00130 is still broader than strict UQ biosynthesis:
`hpd`, `PP_1218`, `PP_1644`, `PP_2789`, and `PP_3720` were curated as
homogentisate, thioesterase, or quinone-redox side nodes rather than
biosynthetic steps.

## 2026-07-06

Completed the `ppu00074` / `mycolic_acid_biosynthesis` boundary checkpoint.
Created `modules/mycolic_acid_biosynthesis.yaml`, curated the newly fetched
`PP_1183` review, rechecked the already curated `fabD` review, ran both Falcon
reports, and validated the module plus both gene reviews.

The main ppu00074 conclusion is a clean absence call. KT2440 does not have a
satisfiable mycolic-acid biosynthesis pathway; the KEGG assignment is a
spillover from shared PPTase and FabD chemistry. `PP_1183` remains a
siderophore/NRPS carrier-protein activation enzyme, while `fabD` remains the
FAS-II malonyl-CoA:ACP transacylase already covered by `ppu00061`. The
diagnostic mycolate machinery, including Pks13, FadD32, CmrA, MmpL3,
Ag85/Fbp, KasA/KasB, InhA, MabA, HadABC, and meromycolate modification enzymes,
is absent/not expected in this Gram-negative target taxon.

Started the `ppu00061` / `fatty_acid_biosynthesis` checkpoint. Created and
validated `modules/fatty_acid_biosynthesis.yaml`, extracted the 19-gene KEGG
candidate checklist, fetched all missing review folders, ran Asta retrieval for
all candidates, curated every gene review, ran both Falcon reports, and
validated the batch.

The Falcon-backed ppu00061 split is now stable. The canonical ACC/FAS-II core
is represented by `accA`, `accB`, `accC`, `accD`, `fabD`, `fabG`, `fabZ`,
`fabA`, `fabB`, `fabF`, `PP_4379`, and `fabV`. The main module lesson is that
pseudomonad initiation should not be modeled as FabH-only: `fabB` is now noted
as a possible FabH-independent initiator, while `PP_4379` remains a candidate
KAS III initiator without assumed essentiality. `PP_1852` was downgraded from
a provisional core alternate reductase to an undecided/boundary candidate
because `fabV` is the best core ENR assignment. `PP_3303` remains a plausible
FabF/KAS-II paralog. `fadD-I` and `fadD-II` are valid long-chain
fatty-acid-CoA ligases for beta-oxidation context, not de novo acyl-ACP FAS-II
steps. `PP_2783` was curated as p-cumate dehydrogenase and its
fatty-acid-elongation TreeGrafter annotation was removed. `PP_0581` and
`PP_2540` remain deliberately no-core-function boundary/unknown SDR candidates.

Completed the lipid/cell-envelope checkpoint, `ppu00071` /
`bacterial_fatty_acid_beta_oxidation`. Regenerated the batch worklist, fetched
the 7 previously missing KEGG candidates (`fadE`, `acd`, `PP_2437`, `PP_2793`,
`PP_3725`, `alkT`, and `PP_5371`), ran Asta for them, curated the seven
pending first-pass reviews, and validated the full 22-gene KEGG batch. Falcon
then promoted `PP_0368`, `PP_0370`, `PP_0763`, and `hbd`/PP_3755 as missing
coverage and triggered a check of `def2`/PP_4559, which was curated as a
peptide-deformylase identifier conflict rather than accepted as a CoA ligase.
The new `modules/bacterial_fatty_acid_beta_oxidation.yaml` seed validates after
adding the promoted activation, ACAD, and short-chain oxidation context, while
the existing metazoan mitochondrial `fatty_acid_beta_oxidation` module remains
unchanged.

Completed the `ppu00051` / `fructose_mannose_metabolism` checkpoint. Created
`modules/fructose_mannose_metabolism.yaml`, regenerated the 18-gene KEGG
checklist, fetched and Asta-backed all missing candidates, ran both Falcon
reports, curated the new reviews, and validated the 18 KEGG candidates plus the
Falcon-promoted `fruB`/PP_0793 review.

The main ppu00051 conclusion is another boundary split. KEGG combines fructose
PTS entry, GDP-mannose/alginate precursor synthesis, alginate polymer handling,
the PP_1776/gmd/rmd LPS/O-antigen GDP-D-rhamnose branch, and central-carbon
spillover genes. Falcon identified `fruB` as the missing PTS phosphorelay
component required with `fruA`, so it was promoted from `ppu02060` and curated.
Falcon also corrected the PP_1776 branch interpretation: PP_1776 is WbpW-like
LPS/O-antigen GDP-mannose context, not the alginate operon `algA`; `gmd` and
`rmd` were updated to GDP-D-rhamnose/LPS branch terms. `PP_2037` remains
deliberately unresolved as a likely KEGG spillover artifact.

Completed the `ppu00053` / `hexuronate_aldarate_catabolism` checkpoint.
Created `modules/hexuronate_aldarate_catabolism.yaml`, regenerated the 8-gene
checklist, fetched and Asta-backed the missing primary KEGG candidates
(`PP_3599`, `garD`, and `gudD`), ran both Falcon reports, curated the new
reviews, refined `gnl`/PP_1170 and `PP_3602`, and validated the batch plus the
module.

The main ppu00053 conclusion is that the KEGG ascorbate/aldarate map should be
curated as a free-hexuronate/aldarate catabolic module in KT2440, not as
eukaryotic ascorbate metabolism. The satisfiable route is `udh` -> `gnl`/UxuL
-> `gudD` or `garD` -> `PP_3599`/KdgD -> `PP_3602`/KgsD. Falcon promoted
`gnl`/PP_1170 as the missing UxuL-family lactonase and resolved `PP_3602` as
the strongest local aldarate-pathway KGSADH candidate; `PP_1256` and `PP_2585`
remain KGSADH-like paralogs without equivalent aldarate-cluster context. `udg`
is a UDP-glucuronate/nucleotide-sugar side node and should not satisfy the
free-aldarate catabolic module.

Completed the `ppu00040` / `pentose_glucuronate_interconversions` checkpoint.
Regenerated the 8-gene checklist, fetched and Asta-backed the six missing KEGG
candidate reviews (`PP_1256`, `PP_2037`, `PP_2585`, `PP_2694`, `udg`, and
`PP_3602`), ran both Falcon reports, curated all KEGG candidate reviews, and
validated the batch plus `modules/pentose_glucuronate_interconversions.yaml`.
The species-aware Falcon report also promoted two gap-fill genes absent from the
KEGG candidate list, `gnl`/PP_1170 and `udh`/PP_1171, so both were fetched,
Asta-backed, curated, and validated as part of this checkpoint.

The main ppu00040 conclusion is another boundary call. KEGG conflates
pentose-phosphate interconversion (`rpe`), nucleotide-sugar/envelope precursor
chemistry (`galU` and `udg`), and oxidative free-hexuronate or aldarate
catabolism. The real hexuronate entry arm is anchored by experimentally
characterized `udh` and a candidate lactonase `gnl`; the aldarate dehydratase
and KGSADH questions were carried into the adjoining ppu00053 pass. The three
EC 1.2.1.26 candidates (`PP_1256`, `PP_2585`, `PP_3602`) were curated as
predicted 2,5-dioxovalerate/KGSA dehydrogenases but not assigned uniquely to
hexuronate catabolism from ppu00040 alone. `PP_2037` and `PP_2694` remain weak
or over-propagated KEGG-side candidates.

Completed the `ppu00052` / `galactose_leloir_pathway` checkpoint. Regenerated the
8-gene checklist, fetched and Asta-backed the missing `PP_0501`, `galE`, and
`galU` reviews, curated all batch review YAMLs, ran both Falcon reports, and
validated all gene reviews plus `modules/galactose_leloir_pathway.yaml`.

The main ppu00052 conclusion is that canonical Leloir galactose catabolism is
not satisfied in KT2440. The committed `galK` and `galT` steps are absent, and
Falcon found the literature pattern expected for KT2440: wild-type cells do not
natively grow on D-galactose, while engineered strains require heterologous
galactose-utilization genes. The KEGG galactose map candidates are therefore
side nodes: `galE`, `galU`, `algC`, `cpsG`, and `pgm` belong to UDP-sugar,
cell-envelope, glycogen, or central-carbohydrate context; `glk` and `PP_1165`
belong with glucose/aldose handling; and `PP_0501` remains an uncertain
NAD-dependent epimerase/dehydratase family protein with no core function.

Completed the `ppu00340` / `histidine_biosynthesis` checkpoint. Regenerated the
20-gene checklist, fetched all missing reviews, ran Asta for all candidates, ran
both Falcon reports, curated the full batch, and validated all gene reviews plus
`modules/histidine_biosynthesis.yaml`.

The main ppu00340 conclusion is that KT2440 has the expected de novo histidine
biosynthesis route, but the histidinol-phosphate phosphatase step remains a
candidate-uncertain point between `PP_3157` and `PP_5147`. Core biosynthesis
coverage includes `hisG`/`hisZ`, `hisE`, `hisI`, `hisA`, `hisH`/`hisF`,
`hisB`, `hisC`, and `hisD`. KEGG "Histidine metabolism" is broader than the
biosynthesis module: `hutH`, `hutU`, `hutI`, `hutF`, and `hutG` are histidine
catabolism; `gshA`, `PP_4983`, and `PP_1721` are off-pathway or over-mapped side
nodes. Module curation fixed a neutral-module error where HisE/HisI step labels
and connections were reversed; Falcon reports were regenerated after the fix.

Completed the `ppu00270` / `methionine_biosynthesis` checkpoint. Regenerated the
46-gene checklist, ran both Falcon reports, fetched and Asta-backed all selected
genes, curated all review YAMLs, and validated the full batch plus
`modules/methionine_biosynthesis.yaml`.

The main ppu00270 conclusion is that KT2440 satisfies the strict methionine
biosynthesis-from-homoserine module. The preferred route is homoserine
O-succinylation by `metXS`/MetXW, direct sulfhydrylation through `metZ`, and
terminal methylation by `metE` and/or `metH`; `PP_2528`, `metB`, `PP_4348`, and
`PP_4594` are secondary or candidate sulfur-incorporation context rather than
the primary route. The broad KEGG cysteine and methionine map also pulls in
cysteine biosynthesis, upstream aspartate-family precursor supply, SAM
cycle/salvage, DNA methyltransferases, serine/threonine/BCAA side nodes, and
sulfurtransferases. First-pass fixes included removing bacterial-inappropriate
CpG-island methylation terms from DNA methyltransferases, treating `PP_4637` as
an unresolved MetE-like fragment/family member rather than a full methionine
synthase, and removing hydroxyglutarate over-propagation from `serA`.

Completed the `ppu00622` / `benzoate_upper_pathway` checkpoint. Created the
neutral `modules/benzoate_upper_pathway.yaml`, ran both Falcon reports,
regenerated the 6-gene checklist, and validated the module plus all resolved
batch review files.

The main ppu00622 conclusion is that KT2440 satisfies the benzoate upper pathway
with `benA`, `benB`, `benC`, and `benD`: benzoate 1,2-dioxygenase converts
benzoate to the cis-dihydrodiol, and BenD oxidizes that intermediate to
catechol. KEGG "Xylene degradation" is broader than this module and includes
TOL/meta-cleavage context not encoded as the benzoate route in KT2440.
`PP_1791` and `PP_2504` remain side meta-cleavage context, while `catA-II` is
downstream/boundary-adjacent rather than part of the upper-pathway module.

Completed the `ppu01220` / `aromatic_compound_degradation` checkpoint. Created
the neutral `modules/aromatic_compound_degradation.yaml` as an umbrella route
map, ran both Falcon reports, fetched/Asta-backed/curated the missing `ubiX`
review, regenerated the 20-gene checklist, and validated the full batch plus the
module.

The main ppu01220 conclusion is that KEGG "Degradation of aromatic compounds" is
not a single satisfiability module. In KT2440 the core benzoate and
4-hydroxybenzoate ortho-cleavage route runs through `benABCD`, `pobA`,
`catA`/`catB`/`catC`, `pcaG`/`pcaH`, `pcaB`/`pcaC`/`pcaD`, and the lower
beta-ketoadipate genes `pcaI`, `pcaJ`, and `pcaF`. Falcon flagged `pcaI`,
`pcaJ`, and `pcaF` as missing from the KEGG ppu01220 candidate list even though
they are encoded in KT2440 and already covered by the `ppu00362` pass. `ubiX`,
`frmA`, `adhP`, `PP_1791`, and `PP_2504` are side-node or over-propagated
members for this umbrella, while `catA-II` and `PP_3648` remain
paralog/substrate-ambiguous.

Completed the `ppu00362` / `benzoate_degradation` checkpoint. Created the
neutral `modules/benzoate_degradation.yaml`, ran both Falcon module reports,
fetched/Asta-backed/curated all 40 KEGG candidate genes, and validated the full
batch. The regenerated checklist now records 40 review files, 40 curated
reviews, and 40 Asta reports.

The main ppu00362 conclusion is a scope boundary for aromatic catabolism. The
strict satisfiable route is benzoate entry through `benA`/`benB`/`benC`/`benD`
and catechol/protocatechuate beta-ketoadipate metabolism through the `cat`,
`pca`, and `pobA` branches. KEGG `ppu00362` also pulls in gallate, phenylacetate,
fatty-acid-like CoA metabolism, cytochrome P450/ferredoxin side nodes, and
generic thiolases; these were curated where useful but should not be counted as
strict benzoate/beta-ketoadipate module steps. `PP_3648` was reviewed as a
no-GOA uncertain CMD-family protein, and `PP_1791` remains undecided with no
core function because the family-level synthase/pathway assignment is ambiguous.

Completed the `ppu00010` / `entner_doudoroff_and_gluconeogenesis` checkpoint.
Created the neutral `modules/entner_doudoroff_and_gluconeogenesis.yaml`, ran
both Falcon module reports, fetched/Asta-backed/curated the 18 previously
missing ppu00010 reviews, and validated the full 38-gene batch. Regenerating the
TCA checklist after this pass also reconciled the pyruvate-dehydrogenase/lipoate
overlap: `ppu00020` now records 30/30 review files, 30/30 curated reviews, and
30/30 Asta reports.

The main ppu00010 conclusion is another boundary decision. KT2440 glucose
catabolism is ED/EDEMP-centered, while KEGG `ppu00010` omits the defining `edd`
and `eda` ED genes and includes many adjacent nodes: pyruvate dehydrogenase,
acetyl-CoA synthetases, alcohol/aldehyde dehydrogenases, lipoate E3 paralogs,
and sugar-phosphate epimerases. These were curated as valid enzyme reviews where
supported, but they should not be counted as satisfying strict ED/lower-EMP
steps.

Completed the `ppu00030` / `pentose_phosphate_pathway` checkpoint. Created the
neutral `modules/pentose_phosphate_pathway.yaml`, ran both Falcon module reports,
and curated all 36 candidate genes in the batch. The regenerated checklist
`projects/P_PUTIDA/batches/ppu00030_pentose_phosphate_pathway.md` now records 36
review files, 36 curated reviews, and 36 Asta reports.

The main PPP conclusion is a boundary decision: strict PPP chemistry is covered
in KT2440, but KEGG `ppu00030` mixes strict PPP genes with ED genes, peripheral
glucose/gluconate oxidation, EDEMP-cycle recycling, ribose/PRPP metabolism, and
cell-envelope sugar-node enzymes. These neighboring genes are useful biological
context but should not satisfy strict PPP module steps.

Corrected a real alias collision for `pgm`. The initial fetch followed UniProt
GpmI/Q88CX4, which has synonym `pgm`; the KEGG PSEPK `ppu00030` member is
PP_3578/Q88GY7 phosphoglucomutase. The `genes/PSEPK/pgm` folder now targets
Q88GY7 and validates.

Validation completed for all 36 `ppu00030` gene reviews and for
`modules/pentose_phosphate_pathway.yaml`. Remaining warnings are non-blocking:
the environment-level `pkg_resources` deprecation notice, a few older reviews
that do not cite Asta/Falcon directly, and the intentional no-core-function
warning for `ppgL`.

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
