---
title: "Worked example: LDLRAP1"
species: [human]
---

# Worked example: LDLRAP1 / ARH (`Q5SW96`)

Back to the [project page](../MOLECULAR_ADAPTOR_ACTIVITY.md).

Unlike the [GRB2 example](worked-example-GRB2.md), which re-read an existing
review, **LDLRAP1 was unreviewed when this project picked it** — so it is a real
review driven by the project, not a narration of one. It is a clean
`clathrin-cargo adaptor` (a different child from GRB2's signaling adaptor),
a Mendelian disease gene, and compact enough (90 GOA annotations) to review in
full. See the full review of LDLRAP1 (linked from the gene symbol) and its notes
at `genes/human/LDLRAP1/LDLRAP1-notes.md`.

## The gene in one line

LDLRAP1 (ARH) is the cargo-selective **CLASP** (clathrin-associated sorting
protein) that couples the LDL receptor to the clathrin endocytic machinery: its
PID/PTB domain reads the **FxNPxY** internalization motif in the LDLR tail, while
separate C-terminal motifs bind **clathrin** and the **β2-adaptin subunit of
AP-2**, and it binds PtdIns(4,5)P2. Loss of function causes autosomal recessive
hypercholesterolemia [PMID:12221107].

## Starting state (GOA, 90 rows)

- **23 × `GO:0005515` protein binding** (IPI) — almost all from high-throughput
  interactome/two-hybrid screens (HuRI `PMID:32296183`, BioPlex, Lit-BM, …).
- A full set of informative, experimentally-supported adaptor MFs already
  present: `GO:0035615` clathrin-cargo adaptor activity, `GO:0035612` AP-2
  adaptor complex binding, `GO:0030276` clathrin binding, `GO:0050750` LDL
  receptor binding, `GO:0001784` phosphotyrosine residue binding, `GO:0005546`
  PtdIns(4,5)P2 binding — plus two *mis-typed* adaptor MFs (`GO:0035591`
  signaling adaptor activity, `GO:0030159` signaling receptor complex adaptor
  activity).

## What the decision rules produced

| Action | n | Representative calls |
|---|---:|---|
| ACCEPT | 48 | the adaptor MFs and endocytic-contact bindings; endocytosis / LDL-clearance / cholesterol-homeostasis processes; plasma-membrane, coated-vesicle and endosome locations |
| REMOVE | 17 | bare `protein binding` rows from interactome screens (protein-binding policy) |
| KEEP_AS_NON_CORE | 10 | AP-1 binding, broad cholesterol-transport/metabolism, APP-related and regulatory-framing rows |
| MODIFY | 9 | see below |
| MARK_AS_OVER_ANNOTATED | 6 | neurofilament/axon localisation; vague "regulation of protein binding"; cytokine-response and VSMC-proliferation rows that make LDLRAP1 the *target* of regulation, not a participant |

The nine `MODIFY` calls are the instructive part, and they exercise two
different senses of the action:

1. **Partner → specific binding (refinement of `protein binding`).** Six
   `GO:0005515` rows whose interactor is **AP2B1 / β2-adaptin** (`P63010`) were
   recast to `GO:0035612` AP-2 adaptor complex binding — the same
   "IntAct rows are a partner list" move as in GRB2, here consolidating six
   screen hits onto the informative term.
2. **Lateral correction of a mis-typed adaptor.** `GO:0035591` signaling adaptor
   activity and `GO:0030159` signaling receptor complex adaptor activity were
   changed to `GO:0035615` clathrin-cargo adaptor activity. LDLR endocytosis is
   **not** a signaling event; the same experiments (`PMID:12221107`,
   `PMID:15166224`) show LDLRAP1 coupling LDLR to the endocytic machinery, so the
   signaling-branch terms are the wrong child and the clathrin-cargo child is
   right. This is `MODIFY` as a lateral/branch correction, not a generalise/
   specialise refinement.
3. One location refinement: `GO:0005737` cytoplasm → `GO:0005829` cytosol (the
   gene's own IDA term).

Core functions settled on two: `GO:0035615` **clathrin-cargo adaptor activity**
(the integrative function — clathrin + AP-2 + PIP2 contacts) and `GO:0050750`
**LDL particle receptor binding** (the PTB domain reading the LDLR NPxY motif for
cargo selection).

> **Term-precision note.** An earlier draft used `GO:0001784` phosphotyrosine
> residue binding for the cargo-recognition core function. That is wrong for
> LDLRAP1: its ARH/Dab2-class PID/PTB domain binds the **unphosphorylated** FxNPxY
> motif (PMID:12451172, *"PTB domains bind to the consensus sequence FXNPXY"*) —
> "PTB" is a fold name inherited from the phospho-dependent Shc/IRS class, not a
> claim of phosphotyrosine binding here. `core_functions` ids are author-supplied
> and hard-validated, so the core function now uses `GO:0050750` (already present
> as an IPI row); the GOA `GO:0001784` IDA row is kept non-core by deference to the
> curator. Contrast GRB2, where `GO:0001784` is genuinely phospho-dependent (its
> SH2 domain) — the same term is right there and wrong here.

## What this example adds beyond GRB2

- **It drove a real review** of a previously unreviewed gene, now `COMPLETE`
  and validating, rather than illustrating one.
- **`MODIFY` is not only for `protein binding`.** The most consequential calls
  here corrected two *existing, experimentally-evidenced* adaptor annotations
  that sat in the wrong branch (signaling vs clathrin-cargo). A reviewer working
  the core_adaptor worklist should expect mis-typed adaptor children, not just
  bare `protein binding`.
- **Over-annotation has a characteristic shape.** The rows marked over-annotated
  were ones where LDLRAP1 is the *object* of a process (a miRNA target; a
  downstream effect on smooth-muscle proliferation) — the `NEW`/participation
  test from CLAUDE.md applied in reverse to existing rows.
