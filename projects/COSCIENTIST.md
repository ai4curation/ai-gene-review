---
title: "COSCIENTIST"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [human, ECOLI, MYCTU, METJA, SCHPO, worm]
---

# COSCIENTIST

**Using an autonomous AI "co-scientist" (OpenScientist) as an independent
bioinformatician to test specific gene-function hypotheses that the literature
cannot settle — and wiring the verdicts back into curated GO reviews.**

## Motivation

Most AI assistance in curation is literature synthesis: read the papers, summarize,
cite. That is valuable but it cannot answer questions the literature never asked —
"does this orphan fold imply a function?", "are the catalytic residues actually
present?", "is this annotation a phylogenetic over-propagation?" Those require
*running analyses*, not just reading.

[OpenScientist](https://www.openscientist.io/) is an autonomous research agent that
can execute code (structure fetches, Foldseek searches, sequence/active-site
analysis, plotting) across several iterations and emit a cited report plus
provenance artifacts. This project treats it as a blinded, independent
bioinformatics scientist exploring a single hypothesis `gene G has function F`, then
compares its conclusion against held-out local analyses and curator judgment, and
folds the result into the gene's `-ai-review.yaml`.

Operational conventions live in the `openscientist-hypothesis` skill. The driver is
`just gene-hypothesis-research openscientist <ORG> <GENE> --focus-type free-text
--hypothesis "…"` (defaults: 3 iterations, 2 h job timeout).

## Where it adds the most value

Across runs, the highest-value, least-redundant results share a signature: **the
question is not answerable from papers alone**. When OpenScientist is asked a
literature-settleable core-vs-non-core question it tends to (correctly) reproduce
the existing review; when asked a compute-requiring question it produces genuinely
new evidence. So we deliberately steer it toward:

- uncharacterized / orphan proteins with a predicted-but-unverified function;
- suspected over-annotations propagated by IEA/IBA/ISS inference;
- "protein binding"-style uninformative molecular functions;
- pseudoenzyme / missing-catalytic-residue questions;
- paralog-discrimination by sequence or structure.

A recurring, high-value pattern is catching a **systematic mis-annotation**: an
error that has propagated from a reference protein to a whole family or to a
paralog, not just the gene under review.

## Completed runs

### Compute-requiring batch (structure / sequence)

| Gene | Hypothesis | Verdict (compute-driven) | Review action |
|------|-----------|--------------------------|---------------|
| METJA/MJ1511 | Does it retain AhpD oxidoreductase activity (GO:0016491, IBA) or is it a pseudoenzyme? | **Pseudoenzyme.** AlphaFold: the two cysteines are 36.5 Å apart with zero histidines — no CXXC, no proton relay. Paralog MJ0742 carries the same erroneous annotation. | `GO:0016491` **UNDECIDED → REMOVE**; flagged systematic methanogen-CMD mis-annotation |
| ECOLI/yrhB | Is the ISS Imm35 immunity / peptidase-inhibitor function real? | **Fold correct, function over-annotated.** Imm35 fold confirmed (AlphaFold pLDDT 95.2, Foldseek), but no Imm35 family member has experimental immunity evidence and there is no adjacent toxin gene; direct assays show chaperone activity (applies to K12 — 100% identical to BL21). | Immunity tempered; added experimentally-grounded `GO:0044183` (protein folding chaperone) + `GO:0042026`; core function reassigned |
| MYCTU/Rv0898c | Can the DUF2630 orphan fold be assigned a molecular function? | **Partially supported — keep ND.** Fold is classifiable (two-helix hairpin; weak uL29 hit at 27% identity, twilight zone) but function is not inferable (CATH 1.10.287 spans >600 superfamilies; motif CWDLLRQRR has no characterized match). | `GO:0003674` ND **retained**, rationale strengthened |

### Earlier hypothesis runs (core-vs-non-core / over-annotation)

| Gene | Hypothesis | Verdict | Note |
|------|-----------|---------|------|
| SCO1 | `GO:0016531` copper chaperone = core MF | Supported (high) | flagged SCO2 paralog over-annotation; IEA→IMP upgrade lead |
| SCHPO/pmp20 | `GO:0008379` thioredoxin peroxidase | Over-annotated → remove | reference *refutes* activity; GO logic conflict (NOT on parent) |
| IL21 | `GO:0042102` pos. reg. T-cell proliferation = core | Keep as non-core | B-cell/Tfh axis is the signature function |
| STAT3 | `GO:0030335` pos. reg. cell migration = core | Non-core | bidirectional migration effect = downstream, not core |
| CFAP300 | scaffold/adaptor/chaperone in dynein preassembly? | Unresolvable; add BP | "protein binding" confirmed uninformative; structural compute |

**Evidence integrity.** Across all runs, cited PMIDs were real, on-target, and
verbatim-quotable; no hallucinated citations were found. Every `supporting_text`
wired into a review is checked as a verbatim substring of its source.

## Beyond structure: other informatics that could decide a call

The batch above leans heavily on AlphaFold/Foldseek because those questions were
structural. But the same "ask a question the literature can't settle, then compute"
approach applies to other data types. Candidate genes where a **non-structural**
analysis would be the deciding evidence:

### A. Disputed membrane topology / transmembrane proteins
*Resolvable by sequence-topology tools: DeepTMHMM, SignalP, Phobius, positive-inside / orientation analysis.*

| Gene | Disputed point | Method | Rank |
|------|----------------|--------|------|
| CLCN7 | `GO:0030321` transepithelial chloride transport — endolysosomal antiporter vs plasma-membrane epithelial channel | DeepTMHMM/Phobius topology + transporter-vs-channel mechanism | HIGH |
| WFS1 | multi-pass ER membrane topology; EF-hand / `GO:0005516` calmodulin binding (UNDECIDED) | DeepTMHMM 9-TM topology, signal-anchor orientation, EF-hand motif scan | MED |
| SORL1 | disputed subcellular localizations (`GO:0005641` nuclear envelope lumen, UNDECIDED; secretory-granule/MVB) | signal peptide + domain-architecture topology; localization-prediction consensus | MED |

### B. Transcription factors / DNA-binding with disputed function
*Resolvable by motif analysis (JASPAR) + ChIP/regulatory databases (ChIP-Atlas, ReMap) + co-expression/regulon inference (ARACNe/GENIE3) — not structure.*

| Gene | Disputed point | Method | Rank |
|------|----------------|--------|------|
| worm/skn-1 | isoform-specific regulons & `GO:0006417` translation regulation (UNDECIDED); A/B/C isoforms differ | isoform-resolved ChIP/CUT&RUN + tissue co-expression to partition regulons | HIGH |
| ASCL1 | pioneer-factor claim; direct vs indirect targets; neuronal vs SCLC E-box preference | ChIP-Atlas peaks + motif enrichment + enhancer/ATAC co-localization | HIGH |
| CTBP1 | corepressor vs context-specific coactivator (`GO:0003713`); which regulons | ReMap/ChIP-Atlas target sets + differential co-expression by cell type | MED |

### C. Expression-data-resolvable annotations
*Resolvable by tissue/cell-type specificity and co-expression atlases: Bgee, Expression Atlas, single-cell references, GTEx.*

| Gene | Disputed point | Method | Rank |
|------|----------------|--------|------|
| WFS1 | `GO:0031016` pancreas development — developmental role vs β-cell *degeneration* (ER-stress apoptosis) | developmental vs adult β-cell expression timecourse; single-cell ER-stress signatures | MED |
| worm/skn-1 | are isoform modules (ASI chemosensory / intestinal detox / ER stress) distinct or context-induced | tissue-specific + developmental-stage expression; condition-induction profiles | HIGH |
| STAT3 | already-resolved migration call could be generalized: which processes are direct vs co-expression-driven | regulon/co-expression to separate direct targets from convergent phenotypes | LOW |

> These are leads, not yet run. The next OpenScientist batch should pick from the
> HIGH rows so the deciding evidence is a database/compute analysis the agent can
> actually perform, rather than a wet-lab experiment.

## Operational lessons

- **Give jobs ample time.** Real 3-iteration runs take ~50–90 min; structural runs
  routinely exceed the upstream 3600 s default and get cancelled mid-analysis. The
  `just` recipes now inject `--param timeout=7200` (the API ceiling, `le=7200`) and
  the subprocess wall (`--timeout-seconds`, default 8100 s) is kept above it.
- **A job can exit 0 yet write nothing.** Always confirm `openscientist.md` (and the
  `openscientist_artifacts/` dir) exist. Two empty-output failure modes: timeout
  (`… timed out after Ns … cancelled` → raise the timeout) and a transient
  server-side LLM error (`… Request ID: req_…` → re-run; if it recurs for the same
  gene, treat as a persistent upstream issue and report rather than retry forever).
- **Keep local bioinformatics held out.** Do not feed existing `*-bioinformatics/
  RESULTS.md` into the prompt; compare against it after the run.
- **Verify quotes.** Every `supporting_text` added to a review must be a verbatim
  substring of its cited source; this is enforced for both publication PMIDs and the
  `file:…/openscientist.md` report itself.

## Status & next steps

- [x] Compute-requiring structural batch (MJ1511, yrhB, Rv0898c) run, reviewed, and
      wired into `-ai-review.yaml`.
- [x] Timeout/failure-mode handling hardened in the skill + justfile.
- [ ] Run the HIGH non-structural leads (skn-1, ASCL1, CLCN7) to exercise
      topology / regulatory / expression informatics.
- [ ] Write up the systematic-mis-annotation cases (MJ1511/MJ0742; pmp20 family) as
      examples of family-level error propagation caught by compute.
