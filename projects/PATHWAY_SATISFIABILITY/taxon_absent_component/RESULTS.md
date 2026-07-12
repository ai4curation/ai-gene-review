# Taxon-absent-component detector — results

- **Target taxon:** 44689  ·  **Control taxon:** 9606
- Two oracles per component: **PANTHER family** (primary, divergence-robust)
  and **InterPro domain** (contrast). Counts fetched live from UniProt REST.
- `COMPONENT_PRESENT` where PANTHER finds a member; `ABSENT` where it does
  not (confidence HIGH when InterPro agrees). A **divergence flag** marks
  components present by PANTHER but missed by the InterPro domain screen.

| Case | GO term | Component | PANTHER (ctrl/tgt) | InterPro (ctrl/tgt) | Status | Conf | Divergent? |
|------|---------|-----------|:------------------:|:-------------------:|--------|:----:|:----------:|
| jak_stat | GO:0007259 | Janus kinase (JAK) | 56/0 | 56/0 | **ABSENT** | HIGH | - |
| stat_divergence_control | GO:0097696 | STAT transcription factor (divergent in Dictyostelium) | 128/4 | 100/0 | **COMPONENT_PRESENT** | - | YES |
| gpcr_purinergic | GO:0035589 | metabotropic (P2Y-type, GPCR) purinergic receptor | 21/0 | 3/0 | **ABSENT** | HIGH | - |
| p2x_divergence_control | GO:0035590 | P2X ionotropic receptor (divergent in Dictyostelium) | 47/5 | 26/0 | **COMPONENT_PRESENT** | - | YES |

## Interpretation

### jak_stat — ABSENT (confidence HIGH)

- **Term:** GO:0007259 — cell surface receptor signaling pathway via JAK-STAT
- **PANTHER:** PTHR45807 ctrl 56/tgt 0
- **InterPro:** IPR051286 ctrl 56/tgt 0
- **Corroboration:** TRUE ABSENCE (both oracles agree). Dictyostelium STATs (Dd-STATa/c) are activated JAK-independently by the TKL kinases Pyk2/Pyk3; no JAK-family kinase is encoded. Correct annotation: the JAK-independent parent GO:0097696 (STAT signaling).

### stat_divergence_control — COMPONENT_PRESENT

- **Term:** GO:0097696 — STAT signaling (control - STAT itself IS present in Dictyostelium)
- **PANTHER:** PTHR11801 ctrl 128/tgt 4
- **InterPro:** IPR013801 ctrl 100/tgt 0, IPR012345 ctrl 99/tgt 0
- **⚠ Divergence flag:** present by PANTHER but the InterPro domain signature scores zero — a domain-only screen would have falsely called this absent.
- **Corroboration:** PRESENT (divergent). PANTHER recovers the four Dd-STATs; the InterPro domain signature misses them because they are too sequence-divergent from metazoan STATs. The panther/interpro DISAGREEMENT is the divergence flag.

### gpcr_purinergic — ABSENT (confidence HIGH)

- **Term:** GO:0035589 — G protein-coupled purinergic nucleotide receptor signaling pathway
- **PANTHER:** PTHR24231 ctrl 21/tgt 0
- **InterPro:** IPR000142 ctrl 2/tgt 0, IPR000018 ctrl 3/tgt 0
- **Corroboration:** ABSENT (both oracles agree). P2Y GPCRs are a metazoan expansion, absent from Dictyostelium. Note this is specific to the GPCR pathway - the organism does have ionotropic P2X receptors (next case).

### p2x_divergence_control — COMPONENT_PRESENT

- **Term:** GO:0035590 — purinergic nucleotide receptor signaling pathway (P2X, ionotropic - control)
- **PANTHER:** PTHR10125 ctrl 47/tgt 5
- **InterPro:** IPR001429 ctrl 26/tgt 0
- **⚠ Divergence flag:** present by PANTHER but the InterPro domain signature scores zero — a domain-only screen would have falsely called this absent.
- **Corroboration:** PRESENT (divergent). PANTHER recovers ~5 Dictyostelium P2X receptors, matching Fountain et al. 2007 (Nature 448:200); the InterPro P2X family signature misses them. Another panther/interpro divergence flag.

