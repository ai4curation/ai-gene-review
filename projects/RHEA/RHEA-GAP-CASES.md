---
title: "RHEA Gap Case Reviews: Swiss-Prot RHEA, No Mapping, Missing/High-Level GO"
species: [human]
genes: [PHYKPL, B3GALNT2, SAMD8, SULT6B1]
---

# RHEA Gap Case Reviews

**Parent project:** [RHEA.md](../RHEA.md) · **Background:** [RHEA-EC-SPECIFICITY.md](RHEA-EC-SPECIFICITY.md)

These are reviews of concrete cases of gap class **G4/G6**: a reviewed
(Swiss-Prot) human enzyme carries an **experimentally or curator-asserted RHEA
reaction**, that reaction has **no `rhea2go` mapping**, and as a result the
protein's GO **molecular function is missing or only ultra-high-level**. They
were drawn from the reproducible candidate set built by
[`rhea_gap_finder.py`](rhea_gap_finder.py) (stream reviewed human enzymes → keep
those whose every annotated RHEA is absent from `rhea2go` and that carry a
complete EC → **115 human enzymes**). Of those, the finder's strict filter (MF
*catalytic* terms absent or only enzyme-class roots, ignoring cofactor "binding"
terms) auto-flags the root/class cases **PHYKPL** and **SULT6B1**; **B3GALNT2**
and **SAMD8** were selected by inspecting the same 115-entry list for enzymes
whose only activity term is a too-general class term or an off-target activity.
Each case was then verified by hand against UniProt, the `rhea2go`/`ec2go`
mappings, and a QuickGO term search.

Every identifier below is checkable: the RHEA id and reaction come from the
UniProtKB `CC -!- CATALYTIC ACTIVITY` line; the "no mapping" claim was confirmed
against the public `rhea2go` file; the "current GO MF" is the molecular-function
subset of the entry's GOA terms; "specific term exists?" is a QuickGO search.

## Summary

| Gene | UniProt | RHEA (unmapped) | EC | Current GO MF | Specific GO term exists? | Action |
|------|---------|-----------------|----|---------------|--------------------------|--------|
| **PHYKPL** | Q8IUZ5 | RHEA:34091 | 4.2.3.134 | only `lyase activity` (GO:0016829, **root**) | **No** | MODIFY off root + **propose NEW** term |
| **B3GALNT2** | Q8NCR0 | RHEA:37667 | 2.4.1.313 | only class-level GalNAc-T terms | **No** (no β1,3-specific term) | **propose NEW** term |
| **SAMD8** (SMSr) | Q96LT4 | RHEA:36079* | 2.7.8.- | `hydrolase activity` + SM-synthase terms | **Yes — GO:0002950 exists, not applied** | **ADD GO:0002950**; drop `hydrolase activity` |
| **SULT6B1** | Q6IMI4 | RHEA:26422 | 2.8.2.n2 | only `sulfotransferase activity` (GO:0008146, class) | partial (`aryl sulfotransferase` GO:0004062) | MODIFY (cautious) / UNDECIDED |

\* SAMD8 carries several unmapped RHEA reactions; RHEA:36079 is the
ceramide-phosphoethanolamine synthase reaction that defines its function.

These four span the gap taxonomy: a **GO granularity gap** where no term exists
(PHYKPL, B3GALNT2), a **clean propagation gap** where the right term already
exists but never reached the protein (SAMD8), and an **evidence-limited** gap
where the fill is real but the confidence is lower (SULT6B1).

---

## PHYKPL — 5-phosphohydroxy-L-lysine phospho-lyase (Q8IUZ5)

- **RHEA:34091** (`O-phosphohydroxy-L-lysine = (S)-1-pyrroline-... + NH4(+) + phosphate`), EC 4.2.3.134.
- **rhea2go:** no mapping. **ec2go:** EC 4.2.3.134 has no `ec2go` line either.
- **Current GO MF:** `GO:0016829 lyase activity` (the lyase root), plus
  `pyridoxal phosphate binding` and `identical protein binding`. So the *only*
  catalytic GO term is the top of the lyase branch — maximally uninformative.
- **Evidence:** human enzyme experimentally characterised — catalytic activity,
  cofactor (PLP) and kinetics in PubMed:22241472 (UniProt `ECO:0000269`). This is
  the gene mutated in phosphohydroxylysinuria.

**Assessment.** Neither GO pipeline can lift this protein off `lyase activity`:
RHEA has the precise reaction but it is unmapped, and the EC is absent from
`ec2go`. A QuickGO search finds **no** GO term for this activity (the nearest
analogue is `GO:0050459 ethanolamine-phosphate phospho-lyase activity`, a sibling
pyridoxal-phosphate phospho-lyase). The biology is solid and specific; GO simply
lacks the node.

**Action.**
- `MODIFY` the existing `GO:0016829 lyase activity` annotation — it is correct but
  far too high-level to be the protein's curated function.
- **`proposed_new_terms`:** *5-phosphooxy-L-lysine phospho-lyase activity* (a.k.a.
  5-phosphohydroxy-L-lysine ammonia-(phosphate)-lyase), placed in the
  carbon-oxygen / phospho-lyase grouping that already contains the sibling
  `GO:0050459 ethanolamine-phosphate phospho-lyase activity`; definition tied to
  RHEA:34091 and EC 4.2.3.134. This is the right long-term fix and would let the
  RHEA pipeline propagate it.

This is the cleanest "ultra-high-level" case in the human set: the difference
between `lyase activity` and the actual reaction is the entire informativeness of
the annotation.

---

## B3GALNT2 — β-1,3-N-acetylgalactosaminyltransferase 2 (Q8NCR0)

- **RHEA:37667** (transfers GalNAc in β1,3 linkage onto a GlcNAc-β-terminated
  glycan of α-dystroglycan), EC 2.4.1.313.
- **rhea2go:** no mapping. **ec2go:** EC 2.4.1.313 has no `ec2go` line.
- **Current GO MF:** `UDP-glycosyltransferase activity` and
  `acetylgalactosaminyltransferase activity` — both generic class terms; neither
  states the β1,3 linkage or the dystroglycan acceptor.
- **Evidence:** experimentally characterised acceptor specificity in
  PubMed:23929950 (`ECO:0000269`). Disease relevance: loss of function causes
  muscular dystrophy-dystroglycanopathy MDDGA11 (a defect in the α-dystroglycan
  *O*-mannosyl glycan elongation, where B3GALNT2 adds the GalNAc-β1,3-GlcNAc
  unit).

**Assessment.** QuickGO has many specific GalNAc-transferase terms but **none**
for the β1,3 activity on the GlcNAc-terminated *O*-mannosyl glycan — the curated
terms are the generic class. RHEA encodes the precise acceptor, but with the
reaction unmapped and the EC outside `ec2go`, that specificity never reaches GO.

**Action.**
- **`proposed_new_terms`:** *N-acetyl-β-glucosaminyl-glycoprotein
  β-1,3-N-acetylgalactosaminyltransferase activity* (acceptor = the
  GlcNAc-β-terminated α-dystroglycan *O*-mannosyl glycan), child of
  `GO:0008376 acetylgalactosaminyltransferase activity`, anchored to RHEA:37667 /
  EC 2.4.1.313.
- Keep the generic `acetylgalactosaminyltransferase activity` as a parent until
  the specific term exists; do **not** treat `UDP-glycosyltransferase activity`
  as the curated function.

Medically important and mechanistically precise — a strong gap-fill candidate.

---

## SAMD8 (SMSr) — ceramide phosphoethanolamine synthase (Q96LT4)

- **RHEA:36079** (`an N-acylsphing-4-enine + a
  1,2-diacyl-sn-glycero-3-phosphoethanolamine = a ceramide phosphoethanolamine +
  a 1,2-diacyl-sn-glycerol`), EC 2.7.8.-, the **defining** SMSr reaction (one of a
  family of unmapped CPE-synthase RHEA reactions on this entry: 36079/36080,
  42128/42129, …); plus a PE-PLC hydrolase reaction (EC 3.1.4.62).
- **rhea2go:** no mapping for the CPE-synthase reaction. **ec2go:** only the
  generic `EC:2.7.8.- → GO:0016780 phosphotransferase activity, for other
  substituted phosphate groups`.
- **Current GO MF:** `hydrolase activity` (ultra-high-level), `sphingomyelin
  synthase activity`, `ceramide cholinephosphotransferase activity`. It does
  **not** carry the term for its principal activity.
- **Specific term EXISTS:** `GO:0002950 ceramide phosphoethanolamine synthase
  activity` is already in GO — but is **not annotated** to SMSr.
- **Evidence:** SMSr characterised as the ER ceramide-phosphoethanolamine synthase
  (PubMed:19506037) with later mechanistic work (e.g. PubMed:33621517).

**Assessment.** This is the **clean propagation gap**: unlike PHYKPL/B3GALNT2 the
correct GO term already exists, yet the protein carries everything *except* it —
two SM-synthase-flavoured terms (SMSr is at best a weak SM synthase) and a bare
`hydrolase activity`. The RHEA reaction that would have delivered `GO:0002950` is
unmapped, so the term fell through the cracks even though no new term is needed.

**Action.**
- **`NEW` (add) `GO:0002950 ceramide phosphoethanolamine synthase activity`** as
  the core molecular function — the term exists; this is pure gap-filling.
- `MARK_AS_OVER_ANNOTATED` / `MODIFY` the bare `GO:0016787 hydrolase activity`
  (uninformative; the PE-PLC activity, if kept, should use a specific
  phospholipase-C-type term, not the root).
- Review `sphingomyelin synthase activity`: keep only as non-core if supported,
  since SMSr's mammalian activity is predominantly CPE synthase, not SM synthase.

The highest-value action of the four because it requires **no ontology work** —
just apply an existing term the RHEA mapping should already carry.

---

## SULT6B1 — sulfotransferase 6B1 / thyroxine sulfotransferase (Q6IMI4)

- **RHEA:26422** (sulfo transfer from PAPS to substrate, producing adenosine
  3',5'-bisphosphate), EC 2.8.2.n2 (provisional).
- **rhea2go:** no mapping. **ec2go:** the provisional `2.8.2.n2` is absent; only
  `EC:2.8.2.- → GO:0008146 sulfotransferase activity` applies.
- **Current GO MF:** `GO:0008146 sulfotransferase activity` only — the class term.
- **Evidence caveat:** the human catalytic-activity annotation is **by similarity**
  (`ECO:0000250|UniProtKB:P0CC03`), and the EC is provisional (`n2`). Substrate
  preference (thyroxine / thyroid hormones) is inferred, not directly shown for
  the human protein in the cited evidence.

**Assessment.** A real gap (only the class term), but the **fill is less certain**
than the others. There is no `thyroxine sulfotransferase activity` term in GO; the
closest specific existing term is `GO:0004062 aryl sulfotransferase activity`
(SULT6B1 is an aryl/phenolic sulfotransferase). Given the by-similarity evidence,
the responsible move is a *cautious* refinement plus an explicit question, not a
confident substrate-specific assertion.

**Action.**
- `MODIFY` toward `GO:0004062 aryl sulfotransferase activity` as a more
  informative-but-defensible parent, **or** leave as `UNDECIDED` pending direct
  human-enzyme substrate data — flag in `suggested_questions`.
- Only `propose` a thyroxine-specific term once direct activity (not similarity)
  is established for the human protein.

A deliberate contrast case: not every RHEA gap is a confident fill — evidence
quality gates how specific the proposed GO term should be.

---

## Cross-case lessons

1. **The gap is usually about specificity, not coverage.** None of these enzymes
   is left with *no* MF term — each has a class/root term (`lyase activity`,
   `sulfotransferase activity`, generic GalNAc-T, `hydrolase activity`). The RHEA
   reaction is the only place the *specific* activity is recorded, and the
   unmapped reaction is why it never reaches GO. This matches the project-level
   finding that G4/G5 are specificity gaps, not coverage gaps.
2. **Two fixes, picked by whether the GO term exists.** SAMD8 needs only an
   *existing* term applied (propagation gap). PHYKPL and B3GALNT2 need a *new*
   term (granularity gap) — these are `proposed_new_terms` for GO, and good
   candidates for the RHEA team to add to `rhea2go` once the term exists.
3. **Evidence gates specificity.** SULT6B1 shows that an unmapped RHEA on a
   by-similarity annotation justifies only a cautious parent-level refinement.
4. **These would all be fixed at the source** by mapping the reactions in
   `rhea2go` (where a GO term exists) and by adding the three missing GO MF terms
   (where one does not) — exactly the two levers this project recommends.

## Reproduce

```bash
uv run python rhea_gap_finder.py --organism 9606   # regenerate candidate list
```

To promote any case to a full gene review, run the standard workflow
(`just fetch-gene human PHYKPL`, edit `PHYKPL-ai-review.yaml`, `just validate …`)
and link it back here.
