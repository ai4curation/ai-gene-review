---
title: "COSCIENTIST"
marp: true
theme: default
paginate: true
backgroundColor: #fff
---

<!-- _class: lead -->

# COSCIENTIST

## An AI co-scientist as an independent bioinformatician for GO curation

Running OpenScientist on focused gene-function hypotheses the literature
cannot settle — and wiring the verdicts back into curated reviews

AI-Assisted Gene Review

---

## The gap

Most AI curation help is **literature synthesis**: read papers, summarize, cite.

It cannot answer questions the literature never asked:

- Does this orphan fold imply a function?
- Are the catalytic residues actually present?
- Is this annotation an over-propagated electronic inference?

These need **running analyses**, not just reading.

---

## The approach

Treat **OpenScientist** as a blinded, independent bioinformatics scientist
testing one hypothesis: *gene G has function F*.

- Executes code over iterations: structure fetches, Foldseek, sequence /
  active-site analysis, plotting — with provenance artifacts
- **Holdout discipline:** local `*-bioinformatics/RESULTS.md` is withheld from
  the prompt, then compared after the run
- Verdict + verbatim-checked quotes wired into `GENE-ai-review.yaml`

`just gene-hypothesis-research openscientist <ORG> <GENE> --hypothesis "…"`

---

## Where it adds the most value

Steer it at questions **the papers can't decide**:

- uncharacterized / orphan proteins (predicted-but-unverified function)
- suspected over-annotations (IEA / IBA / ISS propagation)
- uninformative "protein binding" molecular functions
- pseudoenzymes / missing catalytic residues
- paralog discrimination

Highest-value pattern: catching a **systematic mis-annotation** that propagated
across a family or paralog.

---

## Completed runs — structure / sequence

| Gene | Hypothesis | Verdict | Action |
|------|-----------|---------|--------|
| MJ1511 | AhpD oxidoreductase (IBA)? | Pseudoenzyme (Cys 36.5 Å apart, no His) | REMOVE |
| yrhB | Imm35 immunity (ISS)? | Fold yes, function no → chaperone | MODIFY |
| Rv0898c | DUF2630 → a function? | Fold classifiable, function not | keep ND |
| Rv0311 | Intein splicing (IEA)? | Over-annotated | REMOVE |
| RvY_17310 | Tardigrade Cu/Zn-SOD? | **Supported** — full active site retained | keep |

---

## Completed runs — core-vs-non-core / over-annotation

| Gene | Hypothesis | Verdict |
|------|-----------|---------|
| SCO1 | copper chaperone = core MF | supported (high) |
| pmp20 | thioredoxin peroxidase | over-annotated → remove |
| IL21 | pos. reg. T-cell proliferation = core | keep as non-core |
| STAT3 | pos. reg. cell migration = core | non-core (bidirectional) |
| CFAP300 | scaffold/adaptor/chaperone? | unresolvable; add BP |

---

## Systematic mis-annotation catches

The highest-value outcomes were **family-level errors**, not single genes:

- **MJ1511 → MJ0742**: same erroneous oxidoreductase IBA on a catalytically
  dead paralog (crystal structure available)
- **CLCN7**: transepithelial-transport term traced to a ComplexPortal
  family-level sentence → propagated by PANTHER IBA to **~1,198 ortholog
  annotations**
- **RvY_17310**: independently flagged the *degenerate paralogs*
  (RvY_13070 / RvY_13431) while clearing the target itself

---

## Finding: execution depends on the question

- **Structural questions → it executes code** (AlphaFold fetch, Foldseek,
  geometry) with provenance artifacts
- **Topology / regulatory / motif questions → it mostly reasons** over domain
  architecture, sorting motifs, ChIP/E-box, InterPro/PANTHER families

Verdicts were strong either way — but the *provenance* differed.

---

## Closing the gap: template tweak + A/B test

Tweaked the prompt to **execute** hypothesis-matched analyses (and save
provenance), with a hard *never-fabricate / say-so-if-web-only* clause.

**CLCN7 A/B — only the template changed:**

| | Before | After |
|---|---|---|
| Provenance | none | **Kyte–Doolittle hydropathy from UniProt seq** |
| Verdict | over-annotated | identical |
| Runtime | 41 min | 24 min |

Topology behaviour is **promptable**; ChIP/expression remain tool-access-limited.

---

## Proteostasis Network use cases

The PN reviewers assigned families by **InterPro / CDD domain** — *not* by
structure or catalytic-residue analysis. That layer is exactly the gap.

- **HSPA12A / HSPA12B** — HSP70 by architecture; do they retain folding
  machinery? (their InterPro set lacks HSP70-specific domains HSPA8 has)
- **NPLOC4** — `DUB > MPN`: real JAMM metalloprotease, or pseudo-DUB?
- **AARSD1** — AlaX editing residues present vs HSP90-cochaperone artifact?
- **GABARAPL3** — ATG8 ortholog flagged "pseudogene": functional?

---

## Evidence integrity & operational lessons

- **No hallucinated citations** across runs; every wired `supporting_text` is a
  verbatim substring of its source
- **Give jobs time**: ~50–90 min; inject `timeout=7200` (API max) + subprocess
  wall 8100 s; 3600 s default cancels structural runs mid-analysis
- **Empty output ≠ done**: timeout vs transient `req_…` LLM error; clear the dir
  and re-run
- **Holdout** local bioinformatics for post-run comparison

---

<!-- _class: lead -->

## Status

8 reviews wired in; new batch (DNAJC28, C18orf21, HSPA12A/B, NPLOC4, AARSD1)
in flight.

Next: run MED non-structural leads; write up the systematic-mis-annotation
cases; resolve the RvY_17310 vs prior-review disagreement.

**Ask a question the literature can't settle — then compute.**
