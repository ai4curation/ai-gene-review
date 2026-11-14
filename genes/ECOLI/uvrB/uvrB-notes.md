# uvrB (E. coli K-12, P0A8F8) review notes

Reviewer: Claude (AI-assisted). Session date: 2026-11-10.

## Deep research

No provider deep-research file exists for this gene and none could be generated (no provider
API keys in this environment). These notes are built from the cached UniProt record and from
primary literature cached in `publications/` (fetched with `just fetch-pmid`). Literature search:
PubMed queries "UvrB ATPase cryptic", "role of ATP binding and hydrolysis by UvrB", "UvrB
beta-hairpin damaged DNA binding", "UvrB ATP hydrolysis preincision", "uvrB LexA SOS
Escherichia coli regulation". Papers read (abstracts; full text noted where cached):
PMID:2974538, PMID:10713125, PMID:10601012, PMID:11689453, PMID:16532007, PMID:8035457,
PMID:12145219, PMID:2546148, PMID:10671556, PMID:10631326, PMID:29967594 (full text),
PMID:24561554 (full text), PMID:19516334 (full text), PMID:19458048, PMID:27718375.

## Function

- UvrB is the damage-verification subunit of UvrABC. UvrA2B2 scans DNA; DNA wraps around one
  UvrB, the beta-hairpin inserts between the strands and UvrB probes one strand; on finding a
  lesion UvrA leaves and the UvrB-DNA preincision complex recruits UvrC
  [PMID:12145219 "the damage recognition complex consists of two UvrA and two UvrB subunits, with the DNA wrapped around one of the UvrB monomers"].
- ATPase: purified UvrB alone has no detectable NTPase, but the UvrB* proteolytic fragment has
  ssDNA-dependent ATPase, and the UvrAB-associated ATPase is the activated UvrB ATPase, essential
  for incision [PMID:2974538 "the stimulation in DNA dependent ATPase activity following formation of the UvrAB complex results from the activation of the normally sequestered UvrB associated ATPase"].
- ATP hydrolysis by UvrB is needed to form an incision-competent UvrBC-DNA complex; ATP binding
  (not hydrolysis) is needed for 3' incision
  [PMID:10713125 "To initiate the formation of an active UvrBC-DNA incision complex, however, UvrB first needs to hydrolyze ATP, and subsequently a new ATP molecule must be bound."].
- Helicase motifs V and VI are needed for damaged-DNA-induced ATP hydrolysis and strand
  displacement by UvrA2B [PMID:8035457].
- Structure: two helicase-like domains plus repair-specific domains; ATP-bound structure
  [PMID:10601012 "The structure contains all elements of an intact helicase, and is evidence that UvrB utilizes ATP hydrolysis to move along the DNA to probe for damage."].
- Damaged DNA binding / recognition: beta-hairpin residues Y95/Y96 contact the lesion; Y92/Y93
  prevent binding to undamaged DNA [PMID:11689453]; UvrB-DNA structure shows the flipped
  nucleotide in a conserved pocket [PMID:16532007].
- Incision chemistry is in UvrC, not UvrB [PMID:10671556 "Here we show that the catalytic site for incision on the 3' side is in this protein as well"] (the 5' site was already known to be in UvrC).
- Regulation: uvrB belongs to the LexA/SOS regulon in E. coli [PMID:29967594 "The uvrB gene belongs to the SOS network, encoding a key component of the nucleotide excision repair."].

## Annotation notes

- Seven bare GO:0005515 rows (UvrA, SeqA, Ugd partners): removed per protein-binding policy.
  PMID:19458048 (PBP1b crystal structure) and PMID:19516334 (alkyltransferase-like proteins)
  do not mention UvrB in the cached text; the UvrA-UvrB IPI from them is probably a control
  or figure interaction we cannot see. Not recorded as a source defect (full text not
  inspected for 19458048).
- GO:0009381 excinuclease ABC activity with `enables` overstates UvrB: the hydrolysis of DNA
  ester bonds is catalysed by UvrC; UvrB contributes. Marked over-annotated.
- Core MF: GO:0016887 ATP hydrolysis activity (module function) and GO:0003684 damaged DNA binding.
