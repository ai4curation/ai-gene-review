---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T14:47:05.010444'
end_time: '2026-07-11T15:01:50.944321'
duration_seconds: 885.93
template_file: templates/module_pathway_taxon_research.md.j2
template_variables:
  module_title: Rubredoxin electron transfer
  module_summary: A Pseudomonas putida KT2440 UniPathway UPA00191 module for the small
    iron-binding rubredoxin electron carrier RubA (PP_5315, UniProtKB:Q88C68). RubA
    is annotated as transferring electrons in a hydrocarbon hydroxylating system,
    likely functioning with the adjacent rubredoxin reductase AlkT as an electron-transfer
    component for alkane monooxygenase chemistry.
  module_outline: "- Rubredoxin electron transfer\n  - 1. Rubredoxin electron carrier\
    \ for hydrocarbon hydroxylation\n  - RubA rubredoxin electron-transfer step\n\
    \    - rubA: rubredoxin electron carrier (molecular player: PSEPK rubA; activity\
    \ or role: electron transfer activity)"
  module_connections: No explicit connections.
  pathway_query: UPA00191
  pathway_id: UPA00191
  pathway_name: UniPathway UPA00191
  pathway_source: UniPathway
  pathway_context: 'Resolved local bucket unipathway:UPA00191 with 1 primary genes;
    module area: unipathway.'
  organism: PSEPK
  species_name: Pseudomonas putida KT2440
  taxon_id: '160488'
  proteome_id: UP000000556
  candidate_gene_count: '1'
  candidate_genes: '- rubA: PP_5315 | Q88C68 | Rubredoxin (primary bucket unipathway:UPA00191)'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 3
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PSEPK__rubredoxin_electron_transfer__upa00191-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PSEPK__rubredoxin_electron_transfer__upa00191-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Module/Pathway/Taxon Review Brief

## Review Topic

Rubredoxin electron transfer in Pseudomonas putida KT2440

## Target Taxon

- Organism code: PSEPK
- Species/strain: Pseudomonas putida KT2440
- NCBI taxon: 160488
- Proteome: UP000000556

## Target Pathway Or Bucket

- Query: UPA00191
- Resolved ID: UPA00191
- Resolved name: UniPathway UPA00191
- Source: UniPathway

Resolved local bucket unipathway:UPA00191 with 1 primary genes; module area: unipathway.

## Candidate Genes From Local Metadata

Candidate gene count: 1

- rubA: PP_5315 | Q88C68 | Rubredoxin (primary bucket unipathway:UPA00191)

## Generic Module Context

### Working Scope

A Pseudomonas putida KT2440 UniPathway UPA00191 module for the small iron-binding rubredoxin electron carrier RubA (PP_5315, UniProtKB:Q88C68). RubA is annotated as transferring electrons in a hydrocarbon hydroxylating system, likely functioning with the adjacent rubredoxin reductase AlkT as an electron-transfer component for alkane monooxygenase chemistry.

### Provisional Biological Outline

- Rubredoxin electron transfer
  - 1. Rubredoxin electron carrier for hydrocarbon hydroxylation
  - RubA rubredoxin electron-transfer step
    - rubA: rubredoxin electron carrier (molecular player: PSEPK rubA; activity or role: electron transfer activity)

### Known Relationships Among Steps

No explicit connections.

## Assignment

Write a species-aware review of this module/pathway in the target organism. The
goal is not a generic pathway essay; the goal is to support manual module
satisfiability and gene annotation curation.

Treat the candidate gene list as a starting point, not ground truth. Use the
literature and authoritative resources to decide whether each expected pathway
step is present, absent, ambiguous, replaced by a lineage-specific alternative,
or represented by a likely over-propagated annotation.

Prioritize direct evidence from the target species/strain. When using evidence
from related organisms, state the organism and explain whether transfer to the
target taxon is strong, weak, or uncertain. Distinguish *Pseudomonas putida*
KT2440 evidence from broader *Pseudomonas* or generic bacterial evidence.

## Questions To Address

1. **Pathway boundaries**
   - What exact biochemical or cellular process is included?
   - Which neighboring pathways or broad overview maps should be kept separate?
   - Are there alternate names or database-specific definitions for this pathway?

2. **Satisfiability in the target taxon**
   - Which expected steps are encoded by candidate genes?
   - Which steps are missing from the metadata but likely present under a
     different gene name, paralog, or enzyme family?
   - Which steps are probably not expected in this organism?

3. **Candidate gene assessment**
   - For each high-confidence gene, summarize the likely role, evidence type,
     and any curation-relevant caveats.
   - Identify paralog ambiguity, broad EC/GO mappings, and likely annotation
     over-propagation.
   - Note genes that should be promoted to full `fetch-gene` review.

4. **Module implications**
   - What module steps should be marked covered, candidate_uncertain, gap,
     not_expected_in_target_taxon, or module_needs_revision?
   - Are existing generic module boundaries wrong for this organism?
   - Are new module documents or GO term requests likely needed?

5. **Evidence and open questions**
   - Which conclusions are supported by direct experiments?
   - Which are inferred from homology, pathway databases, or neighboring genes?
   - What experiments or expert questions would resolve the important gaps?

## Output Format

Use concise review sections:

1. Executive summary
2. Target-organism pathway definition
3. Expected step model
4. Candidate genes and evidence
5. Gaps, ambiguities, and likely over-annotations
6. Module and GO-curation recommendations
7. Genes to promote to full review
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty, species transfer, and whether evidence is direct for the target
organism.

## Output

# Commissioned Module/Pathway/Taxon Review — Rubredoxin Electron Transfer in *Pseudomonas putida* KT2440

**Module/Bucket:** UniPathway UPA00191 (`unipathway:UPA00191`)
**Target taxon:** *Pseudomonas putida* KT2440 (PSEPK; NCBI taxon 160488; proteome UP000000556)
**Candidate genes from local metadata:** 1 — `rubA` (PP_5315 | Q88C68 | Rubredoxin)
**Curation verdict (headline):** Electron-carrier step **COVERED**; terminal alkane-monooxygenase step **GAP / not_expected_in_target_taxon**; UPA00191 as an alkane-degradation pathway is **NOT satisfiable**; RubA's alkane-hydroxylase coupling is a **likely over-propagated annotation**.

---

## 1. Executive Summary

The UniPathway UPA00191 module for *Pseudomonas putida* KT2440 rests on a single candidate gene, `rubA` (PP_5315, UniProtKB:Q88C68), an iron-binding rubredoxin annotated as an electron-transfer component of a hydrocarbon-hydroxylating system. This review evaluated whether the module is satisfiable in KT2440 and whether the alkane-oxidation framing of RubA holds up against direct sequence, genomic-context, and literature evidence. The short answer: the **electron-carrier machinery is genuinely present, but the pathway it is supposed to feed is not.**

RubA is a *bona fide* single-domain rubredoxin (55 aa) with two canonical CxxCG iron-binding motifs, sitting immediately adjacent to a FAD-dependent rubredoxin–NAD(+) reductase, AlkT (PP_5314, K05297 / EC 1.18.1.1). KT2440 additionally carries a second, fused reductase–rubredoxin protein (PP_5371). So the reductase → rubredoxin electron-relay hardware — NADH → AlkT → RubA — is encoded and structurally intact. That part of the module is **covered**.

However, the terminal enzyme that this relay is meant to power — a membrane non-heme diiron **alkane 1-monooxygenase (AlkB, EC 1.14.15.3)** — is **absent** from the KT2440 proteome. The only gene named "alkB" in KT2440 (PP_3400) is a **homonym**: it is the DNA-repair α-ketoglutarate/Fe(II)-dependent dioxygenase AlkB (KEGG K03919), an entirely different enzyme. The prototypical alkane-degradation system (`alkBFGHJKL`/`alkST`) resides on the OCT plasmid of *P. putida* GPo1 / *P. oleovorans*, which KT2440 does not carry. KT2440 is not an alkane-degrader. Consequently, UPA00191 read as "alkane degradation via alkane 1-monooxygenase" is **not satisfiable** in this organism, and RubA's `GO:0043448 alkane catabolic process` / UPA00191 assignments (all IEA, propagated by pathway inference rather than experiment) are **over-propagated**. Sequence typing reinforces this: RubA is a conserved single-domain **AlkG1-type housekeeping rubredoxin** (90% identical to a conserved *Ectopseudomonas (Pseudomonas) oleovorans* rubredoxin, only ~54–56% to the two-domain alkane-transfer AlkG/Rd2), most plausibly a general NAD(P)H:rubredoxin electron carrier — not a dedicated alkane-hydroxylase partner.

**Curation bottom line:** Keep the *rubredoxin electron-transfer step* as **covered** (RubA + AlkT present), but mark the overall alkane-degradation module as **gap / not_expected_in_target_taxon** at the terminal monooxygenase step, flag RubA's alkane-specific role as **candidate_uncertain (likely over-annotation)**, and treat the whole UPA00191 module as **module_needs_revision** for this organism. The generic module boundary (rubredoxin = "alkane degradation") is **wrong for KT2440**.

---

## 2. Target-Organism Pathway Definition

**What UPA00191 is meant to include.** UniPathway UPA00191 is defined around the rubredoxin-dependent electron-transfer step that supplies reducing equivalents to a hydrocarbon (alkane) hydroxylating system. In the canonical, best-characterized version of this chemistry — the *P. putida* GPo1 / *P. oleovorans* OCT-plasmid Alk system — the electron flow is:

```
NADH → AlkT (rubredoxin reductase, FAD) → AlkG (rubredoxin, Fe) → AlkB (alkane 1-monooxygenase) → alkane → 1-alkanol
```

RubA (with AlkT) corresponds to the **reductase/carrier** components of that chain. The module scope as commissioned is narrow: "rubredoxin electron transfer" for "hydrocarbon hydroxylation." This is the canonical two-electron delivery system for AlkB activation (Williams et al., 2022, [PMID: 34990970](https://pubmed.ncbi.nlm.nih.gov/34990970/): *"Electrons are typically supplied by NADH via a rubredoxin reductase (AlkT) to a rubredoxin (AlkG) to AlkB"*).

**What must be kept separate for KT2440.** For curation purposes it is essential to distinguish three things that share names or EC-space but are biologically distinct in KT2440:

1. **Alkane 1-monooxygenase AlkB (EC 1.14.15.3)** — a ~400-aa integral-membrane non-heme diiron hydroxylase. This is the pathway's terminal enzyme. It is **not present** in KT2440.
2. **DNA-repair AlkB (K03919, EC 1.14.11.-)** — a ~215-aa cytoplasmic α-ketoglutarate/Fe(II) dioxygenase that oxidatively demethylates alkylated DNA. This *is* present (PP_3400) but is unrelated to hydrocarbon catabolism. It must not be counted toward UPA00191.
3. **General rubredoxin/reductase redox housekeeping** — RubA + AlkT + PP_5371 function as a NAD(P)H:rubredoxin electron-relay module that in KT2440 is associated with **fatty-acid degradation (KEGG ppu00071)** and general redox/oxidative-stress physiology, *not* a dedicated alkane pathway.

**Alternate names / database definitions.** UPA00191 = "alkane degradation" (UniPathway); GO:0043448 = "alkane catabolic process." RubA = "Rubredoxin," locus PP_5315, UniProtKB Q88C68. In the alkane literature the functional rubredoxins are called **Rd2 / AlkG (AlkG2-type)** and the non-functional conserved ones **AlkG1-type**. The adjacent reductase AlkT (PP_5314) is variously "rubredoxin reductase," "rubredoxin–NAD(+) reductase" (EC 1.18.1.1), KEGG K05297. Curators should be alert that "AlkB" and "AlkG/AlkT" naming is heavily overloaded across databases.

---

## 3. Expected Step Model

The minimal expected-step model for a satisfiable UPA00191 alkane-hydroxylation module, and its status in KT2440:

| Step | Enzyme / role | EC / KO | Expected gene | KT2440 status |
|------|---------------|---------|---------------|---------------|
| S1 | Rubredoxin–NAD(+) reductase (FAD); NADH → rubredoxin | EC 1.18.1.1 / K05297 | alkT | **Present** — PP_5314 (Q88C69); also fused PP_5371 (Q88C12) |
| S2 | Rubredoxin electron carrier; reductase → hydroxylase | GO:0009055; Fe binding | rubA / alkG | **Present but reclassified** — PP_5315 (Q88C68), AlkG1-type housekeeping rubredoxin |
| S3 | Alkane 1-monooxygenase; hydroxylates alkane | EC 1.14.15.3 | alkB | **Absent** — no true membrane diiron AlkB; PP_3400 is a homonymous DNA-repair dioxygenase (K03919) |

**Satisfiability conclusion:** Steps S1 and S2 (the electron-transfer components that the module nominally covers) are encoded. Step S3, the oxygen-activating catalytic terminus that gives the pathway biological meaning, is **missing**. A pathway that supplies electrons to an enzyme that does not exist in the organism cannot be considered satisfiable. UPA00191 as an *alkane-degradation* module is therefore **not satisfiable** in KT2440; the rubredoxin/reductase genes are best modeled as a general electron-transfer couple rather than as members of an alkane-catabolic pathway.

---

## 4. Candidate Genes and Evidence

### 4.1 RubA — PP_5315 (Q88C68) — Rubredoxin *[primary candidate]*

**Likely role:** Genuine single-domain rubredoxin electron carrier; small Fe(3+) redox protein. Evidence is strong that it *is* a rubredoxin; evidence that it feeds an alkane monooxygenase is weak/over-propagated.

**Evidence type and detail (Findings F001, F004):**
- UniProt Q88C68 describes a 55-aa rubredoxin with an Fe(3+) cofactor and **two canonical iron-binding CxxCG motifs** (C6IVCG10 and C38PDCG42).
- Domain signatures: InterPro **IPR024922** (rubredoxin) and **IPR018527** (rubredoxin, iron binding site); Pfam **PF00301**.
- Architecture is a **single rubredoxin domain (~55 aa)**. This is the decisive discriminator: functional alkane-transfer rubredoxins (GPo1 AlkG/Rubredoxin-2, P00272, 173 aa; *P. putida* AlkG, Q9WWW4, 175 aa) are **two-domain ~173–175-aa** proteins whose C-terminal metal domain carries the signature `WICITCGHIYDEAL...CCPDCGATKEDY`. RubA lacks this second domain.
- Anchored pairwise identity: **90%** to a conserved single-domain rubredoxin of the alkane-degrader *Ectopseudomonas (Pseudomonas) oleovorans* (A0A061CWA0, 55 aa), but only **~54–56%** to the alkane-competent two-domain donors (P00272; Q9WWW4). Even the alkanotroph *P. oleovorans* keeps this single-domain rubredoxin as a **separate gene** from its functional AlkG.

**Curation-relevant caveats (Finding F003):**
- All of RubA's pathway/GO annotations are **electronic (IEA)**: `GO:0043448 alkane catabolic process` (IEA:UniProtKB-UniPathway), `GO:0009055 electron transfer activity` (IEA:InterPro), and UPA00191 itself is assigned by **pathway propagation, not experiment**.
- Functional typing (van Beilen 2002, [PMID: 11872724](https://pubmed.ncbi.nlm.nih.gov/11872724/)) places RubA in the **AlkG1 housekeeping class** — conserved across gram-positive and gram-negative bacteria including non-alkane-degraders, and demonstrated *not* to complement alkane hydroxylation. The alkane-catabolic framing is therefore an over-propagation.
- **Status:** **covered** for a generic rubredoxin electron-transfer role; **candidate_uncertain** for the alkane-specific role.

### 4.2 AlkT — PP_5314 (Q88C69) — Rubredoxin–NAD(+) reductase *[adjacent, not in candidate list]*

**Likely role:** FAD-dependent rubredoxin reductase (382 aa); oxidizes NADH and reduces RubA. KEGG **K05297 / EC 1.18.1.1**, KEGG pathway ppu00071. Immediately adjacent to RubA (PP_5315), forming a discrete **two-gene electron-transfer couple**. The other genomic neighbor, PP_5313, is HU-alpha (a nucleoid protein, unrelated), confirming this is a minimal RubA+AlkT unit and **not** part of a larger `alk` operon (Finding F001). Evidence: homology-based; annotation appears correct.

### 4.3 PP_5371 (Q88C12) — fused reductase–rubredoxin *[additional, not in candidate list]*

**Likely role:** A second FAD + Fe **fused** rubredoxin-reductase protein (461 aa; FAD-dependent oxidoreductase domain + rubredoxin domain), KEGG K05297, ppu00071. Provides redundant NAD(P)H:rubredoxin reductase capacity and carries the *same* over-propagated "hydrocarbon hydroxylating system → alkane 1-monooxygenase" text. Represents **paralog ambiguity**: a second, self-contained NADH→rubredoxin relay, reinforcing that KT2440 maintains general rubredoxin-based electron transfer independent of any alkane pathway.

### 4.4 PP_3400 (Q88HF9) — "alkB" homonym *[a trap, not a pathway member]*

**Likely role:** DNA oxidative demethylase / DNA-repair AlkB. UniProt gene name is "alkB," 215 aa, Fe(2+) cofactor, keyword "Dioxygenase," protein existence "Predicted." KEGG assigns ppu:PP_3400 to **K03919** ("DNA oxidative demethylase AlkB," α-ketoglutarate/Fe(II)-dependent dioxygenase, EC 1.14.11.-). This is **not** the membrane non-heme diiron alkane 1-monooxygenase (EC 1.14.15.3). Any automated satisfiability routine that matches on the gene name "alkB" will **falsely** conclude the pathway is complete; PP_3400 must be explicitly excluded (Finding F002).

---

## 5. Gaps, Ambiguities, and Likely Over-Annotations

1. **Terminal-step GAP (decisive).** No true alkane 1-monooxygenase (EC 1.14.15.3) exists in UP000000556. The prototypic system `alkBFGHJKL` + `alkST` is OCT-plasmid-borne in *P. putida* GPo1 / *P. oleovorans*; KT2440 does not carry it and does not grow on n-alkanes. This is the single most important curation fact: **the pathway lacks its catalytic terminus.**
2. **Homonym ambiguity (AlkB).** The DNA-repair AlkB (PP_3400, K03919) and the alkane hydroxylase AlkB (EC 1.14.15.3) share a name but nothing else — same three-letter name, different biochemistry. This is a classic source of false module satisfaction and must be flagged.
3. **Over-propagated alkane annotation on RubA (and PP_5371).** UniProt FUNCTION / UPA00191 / GO:0043448 are all IEA propagations from the GPo1 Alk paradigm, not experimentally supported for KT2440. Single- vs two-domain typing (single-domain, AlkG1-class, 90% to a housekeeping *P. oleovorans* rubredoxin, ~55% to two-domain AlkG2/Rd2) shows RubA is a housekeeping electron carrier; the alkane-specific function does not transfer to KT2440.
4. **Paralog redundancy in the electron-relay layer.** Two reductase routes to rubredoxin (standalone AlkT PP_5314 + fused PP_5371, both K05297) suggest a general/redundant electron-transfer role rather than a single dedicated alkane pathway. KEGG associates them with fatty-acid degradation (ppu00071), not alkane degradation.
5. **Broad EC/GO mappings.** `GO:0009055 (electron transfer activity)` and `GO:0005506 (iron ion binding)` are correct but generic; `GO:0043448 (alkane catabolic process)` is the problematic over-specific term.

---

## 6. Module and GO-Curation Recommendations

| Module step | Recommended status | Rationale |
|-------------|--------------------|-----------|
| Rubredoxin reductase (AlkT, S1) | **covered** | PP_5314 (+PP_5371), K05297 / EC 1.18.1.1 present, adjacent to RubA |
| Rubredoxin electron carrier (RubA, S2) | **covered** as a rubredoxin carrier, but **candidate_uncertain** for the *alkane-specific* role | Gene present and a bona fide rubredoxin; alkane coupling unproven/over-propagated |
| Alkane 1-monooxygenase (S3) | **gap → not_expected_in_target_taxon** | No true AlkB; KT2440 is a non-alkanotroph; PP_3400 is a homonym |
| Whole UPA00191 module | **module_needs_revision** / not satisfiable | Terminal enzyme absent ⇒ pathway not satisfiable; boundary "rubredoxin = alkane degradation" is wrong for this organism |

**GO / annotation actions:**
1. **Downgrade / requalify RubA's alkane annotations.** Recommend removing or qualifying `GO:0043448 (alkane catabolic process)` on RubA / PP_5371 for KT2440; retain generic `GO:0009055 (electron transfer activity)` and `GO:0005506 (iron ion binding)` as the experimentally-defensible core.
2. **Exclude PP_3400 from UPA00191.** Explicitly annotate it as the DNA-repair AlkB (K03919) to prevent name-based false satisfaction.
3. **Mark the module boundary as wrong for this organism.** The generic module presumes a downstream alkane hydroxylase that KT2440 lacks. Either (a) split the "rubredoxin electron transfer" carrier steps into an organism-agnostic redox module decoupled from alkane degradation, or (b) mark UPA00191 `not_expected_in_target_taxon` for KT2440. Consider a **NOT** qualifier or a request for a more accurate "rubredoxin-mediated electron transfer" grouping term.
4. **Consider a housekeeping-rubredoxin module/GO document.** RubA + AlkT (+PP_5371) constitute a general NAD(P)H:rubredoxin electron-transfer couple. A module scoped to "rubredoxin-mediated electron transfer / oxidative-stress redox" (not alkane catabolism) would represent the KT2440 biology more accurately.

---

## 7. Genes to Promote to Full Review

| Gene | Locus | Why promote | Priority |
|------|-------|-------------|----------|
| **rubA** | PP_5315 (Q88C68) | Primary candidate; needs reclassification from "alkane-hydroxylase rubredoxin" to AlkG1-type/generic electron carrier; record the over-propagation caveat | **High** — promote to full `fetch-gene` review |
| PP_5371 | PP_5371 (Q88C12) | Fused reductase–rubredoxin carrying identical over-propagated annotation; correct pathway assignment and clarify paralog relationship with AlkT | Medium |
| PP_3400 | PP_3400 (Q88HF9) | Homonym "alkB"; fix to K03919 DNA-repair dioxygenase and explicitly exclude from the alkane module | Medium (documentation) |
| alkT | PP_5314 (Q88C69) | Confirm as the RubA reductase partner; annotation appears correct | Low |

---

## 8. Mechanistic Model / Interpretation

The evidence converges on a clean, coherent picture. KT2440 possesses the **upstream electron-supply half** of the canonical alkane-oxidation relay but **not the downstream catalytic half**:

```
   Present in KT2440 (covered)                 Absent in KT2440 (gap)
 ┌──────────────────────────────────┐   ┌────────────────────────────────┐
 │ NADH → AlkT (PP_5314, FAD, K05297)│   │  Alkane 1-monooxygenase AlkB    │
 │        ↓                          │   │  (EC 1.14.15.3, membrane        │
 │      RubA (PP_5315, Fe, 55 aa)    │ ✗ │   non-heme diiron, ~400 aa)     │
 │   [AlkG1-type housekeeping Rd]    │   │  → NOT in proteome              │
 │        + PP_5371 (fused, K05297)  │   │  PP_3400 "alkB" = DNA-repair    │
 └──────────────────────────────────┘   │  dioxygenase K03919 (homonym)   │
          general redox / ppu00071        └────────────────────────────────┘
```

**Rubredoxin functional typing** is the linchpin. Van Beilen et al. showed that Alk-rubredoxins divide into AlkG1 (conserved, housekeeping, non-complementing) and AlkG2/Rd2 (alkane-degrader-specific, complementing) classes, and that the alkane-functional donor is the **two-domain** AlkG. RubA's single ~55-aa domain, its 90% identity to a conserved *P. oleovorans* housekeeping rubredoxin, and its ~55% identity to true two-domain AlkG together place it firmly in the AlkG1 class. In a non-alkanotroph like KT2440, the parsimonious interpretation is that RubA + AlkT provide **general NAD(P)H:rubredoxin electron transfer** — a redox-housekeeping function (KEGG associates the reductases with fatty-acid degradation, ppu00071) — and that the UPA00191/alkane annotation was inherited by homology-based propagation from the well-studied GPo1 Alk system rather than reflecting KT2440 biology.

The practical consequence for module curation is that satisfiability cannot be inferred from the presence of rubredoxin + reductase alone. The module's biological meaning depends on the terminal hydroxylase, which is missing. The "alkB" homonym makes automated satisfiability especially treacherous here — a name-based match on PP_3400 would produce a spurious "complete pathway" call.

---

## 9. Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|------|-----------------|------------------------------|
| [11872724](https://pubmed.ncbi.nlm.nih.gov/11872724/) | *Rubredoxins involved in alkane oxidation.* | **Central.** Establishes AlkG1 (housekeeping, non-complementing, conserved in non-degraders) vs AlkG2/Rd2 (alkane-functional, two-domain) classification; underpins F003 and F004 typing of RubA as AlkG1-housekeeping and its over-propagated alkane annotation. |
| [34990970](https://pubmed.ncbi.nlm.nih.gov/34990970/) | *An alkane monooxygenase (AlkB) family…covalently bound electron transfer partners.* | Defines the canonical NADH → AlkT → rubredoxin (AlkG) → AlkB electron chain, situating RubA + AlkT as the reductase/carrier components (F001). |
| [16958757](https://pubmed.ncbi.nlm.nih.gov/16958757/) | *Inactivation of the P. putida cytochrome o ubiquinol oxidase…* | Context on KT2440's respiratory chain and global regulation of "alkane assimilation" genes; indicates alkane-response regulation exists but does not establish a functional alkane hydroxylase. |

**Verbatim support snippets used in the findings:**
- van Beilen ([PMID: 11872724](https://pubmed.ncbi.nlm.nih.gov/11872724/)): *"All alkane-degrading strains contain AlkG2-type Rds, which are able to replace the GPo1 Rd 2 in n-octane hydroxylation. Most strains also contain AlkG1-type Rds, which do not complement the deletion mutant but are highly conserved among gram-positive and gram-negative bacteria."*
- van Beilen ([PMID: 11872724](https://pubmed.ncbi.nlm.nih.gov/11872724/)): *"Complementation tests in an Escherichia coli recombinant containing all Pseudomonas putida GPo1 genes necessary for growth on alkanes except Rd 2 (AlkG) and sequence comparisons showed that the Alk-Rds can be divided in AlkG1- and AlkG2-type Rds."*
- Williams et al. ([PMID: 34990970](https://pubmed.ncbi.nlm.nih.gov/34990970/)): *"Electrons are typically supplied by NADH via a rubredoxin reductase (AlkT) to a rubredoxin (AlkG) to AlkB, although alternative electron transfer partners have been observed."*

**Database anchors:** UniProtKB Q88C68 (RubA/PP_5315), Q88C69 (AlkT/PP_5314), Q88C12 (PP_5371), Q88HF9 (PP_3400); KEGG ppu:PP_5314/PP_5371 → K05297 (rubredoxin–NAD⁺ reductase, EC 1.18.1.1), ppu:PP_3400 → K03919 (DNA oxidative demethylase AlkB); UniPathway UPA00191; comparator sequences A0A061CWA0 (*P. oleovorans* single-domain rubredoxin), P00272 (GPo1 AlkG/Rubredoxin-2), Q9WWW4 (*P. putida* AlkG).

**Evidence provenance summary:**
- **Direct genomic (target-specific), strong:** existence and family of RubA/AlkT/PP_5371 (UniProt/KEGG, KT2440-specific); the "alkB" homonym identity of PP_3400.
- **Experimental but from related organisms, transferred by typing:** AlkG1/AlkG2 complementation biology (van Beilen, GPo1/*P. oleovorans*). Strong for classifying RubA as AlkG1 and for concluding KT2440 lacks the OCT-plasmid Alk system.
- **Inferred from databases/homology, weak for KT2440:** RubA's alkane-specific electron-transfer role (UPA00191, GO:0043448), transferred from GPo1 and undermined by the absence of a terminal AlkB.

---

## 10. Limitations and Knowledge Gaps

1. **No direct KT2440 experiment defines RubA's physiological partner.** The conclusion that RubA is a general redox carrier rather than an alkane-hydroxylase donor is a strong inference (sequence class + absence of AlkB), not a direct enzymatic measurement in KT2440.
2. **Sequence typing used anchored pairwise identities, not a full phylogeny.** A formal maximum-likelihood tree of AlkG1 vs AlkG2 rubredoxins with KT2440 RubA included would harden the classification, though the single-domain architecture already discriminates cleanly.
3. **Proteome-wide search for a cryptic alkane hydroxylase was targeted, not exhaustive.** KT2440 could in principle oxidize hydrocarbons via unrelated enzyme families (e.g., cytochrome P450s, AlmA-type flavin monooxygenases, LadA); these were not systematically enumerated. However, none would satisfy the *rubredoxin-AlkB* UPA00191 model.
4. **Physiological role of the two reductases (PP_5314, PP_5371) is unresolved.** Whether they are functionally redundant, differentially regulated, or serve distinct acceptors is unknown.
5. **Plausible alternative role is inferential.** In diverse bacteria, rubredoxin/rubredoxin-reductase couples act as general NAD(P)H electron carriers and in oxidative/nitrosative-stress defense (e.g., rubredoxin:oxygen oxidoreductase systems; Figueiredo et al. 2013, [PMID: 23564166](https://pubmed.ncbi.nlm.nih.gov/23564166/), in the anaerobe *Desulfovibrio* — so species transfer to the aerobe KT2440 is **weak/uncertain**). This is the most plausible physiological function of the KT2440 RubA+AlkT couple in the absence of an alkane hydroxylase, but there is no direct KT2440 experimental evidence.
6. **UniPathway/GO term structure.** Whether UPA00191 should be formally split (carrier step vs terminal hydroxylase) is a database-modeling question beyond this organism-level review.

---

## 11. Proposed Follow-up Experiments / Actions

**Curation actions (immediate, no bench work):**
1. Requalify Q88C68 (RubA): remove/flag `GO:0043448` and the UPA00191 alkane-catabolic assignments as over-propagated IEA; retain `GO:0009055 electron transfer activity` and `GO:0005506 iron ion binding`.
2. Annotate PP_3400 explicitly as DNA-repair AlkB (K03919) and exclude it from UPA00191 satisfiability logic.
3. Set UPA00191 for KT2440 as **not satisfiable / not_expected_in_target_taxon** with the terminal AlkB step marked **gap**; add a note that the electron-relay genes are present but the pathway lacks its hydroxylase.
4. Promote `rubA` (PP_5315) to full `fetch-gene` review; secondary review of PP_5371 and PP_3400.

**Computational follow-ups:**
5. Build a maximum-likelihood phylogeny of AlkG1/AlkG2 rubredoxins including RubA to formally confirm AlkG1 placement.
6. Systematically scan UP000000556 for any alternative alkane-oxidizing families (P450, AlmA, LadA) to document, definitively, the absence of an alkane hydroxylase — and record that even if found, none would satisfy the rubredoxin-AlkB UPA00191 model.

**Experimental resolution of open questions:**
7. Growth/activity assays: confirm KT2440 cannot use medium- to long-chain n-alkanes as sole carbon source (expected negative), consistent with the absence of a functional Alk pathway.
8. In vitro reconstitution: assemble AlkT/PP_5371 + RubA and test NAD(P)H:rubredoxin electron transfer and candidate physiological acceptors (fatty-acid desaturase/oxidase systems, oxidative-stress partners).
9. Genetics/transcriptomics: phenotype of ΔrubA under oxidative/nitrosative stress vs hydrocarbon exposure; test co-regulation of PP_5314–PP_5315 to identify the true redox partner.

---

## Consensus Verdict

The rubredoxin electron-transfer *components* of UPA00191 are genuinely encoded in *P. putida* KT2440 — RubA (PP_5315), its adjacent FAD rubredoxin–NAD(+) reductase AlkT (PP_5314), and a fused reductase-rubredoxin PP_5371 — so the electron-carrier step is **covered**. But the pathway's terminal alkane 1-monooxygenase (AlkB) is **absent**: the only "alkB"-named gene (PP_3400) is the DNA-repair dioxygenase AlkB (K03919), a homonym. UPA00191 alkane degradation is therefore **not satisfiable** in this non-alkanotroph, and RubA — a conserved single-domain AlkG1-type housekeeping rubredoxin (90% identical to a conserved *P. oleovorans* rubredoxin, only ~55% to two-domain alkane-transfer AlkG/Rd2) — carries a **likely over-propagated** alkane-hydroxylase annotation; it most plausibly functions as a general NAD(P)H:rubredoxin electron carrier.


## Artifacts

- [OpenScientist final report](PSEPK__rubredoxin_electron_transfer__upa00191-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PSEPK__rubredoxin_electron_transfer__upa00191-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:34990970
2. PMID:11872724
3. PMID:23564166