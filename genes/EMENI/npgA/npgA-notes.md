# npgA review notes

## 2026-11-06 PTHR12215 review

`npgA`/`cfwA` encodes the broad Sfp-type phosphopantetheinyl transferase of
*Aspergillus nidulans*. The local GOA seed has the PTHR12215 PTN000259224 IBAs
for cytosol, holo-[acyl-carrier-protein] synthase activity, and protein
maturation, plus the PTN000954835 fungal lysine-biosynthesis IBA.

Deep research could not run in this checkout because the requested providers
were unavailable from `deep-research-client`; only `claude_code` was listed.
I therefore used the cached UniProt record, the cached GOA-seeded papers, the
UniProt direct papers that were not in GOA, the local PTHR12215 PAINT/family
files, and a web/PubMed search for newer `npgA` papers. The search found the
2015 direct NpgA characterization but did not surface a newer paper that changes
the functional interpretation.

Key direct papers:

- Mootz et al. 2002 functionally characterized *A. nidulans* `npgA` by
  complementation of *S. cerevisiae* `lys5`: "Two yet uncharacterized fungal
  genes, q10474 of Schizosaccharomyces pombe, meanwhile annotated as the
  putative lys7 gene, and npgA of Aspergillus nidulans, also complemented the
  lys5 deletion and have thus been functionally characterized as PPTases."
  [PMID:12127488]
- Keszenman-Pereyra et al. 2003 showed that the temperature-sensitive `cfwA2`
  allele blocks penicillin production: "The cfwA2 mutant did not produce
  penicillin at the non-permissive temperature." [PMID:12664133]
- Oberegger et al. 2003 showed that the `cfwA2` allele blocks both extracellular
  and intracellular siderophores: "Using a strain carrying a
  temperature-sensitive allele, cfwA2, we showed that NpgA is essential for
  biosynthesis of both the peptide bond-containing ferricrocin and the ester
  bond-containing triacetylfusarinene C." [PMID:14508603]
- Marquez-Fernandez et al. 2007 generated conditional and null `cfwA` mutants
  and showed a broad PKS/NRPS activation role. Their abstract states:
  "The PPTase CfwA/NpgA was required for the production of these polyketide
  compounds but dispensable for ergosterol and cerevisterol and for fatty acid
  biosynthesis." [PMID:17277172]
- Kim et al. 2015 cloned `npgA`, assayed NpgA in vivo and in vitro, and found
  severe null phenotypes: "Deletion of the npgA gene caused perfectly a lethal
  phenotype and the absence of asexual/sexual sporulation and secondary
  metabolites such as pigments in A. nidulans." [PMID:25557478]

IBA assessment:

- `PTN000259224` is the eukaryotic/broad SF10 node for Sfp-type
  4'-phosphopantetheinyl transferase activity. `G5EB87` is an experimental
  descendant seed for GO:0008897, so the self-source is direct support rather
  than circularity.
- `PTN000954835` is the fungal node for L-lysine biosynthesis and is supported
  by *S. cerevisiae*, *S. pombe*, and *A. fumigatus* seeds. *A. nidulans* NpgA
  is in this fungal SF10 clade, complements *S. cerevisiae lys5*, and its
  growth defect is remediated by lysine plus triacetylfusarinine C, so there is
  no branch-loss argument against the IBA.
- `GO:0051604 protein maturation` is true but generic. The more informative
  process is phosphopantetheinylation of carrier-domain proteins.

No new narrow secondary-metabolite pathway rows in this pass: NpgA plainly
activates NRPSs/PKSs used for penicillin, siderophore and polyketide production,
but the present GOA review is sufficient to align the PAINT rows and refine
`protein maturation` to a carrier-protein phosphopantetheinylation NTR without
enumerating every downstream metabolite cluster.
