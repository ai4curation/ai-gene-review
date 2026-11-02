# gmhA curation notes

- Q88N89 carries the exact phosphoheptose-isomerase reaction, EC 5.3.1.28, and
  GmhA-specific HAMAP/InterPro signatures
  [file:PSEPK/gmhA/gmhA-uniprot.txt, "Catalyzes the isomerization of
  sedoheptulose 7-phosphate"].
- The same record maps Q88N89 to `PTHR30390:SF6` with the label "DNAA
  INITIATOR-ASSOCIATING PROTEIN DIAA", but this conflicts with the exact
  catalytic, pathway, and GmhA-family evidence
  [file:PSEPK/gmhA/gmhA-uniprot.txt, "PTHR30390:SF6; DNAA
  INITIATOR-ASSOCIATING PROTEIN DIAA"]. The module therefore uses the
  GmhA-specific InterPro selector rather than transferring a DiaA role.
- The broad carbohydrate-binding rows are not used as core functions; the
  exact GO:0008968 reaction and GO:2001061 product process carry the biological
  assertions.

## 2026-10-25 source-specific annotation audit

All 8 seeded annotations were reviewed individually. The central assignment remains a predicted GmhA enzyme; there is no direct Q88N89 enzymology in the sources examined.

- HAMAP MF_00067, CDD SIS_GmhA and InterPro IPR004515 support the catalytic GmhA assignment independently of GOA. The broad GmhA/DiaA family alone does not establish catalysis, and the inherited diaA synonym does not establish a DnaA regulatory role. No new replication annotation is added.
- [PMID:18056714, "Here we report structures of GmhA from Escherichia coli and Pseudomonas aeruginosa in apo, substrate, and product-bound forms"] supports homolog catalytic chemistry and substrate recognition. These are not experiments on KT2440 Q88N89.
- Cytoplasm and zinc binding are accepted as conserved aspects of the core enzyme, with the comparative evidence explicit. Broad sugar-binding rows are retained as substrate recognition, not a separate lectin function. The exact isomerase MF is the single synthesized core activity.
- [file:PSEPK/gmhA/gmhA-uniprot.txt, "Binds 1 zinc ion per subunit."] is a curated HAMAP cofactor inference. It is not a metal-occupancy measurement on Q88N89. The record's phrase "racemic mixture" is not repeated: alpha/beta heptoses are anomers, not an enantiomeric pair.
- The two broad metabolic terms are MODIFY to the already annotated GO:2001061. Independent functional text and primary homolog experiments replace DE/EC-label support; circular module and GOA-file references were removed.
- Falcon research was attempted with perplexity-lite fallback: Falcon authentication failed (403); Perplexity returned 401 insufficient_quota. Logs: `/tmp/adp-gmhA-deep.log`. No generated research file was fabricated; this section records the manual primary-literature review.

### Row ledger

1. GO:0005737 IEA — ACCEPT: The soluble GmhA pathway operates in the cytoplasm.
2. GO:0005975 IEA — MODIFY: Carbohydrate metabolism is correct but less specific than the demonstrated reaction class.
3. GO:0008270 IEA — ACCEPT: GmhA is predicted to bind catalytic zinc.
4. GO:0008968 IEA — ACCEPT: The GmhA-specific assignment supports sedoheptulose 7-phosphate isomerization.
5. GO:0030246 IEA — ACCEPT: Recognition of the sugar substrate is part of GmhA catalysis.
6. GO:0097367 IEA — ACCEPT: The GmhA substrate is a phosphorylated carbohydrate derivative.
7. GO:1901135 IEA — MODIFY: GmhA catalyzes a specific carbohydrate-derivative biosynthetic reaction.
8. GO:2001061 IEA — ACCEPT: GmhA directly produces D-glycero-D-manno-heptose 7-phosphate.

Action counts: 6 ACCEPT, 2 MODIFY.

### Evidence and retrieval limits

- The publication cache was populated with `just fetch-gene-pmids` in parallel with research retrieval. Existing UniProt/GOA files were not modified.
- `just fetch-fitness PSEPK gmhA` failed: no local FEBA database or BarSeqR tables were available and no remote FEBA source was reachable. No fitness artifact was written and no growth phenotype or essentiality claim is inferred from this failure.
- No NEW annotations were added. All seeded annotation fields and rows were preserved; only review judgments and synthesis were revised. Broad correct metabolic/catalytic terms were refined with MODIFY, not removed or marked false merely because they were broad.
- The generated OpenScientist report's assertion of a genome-confirmed HldD gap has not been independently reproduced in this audit. An unresolved assignment is not proof that the protein or reaction is absent. Upstream D,D chemistry does not by itself establish a KT2440 L,D endpoint.
