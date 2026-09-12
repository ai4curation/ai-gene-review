# mek-1 research notes

Review date: 2026-09-09T03:17:51.839101+00:00. Target: Q7RYZ6, NEUCR, 518 residues. Identity is anchored to the frozen current UniProt accession and gene record. The accession-specific fetch seeded all 16 current GOA rows.

## Evidence basis

MEK-1 is the MAP kinase kinase of the Neurospora crassa MIK-1–MEK-1–MAK-1 signaling module. It is required for MAK-1 phosphorylation and helps control cell wall integrity, vegetative growth, asexual development and sexual differentiation. MEK-1 also accumulates at the contact sites of fusing germlings, linking this signaling module to local remodeling during cell fusion.

- PMID:18849472: “The MAK-1 MAPK was not phosphorylated in Δ mik-1 and Δ mek-1 mutants, consistent with the involvement of MIK-1, MEK-1, and MAK-1 in the same signaling cascade.”
- PMID:41071819: “In a first step, we confirmed the accumulation of the kinase MAK-1 at the contact sites and showed the same localization pattern for both its upstream kinases (Fig 7).”

## Source claim provenance

The full API prediction JSON is preserved without deleting any fields. Function and location reports retain original words, SL identifiers and entire evidence objects. GO sidecars preserve all emitted GO IDs and labels; main reviews assess the independent current GOA rows.


## Research execution

The original Falcon report returned and was inspected. Publication caching ran concurrently. The report is retained as received; consequential claims are checked against primary sources and sequence evidence below.

## Falcon report appraisal

The 342.39-second original Falcon report correctly distinguishes NCU06419/mek-1 from mek-2 and identifies the middle kinase of the cell-integrity cascade. Its principal primary source, PMID:22900028 (DOI:10.1371/journal.pone.0042565), was cached and inspected: Table 1 maps Δmek-1 to NCU06419 and the developmental analysis distinguishes the CWI module. The report’s claim that no direct MEK-1 localization was found is a search limitation. Independently recovered PMID:41071819 contains direct MEK-1-GFP microscopy at germling contacts (Figure 7B); the whole cached results section was inspected. This supports cytoplasmic/cortical localization, not division septum or diffuse uniform cytosol. PMID:18849472 directly shows dependence of MAK-1 phosphorylation on mek-1. The report’s serine/threonine-only substrate shorthand is not used to displace the established MAPKK functional class; specific target biochemical kinetics remain unmeasured. QuickGO definitions of MAP kinase and MAP kinase kinase were checked before modifying the EC-derived MAPK row.
