# PP_3995 curation notes

## Functional assignment

PP_3995/Q88FT7 is assigned as the structural TusB-family subunit of TusBCD by
the specific IPR007215 and TIGR03011 family records and its position in the
contiguous PP_3993-PP_3996 `tusD-tusC-tusB-tusE` locus.
[file:PSEPK/PP_3995/PP_3995-uniprot.txt "DR   InterPro; IPR007215;
Sulphur_relay_TusB/DsrH."] The machine-generated UniProt recommended name is
not used as the evidentiary anchor.

The complex-level assignment is transferred from the *E. coli* TusBCD
structure; no direct KT2440 complex study was identified. [PMID:16472754 "Here,
we solved the 2.15 angstroms crystal structure of the E. coli TusBCD complex, a
sulfur transfer mediator, forming a heterohexamer composed of a dimer of the
heterotrimer."] The complete *E. coli* relay was also reconstituted with TusBCD.
[PMID:16387657 "Efficient 2-thiouridine formation in vitro was reconstituted
with recombinant TusA, a TusBCD complex, TusE, and previously identified IscS
and MnmA."]

## Completion pass (module bacterial_mnma_trna_thiolation)

- Every existing row now carries verbatim support: KT2440 UniProt family
  signatures (InterPro, NCBIfam, HAMAP, PIRSF, PANTHER) and active-site features,
  the cached E. coli primary papers (PMID:16387657, PMID:16472754,
  PMID:12549933, PMID:16871210, abstract-only), and the OpenScientist locus and
  identity analysis (quoted, not treated as experimental evidence).
- Broad terms (tRNA processing, tRNA modification, transferase,
  sulfurtransferase) are MODIFIED to the specific terms the gene already
  carries, matching the treatment of the E. coli orthologs in
  genes/ECOLI/*. GOA and module files are no longer listed as references.
- No KT2440-specific experiment on the Tus relay or MnmA was found; all
  functional assignments are ortholog- and locus-based.
