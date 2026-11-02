# prpE (P77495, b0335) notes

## Session log (2026-10-23)

- Provider deep research (`just deep-research ECOLI prpE --provider ...`) could not be run in this session because provider API credentials were unavailable. No `*-deep-research-*.md` file was created.
- Fetched Salmonella comparators via `just fetch-gene-pmids ECOLI prpE`: PMID:10411265 (abstract only) and PMID:10482501 (PMC full text).
- UniProt entry is PE 3 (inferred from homology) and its FUNCTION text is "By similarity"; the only direct E. coli biochemistry is PMID:22834299 (abstract only).

## Function

- E. coli PCS purified and characterized [PMID:22834299 "Kinetic analyses suggested that the enzyme preferred propionate as substrate but would also use acetate."]; redox regulation [PMID:22834299 "It was revealed that the C128A and C315A mutants had wildtype enzyme activity but were no longer activated by DTT or inhibited by diamide."].
- Expression in E. coli: prpE RNA propionate-specific, protein not seen on 2D gels [PMID:12473114 "except PrpE, which seems to be replaced by acetyl-CoA synthetase"].
- Salmonella ortholog: [PMID:10411265 "Cell-free extracts enriched for PrpE catalysed the formation of propionyl-CoA in a propionate-, ATP-, Mg2+- and HS-CoA dependent manner."]; Acs redundancy [PMID:10411265 "indicating that Acs can compensate for the lack of PrpE in prpE mutants"]; pathway role [PMID:10482501 "In this pathway, PrpE is the propionyl-CoA synthetase ( 13 ) and PrpC is the 2-methylcitrate synthase."].

## Curation decisions

- Accept all 4 rows (propionate-CoA ligase activity x3, propionate catabolic process).
- Considered but did not add NEW acetate-CoA ligase activity: acetate is a secondary in vitro substrate only; not strongly evidenced as a physiological function.
