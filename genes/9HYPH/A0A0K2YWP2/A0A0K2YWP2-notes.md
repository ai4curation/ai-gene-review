# A0A0K2YWP2 — Mesorhizobium australicum T-G1 PgeF fragment — review notes

Reviewed 2026-10-28. The family literature, the PgeF biochemistry and the critique of the CMMMech
`bixbyite-mn.yaml` claims are in `genes/MESAW/Mesau_02205/Mesau_02205-notes.md` (UniProtKB:L0KKS2).
They are not repeated here.

## Identity

- A0A0K2YWP2_9HYPH: 54-aa TrEMBL fragment (NON_TER at both ends), PE 3, taxon 536018
  (species level), strain T-G1. Translated from EMBL LN864498 / CRL80388.1, the RT-PCR amplicon
  deposited by Bohu et al. 2015
  [PMID:26236307 "The partial sequence of the orthologs of mesau_02205 for RT-PCR was also deposited in the EMBL database under the accession number LN864498."].
  No gene name in UniProt. Not in any reference proteome.
- Same protein as L0KKS2? No. The UniParc ids differ (UPI00067A44EE vs UPI00022DFB2D) and the sequences
  differ. The fragment aligns to L0KKS2 residues 207-260 at 48/54 identity (88.9%), without gaps
  (`A0A0K2YWP2-bioinformatics/RESULTS.md`). It is the T-G1 counterpart of the WSM2073 locus from a
  different strain: probably orthologous, as Bohu et al. call it, but a 54-residue fragment
  cannot establish locus identity. Following repo conventions this gives one review per accession, with
  L0KKS2 recorded as an `alternative_records` REFERENCE_PROTEOME_CANDIDATE (UP000010998). Equivalence
  is not asserted and GO annotations are not transferred.
- The fragment covers the C-terminal quarter of the PgeF domain. The catalytic cysteine (L0KKS2
  Cys117, aligned with E. coli PgeF Cys107) lies outside it. Any functional statement about this
  record is a family-level inference about the full-length T-G1 protein whose partial sequence it is.

## CMMMech

- CMMMech gives this record `gene_symbol: Mesau_02205`. That is the WSM2073 locus tag, not a T-G1
  gene name.
- Its `functional_role` repeats the "putative multicopper polyphenol oxidase (Cu-oxidase_4)"
  label. The protein belongs to the PgeF/LACC1 family and is not a multicopper oxidase; see the
  MESAW notes.
- The only experimental data on this sequence are transcript levels (qRT-PCR) in pH 5.5 versus
  pH 7.2 T-G1 cultures. They show expression correlated with acidic Mn(II) oxidation. They do not
  show function.

## Decisions

- cytoplasm (IEA SubCell, ARBA-derived) -> ACCEPT as the location of the full-length T-G1 PgeF,
  the cytoplasmic PG-precursor editing enzyme.
- No NEW rows on the fragment record. Process and function proposals are made on the
  full-length reference-proteome record L0KKS2.
