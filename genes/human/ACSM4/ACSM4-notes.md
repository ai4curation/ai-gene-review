# ACSM4 (human, P0C7M7) curation notes

## Session 2026-11-02

### Sources and deep research
- Perplexity deep research was not run: the provider is not available in this environment (available: openscientist, claude_code). No `-deep-research-<provider>.md` file was created.
- No study has assayed human ACSM4 enzymatically. UniProt function, EC and catalytic activities are "By similarity" to rat Acsm4 (Q7TN78), which was characterised in PMID:12709059 [PMID:12709059 "Recombinant O-MACS protein tagged with c-Myc and His6 demonstrated an acyl-CoA synthetase activity for fatty acid activation"].
- Family context:
  - [PMID:17762044 "Acyl-coenzyme A synthetases (ACSs) catalyze the fundamental, initial reaction in fatty acid metabolism."]
  - [PMID:27351777 "Kinetic data on the substrate specificity of the human ACSM ligases are non-existent"]
- Mitochondrion HTP comes from MitoCoP [PMID:34800366 "defined a mitochondrial high-confidence proteome of >1,100 proteins (MitoCoP)"].

### Decisions
These are kept consistent with the rat and mouse Acsm4 reviews.
- GO:0004321 IBA: REMOVE. This is the synthase/synthetase confusion, with a GO_CENTRAL source defect on PTN001944787.
- GO:0006633 IBA: MARK_AS_OVER_ANNOTATED. The seeds are mouse Acsm1/Acsm3, whose products are [PMID:11470804 "utilized mainly for oxidation"].
- GO:0006637 IBA: MODIFY to GO:0046949.
- GO:0015645 IBA and ISS: MODIFY to GO:0031956.
- Other rows: ACCEPT.
