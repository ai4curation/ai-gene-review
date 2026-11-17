# PpSQ1_00405 (P0DOV5) sulfoquinovose 1-dehydrogenase, Pseudomonas putida SQ1 — notes

## Provenance and access

- `just deep-research PSEPU PpSQ1_00405 --provider perplexity` was tried once (2026-11-10) and
  failed: the provider environment could not be resolved ("All providers failed"). No provider
  deep-research file exists; this journal is built from the UniProt record and cached literature.
- PMID:26195800 (Felux et al. 2015, PNAS) is cached abstract-only (PNAS restricts PMC XML; a
  forced re-fetch returned 403). Curated UniProt statements that cite it (ECO:0000269) carry the
  enzymology details.
- PMID:39840830 (Burchill et al. 2025, Biochem J) was fetched with full text for this review.
- PMID:41676062 (2026 review of SQ catabolism) and PMID:32444469 (Rhizobium sulfo-ED, abstract
  only) used for context.

## Function

- UniProt (curated, ECO:0000269 PubMed:26195800): "Catalyzes the oxidation of sulfoquinovose to
  6-deoxy-6-sulfo-D-glucono-1,5-lactone, with a strong preference for NAD(+) as the electron
  acceptor." Reaction RHEA:47896, EC 1.1.1.390. Km 0.5 mM SQ with NAD+, kcat 33.8 s-1;
  NADP+ much poorer (kcat 1.4 s-1).
- Pathway: [PMID:26195800 "It involves an NAD(+)-dependent SQ dehydrogenase,
  6-deoxy-6-sulfogluconolactone (SGL) lactonase, 6-deoxy-6-sulfogluconate (SG) dehydratase, and
  2-keto-3,6-dideoxy-6-sulfogluconate (KDSG) aldolase."] — reconstituted in vitro from five
  heterologously produced enzymes; the protein is strongly induced during growth on SQ.
- Structure/kinetics [PMID:39840830 "PpSQDH is a tetrameric enzyme belonging to the short-chain
  dehydrogenase/reductase (SDR) superfamily with a strong preference for NAD+ over NADP+."];
  "This corresponds to a million-fold preference for NAD+ in terms of (kcat/KM)app values.";
  ordered mechanism with NAD+ binding first; catalytic tetrad Asn119-Ser147-Tyr160-Lys164; Arg152
  forms the sulfonate pocket; Asp45 confers NAD(H) specificity.
- Exact reactions lack GO terms: GO has no "sulfoquinovose 1-dehydrogenase" MF term (OLS search
  2026-11-10 for sulfoquinovose / sulfogluconolactone returned none). Nearest parent:
  GO:0016616 (oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as
  acceptor), which the module uses. A new-term request is recorded in proposed_new_terms.
- Process: GO:0061722 sulphoglycolysis is defined as SQ breakdown "resulting in the formation of
  glycerone phosphate (DHAP) and pyruvate"; the sulfo-ED route yields pyruvate, so the term fits.

## GOA

- The GOA file has zero rows. PANTHER: PTHR43639:SF1. PAINT root node PTN002462421 (GO:0016491
  oxidoreductase activity, the root of the 55-leaf PTHR43639 tree) would cover the protein, but no
  IBA/TreeGrafter row reached it in this GOA snapshot. The new rows below are added from the
  direct enzymology.

## Family context (for PTHR43639 review)

- SF1 is a mixed SDR subfamily: glucose 1-dehydrogenases (B. megaterium gdh), xylose
  1-dehydrogenase XylB, L-fucose dehydrogenase, pteridine reductase PTR1, hydroxynaphthalene
  reductases, diacetyl reductase ButA, FabL. Membership does not predict substrate.
