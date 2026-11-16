# PDE6C notes

Session 2026-11-16, review of 18 GOA rows (vision-disorder alignment campaign), after PDE6A and PDE6B.

## Function

- Catalytic subunit (alpha') of cone PDE6, a homodimer of PDE6C with two PDE6H (Pgamma-c)
  subunits [PMID:39739818 "cone holoPDE6 is a catalytic homodimer of PDE6C"; PMID:28583373].
  Human PDE6C has been expressed and assayed directly: with AIPL1 and Pgamma in HEK293T and insect
  cells [PMID:28583373], and as purified human holoenzyme for cryo-EM [PMID:39739818]. Because the
  enzyme is a homodimer and each subunit carries an active site, the activity is the subunit's own:
  molecular_function GO:0047555, same decision as for PDE6A and PDE6B. GO has no cone PDE6 complex
  term (only GO:7770030 for rod), so no in_complex.
- GAF-A binds noncatalytic cGMP; shown on the human cone enzyme (cryo-EM with and without cGMP)
  [PMID:39739818]. NEW IDA row GO:0030553 cGMP binding (human evidence, unlike PDE6A/B, where it is
  bovine).
- AIPL1 is an obligate chaperone; Pgamma acts as co-chaperone [PMID:27268253; PMID:28583373].
- Location: cone disc membranes, by similarity to mouse Q91ZQ1; prenylated.

## Disease

Recessive achromatopsia and early-onset cone dystrophy [PMID:19615668; PMID:21127010]; missense
alleles either fold badly or lose Pgamma co-chaperoning [PMID:28583373].

## Questionable rows

- Row 13, no-go mRNA decay (IDA, PMID:21127010): the cached abstract reports minigene splicing assays
  of mutant transcripts and no mRNA decay assay; a phosphodiesterase does not take part in no-go
  decay. Removed; full text not cached.
- cAMP rows propagated from the cAMP-directed node, as for PDE6A/B.
