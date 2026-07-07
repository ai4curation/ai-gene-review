---
title: "Dark-Gene Batch Reviews: Curation Highlights"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [worm, yeast]
autolink_gene_symbols: false
---

# Dark-Gene Batch Reviews: Curation Highlights

Three batched review campaigns targeted deliberately *understudied* genes — the population
where function knowledge gaps concentrate — rather than the well-annotated core:

| Campaign | Organism | Genes | Selection basis |
|---|---|---|---|
| CAEEL | *C. elegans* (`worm`) | 50 | Unreviewed members of the flagship CAEEL pathway projects (cilia/IFT, mitophagy, proteostasis, UPR, surveillance immunity, P-granule) |
| YEAST | *S. cerevisiae* (`yeast`) | 50 | Named-but-dark genes from the SGD GAF: standard gene name, **zero experimental-evidence annotations**, few informative GO terms |
| POMBE | *S. pombe* (`SCHPO`) | 20 | Named-but-dark genes from the PomBase GAF, same darkness filter |

Each gene received a full annotation review plus a literature-grounded `knowledge_gaps`
section (the point of the exercise — see the [parent project](../FUNCTION_KNOWLEDGE_GAPS.md)).
Beyond the gap records themselves, the reviews surfaced recurring, generalizable curation
findings. Those patterns are collected here because they are the concrete argument for *why*
dark genes need human-grade review rather than electronic propagation.

## 1. Identity correction before curation

Dark genes are disproportionately mislabeled — a "standard name" or a family hint can point at
the wrong biology. Grounding every review in the actual UniProt/PomBase record (not the symbol
or a prior assumption) caught several outright misassignments *before* they could drive wrong
annotations:

- **`sel0` (pombe, SPAC20G4.05c)** — not a Sel1-repeat / SEL1L ERAD protein as the name suggests,
  but **Selenoprotein O**, a mitochondrial protein AMPylase / adenylyltransferase (SELO family,
  pseudokinase fold). Entire review reframed around AMPylation.
- **`mtl3` (pombe, SPBC215.13)** — not the Mtr4-like MTREC RNA helicase (that is `mtl1`), but a
  **Mid2-like GPI-anchored plasma-membrane cell-wall stress sensor** with no catalytic domain.
- **`spa1` (pombe, SPBC577.14c)** — not the mammalian Rap-GAP SIPA1/SPA1 despite the shared
  symbol, but **ornithine decarboxylase antizyme** (an ODC inhibitor).
- **`knh4` (pombe, SPBC1E8.05)** — not a Knr4/Smi1 protein, but a **Kre9/Knh1-family β-glucan
  cell-wall glycoprotein**.
- **`MNN14` (yeast, YJR061W)** — not a GT15/MNN1 α-1,3-mannosyltransferase, but a **LicD-family
  mannosyl-phosphate transferase** (activity later added from primary literature; see §4).
- **`ppgn-1` (worm)** — the flagship-project framing implied an immunity effector; the record
  shows the **paraplegin / SPG7 m-AAA protease** (a reproducible motif scan confirmed intact
  catalytic residues).
- **`MCO14` (yeast)** — `fetch-gene` failed on the symbol; resolved via SGD to **YHL018W**, a
  PCD/DCoH-family protein. (Yeast/pombe standard names frequently are not in UniProt's gene
  line — the pipeline now falls back to the systematic name + `--uniprot-id`.)

## 2. Pseudoenzyme detection

A conserved catalytic *fold* is routinely over-annotated with the ancestral catalytic *activity*
even when the catalytic residues have degenerated. Inline domain analysis (reading the UniProt
features and checking the specific catalytic motif) flagged several:

- **`KDX1` (yeast)** — protein-kinase fold but activation-loop **DFG→NFG** and catalytic-loop
  **HRD→HCD**; a catalytically inactive **pseudokinase**. Nine propagated catalytic-kinase MF/BP
  terms marked as over-annotations; its real role is a non-catalytic Swi4/Rlm1 scaffold.
- **`OCA6` (yeast)** — PTP/DSP fold but the invariant CX5R catalytic arginine is replaced (→Ile);
  a likely **pseudophosphatase**; the "protein tyrosine phosphatase activity" IEA flagged.
- **`GPM3` (yeast)** — retains the phosphoglycerate-mutase histidines yet is experimentally
  **inactive as a mutase**; glycolysis/mutase terms demoted with `propagation_review`.
- **`wago-4` (worm)** — an Argonaute lacking the catalytic tetrad; the endonuclease/"slicer" term
  removed on biological grounds, `miRNA binding` corrected to `siRNA binding` (binds 22G-RNAs).

## 3. Family over-propagation removed or demoted

The dominant false-positive class for dark genes is IBA/ISS transfer from a characterized
paralog or distant ortholog whose function does not hold for the target:

- **`fis-1` (worm)** — contrary to the FIS1 family's fission-receptor reputation, worm FIS-1 is
  **not required** for mitochondrial or peroxisomal fission (LOF is silent); family fission
  terms kept non-core, and its supported role (mitophagy coupling) added as NEW.
- **`ILT1` (yeast)** — PQ-loop transporter annotated as a *vacuolar* basic-amino-acid transporter
  by propagation from Ypq1/2; ILT1 is experimentally **plasma-membrane** and in a distinct
  uncharacterized subfamily — vacuolar terms removed.
- **`LEE1` (yeast)** — makorin-family; ubiquitin-ligase activity propagated from RING-containing
  metazoan makorins, but LEE1 has **no RING domain** (confirmed by direct InterPro query) —
  ligase terms marked over-annotated; only its CCCH zinc-finger zinc-binding kept.
- **`NVJ3` (yeast)** — PI3P-binding transferred from paralog Mdm1, but NVJ3 shares only the PXA
  domain and **lacks the PX domain** that carries the activity — removed.
- **`AAD3` (yeast)** — aryl-alcohol dehydrogenase activity propagated from a lignin-degrader
  enzyme; the AAD deletants are phenotype-null and budding yeast is not a lignin degrader —
  demoted to the honest superfamily-level oxidoreductase term.
- **`THI22` (yeast)** — HMP-P kinase activity: the one direct assay found **no activity** for
  THI22, so the propagated kinase term was marked over-annotated (residues intact → not a
  pseudoenzyme, but activity unproven).
- **`gpa-12` (worm)** — Gα subunit carrying propagated Gs/Gi adenylate-cyclase-modulating and
  D5-dopamine-receptor-binding terms wrong for the G12/13 subfamily — removed.

In every case the annotation was flagged as electronic over-propagation with a structured
`propagation_review`, **not** by overruling an experimental annotation.

## 4. Evidence-grounded upgrades

Dark-gene review is not only subtractive; deep reading also finds well-supported functions
*missing* from GOA:

- **`MNN14` (yeast)** — a falcon-surfaced, PubMed-verified paper (Kang et al. 2021) shows
  recombinant Mnn14 transfers mannose-phosphate from GDP-mannose to high-mannose N-glycans;
  `mannosylphosphate transferase activity` (GO:0000031) added as an evidence-backed NEW MF.
- **`spa1` (pombe)** — ornithine-decarboxylase-inhibitor activity confirmed directly for the
  fission-yeast protein (recombinant Spa1 inhibits *S. pombe* ODC) and kept as the core function.

## 5. Fabrication guardrails held

The `supporting_text`-must-be-verbatim rule and independent fact-checking caught deep-research
errors before they entered a review:

- **`tin-44` (worm)** — a falcon report's "RNAi extended lifespan 11.1%" was a hallucination; the
  cached full text actually groups tin-44 among lifespan-*shortening* import knockdowns. Removed.
- **`NIT1` (yeast, YIL164C)** — a falcon report conflated NIT1 with its dGSH-amidase paralog
  NIT2/YJL126W; the misattributed activity claim was fact-checked out (catalytic-residue numbering
  mismatch) and the reference flagged `MISCITED`.
- **`prg-2` (worm)** — correctly **failed** rather than being fabricated: it is a WormBase
  pseudogene with no UniProt entry and zero GO annotations; substituted with another gene.
- **`LPX2` (yeast)** — a rebase accident degraded a protected publication cache to abstract-only,
  which had let the review claim the Ploier 2013 full text was "inaccessible." Restoring the
  full text showed that paper *tested* Ykl050c and found **no** in-vivo lipolytic activity —
  correcting the review and strengthening its MF-unknown conclusion.

## Why this matters

Across 120 dark genes, the value was rarely a brand-new function statement; it was (a) getting the
protein's *identity* right, (b) refusing to inherit a paralog's activity through a degenerate fold
or a wrong-subfamily transfer, and (c) writing down, with provenance, exactly what remains unknown.
That is the raw material the [Function Knowledge Gaps](../FUNCTION_KNOWLEDGE_GAPS.md) register is
built from.
