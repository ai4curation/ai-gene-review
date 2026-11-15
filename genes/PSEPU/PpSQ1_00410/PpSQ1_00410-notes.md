# PpSQ1_00410 (P0DOV6) 6-deoxy-6-sulfogluconolactonase, Pseudomonas putida SQ1 — notes

## Provenance and access

- Deep research (`just deep-research ... --provider perplexity`) failed in this environment on
  2026-11-10 (provider requirements unresolvable; "All providers failed"), so no provider file
  exists. Sources: UniProt P0DOV6, PMID:26195800 (abstract only; PNAS restricts PMC XML),
  PMID:41676062 (review, full text), PMID:39840830 (full text, pathway context).

## Function

- UniProt (ECO:0000269 PubMed:26195800): "Catalyzes the hydrolysis of
  6-deoxy-6-sulfo-D-glucono-1,5-lactone to form 6-deoxy-6-sulfo-D-gluconate." RHEA:47908,
  EC 3.1.1.99. Highly induced on SQ (protein level).
- [PMID:26195800 "It involves an NAD(+)-dependent SQ dehydrogenase,
  6-deoxy-6-sulfogluconolactone (SGL) lactonase, ..."]; pathway reconstituted in vitro from five
  purified enzymes.
- [PMID:41676062 "SGL is then hydrolyzed and ring-opened by an SGL lactonase (SGL-L), yielding
  6-deoxy-6-sulfogluconate (SG)."]
- No kinetic constants and no substrate-range data (e.g. activity on D-glucono-1,5-lactone) are
  available in accessible text. Metal: UniProt infers one divalent cation per subunit only by
  similarity to human regucalcin (Q15493, ECO:0000250); no metal assay on P0DOV6 is available.
- GO has no SGL-lactonase term (OLS search for sulfogluconolactone / sulfogluconate returned no GO
  term, 2026-11-10). Nearest parent: GO:0052689 carboxylic ester hydrolase activity (the module's
  term). GO:0004341 gluconolactonase is defined for D-glucono-1,5-lactone, a different
  (non-sulfonated) substrate.

## GOA rows (all IEA, GO_REF:0000118 TreeGrafter, with PANTHER:PTN001656416)

- PTN001656416 is a leaf of the current PTHR10907 tree (Salmonella STM2668, SF47), the graft
  point. In the current PAINT slice it has no annotated ancestor: the only IBD node,
  PTN004208435 (gluconolactonase/regucalcin; seeds mouse/rat/human regucalcin), covers a 72-leaf
  clade that does not contain the STM2668 leaf. So the three TreeGrafter rows are inherited from a
  PAINT state no longer present in the current slice.
- gluconolactonase -> MODIFY to GO:0052689 (substrate correction to the parent).
- calcium ion binding -> MODIFY to GO:0046872 metal ion binding (cation identity not shown;
  regucalcin-derived Ca2+ claim not transferable).
- L-ascorbic acid biosynthetic process -> REMOVE (animal regucalcin role in the L-gulonolactone
  pathway; Pseudomonas does not make ascorbate this way, and this protein's only shown role is SQ
  catabolism).
