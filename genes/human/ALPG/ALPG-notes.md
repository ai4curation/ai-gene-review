# ALPG (human) — review notes

UniProt: P10696 (PPBN_HUMAN) · germ cell alkaline phosphatase (GCAP), Nagao isozyme,
placental-like ALP · gene long known as **ALPPL2** · EC 3.1.3.1 · 532 aa precursor,
chromosome 2q37 cluster with ALPI and ALPP.

Reviewed alongside the other three human alkaline phosphatases; shared reasoning is in
`genes/human/ALPL/ALPL-notes.md`.

## The sparsest record of the four

Only 9 GOA rows, and almost all of them are the same two facts stated repeatedly:
alkaline phosphatase activity (four times) and plasma membrane (four times), plus the
generic InterPro2GO `phosphatase activity`. **No metal binding at all** — no zinc, no
magnesium, no calcium — even though ALPI and ALPP both carry zinc and magnesium terms and
ALPG is 98% identical to ALPP. That asymmetry looks like an oversight rather than a
considered judgement, so five NEW annotations are proposed here, more than for any other
gene in this set.

## Why the ISS transfers are unusually safe here

GCAP and PLAP differ at only seven residues [PMID:1939159, "Yet, they differ by only 7
amino acids at positions 15, 67, 68, 84, 241, 254, and 429 within their respective 484
residues."]. None of those seven is a metal ligand. UniProt's ALPG metal sites are all
`ECO:0000250|UniProtKB:P05187`, i.e. transferred from PLAP, whose sites are resolved in a
1.8 Å structure (PMID:11124260). If a sequence-similarity metal transfer is defensible
anywhere, it is here. ISS is still the honest code — the metals were seen in ALPP, not in
ALPG — and that is what I used for zinc, magnesium, calcium and homodimerization.

Calcium is transferred one step further out, from ALPL (PMID:11395499, the synchrotron XRF
study that identified the mammalian-specific metal). Noted in the review that this site is
structural and does not influence phosphatase activity, per the UniProt DOMAIN comment on
ALPL.

## The one paper GOA undersells

PMID:2162249 (Lowe & Strauss 1990) is cited as **NAS**, but it is the gene-defining study
and it contains direct experimental data:

- It resolved the identity of the tumour "placenta-like" enzyme [PMID:2162249, "The
  complementary DNA is the product of the germ cell AP (Nagao isozyme) gene and not of the
  term PLAP gene."] and [same, "These data demonstrate that BeWo AP is the product of a
  gene normally expressed in testis, thymus, and germ cells, but not in placenta."].
- It directly demonstrated GPI anchoring of the human enzyme [same, "Immunoprecipitation
  of phosphaditylinositol-specific phospholipase C-treated AP and analysis by
  polyacrylamide gel electrophoresis or isoelectric focusing demonstrates that at least
  95% of the AP contains PI-glycan."].

That second result is direct evidence for `GO:0009897 external side of plasma membrane`,
proposed here as IDA. Note the paper's own spelling, "phosphaditylinositol" — quotes must
be verbatim, typo included.

(The supporting-text validator lowercases, strips punctuation and collapses whitespace, so
line-wrapped quotes match; `grep -F` against the cached file will *not* find them. Verify
with a normalising Python one-liner instead, not grep.)

## Gly429 is the whole story of this gene's identity

[PMID:1939159, "We report that the differential reactivity of PLAP and GCAP depends
critically on a single amino acid at position 429. GCAP with Gly-429 is strongly inhibited
by L-leucine, EDTA, and heat, whereas PLAP with Glu-429 is resistant."] The classical
Nagao/Regan distinction — L-leucine, EDTA and heat sensitivity — reduces to one residue.
UniProt's ACTIVITY REGULATION line for ALPG cites this paper for exactly that. Worth
recording that the EDTA sensitivity is itself indirect evidence for a multi-metal
metalloenzyme, which is consistent with the metal terms proposed above.

## Functionally dark below the level of chemistry

No physiological substrate, no pathway, no loss-of-function phenotype. The deep research
searched and came back empty [file:human/ALPG/ALPG-deep-research-falcon.md, "No compelling
ALPG-specific endogenous substrate or dedicated signaling pathway was identified in the
retrieved literature."]. Recorded as a `knowledge_gaps` entry (BIOLOGY / BP_DARK) on the
core function rather than filled with a plausible guess. Like ALPP, the ALPG core function
therefore has a molecular function and a location but no `directly_involved_in`.

## Methodological hazard to flag for anyone reusing this literature

GCAP and PLAP are ~98% identical and most antibodies and activity assays cannot separate
them. Much of the "placental alkaline phosphatase" serum-marker and immunohistochemistry
literature may be measuring either gene or both. This is why the `GO:0005576 extracellular
region` row is KEEP_AS_NON_CORE here rather than ACCEPT as it is for ALPI: the released
serum pool is exactly the compartment where the isozyme confusion is worst.
