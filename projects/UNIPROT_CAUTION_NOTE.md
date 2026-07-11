---
title: "UniProt CAUTION Note Project"
maturity: MATURE
tags: [PIPELINE, FLAGSHIP]
---

# UniProt CAUTION Note Project

## Overview

UniProtKB records can carry one or more free-text **CAUTION** comments in the
flat file:

```
CC   -!- CAUTION: In contrast to other JHDM1 histone demethylases, it lacks the
CC       iron catalytic His in position 370 which is replaced by a Tyr residue
CC       and has no histone demethylase activity in vitro (PubMed:16362057). It
CC       therefore may not be functional in vivo. {ECO:0000305|PubMed:16362057}.
```

A CAUTION comment is a curator's explicit warning to the reader: a function is
**contested**, an activity was **mis-attributed**, a supporting paper was
**retracted**, a domain is **degenerate** (pseudo-enzyme), or a feature is a
likely **artifact**. These are exactly the situations where automated GO
annotation (IEA/IBA, domain-to-function mappings) is most likely to be wrong,
and where AI-assisted review adds the most value.

This project systematically harvests CAUTION comments, categorizes them, and
uses them as a **prioritized worklist** for annotation review — a CAUTION note is
a strong signal that one or more existing GO annotations on that gene deserve
scrutiny.

> **Yes, this is a real UniProt feature.** CAUTION is a standard UniProtKB
> "General annotation (Comments)" topic
> (<https://www.uniprot.org/help/caution>), distinct from the structured
> `SEQUENCE CAUTION` block. We extract `CC   -!- CAUTION:` free-text comments
> and **exclude** the separate structured `CC   -!- SEQUENCE CAUTION:` block
> (erroneous initiation / frameshift / predicted-gene-model issues), which is
> about sequence construction rather than function.

## Headline numbers

**Database-wide (Swiss-Prot / reviewed, 2026-06-16):**

- **14,513** reviewed entries carry a CAUTION comment (vs 45,468 with the
  unrelated `SEQUENCE CAUTION` block — confirming `cc_caution` is the right field).
- **14,830** individual CAUTION notes; **~7,200** fall in high-signal categories.

| Category | Notes (DB-wide) | Curation value |
|----------|------:|----------------|
| contested-function | 3,035 | high |
| reclassified-function | 2,476 | high |
| degenerate-domain (pseudo-enzyme) | 1,366 | high |
| retracted-reference | 279 | high |
| possible-artifact | 63 | high |
| other | 7,605 | mixed (keyword classifier residual) |
| lacks-conserved-residue | 6 | low |

**Distribution by organism** (top): Human (2,298 entries), *S. cerevisiae* (895),
Mouse (844), *A. thaliana* (714), *E. coli* K12 (334), Rat (329), Bovine (206),
*Dictyostelium* (192), *Drosophila* (160), Rice (150), *C. elegans* (122),
Zebrafish (109).

**Local corpus** (genes already fetched in this repo) — **209 CAUTION notes
across 201 cached `*-uniprot.txt` records**:

| Category | Count | Curation value | Description |
|----------|------:|----------------|-------------|
| contested-function | 44 | **high** | function is controversial / disputed / "however ..." |
| reclassified-function | 37 | **high** | "was originally/initially thought to be ..." |
| degenerate-domain | 16 | **high** | pseudo-enzyme; "lacks the catalytic/active-site residue" |
| retracted-reference | 12 | **high** | a supporting paper has been retracted |
| possible-artifact | 4 | **high** | result may be an experimental artifact |
| other | 38 | mixed | residual curatorial notes not matched by keywords |
| wgs-preliminary | 39 | low | boilerplate: sequence from a preliminary WGS entry |
| lacks-conserved-residue | 19 | low | boilerplate feature-propagation warning |
| **Total** | **209** | | across **201** records |

The WGS-preliminary boilerplate that dominated the *local* corpus essentially
**vanishes** in reviewed entries (0–6), confirming it was a TrEMBL/unreviewed
artifact rather than a curatorial signal.

## Why this matters for GO review

The high-value categories map directly onto well-known GO over-annotation
failure modes:

- **degenerate-domain / pseudo-enzyme** → domain-based IEA/IBA assigns a
  catalytic MF the protein cannot perform. Overlaps strongly with the
  [Contested Function project](CONTESTED_FUNCTION.md) and
  [Pseudoenzymes project](PSEUDOENZYMES.md).
- **reclassified-function** → the gene was historically placed in the wrong
  complex/pathway; legacy GO terms may persist (e.g. NDUFA4 "was initially
  believed to be a subunit of complex I").
- **retracted-reference** → annotations whose `original_reference_id` points to
  a retracted paper should be flagged `is_invalid` and the function re-examined.
- **contested-function / possible-artifact** → candidates for the schema's
  `finding_review` (`DISPUTED`) and `reference_review` machinery, or
  `KEEP_AS_NON_CORE` / `MARK_AS_OVER_ANNOTATED` actions.

Cross-referencing the DB-wide survey against the accessions we have **already
fetched** (148 of our local genes overlap the reviewed-CAUTION set) yields
**4,046 high-value, not-yet-reviewed candidates**: reclassified-function (2,401),
degenerate-domain (1,342), retracted-reference (255), possible-artifact (48).
Human alone contributes **95 pseudo-enzyme (degenerate-domain)** and **111
retracted-reference** candidates, e.g.:

- **RHBDF1** (Q96CC6) — "Lacks serine protease activity ... lacks the catalytic
  Ser residue at position 720" (iRhom pseudo-protease).
- **SUMF2** (Q8NBJ7) — "strongly similar to formylglycine-generating enzyme,
  lacks the catalytic Cys".
- **PANK4** (Q9NVE7) — pantothenate kinase domain is degenerate.
- **CHI3L1** (P36222), **SPACA3** (Q8IXA5) — glycosyl hydrolase folds with
  substituted catalytic residues.
- **ERCC8** (Q13216), **H3-3A/B** (P84243), **CBX1/CBX5** — annotations resting
  on retracted papers.

## Findings

### Deep dive batch 1 (degenerate-domain)

Fetched 5 human `degenerate-domain` candidates (RHBDF1, SUMF2, PANK4, DPYSL5,
NAALADL2) and checked their curated GO molecular functions against the CAUTION
note:

- **4 of 5 are already correctly handled by GO**, usually via an explicit
  `NOT|enables` on the lost catalytic term — frequently citing the *same* paper
  named in the CAUTION (RHBDF1↔PMID:21439629, PANK4↔PMID:30927326). The GO `NOT`
  qualifier is effectively the curated counterpart of the UniProt CAUTION.
- **One suspect over-annotation — DPYSL5 (CRMP5):** `GO:0004157`
  dihydropyrimidinase is correctly `NOT`-ed, while two positive **InterPro IEA**
  parent terms (`GO:0016787`, `GO:0016810` hydrolase activity) survive. This is
  *not* a logical contradiction (GO `NOT` propagates **down**, not up — so a
  negated child does not negate the parent), but it is an evidentially weak
  fold/domain-based propagation: the metal-site loss that justifies the `NOT`
  also removes the mechanistic basis for *any* metallo-hydrolase activity, with
  no positive evidence for an alternative → candidate `MARK_AS_OVER_ANNOTATED`.

### Systematic over-annotation queries (local corpus, 2,675 genes)

Two CAUTION-driven detectors, run over the locally-fetched corpus (GO ancestry
via oaklib; no network).

**Query A — negated-child / positive-parent conjunction.** Within a gene, a
molecular-function term `X` is annotated positively while a more specific
descendant `Y` is annotated `NOT`. **33 hits / 22 genes** (24 with an electronic
IEA/IBA parent). A triage column marks a hit **STRONG** when the parent's
specificity has *no* experimental positive support in GOA (the DPYSL5 pattern):

| Gene | positive parent | NOT-ed child | note |
|------|-----------------|--------------|------|
| DPYSL5 | hydrolase activity (IEA) | dihydropyrimidinase (IBA) | confirmed over-annotation → REMOVE (done) |
| CPT1C | (acyl)transferase activity (IEA) | carnitine O-palmitoyltransferase (ISS) | CAUTION: little/no CPT activity in vivo — likely over-annotation |
| ENDOU | hydrolase activity (IEA) | serine-type peptidase (IDA) | parent legit (it's a ribonuclease), child correctly NOT-ed |
| pmp20 | peroxidase activity (IEA) | glutathione peroxidase (IDA) | **false positive**: genuine peroxiredoxin, peroxidase only IEA-annotated |

Query A also surfaces **9 DIRECT same-term conflicts** — a term annotated *both*
positively and `NOT` on the same gene (genuine GOA inconsistencies worth
reporting upstream), e.g. EDEM1/EDEM2 `mannosyl-oligosaccharide 1,2-α-mannosidase`
(TAS vs NOT IDA), ENDOU `serine-type peptidase` (IDA vs NOT IDA), PARK7
`protein deglycase` (IDA vs NOT IDA), CYB5R4 `NAD(P)H oxidase` (IDA vs NOT IDA).

**Query B — CAUTION PMID cited positively, never negated.** Flags genes where a
UniProt CAUTION cites a PMID, a GO annotation is made *to that same PMID*, and
there is *no* `NOT` annotation citing it. **69 flags / 39 genes.** Highest-value
molecular-function hits:

- **CHMP1A** ↔ PMID:8863740 — `metallopeptidase activity` + `zinc ion binding`
  (TAS) from a paper whose "metalloprotease (PRSM1)" reading came from a **wrong
  ORF translation** → strong REMOVE candidates.
- **ENDOU** ↔ PMID:2350438 — `serine-type peptidase activity` (IDA) from the paper
  later refuted (it is an endoribonuclease, not a protease).
- **HDAC6** ↔ PMID:10220385 — `histone deacetylase activity` (IDA) from the
  "originally thought to be a histone deacetylase" paper (it is predominantly a
  cytoplasmic tubulin deacetylase).
- **TCF25** ↔ PMID:16574069 — DNA-binding shown only via a GAL4-DBD fusion (CAUTION:
  "uncertain"); **CSNK1D** ↔ PMID:20637175 — DCK phosphorylation "probably not in
  vivo"; **NME2** ↔ PMID:11121025 — contested intrinsic nuclease activity.

Many other Query B hits are *localization* debates (AGK, AIFM2, ASAH2, C1QBP,
ATP13A1, Dnajb11) where the positive annotation may have been deliberately
retained — these are flags for a curator's eye, not automatic removals.

### Validation against existing curated reviews

Because the local corpus is *already curated*, the query hits double as a test of
the method — each flag is joined to the action the existing review assigned:

- **Query A STRONG: 8/11 CONFIRMED** — the curator had already set
  `REMOVE`/`MARK_AS_OVER_ANNOTATED`/`MODIFY` on the flagged parent (DPYSL5, CPT1C
  ×2, pmp20 ×2…). The 3 "kept" are correctly-retained parents on a *different*
  branch (ENDOU is a ribonuclease → `hydrolase` is right; MAP1S really does bind
  actin; PEX12 is a ubiquitin ligase). The STRONG triage tracks expert decisions.
- **Query B: 17 CONFIRMED** real catches (CHMP1A metalloprotease/zinc from a
  mistranslated ORF; ENDOU serine protease; HDAC6 histone-deacetylase; NME2
  nuclease; the retracted TP53–BANP interactions…) — but **~47 "kept" are
  expected false-positives** (see Lessons learned).

**Net:** the two genes spot-checked — **CPT1C** and **CHMP1A** — were both already
**correctly curated** (CPT1C `REMOVE`s the unsupported transferase parents and keeps
`catalytic activity` because the real palmitoyl-hydrolase activity sits under it,
exactly matching the STRONG-vs-supported split; CHMP1A `REMOVE`s the mistranslated-ORF
metalloprotease/zinc terms). No edits were needed — the queries reproduced the
experts' decisions, the validation we wanted before scaling UniProt-wide.

### UniProt-wide scaling (QuickGO) — net-new pseudoenzyme families

Pulling molecular-function GOA from QuickGO for **all 14,513 reviewed CAUTION
accessions** (MF annotations found for 12,194) and running both queries
database-wide, flagging genes **not yet in this repo** (`net_new`):

- **Query A: 247 conjunctions → 105 STRONG (100 in net-new genes)**, plus **97
  DIRECT same-term conflicts**.
- **Query B: 1,140 flags (1,083 net-new).**

**The STRONG net-new hits land squarely on known pseudoenzyme families**, recovered
automatically and extended across orthologs — strong external validation:

| Gene(s) | Lost activity (NOT) | Persisting electronic over-annotation |
|---------|---------------------|----------------------------------------|
| **DPYSL2/CRMP2, DPYSL3, DPYSL4, CRMP1** (+ mouse/rat/chicken/bovine orthologs) | dihydropyrimidinase (GO:0004157) | `hydrolase activity` (GO:0016787/0016810) IEA — *the exact DPYSL5 pattern across the whole CRMP family* |
| **ILK** (integrin-linked kinase) | protein Ser/Thr kinase (GO:0004674) | `protein kinase activity` IEA — classic **pseudokinase** |
| **ROR1** (+ orthologs, lin-18) | receptor tyrosine kinase (GO:0004714) | `protein kinase activity` IEA — **pseudokinase RTK** |
| **CASP12** (+ CASP13 bovine) | cysteine-type endopeptidase (GO:0004197) | `cysteine-type peptidase activity` IEA — **pseudo-caspase** |
| **AZIN2** (+ orthologs) | ornithine/arginine decarboxylase (GO:0004586/0008792) | `catalytic activity` IEA — dead ODC paralog (antizyme inhibitor) |
| **Cpt1c** (mouse/rat) | carnitine O-palmitoyltransferase (GO:0004095) | `acyltransferase activity` IEA — same as the human CPT1C we audited |

That the method **independently rediscovers ILK, ROR1, CASP12, AZIN2 and the CRMP
family** — canonical pseudoenzymes — from nothing but "CAUTION text + GO `NOT` +
GO ancestry" is the validation that matters. **Immediate human review targets** (not
yet in this repo): DPYSL2 (Q16555), DPYSL3 (Q14195), DPYSL4 (O14531), CRMP1
(Q14194), ILK (Q13418), ROR1 (Q01973), CASP12 (Q6UXS9), AZIN2.

### Featured examples (from the cached corpus)

- **SCHPO/Epe1** (O94603) — "lacks the iron catalytic His ... no histone
  demethylase activity in vitro ... may not be functional in vivo." Textbook
  pseudo-enzyme; already a flagship of [CONTESTED_FUNCTION](CONTESTED_FUNCTION.md).
- **human/NDUFA4** (O00483) — "Was initially believed to be a subunit of
  complex I" (it is a subunit of complex IV). Legacy complex-I GO terms are the
  risk.
- **human/AKT1** (P31749) — two CAUTION notes flag **retracted** papers
  (PUBMED:20231902, PUBMED:19940129) plus an isoform-redundancy caveat.
- **human/PARK7 / DJ-1** (Q99497) — glyoxalase vs deglycase activity is
  explicitly called **controversial**; a clean test case for contested MF.
- **human/IL4I1** (Q96RQ9) — an enzymatic-independence claim is flagged as
  needing confirmation (only Phe, not Trp, deprivation was tested).
- **human/UCHL1** (P09936) — disease association and ubiquitin-ligase activity
  both flagged as contested across conflicting papers.
- **SACEN/eryCII** (Q939Z0) — "related to the cytochrome P450 family, lacks the
  heme-binding sites"; pseudo-enzyme that is actually a glycosyltransferase
  activator (already reviewed under CONTESTED_FUNCTION).
- **ARATH/CRY1, CRY2** — "Was originally thought to be a DNA photolyase"
  (cryptochromes are photoreceptors, not repair enzymes).

## Lessons learned

- **A flag is a prioritization signal, not a verdict.** Query A STRONG means "no
  experimental backing for the parent's specificity in GOA" — but some flagged
  parents are real activities that simply lack an experimental annotation (e.g.
  pmp20 is a genuine peroxiredoxin; the peroxidase parent is only IEA-annotated).
  Adjudication stays evidential.
- **GO `NOT` propagates down, not up.** A negated child does not negate the
  parent, so a positive-parent / negated-child pair is logically admissible. The
  generalizable review flag is a **positive IEA** parent whose curated,
  more-specific **child is `NOT`-ed** — admissible but evidentially weak when the
  same residue loss that justifies the `NOT` removes the basis for the parent too.
- **Genericity ≠ wrongness.** The maximally generic MF term can be the *correct*
  family-level annotation (cf. the InterPro Radical-SAM case): the issue is
  whether the specificity is supported, not how general the term is.
- **PMID-level matching over-flags (Query B).** A contested CAUTION paper usually
  makes *several* claims and only one is doubted, so matching on PMID alone catches
  the real refutation plus collateral (e.g. CPT1C↔PMID:30135643 *is* the real
  palmitoyl-hydrolase paper; UFSP1 is now known active; CSNK1D's kinase activity is
  bona fide — only its DCK substrate is doubted). Precise use needs matching the
  contested *activity* to the GO term, not just the citation.
- **The GO `NOT` qualifier is the curated counterpart of a UniProt CAUTION** —
  when both exist they usually cite the same paper, so the highest-value targets
  are CAUTIONs with *no* corresponding GO `NOT`.

## Reproducibility

All numbers above are produced by reproducible scripts under
[`UNIPROT_CAUTION_NOTE/`](UNIPROT_CAUTION_NOTE/); the multi-MB GOA dumps are
gitignored but regenerable. Rerun after fetching new genes.

| Step | Command | Outputs |
|------|---------|---------|
| Local extraction | [`extract_caution_notes.py`](UNIPROT_CAUTION_NOTE/extract_caution_notes.py) | [`caution_notes.tsv`](UNIPROT_CAUTION_NOTE/caution_notes.tsv), [`caution_notes.md`](UNIPROT_CAUTION_NOTE/caution_notes.md) |
| DB-wide survey (REST API `cc_caution`) | [`uniprot_api_survey.py`](UNIPROT_CAUTION_NOTE/uniprot_api_survey.py) (`--organism 9606` for human) | [`caution_uniprot_reviewed.tsv`](UNIPROT_CAUTION_NOTE/caution_uniprot_reviewed.tsv), [`api_survey.md`](UNIPROT_CAUTION_NOTE/api_survey.md) |
| Prioritized worklist | [`shortlist_candidates.py`](UNIPROT_CAUTION_NOTE/shortlist_candidates.py) | [`candidates_high_value.tsv`](UNIPROT_CAUTION_NOTE/candidates_high_value.tsv), [`candidates.md`](UNIPROT_CAUTION_NOTE/candidates.md) |
| Local over-annotation queries (A/B) | [`caution_conjunction_queries.py`](UNIPROT_CAUTION_NOTE/caution_conjunction_queries.py) | [`caution_conjunction.md`](UNIPROT_CAUTION_NOTE/caution_conjunction.md), `conjunction_hits.tsv`, `caution_pmid_unnegated.tsv` |
| Validate queries vs reviews | [`audit_queries_vs_reviews.py`](UNIPROT_CAUTION_NOTE/audit_queries_vs_reviews.py) | [`audit_queries_vs_reviews.md`](UNIPROT_CAUTION_NOTE/audit_queries_vs_reviews.md) |
| UniProt-wide scaling (QuickGO) | [`uniprot_wide_queries.py`](UNIPROT_CAUTION_NOTE/uniprot_wide_queries.py) | [`uniprot_wide_queries.md`](UNIPROT_CAUTION_NOTE/uniprot_wide_queries.md), `uniprot_wide_conjunctions.tsv`, `uniprot_wide_pmid.tsv` |

The deep-dive write-up is in
[`deep_dive_batch1.md`](UNIPROT_CAUTION_NOTE/deep_dive_batch1.md). To run UniProt-wide
the queries need GOA (evidence codes + `NOT` qualifiers) per accession, which the
`cc_caution` API survey does not carry — supplied here by the QuickGO pull.

## Workflow

1. (Re)generate the worklist: run `extract_caution_notes.py`.
2. Prioritize the high-value categories (contested / reclassified /
   degenerate-domain / retracted / possible-artifact).
3. For each gene that **already has** a `*-ai-review.yaml`, check whether its
   existing annotations are consistent with the CAUTION note; if a retracted
   PMID is an `original_reference_id`, flag it.
4. For genes without a review yet, treat the CAUTION note as a strong reason to
   prioritize a full review (`just fetch-gene <org> <gene>`).
5. Record findings using `reference_review` (retracted → `is_invalid`),
   `finding_review` (`DISPUTED`), and appropriate annotation `action`s.

## Related projects

- [CONTESTED_FUNCTION.md](CONTESTED_FUNCTION.md)
- [PSEUDOENZYMES.md](PSEUDOENZYMES.md)
- [OVER_ANNOTATION_PATTERNS.md](OVER_ANNOTATION_PATTERNS.md)

---

# STATUS

## Done
- [x] Confirmed UniProt CAUTION comments exist and are present in the cached
  corpus (209 notes / 201 records).
- [x] Wrote reproducible local extractor `extract_caution_notes.py`.
- [x] Surveyed the **whole reviewed UniProt** via the REST API
  (`uniprot_api_survey.py`): 14,513 entries / 14,830 notes, with category and
  per-organism distributions — no `fetch-gene` required.
- [x] Built `shortlist_candidates.py` → 4,046 high-value, not-yet-reviewed
  candidates (`candidates_high_value.tsv`, `candidates.md`).
- [x] **Deep dive batch 1** (`deep_dive_batch1.md`): fetched RHBDF1, SUMF2,
  PANK4, DPYSL5, NAALADL2; found 4/5 already correctly negated by GO and **1
  suspect domain-based over-annotation (DPYSL5 hydrolase IEAs — evidentially
  weak, not a logical contradiction)**.

- [x] **DPYSL5 (CRMP5) full review** written and validated
  (`genes/human/DPYSL5/DPYSL5-ai-review.yaml`, DRAFT): `REMOVE` on the two IEA
  hydrolase over-annotations (`GO:0016787`, `GO:0016810`), `ACCEPT` on the curated
  `NOT`s, core function = negative regulation of dendrite morphogenesis.

- [x] **All 5 batch-1 reviews completed** and validated (RHBDF1, SUMF2, PANK4,
  NAALADL2 + DPYSL5). DPYSL5 was the only one needing a `REMOVE` of a positively
  asserted catalytic term; PANK4 is a domain-swap pseudoenzyme (dead PanK domain
  + real, correctly annotated 4'-phosphopantetheine phosphatase).

- [x] **Two systematic over-annotation queries implemented**
  (`caution_conjunction_queries.py`): Query A (negated-child/positive-parent
  conjunction, 33 hits + 9 direct conflicts, with a STRONG/experimental-support
  triage) and Query B (CAUTION-PMID-cited-positively-never-negated, 69 flags).
- [x] **Validated the queries against existing reviews**
  (`audit_queries_vs_reviews.py`): Query A STRONG 8/11 CONFIRMED; Query B 17
  CONFIRMED catches (rest are expected PMID-level false-positives). **CPT1C and
  CHMP1A were already correctly curated** — the queries reproduced the experts'
  REMOVE/MODIFY decisions, so no edits needed.
- [x] **Scaled both queries UniProt-wide via QuickGO** (`uniprot_wide_queries.py`):
  14,513 CAUTION accessions → Query A 247 conjunctions / 105 STRONG (100 net-new) +
  97 direct conflicts; Query B 1,140 flags. STRONG net-new hits recover known
  pseudoenzyme families (CRMP/DPYSL, ILK, ROR1, CASP12, AZIN2) across orthologs.
- [x] **Reviewed the human CRMP family** (DPYSL2, DPYSL3, DPYSL4, CRMP1) — full
  validated DRAFT reviews applying the DPYSL5 fix: `REMOVE` the electronic
  `hydrolase activity` parents (GO:0016787/0016810/0016812), `ACCEPT` the curated
  `NOT|dihydropyrimidinase`; DPYSL2 additionally `REMOVE`s a legacy positive
  dihydropyrimidinase (TAS) + its dependent nucleobase-metabolism term. Core
  function recorded as catalytically dead cytoskeletal regulator in semaphorin signaling.

- [x] **Reviewed net-new pseudoenzymes ILK, ROR1, CASP12, AZIN2** — full validated
  DRAFT reviews. Each `REMOVE`s the electronic catalytic over-annotation flagged by
  the query (ILK `protein kinase activity`; ROR1 `protein kinase activity` + legacy
  TAS RTK/PTK-signaling; CASP12 `cysteine peptidase`/`endopeptidase`/proteolysis;
  AZIN2 `catalytic activity`/`carboxy-lyase`/legacy arginine-decarboxylase), `ACCEPT`s
  the curated `NOT`s, and records the real non-catalytic core (ILK = IPP-complex
  scaffold; ROR1 = Wnt coreceptor; CASP12 = dominant-negative inflammasome modulator;
  AZIN2 = ODC-activator/antizyme inhibitor).

## Pending
- [ ] Report the 9 local + 97 UniProt-wide DIRECT same-term GOA conflicts upstream
  to GO.
- [ ] Scale Queries A/B UniProt-wide via a QuickGO GOA pull keyed on the 14k
  CAUTION accessions.
- [ ] Audit the 255 retracted-reference candidates for retracted
  `original_reference_id`s in existing reviews.
- [ ] Scale the "positive-IEA-catalytic + curated-NOT" conjunction query across
  the 1,342 degenerate-domain candidates to auto-surface over-annotations.
- [ ] Audit retracted-reference candidates for retracted `original_reference_id`s
  in any existing review.
- [ ] Refine the keyword classifier to shrink the large "other" bucket (7,605
  DB-wide notes) — many are genuine but unmatched.
- [ ] Add a `just` target to regenerate the survey + shortlist on demand.

Last updated: 2026-06-16

# NOTES

## 2026-06-16

**Project creation.** Verified the premise before building: UniProt CAUTION is a
real, documented comment topic, and `grep -c '\-!- CAUTION:'` across the cached
`*-uniprot.txt` files returns 209 matches in 201 records. Built a parser that
correctly handles multi-line CAUTION comments and excludes the structured
`SEQUENCE CAUTION` block. Keyword categorizer separates curation-meaningful
notes (contested / reclassified / degenerate-domain / retracted / artifact) from
automatic boilerplate (WGS-preliminary, lacks-conserved-residue). The
degenerate-domain bucket overlaps heavily with existing CONTESTED_FUNCTION and
PSEUDOENZYMES work, confirming CAUTION notes are a good signal for finding
over-annotated catalytic functions.

**API survey added (same day).** Per request, queried the live UniProt REST API
on the `cc_caution` field (distinct from `cc_sequence_caution`) to get a
database-wide distribution without fetching genes: 14,513 reviewed entries,
14,830 notes, ~7,200 high-signal. Human dominates (2,298). Cross-referencing
against the 148 reviewed-CAUTION genes we already have yields a 4,046-entry
high-value worklist — the basis for a prioritized deep dive (starting with human
pseudo-enzymes flagged by degenerate-domain cautions).
