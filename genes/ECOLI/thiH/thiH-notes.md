# thiH (P30140) notes, E. coli K-12

Deep research was unavailable for this gene (falcon 403, asta returned nothing in Phase 1
of the RADICAL_SAM project). Notes are built from cached publications, PubMed and UniProt.

## Identity

- UniProt P30140, 2-iminoacetate synthase (tyrosine lyase, dehydroglycine synthase),
  EC 4.1.99.19, b3990, last gene of thiCEFSGH. Radical SAM superfamily, ThiH family
  (TIGR02351, IPR012726), with a C-terminal BATS domain (shared with HydG/NosL).
  One radical SAM [4Fe-4S] cluster (Cys85/89/92). Heterodimer with ThiG (P30139)
  [file:ECOLI/thiH/thiH-uniprot.txt].

## Which subunit does what

- ThiH (radical SAM) cleaves the Calpha-Cbeta bond of L-tyrosine to dehydroglycine
  (2-iminoacetate) and p-cresol, consuming SAM to 5'-dA + Met
  [PMID:19923213 "ThiH is a tyrosine lyase that cleaves the C alpha-C beta bond of tyrosine, generating p-cresol as a by-product, to form dehydroglycine."].
- ThiG (thiazole synthase, GO:1990107) condenses dehydroglycine with DXP and ThiS
  thiocarboxylate to form the thiazole phosphate
  [PMID:17403671 "the resultant substrate radical cleaves to yield dehydroglycine, which is required by ThiG for the thiazole cyclization reaction"].
- ThiG and ThiH co-purify as a complex [PMID:12650933 "When isolated under anaerobic conditions, ThiG and ThiH-His co-purify as a large multimeric non-covalent complex."];
  described as an alpha-beta heterodimer [PMID:19923213 "Thiazole synthase in Escherichia coli is an alphabeta heterodimer of ThiG and ThiH."].
  ThiH has been studied only as the ThiGH complex, so the GO complex term
  GO:1902508 2-iminoacetate synthase complex fits (ThiG also carries it in GOA).
  ThiH should NOT get thiazole synthase activity (that is ThiG); the complex could equally
  be called the thiazole synthase complex (GO:1902507), which GOA does not use for either
  subunit.
- [4Fe-4S] cluster reconstitution essential; SAM binds the cluster
  [PMID:17403671 "Spectroscopic studies with ThiGH strongly suggested that S-adenosylmethionine (AdoMet) bound to the [4Fe-4S] cluster"].
- Catalytic (multiple turnover) tyrosine lyase with product inhibition by 5'-dA (PMID:19923213).
- In aerobes (B. subtilis) ThiO glycine oxidase replaces ThiH; module
  thiamine_diphosphate_biosynthesis models this as alternative dehydroglycine routes.

## Genetics

- thiH required for thiazole synthesis [PMID:8432721 "The thiE, thiF, thiG, and thiH gene products are required for synthesis of the thiazole."].
- DNA damage response (PMID:11967071): mitomycin C microarray expression change; not a function.

## Curation decisions

- GO:1904047 SAM binding absent from GOA; added as NEW (IDA, PMID:17403671).
- Iron ion binding (GO:0005506): lateral MODIFY to GO:0051539, as for GO:0046872 under the
  RADICAL_SAM treatment rule; ThiH has no separate iron site.
- Protein binding (ThiG) REMOVE as uninformative; the ThiGH association is captured by
  GO:1902508.
