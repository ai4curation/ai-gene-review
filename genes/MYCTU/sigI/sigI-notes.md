# sigI (Rv1189, P9WGH3) — Mycobacterium tuberculosis H37Rv

## 2026-10-21 — Full review, independent of any ProtNLM2 predictions

Deep research: `just deep-research-falcon MYCTU sigI --fallback perplexity-lite`
failed — the falcon/Edison endpoint returned `403 Forbidden` ("Failed to
authenticate") and the perplexity fallback also failed, so no
`sigI-deep-research-*.md` file exists. This review was therefore built from
primary literature retrieved directly from PubMed/PMC and cached under
`publications/`.

### What the protein is

- UniProt P9WGH3, 290 aa, "Probable ECF RNA polymerase sigma factor SigI",
  locus Rv1189. Sigma-70 region 2 (res. ~11–74) and region 4_2 (~110–162) with
  an H-T-H DNA-binding motif at 137–156, followed by an NTF2-like/SnoaL-type
  C-terminal extension (`DR   InterPro; IPR032710; NTF2-like_dom_sf.`;
  `DR   NCBIfam; TIGR02937; sigma70-ECF; 1.`).
- PANTHER placement: `PTHR30173:SF43` (ECF RNA POLYMERASE SIGMA FACTOR
  SIGI-RELATED), per `interpro/panther/PTHR30173/PTHR30173-entries.csv`. The
  other M. tuberculosis ECF41 sigma factor, SigJ (L0TCG5), is in a *different*
  subfamily, `PTHR30173:SF36`.
- Group assignment: SigI is an **ECF41** sigma factor
  [PMID:28934483 "tuberculosis has two ECF41 σ factors σI and σJ (11)."],
  [PMID:32180013 "Mtb-SigI belongs to the ECF41 family of sigma factor"].
  ECF41 members have no cognate anti-sigma factor; the fused C-terminal
  extension appears to take over that regulatory role
  [PMID:22950025 "Based on our data, ECF41-dependent signal transduction does
  not seem to involve a second protein that functions as an anti-σ factor."],
  [PMID:30990934 "In a number of highly abundant ECF groups, including ECF41
  and ECF42, σ-factors contain fused C-terminal protein domains, which provide
  the necessary regulatory function instead."].

### Experimentally established in M. tuberculosis (this species)

The decisive paper is Lee et al. 2012 (PMID:22434196), which is the basis for
every function claim in the review that is not purely domain-based:

- **Sigma factor activity / promoter-specific transcription initiation (direct,
  in vitro).** Recombinant SigI reconstituted with E. coli core RNA polymerase
  initiated transcription from the katG promoter but not from a non-target
  template: "Although the SigI-containing RNA polymerase holoenzyme was unable
  to direct transcription from the non-SigI-regulated gene Rv1186,
  SigI-directed transcription was detected from the katG promoter, providing
  direct evidence that SigI can direct transcription from the katG promoter
  located 379 bp upstream of the gene".
- **Sequence-specific promoter recognition.** Deleting the candidate SigI motif
  from the katG promoter abolished activity: "Removal of this short sequence
  nearly abolished the ability of SigI to direct transcription of katG (Fig.
  3e), thus confirming SigI-mediated transcription of katG."
- **In vivo transcriptional effect.** "lysates from the ΔsigI mutant were
  associated with significantly decreased katG transcription, further
  demonstrating a direct SigI transcriptional effect in expression of katG."
- **Regulon (microarray screen).** "The SigI regulon identified included an ATP
  synthase (Rv1304), heat shock proteins (Rv0440, Rv0350, and Rv3417), and
  katG."
- **Expression.** "sigI transcript levels were increased during stationary
  phase (Fig. 1a) as well as during heat shock (Fig. 1b). However, little
  variation in sigI expression was observed in response to other stress
  conditions."
- **Phenotypes.** ΔsigI is isoniazid-resistant (via reduced katG, the
  INH-activating catalase-peroxidase) and is *not* attenuated — it is
  hypervirulent in BALB/c mice. These are downstream organismal phenotypes of
  losing a transcription factor and are not annotated as process participation.

Upstream regulation: sigI is transcribed from a sigma-J-dependent promoter
[PMID:18248429 abstract: "The only positive clone revealed a promoter directing
expression of the sigI gene encoding ECF sigma factor sigma(I)."], confirmed
biochemically in [PMID:28934483 "σJ recognizes the promoter of another ECF41 σ
factor, σI, thereby controlling the expression of this σ factor (19)."]. This
is regulation *of* sigI, not a function *of* SigI, so it is background, not an
annotation.

Recent CRISPRi/overexpression work adds that SigI level modulates rifampicin
susceptibility and that knocking it down impairs growth
[PMID:41392072 "We noted that CRISPRi-mediated repression of SigI resulted in a
growth-defective phenotype (in the absence of rifampicin exposure)"], with the
mechanism explicitly unresolved by the authors. Not annotated.

### The cold-shock annotation

GOA carries `GO:0009409 response to cold` with IEP from PMID:10027986
(Manganelli et al. 1999), curated by MTBBASE. The cached record is
abstract-only; the abstract states "we also identified a sigma factor gene
whose mRNA increased after mild cold shock" without naming which. Secondary
reviews attribute the mild cold-shock induction to sigD and sigI. Lee 2012 saw
"little variation in sigI expression ... in response to other stress
conditions" beyond stationary phase and heat shock. Per the repo rule against
overruling a curator from an abstract-only cache, the row is kept, but as
non-core: a transcript-level induction is a response, not evidence that SigI
performs work in cold adaptation, and the magnitude was described as modest.

### Evolutionary grounding of the propagated rows

The only IBA is `GO:0016987 sigma factor activity` from PAINT node
`PTN001249270` in PTHR30173, seeded by `UniProtKB:L0TCG5` (M. tuberculosis
SigJ, subfamily SF36) — see
`interpro/panther/PTHR30173/PTHR30173-paint.tsv`. The node therefore sits above
both SF36 and SigI's SF43, and the asserted function (sigma factor activity) is
exactly the family-wide property that PTHR30173's family review grants
(`interpro/panther/PTHR30173/PTHR30173-review.yaml`, scope FAMILY_WIDE for
GO:0006352). Nothing subfamily-specific (SigJ's regulon, its H2O2 phenotype) is
transferred, and nothing needs to be: SigI has its own direct in vitro
transcription evidence. Note also that M. bovis BCG Pasteur has deleted the
sigI locus and M. avium/M. paratuberculosis lack a clear ortholog
[PMID:14761983 "However, M. bovis BCG Pasteur lacks sigI as this locus is
deleted, while in its genome, the sigH and sigM loci are duplicated ( 11 )."],
so the gene is not universally retained even within mycobacteria.

### Decisions

| Term | Evidence | Action | Why |
|---|---|---|---|
| GO:0003677 DNA binding | IEA | ACCEPT | H-T-H motif; motif-deletion abolishes SigI-driven transcription |
| GO:0003700 DNA-binding TF activity | IEA | MODIFY → GO:0016987 | strict ancestor of sigma factor activity (OLS-verified), which the gene carries |
| GO:0006352 transcription initiation | IEA | ACCEPT | direct in vitro transcription |
| GO:0006355 regulation of transcription | IEA | MODIFY → GO:2000142 | strict ancestor of the initiation-regulation term the gene carries |
| GO:0009409 response to cold | IEP | KEEP_AS_NON_CORE | curator IEP retained; peripheral, abstract-only cache |
| GO:0016987 sigma factor activity | IBA, IEA | ACCEPT (both) | family-wide node + direct species evidence |
| GO:2000142 reg. of transcription initiation | IEA | ACCEPT | follows from sigma activity and from the katG data |

No `NEW` terms proposed. A signed term (positive regulation of transcription
initiation) would be a descendant of GO:2000142, which the gene already
carries, and CLAUDE.md rejects proposing an ancestor/descendant of an existing
term. The INH-resistance and hypervirulence phenotypes of ΔsigI are
loss-of-regulator consequences, not processes SigI performs.
