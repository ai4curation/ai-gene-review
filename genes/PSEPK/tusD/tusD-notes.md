# tusD curation notes

## Functional assignment

PP_3993/Q88FT9 is the TusD-family catalytic sulfur-bearing subunit in the
contiguous `tusD-tusC-tusB-tusE` locus. The target retains the
Cys78-equivalent residue identified by the OpenScientist sequence analysis.
[file:projects/P_PUTIDA/deep-research/PSEPK__bacterial-mnma-trna-wobble-uridine-thiolation-sulfur-relay__ppu04122-deep-research-openscientist.md
"**Catalytic Cys78-equivalent conserved**"]

The orthologous *E. coli* structure establishes TusBCD as a heterohexamer and
mutagenesis identifies TusD Cys78 as the sulfur-transfer residue.
[PMID:16472754 "In vivo mutant analyses revealed that only Cys78, in the TusD
subunit, participates in sulfur transfer during the s2U modification process."]
Accordingly, broad sulfurtransferase activity is retained as non-core rather
than rejected; sulfur carrier activity is the more specific molecular-function
summary.

No direct biochemical characterization of KT2440 TusD was identified, so the
species assignment remains a conservative family-, residue-, and locus-based
transfer from the enterobacterial mechanism. [PMID:16387657 "TusE binds TusBCD
complex and stimulates sulfur transfer from TusA to TusD."]

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
