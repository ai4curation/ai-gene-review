# fezf2 (Danio rerio, Q804Q5) — curation notes

## 2026-09-27 — initial review (claude-code, Fable 5.1)

**Deep research not available.** `just deep-research-falcon DANRE fezf2 --fallback perplexity-lite`
failed: no EDISON_API_KEY / ASTA_API_KEY / PERPLEXITY_API_KEY in the environment. Literature
synthesis below was done by hand from the nine GOA-cited papers in `publications/` plus the
UniProt record. Only two of the nine have full text cached (PMID:18799544, PMID:21471212);
the rest are abstract-only, and the review says so wherever it matters.

### Gene gestalt

- Forebrain-specific C2H2 zinc-finger TF; six C-terminal zinc fingers (aa 249–412), N-terminal
  eh1-related repressor motif (aa 27–42, UniProt MOTIF). Also known as fezl, too few (tof).
- Molecular function is directly shown once, in PMID:21471212: genomic SELEX with the ZF domain
  → core motif CAGCAACC; anisotropy binding; luciferase transactivation in HEK293 (1.5–4×);
  in vivo forebrain enhancer activity abolished by motif mutation or fezf2 MO; ChIP of endogenous
  Fezf2 at eomesa/tbr2 and lhx2b; lhx2b down in tof/MO, up on hs:gal4;uas:fezf2. Authors call
  Fezf2 a *transcription activator*. PMID:12469125 (abstract) calls it a *repressor* with the eh1
  motif required for function. Both are probably true; flagged in `suggested_questions`.
- Developmental roles (all IMP, tof m808 hypomorph and/or MOs): diencephalon subdivision
  (prethalamus vs ZLI, via wnt repression; PMID:17164418), hypothalamus / otp regulation
  (PMID:18003738, PMID:23533176), DA/5HT neuron number downstream of Wnt and
  non-cell-autonomous (PMID:12469125, PMID:15219677, PMID:18799544).
- Adult: fezf2-high quiescent vs fezf2-low proliferative dorsal telencephalic NSCs; patterns a
  Notch gradient; required for quiescence (PMID:25319688).

### Decisions worth a second look

| Term | Action | Why |
|---|---|---|
| GO:0007399 nervous system development (PMID:15219677) | MODIFY → GO:0021879 / GO:0071542 | Root-level term; paper is about forebrain DA/5HT subgroups |
| GO:0021954 CNS neuron development (PMID:10191060) | MODIFY → GO:0071542 / GO:0021879 | 1999 screen paper: specific hypothalamic DA reduction |
| GO:0071679 commissural neuron axon guidance ×2 (PMID:21471212) | KEEP_AS_NON_CORE | Transient phenotype, attributed by authors to reduced lhx2b; supported as an upstream `acts_upstream_of_or_within` assertion but downstream of Fezf2's core transcription-factor activity |
| GO:0045944 positive regulation of transcription by RNAPII | NEW (IDA, PMID:21471212) | Activator function demonstrated; no existing positive-regulation row |
| GO:0045892 negative regulation of DNA-templated transcription | ACCEPT | Abstract identifies tof/fezl as a transcription repressor; could narrow to GO:0000122 with full text |

Everything else ACCEPTed, including all IBAs (PTN001803442 node; target-specific experimental
grounding exists in PMID:21471212).

### Not done / follow-ups

- No `propagation_review` blocks added: all IBA rows were accepted, so there is no failure to
  trace.
- ZFIN gene id in the nucleus IBA WITH/FROM is ZDB-GENE-020424-1, whereas UniProt cross-refs
  fezf2 to ZDB-GENE-001103-3. Not investigated; may be a paralog (fezf1?) as donor.
- Human FEZF2 / mouse Fezf2 have no review in this repo yet; a cross-species pass would help
  settle the activator/repressor question.

## 2026-10-09 - commissural axon guidance follow-up

Revisited the two `GO:0071679` rows from PMID:21471212. The initial
`MARK_AS_OVER_ANNOTATED` action was too strong: the paper explicitly observes an anterior
and post-optic commissure crossing defect in both tof mutants and fezf2 morphants, and the
`acts_upstream_of_or_within` qualifier covers Fezf2's transcriptional activation of `lhx2b`
as the upstream mechanism. Changed both rows to `KEEP_AS_NON_CORE` because the defect is
transient, downstream of the core transcription-factor activity, and attributed at least
partly to the direct Fezf2 target `lhx2b`.
