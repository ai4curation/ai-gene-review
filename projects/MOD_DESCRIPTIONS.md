---
title: "MOD gene descriptions as review input"
maturity: SCOPING
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

## Recommendations

1. **Use the curated MOD description as an input, not as an authority.** Add
   `fetch-descriptions` to `just fetch-gene` and have the review and
   annotation-reviewer skills read `<gene>-descriptions.yaml`. Each claim in
   the curated text should be either covered by the review or dismissed in the
   notes (for example, "stale: CED-4 is the Apaf-1-like apoptosome adaptor").
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
- [ ] Decide whether to wire the sidecar into `fetch-gene` and the review skills
- [ ] Follow up the fshr-1 synaptic role and gst-4 sperm guidance in their reviews
- [ ] Repeat for fly and mouse
