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

📊 **Slides:** [COSCIENTIST-slides](COSCIENTIST/slides/COSCIENTIST-slides.md)
(Marp; regenerate the PDF with `just gen-project-slides COSCIENTIST`).

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

### Non-structural batch (topology / regulatory / motif)

A second batch deliberately targeted questions decidable by *non-structural* data
to test whether the agent exercises those data types as well as it does structure.

| Gene | Data type | Verdict (compute/reasoning-driven) | Review action |
|------|-----------|------------------------------------|---------------|
| worm/skn-1 | regulatory / domain | **Over-annotated.** Bzip/CNC transcription factor with no RNA-binding or translation-factor domain; the IEA `GO:0006417` (regulation of translation) comes from UniProt keyword KW-0810, conflating SKN-1 being activated *by* translation inhibition with directly regulating it. | `GO:0006417` **UNDECIDED → REMOVE** |
| CLCN7 | localization / sorting-signal | **Over-annotated — second systematic catch.** ClC-7 is an endolysosomal antiporter (N-terminal dileucine + acidic-cluster sorting motifs, absent from plasma-membrane paralogs CLCNKA/KB); `GO:0030321` traces to a ComplexPortal family-level intro sentence propagated by PANTHER IBA to **~1,198 ortholog annotations**. | `GO:0030321` **→ REMOVE** |
| ASCL1 | TF / ChIP / motif | **Over-annotated.** ASCL1 binds DNA as a functionally obligate class II bHLH heterodimer with class I E-proteins (TCF3/E2A, TCF4/E2-2, TCF12/HEB); the IEA `GO:0042802` (identical protein binding, implying homodimer) is an Ensembl-Compara transfer; homodimers form only in vitro. | `GO:0042802` **→ MODIFY** → `GO:0046982` heterodimerization |

**Execution behaviour differs by question type.** The structural runs *executed code*
(fetched AlphaFold models, ran Foldseek, computed distances/composition) and emitted
provenance artifacts. The non-structural runs reached equally strong, correct
verdicts but mostly **reasoned over** the relevant data — domain architecture,
sorting motifs, ChIP/regulon/E-box signatures, InterPro/PANTHER families — rather
than executing topology tools or querying ChIP-Atlas; skn-1 and CLCN7 produced no
provenance artifacts and ASCL1 emitted only an evidence-*summary* figure. So
OpenScientist's code-execution mode appears triggered chiefly by structural
questions; for topology/regulatory questions it behaves as an expert reasoner over
sequence features and curated databases. The verdicts are still high-value — CLCN7
delivered a *second* systematic-mis-annotation catch (after MJ1511/MJ0742).

**The prompt template can shift this — validated by an A/B test.** After tweaking
`templates/gene_hypothesis_deep_research.md` to ask the agent to *execute*
hypothesis-matched analyses (and save provenance), the CLCN7 topology question was
re-run with **only the template changed**. The original run produced zero provenance;
the re-run **computed a Kyte–Doolittle hydropathy profile from the UniProt sequence**,
aligned the 10 TM helices to UniProt topology, and localized the lysosomal sorting
motifs — saved as provenance — while reaching the identical over-annotation verdict
and honestly labelling the computation "supportive provenance rather than novel
evidence" (no fabricated web-only DeepTMHMM result). So for **topology / pure-sequence**
questions the behaviour gap is largely promptable. ChIP/expression questions that
depend on web-only resources (ChIP-Atlas, DeepTMHMM web server) remain limited by
tool access, not prompting.

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

> The three HIGH leads (skn-1, ASCL1, CLCN7) have now been run — see the
> non-structural batch above; all three returned actionable over-annotation
> verdicts. The remaining MED rows (WFS1, SORL1, CTBP1) are still open leads.

## Operational lessons

- **Give jobs ample time, then scope.** Real 3-iteration runs take ~50–90 min;
  structural runs routinely exceed the upstream 3600 s default and get cancelled
  mid-analysis. The `just` recipes now inject `--param timeout=7200` (the API ceiling,
  `le=7200`) and keep the subprocess wall (`--timeout-seconds`, default 8100 s) above
  it. When a job still hits the 7200 s cap — common for human proteins asked a
  multi-faceted question — the fix is **scope, not time**: re-run with one decisive
  analysis and/or `max_iterations=2` (C18orf21: 7200 s timeout → 2708 s when narrowed
  to Foldseek-only).
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
- [x] HIGH non-structural leads (skn-1, ASCL1, CLCN7) run, reviewed, and wired in —
      all three actionable over-annotation verdicts; established that code execution
      is triggered mainly by structural questions.
- [x] Tweaked the prompt template (`templates/gene_hypothesis_deep_research.md`) to
      encourage *executing* hypothesis-matched analyses (hydropathy/topology +
      targeting motifs; active-site/motif residue checks; binding-domain/PWM;
      domain/orthology) and saving the computed result as provenance, with a hard
      "never fabricate / inconclusive is fine / say so if web-only" clause.
- [x] Validated the template tweak with a CLCN7 A/B re-run: same question, only the
      template changed; behaviour shifted from zero provenance to a computed
      Kyte–Doolittle hydropathy + sorting-motif analysis, identical verdict, honest
      labelling. Confirms topology behaviour is promptable; ChIP/expression remain
      tool-access-limited.
- [x] Executable-bioinformatics + Proteostasis-Network batch run and wired in
      (Rv0311 intein REMOVE; NPLOC4 pseudo-DUB; HSPA12A/HSPA12B pseudo-chaperones,
      no GO:0140662; AARSD1 AlaX editing confirmed; RvY_17310 left UNDECIDED after
      verifying the paralog claims; C18orf21 → RMP24/RNase MRP recorded as a
      verification-gated lead). DNAJC28 pending its re-run.
- [ ] Formalize C18orf21 → RNase MRP (GO:0000172) once the 2025–26 primary papers
      are fetched/cached and verified.
- [ ] Run the MED non-structural leads (WFS1, SORL1, CTBP1).
- [ ] Write up the systematic-mis-annotation cases (MJ1511/MJ0742; CLCN7's ~1,198
      propagated annotations; pmp20 family) as examples of family-level error
      propagation caught by compute.
