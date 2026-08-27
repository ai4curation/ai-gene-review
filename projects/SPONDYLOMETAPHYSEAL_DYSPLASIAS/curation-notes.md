---
title: "Spondylometaphyseal Dysplasias — Per-Disorder Curation Notes"
---

# Spondylometaphyseal dysplasias: per-disorder curation notes

Working notes behind [`smd-nosology-classification.tsv`](smd-nosology-classification.tsv).
Parent project: [Spondylometaphyseal Dysplasias](../SPONDYLOMETAPHYSEAL_DYSPLASIAS.md).

Every classification below is anchored to the ISDS *Nosology of genetic skeletal
disorders: 2023 revision* [PMID:36779427](https://pubmed.ncbi.nlm.nih.gov/36779427/), whose Table 1 is published open access by
the International Skeletal Dysplasia Society at <https://www.isds.ch/>. NOS identifiers
(`NOS 12-0010` and so on) are that table's dyadic entry numbers. Disease identifiers,
cross-references, and gene assertions are as retrieved by
[`fetch_smd_landscape.py`](fetch_smd_landscape.py) into
[`smd-landscape.tsv`](smd-landscape.tsv).

## Why group 12 is small, and what belongs in it

Group 12 is not "everything whose name contains *spondylometaphyseal*". The nosology
sorts on several axes at once, and three of them outrank the vertebra-plus-metaphysis
radiographic pattern:

- **Gene-family grouping wins.** A TRPV4 channelopathy goes to group 8 and a COL2A1
  collagenopathy to group 2 even when the resulting phenotype is called an SMD.
- **Severity wins.** Perinatally lethal platyspondylic disorders go to group 14
  (severe spondylodysplastic dysplasias), which is where the Sedaghatian-type,
  Sedaghatian-like, and PAM16 SMDs sit despite their names.
- **Pathogenetic mechanism wins.** Axial SMD is a skeletal ciliopathy and is filed in
  group 10.

What is left in group 12 is a genuinely residual set: six molecularly unrelated
disorders that share combined vertebral and metaphyseal involvement and are not claimed
by a stronger axis. The group's own closing note in the 2023 table acknowledges the
loose edge, recording that "there are many reports of sporadic patients with
unclassified SMD variants".

## Group 12 members (ISDS 2023)

### NOS 12-0010 — Spondyloenchondrodysplasia with immune dysregulation (SPENCD), ACP5-related

`MONDO:0011939` · `OMIM:607944` · AR · ACP5 (P13686)

Biallelic loss of tartrate-resistant acid phosphatase. Two 2011 *Nature Genetics*
papers established the gene: [PMID:21217752](https://pubmed.ncbi.nlm.nih.gov/21217752/) reported "genetic deficiency of
tartrate-resistant acid phosphatase associated with skeletal dysplasia, cerebral
calcifications and autoimmunity", and [PMID:21217755](https://pubmed.ncbi.nlm.nih.gov/21217755/) independently found that "TRAP
deficiency causes a bone dysplasia with autoimmunity and a type I interferon expression
signature". The skeletal phenotype — platyspondyly with metaphyseal enchondroma-like
lucencies — is what earns the group-12 placement; the interferonopathy is what makes it
a dismech-relevant mechanism entry.

The MONDO term carries two OMIM xrefs (`OMIM:271550`, `OMIM:607944`) and two Orphanet
xrefs (`Orphanet:1855`, `Orphanet:50816`), a merge of the older spondyloenchondrodysplasia
and immune-dysregulation entries.

### NOS 12-0020 — Odontochondrodysplasia (ODCD), TRIP11-related

`MONDO:0100325` · `OMIM:184260` · AR · TRIP11 (Q15643)

[PMID:30728324](https://pubmed.ncbi.nlm.nih.gov/30728324/) showed ODCD is caused by *hypomorphic* TRIP11 variants and identified it
as "the nonlethal counterpart to achondrogenesis 1A (ACG1A), the known null phenotype in
humans". [PMID:31903676](https://pubmed.ncbi.nlm.nih.gov/31903676/) confirmed the allelic series. TRIP11 encodes GMAP-210, a
Golgi-associated microtubule-binding protein, so the two ends of the series sit in
different nosology groups by severity: ODCD in group 12, TRIP11 achondrogenesis 1A at
NOS 14-0010 in group 14. A dismech mechanism entry for either should cross-reference the
other rather than treat them as unrelated.

### NOS 12-0030 — SMD Sutcliffe / "corner fracture" type, FN1-related

`MONDO:0008479` · `OMIM:184255` · AD · FN1 (P02751)

[PMID:29100092](https://pubmed.ncbi.nlm.nih.gov/29100092/) identified heterozygous FN1 variants as the cause. This entity is
**gene-split in the nosology**, and the split is the single most error-prone call in this
group: MIM 184255 appears twice in the 2023 table — under NOS 12-0030 (FN1-related, with
the note that "some cases are linked to COL2A1 but not the original family") and again
inside NOS 02-0050 (SEMD, COL2A1-related, "includes … some cases of SMD 'corner fracture
type'"). Only the FN1-related form is a group-12 disorder.

MONDO encodes the same ambiguity structurally: `MONDO:0008479` has two parents,
`MONDO:0016763` (SMD) and `MONDO:0022800` (type 2 collagenopathy). The dismech enum
already records `MONDO:0022800` as a rejected mapping candidate for group 2 *because* it
contains this term — consistent with, and explained by, the gene split.

### NOS 12-0040 — SMD with cone-rod dystrophy, PCYT1A-related

`MONDO:0012160` · `OMIM:608940` · AR · PCYT1A (P49585)

Two 2014 *AJHG* papers reported the gene simultaneously ([PMID:24387991](https://pubmed.ncbi.nlm.nih.gov/24387991/),
[PMID:24387990](https://pubmed.ncbi.nlm.nih.gov/24387990/)). PCYT1A encodes CCTα, the rate-limiting and regulated enzyme of the
CDP-choline (Kennedy) pathway of phosphatidylcholine synthesis; PCYT1A already has a
GO annotation review in this repository.

### NOS 12-0050 — SMD with corneal dystrophy, PLCB3-related

`MONDO:0030074` · `OMIM:618961` · AR · PLCB3 (Q01970)

[PMID:29122926](https://pubmed.ncbi.nlm.nih.gov/29122926/) reported "a new form of syndromic autosomal recessive spondylometaphyseal
dysplasia (SMD) in two Emirati first cousins" with "radiological abnormalities involving
the spine, pelvis and metaphyses, corneal clouding and intellectual disability", caused by
a hypomorphic PLCB3 variant. Notably, the authors reached PLCB3 *because* of the
phospholipid precedent: "pathogenic variants in genes involved in phospholipid metabolism,
such as PLCB4 and PCYT1A, are known to cause bone dysplasia with or without eye anomalies".

Group 12 therefore contains two phospholipid-signalling SMDs with eye involvement
(PCYT1A, PLCB3) — the closest thing this residual group has to a shared mechanism, and
worth flagging for dismech as a mechanism cluster rather than a coincidence.

**Two gaps found here.** (1) The disorder is missing from the dismech group-12
description, which names only ACP5, TRIP11, FN1 and PCYT1A. (2) In MONDO the term's only
parent is `MONDO:0003847` (hereditary disease), so it is *not* reachable from
`MONDO:0016763` and does not appear in a MONDO-driven SMD listing at all.

### NOS 12-0060 — Chondrodysplasia-pseudohermaphroditism (Nivelon-Nivelon-Mabille), HHAT-related

`MONDO:0010814` · `OMIM:600092` · AR · HHAT (Q5VTY9)

[PMID:24784881](https://pubmed.ncbi.nlm.nih.gov/24784881/) showed loss of function in the palmitoyl-transferase HHAT "leads to
syndromic 46,XY disorder of sex development by impeding Hedgehog protein palmitoylation
and signaling"; [PMID:40326711](https://pubmed.ncbi.nlm.nih.gov/40326711/) adds four patients with "46,XY gonadal dysgenesis,
microcephaly, microphthalmia, ocular coloboma, skeletal dysplasia, and cerebellar vermis
hypoplasia".

This is the least phenotype-obvious member of the group: it presents as a multiple
congenital anomaly syndrome, not as a classical SMD. The group-12 placement is the
nosology's own (NOS 12-0060) and is followed here, but it is recorded as a
nosology-authority call rather than a radiographic one. Like PLCB3 it is absent from the
dismech group-12 description, and in MONDO it has no skeletal-dysplasia parent at all
(parents are syndromic disease, hereditary disease, and 46,XY DSD).

## New disorder proposed for group 12

### Odontochondrodysplasia 2 with hearing loss and diabetes, MIA3 (TANGO1)-related

`MONDO:0031010` · `OMIM:619269` · AR · MIA3 (Q5JRA6) · **not in the 2023 nosology table**

[PMID:32101163](https://pubmed.ncbi.nlm.nih.gov/32101163/) reported the first TANGO1-associated syndrome in humans: four
homozygously affected brothers with "severe dentinogenesis imperfecta, short stature,
various skeletal abnormalities, insulin-dependent diabetes mellitus, sensorineural
hearing loss, and mild intellectual disability", with functional work showing the
truncated protein "impairs cellular collagen I secretion". At that point the entity read
as a syndromic collagen-secretion disorder rather than a named skeletal dysplasia, which
is plausibly why the 2023 revision does not carry it.

[PMID:40119123](https://pubmed.ncbi.nlm.nih.gov/40119123/) reframes it. Two further unrelated patients had "severe short limbs,
short stature, metaphyseal dysplasia, dysmorphic facies, lax joints, and DI", variably
with scoliosis, and — decisively for classification — "more severe skeletal deformities
closely resembling those observed in patients with TRIP11 variants". OMIM titles the
entry "Odontochondrodysplasia 2 with hearing loss and diabetes"; MONDO makes it a child
of `MONDO:0031169` odontochondrodysplasia alongside ODCD1.

**Recommendation: tag `spondylometaphyseal_dysplasias`, confidence MEDIUM.** The
argument is dyadic-naming symmetry with NOS 12-0020: TRIP11 (GMAP-210, Golgi tethering)
and MIA3 (TANGO1, ER exit site cargo loading) are consecutive steps in bulky-procollagen
export, and both produce odontochondrodysplasia. The confidence is MEDIUM rather than
HIGH only because the phenotypic spectrum has a lethal end ([PMID:40119123](https://pubmed.ncbi.nlm.nih.gov/40119123/) cites a fetus
with lethal skeletal dysplasia and hydrops); if that end dominates future reports, the
severity axis could pull the entity toward group 14 the way GPX4 and PAM16 were pulled.

`MONDO:0031169` (odontochondrodysplasia, `OMIMPS:184260`) is the grouping class over
ODCD1 and ODCD2. Both members resolve to group 12, so the grouping term can carry the
same tag if dismech curates grouping classes.

## SMD-named disorders that belong to other groups

Recorded so they are not re-proposed for group 12.

| Disorder | Gene | ISDS | dismech value | Why not group 12 |
|---|---|---|---|---|
| SMD Kozlowski type | TRPV4 | NOS 08-0030 | `trpv4` | Gene-family axis. Already tagged in dismech. [PMID:19232556](https://pubmed.ncbi.nlm.nih.gov/19232556/) |
| Severe SMD, Sedaghatian type | GPX4 | NOS 14-0030 | `severe_spondylodysplastic_dysplasias` | Severity axis; perinatally lethal. [PMID:24706940](https://pubmed.ncbi.nlm.nih.gov/24706940/) |
| Severe neonatal SMD, Sedaghatian-like | SBDS | NOS 14-0040 | `severe_spondylodysplastic_dysplasias` | Severity axis. [PMID:17400792](https://pubmed.ncbi.nlm.nih.gov/17400792/) |
| SMD Megarbane-Dagher-Melki type | PAM16 | NOS 14-0060 | `severe_spondylodysplastic_dysplasias` | Severity axis. [PMID:24786642](https://pubmed.ncbi.nlm.nih.gov/24786642/) |
| Axial SMD | CFAP410, NEK1 | NOS 10-0340/0350 | `ciliopathies_with_major_skeletal_involvement` | Mechanism axis; skeletal ciliopathy. [PMID:26974433](https://pubmed.ncbi.nlm.nih.gov/26974433/), [PMID:28123176](https://pubmed.ncbi.nlm.nih.gov/28123176/) |
| Rhizomelic SMD with remission (regressive SMD) | LBR | NOS 13-0310 | `spondylo_epi_metaphyseal_dysplasias` | Epiphyseal involvement plus anadysplasia-like course. [PMID:25348816](https://pubmed.ncbi.nlm.nih.gov/25348816/) |
| SMD Pagnamenta type | PRKG2 | NOS 16-0020 | `acromesomelic_dysplasias` | Segment axis; see naming conflict below. [PMID:33106379](https://pubmed.ncbi.nlm.nih.gov/33106379/) |
| SMD Schmidt type | COL2A1 | NOS 02-0050 | `type_2_collagen` | Gene-family axis; MIM 184253 folded into COL2A1 SEMD |
| SEMD Strudwick type | COL2A1 | NOS 02-0050 | `type_2_collagen` | Gene-family axis. Already tagged in dismech |
| Kniest dysplasia | COL2A1 | NOS 02-0060 | `type_2_collagen` | Gene-family axis. Already tagged in dismech |

Three of these need a comment.

**SBDS (NOS 14-0040).** [PMID:17400792](https://pubmed.ncbi.nlm.nih.gov/17400792/) describes two patients whose "neonatal skeletal
manifestations … included platyspondyly, lacy iliac crests and severe metaphysial
dysplasia, and thus did not fall in the range of the known Shwachman-Diamond syndrome
skeletal phenotype but resembled spondylometaphysial dysplasia (SMD) Sedaghatian type".
The same gene therefore appears twice in the nosology — NOS 11-0050 (Shwachman-Bodian-Diamond
syndrome, group 11) and NOS 14-0040 — which is exactly the dyadic system working as
intended and a case where a dismech mechanism entry should span both. Separately, Monarch
holds **no** causal-gene association for `MONDO:0850096` even though the label names SBDS.

**PRKG2 (NOS 16-0020) — naming conflict.** OMIM titles 619638 "Spondylometaphyseal
dysplasia, Pagnamenta type" and MONDO follows OMIM, which is why `MONDO:0030487` surfaces
in an SMD query at all. The nosology lists the PRKG2 disorder once, as "Acromesomelic
dysplasia, PRKG2-related", against both MIM 619636 and 619638, and notes explicitly that
the three brothers reported with a spondylo-metaphyseal phenotype are the 619638 entry.
The primary report [PMID:33106379](https://pubmed.ncbi.nlm.nih.gov/33106379/) describes "a novel acromesomelic dysplasia". Classified
with the nosology; the SMD label is retained in the table only so the conflict is visible.

**TRPV4 (NOS 08-0030) — label drift.** The 2023 table names this row "Spondyloepiphyseal
dysplasia, Kozlowski type" while OMIM (184252), MONDO and the dismech group-8 description
all say *spondylometaphyseal*. No classification consequence — group 8 either way — but
a string match on the nosology text will miss it.

## Unsolved legacy SMD entities

Five MONDO terms in the SMD subtree have no causal gene, so under dyadic naming they have
no NOS entry and no formal group:

| Disorder | MONDO | OMIM / Orphanet |
|---|---|---|
| SMD, Golden type | `MONDO:0010738` | `OMIM:313420`, `Orphanet:168544` |
| SMD with bowed forearms and facial dysmorphism | `MONDO:0011856` | `OMIM:607543`, `Orphanet:168552` |
| SMD, A4 type | `MONDO:0012185` | `OMIM:609052`, `Orphanet:168555` |
| SMD, East African type | `MONDO:0012713` | `OMIM:611702` |
| SMD, Czarny-Ratajczak type | `MONDO:0018255` | `Orphanet:370019` |

They are marked `PROVISIONAL_GROUP_12` at LOW confidence: they match the group's
radiographic definition and are covered by its closing note on unclassified SMD variants,
but a group assignment for a gene-less entity is a phenotype call that a future gene
discovery can overturn — as it would have for Sedaghatian type, which looked like a
classical SMD until GPX4 moved it to group 14 on severity.

The A4 type has a follow-up report, [PMID:22528043](https://pubmed.ncbi.nlm.nih.gov/22528043/) ("A new form or a variant of SMD type
A4"). For the Czarny-Ratajczak type, the defining report [PMID:19764033](https://pubmed.ncbi.nlm.nih.gov/19764033/) is explicit that
the gene is unknown: molecular analysis "excluded" COL2A1, PTH1R was also analysed with no
mutation found, and the authors conclude "a new candidate gene for the reported form of
SMD should be sought". Pedigree data indicated autosomal recessive inheritance.

## Data-quality findings for upstream resources

Actionable items generated by this pass, kept separate from the classification itself.

**dismech (`ISDSNosologyGroupEnum`)**
1. `spondylometaphyseal_dysplasias` has **no tagged disorders**, while its neighbouring
   groups all do. The 23-row table here is the candidate set.
2. The group-12 description names four exemplars (ACP5, TRIP11, FN1, PCYT1A) and omits
   NOS 12-0050 (PLCB3) and NOS 12-0060 (HHAT). This is the documented consequence of the
   enum's known gap — descriptions were transcribed from the 2019 revision and corrected
   only selectively — so it is a description fix, not a membership dispute.

**MONDO**
3. `MONDO:0030074` (SMD with corneal dystrophy, PLCB3) has only `MONDO:0003847`
   (hereditary disease) as a parent. It is an ISDS group-12 disorder with
   *spondylometaphyseal dysplasia* in its own label and should be classified under
   `MONDO:0016763`.
4. `MONDO:0010814` (chondrodysplasia-pseudohermaphroditism, HHAT) has no skeletal
   dysplasia parent. Weaker case than (3), since the phenotype is syndromic, but the
   nosology does file it as a skeletal dysplasia.
5. `MONDO:0030487` inherits the OMIM title "spondylometaphyseal dysplasia, Pagnamenta
   type" for what the nosology treats as an acromesomelic dysplasia. Worth at least an
   exact-synonym for the acromesomelic name.

**Monarch associations**
6. `MONDO:0850096` (SBDS-related severe neonatal SMD) has no causal-gene association
   despite naming SBDS in its label; the supporting report is [PMID:17400792](https://pubmed.ncbi.nlm.nih.gov/17400792/).
7. `MONDO:0011211` (axial SMD) links only CFAP410. NEK1 causes the same entity
   ([PMID:28123176](https://pubmed.ncbi.nlm.nih.gov/28123176/)) and is listed separately in the nosology as NOS 10-0350.
