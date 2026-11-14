# LhpG (KGSADH-III) curation notes

- Deep research: unavailable. `just deep-research-falcon` fails for every gene
  in this session (the Edison provider API returns 403 "Failed to
  authenticate"), so no provider file was written and none was fabricated.
  This review rests on the cached abstract of PMID:17202142, the UniProt
  record Q08IB7, and the PANTHER PTHR43353 member listing.
- Literature searched: the repository's cached publications were searched for
  hydroxyproline and KGSADH terms, which returned PMID:17202142 (the
  characterization of the A. brasilense isozymes), PMID:16835232 (the
  L-arabinose-pathway KGSADH-I), PMID:22833679 and PMID:24980702 (the
  bacterial hydroxyproline pathway). No full text is cached for PMID:17202142
  and it has no PMC record, so the kinetic constants are taken from UniProt's
  curated, publication-linked statements.
- How this gene was found: re-deriving the PTHR43353:SF3 membership from
  `interpro/panther/PTHR43353/PTHR43353-entries.csv` during review of PR #6274
  showed that the subfamily contains KGSADH-III, whose UniProt FUNCTION states
  "Involved in hydroxy-L-proline metabolism". It is the only characterized
  terminal dehydrogenase of the hydroxyproline route; the module previously
  had only the D-glucarate enzyme of A. baylyi as an exemplar for that step.
- Route assignment rests on induction, not on an in-pathway assay: KGSADH-III
  is the "hydroxy-l-proline-inducible" isozyme and was purified from cells
  grown on hydroxy-L-proline, as against the "d-glucarate/d-galactarate-inducible"
  KGSADH-II [PMID:17202142, "d-glucarate/d-galactarate-inducible KGSADH-II and
  hydroxy-l-proline-inducible KGSADH-III"]. GO:0019470 is therefore proposed
  with IEP rather than IDA.
- Cofactor caveat: the UniProt record is internally inconsistent about which
  cofactor gives faster turnover. Vmax is 30.7 umol/min/mg with NAD+ against
  16.4 with NADP+, while kcat is 21.3 s-1 with NAD+ against 23.0 s-1 with
  NADP+, and neither kcat matches its Vmax for a subunit of this size. The
  reviews therefore cite the Km difference (0.0149 mM NADP+ against 1.136 mM
  NAD+, about 75-fold) and the Vmax figures, and make no claim about turnover.
- KGSADH-I, the L-arabinose-pathway isozyme, is reported as poorly related to
  KGSADH-II and KGSADH-III, so the L-arabinose route is not claimed for this
  subfamily [PMID:17202142, "KGSADH-II and KGSADH-III were poorly related to
  the known ALDH subclasses including KGSADH-I"].
