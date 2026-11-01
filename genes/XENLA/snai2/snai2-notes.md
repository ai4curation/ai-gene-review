# snai2 (Slug; Q91924) — Xenopus laevis — review notes

Project: NEURAL_CREST_ORIGINS (Tier 1, neural crest specifier). Reviewed 2026-10-01.

## Identity

- Q91924 is snai2.L (Xenbase XB-GENE-6255814, chr 6L); 266 aa, N-terminal SNAG repression
  domain (1-20) and five C2H2 zinc fingers (126-262). The S homeolog snai2.S is TrEMBL
  Q90VW5 (also 266 aa) and carries no experimental GO annotations. Most frog loss-of-function
  reagents (antisense RNA, morpholinos, dominant-negative zinc-finger constructs) would not
  distinguish L from S.
- Distinct from snai1 (P19382, Tier 3). Lamprey has a single snail gene "which has affinities
  to both snai1 and snai2" [PMID:39060477].
- UniProt: "Probable transcriptional repressor. Acts downstream of snai1 in the specification
  of the neural crest and neural crest migration." [file:XENLA/snai2/snai2-uniprot.txt]

## Expression (where/when)

- Xslu is expressed in the prospective crest after the convergence-extension movements, later
  than Xsna, and then in pre- and post-migratory cranial and trunk crest [PMID:7720581 "A related
  zinc-finger gene called Slug (Xslu) is expressed specifically in this tissue (i.e. the
  prospective crest) when the convergence extension movements are completed."].
- Induced by noggin + bFGF in animal caps [PMID:7720581 "treated with bFGF and noggin express
  Xslu but not NCAM"]; promoter has a LEF/beta-catenin element (Vallin 2001, PMID:11402039,
  not cached; via UniProt INDUCTION).
- York 2024: in Xenopus snai2 behaves like a definitive crest factor (monotonic increase from
  blastula to late neurula), unlike lamprey [PMID:39060477 "Interestingly, in Xenopus but not
  lamprey twist1, ets1, and snai2 also displayed these dynamics"]. Contrast with snai1, which is
  co-expressed with pluripotency factors in blastula animal cells [PMID:25931449 "We found that
  Id3, TF-AP2, Ets1, FoxD3 and Snail1 were co-expressed with the core pluripotency factors"].

## Molecular activity

- Transcriptional repressor: an Engrailed-repressor fusion mimics XSlug, a Gal4-activator fusion
  inhibits it [PMID:10772801 "The Engrailed repressor fusion was found to mimic the effects of
  wild-type XSlug, indicating that XSlug functions as a transcriptional repressor during neural
  crest formation."].
- Direct target: E-cadherin. Flag-Snail2 ChIP at late neurula [PMID:25617436 "Snail2 bound
  preferentially to the E-boxes located around the TSS"]; Snail2 recruits PRC2 [PMID:25617436
  "The data thus demonstrate that Snail2 helps to recruit PRC2 to the E-cad promoter to set up
  repressive histone modification marks that result in inhibition of E-cad expression during
  neural crest EMT."]. EZH2 binds Snail2 directly [PMID:25617436 "EZH2 interacts directly with
  Snail2"].
- Corepressors: Ajuba LIM proteins (Ajuba, LIMD1, WTIP) bind the SNAG domain [PMID:18331720
  "Ajuba LIM proteins contribute to neural crest development as Snail/Slug corepressors and are
  required for in vivo Snail/Slug function"] (abstract-only in cache; UniProt records frog
  Snai2 SNAG-LIM interactions).
- Elp3 co-IP (the GOA protein binding IPI): mElp3 pulled down xSlug, and xSlug rescues Elp3
  morphants [PMID:27189455 "Indeed, mElp3 pulled down efficiently xSlug in a co-IP experiment"].
  The paper's model is Elp3 stabilising Snail1 protein; for Snai2 this is an upstream regulator
  of Snai2 protein, not a Snai2 activity. Generic protein binding -> REMOVE.

## Gain of function

- XSlug overexpression expands crest markers and melanocytes [PMID:10772801 "overexpression of
  XSlug leads to expanded expression of neural crest markers and an excess of at least one neural
  crest derivative, melanocytes"].
- But Slug alone is not sufficient to induce crest in naive ectoderm; it needs Wnt/FGF
  [PMID:9609823 "Overexpression of the zinc finger transcription factor Slug, one of the earliest
  markers of neural crest formation, is insufficient for neural crest induction."]; Snail2 + Wnt
  is sufficient [PMID:25931449 "Snail2 together with Wnt signaling is sufficient to establish a
  neural crest state"]. Snail (snai1), by contrast, induces Slug and other markers; Slug cannot
  [PMID:12490555 "Slug alone is unable to induce other neural crest markers in animal cap
  assays"].
- Snail2 expands border and crest markers but this needs EZH2 [PMID:25617436 "Snail2 expanded
  several neural plate border and neural crest markers"].

## Loss of function

- Stage-dependent: early inhibition prevents crest precursor formation, later inhibition blocks
  migration [PMID:10772801 "inhibition of XSlug function at early stages prevents the formation of
  neural crest precursors, while inhibition at later stages interferes with neural crest
  migration"].
- Antisense slug: migration and derivatives (cartilage) lost; rescued by Slug or Snail
  [PMID:10452849 "These studies indicate that XSlug is required for neural crest migration, that
  XSlug and XSnail may be functionally redundant"].
- Slug MO abolishes Sox9 and raises apoptosis; mesoderm markers reduced [PMID:17205110 "Injection
  of the Slug MO into one cell of a two cell embryo blocks the expression of Sox9 on the injected
  side"]. The NF-kB/apoptosis loop is a separate (mesoderm/survival) role; not core.
- Network layer: Snail2 knockdown does not reduce border genes [PMID:25617436 "By contrast,
  knockdown of Snail2 did not appreciably diminish either Zic1 or Pax3 levels"]. So snai2 is
  downstream of the border specifiers, and downstream of snai1 [PMID:12490555 "Snail lies upstream
  of Slug in the genetic cascade leading to neural crest formation"].

## Layer placement

NC specifier (and later EMT/delamination effector), not a border specifier and not a blastula
competence factor. Evidence: onset after snai1 and inside the crest domain; border genes
unaffected by its loss; insufficient alone, sufficient with Wnt; repressor activity; direct
repression of E-cadherin via PRC2 during NC EMT; required early for precursors and later for
migration.

Process terms: GO:0014036 NC cell fate specification (core), GO:0001755 NC cell migration (core).
GO:0036032 NC cell delamination was considered (Snai2 recruits PRC2 to the E-cad promoter) but
WITHHELD: E-cad RNA rises only ~1.5-fold in Snai2 morphant crest, migrating Xenopus cranial crest
retain E-cadherin and need it (Huang 2016, cited in the updated deep research
[file:XENLA/snai2/snai2-deep-research-falcon.md "E-cadherin depletion impaired their migration and
protrusions, and other tested classical cadherins did not replace it."]), and no Snai2-specific
delamination assay exists in frog. Raised as a suggested question. GO:0014029 TAS row (Id2 cardiac crest ablation paper, which
does not appear to study Slug) -> MODIFY to GO:0014036 per the project convention (sox10, sox9-a).

## Evolution

- Amphioxus Snail is the one NC specifier transiently expressed at the border [PMID:18562679 "The
  single exception was amphioxus Snail , which is transiently expressed at the neural plate border
  in the early neurula stage."]. So Snail border expression predates vertebrates; the
  Snai1/Snai2 split and snai2's specifier-specific behaviour are vertebrate (gnathostome-level,
  given a single lamprey snail).
- Lamprey snail is in the conserved NC-GRN [PMID:17765683].

## Open issues

- snai2.S (Q90VW5) carries none of the experimental annotations.
- Snai1/Snai2 redundancy: which roles are snai2-specific?
- Apoptosis/NF-kB and mesoderm roles (PMID:17205110) not annotated; possible non-core.
- No GO neural plate border term; snai2 is NOT a border gene, so it is unaffected by that decision.

## Update after deep-research rewrite (2026-10-01)

The falcon report was regenerated mid-review. New points: two X. laevis Slug pseudoalleles
(L/S) with identical zinc fingers (Vallin 2001); LEF/beta-catenin site in the snai2 promoter
(upstream input, not a Snai2 activity); Ppa F-box degradation of Slug; Bcl-xL rescue indicates a
survival component in Slug MO phenotypes [file:XENLA/snai2/snai2-deep-research-falcon.md "it
should not be annotated as secreted or as a cell-surface receptor."]. Quotes re-checked against
the new file.
