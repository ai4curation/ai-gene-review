# LitScan: literature-scan jobs for genes and modules

Date: 2026-06-19
Status: Design approved, pending spec review
Branch: `feat/litscan`

## Motivation

The sibling project `dismech` runs two deterministic Europe PMC "scan" jobs
(`scripts/literature_scan.py`, `scripts/knowledge_gap_scan.py`) that act as
high-recall **lead generators**: each hits Europe PMC for recent papers, matches
them against the existing curated knowledge base, and emits a markdown + JSON
"packet" for a human or agent to triage. No LLM runs inside the scan; the packet
is a reproducible handoff, never an auto-edit.

We want analogous jobs for `ai-gene-review`, adapted to our two-tier KB
(per-gene reviews and pathway/complex modules) and to our specific interest:
papers that **close knowledge gaps in molecular function** — de-orphaning an
uncharacterized protein, assigning a new molecular activity, adding a new member
to a known pathway/complex, or describing a wholly new pathway. We are explicitly
*less* interested in incremental phenotype/association/expression papers (e.g.
another mouse-knockout phenotype with no new molecular mechanism).

## What dismech does (the pattern we are copying)

Both dismech jobs share one engine:

1. **Reverse retrieval**: one broad Europe PMC query for recent papers, then
   deterministic string-matching of each paper against the curated KB entities.
2. **Anchored to the KB with an "already_cited" flag** — the flag is the gap
   detector: it surfaces papers relevant to an entry but not yet folded into it.
3. **A controlled negative vocabulary** (`GENERIC_DISEASE_TERMS`) to suppress
   noise from ambiguous matchable terms.
4. **Output is a packet** (md for humans/agents, JSON for tooling), ranked.

`literature_scan.py` is the *freshness* job (broad mechanism/variant/treatment
query → which existing disease files each paper touches). `knowledge_gap_scan.py`
is the *novelty* job: the query is gated on gap-signal phrases ("knowledge gap",
"remains unclear", "poorly understood", "controversial", "conflicting evidence")
plus mechanism context, and it additionally **extracts and categorizes the
gap-signal sentences** from each abstract and scores them. That sentence
extraction — handing the reviewer the *evidence of the gap*, not just the paper —
is the part most worth carrying over.

## Goals

- A shared, deterministic, no-LLM Europe PMC scan engine for `ai-gene-review`.
- Four job configs over that engine: gene refresh (A), function-gap /
  de-orphaning (B), module-member discovery (C), new-pathway discovery (D).
- A function-vs-phenotype scorer that ranks "interesting function" papers above
  incremental phenotype/association/expression papers (soft down-weight, not a
  hard drop).
- `just` recipes that produce md + JSON packets under `reports/litscan/`.
- Tests: index-building, scoring/classification, query building, packet render.

## Non-goals (this spec)

- No scheduled CI workflow / auto-PR (deferred; the recipes are on-demand).
- No agent that auto-drafts review/module edits from a packet (deferred).
- No forward retrieval (per-entity Europe PMC queries). Reverse only for now;
  a forward pass over the dark-gene shortlist is a documented future option.
- No changes to the gene-review or module schema.

## Architecture

New package `src/ai_gene_review/litscan/`, wired into the existing typer CLI
(`ai_gene_review.cli:app`) and `just`. Modules:

### `europepmc.py`
Thin Europe PMC search client: paginated GET against
`https://www.ebi.ac.uk/europepmc/webservices/rest/search` with
`resultType=core`, returning `(hit_count, records)`. Reuse the httpx patterns
already in `etl/publication*.py`. A `Publication` dataclass normalizes
id/source/pmid/doi/title/journal/date/authors/abstract (port dismech's
`normalize_text` / `publication_from_record`).

### `entity_index.py`
Builds the match index from our KB and caches it as JSON under
`reports/litscan/index/` (rebuilt on demand or when stale):

- **GeneEntity**: UniProt accession(s), `gene_symbol`, taxon, protein
  names/synonyms (parsed from the gene folder's `*-uniprot.txt` `DE` lines),
  path to the review YAML, the set of cited refs
  (`references[].id` + `existing_annotations[].original_reference_id`,
  normalized to `PMID:`/`DOI:`), and a darkness score (see Dark genes).
- **ModuleEntity**: module `id`/`title`, a term index (title tokens +
  descriptor `preferred_term`s + GO labels + member gene symbols/accessions),
  the current member set (symbols + accessions), and cited refs
  (`evidence[].source_id` entries that are `PMID:`).

**Ambiguity handling** (the `GENERIC_DISEASE_TERMS` analog — critical, because
gene symbols are short and collide with English words and acronyms):

- Each matchable term carries a `confidence` tier: `accession` (e.g. `Q9NRN5`) >
  `protein_name` (full DE name / synonym, length-gated) > `symbol`.
- An **ambiguous-symbol denylist** (e.g. `CS`, `SET`, `ACE`, `APP`, `MET`,
  `CAT`, `REST`, …) plus a minimum-length rule: bare symbols shorter than a
  threshold, or on the denylist, only match when they **co-occur** in the
  title/abstract with a function/organism context token. Accession and
  protein-name matches are always accepted.
- The packet records the matched term and its confidence tier so a downstream
  reviewer can discount low-confidence symbol-only hits.

### `scoring.py`
Vocabularies and a sentence extractor (port dismech's `split_sentences` +
category tagging so packets carry the evidence sentence):

- `FUNCTION_SIGNALS`, grouped and weighted:
  - `de_orphaning`: "previously uncharacterized", "functional characterization
    of", "function … was unknown", "orphan enzyme/receptor", "de-orphan".
  - `enzyme_activity`: "catalyzes", "enzymatic activity", "we show that … is a
    {kinase|phosphatase|methyltransferase|…}", "substrate of", "novel activity".
  - `structure_function`: "crystal structure of", "cryo-EM structure of",
    "structural basis", "structure reveals".
  - `complex_membership`: "subunit of", "component of", "novel member of",
    "part of the … complex", "assembly factor", "directly interacts with".
  - `reclassification`: "pseudoenzyme", "previously thought to be",
    "misannotated", "reannotation", "moonlighting".
- `PHENOTYPE_NEGATIVE` (soft down-weight only — a knockout paper may still carry
  mechanism): knockout-phenotype-only ("knockout mice exhibit", "conditional
  knockout", "deficient mice"), GWAS/association ("genome-wide association",
  "associated with risk", "susceptibility locus", "polymorphism", "SNP"),
  expression/biomarker ("upregulated", "downregulated", "prognostic",
  "biomarker", "expression correlates"), clinical ("case report", "we report a
  patient").
- `MEMBERSHIP_SIGNALS` (job C): "novel component/subunit/member/factor", "is
  required for assembly of", "new … of the … complex/pathway".
- `NEW_PATHWAY_SIGNALS` (job D): "novel pathway", "previously unknown
  biosynthetic", "newly identified complex", "uncharacterized pathway".
- `interest_score = function_score − phenotype_penalty`. Records are sorted by
  the job-appropriate score; phenotype papers fall to the bottom but remain in
  the packet.

### `packet.py`
Markdown + JSON renderers, dismech-style: header (generated_at, profile, date
range, hit_count, record_count), the raw query, then ranked records. Each record
shows title, PMID/DOI/journal/date/authors/URLs, the matched genes/modules with
`already_cited` / `already_member` / `is_dark` / match-confidence flags, the
extracted function/gap/membership sentences with their categories, and the
score. JSON is sorted and deterministic for diffing.

### `jobs.py`
A/B/C/D as configs over the engine (query builder + which index + which scorer +
which sort key + which flags to compute). This is the dismech relationship where
`knowledge_gap_scan` is a thin layer over `literature_scan`.

## The four jobs

All four are reverse: a broad Europe PMC query restricted to a recent date
range, then deterministic matching against an index.

- **A — gene refresh.** Broad recent-papers query with light function context →
  match against the gene index → flag `already_cited` → sort by interest score.
  Direct analog of `literature_scan`. Keeps reviews current; surfaces
  not-yet-integrated papers.
- **B — function-gap / de-orphaning.** Query gated on `FUNCTION_SIGNALS`
  (de-orphaning + characterization phrasing) → match the gene index → **boost
  genes on the dark list**, apply phenotype down-weight → extract the
  characterization sentence. The intersection **dark-gene ∩ just-characterized**
  sorts to the top: that is the highest-value lead.
- **C — module-member discovery.** Query gated on `MEMBERSHIP_SIGNALS` → match
  the module index → flag `already_cited` (against `evidence[].source_id`) **and**
  whether the abstract/title names a gene (symbol or accession) that is **not**
  in the module's current member set → extract the membership sentence. The
  "already_member" flag is the membership-level gap detector.
- **D — new-pathway discovery** (low cadence, lower precision). Query gated on
  `NEW_PATHWAY_SIGNALS` → report high-signal papers that match **no** module
  (anti-match) → candidate new modules. Documented as intentionally
  lower-precision and run less often than A/B/C.

## Dark genes (powers job B)

A precomputed report `reports/litscan/dark_genes.tsv`, derived from existing
review data (no network):

- `core_functions` empty or trivially small, AND/OR
- existing GO annotations dominated by uninformative roots/terms
  (`GO:0003674` molecular_function, `GO:0005515` protein binding, `GO:0005488`
  binding) or are entirely IEA/IBA, AND/OR
- the UniProt protein name matches "Uncharacterized protein" / "Putative" /
  "DUF…".

Each gene gets a `darkness` score (count of the above signals, weighted). The
report is both a standalone curation target list (`ai-gene-review litscan
dark-genes`) and the boost source for job B.

## CLI and just recipes

CLI subcommands on the existing typer app:

```
ai-gene-review litscan build-index        # (re)build the cached entity index
ai-gene-review litscan dark-genes         # write reports/litscan/dark_genes.tsv
ai-gene-review litscan gene-refresh   [--days N | --date-from D --date-to D] [--max-records N]
ai-gene-review litscan function-gap   [...]
ai-gene-review litscan module-member  [...]
ai-gene-review litscan new-pathway    [...]
```

`just` recipes (the core deliverable, mirroring dismech):

```
just litscan-gene-refresh days='7'
just litscan-function-gap days='30'
just litscan-module-member days='30'
just litscan-new-pathway date_from date_to
just litscan-dark-genes
```

## Output

`reports/litscan/<job>/<YYYY-MM-DD>-<job>.md` and `.json`. The markdown packet is
the human/agent triage handoff; the JSON is the diffable machine view. A scan
never edits a review or module file.

## Testing

- Unit: entity-index building from tiny YAML + uniprot.txt fixtures (accession /
  protein-name / symbol tiers, ambiguous-symbol gating, already-cited ref
  collection); dark-gene scoring; scorer sentence classification and
  interest/penalty arithmetic; packet render (golden md/json on a fixed record
  set).
- Doctests on the query builders and `normalize_*` helpers.
- The live Europe PMC fetch goes behind the repo's existing VCR / integration
  marker so unit tests stay offline.

## Risks and mitigations

- **Gene-symbol false positives** (chief risk): mitigated by the confidence
  tiers, ambiguous-symbol denylist, min-length, and context-token requirement
  for bare symbols; the packet labels confidence so reviewers can discount.
- **Recall ceiling of reverse retrieval** (a gene not named in title/abstract is
  missed): accepted for v1; a forward per-entity pass over the dark-gene
  shortlist is the documented future enhancement.
- **Module term breadth** (e.g. "photosynthesis" matches broadly): module term
  index is built from specific descriptor `preferred_term`s and member symbols,
  not just the title, and job C additionally requires a `MEMBERSHIP_SIGNAL`.

## Deferred / future work

- Scheduled GitHub Actions workflow that runs the scans and opens a PR/issue.
- A triage agent/skill that drafts candidate review/module edits from a packet.
- Forward retrieval pass over the dark-gene shortlist for higher recall.
- Precision tuning and a curated benchmark set for job D.
