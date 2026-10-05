---
title: "PANTHER family assignment discrepancies"
maturity: SCOPING
tags: [EVALUATION, PIPELINE]
species: [human, worm]
genes: [MEGF10, ced-1]
---

# PANTHER family assignment discrepancies

**Bottom line:** the same PANTHER release can put a protein in different
families depending on where you look. UniProt's `DR PANTHER` cross-references
come from InterPro's best-hit HMM match. PANTHER's own sequence classification
files (and the PAINT trees that IBA annotations come from) come from PANTHER's
own pipeline. When the two disagree, a module or review that takes its family
id from UniProt can be grounded on a family that has no PAINT tree for the
protein, while the family that does carry that tree goes unused. This project
records such cases. So far it holds one, found while building the phagocytosis
modules.

## Why this matters here

- **Module grounding.** `FamilyDescriptor.term` ids are checked against the
  PANTHER member index (`.cache/panther/panther-members-<release>.tsv`, built by
  `just refresh-panther-members`), which uses PANTHER's own classification first
  and falls back to UniProt. A curator who copies the family id from a UniProt
  entry may therefore get a family that differs from the one the validator
  checks against.
- **IBA interpretation.** PAINT nodes (PTNs) belong to PANTHER's own trees. If
  the UniProt cross-reference names another family, the IBAs a protein carries
  appear to come from a family it does not belong to.
- **Orthology claims.** Family ids are used as evidence of orthology between
  representative members. Two sources that disagree make that evidence
  ambiguous.
- **Gene fetching.** `fetch-gene` picks the PANTHER family to download from
  the UniProt cross-reference (`_extract_panther_family_id` in
  `src/ai_gene_review/etl/gene.py`). For a discrepant gene it caches family
  data for the wrong family, and `fetch-panther-paint` then cannot build the
  PAINT slice for the right one, because that needs `<FAMILY>-entries.csv`.

## Case log

| # | Proteins | UniProt / InterPro family | PANTHER 19.0 classification | PAINT | Status | Found in |
|---|---|---|---|---|---|---|
| 1 | C. elegans ced-1 (UniProtKB:Q9XWD6), human MEGF10 (UniProtKB:Q96KG7) | ced-1 → PTHR24043:SF8 (SCAVENGER RECEPTOR CLASS F / EGF-LIKE DOMAIN-CONTAINING PROTEIN); MEGF10 → PTHR24052:SF13 (DELTA-RELATED / MULTIPLE EGF LIKE DOMAINS 11) | Both in PTHR24035 (MULTIPLE EPIDERMAL GROWTH FACTOR-LIKE DOMAINS PROTEIN): ced-1 → SF109 PROTEIN DRAPER; MEGF10 → SF136 | MEGF10 IBAs come from PTN002372116 and PTN009076277, nodes whose seeds include ced-1, Draper and mouse Megf10 | Resolved in module: grounded on PTHR24035 with PAINT nodes; upstream discrepancy still open | [phagocytic engulfment module](../modules/phagocytic_engulfment.yaml) |

### Case 1: CED-1 / Draper / MEGF10 engulfment receptors

CED-1 (C. elegans), Draper (Drosophila) and MEGF10 (vertebrates) are the
standard orthologous engulfment receptors for apoptotic cells. They are
multiple-EGF-like-domain transmembrane proteins with an EMI domain and NPxY /
YxxL tail motifs.

**What UniProt says** (entry version 168 for Q9XWD6 and 173 for Q96KG7,
2026-06-10; InterPro 110.0, PANTHER 19.0):

- ced-1 → `PTHR24043` SCAVENGER RECEPTOR CLASS F, subfamily `PTHR24043:SF8`.
  The InterPro match covers only residues 685–963 of 1111, which lie in the
  EGF-like-repeat region.
- MEGF10 → `PTHR24052` DELTA-RELATED, subfamily `PTHR24052:SF13`
  ("MULTIPLE EGF LIKE DOMAINS 11"). The InterPro match covers residues 9–675
  of 1140.

**What PANTHER's own classification says** (`PTHR19.0_<organism>` sequence
classification files, cached under `.cache/panther/` by
`refresh-panther-members`):

- `PTHR24035:SF109` PROTEIN DRAPER: ced-1 (Q9XWD6), Drosophila drpr (Q9W0A0),
  and Dictyostelium sibA–sibD (Q54KF7, Q54JE1, Q54JA5, Q54JA4).
- `PTHR24035:SF136` MULTIPLE EPIDERMAL GROWTH FACTOR-LIKE DOMAINS PROTEIN 10:
  MEGF10 orthologs from human, mouse, rat, cow, chicken, Xenopus and
  zebrafish.

**What PAINT says** (QuickGO IBA rows for Q96KG7, WITH/FROM column):

- `GO:0043652` engulfment of apoptotic cell, from `PTN002372116`. Seeds:
  FB:FBgn0027594 (drpr), MGI:2685177 (Megf10), WB:WBGene00000415 (ced-1).
- `GO:0005044` scavenger receptor activity, from `PTN009076277`. Seeds:
  Q96KG7 and WB:WBGene00000415.

PAINT therefore treats CED-1, Draper and MEGF10 as a single clade inside
PANTHER's tree. This agrees with the PANTHER classification and the
literature, and disagrees with the UniProt cross-references.

**InterPro's own family membership is consistent with its cross-references.**
The member list InterPro returns for PTHR24052
(`interpro/panther/PTHR24052/PTHR24052-entries.csv`, fetched by `fetch-gene`)
places human, mouse and zebrafish MEGF10 in `PTHR24052:SF13`, together with
human MEGF11. The PTHR24035 member list contains no MEGF10. The disagreement
therefore covers MEGF10 across vertebrates, not just one entry, and it lies
between the InterPro and PANTHER assignment pipelines.

**Caveats.**

- PTHR24035 is a broad family. Of its 11 human members, 9 sit in a
  laminin-dominated subfamily (`SF127` LAMININ SUBUNIT ALPHA-5-RELATED, which
  also holds MEGF11) and MEGF6 has its own subfamily (`SF137`). A family-level
  id alone therefore says little. No single subfamily contains both
  representatives.
- The name of the UniProt-assigned subfamily (`PTHR24052:SF13`, "MULTIPLE EGF
  LIKE DOMAINS 11") does not match PANTHER's own placement of human MEGF11,
  which is `PTHR24035:SF127`. In the cached classification files the only
  member of `PTHR24052:SF13` is bovine MEGF11 (F1MRL6). MEGF11 may be a second
  case; it has not been checked.
- The likely mechanism is an assumption, not a verified fact. InterPro keeps
  the single best-scoring family HMM, and EGF-repeat-rich proteins score well
  against several neighbouring EGF-rich families. This needs confirming, for
  example by comparing full HMM score tables or asking the PANTHER and
  InterPro teams.

**Current handling (resolved locally, 2026-10-03).**

- `fetch-gene human MEGF10` followed the UniProt cross-reference and cached
  `interpro/panther/PTHR24052/`.
- The PTHR24035 family data was fetched explicitly with the same helper
  (`_fetch_panther_family_data`). `fetch-panther-paint PTHR24035` then produced
  `interpro/panther/PTHR24035/PTHR24035-paint.tsv`. That slice contains
  PTN002372116 (P:GO:0043652, seeds drpr, Megf10 and ced-1) and PTN009076277
  (F:GO:0005044 scavenger receptor activity, seeds MEGF10 and ced-1;
  C:GO:0005886).
- `modules/phagocytic_engulfment.yaml` now grounds the CED-1/MEGF10 annoton on
  `PTHR24035`, with both nodes as ancestral nodes and scavenger receptor
  activity as its function.
- The new MEGF10 gene review (`genes/human/MEGF10/`) accepts the IBAs from
  both nodes and records the family question under `suggested_questions`.

## Reproduce

```bash
# UniProt cross-reference (InterPro-derived)
curl -s https://rest.uniprot.org/uniprotkb/Q96KG7.txt | grep '^DR   PANTHER'
# InterPro match coordinates
curl -s https://www.ebi.ac.uk/interpro/api/entry/panther/protein/uniprot/Q96KG7
# PANTHER's own classification (after `just refresh-panther-members`)
grep -h Q96KG7 .cache/panther/PTHR19.0_human
# PAINT provenance of the IBAs
curl -s -H 'Accept: application/json' \
  'https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:Q96KG7&evidenceCode=ECO:0000318'
```

## Next steps

- [x] MEGF10 gene review.
- [ ] ced-1 gene review.
- [ ] Check MEGF11 (possible case 2).
- [ ] Triage the systematic scan. Since the member index moved to
      `.cache/panther/`, `refresh-panther-members` records UniProt's family
      next to PANTHER's (`uniprot_panther_family_sf` column) and reports
      disagreements. A run on 2026-10-05 over every accession cited in
      `modules/` and family reviews found 137 disagreements: 119 at the
      family level and 18 at the subfamily level only. MEGF10 (Q96KG7) and
      ced-1 (Q9XWD6) are among them. Remaining tooling question: should
      `fetch-gene` prefer the PANTHER classification over the UniProt
      cross-reference when choosing which family to cache?
- [ ] Decide whether disagreements of this kind should be reported to
      PANTHER/InterPro.
