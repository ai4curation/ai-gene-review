# squF (Saro_2444, Q2G5J3) notes

## Deep research
- 2026-11-10: perplexity deep research fails in this environment (no provider credentials;
  "All providers failed", tried on AGRFC smoA). Review built from UniProt and cached literature.

## Sources
- Primary paper Liu et al. 2021 ACS Catal. (DOI 10.1021/acscatal.1c04321), no PMID, not cached;
  UniProt curates function from it as Ref.2
  [file:NOVAD/squF/squF-uniprot.txt "NADP-dependent reduction of 6-dehydro-D-glucose to D-glucose (Ref.2)."]
  plus reverse NADP+-dependent glucose oxidation. UniProt binding-site FTs are by similarity to SmoB.
- Review PMID:41676062
  [PMID:41676062 "Following the C-S cleavage by SquD/SsuE, the NAD(P)H-dependent oxidoreductase SquF reduces 6-dehydro-D-glucose to form glucose, which can enter primary metabolism"]
  ["Both pathways use dehydrogenase (SquF) to form glucose."]

## Decisions
- Same treatment as SmoB (cytosol non-core; oxidoreductase -> GO:0016616; NEW GO:1902777;
  NTR 6-dehydroglucose reductase activity). PANTHER PTHR43364:SF1.
