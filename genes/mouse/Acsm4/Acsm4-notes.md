# Acsm4 (mouse, Q80W40) curation notes

## Session 2026-11-02

### Sources and deep research
- Perplexity deep research was not run: the provider is not available in this environment (available: openscientist, claude_code). No `-deep-research-<provider>.md` file was created.
- `mod-description-deep-research mouse Acsm4` returned `no_curated: 1`: MGI has no curated description, so no `-deep-research-mgi.md` was written.
- There is no primary functional literature on mouse Acsm4. All activity rows trace to the rat ortholog paper PMID:12709059 (abstract only): [PMID:12709059 "Recombinant O-MACS protein tagged with c-Myc and His6 demonstrated an acyl-CoA synthetase activity for fatty acid activation"].
- Mitochondrion HDA comes from MitoCarta [PMID:18614015 "we performed mass spectrometry, GFP tagging, and machine learning to create a mitochondrial compendium of 1098 genes and their protein expression across 14 mouse tissues"].

### Decisions
These are kept consistent with genes/rat/Acsm4 and genes/human/ACSM4.
- GO:0004321 fatty-acyl-CoA synthase activity: all three rows are REMOVE.
  - IBA: from PTHR43605 node PTN001944787, recorded as a GO_CENTRAL source defect.
  - ISO (GO_REF:0000096) and Ensembl IEA (GO_REF:0000107): both derive from the erroneous rat RGD IDA row. Fixing RGD:727928 removes them. The RGD source defect is recorded on the rat review.
- GO:0006633 fatty acid biosynthetic process (IBA, and ARBA IEA): MARK_AS_OVER_ANNOTATED. The seed paper says [PMID:11470804 "acyl-CoAs produced by MACS1 and Sa protein are utilized mainly for oxidation"].
- GO:0006637: MODIFY to GO:0046949 fatty-acyl-CoA biosynthetic process.
- GO:0015645: MODIFY to GO:0031956.
- GO:0031956, GO:0102391 and the mitochondrion rows: ACCEPT. Mitochondrial matrix (IBA): ACCEPT.
