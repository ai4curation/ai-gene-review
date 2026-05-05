# Ciliary Basal Body-Plasma Membrane Docking — Obsoletion & Replacement

## Overview

A GO obsoletion proposal will retire two ciliogenesis BP terms and merge their
annotations into the existing assembly term for the ciliary transition zone:

- **GO:0097711 ciliary basal body-plasma membrane docking** (BP)
- **GO:1905353 ciliary transition fiber assembly** (BP)

Both will be replaced by **GO:1905349 ciliary transition zone assembly** (BP).

The rationale, captured in the upstream go-ontology discussion, is that the
"docking" term as written actually describes the multi-step process of
transition zone assembly — including basal body recruitment, ciliary vesicle
docking, and plasma membrane fusion — rather than a single docking event.
Annotations are well-covered by the existing transition zone assembly term, so
the redundant/over-broad child can be retired. GO:1905353 (transition fiber
assembly) is being retired alongside it because there are no experimental
annotations to defend its existence and its scope overlaps with the same
assembly process.

This project tracks the impact on AI Gene Review and queues affected genes for
review, since none of the directly annotated genes are currently in this
repository.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6405](https://github.com/geneontology/go-annotation/issues/6405)
- Ontology ticket: [geneontology/go-ontology#31882](https://github.com/geneontology/go-ontology/issues/31882)
- Related (vesicle docking obsoletion): [geneontology/go-annotation#6379](https://github.com/geneontology/go-annotation/issues/6379)

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement |
|---|---|---|
| ciliary basal body-plasma membrane docking | GO:0097711 | GO:1905349 ciliary transition zone assembly |
| ciliary transition fiber assembly | GO:1905353 | GO:1905349 ciliary transition zone assembly |

### Affected experimental annotations (from upstream spreadsheet)

GO:0097711 has 7 experimental annotations across 6 groups. GO:1905353 has no
experimental annotations on the spreadsheet (an additional reason for its
retirement).

| Group | Gene | Species | UniProt / Source ID | Reference | Evidence | Status |
|---|---|---|---|---|---|---|
| FlyBase | Cby | D. melanogaster | FBgn0067317 | PMID:27646273 | IGI | Removed (hattrill, 2026-05-04) |
| FlyBase | dila | D. melanogaster | FBgn0033447 | PMID:27646273 | IGI | Removed (hattrill, 2026-05-04) |
| MGI | Cep290 | M. musculus | MGI:2384917 | PMID:27002738 | IMP | move to GO:1905349 |
| Reactome | RAB3IP | H. sapiens | UniProtKB:Q96QF0 | Reactome:R-HSA-5620912 | TAS | Reactome fixed; appears in June 2026 release |
| UniProt | Cep290 | D. melanogaster | FBgn0035168 | PMID:30013109 | IMP | move to GO:1905349 |
| Xenbase | foxj1.L | X. laevis | XB-GENE-856300 | PMID:24048590 | NAS | move to GO:1905349 |
| ZFIN | pam | D. rerio | ZDB-GENE-090313-384 | PMID:29540787 | IMP | move to GO:1905349 |

No InterPro2GO, UniProt-Keywords, or UniRule mappings to either term were
listed in the upstream issue.

## Impact on this repo

No genes directly annotated to GO:0097711 or GO:1905353 are currently reviewed
here. Searches under `genes/` for CEP290, RAB3IP, foxj1, and pam returned no
matches.

This means **no existing reviews need refresh** for the obsoletion itself, but
the propagated (IBA / electronic) ancestry of GO:0097711 reaches a much wider
set of ciliopathy genes — the GO API returns ~30 species-level entries for
CEP290 alone (the dominant PANTHER family for this term) plus other
transition-zone components — so the obsoletion is timely for any future
ciliopathy-focused reviews. The repo already has substantial cilia coverage
through the [`CAEEL_CILIOPATHY`](CAEEL_CILIOPATHY.md) project (worm `mks-1/3/5/6`,
`mksr-2`, `nphp-1/4`, `daf-19`) and human `INTU` and `TMEM67`, so adding the
basal-body-docking-affected genes would strengthen that coverage.

## Scope

- **Organisms**: human (RAB3IP), mouse (Cep290), D. melanogaster (Cep290 — the
  fly ortholog also has direct experimental support), Xenopus (foxj1), zebrafish
  (pam). Drosophila Cby and dila annotations have already been removed by
  FlyBase upstream and don't need separate handling.
- **GO branches**: BP — the two obsoleted terms are both children of ciliary
  basal body / transition zone assembly. The replacement is a sibling/parent
  in the same branch (no MF or CC component).
- **Type of fix**: terminological — the underlying biology (transition zone
  assembly) is unchanged; reviews would evaluate whether GO:1905349 (transition
  zone assembly) is the appropriate ACCEPT for core function, or whether a more
  specific MF (e.g. basal-body / vesicle tethering MFs from the parallel
  vesicle-tethering obsoletion in #6379) better captures the gene's role.

## Candidate genes for initial review

Verify each with `just fetch-gene <organism> <gene>` before starting and
confirm UniProt accessions. None are currently in the repo.

### Tier 1 — high-priority, multi-disease ciliopathy gene

1. **CEP290** (human, UniProt **O15078**) — centrosomal protein 290; most
   heavily annotated gene under GO:0097711 across species (mouse, fly, fish
   all have direct annotations and the human gene receives IBA propagation
   from PTHR18879). Causal in Joubert syndrome, Leber congenital amaurosis 10,
   Meckel syndrome, Senior-Løken syndrome, and Bardet-Biedl syndrome. Strong
   functional literature on its role in transition zone assembly and ciliary
   gating; an excellent anchor review for the obsoletion.

### Tier 2 — supporting ciliogenesis genes with direct annotations

2. **RAB3IP / Rabin8** (human, UniProt **Q96QF0**) — Rab3-interacting protein,
   guanine nucleotide exchange factor for Rab8a; the Reactome direct-annotation
   target. Important for ciliary vesicle delivery to the basal body — the very
   process that the obsoleted term partially described.
3. **FOXJ1** (Xenopus / human, NCBITaxon:8355 for the upstream NAS annotation)
   — master transcriptional regulator of motile ciliogenesis; the foxj1.L
   annotation is from PMID:24048590. A FOXJ1 review would also feed downstream
   ciliopathy and laterality projects.

### Tier 3 — direct annotations, lower repo priority

4. **PAM** (zebrafish, ZDB-GENE-090313-384) — peptidylglycine alpha-amidating
   monooxygenase ortholog; ZFIN annotation from PMID:29540787 (IMP). Less
   well-aligned with the repo's mammalian-and-canonical-model focus.
5. **Drosophila CEP290** (FBgn0035168) — the fly ortholog has its own direct
   annotation from UniProt, but a single human CEP290 review would cover the
   biology more efficiently than separate fly/mouse reviews.

## Proposed approach

1. **Wait for the obsoletion to land.** The upstream ontology ticket #31882 is
   still open at the time of writing (most recent activity 2026-05-04). FlyBase
   has already removed the two fly annotations and Reactome has fixed the
   RAB3IP entry for the June 2026 release; the remaining four direct
   annotations are pending action by MGI, UniProt, Xenbase, and ZFIN.
2. **Once the obsoletion is applied**, regenerate GOA for any candidate gene
   that gets reviewed; the merged term GO:1905349 should appear in place of
   GO:0097711 for the IBA-propagated entries.
3. **Begin with CEP290 (human)** as the anchor review. Its annotation portfolio
   is large enough to exercise the cilia / ciliopathy curation pattern, and it
   has direct experimental support across multiple species that all converge
   on the transition zone biology.
4. **Follow with RAB3IP** as the second review — the GEF-for-Rab8a function is
   distinct from CEP290's structural role and would diversify the project's
   coverage of ciliogenesis machinery.
5. **Defer FOXJ1, fly CEP290, and zebrafish pam** unless the broader cilia
   project explicitly expands to cover them; for the obsoletion-tracking
   purpose, CEP290 + RAB3IP are sufficient.
6. **Cross-reference with the parallel vesicle docking / vesicle tethering
   obsoletions** ([#6379](https://github.com/geneontology/go-annotation/issues/6379)
   and [#6375](https://github.com/geneontology/go-annotation/issues/6375)) — the
   ciliary-vesicle-tethering biology that the obsoleted term partially captured
   may be better represented by the new MF GO:7770062 vesicle membrane
   tethering activity once that is in production.

## Priority

**Medium-low.** The biology is well-established and there is strong existing
ciliopathy coverage in this repo to leverage, but no current reviews are
blocked by the obsoletion. This is opportunistic — CEP290 in particular is a
major unreviewed ciliopathy gene whose obsoletion-affected annotation makes
this a natural moment to tackle it.

## Status

- 2026-05-05 — Project file created. Tracking upstream issue #6405 (last
  active 2026-05-05). Obsoletion not yet applied. FlyBase Cby/dila annotations
  already removed; Reactome RAB3IP fix scheduled for June 2026 release;
  MGI/UniProt/Xenbase/ZFIN direct annotations still pending. No gene reviews
  started yet in this repo.
