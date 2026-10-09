---
title: "Neural Crest Formation (GO:0014029) — Obsoletion Proposal"
maturity: SCOPING
tags: [OBSOLETION]
species: [XENLA, human]
genes: [pax3-a, zic1, gbx2, MSX1, PAX7, TFAP2A, TFAP2C, hes4-a, id3-a, myc-a, pou5f1.1, sox8, sox9-a, sox10, snai1, snai2, twist1, LRP6]
---

# Neural Crest Formation (GO:0014029) — Obsoletion Proposal

**Bottom line:** we propose to obsolete GO:0014029 *neural crest formation*
and its three regulation terms. We also propose two new terms, *neural plate
border formation* and *neural crest progenitor maintenance*. GO:0014029 contradicts itself: its text defines forming *a region of
ectoderm* (the neural plate border), while its place in GO is under *epithelial
to mesenchymal transition*. The 1,454 annotations to it therefore have no single
meaning. They mix border specifiers, crest specifiers, competence factors,
signalling modulators and ribosome-biogenesis genes. 1,322 of them (91%) are
electronic, and one machine-learned UniProt rule (ARBA00027170) alone produces
665. Only 84 rows are experimental (48 gene products, 36 papers). Each of these
can be remapped to a precise existing term, or to one of the two new terms. This
project holds the case, the replacement rules, the remapping of every
experimental annotation, and the draft GO request. It originated in the
[Origins of the Neural Crest](NEURAL_CREST_ORIGINS.md) project. Nothing has
been submitted to GO yet.

## The defect

GO:0014029 *neural crest formation* (checked against QuickGO and OLS, 2026-10-09):

- **Text definition:** "The formation of the specialized region of ectoderm
  between the neural ectoderm (neural plate) and non-neural ectoderm. The neural
  crest gives rise to the neural crest cells that migrate away from this region
  as neural tube formation proceeds." This describes forming the **neural plate
  border region**.
- **Placement:** `is_a` GO:0001837 *epithelial to mesenchymal transition*;
  ancestors include GO:0048762 *mesenchymal cell differentiation* and GO:0060485
  *mesenchyme development*. This describes **making migratory crest cells**.
- **Children:** GO:0014034 *neural crest cell fate commitment* is `part_of`
  both GO:0014029 and GO:0014033 *neural crest cell differentiation*, and
  GO:0014036 *fate specification* is `part_of` GO:0014034.

The two readings pick out different genes. A border specifier such as Gbx2,
Msx1 or Pax7 builds the border territory but does no EMT. A competence factor
such as Id3 or Myc keeps crest progenitors undifferentiated and does neither.
Both are annotated to the same term as Sox10. The evolutionary data make the
split unavoidable. Amphioxus and tunicates have a neural plate border, with
Pax3/7, Msx and Zic expressed there [PMID:18562679], but no neural crest. Border
formation cannot be part of neural crest formation.

## How the term is used

Inventory from QuickGO, exact annotations only (`inventory.py`; full rows in
`NEURAL_CREST_FORMATION_OBSOLETION/annotations.tsv`, counts in
`NEURAL_CREST_FORMATION_OBSOLETION/summary.md`):

| Term | Rows | Experimental | Notes |
|---|---:|---:|---|
| GO:0014029 neural crest formation | 1,454 | 84 (48 products, 36 refs) | IEA 1,322; no IBA; 40 rows `acts_upstream_of_or_within`, 1 NOT |
| GO:0090299 regulation of neural crest formation | 8 | 8 | zebrafish hdac4, parp3 (ZFIN) |
| GO:0090300 positive regulation of neural crest formation | 2 | 2 | chick Id2 (IEP), SOX9 (IMP) |
| GO:0090301 negative regulation of neural crest formation | 7 | 4 | zebrafish rgs2, TSPAN18, Fuz (+ISS/ISO) |

Where the electronic rows come from:

- **ARBA:ARBA00027170 (GO_REF:0000117), 665 rows.** One UniProt rule with six
  unrelated condition sets: Zic-type C2H2 zinc fingers, HMG box (Sox),
  winged-helix (Fox/Ets), BTB-kelch and others, each restricted to Amphibia,
  Anura, Pipoidea, Pipidae or Craniata. It learns "is a crest gene" across all
  network layers and writes one term for all of them.
- **Ensembl Compara orthology (GO_REF:0000107), 570 rows,** and the combined
  automatic pipeline (GO_REF:0000120), 87 rows, propagating from the
  experimental rows below.

No production GO-CAM in the local cache (`gocams/`) uses any of the four terms.

## Proposed changes

1. **New term: neural plate border formation.** "The formation of the neural
   plate border, the region of ectoderm at the boundary between the neural plate
   and the non-neural ectoderm that is competent to give rise to neural crest,
   preplacodal ectoderm, dorsal neural tube and epidermis." Proposed `part_of`
   GO:0007398 *ectoderm development*. It should not sit under any crest or
   mesenchyme term.
2. **New term: neural crest progenitor maintenance.** "The process by which
   neural plate border and premigratory neural crest progenitor cells are kept in
   an undifferentiated, proliferative and multipotent state until neural crest
   specification." Proposed `is_a` GO:0019827 *stem cell population
   maintenance*. It is for competence factors such as Myc, Id3, Hairy2 and
   Pou5f3/Oct25. These are required for crest to form, but their loss causes
   progenitor arrest or death rather than a change of fate, and sustained Id3
   blocks differentiation.
3. **Obsolete GO:0014029.** Replacements to suggest ("consider"): neural plate
   border formation (new), neural crest progenitor maintenance (new), GO:0014033 *neural crest cell differentiation*,
   GO:0014034 *fate commitment*, GO:0014036 *fate specification*, GO:0036032
   *delamination*. GO:0014034 keeps its existing `part_of` GO:0014033.
4. **Obsolete the regulation terms**, replaced by the existing regulation
   terms for crest cell differentiation:

| Obsoleted | Replaced by |
|---|---|
| GO:0090299 regulation of neural crest formation | GO:1905292 regulation of neural crest cell differentiation |
| GO:0090300 positive regulation of neural crest formation | GO:1905294 positive regulation of neural crest cell differentiation |
| GO:0090301 negative regulation of neural crest formation | GO:1905293 negative regulation of neural crest cell differentiation |

## Replacement rule for existing annotations

Decide each annotation by what the gene product *does*, using the layers worked
out in [NEURAL_CREST_ORIGINS](NEURAL_CREST_ORIGINS.md) and the
[neural crest GRN module](../modules/neural_crest_gene_regulatory_network.yaml):

| The gene product… | Replacement |
|---|---|
| builds the border territory (border specifier) | neural plate border formation (new) |
| … and directly drives crest fate from the border | also GO:0014034 fate commitment |
| confers crest identity within the prospective crest | GO:0014036 fate specification |
| keeps border/crest progenitors undifferentiated and competent | neural crest progenitor maintenance (new) |
| drives delamination | GO:0036032 delamination |
| is only expressed there (IEP) | no process replacement; expression is not participation |
| modulates an inducing signal (BMP/Wnt antagonist or receptor) | regulation term on the signal, or border formation if the evidence supports it; review case by case |

**Competence factors (decided 2026-10-09).** Three options were considered:
(a) GO:0014033 *neural crest cell differentiation*; (b) a new term; (c)
GO:0019827 *stem cell population maintenance*. Option (b) was chosen. (a) is
awkward for factors that hold off differentiation. (c) is too general to say
which population is maintained, and the lin28a review judged it unsupported for
lin28 in frog.

## Remapping of every experimental annotation

`NEURAL_CREST_FORMATION_OBSOLETION/remapping.tsv` has one row per distinct GOA
annotation: all 84 experimental GO:0014029 rows plus the 17 regulation-term
rows (12 distinct). That is 94 rows and 62 distinct gene–paper decisions. Each
row gives an action, replacement ids and labels, a rationale and a verbatim
quote. Every quote and every replacement id passes `check_remap.py` (live GO
terms with matching labels, quotes found in the cached papers). The table is
assembled by `merge_remap.py` from four review batches (`remap/*.tsv`, each with
a `.notes.md`) and from the gene reviews already in this repo.

| Action | Rows | Distinct decisions |
|---|---:|---:|
| REPLACE | 86 | 55 |
| REMOVE (expression only) | 3 | 2 |
| UNDECIDED | 5 | 5 |

Decisions by gene (species; paper):

| Replacement | Gene products |
|---|---|
| Neural plate border formation (new) + GO:0014034 fate commitment | pax3-a, pax3-b, zic1, zic2-a, zic4, zic5 (X. laevis) |
| Neural plate border formation (new) | mdkb (zebrafish; its abstract says it is "responsible for establishment of the neural plate border") |
| Neural plate border formation (new) + GO:1905297 positive regulation of NC fate specification | snw1 (zebrafish; sets BMP activity at the border) |
| Neural crest progenitor maintenance (new) | hes4-a, hes4-b, id3-a (X. laevis) |
| GO:0014036 fate specification | sox8 (+ GO:0001755), sox9-a, sox10 (X. laevis); sox9 (X. tropicalis); sox10 (zebrafish); KBTBD8, TCOF1, NOLC1 (human) and kbtbd8 (X. tropicalis) |
| GO:0036032 delamination | SOX9 (chicken; replaces positive regulation of NC formation) |
| GO:0014033 differentiation (nothing more specific supported) | zeb2a, zeb2b, cnbpa, chd7 (zebrafish) |
| Regulation of NC fate specification (GO:1905295/6/7) | parp3; rgs2 (negative); hsbp1b (negative); bmper (positive, + GO:0030513 positive regulation of BMP signaling) |
| Regulation of NC differentiation (GO:1905292/3/4) | hdac4; Fuz/FUZ (negative; mouse IMP plus rat/human transfers); LRP6 (human, positive) |
| Other existing terms | TSPAN18 (chicken) → GO:0010719 negative regulation of epithelial to mesenchymal transition; polr1b (zebrafish) → GO:0006360 transcription by RNA polymerase I |
| REMOVE (expression only) | grem1 (X. laevis, IEP); Id2 (chicken, IEP, on both GO:0014029 and GO:0090300) |
| UNDECIDED | KLHL12, PEF1, PDCD6 (human; PMID:27716508 full text not accessible); Chrd (mouse; the cached abstract concerns vascular patterning); hes4-a NOT row (contradicted by PMID:25997789) |

What the remapping shows:
- **Only 14 of 94 rows land on a precise crest-cell term** (fate
  specification or delamination): the SoxE genes, the ubiquitin group and SOX9.
  The rest move to the border term (14), the progenitor term (11), a regulation
  term (14), the general differentiation term (32, of which 28 are zeb2
  accessions from one paper) or a non-crest term (polr1b), or are removed or left
  undecided. The obsoleted term was carrying all of these meanings.
- **Ribosome biogenesis is split on purpose.** polr1b knockdown makes crest
  precursors die from a ribosome shortage, which is a requirement, not a crest
  step. TCOF1 and NOLC1 knockdown switches cells from crest to CNS identity
  without affecting rRNA output or survival, which is participation in
  specification [PMID:26399832].
- **GO lacks regulation terms for crest migration and delamination.** TSPAN18
  therefore goes to a generic EMT term. A follow-up request for "negative
  regulation of neural crest cell delamination" may be worth making.
- **Weaker calls flagged in the notes:** the Zic2/4/5 evidence is mostly
  overexpression; zeb2 and cnbpa rest on abstracts; rgs2 rests on its abstract
  only; for KBTBD8, GO:1905297 (regulation) is a defensible alternative to
  GO:0014036.

## Impact on this repo

18 gene reviews mention one of the four terms (2026-10-09):

- **Border specifiers, done.** gbx2, MSX1, PAX7, TFAP2A and TFAP2C: NEW rows
  now point to the proposed term (`id: NTR`). pax3-a and zic1: their GOA
  GO:0014029 rows are MODIFY → NTR (+ GO:0014034). All seven carry a
  `proposed_new_terms` entry. Applied with
  `NEURAL_CREST_FORMATION_OBSOLETION/apply_border_ntr.py`.
- **Crest specifiers, already consistent.** sox8, sox9-a, sox10, snai1, snai2
  and twist1 MODIFY their GO:0014029 rows to GO:0014036.
- **Competence factors, done.** hes4-a and id3-a: their GOA GO:0014029 rows
  are MODIFY → NTR *neural crest progenitor maintenance*. myc-a and pou5f1.1:
  NEW rows re-pointed to it. All four carry a `proposed_new_terms` entry.
  Applied with `apply_border_ntr.py --competence`.
- **Outside the crest project.** human LRP6 keeps GO:0014029 (IDA,
  PMID:11029007) as non-core. Revisit it with the signalling-modulator group.
- lin28a, sox2, sox3-a and TFAP2B mention the term only in prose.

## Draft request to GO (not submitted)

> **Obsolete GO:0014029 neural crest formation (and GO:0090299/0090300/0090301); add "neural plate border formation" and "neural crest progenitor maintenance"**
>
> GO:0014029 is defined as "the formation of the specialized region of ectoderm
> between the neural ectoderm (neural plate) and non-neural ectoderm", but it is
> `is_a` GO:0001837 epithelial to mesenchymal transition. The definition
> describes the neural plate border, a territory that also gives rise to
> preplacodal ectoderm, dorsal neural tube and epidermis, and that exists in
> chordates without neural crest (amphioxus, tunicates). The placement describes
> the generation of migratory crest cells. Current annotations (1,454; 84
> experimental) mix border specifiers (Pax3, Zic), crest specifiers (SoxE),
> competence factors (Id3, Hairy2) and others; 665 come from a single ARBA rule
> spanning unrelated families.
>
> Proposal: (1) new BP "neural plate border formation", part_of GO:0007398
> ectoderm development; (2) new BP "neural crest progenitor maintenance",
> is_a GO:0019827 stem cell population maintenance, for factors that keep
> border/crest progenitors undifferentiated and competent (Myc, Id3, Hairy2,
> Pou5f3); (3) obsolete GO:0014029 with consider: the two new terms, GO:0014033,
> GO:0014034, GO:0014036, GO:0036032; (4) obsolete GO:0090299, GO:0090300 and
> GO:0090301, replaced by GO:1905292, GO:1905294 and GO:1905293.
> A per-annotation remapping of the 84 experimental annotations is attached.

---
# STATUS

Last updated: 2026-10-09

- [x] Defect documented (text vs placement), checked in QuickGO and OLS
- [x] Inventory of all annotations to the four terms (`inventory.py`, `annotations.tsv`, `summary.md`)
- [x] Source of the electronic bulk identified (ARBA00027170; Ensembl orthology)
- [x] Replacement rule drafted; regulation-term mappings identified
- [x] Border-specifier reviews in this repo moved to the proposed term (7 reviews)
- [x] Competence-factor replacement decided: new term *neural crest progenitor maintenance* (2026-10-09)
- [x] Applied to hes4-a, id3-a, myc-a, pou5f1.1; module competence part updated
- [x] Review the remaining experimental annotations (four batches; 2026-10-09)
- [x] Review the 17 regulation-term annotations (12 distinct)
- [x] Per-annotation remapping table for GO (`remapping.tsv`, 94 rows, checker clean)
- [ ] Resolve the 5 UNDECIDED rows (needs PMID:27716508 full text; Chrd full text; hes4-a NOT row)
- [ ] Consider a request for "negative regulation of neural crest cell delamination"
- [ ] Report ARBA00027170 to UniProt (see the rule-reviewer workflow)
- [ ] Submit the GO request (needs sign-off)

# NOTES

## 2026-10-09 (remapping)

Four review batches covered the remaining 72 distinct rows, and 22 more rows
were taken from the existing gene reviews. Result: 94 rows, 62 distinct
gene–paper decisions (55 replace, 2 remove, 5 undecided). All quotes and ids
pass `check_remap.py`. Spot checks by the coordinator: GO:0044335 (Wnt in crest
differentiation) is indeed obsolete, which is why LRP6 maps to GO:1905294; and
the chicken SOX9 paper's title and text support delamination. Inventory
coverage was checked: every experimental and regulation row is in the table.

## 2026-10-09 (later)

Decided option (b) for competence factors: a second new term, *neural crest
progenitor maintenance* (is_a GO:0019827). Applied to the four competence
reviews and to the module. No GO:0014029 term IDs remain in the module or in
the project's core functions. The 4 competence reviews and the 7 border
reviews still have GOA rows on GO:0014029, now MODIFY to an NTR, which is the
intended state until GO acts.

## 2026-10-09

Project created from the NEURAL_CREST_ORIGINS convention discussion. The
earlier convention (border and competence genes at GO:0014029, specifiers at
GO:0014036) used the term's text definition. Checking its placement showed the
text and placement disagree, so the term itself was judged unfit and an
obsoletion was proposed rather than a definition fix. Inventory run: 1,471 rows
across the four terms. All 665 ARBA rows come from ARBA00027170, whose six
condition sets span Zic, SoxE, Fox/Ets and kelch families.
