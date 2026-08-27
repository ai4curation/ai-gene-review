---
title: "Spondylometaphyseal Dysplasias (ISDS Nosology Group 12)"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [human]
genes: [ACP5, TRIP11, FN1, PCYT1A, PLCB3, HHAT, MIA3, TRPV4, GPX4, SBDS, PAM16, CFAP410, NEK1, LBR, PRKG2, COL2A1]
---

# Spondylometaphyseal dysplasias (ISDS nosology group 12)

## Overview

Spondylometaphyseal dysplasias (SMDs) are genetic skeletal disorders with combined
vertebral and metaphyseal involvement. They form **group 12** of the International
Skeletal Dysplasia Society *Nosology of genetic skeletal disorders*, 2023 revision
([PMID:36779427](https://pubmed.ncbi.nlm.nih.gov/36779427/)) — the classification exposed by Monarch's disease-mechanism knowledge
base as the
[`ISDSNosologyGroupEnum`](https://dismech.monarchinitiative.org/pages/classifications/ISDSNosologyGroupEnum.html)
permissible value `spondylometaphyseal_dysplasias`.

That enum value currently carries **no tagged disorders**, unlike every neighbouring
group. This project reviews, curates, and classifies the candidate set: which disorders
belong in group 12, which SMD-named disorders belong elsewhere, and which are new since
the 2023 revision.

The deliverable is a classification table plus the evidence behind each call, in a form
another curation effort can ingest. This repository has no write access to
`monarch-initiative/dismech`, so the output is staged here for handoff rather than
applied there directly.

## Scope and method

The candidate set was assembled from three public sources and joined by
[`fetch_smd_landscape.py`](SPONDYLOMETAPHYSEAL_DYSPLASIAS/fetch_smd_landscape.py) into
[`smd-landscape.tsv`](SPONDYLOMETAPHYSEAL_DYSPLASIAS/smd-landscape.tsv):

- **MONDO** — every hierarchical descendant of `MONDO:0016763` (spondylometaphyseal
  dysplasia), i.e. what MONDO itself calls an SMD (21 terms), plus two ISDS group-12
  disorders that MONDO does not place in that subtree.
- **Monarch** — the causal gene(s) asserted for each disease.
- **MedGen** — the OMIM entry title for each cross-referenced MIM number, so OMIM naming
  can be compared against the MONDO label.

Each of the 23 resulting disorders was then classified against the 2023 nosology table.
Classification calls are authored, not derived — assigning a nosology group is a
judgement — and each carries its evidence in
[`smd-nosology-classification.tsv`](SPONDYLOMETAPHYSEAL_DYSPLASIAS/smd-nosology-classification.tsv),
with the reasoning in
[per-disorder curation notes](SPONDYLOMETAPHYSEAL_DYSPLASIAS/curation-notes.md).

Actions used: `TAG_GROUP_12` (in the 2023 table as a group-12 disorder),
`PROPOSE_GROUP_12` (new entity proposed for the group), `TAG_OTHER_GROUP` (SMD-named but
the nosology places it elsewhere), `PROVISIONAL_GROUP_12` (gene-less legacy entity, group
assigned on phenotype alone).

## Results

| Action | Disorders |
|---|---|
| `TAG_GROUP_12` | 7 |
| `PROPOSE_GROUP_12` | 1 |
| `TAG_OTHER_GROUP` | 10 |
| `PROVISIONAL_GROUP_12` | 5 |

### Group 12 as it stands in the 2023 nosology

| NOS | Disorder | Gene | MONDO | Inh. |
|---|---|---|---|---|
| 12-0010 | Spondyloenchondrodysplasia with immune dysregulation (SPENCD) | ACP5 | `MONDO:0011939` | AR |
| 12-0020 | Odontochondrodysplasia (ODCD) | TRIP11 | `MONDO:0100325` | AR |
| 12-0030 | SMD Sutcliffe / "corner fracture" type | FN1 | `MONDO:0008479` | AD |
| 12-0040 | SMD with cone-rod dystrophy | PCYT1A | `MONDO:0012160` | AR |
| 12-0050 | SMD with corneal dystrophy | PLCB3 | `MONDO:0030074` | AR |
| 12-0060 | Chondrodysplasia-pseudohermaphroditism (Nivelon-Nivelon-Mabille) | HHAT | `MONDO:0010814` | AR |

Six molecularly unrelated disorders. The group is residual by construction: the nosology
sorts on gene family, severity, and pathogenetic mechanism before it sorts on the
vertebra-plus-metaphysis radiographic pattern, so a TRPV4 SMD goes to group 8, a lethal
SMD to group 14, and a ciliary SMD to group 10. What group 12 keeps is what none of those
axes claims.

### New disorder proposed for the group

**Odontochondrodysplasia 2 with hearing loss and diabetes, MIA3 (TANGO1)-related**
(`MONDO:0031010`, `OMIM:619269`, AR) is absent from the 2023 table and is proposed for
group 12 at MEDIUM confidence.

The case is dyadic-naming symmetry with NOS 12-0020. TRIP11 (GMAP-210, Golgi tethering)
and MIA3 (TANGO1, ER exit site cargo loading) are consecutive steps in bulky-procollagen
export, and both produce odontochondrodysplasia. The first human report
([PMID:32101163](https://pubmed.ncbi.nlm.nih.gov/32101163/)) read as a syndromic collagen-secretion disorder — dentinogenesis
imperfecta, short stature, insulin-dependent diabetes, hearing loss — which plausibly
explains its absence from the 2023 revision. The 2025 spectrum paper ([PMID:40119123](https://pubmed.ncbi.nlm.nih.gov/40119123/))
reframes it, describing metaphyseal dysplasia and scoliosis "closely resembling those
observed in patients with TRIP11 variants". Confidence is held at MEDIUM because the
spectrum has a lethal end; if that end dominates future reports, the severity axis could
pull the entity to group 14 the way it pulled GPX4 and PAM16.

### SMD-named disorders that belong to other groups

Ten disorders carry *spondylometaphyseal* (or sit in MONDO's SMD subtree) but are
classified elsewhere by the nosology — TRPV4 Kozlowski type to group 8; the Sedaghatian
(GPX4), Sedaghatian-like (SBDS) and PAM16 forms to group 14 on severity; axial SMD
(CFAP410, NEK1) to group 10 as a skeletal ciliopathy; LBR regressive SMD to group 13;
PRKG2 to group 16; and the COL2A1 entities (Kniest, SEMD Strudwick, SMD Schmidt type) to
group 2. They are recorded explicitly so they are not re-proposed for group 12.

Two are worth singling out:

- **`MONDO:0008479` (SMD corner-fracture type) is gene-split.** MIM 184255 appears twice
  in the 2023 table: under NOS 12-0030 as the FN1-related disorder, and inside NOS 02-0050
  as "some cases of SMD 'corner fracture type'" with COL2A1. Only the FN1 form is group 12.
  MONDO encodes the same ambiguity by giving the term two parents, SMD and type 2
  collagenopathy.
- **`MONDO:0030487` is a naming conflict.** OMIM titles 619638 "Spondylometaphyseal
  dysplasia, Pagnamenta type" and MONDO follows OMIM; the nosology lists the PRKG2
  disorder once, as an acromesomelic dysplasia, and notes that the SMD-phenotype family is
  exactly that MIM entry. Classified with the nosology, at MEDIUM confidence.

### Unsolved legacy entities

Five MONDO SMD terms have no causal gene (Golden, bowed-forearms/facial dysmorphism, A4,
East African, Czarny-Ratajczak types), so under dyadic naming they have no NOS entry and
no formal group. They are marked `PROVISIONAL_GROUP_12` at LOW confidence: they match the
radiographic definition and fall under the group's closing note on "sporadic patients with
unclassified SMD variants", but a phenotype-only assignment is exactly what a future gene
discovery can overturn — as it would have for Sedaghatian type before GPX4 moved it to
group 14.

## Data-quality findings for upstream resources

Seven actionable items came out of this pass; full statements are in the
[curation notes](SPONDYLOMETAPHYSEAL_DYSPLASIAS/curation-notes.md#data-quality-findings-for-upstream-resources).

- **dismech** — group 12 has no tagged disorders; its description names four exemplars
  and omits NOS 12-0050 (PLCB3) and NOS 12-0060 (HHAT), a known consequence of
  descriptions having been transcribed from the 2019 revision.
- **MONDO** — `MONDO:0030074` (PLCB3) sits directly under *hereditary disease* and is not
  in the SMD subtree at all, despite being an ISDS group-12 disorder whose own label reads
  *spondylometaphyseal dysplasia*; `MONDO:0010814` (HHAT) has no skeletal-dysplasia
  parent; `MONDO:0030487` needs the acromesomelic name as a synonym.
- **Monarch** — `MONDO:0850096` has no causal-gene association despite naming SBDS in its
  label; `MONDO:0011211` (axial SMD) links only CFAP410, not NEK1.

## Gene review status in this repository

Four of the sixteen genes already have GO annotation reviews here, and all four were
checked against this project's scope without needing changes:

| Gene | UniProt | Nosology group |
|---|---|---|
| FN1 | P02751 | 12 (NOS 12-0030) |
| PCYT1A | P49585 | 12 (NOS 12-0040) |
| GPX4 | P36969 | 14 (NOS 14-0030) |
| PAM16 | Q9Y3D7 | 14 (NOS 14-0060) |

(Gene symbols throughout this page link to their reviews where one exists.)

Not yet reviewed, in priority order:

1. **ACP5, TRIP11, PLCB3, HHAT** — the remaining group-12 core. ACP5 and TRIP11 are the
   two best-characterised; PLCB3 completes the phospholipid-signalling pair with PCYT1A.
2. **MIA3** — needed to support the group-12 proposal above, and interesting in its own
   right as the ER-exit-site half of the procollagen-export pair with TRIP11.
3. **SBDS, CFAP410, NEK1, LBR, TRPV4, PRKG2, COL2A1** — boundary genes; useful for the
   group 8/10/13/14/16 calls but not required for group 12.

## Reproducing the raw data

```bash
cd projects/SPONDYLOMETAPHYSEAL_DYSPLASIAS
python3 fetch_smd_landscape.py        # rewrites smd-landscape.tsv
```

Stdlib only, no dependencies. The script queries EBI OLS4, the Monarch v3 API, and NCBI
E-utilities. It deliberately does **not** download or redistribute the ISDS nosology
table, which is published open access by the society at <https://www.isds.ch/>; individual
facts taken from it (NOS identifier, gene, inheritance, MIM number) are cited per row in
the classification table.

`smd-landscape.tsv` records what the sources say;
`smd-nosology-classification.tsv` records what this project concluded. Keeping the two
apart means a source refresh never silently rewrites a curation call.

## Files

- [`smd-nosology-classification.tsv`](SPONDYLOMETAPHYSEAL_DYSPLASIAS/smd-nosology-classification.tsv) — curated classification, 23 disorders
- [`curation-notes.md`](SPONDYLOMETAPHYSEAL_DYSPLASIAS/curation-notes.md) — per-disorder reasoning and citations
- [`smd-landscape.tsv`](SPONDYLOMETAPHYSEAL_DYSPLASIAS/smd-landscape.tsv) — raw MONDO/Monarch/MedGen join
- [`fetch_smd_landscape.py`](SPONDYLOMETAPHYSEAL_DYSPLASIAS/fetch_smd_landscape.py) — regenerates the raw join

## References

- [PMID:36779427](https://pubmed.ncbi.nlm.nih.gov/36779427/) Unger S, et al. Nosology of genetic skeletal disorders: 2023 revision. *Am J Med Genet A*. 2023.
- Per-disorder primary references are cited in the classification table and curation notes.
