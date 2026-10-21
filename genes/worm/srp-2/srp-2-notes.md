# srp-2 (C05E4.1, O17365) review notes

## Deep research status

- 2026-10-20: `just deep-research-falcon worm srp-2 --fallback perplexity-lite` failed.
  Falcon returned `403 Forbidden` at the Edison auth endpoint; the perplexity-lite
  fallback returned `401 insufficient_quota`. No deep-research file was produced. The
  review is based on the cached primary papers listed below plus the UniProt record and
  the PANTHER PTHR11461 PAINT table.

## Identity and family placement

- 359-aa serpin of clade L (nematode intracellular serpins), one of nine tandemly arrayed
  serpin genes on chromosome V [PMID:14739286 "A screen of the C. elegans genomic and
  cDNA databases revealed nine serpin genes, tandemly arrayed on chromosome V."].
- UniProt: PANTHER PTHR11461 (serpin), subfamily PTHR11461:SF352; CDD cd19581
  serpinL_nematode; MEROPS I04.041. UniProt entry is unreviewed (TrEMBL), PE 1.
- PAINT (PTHR11461-paint.tsv): an IBD for GO:0004867 serine-type endopeptidase
  inhibitor activity sits at the Rhabditida clade-L node PTN002479231, seeded only by
  WB:WBGene00005643 (srp-2 itself). The deep root node PTN000156123 carries GO:0005576
  extracellular region (IBD, seeded by vertebrate, fly and plant extracellular serpins),
  and an IRD NOT GO:0005576 is placed at PTN002606963 (taxon 117571), i.e. on a
  vertebrate intracellular branch, not on the nematode branch. The GOA row for srp-2 is
  the mechanical descent from the root IBD.
- No GO:0004869 (cysteine-type endopeptidase inhibitor activity) IBD exists in PAINT for
  the clade-L node, even though srp-2 has an IDA for it. The PAINT curator propagated
  the serine-protease inhibitor term from srp-2 but not the cysteine-protease inhibitor
  term; treat that as a deliberate decision when considering transfer to paralogs.

## Molecular function (experimental, this species' protein, in vitro)

- Recombinant SRP-2 inhibits mammalian granzyme B (serine peptidase) and cathepsins K,
  L, S and V (papain-like cysteine peptidases) [PMID:14739286 "Biochemical analysis of
  recombinant SRP-2 protein revealed SRP-2 to be a dual cross-class inhibitor of the
  apoptosis-related serine proteinase, granzyme B, and the lysosomal cysteine
  proteinases, cathepsins K, L, S, and V."]. Full text of PMID:14739286 is not cached
  (abstract only); kinetic constants and complex-formation data could not be checked.
- The targets are mammalian enzymes; no endogenous C. elegans target peptidase has been
  identified. The RCL analysis in PMID:25786854 notes a hydrophobic P2 residue that
  favours papain-like cysteine peptidases [PMID:25786854 "SRP-2 , unlike NS/SERPINI1,
  harbors a hydrophobic residue at the P2 position, which signals a preference for
  lysosomal cysteine proteinases."].

## Localization (experimental, in vivo)

- No signal peptide; GFP-tagged SRP-2 is cytosolic and does not colocalise with an ER
  marker [PMID:25786854 "As expected, SRP-2::GFP ( i.e. , the wild-type protein) also
  showed a diffuse cytoplasmic distribution, which did not colocalize with sDsRed::KDEL"].
- Not secreted by any route: SRP-2::GFP under its own promoter was not found in the
  cuticle or perivitelline space [PMID:25786854 "Taken together these imaging studies
  suggested that SRP-2 was not secreted and behaved as an obligate intracellular
  serpin."].
- Hence the GO:0005576 extracellular region rows (IBA from the deep root and IEA from
  InterPro IPR000215) are contradicted by direct experiment on this protein. Proposed
  NEW: cytosol (GO:0005829), IDA, PMID:25786854.

## Expression

- Present in early embryos; strongly expressed in intestine and hypodermis of larvae and
  adults [PMID:14739286]; also hypodermal and seam cells [PMID:25786854].

## Phenotypes not annotated as process

- Overexpression causes slow growth and L1-L3 arrest [PMID:14739286]. This is a
  gain-of-function perturbation of serpin-protease balance; it does not establish that
  SRP-2 participates in postembryonic development, so no BP term is proposed.
- The H302R aggregation-prone mutant has been used as a cytosolic proteostasis reporter
  (PMID:25786854 and studies cited therein). That is a use of the protein as a tool,
  not a function.

## Paralogs

- SRP-3 (G5ECY2), a muscle-specific clade-L serpin, inhibits chymotrypsin-like serine
  peptidases [PMID:16584183]. SRP-6 is the clade-L serpin with in vivo evidence for
  blocking lysosome-mediated necrosis (not cited here; not srp-2 evidence).
- Relevance to C28G1.2 (Q18287): both sit in the Caenorhabditis node PTN002479232. Only
  inhibitory activity that depends on an intact reactive-centre loop is established for
  SRP-2; anything transferred must be conditioned on the recipient retaining the RCL and
  hinge. SRP-2's localization evidence (cytosolic, non-secreted) is direct for SRP-2 only.
