---
title: "Ortholog Conjecture Project"
marp: true
theme: default
paginate: true
backgroundColor: #fff
style: |
  section { font-size: 24px; }
  h1 { color: #2c3e50; }
  h2 { color: #34495e; }
  table { font-size: 18px; }
  section.lead h1 { font-size: 48px; }
---

<!-- _class: lead -->

# Ortholog Conjecture Project

Do orthologs really retain function better than paralogs? — the conjecture that underpins automated annotation

Chris Mungall | AI-Assisted Gene Review

2026-06-22

---

## Why it matters

- The **ortholog conjecture (OC)** posits that orthologs (separated by speciation) tend to retain more similar functions than paralogs (separated by duplication) at the same evolutionary distance.
- This assumption **underpins many automated functional annotations** and cross-species inference pipelines.
- The OC **remains debated**: different data types, bias controls, and evaluation metrics can yield opposite conclusions.
- Consequence: the OC is not just theoretical — it affects **annotation propagation, evidence reliability, and the risk of over-annotation**.

---

## How orthology appears in GO annotation

GO annotations explicitly encode *how* an inference was made:

- **`ISO`** — evidence code for inferences from sequence orthology.
- **Phylogenetic annotations (PAINT/PANTHER, IBA/IBD)** — explicit ancestral inference with traceability to experimental evidence. [GO_REF:0000033]
- **Automated ortholog transfers** documented in GO_REFs:
  - OrthoMCL-based ISO transfers [GO_REF:0000101]
  - Ensembl Compara orthology transfers yielding IEA [GO_REF:0000107]

These mechanisms make the OC a practical concern, not just a theoretical one.

---

## The approach (science-first)

- This project is about the **science** of orthology vs. functional divergence and how to measure it **without circularity or annotation bias**.
- It is **not** primarily a curation rulebook — repo-level guidelines cover that.
- GO context and evidence codes are **inputs**; the emphasis is a **reproducible, unbiased analysis** of functional conservation/divergence.
- Built on the **AI gene review framework** to assemble literature-backed cases and test how evidence filters change conclusions.

---

## Project goals

- Assemble **literature-backed examples** of functional divergence among orthologs (neofunctionalization, subfunctionalization, domain loss, subcellular relocalization).
- Build an **"open world" curation lens**: treat missing annotations as *unknown*, not absence; separate *lack of evidence* from *evidence of loss*.
- Develop **unbiased similarity metrics** controlling for annotation bias (authorship, term frequency, propagated annotation bias); compare GO-based vs. expression/phenotype signals.
- Identify families where **orthology-based transfer overstates conservation**, and quantify how often under different evidence filters.

---

## The debate: conflicting conclusions

| Direction | Finding | Reference |
|---|---|---|
| Challenges OC | Within-species paralogs can show *higher* functional similarity than orthologs (GO + microarray); "cellular context" hypothesis | PMID:21695233 |
| Methodological caution | GO is incomplete & biased; GO-based OC tests can be confounded — GO argued *inappropriate* for testing OC | PMID:22359495; PMID:23209392 |
| Supports OC | With confounders controlled, orthologs show *higher* functional similarity (esp. cellular component) | PMID:22615551 |
| Supports OC | RNA-seq: higher expression similarity among orthologs than within-species paralogs | PMID:23209392 |

Same question, opposite answers — depending on data and bias controls.

---

## Open-world metrics (draft spec)

**Inputs:** ortholog pairs/groups (1:1 → 1:many → many:many); GO annotations w/ evidence codes & dates; optional expression/phenotype matrices.

**Evidence tiers (configurable):**
- `experimental_only` — EXP, IDA, IMP, IGI, IEP
- `curated_plus` — + IBA/IBD/IC/ISS/ISO
- `all_including_iea` — + electronic, to quantify propagation effects

**Goal:** avoid penalizing missing annotations (unknowns) while still capturing divergence signals.

---

## Similarity metrics & bias controls

**Open-world similarity metrics:**
- **Asymmetric containment** |A ∩ B| / |A| — do not penalize missing in B.
- **Symmetric overlap (Jaccard)** |A ∩ B| / |A ∪ B| — conservative baseline.
- **IC-weighted overlap** — weight by information content to reduce generic-term bias.

**Bias controls:**
- Author/publication bias — downweight same-source annotations across pairs.
- Term-frequency bias — inverse frequency or ontology depth.
- Propagation bias — compare `experimental_only` vs. `curated_plus` vs. `all_including_iea`.

**Reporting:** separate MF/BP/CC; stratify by orthology class; show "delta" when ISO/IEA added.

---

## Curated divergence cases (1/2)

| Gene | Case | Type | Evidence |
|---|---|---|---|
| **CMAH** | Human CMAH inactivated; nonhuman primates retain function (lost 92-bp exon → no Neu5Gc) | Lineage-specific LOF | PMID:9751737; PMID:11562455 |
| **UOX** | Urate oxidase inactivated in hominoids, functional in many mammals; independent gibbon inactivation | LOF, independent events | PMID:11961098 |
| **GULO/GULOP** | Humans/primates lack functional GULO → no endogenous vitamin C | LOF / pseudogenization | PMID:1962571; PMID:10572964 |

---

## Curated divergence cases (2/2)

| Gene | Case | Type | Evidence |
|---|---|---|---|
| **CDC14** | Budding yeast Cdc14 essential for mitotic exit; fission yeast/vertebrate orthologs not required, different roles | Functional role shift | PMID:20720150 |
| **Arabidopsis vs. A. lyrata co-orthologs** | Multi-copy ortholog groups diverge in expression & complementation; nonexpressologs fail to complement | Neo-/nonfunctionalization | PMID:27303025 |

---

## Large-scale datasets to mine

- **Yeast–human replacement assays:** only **~47%** of essential yeast genes are functionally replaceable by their human orthologs; replaceability **clusters by biological module** → a divergence filter for ortholog transfer. [PMID:25999509]
- **Expressolog dataset (Arabidopsis vs. A. lyrata):** **one-to-one** groups show higher expression correlation than one-to-many or many-to-many; includes gene-level validation via complementation. [PMID:27303025]

These provide ground-truth signals beyond GO for benchmarking metrics.

---

## Challenges

- **Circularity & annotation bias:** GO is incomplete and biased by study design and annotation practice — negative results can be misleading. [PMID:22359495; PMID:23209392]
- **Conflicting conclusions** depend on data type, bias controls, and evaluation metrics (microarray vs. RNA-seq; GO vs. expression).
- **Open-world problem:** missing annotation ≠ absence of function; must separate *lack of evidence* from *evidence of loss*.
- **Boundary cases** (lineage-specific LOF: UOX, GULOP) show orthology does not guarantee retention — but are excluded from subtle-divergence metrics.

---

## Conclusions, status & future directions

**Status (last updated 2026-02-09):**
- [x] Seed list of divergence examples with citations (v0.1)
- [ ] Define open-world metric set and data filters
- [ ] Select ortholog datasets and clades for pilot analysis

**Workplan ahead:**
1. Build ortholog sets across well-studied clades; tag dominant evidence codes (ISO/IEA vs. IBA/IBD vs. experimental).
2. Compute similarity with experimental-only, then add ISO/IBA to measure transfer impact.
3. Cross-check GO-based similarity against RNA-seq / phenotype signals.
4. Summarize divergence rates + a **"bias checklist"** for correct interpretation.
