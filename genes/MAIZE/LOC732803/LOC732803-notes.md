# LOC732803 notes (K7TR93; orange pericarp 2 / TSB2)

## Session 2026-10-28

- `just fetch-gene MAIZE LOC732803` resolved by symbol to A0A804RDH5 (the
  Zm00001eb416990_P002 transcript model, 3 IEA rows). The requested accession K7TR93 still
  exists, carries GeneID 732803 and has its own 6 GOA rows (including 3 IBA), so the folder
  was re-fetched with `--uniprot-id K7TR93`. The review is for K7TR93.
- Identity: GeneID 732803 = "orange pericarp 2" (TSB2, orp2), chromosome 10; Swiss-Prot
  counterpart P43284 (fragment). Paralog orp1/TSB1 = LOC732842 / K7TTR0 / P43283.
- Sequence check (bioinformatics/RESULTS.md): PLP lysine K174 retained; K7TR93 is 96.6%
  identical to P43284 and 98.2% to P43283, so the Swiss-Prot TSB2 cDNA is not a near-exact
  match. Not treated as a defect; question raised.
- Key evidence: [PMID:1356534 "Together, the biochemical, genetic, and molecular data verify
  the identity of orp1 and orp2 as duplicate structural genes for the beta subunit of
  tryptophan synthase."]; PMID:18430213 shows beta activity in both the beta2 and
  alpha2beta2 fractions of the Zmtsb1 single mutant (TSB2 remaining).
- Decisions:
  - GO:0000162 (IBA, IEA): ACCEPT, core process.
  - GO:0004834 contributes_to (IBA): ACCEPT. GO:0004834 enables (IEA): ACCEPT the term with
    a WRONG_QUALIFIER source defect (the beta subunit cannot perform the IGP + serine
    reaction alone), consistent with the ZmTSA (LOC100170238) review.
  - GO:0005737 cytoplasm (IBA, is_active_in): MODIFY to chloroplast (OAK: chloroplast is_a
    plastid part_of cytoplasm). Bacterial donor P0A879 drives the cytoplasm term.
  - GO:0009507 chloroplast (IEA SubCell, ARBA): ACCEPT; transit peptide + plastid partner.
    No stroma row: no sub-plastid assay and only one line beyond the transit peptide.
  - NEW GO:0052684 (indole + L-serine = L-tryptophan + H2O) as the subunit's own activity.
    Comparator check: E. coli TrpB (P0A879), Arabidopsis TSB1 (P14671) and yeast TRP5
    (P00931) carry only GO:0004834; GO:0052684 is mostly TreeGrafter IEA on TrpB-like
    proteins. So there is a convention of using GO:0004834 for type-1 TSB. Kept the NEW row
    nonetheless because it is an MF the subunit performs itself (beta-reaction measured for
    recombinant ZmTSB1 alone and in TSB2-only extracts), which is exactly the
    "subunit's own activity" case; flagged for expert check.
- Did not add any auxin process term (orp is a tool for Trp-independent IAA studies,
  not a TSB2 function), and no seedling-lethality/development term.
