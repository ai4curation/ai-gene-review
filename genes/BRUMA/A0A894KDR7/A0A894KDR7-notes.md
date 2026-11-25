# BRUMA A0A894KDR7 / GLC-2 notes

## Setup

- 2026-11-22: fetched `BRUMA` `GLC-2` from UniProt accession `A0A894KDR7` into an accession-named `genes/BRUMA/A0A894KDR7/` folder to avoid overloading the short `GLC-2` name across the broad PTHR18945 Cys-loop receptor family.
- UniProt exact-accession resolution: live UniProtKB returned `A0A894KDR7_BRUMA`, gene `GLC-2`, protein `Glutamate-gated chloride channel subunit 2`, EMBL `MW196266` / `QRW38684.1`, and PANTHER `PTHR18945`.
- Lamassiaude et al. 2022 identify the same cDNA as `B. malayi (Bma): ... GLC-2 (MW196266)`, tying the UniProt accession directly to the Bma-GLC-2 subunit tested in Xenopus oocytes.
- `just fetch-gene-pmids BRUMA A0A894KDR7` found no GOA PMID references; the seven seeded rows all came from GO_REF automated InterPro or UniProt-SubCell mappings.
- `just deep-research-falcon BRUMA A0A894KDR7 --fallback perplexity-lite` could not run because `agentapi` was not on `PATH`; the deep-research wrapper reported only `claude_code` available and both `falcon` and `perplexity-lite` failed before writing provider files.
- `just paint-losses BRUMA A0A894KDR7` reported that A0A894KDR7 is a PTHR18945 member but not a leaf of the cached PAINT tree, so no IRD or IKR loss could be checked on this lineage.

## Annotation decisions

- The seven GOA rows mirror the automated row set on BRUMA A0A0K0J2Q9/AVR-14B: generic receptor, channel and extracellular ligand-gated channel activities, plasma membrane, generic ion transport, membrane and generic ion transmembrane transport.
- Lamassiaude et al. showed that individual B. malayi AVR-14B, GLC-2, GLC-3 and GLC-4 subunits did not yield robust recombinant channels in Xenopus oocytes, but coexpression of Bma-AVR-14B with Bma-GLC-2 produced robust glutamate-sensitive receptors. Model `GO:0008068` as a `contributes_to` molecular-function row rather than assigning independent channel activity to Bma-GLC-2.
- The Lamassiaude assay recorded glutamate-sensitive currents at a fixed holding potential; chloride selectivity is inferred from the Cys-loop GluCl family and the `LGIC_TM_GluCl` CDD signature on A0A894KDR7 rather than directly assayed by ion substitution in that paper.
- Keep `GO:0004888`, `GO:0005216`, `GO:0005230` and `GO:0005886` because they are correct generic parents or location terms for the heteromeric receptor subunit. Mark `GO:0006811`, `GO:0034220` and `GO:0016020` `TOO_GENERAL` beside the new chloride-transport and plasma-membrane assertions.
