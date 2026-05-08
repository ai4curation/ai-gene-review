---
provider: falcon
model: manual fallback after wrapper failure
cached: false
start_time: '2026-03-21T13:50:00'
end_time: '2026-03-21T13:50:00'
duration_seconds: 0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: lapA
  gene_symbol: lapA
  uniprot_accession: Q88RG2
  protein_description: 'SubName: Full=Surface adhesion protein {ECO:0000313|EMBL:AAN65801.1};'
  gene_info: OrderedLocusNames=PP_0168 {ECO:0000313|EMBL:AAN65801.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
  protein_family: Large cell-surface adhesin secreted by a LapEBC type I secretion system.
  protein_domains: HemolysinCabind (PF00353); LapA (PF20579); VWA (PF00092)
notes: Automated Falcon output was requested, but the local CLI import path stalled before the wrapper could execute. The literature synthesis below was prepared manually in the standard falcon output path so the downstream review can cite it transparently.
---

## Identity check

The target protein is UniProt `Q88RG2`, a very large 8682 aa surface adhesion protein encoded by `PP_0168` in *Pseudomonas putida* KT2440. UniProt does not expose a `GN   Name=lapA` line for this entry, but the KT2440 biofilm literature consistently refers to `PP_0168` as `lapA`, the major large adhesin involved in attachment and biofilm development.

## Summary

LapA is a giant cell-surface adhesin of *Pseudomonas putida* KT2440 that promotes stable attachment and biofilm formation on abiotic surfaces. Direct KT2440 studies show that c-di-GMP and FleQ activate `lapA`-dependent biofilm formation, that LapE is required for efficient LapA secretion and cell-surface localization, and that nutrient limitation stimulates LapG-dependent release of LapA during dispersal. The protein also contains a vWFa domain and many calcium-binding RTX-like repeats, explaining why InterPro assigns a calcium ion binding annotation even though the biologically informative role is surface adhesion.

## Key evidence

- LapA is a giant cell-surface adhesin of *Pseudomonas putida* KT2440 that promotes stable attachment and biofilm formation on abiotic surfaces. Direct support comes from KT2440 biofilm studies showing that LapA is one of the two major adhesins used during attachment and mature biofilm development, and that loss of `lapA` strongly reduces biofilm formation. Sources: PMID 25253613, DOI https://doi.org/10.1099/mic.0.082503-0; PMID 35682576, DOI https://doi.org/10.3390/ijms23115898.
- Fis overexpression increases LapA abundance and shifts the LapA/LapF balance toward stronger mature biofilm formation in KT2440. Source: PMID 25253613, DOI https://doi.org/10.1099/mic.0.082503-0.
- FleQ and c-di-GMP activate `lapA` and `lapE` transcription, increasing LapA secretion and biofilm formation. Direct KT2440 evidence shows FleQ is required for c-di-GMP-dependent modulation of `lapA`, and later work identified `lapE` as a direct FleQ target that supports efficient adhesin secretion. Sources: PMID 27120564, DOI https://doi.org/10.1111/1758-2229.12419; PMID 33975969, DOI https://doi.org/10.1128/mSystems.00295-21.
- LapE is an outer membrane pore protein required for efficient LapA secretion, cell-surface localization, and biofilm formation. Source: PMID 33975969, DOI https://doi.org/10.1128/mSystems.00295-21.
- Nutrient starvation triggers LapG-dependent proteolysis and release of surface-associated LapA, and the stringent response further promotes dispersal by increasing `bifA` expression while reducing `lapA`, `lapBC`, and `lapE` transcription. Source: PMID 29273811, DOI https://doi.org/10.1038/s41598-017-18518-0.
- The vWFa domain of LapA is necessary for peptide-enhanced biofilm formation in *Pseudomonas putida*. Source: PMID 35682576, DOI https://doi.org/10.3390/ijms23115898.
- LapA carries numerous LapA repeats and hemolysin-type calcium-binding repeats, so the InterPro-derived calcium ion binding annotation is plausible but under-describes the protein's primary adhesin role. This inference is based on the UniProt domain architecture for Q88RG2 together with the KT2440 adhesion literature. Sources: UniProt Q88RG2 flatfile and the papers above.

## Functional interpretation for GO review

- The existing GOA term `GO:0005509 calcium ion binding` is mechanistically plausible because LapA contains repeated hemolysin-type calcium-binding motifs typical of RTX-like adhesins.
- The more informative core function is adhesin-mediated surface attachment during biofilm formation, best captured by `GO:0098631 cell adhesion mediator activity` together with biofilm process terms such as `GO:0043708 cell adhesion involved in biofilm formation` and `GO:0044011 single-species biofilm formation on inanimate substrate`.
- `cell surface` is the safest cellular component summary for the mature functional protein in KT2440 because LapA must be secreted and retained at the bacterial surface to support adhesion, while dispersal involves its LapG-dependent release.
