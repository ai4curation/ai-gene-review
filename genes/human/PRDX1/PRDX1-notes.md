# PRDX1 notes

## 2026-11-28 PTHR10681 human family review

Automated Falcon deep research was attempted with `just deep-research-falcon human PRDX1 --fallback perplexity-lite`,
but the local deep-research client only exposed `claude_code` and `agentapi` was unavailable. No extra sub-workers
were allowed for this campaign, so this review used manual literature triage from the seeded GOA references,
the UniProt record, Reactome records, and the existing PTHR10681 family review.

Key evidence:

- PMID:9497357 shows that recombinant Prx I, II, and III have peroxidase activity, use thioredoxin
  as reducing equivalents for H2O2 reduction, and places Prx I/II in the cytosol.
- PMID:11986303 assayed PRDX1 peroxidase activity and showed strong inhibition after Cdc2/CDK1
  phosphorylation of Thr90.
- PMID:17603937 places PRDX1 in the cytoplasm and nucleus and shows compartment-specific peroxide
  control of NF-kappaB-associated thiol systems.
- PMID:18606987 identifies PRDX1 and PRDX2 as HDAC6-regulated peroxiredoxins whose major function
  is H2O2 reduction.
- Reactome:R-HSA-9968214 treats extracellular PRDX1 as a DAMP released from damaged cells, which
  supports a peripheral extracellular-region row but not a core location.

Decisions:

- The core retained function is cytosolic thioredoxin-dependent peroxiredoxin activity in hydrogen
  peroxide catabolism and cell redox homeostasis.
- Obsolete or broad MF rows are either refined to `GO:0140824` where their evidence supports the
  same catalytic reaction, or marked over-annotated when they add only a broad antioxidant or
  oxidoreductase parent.
- Bare `GO:0005515` protein-binding IPI rows are removed as uninformative per project policy unless
  the row's own paper supports a specific binding term, as for androgen receptor and MST1/STK4 binding.
- High-throughput RNA-binding, exosome, and cadherin-binding rows are not treated as core PRDX1
  function.
