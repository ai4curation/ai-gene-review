---
title: "MOD gene descriptions as review input"
maturity: IN_PROGRESS
tags: [PIPELINE, EVALUATION]
species: [worm]
autolink_exclude: [MOD, MODS]
---

# MOD gene descriptions as review input

**Bottom line:** model organism databases (MODs) publish hand-written gene
descriptions, for example WormBase's paragraph for
[rab-11.1](https://www.alliancegenome.org/gene/WB:WBGene00004274). Until this
pilot the review workflow did not use them. A fetcher and sidecar format
existed (`ai-gene-review fetch-descriptions`, `<gene>-descriptions.yaml`), but
they had only been run on 118 yeast genes, and nothing in `fetch-gene` or the
reviewer skills read the files. The fetcher had also stopped working: the
Alliance API changed its response shape, and the worm cross-reference was
parsed wrongly. Both are now fixed.

A pilot on all 432 worm genes found that **374 (87%) have a curated WormBase
description**. In the 16 genes read by hand, our review `description` is
usually more mechanistic and more current. The WormBase text is still worth
reading as a **recall checklist**, though: in 7 of the 16 pairs it
names a phenotype, process or regulator that our review leaves out, and in one
case (fshr-1) a whole functional role that our review never mentions.

**Decision (2026-10-30): treat the curated description as a deep-research
source**, the same way as Affinage. It is written verbatim to
`<gene>-deep-research-<mod>.md` (`wormbase`, `flybase`, `sgd`, `mgi`, `rgd`,
`zfin`, `xenbase`). It is cited as a `file:` reference, and the reviewer's
judgment goes in `references[].reference_review`. The source is sparse,
uncited, undated and only partly trusted, but no new data structures or
processes are needed for it. See [Deep-research integration](#deep-research-integration).

## Data and method

- Fetch: `uv run ai-gene-review fetch-descriptions-bulk worm`. This writes
  `genes/worm/<gene>/<gene>-descriptions.yaml` with UniProt FUNCTION, Alliance
  curated (`Alliance_Imported`, the MOD's own hand-written text), Alliance
  automated, and NCBI RefSeq summaries.
- Alliance now returns synopses as `gene.relatedNotes` with
  `noteType.name` set to `MOD_provided_gene_description` (curated) or
  `automated_gene_description`. The old `geneSynopsis` keys are gone, so the
  previous code returned nothing without raising an error.
- Compare: [compare_descriptions.py](MOD_DESCRIPTIONS/compare_descriptions.py)
  writes [worm-comparison.yaml](MOD_DESCRIPTIONS/worm-comparison.yaml), which
  lists, per gene, the WormBase content words that do not appear in our
  `description`. This is a lexical pointer for choosing genes to read, not a
  quality score.

| Measure (worm) | Value |
|---|---|
| Genes fetched | 432 |
| With curated WormBase description | 374 |
| Median words, WormBase curated | 75 |
| Median words, our `description` | 139 |
| Median share of WormBase content words found in ours | 0.35 |

## Hand comparison (16 genes)

There were eight lowest-overlap genes (cep-1, let-60, fshr-1, lgg-2, gst-4,
mpk-1, ced-4, atg-18) and eight random ones (skn-1, sup-17, fasn-1,
hsp-16.41, rsks-1, lag-2, gpr-1, lipl-4). Low lexical overlap mostly reflects
different emphasis, not error.

**Gaps in our reviews that WormBase points to**

- fshr-1: WormBase describes a role in acetylcholine release at neuromuscular
  synapses (a large-scale synaptic screen; FLP-1 and NLP-12 are possible
  ligands). Our review is entirely about intestinal innate immunity and stress,
  and neither the review YAML nor the notes mention synapses or acetylcholine.
  This needs a follow-up literature check.
- gst-4: WormBase describes a putative prostaglandin D synthase needed for
  sperm guidance towards an oocyte PUFA signal. Our description frames GST-4
  only as a SKN-1-induced detoxifying GST. The review raises the prostaglandin
  question only in a suggested question.
- cep-1: WormBase mentions meiotic chromosome segregation and hypoxia
  sensitivity. The review YAML covers them, but the description does not.
- let-60 and mpk-1: WormBase lists phenotypes our short descriptions omit (male
  spicule, sex myoblast migration, chemotaxis, pachytene progression,
  NOS-3/TRA-1 regulation in the germline). For let-60 none of these appear
  anywhere in the review. For mpk-1 they appear in the annotations but not in
  the description.
- lag-2 and skn-1: WormBase gives detailed expression patterns and their
  regulation (LET-23/SUR-2 regulation of lag-2 in the vulval precursor cells),
  which our descriptions largely leave out.

**Where WormBase is stale or weaker**

- ced-4 is still a "novel protein" with sequestration by CED-9 to membranes. It
  has no apoptosome and no Apaf-1 homology.
- lgg-2 is said to have "no obvious function" and a speculative MAP1
  microtubule role. Our review describes its established autophagosome
  maturation role through VPS-39/HOPS.
- rsks-1 is a "putative" S6K, and hsp-16.41 is a "passive ligand". The
  WormBase texts were written years ago and, like UniProt FUNCTION text for
  yeast SAN1 in the earlier pilot, are not updated as the field moves.
- Several WormBase texts contain formatting damage (words run together, such as
  "PUFA-basedsignal"), which suggests they were not cleaned when imported.

## Deep-research integration

- **Emit:** `just mod-description-deep-research <org> [genes...]`
  (`src/ai_gene_review/etl/mod_description_deep_research.py`). The file holds
  the curated note exactly as served, including WormBase's run-together words,
  with frontmatter recording provider, `authorship` (MOD curators),
  `source_url`, MOD gene id, UniProt accession, fetch date, and
  `citations_provided: false` / `authoring_date_provided: false`. As with the
  Affinage emitter, it contains no AIGR judgment.
- **Only the curated note is used.** The Alliance automated description is
  generated from GO annotations, so citing it would cite the annotations under
  review as evidence for themselves.
- **Wrong-gene check:** the MOD id comes from the UniProt cross-reference.
  Writing is refused (unless `--force`) when the symbol or systematic name of
  the Alliance record matches neither the folder nor any UniProt gene name.
  Human is out of scope.
- **Reviewer guidance** (review and annotation-reviewer skills): run the
  emitter for every non-human review, check each claim, and record a verdict in
  `reference_review`. A claim found only in the MOD text is a lead for a
  literature search.
- The `DEEP_RESEARCH` publication type now covers external narrative sources
  in general, not only AI reports. The frontmatter records authorship.
- `<gene>-descriptions.yaml` stays as the input for the description comparison
  ([compare_descriptions.py](MOD_DESCRIPTIONS/compare_descriptions.py)). It is
  not a review source, because it stores the source text together with our AI's
  rubric scores.

**Worked example: fshr-1.** The WormBase text led to Buckley et al. 2024
(PMID:39561202). That paper shows that intestinal FSHR-1 is necessary and
sufficient for acetylcholine release at the neuromuscular junction, with
GSA-1/Gas and ACY-1 acting downstream and the glycoprotein hormone subunits
GPLA-1 and GPLB-1 upstream. The review now has a NEW
`GO:1900075 positive regulation of neuromuscular synaptic transmission` (IMP)
row, a corrected description (which had wrongly said FSHR-1 had been
"repurposed" away from hormone signaling), stronger support for the IBA
adenylate-cyclase row, and updated open questions. The WormBase reference's
`reference_review` records which claims were traced (synaptic role) and which
were judged stale (FLP-1 and NLP-12 as candidate ligands).

## Description reviews (16 worm genes)

The review of each text is stored in the gene's `<gene>-descriptions.yaml`,
separate from both the gene review and the deep-research file. Every source
(UniProt FUNCTION, WormBase curated, Alliance automated, RefSeq) gets a 1–5
score on correctness, utility, compactness, completeness and specificity, with a
note. The file also gets an `overall_concordance` score across sources and
`findings` (gap, discrepancy, insight). The 16 hand-compared genes are now
`COMPLETE` (`ai-gene-review descriptions-status worm`). Scores are AI
judgments made against each gene's review and the literature it cites.

| Source (n) | Correctness | Utility | Compactness | Completeness | Specificity |
|---|---|---|---|---|---|
| UniProt FUNCTION (14) | 4.8 | 4.4 | 3.4 | 4.1 | 4.2 |
| WormBase curated (16) | 4.1 | 3.2 | 3.4 | 3.0 | 3.1 |
| Alliance automated (16) | 4.2 | 2.5 | 4.0 | 2.4 | 2.5 |

RefSeq is left out of the table: for worm it is a re-dated copy of the
Alliance automated text, and it is scored the same. fshr-1 and hsp-16.41 have
no UniProt FUNCTION text. On correctness the WormBase text scores lowest of the
three because it goes stale (lgg-2 2, ced-4 3). It is more useful than the
automated text, which is accurate but picks peripheral GO terms (Hsp70 binding
for skn-1, dauer maintenance for lag-2). Where UniProt has a reviewed FUNCTION
text, it is the best single source. Concordance was lowest for fshr-1 (2: the
WormBase and automated texts describe different roles) and lgg-2 (2: WormBase
contradicts the rest).

## Recommendations

1. **Use the curated MOD description as an input, not as an authority.** This
   is done through the deep-research file above. Each claim in the curated text
   should be either covered by the review or set aside in `reference_review`
   (for example, "stale: CED-4 is the Apaf-1-like apoptosome adaptor").
2. **Treat a claim that appears only in the MOD text as a literature lead.**
   fshr-1 is the model case: the gap is a missed role, not wording.
3. **Re-audit existing reviews** with the comparison script, starting with the
   lowest-overlap genes, then repeat for fly (FlyBase), mouse (MGI) and zebrafish
   (ZFIN), whose Alliance records carry the same note type.
4. The NCBI step hits rate limits (HTTP 429) on bulk runs. It should honour an
   `NCBI_API_KEY`, or back off and retry.

## Status and next steps

- [x] Fix the Alliance parser and the WormBase gene-id extraction
- [x] Fetch worm descriptions (432 genes) and write the comparison table
- [x] Hand-compare 16 genes
- [x] Decide how to feed the text to reviews: as a deep-research file (2026-10-30)
- [x] Emitter, tests, `just` recipe and skill guidance
- [x] Write `-deep-research-wormbase.md` for the worm genes
- [x] Follow up the fshr-1 synaptic role (PMID:39561202) in its review
- [x] Rubric reviews of all description sources for the 16 hand-compared genes
- [ ] Follow up gst-4 sperm guidance, let-60 phenotypes and the other gaps listed above
- [ ] Generate for fly, mouse, rat, zebrafish and yeast
