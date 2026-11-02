# hldE curation notes

- Q88D93 is a bifunctional HldE whose kinase domain forms
  D-glycero-beta-D-manno-heptose 1,7-bisphosphate and whose
  adenylyltransferase domain forms ADP-D-glycero-beta-D-manno-heptose
  [file:PSEPK/hldE/hldE-uniprot.txt, "yielding
  ADP-D-glycero-beta-D-manno-heptose"].
- The target-genome analysis found no credible HldD/GmhD ortholog by KEGG,
  UniProt/UniRef, RefSeq, or genome-level similarity search
  [file:projects/P_PUTIDA/deep-research/PSEPK__adp-heptose-biosynthesis__ppu00541-deep-research-openscientist.md,
  "is a genome-confirmed GAP in KT2440"]. No broad NAD-dependent epimerase is
  assigned to fill this step.
- GO:0097171 names the downstream ADP-L,D-heptose endpoint and remains
  `UNDECIDED`. GO has no process term for the directly produced ADP-D,D-heptose
  endpoint, so a new child of GO:0009226 is proposed without inventing an id.

## 2026-10-25 source-specific annotation audit

All 11 seeded annotations were reviewed individually. Both exact catalytic activities are accepted by curated HldE-specific domain/rule evidence with E. coli primary homolog support, not a KT2440 biochemical assay.

- The reaction order is HldE kinase → GmhB phosphatase → HldE adenylyltransferase. It is essential to retain the intervening C-7 dephosphorylation, since HldE's second domain consumes heptose 1-phosphate, not the bisphosphate kinase product.
- [PMID:11751812, "Synthetic d -β- d -heptose 1-phosphate was incubated with the RfaE protein and ATP, resulting in a peak comigrating with synthetic ADP- d -β- d -heptose"] supports the E. coli reaction. The tested proteins are E. coli and, in some coupled mixtures, A. thermoaerophilus; Q88D93 was not assayed in this study.
- The adenylyltransferase transfers **AMP**, not ADP, from ATP to the phosphate-bearing sugar, releasing pyrophosphate. The previous review and UniProt CC:FUNCTION phrase "ADP transfer" were chemically misleading. The review now quotes the correct curated CC:CATALYTIC ACTIVITY equation. Immutable UniProt source text was preserved.
- Kinase, alcohol-acceptor phosphotransferase, nucleotidyltransferase and broad catalytic/transferase rows are MODIFY to the appropriate one or both existing exact activities. ATP binding is accepted as core cosubstrate recognition. Carbohydrate metabolism is refined to nucleotide-sugar biosynthesis without imposing terminal stereochemistry.
- Cytosol remains UNDECIDED: TreeGrafter supplies the original annotation but no independent target localization statement was found. Purified soluble E. coli HldE is compatible with the inference but does not directly localize native Q88D93.
- GO:0097171 remains UNDECIDED; the adenylyltransferase makes ADP-D,D-heptose, and terminal C-6 epimerization is separate. The existing proposed term for ADP-D,D-heptose biosynthesis is retained with reaction-level support and no invented GO identifier. This does not imply proven absence of an HldD enzyme in KT2440.
- Falcon research was attempted with perplexity-lite fallback: Falcon authentication failed (403); Perplexity returned 401 insufficient_quota. Logs: `/tmp/adp-hldE-deep.log`. No provider report was fabricated; this section records manual primary-literature work.

### Row ledger

1. GO:0003824 IEA — MODIFY: HldE has two specific catalytic activities.
2. GO:0005524 IEA — ACCEPT: ATP is a cosubstrate for both HldE reactions.
3. GO:0005829 IEA — UNDECIDED: Cytosolic localization is consistent with soluble HldE-mediated nucleotide-sugar metabolism.
4. GO:0005975 IEA — MODIFY: HldE directly catalyzes nucleotide-sugar biosynthesis.
5. GO:0016301 IEA — MODIFY: The N-terminal HldE domain is a heptose 7-phosphate kinase.
6. GO:0016772 IEA — MODIFY: Both HldE domains transfer phosphorus-containing groups.
7. GO:0016773 IEA — MODIFY: The kinase transfers phosphate to the C-1 hydroxyl of heptose 7-phosphate.
8. GO:0016779 IEA — MODIFY: The C-terminal HldE domain is an adenylyltransferase.
9. GO:0033785 IEA — ACCEPT: HldE phosphorylates beta-heptose 7-phosphate at C-1.
10. GO:0033786 IEA — ACCEPT: HldE activates heptose 1-phosphate to form ADP-D,D-heptose.
11. GO:0097171 IEA — UNDECIDED: HldE makes the D,D-heptose nucleotide sugar, upstream of any C-6 epimerization.

Action counts: 6 MODIFY, 3 ACCEPT, 2 UNDECIDED.

### Evidence and retrieval limits

- The publication cache was populated with `just fetch-gene-pmids` in parallel with research retrieval. Existing UniProt/GOA files were not modified.
- `just fetch-fitness PSEPK hldE` failed: no local FEBA database or BarSeqR tables were available and no remote FEBA source was reachable. No fitness artifact was written and no growth phenotype or essentiality claim is inferred from this failure.
- No NEW annotations were added. All seeded annotation fields and rows were preserved; only review judgments and synthesis were revised. Broad correct metabolic/catalytic terms were refined with MODIFY, not removed or marked false merely because they were broad.
- The generated OpenScientist report's assertion of a genome-confirmed HldD gap has not been independently reproduced in this audit. An unresolved assignment is not proof that the protein or reaction is absent. Upstream D,D chemistry does not by itself establish a KT2440 L,D endpoint.
