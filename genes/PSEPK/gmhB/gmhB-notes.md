# gmhB curation notes

- GmhB has a secure D-glycero-beta-D-manno-heptose 1,7-bisphosphate
  7-phosphatase activity and contributes to LPS core precursor synthesis
  [file:PSEPK/gmhB/gmhB-uniprot.txt, "LPS core biosynthesis"].
- The inherited GO:0097171 annotation is not accepted as a core process because
  KT2440 lacks a resolved HldD ortholog; the upstream GmhB reaction does not by
  itself establish the L,D stereochemical endpoint
  [file:projects/P_PUTIDA/deep-research/PSEPK__adp-heptose-biosynthesis__ppu00541-deep-research-openscientist.md,
  "is a genome-confirmed GAP in KT2440"].
- GO:0009244 remains the endpoint-neutral biological-process anchor for GmhB.

## 2026-10-25 source-specific annotation audit

All 7 seeded annotations were reviewed individually. The target-specific biochemical evidence is stronger than the earlier generated report recognized.

- `just fetch-pmid 25848029 --force` successfully refreshed an abstract-only record to full text. The main text explicitly states: [PMID:25848029, "Here, we screened GmhB from Pseudomonas putida (UniProt: Q88RS0 ) and found the enzyme dephosphorylated five substrates"]. The paper reports beta-HBP catalytic efficiency of 1.8 × 10^6 M−1 s−1. Thus both the EXP and IEA GO:0034200 rows are ACCEPT with target-specific evidence.
- The five screened substrates include both HBP anomers, fructose 1,6-bisphosphate, D-allitol 6-phosphate and KDO 8-phosphate. This does not establish five physiological pathways. No extra MF/BP assertions are added from screening promiscuity.
- The existing Falcon report was reused, not rewritten. Its statement that no direct target study was found is incomplete and contradicted by the explicitly identified Q88RS0 experiments. Its reference assessment now flags this limitation; it is only background for a compartment inference, not the source of the catalytic claim.
- [PMID:11751812] reconstitutes the pathway with E. coli K-12 HldE/GmhB and A. thermoaerophilus enzymes in some mixtures. Its LPS mutant/biochemical results provide conserved-pathway context, not KT2440 mutant phenotypes. The UniProt LPS-core role is also expressly by similarity; localization is a PIRNR family inference.
- The broad carbohydrate-metabolism and phosphatase rows are MODIFY to existing GO:0009244 and GO:0034200. GO:0097171 remains UNDECIDED because the reviewed target phosphatase experiment does not determine the downstream L,D endpoint. This supersedes the stronger absence language in the earlier notes above.
- The beta-HBP C-7 hydrolysis reaction and Mg2+ cofactor have publication-linked UniProt support; Zn2+ support is by similarity. Physiological metal preference and the relevance of other in-vitro substrates remain suitable experimental questions.

### Row ledger

1. GO:0005737 IEA — ACCEPT: GmhB acts in the cytoplasmic nucleotide-sugar precursor pathway.
2. GO:0005975 IEA — MODIFY: The broad carbohydrate-metabolism term can be refined to the supported LPS-core precursor pathway.
3. GO:0016791 IEA — MODIFY: The broad phosphatase activity is supported but the substrate-specific reaction is known.
4. GO:0034200 IEA — ACCEPT: The exact beta-heptose-bisphosphate 7-phosphatase activity is directly supported for Q88RS0.
5. GO:0009244 IEA — ACCEPT: GmhB supplies heptose donor precursors for LPS core biosynthesis.
6. GO:0097171 IEA — UNDECIDED: The downstream L,D-heptose endpoint is not established by the GmhB reaction alone.
7. GO:0034200 EXP — ACCEPT: The EXP annotation matches a directly assayed target protein.

Action counts: 4 ACCEPT, 2 MODIFY, 1 UNDECIDED.

### Evidence and retrieval limits

- The publication cache was populated with `just fetch-gene-pmids` in parallel with research retrieval. Existing UniProt/GOA files were not modified.
- `just fetch-fitness PSEPK gmhB` failed: no local FEBA database or BarSeqR tables were available and no remote FEBA source was reachable. No fitness artifact was written and no growth phenotype or essentiality claim is inferred from this failure.
- No NEW annotations were added. All seeded annotation fields and rows were preserved; only review judgments and synthesis were revised. Broad correct metabolic/catalytic terms were refined with MODIFY, not removed or marked false merely because they were broad.
- The generated OpenScientist report's assertion of a genome-confirmed HldD gap has not been independently reproduced in this audit. An unresolved assignment is not proof that the protein or reaction is absent. Upstream D,D chemistry does not by itself establish a KT2440 L,D endpoint.
