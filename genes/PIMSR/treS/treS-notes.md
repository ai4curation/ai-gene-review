# treS (Pimelobacter sp. R48, P72235) curation notes

## Sources

- No deep-research provider run was made for this gene; this review rests on
  the fetched UniProt record and the cached PubMed abstract below.
- Tsusaki et al. cloned the trehalose synthase gene from Pimelobacter sp. R48,
  the organism from which the enzyme was first described. [PMID:8645698, "The
  gene encoding trehalose synthase (catalyzing the conversion of maltose into
  alpha, alpha-trehalose by intramolecular transglucosylation) was cloned from
  Pimelobacter sp. R48."]
- The 573-residue product matches P72235. [PMID:8645698, "Sequence analysis
  revealed a 1719-bp synthase gene and a 573-residue amino-acid sequence."]
- UniProt places it in PANTHER PTHR10357:SF219 with the TIGR02456 TreS
  N-terminal signature; its FUNCTION and active-site annotations are
  propagated from M. smegmatis TreS (A0R6E0).
  [file:PIMSR/treS/treS-uniprot.txt, "DR   PANTHER; PTHR10357:SF219; MALTOSE ALPHA-D-GLUCOSYLTRANSFERASE; 1."]

## Decisions

- GO:0003824 and GO:0005975 (InterPro2GO) are MODIFIED to GO:0047471 and to
  the direction-neutral GO:0005991 trehalose metabolic process, because the
  reaction is reversible and in vivo direction is untested.
- Thermus aquaticus TreS (O06458, 963 aa) was considered as a second
  classical-TreS exemplar but not used: its C-terminal ~416 residues are not
  homologous to Pimelobacter TreS and are uncharacterized.
  [PMID:9042362 abstract: "The 547 N-terminal residues were homologous to the
  full-length synthase from Pimelobacter sp. R48 (53.8% identity)."]
