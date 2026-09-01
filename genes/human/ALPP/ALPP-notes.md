# ALPP (human) — review notes

UniProt: P05187 (PPB1_HUMAN) · placental alkaline phosphatase (PLAP), Regan isozyme ·
EC 3.1.3.1 · 535 aa precursor, chromosome 2q37 cluster with ALPI and ALPG.

Reviewed alongside the other three human alkaline phosphatases; shared reasoning is in
`genes/human/ALPL/ALPL-notes.md`.

## Structure paper that GOA does not cite

Le Du et al. 2001 (PMID:11124260) solved PLAP at 1.8 Å. It is the source UniProt cites for
ALPP's catalytic metals and homodimer, yet it appears nowhere in ALPP's GOA. Consequences
for this review:

- The zinc and magnesium rows carry ISS codes transferred from mouse Akp3 (P15693), even
  though the human enzyme's own structure resolves the metals. I ACCEPTed the terms and
  noted in each `reason` that a curator could upgrade the evidence to IDA. I did not
  change the codes — the review action set has no "upgrade evidence" action, and the term
  is what is under review.
- Three NEW annotations rest on it: `GO:0005509 calcium ion binding` (ISS — the metal's
  identity was established in ALPL, not here), `GO:0042803 protein homodimerization
  activity` (IDA), and it backs `GO:0009897 external side of plasma membrane`.

The dimer is worth asserting despite the general rule against binding terms
[PMID:11124260, "Allostery is probably favored by the quality of the dimer interface, by a
long N-terminal alpha-helix from one monomer that embraces the other one, and similarly by
the exchange of a residue from one monomer in the active site of the other."].

The paper also explains the isozyme's diagnostic chemistry [same, "In the neighborhood of
the catalytic serine, the orientation of Glu-429, a residue unique to PLAP, and the
presence of a hydrophobic pocket close to the phosphate product, account for the specific
uncompetitive inhibition of PLAP by l-amino acids"].

## Citation problems found

Two rows where the reference does not obviously support the annotation. Neither was
removed — the CLAUDE.md rule against overruling experimental annotations from abstract-only
caches applies — but both are flagged in `reference_review`, which is what that field is
for.

1. **`GO:0004035` IDA from PMID:2133555** → ACCEPT + `correctness: MISCITED`. The paper is
   "Two alkaline phosphatase genes are expressed during early development in the mouse
   embryo": mouse, preimplantation embryos, RT-PCR of *transcripts*. The abstract states
   both the organism and the method explicitly, so this is the case the guidance allows a
   caveat for. A transcript survey in mouse cannot be direct evidence of human PLAP
   catalytic activity. The term itself is beyond doubt on other evidence, so I accepted
   the annotation and flagged only the citation.
2. **`GO:0009986 cell surface` IDA from PMID:15907827** → KEEP_AS_NON_CORE +
   `correctness: UNVERIFIED`. The cached abstract is entirely about GPI-PLD, CD55 and CD59
   in chronic myeloid leukaemia and does not mention alkaline phosphatase at all
   (`grep -ic "alkaline phosphatase\|PLAP"` returns 0 over the whole cached record). But
   PLAP is a conventional GPI-PLD assay substrate, the full text is not cached, and the
   curator saw it. Marked UNVERIFIED, deliberately not WRONG_IDENTIFIER: I could not
   confirm the citation, which is not the same as showing it wrong.

## Protein binding rows

Both `GO:0005515` rows → MARK_AS_OVER_ANNOTATED. PMID:25416956 (Rolland/Vidal HI-II-14)
gives KRTAP5-9 and KRTAP4-12; PMID:32296183 (HuRI) gives roughly thirty partners of which
ten-plus are KRTAPs (Q5T5A8, Q5T5B0, Q5T752, Q5T753, Q5T754, Q5T871, Q5TA76, Q5TA77,
Q5TA81, Q5TCM9, P26371). A thirty-protein list dominated by one sticky family is the
signature of assay-driven recovery. Contrast with the homodimerization term added as NEW,
which is what a real, functionally load-bearing protein interaction looks like for this
gene.

## What is genuinely unknown

PLAP has no established physiological substrate. This is the most important thing about
the gene's annotation and is recorded as a `knowledge_gaps` entry on the core function
rather than being papered over. The deep research is explicit that ALPL's PPi and
mineralization functions must not be transferred here
[file:human/ALPP/ALPP-deep-research-falcon.md, "**Not justified:** describing ALPP as the
principal human skeletal PPi phosphatase."], and that what is solid is the localisation
[same, "The clearest native biological evidence instead places ALPP on the
syncytiotrophoblast surface, with exceptionally strong induction toward term"].

Consequently the ALPP core function has a `molecular_function` and `locations` but no
`directly_involved_in` — there is no process that can honestly be asserted. That asymmetry
against ALPL (three core functions, several BP terms) is the correct representation of the
evidence, not an omission.
