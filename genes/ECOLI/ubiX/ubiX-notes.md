# ubiX (P0AG03, E. coli K-12) review notes

## Sources
- No deep-research provider output (provider API keys unavailable); built from UniProt, cached papers
  (PMID:16923914 and PMID:17889824 abstracts; PMID:25647642 and PMID:26083754 full text) and the PTHR43374
  PAINT file.

## Findings
- PAD1/UbiX are not decarboxylases [PMID:25647642 "However, it does not function as a decarboxylase. Rather,
  PAD1 catalyzes the formation of a novel, diffusible cofactor required by FDC for decarboxylase activity."]
- prFMN made by UbiX/Pad1 [PMID:26083754 "it requires a new type of cofactor: a prenylated flavin synthesized by
  the associated UbiX/Pad1"].
- deltaubiX phenotype [PMID:17889824 "LLI produces very low levels of Q, grows slowly on succinate as the sole
  carbon source, accumulates 4-hydroxy-3-octaprenyl-benzoate"].

## Decisions
- Carboxy-lyase IBA REMOVE: the current PAINT file for PTN000764671 (2026-06-17) carries GO:0106141 and
  GO:0006744 only; the GOA IBA is a leftover from the PAD1-as-decarboxylase era. propagation_review added.
- catalytic activity / prenyltransferase activity IEA MODIFY to GO:0106141 flavin prenyltransferase activity.
- UQ biosynthesis rows ACCEPT (UbiX supplies the cofactor the UbiD step depends on; PAINT asserts it).
- No location asserted: UniProt gives none and no localisation experiment is cited in GOA.
- cache/go/terms.csv gained the GO:0120232 row (written by validation; the term is used in core_functions).
