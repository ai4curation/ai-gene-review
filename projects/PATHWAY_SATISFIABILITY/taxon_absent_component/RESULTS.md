# Taxon-absent-component detector — results

- **Target taxon:** 44689  ·  **Control taxon:** 9606
- Source: UniProtKB REST (`xref:interpro-*` counts), fetched live.
- **A zero in the target is a CANDIDATE absence, not proof** — divergent
  orthologs can escape a metazoan signature. Read `corroboration`.

| Case | GO term | Obligate component | Control | Target | Status |
|------|---------|--------------------|--------:|-------:|--------|
| jak_stat | GO:0007259 | Janus kinase (JAK) | 56 | 0 | **ABSENT_CANDIDATE** |
| stat_divergence_control | GO:0097696 | STAT transcription factor (divergent in Dictyostelium) | 100 | 0 | **ABSENT_CANDIDATE** |
| gpcr_purinergic | GO:0035589 | metabotropic (P2Y-type, GPCR) purinergic receptor | 3 | 0 | **ABSENT_CANDIDATE** |
| p2x_divergence_control | GO:0035590 | P2X ionotropic receptor (divergent in Dictyostelium) | 26 | 0 | **ABSENT_CANDIDATE** |

## Interpretation

### jak_stat — ABSENT_CANDIDATE

- **Term:** GO:0007259 — cell surface receptor signaling pathway via JAK-STAT
- **Signatures:** IPR051286 (control 56, target 0)
- **Corroboration:** TRUE ABSENCE. Dictyostelium STATs (Dd-STATa/c) are activated JAK-independently by the TKL-family kinases Pyk2/Pyk3; no JAK-family kinase is present in the genome. The correct annotation is the JAK-independent parent GO:0097696 (STAT signaling).

### stat_divergence_control — ABSENT_CANDIDATE

- **Term:** GO:0097696 — STAT signaling (control - STAT itself IS present in Dictyostelium)
- **Signatures:** IPR013801 (control 100, target 0), IPR012345 (control 99, target 0)
- **Corroboration:** FALSE-POSITIVE DEMONSTRATION. Dd-STATa/c are functional STATs but are so sequence-divergent from metazoan STATs that they do not carry the metazoan InterPro STAT signatures. Signature-absence therefore does NOT equal genome-absence in a distant lineage.

### gpcr_purinergic — ABSENT_CANDIDATE

- **Term:** GO:0035589 — G protein-coupled purinergic nucleotide receptor signaling pathway
- **Signatures:** IPR000142 (control 2, target 0), IPR000018 (control 3, target 0)
- **Corroboration:** LIKELY ABSENT but signature is narrow (single subfamilies). P2Y GPCRs are a metazoan expansion. Treat as candidate; confirm with a broader P2Y panel before a confident call.

### p2x_divergence_control — ABSENT_CANDIDATE

- **Term:** GO:0035590 — purinergic nucleotide receptor signaling pathway (P2X, ionotropic - control)
- **Signatures:** IPR001429 (control 26, target 0)
- **Corroboration:** FALSE-POSITIVE DEMONSTRATION. Fountain et al. 2007 (Nature 448:200) characterised functional P2X receptors in Dictyostelium, yet they are divergent enough that the metazoan P2X InterPro family may not annotate them. Signature-absence is not proof of genome-absence.

